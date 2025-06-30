"""EmailWidget缓存系统

提供图片缓存管理功能，支持LRU策略和文件系统存储。
"""
import hashlib
import json
import time
from pathlib import Path
from typing import Optional, Dict, Any, Tuple
from contextlib import suppress

from email_widget.core.logger import get_project_logger


class ImageCache:
    """图片缓存管理器
    
    使用LRU策略管理图片缓存，支持文件系统存储和内存索引。
    """
    
    def __init__(self, cache_dir: Optional[Path] = None, max_size: int = 100):
        """初始化缓存管理器
        
        Args:
            cache_dir: 缓存目录路径，默认为系统临时目录下的emailwidget_cache
            max_size: 最大缓存项目数量
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
        self._cache_index: Dict[str, Dict[str, Any]] = {}
        
        # 加载现有缓存索引
        self._load_cache_index()
        
        self._logger.debug(f"图片缓存初始化完成，缓存目录: {self._cache_dir}")
    
    def _load_cache_index(self) -> None:
        """从文件加载缓存索引"""
        if self._index_file.exists():
            with suppress(Exception):
                with open(self._index_file, 'r', encoding='utf-8') as f:
                    self._cache_index = json.load(f)
                self._logger.debug(f"加载缓存索引，共 {len(self._cache_index)} 项")
    
    def _save_cache_index(self) -> None:
        """保存缓存索引到文件"""
        with suppress(Exception):
            with open(self._index_file, 'w', encoding='utf-8') as f:
                json.dump(self._cache_index, f, ensure_ascii=False, indent=2)
    
    def _generate_cache_key(self, source: str) -> str:
        """生成缓存键
        
        Args:
            source: 图片源（URL或文件路径）
            
        Returns:
            缓存键字符串
        """
        return hashlib.md5(source.encode('utf-8')).hexdigest()
    
    def _cleanup_old_cache(self) -> None:
        """清理过期的缓存项"""
        if len(self._cache_index) <= self._max_size:
            return
        
        # 按访问时间排序，删除最久未访问的项目
        sorted_items = sorted(
            self._cache_index.items(),
            key=lambda x: x[1].get('access_time', 0)
        )
        
        # 删除超出限制的项目
        items_to_remove = sorted_items[:len(self._cache_index) - self._max_size]
        
        for cache_key, cache_info in items_to_remove:
            self._remove_cache_item(cache_key, cache_info)
        
        self._logger.debug(f"清理了 {len(items_to_remove)} 个过期缓存项")
    
    def _remove_cache_item(self, cache_key: str, cache_info: Dict[str, Any]) -> None:
        """删除单个缓存项
        
        Args:
            cache_key: 缓存键
            cache_info: 缓存信息
        """
        # 删除文件
        file_path = Path(cache_info.get('file_path', ''))
        if file_path.exists():
            with suppress(Exception):
                file_path.unlink()
        
        # 从索引中删除
        self._cache_index.pop(cache_key, None)
    
    def get(self, source: str) -> Optional[Tuple[bytes, str]]:
        """获取缓存的图片数据
        
        Args:
            source: 图片源（URL或文件路径）
            
        Returns:
            tuple: (图片二进制数据, MIME类型) 或 None（如果不存在）
        """
        cache_key = self._generate_cache_key(source)
        
        if cache_key not in self._cache_index:
            return None
        
        cache_info = self._cache_index[cache_key]
        file_path = Path(cache_info['file_path'])
        
        # 检查文件是否存在
        if not file_path.exists():
            self._cache_index.pop(cache_key, None)
            self._logger.warning(f"缓存文件不存在: {file_path}")
            return None
        
        try:
            # 读取文件内容
            with open(file_path, 'rb') as f:
                data = f.read()
            
            # 获取MIME类型
            mime_type = cache_info.get('mime_type', 'image/png')
            
            # 更新访问时间
            cache_info['access_time'] = time.time()
            self._save_cache_index()
            
            self._logger.debug(f"从缓存获取图片: {source[:50]}...")
            return data, mime_type
            
        except Exception as e:
            self._logger.error(f"读取缓存文件失败: {e}")
            self._remove_cache_item(cache_key, cache_info)
            return None
    
    def set(self, source: str, data: bytes, mime_type: str = "image/png") -> bool:
        """设置缓存的图片数据
        
        Args:
            source: 图片源（URL或文件路径）
            data: 图片二进制数据
            mime_type: MIME类型
            
        Returns:
            是否设置成功
        """
        try:
            cache_key = self._generate_cache_key(source)
            
            # 生成缓存文件路径
            ext = mime_type.split('/')[-1] if '/' in mime_type else 'png'
            cache_file = self._cache_dir / f"{cache_key}.{ext}"
            
            # 写入文件
            with open(cache_file, 'wb') as f:
                f.write(data)
            
            # 更新索引
            self._cache_index[cache_key] = {
                'file_path': str(cache_file),
                'access_time': time.time(),
                'size': len(data),
                'mime_type': mime_type,
                'source': source[:100]  # 保存源的前100个字符用于调试
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
        """清空所有缓存"""
        try:
            # 删除所有缓存文件
            for cache_info in self._cache_index.values():
                file_path = Path(cache_info.get('file_path', ''))
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
    
    def get_cache_stats(self) -> Dict[str, Any]:
        """获取缓存统计信息
        
        Returns:
            缓存统计信息字典
        """
        total_size = sum(info.get('size', 0) for info in self._cache_index.values())
        
        return {
            'total_items': len(self._cache_index),
            'max_size': self._max_size,
            'total_size_bytes': total_size,
            'cache_dir': str(self._cache_dir),
            'cache_usage_ratio': len(self._cache_index) / self._max_size if self._max_size > 0 else 0
        }


# 全局缓存实例
_global_cache: Optional[ImageCache] = None


def get_image_cache() -> ImageCache:
    """获取全局图片缓存实例
    
    Returns:
        ImageCache实例
    """
    global _global_cache
    if _global_cache is None:
        _global_cache = ImageCache()
    return _global_cache 