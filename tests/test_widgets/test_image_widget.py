"""图片Widget测试模块"""

from pathlib import Path
from unittest.mock import patch

import pytest

from email_widget.core.validators import (
    NonEmptyStringValidator,
    SizeValidator,
    UrlValidator,
)
from email_widget.widgets.image_widget import ImageWidget


class TestImageWidget:
    """ImageWidget测试类"""

    def setup_method(self):
        """每个测试方法前的设置"""
        self.widget = ImageWidget()

    def test_init(self):
        """测试初始化"""
        assert self.widget._image_url is None
        assert self.widget._title is None
        assert self.widget._description is None
        assert self.widget._alt_text == ""
        assert self.widget._width is None
        assert self.widget._height is None
        assert self.widget._border_radius == "4px"
        assert self.widget._show_caption is True
        assert self.widget._max_width == "100%"

        # 验证验证器初始化
        assert isinstance(self.widget._size_validator, SizeValidator)
        assert isinstance(self.widget._url_validator, UrlValidator)
        assert isinstance(self.widget._text_validator, NonEmptyStringValidator)

    def test_init_with_widget_id(self):
        """测试使用widget_id初始化"""
        widget = ImageWidget("test_id")
        assert widget.widget_id == "test_id"

    @patch("email_widget.utils.image_utils.ImageUtils.process_image_source")
    def test_set_image_url_with_string(self, mock_process):
        """测试设置图片URL字符串"""
        mock_process.return_value = "data:image/png;base64,test_data"

        result = self.widget.set_image_url("https://example.com/image.png")

        assert result is self.widget  # 支持链式调用
        mock_process.assert_called_once_with(
            "https://example.com/image.png", cache=True, embed=True
        )
        assert self.widget._image_url == "data:image/png;base64,test_data"

    @patch("email_widget.utils.image_utils.ImageUtils.process_image_source")
    def test_set_image_url_with_path(self, mock_process):
        """测试设置图片Path对象"""
        mock_process.return_value = "data:image/jpeg;base64,test_data"
        image_path = Path("test.jpg")

        result = self.widget.set_image_url(image_path, cache=False)

        assert result is self.widget
        mock_process.assert_called_once_with(image_path, cache=False, embed=True)
        assert self.widget._image_url == "data:image/jpeg;base64,test_data"

    def test_set_title(self):
        """测试设置标题"""
        result = self.widget.set_title("测试标题")

        assert result is self.widget
        assert self.widget._title == "测试标题"

    def test_set_description(self):
        """测试设置描述"""
        result = self.widget.set_description("测试描述")

        assert result is self.widget
        assert self.widget._description == "测试描述"

    def test_set_alt_text(self):
        """测试设置替代文本"""
        result = self.widget.set_alt_text("替代文本")

        assert result is self.widget
        assert self.widget._alt_text == "替代文本"

    def test_set_size_valid(self):
        """测试设置有效尺寸"""
        with patch.object(self.widget._size_validator, "validate", return_value=True):
            result = self.widget.set_size("300px", "200px")

            assert result is self.widget
            assert self.widget._width == "300px"
            assert self.widget._height == "200px"

    def test_set_size_invalid_width(self):
        """测试设置无效宽度"""
        with patch.object(self.widget._size_validator, "validate", return_value=False):
            with patch.object(
                self.widget._size_validator,
                "get_error_message",
                return_value="无效宽度",
            ):
                with pytest.raises(ValueError, match="宽度值验证失败: 无效宽度"):
                    self.widget.set_size("invalid", "200px")

    def test_set_size_invalid_height(self):
        """测试设置无效高度"""
        with patch.object(
            self.widget._size_validator, "validate", side_effect=[True, False]
        ):
            with patch.object(
                self.widget._size_validator,
                "get_error_message",
                return_value="无效高度",
            ):
                with pytest.raises(ValueError, match="高度值验证失败: 无效高度"):
                    self.widget.set_size("200px", "invalid")

    def test_set_size_none_values(self):
        """测试设置None值"""
        result = self.widget.set_size(None, None)

        assert result is self.widget
        assert self.widget._width is None
        assert self.widget._height is None

    def test_set_border_radius(self):
        """测试设置边框圆角"""
        result = self.widget.set_border_radius("8px")

        assert result is self.widget
        assert self.widget._border_radius == "8px"

    def test_set_max_width(self):
        """测试设置最大宽度"""
        result = self.widget.set_max_width("600px")

        assert result is self.widget
        assert self.widget._max_width == "600px"

    def test_show_caption(self):
        """测试设置显示标题"""
        result = self.widget.show_caption(False)

        assert result is self.widget
        assert self.widget._show_caption is False

        # 测试默认值
        result = self.widget.show_caption()
        assert self.widget._show_caption is True

    def test_properties(self):
        """测试所有属性getter"""
        # 设置值
        self.widget._image_url = "test_url"
        self.widget._title = "test_title"
        self.widget._description = "test_desc"
        self.widget._alt_text = "test_alt"
        self.widget._width = "300px"
        self.widget._height = "200px"
        self.widget._border_radius = "8px"
        self.widget._show_caption = False

        # 验证属性
        assert self.widget.image_url == "test_url"
        assert self.widget.title == "test_title"
        assert self.widget.description == "test_desc"
        assert self.widget.alt_text == "test_alt"
        assert self.widget.width == "300px"
        assert self.widget.height == "200px"
        assert self.widget.border_radius == "8px"
        assert self.widget.is_show_caption is False

    def test_get_template_name(self):
        """测试获取模板名称"""
        assert self.widget._get_template_name() == "image.html"

    def test_get_template_context_no_image(self):
        """测试无图片时的模板上下文"""
        context = self.widget.get_template_context()
        assert context == {}

    def test_get_template_context_with_image(self):
        """测试有图片时的模板上下文"""
        # 设置图片数据
        self.widget._image_url = "data:image/png;base64,test"
        self.widget._title = "测试图片"
        self.widget._description = "图片描述"
        self.widget._alt_text = "替代文本"
        self.widget._width = "300px"
        self.widget._height = "200px"
        self.widget._border_radius = "8px"
        self.widget._show_caption = True
        self.widget._max_width = "600px"

        context = self.widget.get_template_context()

        # 验证基本数据
        assert context["image_url"] == "data:image/png;base64,test"
        assert context["title"] == "测试图片"
        assert context["description"] == "图片描述"
        assert context["alt_text"] == "替代文本"
        assert context["show_caption"] is True

        # 验证样式计算
        assert "container_style" in context
        assert "img_style" in context
        assert "img_width" in context
        assert "img_height" in context

        # 验证尺寸处理
        assert context["img_width"] == "300"  # px被移除
        assert context["img_height"] == "200"

    def test_get_template_context_no_caption(self):
        """测试不显示标题时的模板上下文"""
        self.widget._image_url = "data:image/png;base64,test"
        self.widget._show_caption = False

        context = self.widget.get_template_context()

        assert context["show_caption"] is False

    def test_get_template_context_without_px_units(self):
        """测试不含px单位的尺寸处理"""
        self.widget._image_url = "data:image/png;base64,test"
        self.widget._width = "300"
        self.widget._height = "200"

        context = self.widget.get_template_context()

        assert context["img_width"] == "300"
        assert context["img_height"] == "200"


class TestImageWidgetIntegration:
    """ImageWidget集成测试类"""

    def setup_method(self):
        """每个测试方法前的设置"""
        self.widget = ImageWidget()

    def test_chaining_methods(self):
        """测试方法链式调用"""
        with patch(
            "email_widget.utils.image_utils.ImageUtils.process_image_source",
            return_value="data:image/png;base64,test",
        ):
            widget = (
                ImageWidget("test_id")
                .set_image_url("test.png")
                .set_title("标题")
                .set_description("描述")
                .set_alt_text("替代文本")
                .set_size("300px", "200px")
                .set_border_radius("8px")
                .set_max_width("600px")
                .show_caption(True)
            )

            assert widget.widget_id == "test_id"
            assert widget.image_url == "data:image/png;base64,test"
            assert widget.title == "标题"
            assert widget.description == "描述"
            assert widget.alt_text == "替代文本"
            assert widget.width == "300px"
            assert widget.height == "200px"
            assert widget.border_radius == "8px"
            assert widget._max_width == "600px"
            assert widget.is_show_caption is True

    @patch("email_widget.utils.image_utils.ImageUtils.process_image_source")
    def test_full_workflow(self, mock_process):
        """测试完整工作流程"""
        mock_process.return_value = "data:image/jpeg;base64,full_test_data"

        widget = ImageWidget()

        # 配置widget
        widget.set_image_url("https://example.com/image.jpg")
        widget.set_title("产品图片")
        widget.set_description("这是一个产品展示图片")
        widget.set_alt_text("产品展示")
        widget.set_size("400px", "300px")
        widget.set_border_radius("12px")
        widget.show_caption(True)

        # 获取模板上下文
        context = widget.get_template_context()

        # 验证完整上下文
        assert context["image_url"] == "data:image/jpeg;base64,full_test_data"
        assert context["title"] == "产品图片"
        assert context["description"] == "这是一个产品展示图片"
        assert context["alt_text"] == "产品展示"
        assert context["show_caption"] is True
        assert context["img_width"] == "400"
        assert context["img_height"] == "300"

        # 验证ImageUtils调用
        mock_process.assert_called_once_with(
            "https://example.com/image.jpg", cache=True, embed=True
        )

    def test_validation_integration(self):
        """测试验证器集成"""
        widget = ImageWidget()

        # 测试尺寸验证失败时的行为
        with patch.object(widget._size_validator, "validate", return_value=False):
            with patch.object(
                widget._size_validator, "get_error_message", return_value="尺寸格式错误"
            ):
                with pytest.raises(ValueError):
                    widget.set_size("invalid_size", "200px")

    @patch("email_widget.utils.image_utils.ImageUtils.process_image_source")
    def test_set_image_url_with_embed_true(self, mock_process):
        """测试embed=True时的行为（默认行为）"""
        mock_process.return_value = "data:image/png;base64,embedded_data"

        result = self.widget.set_image_url("https://example.com/image.png", embed=True)

        assert result is self.widget
        mock_process.assert_called_once_with(
            "https://example.com/image.png", cache=True, embed=True
        )
        assert self.widget._image_url == "data:image/png;base64,embedded_data"

    @patch("email_widget.utils.image_utils.ImageUtils.process_image_source")
    def test_set_image_url_with_embed_false(self, mock_process):
        """测试embed=False时的行为（网络URL直接返回）"""
        mock_process.return_value = "https://example.com/image.png"

        result = self.widget.set_image_url("https://example.com/image.png", embed=False)

        assert result is self.widget
        mock_process.assert_called_once_with(
            "https://example.com/image.png", cache=True, embed=False
        )
        assert self.widget._image_url == "https://example.com/image.png"

    @patch("email_widget.utils.image_utils.ImageUtils.process_image_source")
    def test_set_image_url_local_file_with_embed_false(self, mock_process):
        """测试本地文件embed=False时的行为（强制嵌入）"""
        mock_process.return_value = "data:image/png;base64,forced_embed_data"
        local_path = Path("test_image.png")

        result = self.widget.set_image_url(local_path, embed=False)

        assert result is self.widget
        mock_process.assert_called_once_with(local_path, cache=True, embed=False)
        assert self.widget._image_url == "data:image/png;base64,forced_embed_data"

    @patch("email_widget.utils.image_utils.ImageUtils.process_image_source")
    def test_set_image_url_with_all_params(self, mock_process):
        """测试所有参数的组合"""
        mock_process.return_value = "https://cdn.example.com/optimized.png"

        result = self.widget.set_image_url(
            "https://example.com/image.png", cache=False, embed=False
        )

        assert result is self.widget
        mock_process.assert_called_once_with(
            "https://example.com/image.png", cache=False, embed=False
        )
        assert self.widget._image_url == "https://cdn.example.com/optimized.png"
