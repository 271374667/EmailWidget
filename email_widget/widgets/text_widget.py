"""Text Widget Implementation

This module provides a text display widget that supports multiple text types and style settings.
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
    """Section number manager.

    This is a singleton class for managing section numbering in documents.
    Supports multi-level section numbering (H2-H5), automatically handling increments and resets.

    Attributes:
        _instance: Singleton instance
        _counters: Dictionary of counters for each level

    Examples:
        >>> manager = SectionNumberManager()
        >>> print(manager.get_next_number(2))  # "1."
        >>> print(manager.get_next_number(3))  # "1.1."
        >>> print(manager.get_next_number(2))  # "2."
        >>> manager.reset()  # Reset all counters
    """

    _instance = None
    _counters: dict[int, int] = {}  # level -> counter

    def __new__(cls):
        """Create singleton instance.

        Returns:
            The unique instance of SectionNumberManager
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._counters = {2: 0, 3: 0, 4: 0, 5: 0}
        return cls._instance

    def get_next_number(self, level: int) -> str:
        """Get the next section number for the specified level.

        Args:
            level: Section level (2-5, corresponding to H2-H5)

        Returns:
            Formatted section number string (e.g., "1.2.3.")

        Examples:
            >>> manager = SectionNumberManager()
            >>> manager.get_next_number(2)  # "1."
            >>> manager.get_next_number(3)  # "1.1."
            >>> manager.get_next_number(3)  # "1.2."
        """
        # Reset lower level counters
        for l in range(level + 1, 6):
            self._counters[l] = 0

        # Increment current level counter
        self._counters[level] += 1

        # Generate number string
        numbers = []
        for l in range(2, level + 1):
            if self._counters[l] > 0:
                numbers.append(str(self._counters[l]))

        return ".".join(numbers) + "."

    def reset(self):
        """Reset all section number counters.

        Examples:
            >>> manager = SectionNumberManager()
            >>> manager.get_next_number(2)  # "1."
            >>> manager.reset()
            >>> manager.get_next_number(2)  # "1." (restart)
        """
        self._counters = {2: 0, 3: 0, 4: 0, 5: 0}


class TextWidget(BaseWidget):
    """TextWidget is a component for displaying various types of text content, supporting multiple predefined text types and rich style configuration.

    This widget supports multiple text types (titles, body text, captions, section headings, etc.),
    and provides rich style setting options. Section headings automatically add numbering.

    Main features:
    - Support for multiple predefined text types
    - Custom fonts, colors, alignment and other styles
    - Automatic section numbering
    - Multi-line text support
    - Responsive design

    Attributes:
        _content (str): Text content.
        _text_type (TextType): Text type.
        _font_size (str): Font size.
        _align (TextAlign): Alignment.
        _color (str): Text color.
        _line_height (str): Line height.
        _font_weight (str): Font weight.
        _font_family (str): Font family.
        _margin (str): Margin.
        _max_width (Optional[str]): Maximum width.
        _section_number (Optional[str]): Section number.

    Examples:
        ```python
        from email_widget.widgets import TextWidget
        from email_widget.core.enums import TextType, TextAlign

        # Basic usage
        text = TextWidget().set_content("Hello World")

        # Method chaining
        title = (TextWidget()\
            .set_content("Important Title")\
            .set_type(TextType.TITLE_LARGE)\
            .set_color("#0078d4")\
            .set_align(TextAlign.CENTER))

        # Section heading (automatic numbering)
        section = TextWidget().set_content("Data Analysis").set_type(TextType.SECTION_H2)
        ```
    """

    # Template definition
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
        """Initialize TextWidget.

        Args:
            widget_id (Optional[str]): Optional widget ID.
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

        # Initialize validators
        self._color_validator = ColorValidator()
        self._size_validator = SizeValidator()
        self._content_validator = NonEmptyStringValidator()

    def set_content(self, content: str) -> "TextWidget":
        """Set text content, supports multi-line text (separated by `\n`).

        Args:
            content (str): Text content.

        Returns:
            TextWidget: Supports method chaining.

        Raises:
            ValueError: When content is an empty string.

        Examples:
            >>> widget = TextWidget().set_content("Hello World")
            >>> # Multi-line text
            >>> widget = TextWidget().set_content("Line 1\nLine 2\nLine 3")
        """
        if not self._content_validator.validate(content):
            raise ValueError(
                f"Text content validation failed: {self._content_validator.get_error_message(content)}"
            )

        self._content = content
        return self

    def set_type(self, text_type: TextType) -> "TextWidget":
        """Set text type, different types apply different preset styles.

        Args:
            text_type (TextType): Text type enum value.

        Returns:
            TextWidget: Supports method chaining.

        Examples:
            >>> widget = TextWidget().set_type(TextType.TITLE_LARGE)
            >>> widget = TextWidget().set_type(TextType.SECTION_H2)
        """
        self._text_type = text_type
        self._apply_type_styles()
        return self

    def set_font_size(self, size: str) -> "TextWidget":
        """Set font size.

        Args:
            size (str): CSS font size value (e.g., "16px", "1.2em", "120%").

        Returns:
            TextWidget: Supports method chaining.

        Raises:
            ValueError: When size format is invalid.

        Examples:
            >>> widget = TextWidget().set_font_size("18px")
            >>> widget = TextWidget().set_font_size("1.5em")
        """
        if not self._size_validator.validate(size):
            raise ValueError(
                f"Font size validation failed: {self._size_validator.get_error_message(size)}"
            )

        self._font_size = size
        return self

    def set_align(self, align: TextAlign) -> "TextWidget":
        """Set text alignment.

        Args:
            align (TextAlign): Alignment enum value.

        Returns:
            TextWidget: Supports method chaining.

        Examples:
            >>> widget = TextWidget().set_align(TextAlign.CENTER)
            >>> widget = TextWidget().set_align(TextAlign.RIGHT)
        """
        self._align = align
        return self

    def set_color(self, color: str) -> "TextWidget":
        """Set text color.

        Args:
            color (str): CSS color value (e.g., "#ff0000", "red", "rgb(255,0,0)").

        Returns:
            TextWidget: Supports method chaining.

        Raises:
            ValueError: When color format is invalid.

        Examples:
            >>> widget = TextWidget().set_color("#ff0000")
            >>> widget = TextWidget().set_color("blue")
        """
        if not self._color_validator.validate(color):
            raise ValueError(
                f"Color value validation failed: {self._color_validator.get_error_message(color)}"
            )

        self._color = color
        return self

    def set_line_height(self, height: str) -> "TextWidget":
        """Set line height.

        Args:
            height (str): CSS line height value (e.g., "1.5", "24px", "150%").

        Returns:
            TextWidget: Supports method chaining.

        Examples:
            >>> widget = TextWidget().set_line_height("1.8")
            >>> widget = TextWidget().set_line_height("28px")
        """
        self._line_height = height
        return self

    def set_font_weight(self, weight: str) -> "TextWidget":
        """Set font weight.

        Args:
            weight (str): CSS font weight value (e.g., "normal", "bold", "600").

        Returns:
            TextWidget: Supports method chaining.

        Examples:
            >>> widget = TextWidget().set_font_weight("bold")
            >>> widget = TextWidget().set_font_weight("600")
        """
        self._font_weight = weight
        return self

    def set_font_family(self, family: str) -> "TextWidget":
        """Set font family.

        Args:
            family (str): CSS font family string.

        Returns:
            TextWidget: Supports method chaining.

        Examples:
            >>> widget = TextWidget().set_font_family("Arial, sans-serif")
            >>> widget = TextWidget().set_font_family("'Microsoft YaHei', SimHei")
        """
        self._font_family = family
        return self

    def set_margin(self, margin: str) -> "TextWidget":
        """Set margin.

        Args:
            margin (str): CSS margin value (e.g., "16px 0", "10px", "1em 2em").

        Returns:
            TextWidget: Returns self to support method chaining.

        Examples:
            >>> widget = TextWidget().set_margin("20px 0")
            >>> widget = TextWidget().set_margin("10px")
        """
        self._margin = margin
        return self

    def set_max_width(self, max_width: str) -> "TextWidget":
        """Set maximum width.

        Args:
            max_width (str): CSS maximum width value (e.g., "600px", "80%", "50em").

        Returns:
            TextWidget: Returns self to support method chaining.

        Examples:
            >>> widget = TextWidget().set_max_width("600px")
            >>> widget = TextWidget().set_max_width("80%")
        """
        self._max_width = max_width
        return self

    def set_bold(self, bold: bool = True) -> "TextWidget":
        """Set whether text is bold.

        Args:
            bold (bool): Whether text is bold, defaults to True.

        Returns:
            TextWidget: Returns self to support method chaining.

        Examples:
            >>> widget = TextWidget().set_bold()  # Set to bold
            >>> widget = TextWidget().set_bold(False)  # Cancel bold
        """
        self._font_weight = "bold" if bold else "normal"
        return self

    def set_italic(self, italic: bool = True) -> "TextWidget":
        """Set whether text is italic.

        Args:
            italic: Whether text is italic, defaults to True

        Returns:
            Returns self to support method chaining

        Note:
            Current version has not implemented italic functionality, interface reserved

        Examples:
            >>> widget = TextWidget().set_italic()  # Set to italic
        """
        # Can extend to support italic styles here
        return self

    @staticmethod
    def reset_section_numbers():
        """Reset section number counters.

        Reset all section number counters, typically called when starting a new document.

        Examples:
            >>> TextWidget.reset_section_numbers()
            >>> # Section titles created afterwards will start numbering from 1
        """
        manager = SectionNumberManager()
        manager.reset()

    def _apply_type_styles(self) -> None:
        """Apply preset styles based on text type.

        Internal method, automatically called when setting text type.
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
        """Get current text content.

        Returns:
            str: Current text content.
        """
        return self._content

    @property
    def font_size(self) -> str:
        """Get current font size.

        Returns:
            str: Current font size CSS value.
        """
        return self._font_size

    @property
    def align(self) -> TextAlign:
        """Get current alignment.

        Returns:
            TextAlign: Current alignment enumeration value.
        """
        return self._align

    @property
    def color(self) -> str:
        """Get current text color.

        Returns:
            str: Current text color CSS value.
        """
        return self._color

    def _get_template_name(self) -> str:
        """Get template name.

        Returns:
            Template filename
        """
        return "text.html"

    def get_template_context(self) -> dict[str, Any]:
        """Get template context data required for rendering.

        Returns:
            Template context data dictionary
        """
        if not self._content:
            return {}

        # Build styles
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

        # Determine HTML tag
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
