"""ImageCache组件的完整测试套件。

测试覆盖：
- LRU缓存功能
- 文件系统存储
- 索引管理
- 缓存清理和大小控制
- 线程安全性
"""

import json
import tempfile
import time
from pathlib import Path
from unittest.mock import patch

import pytest

from email_widget.core.cache import ImageCache


class TestImageCacheInitialization:
    """ImageCache初始化测试"""

    def test_init_default(self):
        """测试默认初始化"""
        cache = ImageCache()
        assert cache._max_size == 100
        assert cache._cache_dir.name == "emailwidget_cache"
        assert cache._cache_index == {}

    def test_init_custom_params(self):
        """测试自定义参数初始化"""
        custom_dir = Path("/tmp/custom_cache")
        cache = ImageCache(cache_dir=custom_dir, max_size=50)
        assert cache._max_size == 50
        assert cache._cache_dir == custom_dir

    def test_init_with_pathlib_path(self):
        """测试使用pathlib.Path初始化"""
        custom_path = Path("/tmp/pathlib_cache")
        cache = ImageCache(cache_dir=custom_path)
        assert cache._cache_dir == custom_path

    @patch("pathlib.Path.mkdir")
    def test_cache_directory_creation(self, mock_mkdir):
        """测试缓存目录创建"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache_dir = Path(temp_dir) / "new_cache"
            cache = ImageCache(cache_dir=cache_dir)

            # 验证目录被创建
            mock_mkdir.assert_called()


class TestImageCacheIndexManagement:
    """ImageCache索引管理测试"""

    def test_load_cache_index_success(self):
        """测试成功加载索引"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache = ImageCache(cache_dir=temp_dir)

            # 创建测试索引文件
            index_data = {
                "test_key": {
                    "file_path": "test.png",
                    "access_time": time.time(),
                    "size": 1024,
                    "mime_type": "image/png",
                }
            }

            with open(cache._index_file, "w", encoding="utf-8") as f:
                json.dump(index_data, f)

            # 重新加载索引
            cache._load_cache_index()

            assert "test_key" in cache._cache_index
            assert cache._cache_index["test_key"]["file_path"] == "test.png"
            assert cache._cache_index["test_key"]["size"] == 1024

    def test_load_cache_index_file_not_exists(self):
        """测试索引文件不存在"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache = ImageCache(cache_dir=temp_dir)

            # 删除索引文件
            if cache._index_file.exists():
                cache._index_file.unlink()

            cache._load_cache_index()
            assert cache._cache_index == {}

    def test_load_cache_index_invalid_json(self):
        """测试无效JSON索引文件"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache = ImageCache(cache_dir=temp_dir)

            # 创建无效JSON文件
            with open(cache._index_file, "w", encoding="utf-8") as f:
                f.write("invalid json content")

            cache._load_cache_index()
            # 应该返回空索引而不抛出异常
            assert cache._cache_index == {}

    def test_save_cache_index_success(self):
        """测试成功保存索引"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache = ImageCache(cache_dir=temp_dir)
            cache._cache_index = {
                "test_key": {
                    "file_path": "test.png",
                    "access_time": time.time(),
                    "size": 1024,
                    "mime_type": "image/png",
                }
            }

            cache._save_cache_index()

            # 验证文件被创建并包含正确数据
            assert cache._index_file.exists()
            with open(cache._index_file, encoding="utf-8") as f:
                loaded_data = json.load(f)
            assert "test_key" in loaded_data

    def test_save_cache_index_error(self):
        """测试保存索引失败"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache = ImageCache(cache_dir=temp_dir)

            # 模拟写入错误
            with patch("builtins.open", side_effect=OSError("写入失败")):
                # 应该不抛出异常
                cache._save_cache_index()


class TestImageCacheOperations:
    """ImageCache操作测试"""

    def test_generate_cache_key(self):
        """测试生成缓存键"""
        cache = ImageCache()

        key1 = cache._generate_cache_key("http://example.com/image.png")
        key2 = cache._generate_cache_key("http://example.com/image.png")
        key3 = cache._generate_cache_key("http://example.com/other.png")

        # 相同源应该生成相同键
        assert key1 == key2
        # 不同源应该生成不同键
        assert key1 != key3
        assert isinstance(key1, str)
        assert len(key1) == 32  # MD5哈希长度

    def test_set_and_get_success(self):
        """测试成功设置和获取缓存"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache = ImageCache(cache_dir=temp_dir)
            source = "http://example.com/test.png"
            data = b"test_image_data"
            mime_type = "image/png"

            # 设置缓存
            result = cache.set(source, data, mime_type)
            assert result is True

            # 获取缓存
            retrieved = cache.get(source)
            assert retrieved is not None
            retrieved_data, retrieved_mime = retrieved
            assert retrieved_data == data
            assert retrieved_mime == mime_type

    def test_get_cache_miss(self):
        """测试缓存未命中"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache = ImageCache(cache_dir=temp_dir)

            result = cache.get("nonexistent_source")
            assert result is None

    def test_get_file_not_exists(self):
        """测试缓存索引存在但文件不存在"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache = ImageCache(cache_dir=temp_dir)

            # 手动创建索引但不创建文件
            cache_key = cache._generate_cache_key("test_source")
            cache._cache_index[cache_key] = {
                "file_path": str(cache._cache_dir / "missing.png"),
                "access_time": time.time(),
                "size": 1024,
                "mime_type": "image/png",
            }

            result = cache.get("test_source")
            assert result is None
            # 索引应该被清理
            assert cache_key not in cache._cache_index

    def test_set_file_write_error(self):
        """测试文件写入错误"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache = ImageCache(cache_dir=temp_dir)

            with patch("builtins.open", side_effect=OSError("写入失败")):
                result = cache.set("test_source", b"test_data", "image/png")
                assert result is False

    def test_get_file_read_error(self):
        """测试文件读取错误"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache = ImageCache(cache_dir=temp_dir)

            # 先成功设置缓存
            cache.set("test_source", b"test_data", "image/png")

            # 模拟读取错误
            with patch("builtins.open", side_effect=OSError("读取失败")):
                result = cache.get("test_source")
                assert result is None


class TestImageCacheLRUEviction:
    """ImageCache LRU淘汰测试"""

    def test_cleanup_old_cache(self):
        """测试清理过期缓存"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache = ImageCache(cache_dir=temp_dir, max_size=2)

            # 添加项目直到超过限制
            cache.set("source1", b"data1", "image/png")
            cache.set("source2", b"data2", "image/png")
            cache.set("source3", b"data3", "image/png")

            # 第三个项目应该触发清理
            assert len(cache._cache_index) <= 2

    def test_lru_order_preservation(self):
        """测试LRU顺序保持"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache = ImageCache(cache_dir=temp_dir, max_size=3)

            # 添加项目
            cache.set("source1", b"data1", "image/png")
            time.sleep(0.01)  # 确保时间戳不同
            cache.set("source2", b"data2", "image/png")
            time.sleep(0.01)
            cache.set("source3", b"data3", "image/png")

            # 访问第一个项目（更新访问时间）
            cache.get("source1")
            time.sleep(0.01)

            # 添加第四个项目，应该淘汰source2（最久未访问）
            cache.set("source4", b"data4", "image/png")

            # source1和source3应该仍然存在
            assert cache.get("source1") is not None
            assert cache.get("source3") is not None
            assert cache.get("source4") is not None

    def test_remove_cache_item(self):
        """测试移除缓存项"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache = ImageCache(cache_dir=temp_dir)

            # 设置缓存
            source = "test_source"
            cache.set(source, b"test_data", "image/png")

            # 获取缓存信息
            cache_key = cache._generate_cache_key(source)
            cache_info = cache._cache_index[cache_key]

            # 移除缓存项
            cache._remove_cache_item(cache_key, cache_info)

            # 验证项目被移除
            assert cache_key not in cache._cache_index
            # 文件应该不存在
            file_path = Path(cache_info["file_path"])
            assert not file_path.exists()


class TestImageCacheClearOperation:
    """ImageCache清理操作测试"""

    def test_clear_success(self):
        """测试成功清理缓存"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache = ImageCache(cache_dir=temp_dir)

            # 添加一些缓存项
            cache.set("source1", b"data1", "image/png")
            cache.set("source2", b"data2", "image/png")

            # 清理缓存
            cache.clear()

            # 验证缓存被清空
            assert len(cache._cache_index) == 0
            assert cache.get("source1") is None
            assert cache.get("source2") is None

    def test_clear_with_file_errors(self):
        """测试清理时文件删除错误"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache = ImageCache(cache_dir=temp_dir)

            # 添加缓存项
            cache.set("source1", b"data1", "image/png")

            # 模拟文件删除错误
            with patch("pathlib.Path.unlink", side_effect=OSError("删除失败")):
                # 应该不抛出异常
                cache.clear()

            # 索引应该被清空
            assert len(cache._cache_index) == 0


class TestImageCacheUtilityMethods:
    """ImageCache工具方法测试"""

    def test_get_cache_stats_empty(self):
        """测试空缓存统计"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache = ImageCache(cache_dir=temp_dir)

            stats = cache.get_cache_stats()

            assert stats["total_items"] == 0
            assert stats["total_size_bytes"] == 0
            assert stats["cache_dir"] == str(cache._cache_dir)
            assert stats["max_size"] == cache._max_size

    def test_get_cache_stats_with_data(self):
        """测试包含数据的缓存统计"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache = ImageCache(cache_dir=temp_dir)

            # 添加一些缓存项
            cache.set("source1", b"data1" * 100, "image/png")  # 500字节
            cache.set("source2", b"data2" * 200, "image/png")  # 1000字节

            stats = cache.get_cache_stats()

            assert stats["total_items"] == 2
            assert stats["total_size_bytes"] == 1500
            assert stats["cache_dir"] == str(cache._cache_dir)
            assert stats["max_size"] == cache._max_size


class TestImageCacheThreadSafety:
    """ImageCache线程安全测试"""

    def test_concurrent_operations_simulation(self):
        """测试并发操作模拟"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache = ImageCache(cache_dir=temp_dir)

            # 模拟并发设置和获取
            sources = [f"source_{i}" for i in range(10)]
            data_items = [f"data_{i}".encode() for i in range(10)]

            # 设置所有项目
            for source, data in zip(sources, data_items, strict=False):
                cache.set(source, data, "image/png")

            # 获取所有项目
            results = []
            for source in sources:
                result = cache.get(source)
                results.append(result)

            # 验证所有项目都能正确获取
            assert len([r for r in results if r is not None]) == len(sources)

    def test_index_consistency_after_operations(self):
        """测试操作后索引一致性"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache = ImageCache(cache_dir=temp_dir)

            # 执行多种操作
            cache.set("source1", b"data1", "image/png")
            cache.set("source2", b"data2", "image/png")
            cache.get("source1")  # 访问
            cache.set("source3", b"data3", "image/png")

            # 验证索引一致性
            for cache_key, cache_info in cache._cache_index.items():
                file_path = Path(cache_info["file_path"])
                assert file_path.exists(), f"文件不存在: {file_path}"
                assert cache_info["size"] > 0
                assert "mime_type" in cache_info


class TestImageCacheErrorHandling:
    """ImageCache错误处理测试"""

    def test_set_none_data(self):
        """测试设置None数据"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache = ImageCache(cache_dir=temp_dir)

            # 应该处理None数据，返回False而不崩溃
            result = cache.set("test_source", None, "image/png")
            assert result is False

    def test_set_empty_data(self):
        """测试设置空数据"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache = ImageCache(cache_dir=temp_dir)

            result = cache.set("test_source", b"", "image/png")
            assert result is True

            retrieved = cache.get("test_source")
            assert retrieved is not None
            data, mime = retrieved
            assert data == b""

    def test_get_none_source(self):
        """测试获取None源"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache = ImageCache(cache_dir=temp_dir)

            # 应该处理None源，抛出AttributeError
            with pytest.raises(AttributeError):
                cache.get(None)

    def test_get_empty_source(self):
        """测试获取空源"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache = ImageCache(cache_dir=temp_dir)

            result = cache.get("")
            assert result is None


class TestImageCacheIntegration:
    """ImageCache集成测试"""

    def test_full_lifecycle(self):
        """测试完整生命周期"""
        with tempfile.TemporaryDirectory() as temp_dir:
            # 创建缓存
            cache = ImageCache(cache_dir=temp_dir, max_size=3)

            # 添加项目
            test_data = [
                ("http://example.com/image1.png", b"image1_data", "image/png"),
                ("http://example.com/image2.jpg", b"image2_data", "image/jpeg"),
                ("http://example.com/image3.gif", b"image3_data", "image/gif"),
            ]

            # 设置缓存
            for source, data, mime in test_data:
                result = cache.set(source, data, mime)
                assert result is True

            # 获取缓存
            for source, expected_data, expected_mime in test_data:
                result = cache.get(source)
                assert result is not None
                data, mime = result
                assert data == expected_data
                assert mime == expected_mime

            # 获取统计信息
            stats = cache.get_cache_stats()
            assert stats["total_items"] == 3

            # 清理缓存
            cache.clear()
            stats_after_clear = cache.get_cache_stats()
            assert stats_after_clear["total_items"] == 0

    def test_persistence_simulation(self):
        """测试持久化模拟"""
        with tempfile.TemporaryDirectory() as temp_dir:
            # 第一个缓存实例
            cache1 = ImageCache(cache_dir=temp_dir)
            cache1.set("persistent_source", b"persistent_data", "image/png")

            # 第二个缓存实例（模拟重启）
            cache2 = ImageCache(cache_dir=temp_dir)

            # 应该能够从索引加载数据
            result = cache2.get("persistent_source")
            assert result is not None
            data, mime = result
            assert data == b"persistent_data"
            assert mime == "image/png"

    def test_large_data_handling(self):
        """测试大数据处理"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache = ImageCache(cache_dir=temp_dir)

            # 创建大数据（1MB）
            large_data = b"x" * (1024 * 1024)

            result = cache.set("large_source", large_data, "image/png")
            assert result is True

            retrieved = cache.get("large_source")
            assert retrieved is not None
            data, mime = retrieved
            assert len(data) == 1024 * 1024
            assert mime == "image/png"

    def test_many_items_performance(self):
        """测试大量项目性能"""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache = ImageCache(cache_dir=temp_dir, max_size=1000)

            # 添加大量项目
            num_items = 100
            sources = [f"source_{i}" for i in range(num_items)]

            # 设置项目
            for i, source in enumerate(sources):
                data = f"data_{i}".encode()
                cache.set(source, data, "image/png")

            # 随机访问项目
            import random

            random.shuffle(sources)

            for source in sources[:50]:  # 访问一半
                result = cache.get(source)
                assert result is not None

            # 验证缓存仍然正常工作
            stats = cache.get_cache_stats()
            assert stats["total_items"] <= 1000
