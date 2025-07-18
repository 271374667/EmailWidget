"""EmailWidget caching system

Provides image cache management functionality with LRU strategy and filesystem storage.
"""

import hashlib
import json
import time
from contextlib import suppress
from pathlib import Path
from typing import Any

from email_widget.core.logger import get_project_logger


class ImageCache:
    """LRU cache system for improving image processing performance.

    This cache manager uses the Least Recently Used (LRU) strategy to manage image data,
    supports storing images to the filesystem, and maintains an in-memory index for fast lookup.
    This significantly improves performance when embedding large amounts of images in emails by
    avoiding redundant downloading and processing.

    Core Features:
        - **LRU Strategy**: Automatically evicts least recently used cache items.
        - **Filesystem Storage**: Persists image data to local files, reducing memory usage.
        - **Memory Index**: Fast cache item lookup, improving access speed.
        - **Performance Monitoring**: Provides cache hit rate and size statistics.

    Attributes:
        _cache_dir (Path): Directory for storing cache files.
        _max_size (int): Maximum number of items allowed in cache.
        _cache_index (Dict[str, Dict[str, Any]]): In-memory cache index.

    Examples:
        ```python
        from email_widget.core.cache import get_image_cache

        cache = get_image_cache()

        # Store data
        # Assuming some_image_data is the binary content of an image, mime_type is the MIME type
        # cache.set("image_url_or_path_1", some_image_data, "image/png")

        # Get data
        # cached_data = cache.get("image_url_or_path_1")
        # if cached_data:
        #     image_bytes, mime = cached_data
        #     print(f"Retrieved image from cache, size: {len(image_bytes)} bytes, type: {mime}")

        # Clear cache
        # cache.clear()

        # Get cache statistics
        stats = cache.get_cache_stats()
        print(f"Cache items: {stats['total_items']}, total size: {stats['total_size_bytes']} bytes")
        ```
    """

    def __init__(self, cache_dir: Path | None = None, max_size: int = 100):
        """Initialize the cache manager.

        Args:
            cache_dir (Optional[Path]): Cache directory path, defaults to `emailwidget_cache` in system temp directory.
            max_size (int): Maximum number of items allowed in cache, defaults to 100.
        """
        self._logger = get_project_logger()
        self._max_size = max_size

        # Set cache directory
        if cache_dir is None:
            import tempfile

            cache_dir = Path(tempfile.gettempdir()) / "emailwidget_cache"

        self._cache_dir = Path(cache_dir)
        self._cache_dir.mkdir(parents=True, exist_ok=True)

        # Cache index file
        self._index_file = self._cache_dir / "cache_index.json"

        # In-memory cache index {cache_key: {"file_path": str, "access_time": float, "size": int}}
        self._cache_index: dict[str, dict[str, Any]] = {}

        # Load existing cache index
        self._load_cache_index()

        self._logger.debug(f"Image cache initialization complete, cache directory: {self._cache_dir}")

    def _load_cache_index(self) -> None:
        """Load cache index from file"""
        if self._index_file.exists():
            with suppress(Exception):
                with open(self._index_file, encoding="utf-8") as f:
                    self._cache_index = json.load(f)
                self._logger.debug(f"Loaded cache index, {len(self._cache_index)} items")

    def _save_cache_index(self) -> None:
        """Save cache index to file"""
        with suppress(Exception):
            with open(self._index_file, "w", encoding="utf-8") as f:
                json.dump(self._cache_index, f, ensure_ascii=False, indent=2)

    def _generate_cache_key(self, source: str) -> str:
        """Generate cache key

        Args:
            source: Image source (URL or file path)

        Returns:
            Cache key string
        """
        return hashlib.md5(source.encode("utf-8")).hexdigest()

    def _cleanup_old_cache(self) -> None:
        """Clean up expired cache items"""
        if len(self._cache_index) <= self._max_size:
            return

        # Sort by access time, delete least recently accessed items
        sorted_items = sorted(
            self._cache_index.items(), key=lambda x: x[1].get("access_time", 0)
        )

        # Delete items exceeding the limit
        items_to_remove = sorted_items[: len(self._cache_index) - self._max_size]

        for cache_key, cache_info in items_to_remove:
            self._remove_cache_item(cache_key, cache_info)

        self._logger.debug(f"Cleaned {len(items_to_remove)} expired cache items")

    def _remove_cache_item(self, cache_key: str, cache_info: dict[str, Any]) -> None:
        """Delete a single cache item

        Args:
            cache_key: Cache key
            cache_info: Cache information
        """
        # Delete file
        file_path = Path(cache_info.get("file_path", ""))
        if file_path.exists():
            with suppress(Exception):
                file_path.unlink()

        # Remove from index
        self._cache_index.pop(cache_key, None)

    def get(self, source: str) -> tuple[bytes, str] | None:
        """Get image data from cache.

        Args:
            source (str): Image source (URL or file path), used to generate cache key.

        Returns:
            Optional[Tuple[bytes, str]]: If cache found, returns (image binary data, MIME type) tuple;
                                         otherwise returns None.
        """
        cache_key = self._generate_cache_key(source)

        if cache_key not in self._cache_index:
            return None

        cache_info = self._cache_index[cache_key]
        file_path = Path(cache_info["file_path"])

        # Check if file exists
        if not file_path.exists():
            self._cache_index.pop(cache_key, None)
            self._logger.warning(f"Cache file does not exist: {file_path}")
            return None

        try:
            # Read file content
            with open(file_path, "rb") as f:
                data = f.read()

            # Get MIME type
            mime_type = cache_info.get("mime_type", "image/png")

            # Update access time
            cache_info["access_time"] = time.time()
            self._save_cache_index()

            self._logger.debug(f"Retrieved image from cache: {source[:50]}... ")
            return data, mime_type

        except Exception as e:
            self._logger.error(f"Failed to read cache file: {e}")
            self._remove_cache_item(cache_key, cache_info)
            return None

    def set(self, source: str, data: bytes, mime_type: str = "image/png") -> bool:
        """Store image data in cache.

        Args:
            source (str): Image source (URL or file path), used as cache key.
            data (bytes): Image binary data.
            mime_type (str): Image MIME type, defaults to "image/png".

        Returns:
            bool: Whether successfully stored in cache.
        """
        try:
            cache_key = self._generate_cache_key(source)

            # Generate cache file path
            ext = mime_type.split("/")[-1] if "/" in mime_type else "png"
            cache_file = self._cache_dir / f"{cache_key}.{ext}"

            # Write to file
            with open(cache_file, "wb") as f:
                f.write(data)

            # Update index
            self._cache_index[cache_key] = {
                "file_path": str(cache_file),
                "access_time": time.time(),
                "size": len(data),
                "mime_type": mime_type,
                "source": source[:100],  # Save first 100 characters of source for debugging
            }

            # Clean up expired cache
            self._cleanup_old_cache()

            # Save index
            self._save_cache_index()

            self._logger.debug(f"Successfully cached image: {source[:50]}... -> {cache_file.name}")
            return True

        except Exception as e:
            self._logger.error(f"Failed to cache image: {e}")
            return False

    def clear(self) -> None:
        """Clear all cache data.

        This method will delete all cache files and cache index.
        """
        try:
            # Delete all cache files
            for cache_info in self._cache_index.values():
                file_path = Path(cache_info.get("file_path", ""))
                if file_path.exists():
                    with suppress(Exception):
                        file_path.unlink()

            # Clear index
            self._cache_index.clear()

            # Delete index file
            if self._index_file.exists():
                self._index_file.unlink()

            self._logger.info("Cleared all image cache")

        except Exception as e:
            self._logger.error(f"Failed to clear cache: {e}")

    def get_cache_stats(self) -> dict[str, Any]:
        """Get cache statistics

        Returns:
            Cache statistics dictionary
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


# Global cache instance
_global_cache: ImageCache | None = None


def get_image_cache() -> ImageCache:
    """Get global image cache instance.

    This function implements singleton pattern, ensuring only one `ImageCache` instance exists
    throughout the entire application.

    Returns:
        ImageCache: Global unique `ImageCache` instance.

    Examples:
        ```python
        from email_widget.core.cache import get_image_cache

        cache1 = get_image_cache()
        cache2 = get_image_cache()
        assert cache1 is cache2 # True, both are the same instance
        ```
    """
    global _global_cache
    if _global_cache is None:
        _global_cache = ImageCache()
    return _global_cache
