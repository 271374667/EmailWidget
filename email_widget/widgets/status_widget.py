"""Status Information Widget Implementation"""

from typing import Any

from email_widget.core.base import BaseWidget
from email_widget.core.enums import LayoutType, StatusType


class StatusItem:
    """Data structure representing a single status item.

    Each status item contains a label (description), a value, and an optional status type,
    used for display in `StatusWidget`.

    Attributes:
        label (str): Descriptive label for the status item.
        value (str): Actual value of the status item.
        status (Optional[StatusType]): Type of the status item, used to determine the color of the value.

    Examples:
        ```python
        from email_widget.widgets import StatusItem
        from email_widget.core.enums import StatusType

        # Create a success status CPU usage item
        cpu_status = StatusItem("CPU Usage", "15%", StatusType.SUCCESS)

        # Create a regular info item
        uptime_info = StatusItem("System Uptime", "30 days")
        ```
    """

    def __init__(self, label: str, value: str, status: StatusType | None = None):
        """Initialize StatusItem.

        Args:
            label (str): Descriptive label for the status item.
            value (str): Actual value of the status item.
            status (Optional[StatusType]): Type of the status item, used to determine the color of the value.
        """
        self.label = label
        self.value = value
        self.status = status


class StatusWidget(BaseWidget):
    """Create a list for displaying key-value pair status information.

    This widget is very suitable for displaying system monitoring metrics, service status, configuration parameters, and other
    structured data. Each item consists of a label and a value, and can display different colors based on status (such as success, warning, error).

    Core features:
        - **Key-value pair list**: Display multiple status items in a clear list format.
        - **Layout switching**: Support both vertical (default) and horizontal layout modes.
        - **Status coloring**: Can set different colors for each status item value to visually reflect its status.
        - **Dynamic management**: Support adding, updating, or removing status items at runtime.

    Attributes:
        items (List[StatusItem]): List containing all status items.
        title (Optional[str]): Title of the entire status list.
        layout (LayoutType): Layout mode of the list (vertical or horizontal).

    Examples:
        Create a vertical layout system monitoring status list:

        ```python
        from email_widget.widgets import StatusWidget
        from email_widget.core.enums import StatusType, LayoutType

        system_monitor = (StatusWidget()\
                          .set_title("System Health Check")\
                          .set_layout(LayoutType.VERTICAL)\
                          .add_status_item("CPU Usage", "15%", StatusType.SUCCESS)\
                          .add_status_item("Memory Usage", "78%", StatusType.WARNING)\
                          .add_status_item("Disk Space", "95%", StatusType.ERROR)\
                          .add_status_item("Uptime", "32 days"))

        # Assuming email is an Email object
        # email.add_widget(system_monitor)
        ```

        Create a horizontal layout service status list:

        ```python
        service_status = (StatusWidget()\
                          .set_title("Microservice Status")\
                          .set_layout(LayoutType.HORIZONTAL)\
                          .add_status_item("Authentication Service", "Online", StatusType.SUCCESS)\
                          .add_status_item("Payment Service", "Offline", StatusType.ERROR))
        ```
    """

    # Template definition
    TEMPLATE = """
    {% if items %}
        <!--[if mso]>
        <table width="100%" cellpadding="0" cellspacing="0" border="0">
            <tr>
                <td>
        <![endif]-->
        <div style="{{ container_style }}">
            {% if title %}
                <h3 style="{{ title_style }}">{{ title }}</h3>
            {% endif %}
            {% for item in items %}
                <div style="{{ item.item_style }}">
                    {% if layout == 'horizontal' %}
                        <span style="{{ item.label_style }}">{{ item.label }}</span>
                        <span style="{{ item.value_style }}">{{ item.value }}</span>
                    {% else %}
                        <div style="{{ item.label_style }}">{{ item.label }}</div>
                        <div style="{{ item.value_style }}">{{ item.value }}</div>
                    {% endif %}
                </div>
            {% endfor %}
        </div>
        <!--[if mso]>
                </td>
            </tr>
        </table>
        <![endif]-->
    {% endif %}
    """

    def __init__(self, widget_id: str | None = None):
        """Initialize StatusWidget.

        Args:
            widget_id (Optional[str]): Optional Widget ID.
        """
        super().__init__(widget_id)
        self._items: list[StatusItem] = []
        self._title: str | None = None
        self._layout: LayoutType = LayoutType.VERTICAL

    def add_status_item(
        self, label: str, value: str, status: StatusType | None = None
    ) -> "StatusWidget":
        """Add a status item to the list.

        Args:
            label (str): Descriptive label for the status item.
            value (str): Actual value of the status item.
            status (Optional[StatusType]): Type of the status item, used to determine the color of the value.

        Returns:
            StatusWidget: Returns self to support method chaining.

        Examples:
            >>> widget = StatusWidget().add_status_item("Service Status", "Running", StatusType.SUCCESS)
        """
        self._items.append(StatusItem(label, value, status))
        return self

    def set_title(self, title: str) -> "StatusWidget":
        """Set the title of the status list.

        Args:
            title (str): Title text.

        Returns:
            StatusWidget: Returns self to support method chaining.

        Examples:
            >>> widget = StatusWidget().set_title("Server Health Status")
        """
        self._title = title
        return self

    def set_layout(self, layout: LayoutType) -> "StatusWidget":
        """Set the layout mode of status items.

        Args:
            layout (LayoutType): Layout type, can be `LayoutType.VERTICAL` or `LayoutType.HORIZONTAL`.

        Returns:
            StatusWidget: Returns self to support method chaining.

        Examples:
            >>> widget = StatusWidget().set_layout(LayoutType.HORIZONTAL)
        """
        self._layout = layout
        return self

    def clear_items(self) -> "StatusWidget":
        """Clear all status items.

        Returns:
            StatusWidget: Returns self to support method chaining.

        Examples:
            >>> widget = StatusWidget().clear_items()
        """
        self._items.clear()
        return self

    def remove_item(self, label: str) -> "StatusWidget":
        """Remove specified status item by label.

        Args:
            label (str): Label of the status item to remove.

        Returns:
            StatusWidget: Returns self to support method chaining.

        Examples:
            >>> widget = StatusWidget().remove_item("CPU Usage")
        """
        self._items = [item for item in self._items if item.label != label]
        return self

    def update_item(
        self, label: str, value: str, status: StatusType = None
    ) -> "StatusWidget":
        """Update value and status of the status item with specified label.

        If a matching label is found, update its value and status; otherwise, do nothing.

        Args:
            label (str): Label of the status item to update.
            value (str): New value.
            status (StatusType): Optional new status type.

        Returns:
            StatusWidget: Returns self to support method chaining.

        Examples:
            >>> widget = StatusWidget().update_item("CPU Usage", "20%", StatusType.WARNING)
        """
        for item in self._items:
            if item.label == label:
                item.value = value
                if status:
                    item.status = status
                break
        return self

    def get_item_count(self) -> int:
        """Get the count of current status items.

        Returns:
            int: Number of status items.

        Examples:
            >>> count = StatusWidget().add_status_item("A", "1").get_item_count()
            >>> print(count) # Output: 1
        """
        return len(self._items)

    def _get_status_color(self, status: StatusType) -> str:
        """Get status color"""
        colors = {
            StatusType.SUCCESS: "#107c10",
            StatusType.WARNING: "#ff8c00",
            StatusType.ERROR: "#d13438",
            StatusType.INFO: "#0078d4",
            StatusType.PRIMARY: "#0078d4",
        }
        return colors[status]

    def _get_template_name(self) -> str:
        return "status_info.html"

    def get_template_context(self) -> dict[str, Any]:
        """Get template context data required for rendering"""
        if not self._items:
            return {}

        container_style = """
            background: #ffffff;
            border: 1px solid #e1dfdd;
            border-radius: 4px;
            padding: 16px;
            margin: 16px 0;
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
        """

        title_style = (
            "font-size: 16px; font-weight: 600; color: #323130; margin-bottom: 12px;"
        )

        # Process status items
        items_data = []
        for item in self._items:
            if self._layout == LayoutType.HORIZONTAL:
                item_style = """
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin: 8px 0;
                    padding: 8px 0;
                    border-bottom: 1px solid #f3f2f1;
                """
            else:
                item_style = (
                    "margin: 8px 0; padding: 8px 0; border-bottom: 1px solid #f3f2f1;"
                )

            label_style = "font-weight: 500; color: #605e5c; font-size: 14px;"
            value_style = "color: #323130; font-size: 14px;"

            if item.status:
                status_color = self._get_status_color(item.status)
                value_style += f" color: {status_color}; font-weight: 600;"

            items_data.append(
                {
                    "label": item.label,
                    "value": item.value,
                    "item_style": item_style,
                    "label_style": label_style,
                    "value_style": value_style,
                }
            )

        return {
            "items": items_data,
            "title": self._title,
            "layout": "horizontal"
            if self._layout == LayoutType.HORIZONTAL
            else "vertical",
            "container_style": container_style,
            "title_style": title_style,
        }
