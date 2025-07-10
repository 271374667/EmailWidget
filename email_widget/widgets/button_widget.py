"""按钮Widget实现"""

from typing import Any

from email_widget.core.base import BaseWidget
from email_widget.core.validators import NonEmptyStringValidator, UrlValidator


class ButtonWidget(BaseWidget):
    """创建一个美观的按钮样式链接。

    该微件用于在邮件中创建按钮样式的链接，主要用于引导用户点击跳转到指定页面。
    支持自定义按钮文本、链接地址、颜色和样式。

    Attributes:
        text (str): 按钮显示的文本内容。
        href (str): 点击按钮后跳转的链接地址。
        background_color (str): 按钮的背景颜色。
        text_color (str): 按钮文字的颜色。
        width (Optional[str]): 按钮的宽度，可以是像素值或百分比。
        align (str): 按钮的对齐方式（left, center, right）。

    Examples:
        创建一个基本的按钮：

        ```python
        from email_widget.widgets import ButtonWidget

        # 创建一个简单的按钮
        button = ButtonWidget()
        button.set_text("点击查看详情")
        button.set_href("https://example.com/details")

        # 使用链式调用创建自定义样式的按钮
        button_custom = (ButtonWidget()
                        .set_text("立即购买")
                        .set_href("https://shop.example.com")
                        .set_background_color("#22c55e")
                        .set_text_color("#ffffff")
                        .set_width("200px")
                        .set_align("center"))

        # 创建完整配置的按钮
        button_full = (ButtonWidget()
                      .set_full_button("免费试用", "https://example.com/trial")
                      .set_padding("12px 24px")
                      .set_font_size("16px")
                      .set_border_radius("8px"))
        ```
    """

    # 模板定义
    TEMPLATE = """
    {% if text and href %}
        <div style="margin: 8px 0; text-align: {{ align }}; width: 100%;">
            <a href="{{ href }}" 
               style="{{ button_style }}"
               target="_blank">{{ text }}</a>
        </div>
    {% endif %}
    """

    def __init__(self, widget_id: str | None = None):
        """初始化ButtonWidget。

        Args:
            widget_id (Optional[str]): 可选的Widget ID。
        """
        super().__init__(widget_id)
        self._text: str = ""
        self._href: str = ""
        self._background_color: str = "#3b82f6"  # 默认蓝色
        self._text_color: str = "#ffffff"  # 默认白色
        self._width: str | None = None
        self._align: str = "left"
        self._padding: str = "10px 20px"
        self._border_radius: str = "6px"
        self._font_size: str = "14px"
        self._font_weight: str = "600"
        self._border: str | None = None

        # 初始化验证器
        self._text_validator = NonEmptyStringValidator()
        self._url_validator = UrlValidator()

    def set_text(self, text: str) -> "ButtonWidget":
        """设置按钮显示的文本。

        Args:
            text (str): 按钮文本内容。

        Returns:
            ButtonWidget: 返回self以支持链式调用。

        Raises:
            ValueError: 当文本为空时。

        Examples:
            >>> button = ButtonWidget().set_text("查看更多")
        """
        if not self._text_validator.validate(text):
            raise ValueError(
                f"按钮文本验证失败: {self._text_validator.get_error_message(text)}"
            )
        self._text = text
        return self

    def set_href(self, href: str) -> "ButtonWidget":
        """设置按钮的链接地址。

        Args:
            href (str): 目标链接地址。

        Returns:
            ButtonWidget: 返回self以支持链式调用。

        Raises:
            ValueError: 当链接格式无效时。

        Examples:
            >>> button = ButtonWidget().set_href("https://example.com")
        """
        if not self._url_validator.validate(href):
            raise ValueError(
                f"链接地址验证失败: {self._url_validator.get_error_message(href)}"
            )
        self._href = href
        return self

    def set_background_color(self, color: str) -> "ButtonWidget":
        """设置按钮的背景颜色。

        Args:
            color (str): 颜色值，支持hex格式（如#3b82f6）或颜色名称。

        Returns:
            ButtonWidget: 返回self以支持链式调用。

        Examples:
            >>> button = ButtonWidget().set_background_color("#22c55e")
        """
        self._background_color = color
        return self

    def set_text_color(self, color: str) -> "ButtonWidget":
        """设置按钮文字的颜色。

        Args:
            color (str): 颜色值，支持hex格式或颜色名称。

        Returns:
            ButtonWidget: 返回self以支持链式调用。

        Examples:
            >>> button = ButtonWidget().set_text_color("#ffffff")
        """
        self._text_color = color
        return self

    def set_width(self, width: str | None) -> "ButtonWidget":
        """设置按钮的宽度。

        Args:
            width (Optional[str]): 宽度值，可以是像素值（如"200px"）或百分比（如"50%"）。
                                  如果为None，按钮将根据内容自适应宽度。

        Returns:
            ButtonWidget: 返回self以支持链式调用。

        Examples:
            >>> button = ButtonWidget().set_width("200px")
            >>> button = ButtonWidget().set_width("100%")
        """
        self._width = width
        return self

    def set_align(self, align: str) -> "ButtonWidget":
        """设置按钮的对齐方式。

        Args:
            align (str): 对齐方式，可选值: "left", "center", "right"。

        Returns:
            ButtonWidget: 返回self以支持链式调用。

        Raises:
            ValueError: 当对齐方式无效时。

        Examples:
            >>> button = ButtonWidget().set_align("center")
        """
        valid_aligns = ["left", "center", "right"]
        if align not in valid_aligns:
            raise ValueError(f"无效的对齐方式: {align}。可选值: {valid_aligns}")
        self._align = align
        return self

    def set_padding(self, padding: str) -> "ButtonWidget":
        """设置按钮的内边距。

        Args:
            padding (str): 内边距值，如"10px 20px"。

        Returns:
            ButtonWidget: 返回self以支持链式调用。

        Examples:
            >>> button = ButtonWidget().set_padding("12px 24px")
        """
        self._padding = padding
        return self

    def set_border_radius(self, radius: str) -> "ButtonWidget":
        """设置按钮的圆角半径。

        Args:
            radius (str): 圆角半径值，如"6px"。

        Returns:
            ButtonWidget: 返回self以支持链式调用。

        Examples:
            >>> button = ButtonWidget().set_border_radius("8px")
        """
        self._border_radius = radius
        return self

    def set_font_size(self, size: str) -> "ButtonWidget":
        """设置按钮文字的字体大小。

        Args:
            size (str): 字体大小，如"16px"。

        Returns:
            ButtonWidget: 返回self以支持链式调用。

        Examples:
            >>> button = ButtonWidget().set_font_size("16px")
        """
        self._font_size = size
        return self

    def set_font_weight(self, weight: str) -> "ButtonWidget":
        """设置按钮文字的字体粗细。

        Args:
            weight (str): 字体粗细，如"normal", "600", "bold"。

        Returns:
            ButtonWidget: 返回self以支持链式调用。

        Examples:
            >>> button = ButtonWidget().set_font_weight("bold")
        """
        self._font_weight = weight
        return self

    def set_border(self, border: str | None) -> "ButtonWidget":
        """设置按钮的边框样式。

        Args:
            border (Optional[str]): 边框样式，如"2px solid #3b82f6"。如果为None，则无边框。

        Returns:
            ButtonWidget: 返回self以支持链式调用。

        Examples:
            >>> button = ButtonWidget().set_border("2px solid #3b82f6")
        """
        self._border = border
        return self

    def set_full_button(
        self, text: str, href: str, background_color: str | None = None
    ) -> "ButtonWidget":
        """一次性设置按钮的基本信息。

        Args:
            text (str): 按钮文本。
            href (str): 链接地址。
            background_color (Optional[str]): 可选的背景颜色。

        Returns:
            ButtonWidget: 返回self以支持链式调用。

        Examples:
            >>> button = ButtonWidget().set_full_button("立即开始", "https://example.com", "#22c55e")
        """
        self.set_text(text)
        self.set_href(href)
        if background_color:
            self.set_background_color(background_color)
        return self

    def _get_template_name(self) -> str:
        return "button.html"

    def get_template_context(self) -> dict[str, Any]:
        """获取模板渲染所需的上下文数据"""
        if not self._text or not self._href:
            return {}

        # 构建按钮样式
        button_style_parts = [
            "display: inline-block",
            f"background-color: {self._background_color}",
            f"color: {self._text_color}",
            f"padding: {self._padding}",
            f"border-radius: {self._border_radius}",
            "text-decoration: none",
            f"font-size: {self._font_size}",
            f"font-weight: {self._font_weight}",
            "font-family: 'Segoe UI', Tahoma, Arial, sans-serif",
            "text-align: center",
            "cursor: pointer",
        ]

        if self._width:
            button_style_parts.append(f"width: {self._width}")
            button_style_parts.append("box-sizing: border-box")

        if self._border:
            button_style_parts.append(f"border: {self._border}")
        else:
            button_style_parts.append("border: none")

        button_style = "; ".join(button_style_parts)

        return {
            "text": self._text,
            "href": self._href,
            "button_style": button_style,
            "align": self._align,
        }
