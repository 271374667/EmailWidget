"""ButtonWidget测试用例"""

import re

import pytest

from email_widget.widgets.button_widget import ButtonWidget


class TestButtonWidget:
    """ButtonWidget测试类"""

    def setup_method(self):
        """每个测试方法执行前的设置"""
        self.widget = ButtonWidget()

    def test_init_default_values(self):
        """测试初始化默认值"""
        widget = ButtonWidget("test_id")
        assert widget._widget_id == "test_id"
        assert widget._text == ""
        assert widget._href == ""
        assert widget._background_color == "#3b82f6"
        assert widget._text_color == "#ffffff"
        assert widget._width is None
        assert widget._align == "left"
        assert widget._padding == "10px 20px"
        assert widget._border_radius == "6px"
        assert widget._font_size == "14px"
        assert widget._font_weight == "600"
        assert widget._border is None

    def test_init_validators(self):
        """测试验证器初始化"""
        widget = ButtonWidget()
        assert hasattr(widget, "_text_validator")
        assert hasattr(widget, "_url_validator")

    @pytest.mark.parametrize(
        "text,should_pass",
        [
            ("点击这里", True),
            ("Click Me", True),
            ("立即购买", True),
            ("", False),
            ("   ", False),
        ],
    )
    def test_set_text_validation(self, text, should_pass):
        """测试文本验证"""
        if should_pass:
            result = self.widget.set_text(text)
            assert result is self.widget
            assert self.widget._text == text
        else:
            with pytest.raises(ValueError, match="按钮文本验证失败"):
                self.widget.set_text(text)

    @pytest.mark.parametrize(
        "href,should_pass",
        [
            ("https://example.com", True),
            ("http://example.com/page", True),
            ("https://example.com/page?param=1", True),
            ("not-a-url", False),
            ("", False),
            ("   ", False),
        ],
    )
    def test_set_href_validation(self, href, should_pass):
        """测试链接验证"""
        # 基本的URL格式验证
        url_pattern = re.compile(
            r"^(?:https?|ftp)://"  # http://, https://, 或 ftp://
            r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|"  # 域名
            r"localhost|"  # localhost
            r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # IP地址
            r"(?::\d+)?"  # 可选端口
            r"(?:/?|[/?]\S+)$",
            re.IGNORECASE,
        )

        if should_pass:
            result = self.widget.set_href(href)
            assert result is self.widget
            assert self.widget._href == href
        else:
            with pytest.raises(ValueError, match="链接地址验证失败"):
                self.widget.set_href(href)

    @pytest.mark.parametrize(
        "color",
        [
            "#3b82f6",
            "#ff0000",
            "red",
            "rgb(255, 0, 0)",
            "rgba(255, 0, 0, 0.5)",
        ],
    )
    def test_set_background_color(self, color):
        """测试设置背景颜色"""
        result = self.widget.set_background_color(color)
        assert result is self.widget
        assert self.widget._background_color == color

    @pytest.mark.parametrize(
        "color",
        [
            "#ffffff",
            "#000000",
            "white",
            "black",
        ],
    )
    def test_set_text_color(self, color):
        """测试设置文字颜色"""
        result = self.widget.set_text_color(color)
        assert result is self.widget
        assert self.widget._text_color == color

    @pytest.mark.parametrize(
        "width",
        [
            "200px",
            "100%",
            "50%",
            "300px",
            None,
        ],
    )
    def test_set_width(self, width):
        """测试设置宽度"""
        result = self.widget.set_width(width)
        assert result is self.widget
        assert self.widget._width == width

    @pytest.mark.parametrize(
        "align,should_pass",
        [
            ("left", True),
            ("center", True),
            ("right", True),
            ("top", False),
            ("bottom", False),
            ("invalid", False),
        ],
    )
    def test_set_align(self, align, should_pass):
        """测试设置对齐方式"""
        if should_pass:
            result = self.widget.set_align(align)
            assert result is self.widget
            assert self.widget._align == align
        else:
            with pytest.raises(ValueError, match="无效的对齐方式"):
                self.widget.set_align(align)

    @pytest.mark.parametrize(
        "padding",
        [
            "10px 20px",
            "12px 24px",
            "8px 16px 8px 16px",
            "15px",
        ],
    )
    def test_set_padding(self, padding):
        """测试设置内边距"""
        result = self.widget.set_padding(padding)
        assert result is self.widget
        assert self.widget._padding == padding

    @pytest.mark.parametrize(
        "radius",
        [
            "6px",
            "8px",
            "12px",
            "50%",
            "0",
        ],
    )
    def test_set_border_radius(self, radius):
        """测试设置圆角半径"""
        result = self.widget.set_border_radius(radius)
        assert result is self.widget
        assert self.widget._border_radius == radius

    @pytest.mark.parametrize(
        "size",
        [
            "14px",
            "16px",
            "18px",
            "1em",
            "1.2rem",
        ],
    )
    def test_set_font_size(self, size):
        """测试设置字体大小"""
        result = self.widget.set_font_size(size)
        assert result is self.widget
        assert self.widget._font_size == size

    @pytest.mark.parametrize(
        "weight",
        [
            "normal",
            "600",
            "bold",
            "700",
            "lighter",
        ],
    )
    def test_set_font_weight(self, weight):
        """测试设置字体粗细"""
        result = self.widget.set_font_weight(weight)
        assert result is self.widget
        assert self.widget._font_weight == weight

    @pytest.mark.parametrize(
        "border",
        [
            "2px solid #3b82f6",
            "1px dashed #ccc",
            "3px double #000",
            None,
        ],
    )
    def test_set_border(self, border):
        """测试设置边框"""
        result = self.widget.set_border(border)
        assert result is self.widget
        assert self.widget._border == border

    def test_set_full_button_basic(self):
        """测试完整按钮设置（基本）"""
        result = self.widget.set_full_button("点击我", "https://example.com")
        assert result is self.widget
        assert self.widget._text == "点击我"
        assert self.widget._href == "https://example.com"
        assert self.widget._background_color == "#3b82f6"  # 默认颜色

    def test_set_full_button_with_color(self):
        """测试完整按钮设置（带颜色）"""
        result = self.widget.set_full_button(
            "立即购买", "https://shop.example.com", "#22c55e"
        )
        assert result is self.widget
        assert self.widget._text == "立即购买"
        assert self.widget._href == "https://shop.example.com"
        assert self.widget._background_color == "#22c55e"

    def test_get_template_name(self):
        """测试模板名称获取"""
        assert self.widget._get_template_name() == "button.html"

    def test_get_template_context_empty(self):
        """测试空内容时的模板上下文"""
        context = self.widget.get_template_context()
        assert context == {}

    def test_get_template_context_missing_text(self):
        """测试缺少文本时的模板上下文"""
        self.widget.set_href("https://example.com")
        context = self.widget.get_template_context()
        assert context == {}

    def test_get_template_context_missing_href(self):
        """测试缺少链接时的模板上下文"""
        self.widget.set_text("点击这里")
        context = self.widget.get_template_context()
        assert context == {}

    def test_get_template_context_basic(self):
        """测试基本模板上下文"""
        self.widget.set_text("查看详情")
        self.widget.set_href("https://example.com/details")

        context = self.widget.get_template_context()

        assert context["text"] == "查看详情"
        assert context["href"] == "https://example.com/details"
        assert context["align"] == "left"
        assert "button_style" in context

        # 检查基本样式
        button_style = context["button_style"]
        assert "display: inline-block" in button_style
        assert "background-color: #3b82f6" in button_style
        assert "color: #ffffff" in button_style
        assert "padding: 10px 20px" in button_style
        assert "border-radius: 6px" in button_style
        assert "text-decoration: none" in button_style
        assert "font-size: 14px" in button_style
        assert "font-weight: 600" in button_style
        assert "border: none" in button_style

    def test_get_template_context_custom_style(self):
        """测试自定义样式的模板上下文"""
        self.widget.set_text("立即购买")
        self.widget.set_href("https://shop.example.com")
        self.widget.set_background_color("#22c55e")
        self.widget.set_text_color("#000000")
        self.widget.set_width("200px")
        self.widget.set_align("center")
        self.widget.set_padding("12px 24px")
        self.widget.set_border_radius("8px")
        self.widget.set_font_size("16px")
        self.widget.set_font_weight("bold")
        self.widget.set_border("2px solid #16a34a")

        context = self.widget.get_template_context()

        assert context["text"] == "立即购买"
        assert context["href"] == "https://shop.example.com"
        assert context["align"] == "center"

        button_style = context["button_style"]
        assert "background-color: #22c55e" in button_style
        assert "color: #000000" in button_style
        assert "width: 200px" in button_style
        assert "box-sizing: border-box" in button_style
        assert "padding: 12px 24px" in button_style
        assert "border-radius: 8px" in button_style
        assert "font-size: 16px" in button_style
        assert "font-weight: bold" in button_style
        assert "border: 2px solid #16a34a" in button_style

    def test_chain_methods(self):
        """测试方法链式调用"""
        result = (
            self.widget.set_text("开始使用")
            .set_href("https://example.com/start")
            .set_background_color("#3b82f6")
            .set_text_color("#ffffff")
            .set_width("150px")
            .set_align("center")
            .set_padding("8px 16px")
            .set_border_radius("4px")
            .set_font_size("14px")
            .set_font_weight("normal")
            .set_border("1px solid #2563eb")
        )

        assert result is self.widget
        assert self.widget._text == "开始使用"
        assert self.widget._href == "https://example.com/start"
        assert self.widget._background_color == "#3b82f6"
        assert self.widget._text_color == "#ffffff"
        assert self.widget._width == "150px"
        assert self.widget._align == "center"
        assert self.widget._padding == "8px 16px"
        assert self.widget._border_radius == "4px"
        assert self.widget._font_size == "14px"
        assert self.widget._font_weight == "normal"
        assert self.widget._border == "1px solid #2563eb"

    def test_render_html_integration(self):
        """测试HTML渲染集成"""
        self.widget.set_text("测试按钮")
        self.widget.set_href("https://test.com")

        # 由于render_html是BaseWidget的方法，这里主要测试get_template_context是否正确
        context = self.widget.get_template_context()
        assert context["text"] == "测试按钮"
        assert context["href"] == "https://test.com"
        assert "button_style" in context
