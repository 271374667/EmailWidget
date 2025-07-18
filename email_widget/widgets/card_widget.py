"""Card Widget Implementation"""

from typing import Any

from email_widget.core.base import BaseWidget
from email_widget.core.enums import IconType, StatusType
from email_widget.core.validators import NonEmptyStringValidator, SizeValidator


class CardWidget(BaseWidget):
    """Create a content card for displaying information in a structured way.

    Cards are ideal for organizing and presenting information, commonly used for displaying data summaries, status updates, profiles, etc.
    They support titles, main content, icons, and one or more metadata entries.

    Attributes:
        title (Optional[str]): The card's title.
        content (str): The card's main content text.
        icon (Optional[str]): Icon displayed before the title, can be Emoji or other characters.
        metadata (Dict[str, str]): A key-value dictionary for displaying additional information at the bottom of the card.

    Examples:
        Create a card for displaying service status:

        ```python
        from email_widget.widgets import CardWidget

        card = CardWidget()
        card.set_title("API Service Monitoring")
        card.set_content("All services running normally, average response time 50ms.")
        card.set_icon("✅")
        card.add_metadata("Last Check Time", "2024-07-07 10:30:00")
        card.add_metadata("Uptime", "99.99%")

        # Using method chaining for more compact code:
        server_status_card = (CardWidget()\
                              .set_title("Database Server")\
                              .set_content("Connection normal, disk space sufficient.")\
                              .set_icon("🗄️")\
                              .set_metadata({
                                  "CPU Usage": "15%",
                                  "Memory Usage": "2.5 GB / 16 GB"
                              }))
        ```
    """

    # Template definition
    TEMPLATE = """
    {% if title or content %}
        <div style="{{ card_style }}">
            {% if title %}
                <h3 style="{{ title_style }}">
                    {% if icon %}{{ icon }} {% endif %}{{ title }}
                </h3>
            {% endif %}
            {% if content %}
                <div style="{{ content_style }}">{{ content }}</div>
            {% endif %}
            {% if metadata %}
                <div style="{{ metadata_container_style }}">
                    {% for key, value in metadata.items() %}
                        <div style="{{ metadata_item_style }}">
                            <strong>{{ key }}:</strong> {{ value }}
                        </div>
                    {% endfor %}
                </div>
            {% endif %}
        </div>
    {% endif %}
    """

    def __init__(self, widget_id: str | None = None):
        """Initialize CardWidget.

        Args:
            widget_id (Optional[str]): Optional Widget ID.
        """
        super().__init__(widget_id)
        self._title: str | None = None
        self._content: str = ""
        self._status: StatusType | None = None
        self._icon: str | None = IconType.INFO.value  # Default Info icon
        self._metadata: dict[str, str] = {}
        self._elevated: bool = True
        self._padding: str = "16px"
        self._border_radius: str = "4px"

        # Initialize validators
        self._text_validator = NonEmptyStringValidator()
        self._size_validator = SizeValidator()

    def set_title(self, title: str) -> "CardWidget":
        """Set the card's title.

        Args:
            title (str): Card title text.

        Returns:
            CardWidget: Returns self to support method chaining.

        Raises:
            ValueError: When title is empty.

        Examples:
            >>> card = CardWidget().set_title("System Status")
        """
        if not self._text_validator.validate(title):
            raise ValueError(
                f"Title validation failed: {self._text_validator.get_error_message(title)}"
            )

        self._title = title
        return self

    def set_content(self, content: str) -> "CardWidget":
        """Set the card's main content text.

        Args:
            content (str): Card content text.

        Returns:
            CardWidget: Returns self to support method chaining.

        Raises:
            ValueError: When content is empty.

        Examples:
            >>> card = CardWidget().set_content("All services running normally.")
        """
        if not self._text_validator.validate(content):
            raise ValueError(
                f"Content validation failed: {self._text_validator.get_error_message(content)}"
            )

        self._content = content
        return self

    def set_status(self, status: StatusType) -> "CardWidget":
        """Set the card's status.

        This status is typically used for internal logic or future visual indicators, currently does not directly affect card appearance.

        Args:
            status (StatusType): The card's status type.

        Returns:
            CardWidget: Returns self to support method chaining.

        Examples:
            >>> card = CardWidget().set_status(StatusType.SUCCESS)
        """
        self._status = status
        return self

    def set_icon(self, icon: str | IconType) -> "CardWidget":
        """Set the icon displayed before the title.

        The icon can be any string (such as Emoji characters) or `IconType` enumeration value.

        Args:
            icon (Union[str, IconType]): Icon string or `IconType` enumeration.

        Returns:
            CardWidget: Returns self to support method chaining.

        Examples:
            >>> card = CardWidget().set_icon("✅")
            >>> card = CardWidget().set_icon(IconType.DATA)
        """
        if isinstance(icon, IconType):
            self._icon = icon.value
        else:
            self._icon = icon
        return self

    def add_metadata(self, key: str, value: str) -> "CardWidget":
        """Add a metadata entry to the card.

        Metadata is displayed at the bottom of the card in key-value pairs.

        Args:
            key (str): The metadata item's key (name).
            value (str): The metadata item's value.

        Returns:
            CardWidget: Returns self to support method chaining.

        Examples:
            >>> card = CardWidget().add_metadata("Version", "1.0.0")
        """
        self._metadata[key] = value
        return self

    def set_metadata(self, metadata: dict[str, str]) -> "CardWidget":
        """Set all metadata for the card.

        This method will replace all existing metadata.

        Args:
            metadata (Dict[str, str]): Dictionary containing all metadata items.

        Returns:
            CardWidget: Returns self to support method chaining.

        Examples:
            >>> card = CardWidget().set_metadata({"CPU": "15%", "Memory": "60%"})
        """
        self._metadata = metadata.copy()
        return self

    def clear_metadata(self) -> "CardWidget":
        """Clear all metadata from the card.

        Returns:
            CardWidget: Returns self to support method chaining.

        Examples:
            >>> card = CardWidget().clear_metadata()
        """
        self._metadata.clear()
        return self

    def _get_template_name(self) -> str:
        return "card.html"

    def get_template_context(self) -> dict[str, Any]:
        """Get template context data required for rendering"""
        if not self._title and not self._content:
            return {}

        card_style = f"""
            background: #ffffff;
            border: 1px solid #e1dfdd;
            border-radius: {self._border_radius};
            padding: {self._padding};
            margin: 16px 0;
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
        """

        if self._elevated:
            card_style += " box-shadow: 0 2px 4px rgba(0,0,0,0.1);"

        title_style = (
            "font-size: 18px; font-weight: 600; color: #323130; margin-bottom: 8px;"
        )
        content_style = "color: #323130; line-height: 1.5; font-size: 14px;"
        metadata_container_style = (
            "margin-top: 12px; padding-top: 12px; border-top: 1px solid #e1dfdd;"
        )
        metadata_item_style = "margin: 4px 0; font-size: 13px;"

        return {
            "title": self._title,
            "content": self._content,
            "icon": self._icon,
            "metadata": self._metadata if self._metadata else None,
            "card_style": card_style,
            "title_style": title_style,
            "content_style": content_style,
            "metadata_container_style": metadata_container_style,
            "metadata_item_style": metadata_item_style,
        }
