import base64
import urllib.error
import urllib.request
from pathlib import Path

from email_widget.core.cache import get_image_cache
from email_widget.core.logger import get_project_logger


class ImageUtils:
    @staticmethod
    def process_image_source(
        source: str | Path, cache: bool = True, embed: bool = True
    ) -> str | None:
        """统一处理图片源，返回base64 data URI或原始URL

        Args:
            source: 图片源（URL、文件路径或Path对象）
            cache: 是否使用缓存
            embed: 是否嵌入图片（True: 转换为base64, False: 返回原始URL）

        Returns:
            base64格式的data URI或原始URL，失败时返回None
        """
        logger = get_project_logger()

        try:
            source_str = str(source)

            # 如果不嵌入且是网络URL，直接返回原始URL
            if (
                not embed
                and isinstance(source, str)
                and source.startswith(("http://", "https://"))
            ):
                return source_str

            # 确定是否是本地文件
            is_local_file = isinstance(source, Path) or (
                isinstance(source, str)
                and not source.startswith(("http://", "https://", "data:"))
            )

            # 如果不嵌入且是本地文件，警告用户但仍然嵌入
            if not embed and is_local_file:
                logger.warning(
                    f"本地图片文件无法通过链接访问，将强制嵌入: {source_str}"
                )
                # 继续执行嵌入逻辑

            # 只有在需要时才获取缓存管理器
            cache_manager = None
            if cache and (embed or is_local_file):
                cache_manager = get_image_cache()

            # 检查缓存（嵌入模式或本地文件强制嵌入时使用）
            if cache_manager:
                cached_result = cache_manager.get(source_str)
                if cached_result:
                    # 从缓存获取的数据需要重新转换为base64
                    cached_data, cached_mime_type = cached_result
                    return ImageUtils.base64_img(cached_data, cached_mime_type)

            # 获取图片数据
            img_data, mime_type = None, None

            if isinstance(source, Path) or (
                isinstance(source, str)
                and not source.startswith(("http://", "https://", "data:"))
            ):
                # 本地文件
                file_path = Path(source)
                if file_path.exists():
                    with open(file_path, "rb") as f:
                        img_data = f.read()
                    mime_type = ImageUtils._get_mime_type(file_path.suffix)
                else:
                    logger.error(f"图片文件不存在: {file_path}")
                    return None
            elif isinstance(source, str) and source.startswith("data:"):
                # 已经是base64格式
                return source
            elif isinstance(source, str) and source.startswith(("http://", "https://")):
                # 网络URL，如果需要嵌入则下载
                if embed:
                    result = ImageUtils.request_url(source)
                    if result:
                        img_data, mime_type = result
                    else:
                        return None
                else:
                    # 不嵌入，直接返回URL（这个分支实际上在上面已经处理了）
                    return source_str
            else:
                logger.error(f"不支持的图片源格式: {source}")
                return None

            if not img_data:
                return None

            # 基本验证图片数据
            if not img_data or len(img_data) < 10:
                logger.error(f"无效的图片数据: {source}")
                return None

            # 缓存图片数据（嵌入模式或本地文件强制嵌入时）
            if cache_manager and (embed or is_local_file):
                cache_manager.set(source_str, img_data, mime_type)

            # 转换为base64
            return ImageUtils.base64_img(img_data, mime_type)

        except Exception as e:
            logger.error(f"处理图片源失败: {e}")
            return None

    @staticmethod
    def request_url(url: str, timeout: int = 10) -> tuple[bytes, str] | None:
        """请求网络URL获取图片数据

        Args:
            url: 图片URL
            timeout: 超时时间（秒）

        Returns:
            tuple: (图片数据, MIME类型) 或 None（失败时）
        """
        try:
            with urllib.request.urlopen(url, timeout=timeout) as response:
                if response.status == 200:
                    img_data = response.read()
                    content_type = response.headers.get("content-type", "image/png")
                    return img_data, content_type
                else:
                    get_project_logger().error(
                        f"下载图片失败，状态码: {response.status}"
                    )
                    return None
        except urllib.error.URLError as e:
            get_project_logger().error(f"网络请求失败: {e}")
            return None
        except Exception as e:
            get_project_logger().error(f"请求图片时发生错误: {e}")
            return None

    @staticmethod
    def base64_img(img_data: bytes, mime_type: str = "image/png") -> str:
        """将图片数据转换为base64格式的data URI

        Args:
            img_data: 图片二进制数据
            mime_type: MIME类型

        Returns:
            str: base64格式的data URI
        """
        try:
            img_base64 = base64.b64encode(img_data).decode("utf-8")
            return f"data:{mime_type};base64,{img_base64}"
        except Exception as e:
            get_project_logger().error(f"转换base64失败: {e}")
            return ""

    @staticmethod
    def _get_mime_type(ext: str) -> str:
        """根据文件扩展名获取MIME类型"""
        mime_types = {
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".gif": "image/gif",
            ".bmp": "image/bmp",
            ".webp": "image/webp",
            ".svg": "image/svg+xml",
        }
        return mime_types.get(ext.lower(), "image/png")
