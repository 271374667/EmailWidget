"""TextWidget测试用例"""

import pytest

from email_widget.core.enums import TextAlign, TextType
from email_widget.widgets.text_widget import SectionNumberManager, TextWidget


class TestSectionNumberManager:
    """章节编号管理器测试类"""

    def setup_method(self):
        """每个测试方法执行前的设置"""
        SectionNumberManager._instance = None
        SectionNumberManager._counters = {}

    def test_singleton_pattern(self):
        """测试单例模式"""
        manager1 = SectionNumberManager()
        manager2 = SectionNumberManager()
        assert manager1 is manager2

    @pytest.mark.parametrize(
        "level,expected",
        [
            (2, "1."),
            (3, "1.1."),
            (4, "1.1.1."),
            (5, "1.1.1.1."),
        ],
    )
    def test_get_next_number_sequential(self, level, expected):
        """测试连续获取编号"""
        manager = SectionNumberManager()
        # 先创建上级编号
        for i in range(2, level + 1):
            result = manager.get_next_number(i)
        assert result == expected

    def test_get_next_number_reset_lower_levels(self):
        """测试高级编号重置低级编号"""
        manager = SectionNumberManager()

        # 创建多级编号
        assert manager.get_next_number(2) == "1."
        assert manager.get_next_number(3) == "1.1."
        assert manager.get_next_number(4) == "1.1.1."

        # 创建新的2级编号，应该重置3级和4级
        assert manager.get_next_number(2) == "2."
        assert manager.get_next_number(3) == "2.1."

    def test_reset(self):
        """测试重置功能"""
        manager = SectionNumberManager()
        manager.get_next_number(2)
        manager.get_next_number(3)

        manager.reset()
        assert manager.get_next_number(2) == "1."


class TestTextWidget:
    """TextWidget测试类"""

    def setup_method(self):
        """每个测试方法执行前的设置"""
        self.widget = TextWidget()
        # 重置章节编号
        SectionNumberManager._instance = None
        SectionNumberManager._counters = {}

    def test_init_default_values(self):
        """测试初始化默认值"""
        widget = TextWidget("test_id")
        assert widget._widget_id == "test_id"
        assert widget._content == ""
        assert widget._text_type == TextType.BODY
        assert widget._font_size == "14px"
        assert widget._align == TextAlign.LEFT
        assert widget._color == "#323130"
        assert widget._line_height == "1.5"
        assert widget._font_weight == "normal"
        assert widget._font_family == "'Segoe UI', Tahoma, Arial, sans-serif"
        assert widget._margin == "16px 0"
        assert widget._max_width is None
        assert widget._section_number is None

    def test_init_validators(self):
        """测试验证器初始化"""
        widget = TextWidget()
        assert hasattr(widget, "_color_validator")
        assert hasattr(widget, "_size_validator")
        assert hasattr(widget, "_content_validator")

    @pytest.mark.parametrize(
        "content,should_pass",
        [
            ("Hello World", True),
            ("多行文本\n第二行", True),
            ("", False),
            ("   ", False),
        ],
    )
    def test_set_content_validation(self, content, should_pass):
        """测试内容验证"""
        if should_pass:
            result = self.widget.set_content(content)
            assert result is self.widget
            assert self.widget._content == content
        else:
            with pytest.raises(ValueError, match="文本内容验证失败"):
                self.widget.set_content(content)

    @pytest.mark.parametrize(
        "text_type",
        [
            TextType.TITLE_LARGE,
            TextType.TITLE_SMALL,
            TextType.BODY,
            TextType.CAPTION,
            TextType.SECTION_H2,
            TextType.SECTION_H3,
            TextType.SECTION_H4,
            TextType.SECTION_H5,
        ],
    )
    def test_set_type(self, text_type):
        """测试设置文本类型"""
        result = self.widget.set_type(text_type)
        assert result is self.widget
        assert self.widget._text_type == text_type

    def test_apply_type_styles_title_large(self):
        """测试大标题样式应用"""
        self.widget.set_type(TextType.TITLE_LARGE)
        assert self.widget._font_size == "28px"
        assert self.widget._font_weight == "bold"
        assert self.widget._color == "#323130"
        assert self.widget._align == TextAlign.CENTER
        assert self.widget._margin == "24px 0 16px 0"

    def test_apply_type_styles_section_h2(self):
        """测试H2标题样式应用"""
        self.widget.set_type(TextType.SECTION_H2)
        assert self.widget._font_size == "24px"
        assert self.widget._font_weight == "bold"
        assert self.widget._section_number == "1."

    @pytest.mark.parametrize(
        "font_size,should_pass",
        [
            ("16px", True),
            ("1.2em", True),
            ("120%", True),
            ("2rem", True),
            ("invalid_size", False),
            ("", False),
        ],
    )
    def test_set_font_size_validation(self, font_size, should_pass):
        """测试字体大小验证"""
        if should_pass:
            result = self.widget.set_font_size(font_size)
            assert result is self.widget
            assert self.widget._font_size == font_size
        else:
            with pytest.raises(ValueError, match="字体大小验证失败"):
                self.widget.set_font_size(font_size)

    @pytest.mark.parametrize(
        "align",
        [
            TextAlign.LEFT,
            TextAlign.CENTER,
            TextAlign.RIGHT,
            TextAlign.JUSTIFY,
        ],
    )
    def test_set_align(self, align):
        """测试对齐方式设置"""
        result = self.widget.set_align(align)
        assert result is self.widget
        assert self.widget._align == align

    @pytest.mark.parametrize(
        "color,should_pass",
        [
            ("#ff0000", True),
            ("red", True),
            ("blue", True),
            ("rgb(255,0,0)", True),
            ("rgba(255,0,0,0.5)", True),
            ("#fff", True),
            ("invalid_color", False),
            ("", False),
        ],
    )
    def test_set_color_validation(self, color, should_pass):
        """测试颜色验证"""
        if should_pass:
            result = self.widget.set_color(color)
            assert result is self.widget
            assert self.widget._color == color
        else:
            with pytest.raises(ValueError, match="颜色值验证失败"):
                self.widget.set_color(color)

    @pytest.mark.parametrize(
        "line_height",
        [
            "1.5",
            "24px",
            "150%",
            "2em",
        ],
    )
    def test_set_line_height(self, line_height):
        """测试行高设置"""
        result = self.widget.set_line_height(line_height)
        assert result is self.widget
        assert self.widget._line_height == line_height

    @pytest.mark.parametrize(
        "font_weight",
        [
            "normal",
            "bold",
            "600",
            "lighter",
            "bolder",
        ],
    )
    def test_set_font_weight(self, font_weight):
        """测试字体粗细设置"""
        result = self.widget.set_font_weight(font_weight)
        assert result is self.widget
        assert self.widget._font_weight == font_weight

    def test_set_font_family(self):
        """测试字体族设置"""
        font_family = "Arial, sans-serif"
        result = self.widget.set_font_family(font_family)
        assert result is self.widget
        assert self.widget._font_family == font_family

    def test_set_margin(self):
        """测试外边距设置"""
        margin = "20px 10px"
        result = self.widget.set_margin(margin)
        assert result is self.widget
        assert self.widget._margin == margin

    def test_set_max_width(self):
        """测试最大宽度设置"""
        max_width = "600px"
        result = self.widget.set_max_width(max_width)
        assert result is self.widget
        assert self.widget._max_width == max_width

    @pytest.mark.parametrize(
        "bold,expected_weight",
        [
            (True, "bold"),
            (False, "normal"),
        ],
    )
    def test_set_bold(self, bold, expected_weight):
        """测试粗体设置"""
        result = self.widget.set_bold(bold)
        assert result is self.widget
        assert self.widget._font_weight == expected_weight

    def test_set_italic(self):
        """测试斜体设置（当前为预留接口）"""
        result = self.widget.set_italic()
        assert result is self.widget
        # 斜体功能暂未实现，只测试返回值

    def test_reset_section_numbers(self):
        """测试重置章节编号"""
        # 先创建一些编号
        widget1 = TextWidget().set_type(TextType.SECTION_H2)
        widget2 = TextWidget().set_type(TextType.SECTION_H3)

        # 重置
        TextWidget.reset_section_numbers()

        # 新建widget应该从1开始
        widget3 = TextWidget().set_type(TextType.SECTION_H2)
        assert widget3._section_number == "1."

    def test_properties(self):
        """测试属性获取"""
        content = "Test content"
        font_size = "18px"
        color = "#ff0000"
        align = TextAlign.CENTER

        self.widget.set_content(content)
        self.widget.set_font_size(font_size)
        self.widget.set_color(color)
        self.widget.set_align(align)

        assert self.widget.content == content
        assert self.widget.font_size == font_size
        assert self.widget.color == color
        assert self.widget.align == align

    def test_get_template_name(self):
        """测试模板名称获取"""
        assert self.widget._get_template_name() == "text.html"

    def test_get_template_context_single_line(self):
        """测试单行文本模板上下文"""
        self.widget.set_content("Single line")
        self.widget.set_type(TextType.BODY)

        context = self.widget.get_template_context()

        assert context["content"] == "Single line"
        assert context["content_lines"] == ["Single line"]
        assert context["section_number"] is None
        assert "text_style" in context
        assert "tag_name" in context

    def test_get_template_context_multi_line(self):
        """测试多行文本模板上下文"""
        self.widget.set_content("Line 1\nLine 2\n\nLine 4")

        context = self.widget.get_template_context()

        assert context["content_lines"] == ["Line 1", "Line 2", "", "Line 4"]

    def test_get_template_context_section_header(self):
        """测试章节标题模板上下文"""
        self.widget.set_content("Chapter Title")
        self.widget.set_type(TextType.SECTION_H2)

        context = self.widget.get_template_context()

        assert context["section_number"] == "1."
        assert context["tag_name"] == "h2"

    def test_get_template_context_styling(self):
        """测试样式生成"""
        self.widget.set_content("Styled text")
        self.widget.set_font_size("20px")
        self.widget.set_color("#ff0000")
        self.widget.set_align(TextAlign.CENTER)
        self.widget.set_max_width("500px")

        context = self.widget.get_template_context()
        text_style = context["text_style"]

        assert "font-size: 20px" in text_style
        assert "color: #ff0000" in text_style
        assert "text-align: center" in text_style
        assert "max-width: 500px" in text_style

    def test_template_context_empty_content(self):
        """测试空内容时的模板上下文"""
        context = self.widget.get_template_context()
        assert context == {}

    @pytest.mark.parametrize(
        "text_type,expected_tag",
        [
            (TextType.SECTION_H2, "h2"),
            (TextType.SECTION_H3, "h3"),
            (TextType.SECTION_H4, "h4"),
            (TextType.SECTION_H5, "h5"),
            (TextType.BODY, "p"),
        ],
    )
    def test_get_tag_name(self, text_type, expected_tag):
        """测试HTML标签名称生成"""
        self.widget.set_type(text_type)
        self.widget.set_content("Test")

        context = self.widget.get_template_context()
        assert context["tag_name"] == expected_tag

    def test_chain_methods(self):
        """测试方法链式调用"""
        result = (
            self.widget.set_content("Chained content")
            .set_type(TextType.TITLE_LARGE)
            .set_color("#0066cc")
            .set_font_size("24px")
            .set_align(TextAlign.CENTER)
        )

        assert result is self.widget
        assert self.widget._content == "Chained content"
        assert self.widget._text_type == TextType.TITLE_LARGE
        assert self.widget._color == "#0066cc"
        assert self.widget._font_size == "24px"
        assert self.widget._align == TextAlign.CENTER
