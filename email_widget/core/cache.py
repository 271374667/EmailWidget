"""EmailWidget缓存系统

提供图片缓存管理功能，支持LRU策略和文件系统存储.
"""

import hashlib
import json
import time
from contextlib import suppress
from pathlib import Path
from typing import Any

from email_widget.core.logger import get_project_logger


class ImageCache:
    """LRU 缓存系统，用于提升图片处理性能.

    该缓存管理器使用最近最少使用（LRU）策略来管理图片数据，
    支持将图片存储到文件系统，并维护内存中的索引以实现快速查找.
    这对于在邮件中嵌入大量图片时，避免重复下载和处理，从而显著提升性能.

    核心功能:
        - **LRU 策略**: 自动淘汰最久未使用的缓存项.
        - **文件系统存储**: 将图片数据持久化到本地文件，减少内存占用.
        - **内存索引**: 快速查找缓存项，提高访问速度.
        - **性能监控**: 提供缓存命中率和大小统计.

    Attributes:
        _cache_dir (Path): 缓存文件存储的目录.
        _max_size (int): 缓存中允许的最大项目数量.
        _cache_index (Dict[str, Dict[str, Any]): 内存中的缓存索引.

    Examples:
        ```python
        from email_widget.core.cache import get_image_cache

        cache = get_image_cache()

        # 存储数据
        # 假设 some_image_data 是图片的二进制内容，mime_type 是图片的MIME类型
        # cache.set("image_url_or_path_1", some_image_data, "image/png")

        # 获取数据
        # cached_data = cache.get("image_url_or_path_1")
        # if cached_data:
        #     image_bytes, mime = cached_data
        #     print(f"从缓存获取图片，大小: {len(image_bytes)} 字节, 类型: {mime}")

        # 清空缓存
        # cache.clear()

        # 获取缓存统计信息
        stats = cache.get_cache_stats()
        print(f"缓存项目数量: {stats['total_items']}, 总大小: {stats['total_size_bytes']} 字节")
        ```
    """

    def __init__(self, cache_dir: Path | None = None, max_size: int = 100):
        """初始化缓存管理器.

        Args:
            cache_dir (Optional[Path]): 缓存目录路径，默认为系统临时目录下的 `emailwidget_cache`.
            max_size (int): 缓存中允许的最大项目数量，默认为100.
        """
        self._logger = get_project_logger()
        self._max_size = max_size

        # 设置缓存目录
        if cache_dir is None:
            import tempfile

            cache_dir = Path(tempfile.gettempdir()) / "emailwidget_cache"

        self._cache_dir = Path(cache_dir)
        self._cache_dir.mkdir(parents=True, exist_ok=True)

        # 缓存索引文件
        self._index_file = self._cache_dir / "cache_index.json"

        # 内存中的缓存索引 {cache_key: {"file_path": str, "access_time": float, "size": int}}
        self._cache_index: dict[str, dict[str, Any]] = {}

        # 加载现有缓存索引
        self._load_cache_index()

        self._logger.debug(f"图片缓存初始化完成，缓存目录: {self._cache_dir}")

    def _load_cache_index(self) -> None:
        """从文件加载缓存索引"""
        if self._index_file.exists():
            with suppress(Exception):
                with open(self._index_file, encoding="utf-8") as f:
                    self._cache_index = json.load(f)
                self._logger.debug(f"加载缓存索引，共 {len(self._cache_index)} 项")

    def _save_cache_index(self) -> None:
        """保存缓存索引到文件"""
        with suppress(Exception):
            with open(self._index_file, "w", encoding="utf-8") as f:
                json.dump(self._cache_index, f, ensure_ascii=False, indent=2)

    def _generate_cache_key(self, source: str) -> str:
        """生成缓存键

        Args:
            source: 图片源（URL或文件路径）

        Returns:
            缓存键字符串
        """
        return hashlib.md5(source.encode("utf-8")).hexdigest()

    def _cleanup_old_cache(self) -> None:
        """清理过期的缓存项"""
        if len(self._cache_index) <= self._max_size:
            return

        # 按访问时间排序，删除最久未访问的项目
        sorted_items = sorted(
            self._cache_index.items(), key=lambda x: x[1].get("access_time", 0)
        )

        # 删除超出限制的项目
        items_to_remove = sorted_items[: len(self._cache_index) - self._max_size]

        for cache_key, cache_info in items_to_remove:
            self._remove_cache_item(cache_key, cache_info)

        self._logger.debug(f"清理了 {len(items_to_remove)} 个过期缓存项")

    def _remove_cache_item(self, cache_key: str, cache_info: dict[str, Any]) -> None:
        """删除单个缓存项

        Args:
            cache_key: 缓存键
            cache_info: 缓存信息
        """
        # 删除文件
        file_path = Path(cache_info.get("file_path", ""))
        if file_path.exists():
            with suppress(Exception):
                file_path.unlink()

        # 从索引中删除
        self._cache_index.pop(cache_key, None)

    def get(self, source: str) -> tuple[bytes, str] | None:
        """从缓存中获取图片数据.

        Args:
            source (str): 图片源（URL或文件路径），用于生成缓存键.

        Returns:
            Optional[Tuple[bytes, str]]: 如果找到缓存，返回 (图片二进制数据, MIME类型) 的元组；
                                         否则返回None.
        """
        cache_key = self._generate_cache_key(source)

        if cache_key not in self._cache_index:
            return None

        cache_info = self._cache_index[cache_key]
        file_path = Path(cache_info["file_path"])

        # 检查文件是否存在
        if not file_path.exists():
            self._cache_index.pop(cache_key, None)
            self._logger.warning(f"缓存文件不存在: {file_path}")
            return None

        try:
            # 读取文件内容
            with open(file_path, "rb") as f:
                data = f.read()

            # 获取MIME类型
            mime_type = cache_info.get("mime_type", "image/png")

            # 更新访问时间
            cache_info["access_time"] = time.time()
            self._save_cache_index()

            self._logger.debug(f"从缓存获取图片: {source[:50]}... ")
            return data, mime_type

        except Exception as e:
            self._logger.error(f"读取缓存文件失败: {e}")
            self._remove_cache_item(cache_key, cache_info)
            return None

    def set(self, source: str, data: bytes, mime_type: str = "image/png") -> bool:
        """向缓存中存储图片数据.

        Args:
            source (str): 图片源（URL或文件路径），作为缓存的键.
            data (bytes): 图片的二进制数据.
            mime_type (str): 图片的MIME类型，默认为 "image/png".

        Returns:
            bool: 是否成功存储到缓存.
        """
        try:
            cache_key = self._generate_cache_key(source)

            # 生成缓存文件路径
            ext = mime_type.split("/")[-1] if "/" in mime_type else "png"
            cache_file = self._cache_dir / f"{cache_key}.{ext}"

            # 写入文件
            with open(cache_file, "wb") as f:
                f.write(data)

            # 更新索引
            self._cache_index[cache_key] = {
                "file_path": str(cache_file),
                "access_time": time.time(),
                "size": len(data),
                "mime_type": mime_type,
                "source": source[:100],  # 保存源的前100个字符用于调试
            }

            # 清理过期缓存
            self._cleanup_old_cache()

            # 保存索引
            self._save_cache_index()

            self._logger.debug(f"缓存图片成功: {source[:50]}... -> {cache_file.name}")
            return True

        except Exception as e:
            self._logger.error(f"缓存图片失败: {e}")
            return False

    def clear(self) -> None:
        """清空所有缓存数据.

        此方法会删除所有缓存文件和缓存索引.
        """
        try:
            # 删除所有缓存文件
            for cache_info in self._cache_index.values():
                file_path = Path(cache_info.get("file_path", ""))
                if file_path.exists():
                    with suppress(Exception):
                        file_path.unlink()

            # 清空索引
            self._cache_index.clear()

            # 删除索引文件
            if self._index_file.exists():
                self._index_file.unlink()

            self._logger.info("清空所有图片缓存")

        except Exception as e:
            self._logger.error(f"清空缓存失败: {e}")

    def get_cache_stats(self) -> dict[str, Any]:
        """获取缓存统计信息

        Returns:
            缓存统计信息字典
        """
        total_size = sum(info.get("size", 0) for info in self._cache_index.values())

        return {
            "total_items": len(self._cache_index),
            "max_size": self._max_size,
            "total_size_bytes": total_size,
            "cache_dir": str(self._cache_dir),
            "cache_usage_ratio": len(self._cache_index) / self._max_size
            if self._max_size > 0
            else 0,
        }


# 全局缓存实例
_global_cache: ImageCache | None = None


def get_image_cache() -> ImageCache:
    """获取全局图片缓存实例.

    此函数实现了单例模式，确保在整个应用程序中只存在一个 `ImageCache` 实例.

    Returns:
        ImageCache: 全局唯一的 `ImageCache` 实例.

    Examples:
        ```python
        from email_widget.core.cache import get_image_cache

        cache1 = get_image_cache()
        cache2 = get_image_cache()
        assert cache1 is cache2 # True，两者是同一个实例
        ```
    """
    global _global_cache
    if _global_cache is None:
        _global_cache = ImageCache()
    return _global_cache
