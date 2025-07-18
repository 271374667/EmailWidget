"""Alert Widget Implementation"""

from typing import Any

from email_widget.core.base import BaseWidget
from email_widget.core.enums import AlertType
from email_widget.core.validators import NonEmptyStringValidator, SizeValidator


class AlertWidget(BaseWidget):
    """Create a GitHub-style alert box (Admonition).

    This widget is used to highlight specific information in emails, such as notes, tips, warnings, or important reminders.
    It supports multiple preset alert types, each with unique colors and icons to attract reader attention.

    Attributes:
        content (str): Main text content displayed in the alert box.
        alert_type (AlertType): Type of alert, determines its appearance (color and icon).
        title (Optional[str]): Custom title for the alert box. If not set, will use default title based on `alert_type`.

    Examples:
        Basic usage, creating a warning type alert box:

        ```python
        from email_widget.widgets import AlertWidget
        from email_widget.core.enums import AlertType

        alert = AlertWidget()
        alert.set_content("System will undergo maintenance in 5 minutes, please save your work in time.")
        alert.set_alert_type(AlertType.WARNING)
        alert.set_title("System Maintenance Notice")

        # You can also use method chaining to simplify code:
        alert_chained = (AlertWidget()
                         .set_content("New features are online, go experience them!")
                         .set_alert_type(AlertType.TIP)
                         .set_title("Product Update")
                         .set_icon("🎉"))
        ```
    """

    # Template definition
    TEMPLATE = """
    {% if content %}
        <div style="{{ container_style }}">
            <!-- Title row -->
            {% if show_icon %}
                <div style="display: flex; align-items: center; margin-bottom: 8px; font-weight: 600; font-size: 16px;">
                    <span style="margin-right: 8px; font-size: 18px;">{{ icon }}</span>
                    <span>{{ title }}</span>
                </div>
            {% else %}
                <div style="margin-bottom: 8px; font-weight: 600; font-size: 16px;">{{ title }}</div>
            {% endif %}
            
            <!-- Content -->
            <div style="line-height: 1.5; font-size: 14px;">{{ content }}</div>
        </div>
    {% endif %}
    """

    def __init__(self, widget_id: str | None = None):
        """Initialize AlertWidget.

        Args:
            widget_id (Optional[str]): Optional Widget ID.
        """
        super().__init__(widget_id)
        self._content: str = ""
        self._alert_type: AlertType = AlertType.NOTE
        self._title: str | None = None
        self._icon: str | None = None
        self._show_icon: bool = True
        self._border_radius: str = "6px"
        self._padding: str = "16px"

        # Initialize validators
        self._content_validator = NonEmptyStringValidator()
        self._size_validator = SizeValidator()

    def set_content(self, content: str) -> "AlertWidget":
        """Set the main text content displayed in the alert box.

        Args:
            content (str): Alert content.

        Returns:
            AlertWidget: Returns self to support method chaining.

        Raises:
            ValueError: When content is empty.

        Examples:
            >>> alert = AlertWidget().set_content("This is an important notice.")
        """
        if not self._content_validator.validate(content):
            raise ValueError(
                f"Alert content validation failed: {self._content_validator.get_error_message(content)}"
            )

        self._content = content
        return self

    def set_alert_type(self, alert_type: AlertType) -> "AlertWidget":
        """Set the alert type.

        Different alert types will apply different colors and icons.

        Args:
            alert_type (AlertType): Alert type enumeration value.

        Returns:
            AlertWidget: Returns self to support method chaining.

        Examples:
            >>> alert = AlertWidget().set_alert_type(AlertType.WARNING)
        """
        self._alert_type = alert_type
        return self

    def set_title(self, title: str) -> "AlertWidget":
        """Set the alert box custom title.

        If not set, will use the default title based on `alert_type`.

        Args:
            title (str): Custom title text.

        Returns:
            AlertWidget: Returns self to support method chaining.

        Examples:
            >>> alert = AlertWidget().set_title("Important Notice")
        """
        self._title = title
        return self

    def set_full_alert(
        self, content: str, alert_type: AlertType, title: str = None
    ) -> "AlertWidget":
        """Set complete alert information at once.

        This method allows setting alert content, type, and optional title simultaneously for convenient quick configuration.

        Args:
            content (str): Alert content.
            alert_type (AlertType): Alert type.
            title (str): Optional custom title.

        Returns:
            AlertWidget: Returns self to support method chaining.

        Examples:
            >>> alert = AlertWidget().set_full_alert("Operation successful!", AlertType.TIP, "Complete")
        """
        self._content = content
        self._alert_type = alert_type
        if title:
            self._title = title
        return self

    def clear_title(self) -> "AlertWidget":
        """Clear the alert box custom title.

        After calling this method, the alert box will display the default title based on `alert_type`.

        Returns:
            AlertWidget: Returns self to support method chaining.

        Examples:
            >>> alert = AlertWidget().set_title("Custom Title").clear_title()
        """
        self._title = None
        return self

    def set_icon(self, icon: str) -> "AlertWidget":
        """Set the alert box custom icon.

        Args:
            icon (str): Icon character (such as emoji or Unicode character).

        Returns:
            AlertWidget: Returns self to support method chaining.

        Examples:
            >>> alert = AlertWidget().set_icon("🚀")
        """
        self._icon = icon
        return self

    def show_icon(self, show: bool = True) -> "AlertWidget":
        """Set whether to display the alert box icon.

        Args:
            show (bool): Whether to show the icon, defaults to True.

        Returns:
            AlertWidget: Returns self to support method chaining.

        Examples:
            >>> alert = AlertWidget().show_icon(False)  # Hide icon
        """
        self._show_icon = show
        return self

    def _get_default_title(self) -> str:
        """Get default title"""
        titles = {
            AlertType.NOTE: "Note",
            AlertType.TIP: "Tip",
            AlertType.IMPORTANT: "Important",
            AlertType.WARNING: "Warning",
            AlertType.CAUTION: "Caution",
        }
        return titles[self._alert_type]

    def _get_default_icon(self) -> str:
        """Get default icon"""
        icons = {
            AlertType.NOTE: "ℹ️",
            AlertType.TIP: "💡",
            AlertType.IMPORTANT: "❗",
            AlertType.WARNING: "⚠️",
            AlertType.CAUTION: "🚨",
        }
        return icons[self._alert_type]

    def _get_alert_styles(self) -> dict[str, str]:
        """Get alert box styles"""
        styles = {
            AlertType.NOTE: {
                "background": "#dbeafe",
                "border": "#3b82f6",
                "color": "#1e40af",
            },
            AlertType.TIP: {
                "background": "#dcfce7",
                "border": "#22c55e",
                "color": "#15803d",
            },
            AlertType.IMPORTANT: {
                "background": "#fef3c7",
                "border": "#f59e0b",
                "color": "#d97706",
            },
            AlertType.WARNING: {
                "background": "#fed7aa",
                "border": "#f97316",
                "color": "#ea580c",
            },
            AlertType.CAUTION: {
                "background": "#fecaca",
                "border": "#ef4444",
                "color": "#dc2626",
            },
        }
        return styles[self._alert_type]

    def _get_template_name(self) -> str:
        return "alert.html"

    def get_template_context(self) -> dict[str, Any]:
        """Get template context data required for rendering"""
        if not self._content:
            return {}

        styles = self._get_alert_styles()
        title = self._title or self._get_default_title()
        icon = self._icon or self._get_default_icon()

        container_style = f"""
            background: {styles["background"]};
            border: 1px solid {styles["border"]};
            border-left: 4px solid {styles["border"]};
            border-radius: {self._border_radius};
            padding: {self._padding};
            margin: 16px 0;
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
            color: {styles["color"]};
        """

        return {
            "content": self._content,
            "container_style": container_style,
            "show_icon": self._show_icon,
            "title": title,
            "icon": icon,
        }
