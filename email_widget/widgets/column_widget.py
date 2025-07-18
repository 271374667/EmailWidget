"""Column Layout Widget Implementation"""

from typing import Any

from email_widget.core.base import BaseWidget


class ColumnWidget(BaseWidget):
    """Create a multi-column layout container for horizontally arranging multiple widgets.

    This widget uses `<table>` elements to ensure maximum compatibility across various email clients.
    You can place any other widgets (such as `TextWidget`, `CardWidget`, `ChartWidget`, etc.)
    in the column layout to create complex and beautiful email layouts.

    Core features:
        - **Auto columns**: By default, it intelligently calculates the optimal number of columns based on the number of internal widgets.
        - **Manual columns**: You can also manually specify a fixed number of columns between 1 and 4.
        - **Responsive**: Layout automatically adjusts based on screen width, ensuring good experience on both desktop and mobile devices.
        - **Spacing control**: Can customize horizontal spacing between columns.

    Auto column rules:
        - 1 widget: 1 column
        - 2 widgets: 2 columns
        - 3 widgets: 3 columns
        - 4 widgets: 2 columns (2x2 grid)
        - 5-6 widgets: 3 columns
        - 7-8 widgets: 2 columns
        - 9+ widgets: 3 columns

    Examples:
        Create a two-column layout with a card on the left and chart on the right:

        ```python
        from email_widget.widgets import ColumnWidget, CardWidget, ChartWidget
        import matplotlib.pyplot as plt

        # Prepare left card
        left_card = (CardWidget()
                     .set_title("Key Metrics")
                     .add_metadata("User Growth", "+15%")
                     .add_metadata("Revenue", "+12%"))

        # Prepare right chart
        plt.figure()
        plt.plot([1, 2, 3], [4, 5, 2])
        right_chart = ChartWidget().set_chart(plt)

        # Create 2-column layout and add widgets
        two_column_layout = (ColumnWidget()
                             .set_columns(2)
                             .set_gap("24px")
                             .add_widget(left_card)
                             .add_widget(right_chart))

        # Assuming email is an Email object
        # email.add_widget(two_column_layout)
        ```
    """

    # 模板定义
    TEMPLATE = """
    {% if widget_groups %}
        <!--[if mso]>
        <table width="100%" cellpadding="0" cellspacing="0" border="0">
            <tr>
                <td>
        <![endif]-->
        <table cellpadding="0" cellspacing="0" border="0" style="{{ table_style }}">
            {% for group in widget_groups %}
                <tr>
                    {% for widget_html in group %}
                        <td style="{{ cell_style }}">{{ widget_html }}</td>
                    {% endfor %}
                    {% for _ in range(empty_columns) %}
                        <td style="{{ empty_cell_style }}"></td>
                    {% endfor %}
                </tr>
            {% endfor %}
        </table>
        <!--[if mso]>
                </td>
            </tr>
        </table>
        <![endif]-->
    {% endif %}
    """

    def __init__(self, widget_id: str | None = None):
        """Initialize ColumnWidget.

        Args:
            widget_id (Optional[str]): Optional Widget ID.
        """
        super().__init__(widget_id)
        self._widgets: list[BaseWidget] = []
        self._columns: int = -1  # -1表示自动模式
        self._gap: str = "20px"

    def add_widget(self, widget: BaseWidget) -> "ColumnWidget":
        """Add a widget to the column layout.

        Args:
            widget (BaseWidget): Widget instance to add.

        Returns:
            ColumnWidget: Returns self to support method chaining.

        Examples:
            >>> column = ColumnWidget().add_widget(TextWidget().set_content("Left content"))
        """
        self._widgets.append(widget)
        return self

    def add_widgets(self, widgets: list[BaseWidget]) -> "ColumnWidget":
        """Add multiple widgets to the column layout.

        Args:
            widgets (List[BaseWidget]): List of widget instances to add.

        Returns:
            ColumnWidget: Returns self to support method chaining.

        Examples:
            >>> column = ColumnWidget().add_widgets([TextWidget(), ImageWidget()])
        """
        self._widgets.extend(widgets)
        return self

    def set_columns(self, columns: int) -> "ColumnWidget":
        """Set the number of columns in the layout.

        Args:
            columns (int): Number of columns. -1 indicates auto mode, other values are limited between 1 and 4 columns.

        Returns:
            ColumnWidget: Returns self to support method chaining.

        Examples:
            >>> column = ColumnWidget().set_columns(2) # Set to 2 columns
            >>> column = ColumnWidget().set_columns(-1) # Auto mode
        """
        if columns == -1:
            self._columns = -1  # Auto mode
        else:
            self._columns = max(1, min(columns, 4))  # Limit to 1-4 columns
        return self

    def set_gap(self, gap: str) -> "ColumnWidget":
        """Set horizontal spacing between columns.

        Args:
            gap (str): CSS spacing value, such as "20px", "1em".

        Returns:
            ColumnWidget: Returns self to support method chaining.

        Examples:
            >>> column = ColumnWidget().set_gap("16px")
        """
        self._gap = gap
        return self

    def clear_widgets(self) -> "ColumnWidget":
        """Clear all widgets in the column layout.

        Returns:
            ColumnWidget: Returns self to support method chaining.

        Examples:
            >>> column = ColumnWidget().clear_widgets()
        """
        self._widgets.clear()
        return self

    def remove_widget(self, widget_id: str) -> "ColumnWidget":
        """Remove specified widget by widget ID.

        Args:
            widget_id (str): ID of the widget to remove.

        Returns:
            ColumnWidget: Returns self to support method chaining.

        Examples:
            >>> column = ColumnWidget().remove_widget("my_text_widget")
        """
        self._widgets = [w for w in self._widgets if w.widget_id != widget_id]
        return self

    def remove_widget_by_index(self, index: int) -> "ColumnWidget":
        """Remove widget at specified index.

        Args:
            index (int): Index of the widget to remove.

        Returns:
            ColumnWidget: Returns self to support method chaining.

        Raises:
            IndexError: If index is out of range.

        Examples:
            >>> column = ColumnWidget().remove_widget_by_index(0) # Remove first widget
        """
        if 0 <= index < len(self._widgets):
            self._widgets.pop(index)
        return self

    def get_widget_count(self) -> int:
        """Get the number of widgets in the column layout.

        Returns:
            int: Number of widgets.

        Examples:
            >>> count = ColumnWidget().add_widget(TextWidget()).get_widget_count()
            >>> print(count) # Output: 1
        """
        return len(self._widgets)

    def is_auto_mode(self) -> bool:
        """Check if currently in auto column mode.

        Returns:
            bool: True if in auto mode, False otherwise.

        Examples:
            >>> column = ColumnWidget().is_auto_mode() # Default is True
        """
        return self._columns == -1

    def get_current_columns(self) -> int:
        """Get the current number of columns actually used.

        If in auto mode, returns the number of columns calculated based on widget count; otherwise returns the manually set number of columns.

        Returns:
            int: Number of columns actually used.

        Examples:
            >>> column = ColumnWidget().add_widgets([TextWidget(), TextWidget()])
            >>> column.get_current_columns() # In auto mode, 2 widgets return 2 columns
        """
        return self.get_effective_columns()

    def set_equal_width(self, equal: bool = True) -> "ColumnWidget":
        """Set whether columns have equal width.

        Args:
            equal (bool): Whether equal width, defaults to True.

        Returns:
            ColumnWidget: Returns self to support method chaining.

        Note:
            This method is currently only a reserved interface, column widths are always equally divided in actual rendering.

        Examples:
            >>> column = ColumnWidget().set_equal_width(False)
        """
        self._equal_width = equal
        return self

    def _calculate_auto_columns(self, widget_count: int) -> int:
        """Automatically calculate appropriate number of columns based on widget count.

        Args:
            widget_count (int): Number of widgets.

        Returns:
            int: Automatically calculated number of columns.
        """
        if widget_count <= 0:
            return 1
        elif widget_count == 1:
            return 1
        elif widget_count == 2:
            return 2
        elif widget_count == 3:
            return 3
        elif widget_count == 4:
            return 2  # 4 widgets use 2 columns, 2 per column
        elif widget_count <= 6:
            return 3  # 5-6 widgets use 3 columns
        elif widget_count <= 8:
            return 2  # 7-8 widgets use 2 columns
        else:
            return 3  # More than 8 widgets use 3 columns

    def get_effective_columns(self) -> int:
        """Get the actual effective number of columns.

        If set to auto mode, calculates based on current widget count; otherwise returns manually set number of columns.

        Returns:
            int: Number of columns actually used.
        """
        if self._columns == -1:
            return self._calculate_auto_columns(len(self._widgets))
        else:
            return self._columns

    def _get_template_name(self) -> str:
        return "column.html"

    def get_template_context(self) -> dict[str, Any]:
        """Get template context data required for rendering"""
        if not self._widgets:
            return {}

        # Get effective columns (handle auto mode)
        effective_columns = self.get_effective_columns()

        # Calculate column width
        column_width = f"{100 / effective_columns:.2f}%"

        # Use table layout to achieve column effect - email client compatible
        table_style = f"""
            width: 100%;
            max-width: 100%;
            table-layout: fixed;
            border-collapse: separate;
            border-spacing: {self._gap} 0;
            margin: 16px 0;
            font-family: Arial, sans-serif;
        """

        cell_style = f"""
            width: {column_width};
            vertical-align: top;
            padding: 0;
            box-sizing: border-box;
        """

        empty_cell_style = f"width: {column_width}; vertical-align: top; padding: 0; box-sizing: border-box;"

        # Group process widgets
        widget_groups = []
        for i in range(0, len(self._widgets), effective_columns):
            group = self._widgets[i : i + effective_columns]
            group_html = []
            for widget in group:
                try:
                    widget_html = widget.render_html()
                    group_html.append(widget_html)
                except Exception as e:
                    self._logger.error(f"Widget rendering failed: {e}")
                    group_html.append("<p style='color: red;'>Widget rendering error</p>")
            widget_groups.append(group_html)

        # Calculate empty columns in the last row
        last_group_size = len(self._widgets) % effective_columns
        empty_columns = (
            (effective_columns - last_group_size) if last_group_size > 0 else 0
        )

        return {
            "widget_groups": widget_groups,
            "table_style": table_style,
            "cell_style": cell_style,
            "empty_cell_style": empty_cell_style,
            "empty_columns": empty_columns,
        }
