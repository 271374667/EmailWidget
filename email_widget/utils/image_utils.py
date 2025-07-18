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
        """Unified image source processing, returns base64 data URI or original URL

        Args:
            source: Image source (URL, file path or Path object)
            cache: Whether to use cache
            embed: Whether to embed image (True: convert to base64, False: return original URL)

        Returns:
            base64 format data URI or original URL, returns None on failure
        """
        logger = get_project_logger()

        try:
            source_str = str(source)

            # If not embedding and is network URL, return original URL directly
            if (
                not embed
                and isinstance(source, str)
                and source.startswith(("http://", "https://"))
            ):
                return source_str

            # Determine if it's a local file
            is_local_file = isinstance(source, Path) or (
                isinstance(source, str)
                and not source.startswith(("http://", "https://", "data:"))
            )

            # If not embedding and is local file, warn user but still embed
            if not embed and is_local_file:
                logger.warning(
                    f"Local image file cannot be accessed via link, will force embed: {source_str}"
                )
                # Continue with embedding logic

            # Only get cache manager when needed
            cache_manager = None
            if cache and (embed or is_local_file):
                cache_manager = get_image_cache()

            # Check cache (used in embed mode or forced embed for local files)
            if cache_manager:
                cached_result = cache_manager.get(source_str)
                if cached_result:
                    # Data retrieved from cache needs to be converted to base64 again
                    cached_data, cached_mime_type = cached_result
                    return ImageUtils.base64_img(cached_data, cached_mime_type)

            # Get image data
            img_data, mime_type = None, None

            if isinstance(source, Path) or (
                isinstance(source, str)
                and not source.startswith(("http://", "https://", "data:"))
            ):
                # Local file
                file_path = Path(source)
                if file_path.exists():
                    with open(file_path, "rb") as f:
                        img_data = f.read()
                    mime_type = ImageUtils._get_mime_type(file_path.suffix)
                else:
                    logger.error(f"Image file does not exist: {file_path}")
                    return None
            elif isinstance(source, str) and source.startswith("data:"):
                # Already in base64 format
                return source
            elif isinstance(source, str) and source.startswith(("http://", "https://")):
                # Network URL, download if embedding is needed
                if embed:
                    result = ImageUtils.request_url(source)
                    if result:
                        img_data, mime_type = result
                    else:
                        return None
                else:
                    # Don't embed, return URL directly (this branch is actually handled above)
                    return source_str
            else:
                logger.error(f"Unsupported image source format: {source}")
                return None

            if not img_data:
                return None

            # Basic validation of image data
            if not img_data or len(img_data) < 10:
                logger.error(f"Invalid image data: {source}")
                return None

            # Cache image data (in embed mode or forced embed for local files)
            if cache_manager and (embed or is_local_file):
                cache_manager.set(source_str, img_data, mime_type)

            # Convert to base64
            return ImageUtils.base64_img(img_data, mime_type)

        except Exception as e:
            logger.error(f"Failed to process image source: {e}")
            return None

    @staticmethod
    def request_url(url: str, timeout: int = 10) -> tuple[bytes, str] | None:
        """Request network URL to get image data

        Args:
            url: Image URL
            timeout: Timeout duration (seconds)

        Returns:
            tuple: (image data, MIME type) or None (on failure)
        """
        try:
            with urllib.request.urlopen(url, timeout=timeout) as response:
                if response.status == 200:
                    img_data = response.read()
                    content_type = response.headers.get("content-type", "image/png")
                    return img_data, content_type
                else:
                    get_project_logger().error(
                        f"Failed to download image, status code: {response.status}"
                    )
                    return None
        except urllib.error.URLError as e:
            get_project_logger().error(f"Network request failed: {e}")
            return None
        except Exception as e:
            get_project_logger().error(f"Error occurred while requesting image: {e}")
            return None

    @staticmethod
    def base64_img(img_data: bytes, mime_type: str = "image/png") -> str:
        """Convert image data to base64 format data URI

        Args:
            img_data: Image binary data
            mime_type: MIME type

        Returns:
            str: base64 format data URI
        """
        try:
            img_base64 = base64.b64encode(img_data).decode("utf-8")
            return f"data:{mime_type};base64,{img_base64}"
        except Exception as e:
            get_project_logger().error(f"Failed to convert to base64: {e}")
            return ""

    @staticmethod
    def _get_mime_type(ext: str) -> str:
        """Get MIME type based on file extension"""
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
