"""Button Widget Implementation"""

from typing import Any

from email_widget.core.base import BaseWidget
from email_widget.core.validators import NonEmptyStringValidator, UrlValidator


class ButtonWidget(BaseWidget):
    """Create a beautiful button-style link.

    This widget is used to create button-style links in emails, mainly for guiding users to click and jump to specified pages.
    Supports custom button text, link address, colors and styles.

    Attributes:
        text (str): Text content displayed on the button.
        href (str): Link address to jump to after clicking the button.
        background_color (str): Background color of the button.
        text_color (str): Text color of the button.
        width (Optional[str]): Width of the button, can be pixel value or percentage.
        align (str): Alignment of the button (left, center, right).

    Examples:
        Create a basic button:

        ```python
        from email_widget.widgets import ButtonWidget

        # Create a simple button
        button = ButtonWidget()
        button.set_text("Click to View Details")
        button.set_href("https://example.com/details")

        # Use method chaining to create custom styled button
        button_custom = (ButtonWidget()
                        .set_text("Buy Now")
                        .set_href("https://shop.example.com")
                        .set_background_color("#22c55e")
                        .set_text_color("#ffffff")
                        .set_width("200px")
                        .set_align("center"))

        # Create fully configured button
        button_full = (ButtonWidget()
                      .set_full_button("Free Trial", "https://example.com/trial")
                      .set_padding("12px 24px")
                      .set_font_size("16px")
                      .set_border_radius("8px"))
        ```
    """

    # Template definition
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
        """Initialize ButtonWidget.

        Args:
            widget_id (Optional[str]): Optional Widget ID.
        """
        super().__init__(widget_id)
        self._text: str = ""
        self._href: str = ""
        self._background_color: str = "#3b82f6"  # Default blue
        self._text_color: str = "#ffffff"  # Default white
        self._width: str | None = None
        self._align: str = "left"
        self._padding: str = "10px 20px"
        self._border_radius: str = "6px"
        self._font_size: str = "14px"
        self._font_weight: str = "600"
        self._border: str | None = None

        # Initialize validators
        self._text_validator = NonEmptyStringValidator()
        self._url_validator = UrlValidator()

    def set_text(self, text: str) -> "ButtonWidget":
        """Set the text displayed on the button.

        Args:
            text (str): Button text content.

        Returns:
            ButtonWidget: Returns self to support method chaining.

        Raises:
            ValueError: When text is empty.

        Examples:
            >>> button = ButtonWidget().set_text("View More")
        """
        if not self._text_validator.validate(text):
            raise ValueError(
                f"Button text validation failed: {self._text_validator.get_error_message(text)}"
            )
        self._text = text
        return self

    def set_href(self, href: str) -> "ButtonWidget":
        """Set the button's link address.

        Args:
            href (str): Target link address.

        Returns:
            ButtonWidget: Returns self to support method chaining.

        Raises:
            ValueError: When link format is invalid.

        Examples:
            >>> button = ButtonWidget().set_href("https://example.com")
        """
        if not self._url_validator.validate(href):
            raise ValueError(
                f"Link address validation failed: {self._url_validator.get_error_message(href)}"
            )
        self._href = href
        return self

    def set_background_color(self, color: str) -> "ButtonWidget":
        """Set the button's background color.

        Args:
            color (str): Color value, supports hex format (e.g., #3b82f6) or color names.

        Returns:
            ButtonWidget: Returns self to support method chaining.

        Examples:
            >>> button = ButtonWidget().set_background_color("#22c55e")
        """
        self._background_color = color
        return self

    def set_text_color(self, color: str) -> "ButtonWidget":
        """Set the button text color.

        Args:
            color (str): Color value, supports hex format or color names.

        Returns:
            ButtonWidget: Returns self to support method chaining.

        Examples:
            >>> button = ButtonWidget().set_text_color("#ffffff")
        """
        self._text_color = color
        return self

    def set_width(self, width: str | None) -> "ButtonWidget":
        """Set the button width.

        Args:
            width (Optional[str]): Width value, can be pixel value (e.g., "200px") or percentage (e.g., "50%").
                                  If None, the button will adapt width based on content.

        Returns:
            ButtonWidget: Returns self to support method chaining.

        Examples:
            >>> button = ButtonWidget().set_width("200px")
            >>> button = ButtonWidget().set_width("100%")
        """
        self._width = width
        return self

    def set_align(self, align: str) -> "ButtonWidget":
        """Set the button alignment.

        Args:
            align (str): Alignment method, possible values: "left", "center", "right".

        Returns:
            ButtonWidget: Returns self to support method chaining.

        Raises:
            ValueError: When alignment method is invalid.

        Examples:
            >>> button = ButtonWidget().set_align("center")
        """
        valid_aligns = ["left", "center", "right"]
        if align not in valid_aligns:
            raise ValueError(f"Invalid alignment method: {align}. Valid values: {valid_aligns}")
        self._align = align
        return self

    def set_padding(self, padding: str) -> "ButtonWidget":
        """Set the button padding.

        Args:
            padding (str): Padding value, e.g., "10px 20px".

        Returns:
            ButtonWidget: Returns self to support method chaining.

        Examples:
            >>> button = ButtonWidget().set_padding("12px 24px")
        """
        self._padding = padding
        return self

    def set_border_radius(self, radius: str) -> "ButtonWidget":
        """Set the button border radius.

        Args:
            radius (str): Border radius value, e.g., "6px".

        Returns:
            ButtonWidget: Returns self to support method chaining.

        Examples:
            >>> button = ButtonWidget().set_border_radius("8px")
        """
        self._border_radius = radius
        return self

    def set_font_size(self, size: str) -> "ButtonWidget":
        """Set the button text font size.

        Args:
            size (str): Font size, e.g., "16px".

        Returns:
            ButtonWidget: Returns self to support method chaining.

        Examples:
            >>> button = ButtonWidget().set_font_size("16px")
        """
        self._font_size = size
        return self

    def set_font_weight(self, weight: str) -> "ButtonWidget":
        """Set the button text font weight.

        Args:
            weight (str): Font weight, e.g., "normal", "600", "bold".

        Returns:
            ButtonWidget: Returns self to support method chaining.

        Examples:
            >>> button = ButtonWidget().set_font_weight("bold")
        """
        self._font_weight = weight
        return self

    def set_border(self, border: str | None) -> "ButtonWidget":
        """Set the button border style.

        Args:
            border (Optional[str]): Border style, e.g., "2px solid #3b82f6". If None, no border.

        Returns:
            ButtonWidget: Returns self to support method chaining.

        Examples:
            >>> button = ButtonWidget().set_border("2px solid #3b82f6")
        """
        self._border = border
        return self

    def set_full_button(
        self, text: str, href: str, background_color: str | None = None
    ) -> "ButtonWidget":
        """Set button basic information at once.

        Args:
            text (str): Button text.
            href (str): Link address.
            background_color (Optional[str]): Optional background color.

        Returns:
            ButtonWidget: Returns self to support method chaining.

        Examples:
            >>> button = ButtonWidget().set_full_button("Start Now", "https://example.com", "#22c55e")
        """
        self.set_text(text)
        self.set_href(href)
        if background_color:
            self.set_background_color(background_color)
        return self

    def _get_template_name(self) -> str:
        return "button.html"

    def get_template_context(self) -> dict[str, Any]:
        """Get template context data required for rendering"""
        if not self._text or not self._href:
            return {}

        # Build button style
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
