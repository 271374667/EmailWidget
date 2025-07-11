"""ImageUtils测试用例"""

import base64
import urllib.error
from pathlib import Path
from unittest.mock import MagicMock, mock_open, patch

import pytest

from email_widget.utils.image_utils import ImageUtils


class TestImageUtils:
    """ImageUtils测试类"""

    def setup_method(self):
        """每个测试方法执行前的设置"""
        # 清理缓存
        from email_widget.core.cache import get_image_cache

        cache = get_image_cache()
        cache.clear()

    def test_base64_img(self):
        """测试base64转换功能"""
        test_data = b"test image data"
        mime_type = "image/png"

        result = ImageUtils.base64_img(test_data, mime_type)

        expected_b64 = base64.b64encode(test_data).decode("utf-8")
        expected_result = f"data:{mime_type};base64,{expected_b64}"

        assert result == expected_result

    def test_base64_img_with_default_mime_type(self):
        """测试默认MIME类型的base64转换"""
        test_data = b"test image data"

        result = ImageUtils.base64_img(test_data)

        expected_b64 = base64.b64encode(test_data).decode("utf-8")
        expected_result = f"data:image/png;base64,{expected_b64}"

        assert result == expected_result

    @patch("email_widget.utils.image_utils.get_project_logger")
    def test_base64_img_exception_handling(self, mock_logger):
        """测试base64转换异常处理"""
        mock_logger_instance = MagicMock()
        mock_logger.return_value = mock_logger_instance

        # 模拟编码失败
        with patch("base64.b64encode", side_effect=Exception("Encoding error")):
            result = ImageUtils.base64_img(b"test data")

            assert result == ""
            mock_logger_instance.error.assert_called_once()

    def test_get_mime_type(self):
        """测试获取MIME类型"""
        test_cases = [
            (".png", "image/png"),
            (".jpg", "image/jpeg"),
            (".jpeg", "image/jpeg"),
            (".gif", "image/gif"),
            (".bmp", "image/bmp"),
            (".webp", "image/webp"),
            (".svg", "image/svg+xml"),
            (".unknown", "image/png"),  # 默认值
            (".PNG", "image/png"),  # 大小写测试
        ]

        for ext, expected_mime in test_cases:
            result = ImageUtils._get_mime_type(ext)
            assert result == expected_mime

    @patch("urllib.request.urlopen")
    def test_request_url_success(self, mock_urlopen):
        """测试成功的URL请求"""
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.read.return_value = b"image data"
        mock_response.headers.get.return_value = "image/jpeg"
        mock_response.__enter__.return_value = mock_response
        mock_response.__exit__.return_value = None

        mock_urlopen.return_value = mock_response

        result = ImageUtils.request_url("http://example.com/image.jpg")

        assert result == (b"image data", "image/jpeg")
        mock_urlopen.assert_called_once_with("http://example.com/image.jpg", timeout=10)

    @patch("urllib.request.urlopen")
    def test_request_url_custom_timeout(self, mock_urlopen):
        """测试自定义超时的URL请求"""
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.read.return_value = b"image data"
        mock_response.headers.get.return_value = "image/png"
        mock_response.__enter__.return_value = mock_response
        mock_response.__exit__.return_value = None

        mock_urlopen.return_value = mock_response

        result = ImageUtils.request_url("http://example.com/image.png", timeout=30)

        assert result == (b"image data", "image/png")
        mock_urlopen.assert_called_once_with("http://example.com/image.png", timeout=30)

    @patch("urllib.request.urlopen")
    @patch("email_widget.utils.image_utils.get_project_logger")
    def test_request_url_non_200_status(self, mock_logger, mock_urlopen):
        """测试非200状态码的URL请求"""
        mock_logger_instance = MagicMock()
        mock_logger.return_value = mock_logger_instance

        mock_response = MagicMock()
        mock_response.status = 404
        mock_response.__enter__.return_value = mock_response
        mock_response.__exit__.return_value = None

        mock_urlopen.return_value = mock_response

        result = ImageUtils.request_url("http://example.com/not_found.jpg")

        assert result is None
        mock_logger_instance.error.assert_called_once()

    @patch("urllib.request.urlopen")
    @patch("email_widget.utils.image_utils.get_project_logger")
    def test_request_url_network_error(self, mock_logger, mock_urlopen):
        """测试网络错误的URL请求"""
        mock_logger_instance = MagicMock()
        mock_logger.return_value = mock_logger_instance

        mock_urlopen.side_effect = urllib.error.URLError("Network error")

        result = ImageUtils.request_url("http://example.com/image.jpg")

        assert result is None
        mock_logger_instance.error.assert_called_once()

    @patch("urllib.request.urlopen")
    @patch("email_widget.utils.image_utils.get_project_logger")
    def test_request_url_general_exception(self, mock_logger, mock_urlopen):
        """测试一般异常的URL请求"""
        mock_logger_instance = MagicMock()
        mock_logger.return_value = mock_logger_instance

        mock_urlopen.side_effect = Exception("General error")

        result = ImageUtils.request_url("http://example.com/image.jpg")

        assert result is None
        mock_logger_instance.error.assert_called_once()

    @patch("builtins.open", new_callable=mock_open, read_data=b"file image data")
    @patch("pathlib.Path.exists")
    def test_process_image_source_local_file_success(self, mock_exists, mock_file):
        """测试成功处理本地文件"""
        mock_exists.return_value = True

        result = ImageUtils.process_image_source("test.png", cache=False, embed=True)

        expected_b64 = base64.b64encode(b"file image data").decode("utf-8")
        expected_result = f"data:image/png;base64,{expected_b64}"

        assert result == expected_result
        mock_file.assert_called_once_with(Path("test.png"), "rb")

    @patch("pathlib.Path.exists")
    @patch("email_widget.utils.image_utils.get_project_logger")
    def test_process_image_source_file_not_exists(self, mock_logger, mock_exists):
        """测试文件不存在的情况"""
        mock_logger_instance = MagicMock()
        mock_logger.return_value = mock_logger_instance
        mock_exists.return_value = False

        result = ImageUtils.process_image_source(
            "nonexistent.png", cache=False, embed=True
        )

        assert result is None
        mock_logger_instance.error.assert_called_once()

    def test_process_image_source_data_uri(self):
        """测试处理data URI"""
        data_uri = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8/5+hHgAHggJ/PchI7wAAAABJRU5ErkJggg=="

        result = ImageUtils.process_image_source(data_uri, cache=False, embed=True)

        assert result == data_uri

    @patch("email_widget.utils.image_utils.ImageUtils.request_url")
    def test_process_image_source_http_url_success(self, mock_request_url):
        """测试成功处理HTTP URL"""
        mock_request_url.return_value = (b"url image data", "image/jpeg")

        result = ImageUtils.process_image_source(
            "http://example.com/image.jpg", cache=False, embed=True
        )

        expected_b64 = base64.b64encode(b"url image data").decode("utf-8")
        expected_result = f"data:image/jpeg;base64,{expected_b64}"

        assert result == expected_result
        mock_request_url.assert_called_once_with("http://example.com/image.jpg")

    @patch("email_widget.utils.image_utils.ImageUtils.request_url")
    def test_process_image_source_http_url_failure(self, mock_request_url):
        """测试HTTP URL请求失败"""
        mock_request_url.return_value = None

        result = ImageUtils.process_image_source(
            "http://example.com/image.jpg", cache=False, embed=True
        )

        assert result is None

    @patch("email_widget.utils.image_utils.ImageUtils.request_url")
    def test_process_image_source_https_url(self, mock_request_url):
        """测试处理HTTPS URL"""
        mock_request_url.return_value = (b"https image data", "image/png")

        result = ImageUtils.process_image_source(
            "https://example.com/image.png", cache=False, embed=True
        )

        expected_b64 = base64.b64encode(b"https image data").decode("utf-8")
        expected_result = f"data:image/png;base64,{expected_b64}"

        assert result == expected_result

    @patch("email_widget.utils.image_utils.get_project_logger")
    def test_process_image_source_unsupported_format(self, mock_logger):
        """测试不支持的格式"""
        mock_logger_instance = MagicMock()
        mock_logger.return_value = mock_logger_instance

        result = ImageUtils.process_image_source(
            "ftp://example.com/image.jpg", cache=False, embed=True
        )

        assert result is None
        mock_logger_instance.error.assert_called_once()

    @patch("email_widget.utils.image_utils.get_image_cache")
    @patch("builtins.open", new_callable=mock_open, read_data=b"cached file data")
    @patch("pathlib.Path.exists")
    def test_process_image_source_with_cache_miss(
        self, mock_exists, mock_file, mock_get_cache
    ):
        """测试缓存未命中的情况"""
        mock_exists.return_value = True
        mock_cache = MagicMock()
        mock_cache.get.return_value = None  # 缓存未命中
        mock_get_cache.return_value = mock_cache

        result = ImageUtils.process_image_source("test.jpg", cache=True, embed=True)

        expected_b64 = base64.b64encode(b"cached file data").decode("utf-8")
        expected_result = f"data:image/jpeg;base64,{expected_b64}"

        assert result == expected_result
        mock_cache.get.assert_called_once_with("test.jpg")
        mock_cache.set.assert_called_once_with(
            "test.jpg", b"cached file data", "image/jpeg"
        )

    @patch("email_widget.utils.image_utils.get_image_cache")
    @patch("email_widget.utils.image_utils.ImageUtils.base64_img")
    def test_process_image_source_with_cache_hit(self, mock_base64_img, mock_get_cache):
        """测试缓存命中的情况"""
        mock_cache = MagicMock()
        mock_cache.get.return_value = (b"cached data", "image/png")  # 缓存命中
        mock_get_cache.return_value = mock_cache
        mock_base64_img.return_value = "data:image/png;base64,cached_result"

        result = ImageUtils.process_image_source("test.png", cache=True, embed=True)

        assert result == "data:image/png;base64,cached_result"
        mock_cache.get.assert_called_once_with("test.png")
        mock_base64_img.assert_called_once_with(b"cached data", "image/png")
        # 缓存命中时不应该调用set
        mock_cache.set.assert_not_called()

    def test_process_image_source_invalid_data(self):
        """测试无效的图片数据"""
        with patch("builtins.open", new_callable=mock_open, read_data=b""):
            with patch("pathlib.Path.exists", return_value=True):
                result = ImageUtils.process_image_source(
                    "empty.png", cache=False, embed=True
                )

                assert result is None
                # 空数据会被验证为无效并返回None

    @patch("email_widget.utils.image_utils.get_project_logger")
    def test_process_image_source_small_data(self, mock_logger):
        """测试过小的图片数据"""
        mock_logger_instance = MagicMock()
        mock_logger.return_value = mock_logger_instance

        with patch("builtins.open", new_callable=mock_open, read_data=b"small"):
            with patch("pathlib.Path.exists", return_value=True):
                result = ImageUtils.process_image_source(
                    "small.png", cache=False, embed=True
                )

                assert result is None
                mock_logger_instance.error.assert_called_once()

    @patch("email_widget.utils.image_utils.get_project_logger")
    def test_process_image_source_exception_handling(self, mock_logger):
        """测试处理过程中的异常"""
        mock_logger_instance = MagicMock()
        mock_logger.return_value = mock_logger_instance

        with patch("pathlib.Path.exists", side_effect=Exception("File system error")):
            result = ImageUtils.process_image_source(
                "test.png", cache=False, embed=True
            )

            assert result is None
            mock_logger_instance.error.assert_called_once()

    def test_process_image_source_path_object(self):
        """测试使用Path对象作为输入"""
        path_obj = Path("test.png")

        with patch(
            "builtins.open", new_callable=mock_open, read_data=b"path object data"
        ):
            with patch("pathlib.Path.exists", return_value=True):
                result = ImageUtils.process_image_source(
                    path_obj, cache=False, embed=True
                )

                expected_b64 = base64.b64encode(b"path object data").decode("utf-8")
                expected_result = f"data:image/png;base64,{expected_b64}"

                assert result == expected_result

    @pytest.mark.parametrize(
        "url,expected_call",
        [
            ("http://example.com/test.jpg", "http://example.com/test.jpg"),
            (
                "https://secure.example.com/image.png",
                "https://secure.example.com/image.png",
            ),
        ],
    )
    @patch("email_widget.utils.image_utils.ImageUtils.request_url")
    def test_process_image_source_url_variations(
        self, mock_request_url, url, expected_call
    ):
        """测试不同URL格式的处理"""
        mock_request_url.return_value = (b"test data", "image/png")

        ImageUtils.process_image_source(url, cache=False, embed=True)

        mock_request_url.assert_called_once_with(expected_call)

    @pytest.mark.parametrize("cache_enabled", [True, False])
    def test_process_image_source_cache_parameter(self, cache_enabled):
        """测试缓存参数的影响"""
        with patch("email_widget.utils.image_utils.get_image_cache") as mock_get_cache:
            with patch("builtins.open", new_callable=mock_open, read_data=b"test data"):
                with patch("pathlib.Path.exists", return_value=True):
                    ImageUtils.process_image_source(
                        "test.png", cache=cache_enabled, embed=True
                    )

                    if cache_enabled:
                        mock_get_cache.assert_called_once()
                    else:
                        mock_get_cache.assert_not_called()


class TestImageUtilsIntegration:
    """ImageUtils集成测试"""

    def test_full_workflow_local_file(self):
        """测试本地文件的完整工作流程"""
        test_data = b"integration test data"

        with patch("builtins.open", new_callable=mock_open, read_data=test_data):
            with patch("pathlib.Path.exists", return_value=True):
                result = ImageUtils.process_image_source(
                    "integration_test.png", embed=True
                )

                assert result is not None
                assert result.startswith("data:image/png;base64,")

                # 验证可以解码回原始数据
                base64_part = result.split(",")[1]
                decoded_data = base64.b64decode(base64_part)
                assert decoded_data == test_data

    def test_full_workflow_data_uri(self):
        """测试data URI的完整工作流程"""
        original_data = b"test image data"
        b64_data = base64.b64encode(original_data).decode("utf-8")
        data_uri = f"data:image/jpeg;base64,{b64_data}"

        result = ImageUtils.process_image_source(data_uri, embed=True)

        assert result == data_uri

    # ========== Embed 功能测试 ==========

    def test_process_image_source_embed_false_url(self):
        """测试embed=False时网络URL直接返回"""
        url = "https://example.com/image.png"

        result = ImageUtils.process_image_source(url, cache=False, embed=False)

        assert result == url
        # 不应该下载图片

    @patch("email_widget.utils.image_utils.get_project_logger")
    def test_process_image_source_embed_false_local_file_warning(self, mock_logger):
        """测试embed=False时本地文件会警告并强制嵌入"""
        mock_logger_instance = MagicMock()
        mock_logger.return_value = mock_logger_instance

        with patch(
            "builtins.open", new_callable=mock_open, read_data=b"local file data"
        ):
            with patch("pathlib.Path.exists", return_value=True):
                result = ImageUtils.process_image_source(
                    "local.png", cache=False, embed=False
                )

                # 应该发出警告
                mock_logger_instance.warning.assert_called_once()
                warning_call = mock_logger_instance.warning.call_args[0][0]
                assert "本地图片文件无法通过链接访问，将强制嵌入" in warning_call
                assert "local.png" in warning_call

                # 仍然应该返回base64编码
                expected_b64 = base64.b64encode(b"local file data").decode("utf-8")
                expected_result = f"data:image/png;base64,{expected_b64}"
                assert result == expected_result

    @patch("email_widget.utils.image_utils.ImageUtils.request_url")
    def test_process_image_source_embed_false_url_no_download(self, mock_request_url):
        """测试embed=False时网络URL不下载"""
        url = "https://example.com/test.jpg"

        result = ImageUtils.process_image_source(url, cache=False, embed=False)

        assert result == url
        # 确保没有调用下载函数
        mock_request_url.assert_not_called()

    def test_process_image_source_embed_false_data_uri(self):
        """测试embed=False时data URI直接返回"""
        data_uri = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8/5+hHgAHggJ/PchI7wAAAABJRU5ErkJggg=="

        result = ImageUtils.process_image_source(data_uri, cache=False, embed=False)

        assert result == data_uri

    @patch("email_widget.utils.image_utils.ImageUtils.request_url")
    def test_process_image_source_embed_true_url_downloads(self, mock_request_url):
        """测试embed=True时网络URL会下载"""
        mock_request_url.return_value = (b"downloaded data", "image/png")

        result = ImageUtils.process_image_source(
            "https://example.com/image.png", cache=False, embed=True
        )

        # 应该调用下载函数
        mock_request_url.assert_called_once_with("https://example.com/image.png")

        # 应该返回base64编码
        expected_b64 = base64.b64encode(b"downloaded data").decode("utf-8")
        expected_result = f"data:image/png;base64,{expected_b64}"
        assert result == expected_result

    @pytest.mark.parametrize(
        "url",
        [
            "http://example.com/image.jpg",
            "https://secure.example.com/photo.png",
            "https://cdn.example.com/assets/logo.gif",
        ],
    )
    def test_process_image_source_embed_false_various_urls(self, url):
        """测试embed=False对各种URL格式的处理"""
        result = ImageUtils.process_image_source(url, cache=False, embed=False)
        assert result == url

    @patch("email_widget.utils.image_utils.get_image_cache")
    def test_process_image_source_embed_false_no_cache_for_urls(self, mock_get_cache):
        """测试embed=False时URL不使用缓存"""
        url = "https://example.com/image.png"

        result = ImageUtils.process_image_source(url, cache=True, embed=False)

        assert result == url
        # 对于非嵌入的URL，不应该使用缓存
        mock_get_cache.assert_not_called()

    @patch("email_widget.utils.image_utils.get_image_cache")
    @patch("email_widget.utils.image_utils.get_project_logger")
    def test_process_image_source_embed_false_local_still_uses_cache(
        self, mock_logger, mock_get_cache
    ):
        """测试embed=False时本地文件仍然使用缓存"""
        mock_cache = MagicMock()
        mock_cache.get.return_value = None  # 缓存未命中
        mock_get_cache.return_value = mock_cache

        with patch(
            "builtins.open", new_callable=mock_open, read_data=b"cached local data"
        ):
            with patch("pathlib.Path.exists", return_value=True):
                result = ImageUtils.process_image_source(
                    "local.png", cache=True, embed=False
                )

                # 应该检查和设置缓存（因为本地文件强制嵌入）
                mock_get_cache.assert_called_once()
                mock_cache.get.assert_called_once_with("local.png")
                mock_cache.set.assert_called_once()
