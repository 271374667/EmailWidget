"""文本Widget实现

这个模块提供了文本显示功能的Widget，支持多种文本类型和样式设置.
"""

from typing import Any

from email_widget.core.base import BaseWidget
from email_widget.core.enums import TextAlign, TextType
from email_widget.core.validators import (
    ColorValidator,
    NonEmptyStringValidator,
    SizeValidator,
)


class SectionNumberManager:
    """章节编号管理器.

    这是一个单例类，用于管理文档中的章节编号.
    支持多级章节编号（H2-H5），自动处理编号的递增和重置.

    Attributes:
        _instance: 单例实例
        _counters: 各级别的计数器字典

    Examples:
        >>> manager = SectionNumberManager()
        >>> print(manager.get_next_number(2))  # "1."
        >>> print(manager.get_next_number(3))  # "1.1."
        >>> print(manager.get_next_number(2))  # "2."
        >>> manager.reset()  # 重置所有计数器
    """

    _instance = None
    _counters: dict[int, int] = {}  # 级别 -> 计数器

    def __new__(cls):
        """创建单例实例.

        Returns:
            SectionNumberManager的唯一实例
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._counters = {2: 0, 3: 0, 4: 0, 5: 0}
        return cls._instance

    def get_next_number(self, level: int) -> str:
        """获取指定级别的下一个章节编号.

        Args:
            level: 章节级别（2-5，对应H2-H5）

        Returns:
            格式化的章节编号字符串（如 "1.2.3."）

        Examples:
            >>> manager = SectionNumberManager()
            >>> manager.get_next_number(2)  # "1."
            >>> manager.get_next_number(3)  # "1.1."
            >>> manager.get_next_number(3)  # "1.2."
        """
        # 重置低级别计数器
        for l in range(level + 1, 6):
            self._counters[l] = 0

        # 增加当前级别计数器
        self._counters[level] += 1

        # 生成编号字符串
        numbers = []
        for l in range(2, level + 1):
            if self._counters[l] > 0:
                numbers.append(str(self._counters[l]))

        return ".".join(numbers) + "."

    def reset(self):
        """重置所有章节编号计数器.

        Examples:
            >>> manager = SectionNumberManager()
            >>> manager.get_next_number(2)  # "1."
            >>> manager.reset()
            >>> manager.get_next_number(2)  # "1." (重新开始)
        """
        self._counters = {2: 0, 3: 0, 4: 0, 5: 0}


class TextWidget(BaseWidget):
    """TextWidget 是用于显示各种类型文本内容的组件，支持多种预定义文本类型和丰富的样式配置.

    这个Widget支持多种文本类型（标题、正文、说明文字、章节标题等），
    并提供丰富的样式设置选项.章节标题会自动添加编号.

    主要功能：
    - 支持多种预定义文本类型
    - 自定义字体、颜色、对齐方式等样式
    - 自动章节编号
    - 多行文本支持
    - 响应式设计

    Attributes:
        _content (str): 文本内容.
        _text_type (TextType): 文本类型.
        _font_size (str): 字体大小.
        _align (TextAlign): 对齐方式.
        _color (str): 文本颜色.
        _line_height (str): 行高.
        _font_weight (str): 字体粗细.
        _font_family (str): 字体族.
        _margin (str): 外边距.
        _max_width (Optional[str]): 最大宽度.
        _section_number (Optional[str]): 章节编号.

    Examples:
        ```python
        from email_widget.widgets import TextWidget
        from email_widget.core.enums import TextType, TextAlign

        # 基本用法
        text = TextWidget().set_content("Hello World")

        # 链式调用
        title = (TextWidget()\
            .set_content("重要标题")\
            .set_type(TextType.TITLE_LARGE)\
            .set_color("#0078d4")\
            .set_align(TextAlign.CENTER))

        # 章节标题（自动编号）
        section = TextWidget().set_content("数据分析").set_type(TextType.SECTION_H2)
        ```
    """

    # 模板定义
    TEMPLATE = """
    <!--[if mso]>
    <table width="100%" cellpadding="0" cellspacing="0" border="0">
        <tr>
            <td>
    <![endif]-->
    {% if section_number %}
        <{{ tag_name }} style="{{ text_style }}">{{ section_number }} {{ content }}</{{ tag_name }}>
    {% else %}
        {% if content_lines|length > 1 %}
            <div style="{{ text_style }}">
                {% for line in content_lines %}
                    {% if line.strip() %}
                        <p style="margin: 4px 0; font-family: Arial, sans-serif;">{{ line.strip() }}</p>
                    {% else %}
                        <br/>
                    {% endif %}
                {% endfor %}
            </div>
        {% else %}
            <p style="{{ text_style }}">{{ content }}</p>
        {% endif %}
    {% endif %}
    <!--[if mso]>
            </td>
        </tr>
    </table>
    <![endif]-->
    """

    def __init__(self, widget_id: str | None = None):
        """初始化TextWidget.

        Args:
            widget_id (Optional[str]): 可选的Widget ID.
        """
        super().__init__(widget_id)
        self._content: str = ""
        self._text_type: TextType = TextType.BODY
        self._font_size: str = "14px"
        self._align: TextAlign = TextAlign.LEFT
        self._color: str = "#323130"
        self._line_height: str = "1.5"
        self._font_weight: str = "normal"
        self._font_family: str = "'Segoe UI', Tahoma, Arial, sans-serif"
        self._margin: str = "16px 0"
        self._max_width: str | None = None
        self._section_number: str | None = None
        self._section_manager = SectionNumberManager()

        # 初始化验证器
        self._color_validator = ColorValidator()
        self._size_validator = SizeValidator()
        self._content_validator = NonEmptyStringValidator()

    def set_content(self, content: str) -> "TextWidget":
        """设置文本内容，支持多行文本（使用`\n`分隔）.

        Args:
            content (str): 文本内容.

        Returns:
            TextWidget: 支持链式调用.

        Raises:
            ValueError: 当内容为空字符串时.

        Examples:
            >>> widget = TextWidget().set_content("Hello World")
            >>> # 多行文本
            >>> widget = TextWidget().set_content("第一行\n第二行\n第三行")
        """
        if not self._content_validator.validate(content):
            raise ValueError(
                f"文本内容验证失败: {self._content_validator.get_error_message(content)}"
            )

        self._content = content
        return self

    def set_type(self, text_type: TextType) -> "TextWidget":
        """设置文本类型，不同类型会应用不同的预设样式.

        Args:
            text_type (TextType): 文本类型枚举值.

        Returns:
            TextWidget: 支持链式调用.

        Examples:
            >>> widget = TextWidget().set_type(TextType.TITLE_LARGE)
            >>> widget = TextWidget().set_type(TextType.SECTION_H2)
        """
        self._text_type = text_type
        self._apply_type_styles()
        return self

    def set_font_size(self, size: str) -> "TextWidget":
        """设置字体大小.

        Args:
            size (str): CSS字体大小值（如 "16px", "1.2em", "120%"）.

        Returns:
            TextWidget: 支持链式调用.

        Raises:
            ValueError: 当尺寸格式无效时.

        Examples:
            >>> widget = TextWidget().set_font_size("18px")
            >>> widget = TextWidget().set_font_size("1.5em")
        """
        if not self._size_validator.validate(size):
            raise ValueError(
                f"字体大小验证失败: {self._size_validator.get_error_message(size)}"
            )

        self._font_size = size
        return self

    def set_align(self, align: TextAlign) -> "TextWidget":
        """设置文本对齐方式.

        Args:
            align (TextAlign): 对齐方式枚举值.

        Returns:
            TextWidget: 支持链式调用.

        Examples:
            >>> widget = TextWidget().set_align(TextAlign.CENTER)
            >>> widget = TextWidget().set_align(TextAlign.RIGHT)
        """
        self._align = align
        return self

    def set_color(self, color: str) -> "TextWidget":
        """设置文本颜色.

        Args:
            color (str): CSS颜色值（如 "#ff0000", "red", "rgb(255,0,0)"）.

        Returns:
            TextWidget: 支持链式调用.

        Raises:
            ValueError: 当颜色格式无效时.

        Examples:
            >>> widget = TextWidget().set_color("#ff0000")
            >>> widget = TextWidget().set_color("blue")
        """
        if not self._color_validator.validate(color):
            raise ValueError(
                f"颜色值验证失败: {self._color_validator.get_error_message(color)}"
            )

        self._color = color
        return self

    def set_line_height(self, height: str) -> "TextWidget":
        """设置行高.

        Args:
            height (str): CSS行高值（如 "1.5", "24px", "150%"）.

        Returns:
            TextWidget: 支持链式调用.

        Examples:
            >>> widget = TextWidget().set_line_height("1.8")
            >>> widget = TextWidget().set_line_height("28px")
        """
        self._line_height = height
        return self

    def set_font_weight(self, weight: str) -> "TextWidget":
        """设置字体粗细.

        Args:
            weight (str): CSS字体粗细值（如 "normal", "bold", "600"）.

        Returns:
            TextWidget: 支持链式调用.

        Examples:
            >>> widget = TextWidget().set_font_weight("bold")
            >>> widget = TextWidget().set_font_weight("600")
        """
        self._font_weight = weight
        return self

    def set_font_family(self, family: str) -> "TextWidget":
        """设置字体族.

        Args:
            family (str): CSS字体族字符串.

        Returns:
            TextWidget: 支持链式调用.

        Examples:
            >>> widget = TextWidget().set_font_family("Arial, sans-serif")
            >>> widget = TextWidget().set_font_family("'Microsoft YaHei', SimHei")
        """
        self._font_family = family
        return self

    def set_margin(self, margin: str) -> "TextWidget":
        """设置外边距.

        Args:
            margin (str): CSS外边距值（如 "16px 0", "10px", "1em 2em"）.

        Returns:
            TextWidget: 支持链式调用.

        Examples:
            >>> widget = TextWidget().set_margin("20px 0")
            >>> widget = TextWidget().set_margin("10px")
        """
        self._margin = margin
        return self

    def set_max_width(self, max_width: str) -> "TextWidget":
        """设置最大宽度.

        Args:
            max_width (str): CSS最大宽度值（如 "600px", "80%", "50em"）.

        Returns:
            TextWidget: 支持链式调用.

        Examples:
            >>> widget = TextWidget().set_max_width("600px")
            >>> widget = TextWidget().set_max_width("80%")
        """
        self._max_width = max_width
        return self

    def set_bold(self, bold: bool = True) -> "TextWidget":
        """设置是否为粗体.

        Args:
            bold (bool): 是否为粗体，默认为True.

        Returns:
            TextWidget: 支持链式调用.

        Examples:
            >>> widget = TextWidget().set_bold()  # 设置为粗体
            >>> widget = TextWidget().set_bold(False)  # 取消粗体
        """
        self._font_weight = "bold" if bold else "normal"
        return self

    def set_italic(self, italic: bool = True) -> "TextWidget":
        """设置是否为斜体.

        Args:
            italic: 是否为斜体，默认为True

        Returns:
            返回self以支持链式调用

        Note:
            当前版本暂未实现斜体功能，预留接口

        Examples:
            >>> widget = TextWidget().set_italic()  # 设置为斜体
        """
        # 这里可以扩展支持斜体样式
        return self

    @staticmethod
    def reset_section_numbers():
        """重置章节编号计数器.

        重置所有章节编号计数器，通常在开始新文档时调用.

        Examples:
            >>> TextWidget.reset_section_numbers()
            >>> # 之后创建的章节标题将从1开始编号
        """
        manager = SectionNumberManager()
        manager.reset()

    def _apply_type_styles(self) -> None:
        """根据文本类型应用预设样式.

        内部方法，当设置文本类型时自动调用.
        """
        if self._text_type == TextType.TITLE_LARGE:
            self._font_size = "28px"
            self._font_weight = "bold"
            self._color = "#323130"
            self._align = TextAlign.CENTER
            self._margin = "24px 0 16px 0"
        elif self._text_type == TextType.TITLE_SMALL:
            self._font_size = "20px"
            self._font_weight = "600"
            self._color = "#605e5c"
            self._align = TextAlign.CENTER
            self._margin = "20px 0 12px 0"
        elif self._text_type == TextType.BODY:
            self._font_size = "14px"
            self._font_weight = "normal"
            self._color = "#323130"
            self._align = TextAlign.LEFT
            self._margin = "16px 0"
        elif self._text_type == TextType.CAPTION:
            self._font_size = "12px"
            self._font_weight = "normal"
            self._color = "#8e8e93"
            self._align = TextAlign.LEFT
            self._margin = "8px 0"
        elif self._text_type == TextType.SECTION_H2:
            self._font_size = "24px"
            self._font_weight = "bold"
            self._color = "#323130"
            self._align = TextAlign.LEFT
            self._margin = "20px 0 12px 0"
            self._section_number = self._section_manager.get_next_number(2)
        elif self._text_type == TextType.SECTION_H3:
            self._font_size = "20px"
            self._font_weight = "600"
            self._color = "#323130"
            self._align = TextAlign.LEFT
            self._margin = "18px 0 10px 0"
            self._section_number = self._section_manager.get_next_number(3)
        elif self._text_type == TextType.SECTION_H4:
            self._font_size = "18px"
            self._font_weight = "600"
            self._color = "#323130"
            self._align = TextAlign.LEFT
            self._margin = "16px 0 8px 0"
            self._section_number = self._section_manager.get_next_number(4)
        elif self._text_type == TextType.SECTION_H5:
            self._font_size = "16px"
            self._font_weight = "500"
            self._color = "#323130"
            self._align = TextAlign.LEFT
            self._margin = "14px 0 6px 0"
            self._section_number = self._section_manager.get_next_number(5)

    @property
    def content(self) -> str:
        """获取当前文本内容.

        Returns:
            str: 当前的文本内容.
        """
        return self._content

    @property
    def font_size(self) -> str:
        """获取当前字体大小.

        Returns:
            str: 当前的字体大小CSS值.
        """
        return self._font_size

    @property
    def align(self) -> TextAlign:
        """获取当前对齐方式.

        Returns:
            TextAlign: 当前的对齐方式枚举值.
        """
        return self._align

    @property
    def color(self) -> str:
        """获取当前文本颜色.

        Returns:
            str: 当前的文本颜色CSS值.
        """
        return self._color

    def _get_template_name(self) -> str:
        """获取模板名称.

        Returns:
            模板文件名
        """
        return "text.html"

    def get_template_context(self) -> dict[str, Any]:
        """获取模板渲染所需的上下文数据.

        Returns:
            模板上下文数据字典
        """
        if not self._content:
            return {}

        # 构建样式
        style_parts = [
            f"font-size: {self._font_size}",
            f"text-align: {self._align.value}",
            f"color: {self._color}",
            f"line-height: {self._line_height}",
            f"font-weight: {self._font_weight}",
            f"font-family: {self._font_family}",
            f"margin: {self._margin}",
        ]

        if self._max_width:
            style_parts.append(f"max-width: {self._max_width}")

        # 确定HTML标签
        tag_name = "p"
        if self._text_type in [
            TextType.SECTION_H2,
            TextType.SECTION_H3,
            TextType.SECTION_H4,
            TextType.SECTION_H5,
        ]:
            tag_map = {
                TextType.SECTION_H2: "h2",
                TextType.SECTION_H3: "h3",
                TextType.SECTION_H4: "h4",
                TextType.SECTION_H5: "h5",
            }
            tag_name = tag_map.get(self._text_type, "p")

        return {
            "content": self._content,
            "content_lines": self._content.split("\n"),
            "section_number": self._section_number,
            "text_style": "; ".join(style_parts),
            "tag_name": tag_name,
        }
