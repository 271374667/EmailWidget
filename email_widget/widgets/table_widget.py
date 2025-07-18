"""Table Widget Implementation"""

from typing import TYPE_CHECKING, Any, Optional

from email_widget.core.base import BaseWidget
from email_widget.core.enums import StatusType
from email_widget.utils.optional_deps import (
    check_optional_dependency,
    import_optional_dependency,
)

if TYPE_CHECKING:
    import pandas as pd


class TableCell:
    """Table cell class.

    Used to encapsulate data and style information for individual cells in a table, supporting setting cell values, status, color,
    font weight, and alignment. This allows tables to display richer, more expressive data.

    Attributes:
        value (Any): The actual value of the cell, can be any type, will be converted to string for display.
        status (Optional[StatusType]): Status type of the cell, used to apply predefined colors and backgrounds.
        color (Optional[str]): Custom color for cell text (CSS color value).
        bold (bool): Whether cell text is bold.
        align (str): Text alignment of the cell (e.g., "left", "center", "right").

    Examples:
        ```python
        from email_widget.widgets import TableCell
        from email_widget.core.enums import StatusType

        # Create a success status cell
        success_cell = TableCell("Success", status=StatusType.SUCCESS, bold=True)

        # Create a custom color cell
        red_text_cell = TableCell("Warning", color="#FF0000", align="right")
        ```
    """

    def __init__(
        self,
        value: Any,
        status: StatusType | None = None,
        color: str | None = None,
        bold: bool = False,
        align: str = "center",
    ):
        """Initialize table cell.

        Args:
            value (Any): Cell value.
            status (Optional[StatusType]): Status type, used to apply predefined colors and backgrounds.
            color (Optional[str]): Text color (CSS color value).
            bold (bool): Whether to bold, defaults to False.
            align (str): Alignment method, defaults to "center".

        Examples:
            >>> cell = TableCell("Success", status=StatusType.SUCCESS, bold=True)
        """
        self.value = value
        self.status = status
        self.color = color
        self.bold = bold
        self.align = align


class TableWidget(BaseWidget):
    """Create a widget for displaying table data in emails.

    This widget provides a flexible way to present structured data, whether manually constructing tables
    or directly importing data from `pandas.DataFrame`. It supports various styling options,
    such as striped patterns, borders, hover effects, and can apply colors and status to specific cells
    to enhance data readability and visual appeal.

    Core features:
        - **Diverse data sources**: Support for directly adding row data or importing from `pandas.DataFrame`.
        - **Style customization**: Can set title, headers, striped patterns, borders, hover effects, etc.
        - **Cell styling**: Allows setting colors, bold, and alignment for individual cells, and supports status coloring.
        - **Email compatibility**: Generated HTML is optimized for mainstream email clients to ensure consistent display.

    Attributes:
        title (Optional[str]): Title of the table.
        headers (List[str]): List of table column headers.
        rows (List[List[Union[str, TableCell]]]): Table row data, each row contains strings or `TableCell` objects.
        show_index (bool): Whether to display row indices.
        striped (bool): Whether to enable striped pattern styling.
        bordered (bool): Whether to display borders for all cells.
        hover_effect (bool): Whether to enable mouse hover highlighting effect.

    Examples:
        Manually create a table with status cells:

        ```python
        from email_widget.widgets import TableWidget, TableCell
        from email_widget.core.enums import StatusType

        project_status_table = (TableWidget()\
                                .set_title("Project Progress Overview")\
                                .set_headers(["Project Name", "Owner", "Progress", "Status"])\
                                .add_row(["Website Redesign", "Alice", "85%",
                                          TableCell("In Progress", status=StatusType.INFO)])\
                                .add_row(["Mobile App Dev", "Bob", "100%",
                                          TableCell("Completed", status=StatusType.SUCCESS)])\
                                .add_row(["Backend Optimization", "Charlie", "60%",
                                          TableCell("At Risk", status=StatusType.WARNING)])\
                                .set_striped(True)\
                                .set_bordered(True))

        # Assuming email is an Email object
        # email.add_widget(project_status_table)
        ```

        Create a table from `pandas.DataFrame`:

        ```python
        import pandas as pd

        data = {
            'Product': ['Laptop', 'Mouse', 'Keyboard'],
            'Sales': [1200, 300, 500],
            'Region': ['North', 'South', 'East']
        }
        df = pd.DataFrame(data)

        sales_table = (TableWidget()\
                       .set_dataframe(df)\
                       .set_title("Product Sales Data")\
                       .show_index(False) # Don't display index
                       .set_hover_effect(True))
        ```
    """

    # Template definition
    TEMPLATE = """
    <!--[if mso]>
    <table width="100%" cellpadding="0" cellspacing="0" border="0">
        <tr>
            <td>
    <![endif]-->
    <div style="{{ container_style }}">
        {% if title %}
            <h3 style="margin: 0 0 16px 0; font-size: 18px; font-weight: 600; color: #323130; text-align: center;">{{ title }}</h3>
        {% endif %}
        <!-- 使用表格布局实现居中对齐 -->
        <table width="100%" cellpadding="0" cellspacing="0" border="0" style="width: 100%; margin: 0;">
            <tr>
                <td align="center" style="padding: 0;">
                    <table cellpadding="0" cellspacing="0" border="0" style="{{ table_style }}">
                        {% if headers %}
                            <thead>
                                <tr>
                                    {% if show_index %}
                                        <th style="{{ index_th_style }}">Index</th>
                                    {% endif %}
                                    {% for header in headers %}
                                        <th style="{{ th_style }}">{{ header }}</th>
                                    {% endfor %}
                                </tr>
                            </thead>
                        {% endif %}
                        <tbody>
                            {% for row_data in rows_data %}
                                <tr style="{{ row_data.row_style }}">
                                    {% if show_index %}
                                        <td style="{{ index_td_style }}">{{ row_data.index }}</td>
                                    {% endif %}
                                    {% for cell_data in row_data.cells %}
                                        <td style="{{ cell_data.style }}">{{ cell_data.value }}</td>
                                    {% endfor %}
                                </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </td>
            </tr>
        </table>
    </div>
    <!--[if mso]>
            </td>
        </tr>
    </table>
    <![endif]-->
    """

    def __init__(self, widget_id: str | None = None):
        """Initialize TableWidget instance.

        Args:
            widget_id (Optional[str]): Optional Widget ID.

        Examples:
            >>> table = TableWidget()
            >>> table_with_id = TableWidget("my-table")
        """
        super().__init__(widget_id)
        self._dataframe: pd.DataFrame | None = None
        self._title: str | None = None
        self._headers: list[str] = []
        self._rows: list[list[str | TableCell]] = []
        self._show_index: bool = False
        self._striped: bool = True
        self._bordered: bool = True
        self._hover_effect: bool = True
        self._max_width: str | None = None
        self._header_bg_color: str = "#f3f2f1"
        self._border_color: str = "#e1dfdd"

    def set_dataframe(self, df: "pd.DataFrame") -> "TableWidget":
        """Set DataFrame data.

        Args:
            df (pd.DataFrame): pandas DataFrame object.

        Returns:
            TableWidget: Returns self to support method chaining.

        Raises:
            ImportError: If pandas library is not installed.

        Examples:
            ```python
            import pandas as pd
            df = pd.DataFrame({'Name': ['Project A', 'Project B'], 'Status': ['Completed', 'In Progress']})
            table = TableWidget().set_dataframe(df)
            ```
        """
        check_optional_dependency("pandas")
        self._dataframe = df.copy()
        self._headers = list(df.columns)
        self._rows = []

        for _, row in df.iterrows():
            row_data = []
            for col in df.columns:
                value = row[col]
                if isinstance(value, dict) and "status" in value:
                    # Handle status type data
                    cell = TableCell(
                        value=value.get("text", str(value)),
                        status=StatusType(value["status"])
                        if "status" in value
                        else None,
                    )
                    row_data.append(cell)
                else:
                    row_data.append(str(value))
            self._rows.append(row_data)
        return self

    def set_title(self, title: str) -> "TableWidget":
        """Set table title.

        Args:
            title (str): Table title.

        Returns:
            TableWidget: Returns self to support method chaining.

        Examples:
            >>> table = TableWidget().set_title("Project Progress Table")
        """
        self._title = title
        return self

    def set_headers(self, headers: list[str]) -> "TableWidget":
        """Set table headers.

        Args:
            headers (List[str]): Header list.

        Returns:
            TableWidget: Returns self to support method chaining.

        Examples:
            >>> table = TableWidget().set_headers(["Project Name", "Progress", "Status"])
        """
        self._headers = headers.copy()
        return self

    def add_row(self, row: list[str | TableCell]) -> "TableWidget":
        """Add row data.

        Args:
            row (List[Union[str, TableCell]]): Row data, can be strings or TableCell objects.

        Returns:
            TableWidget: Returns self to support method chaining.

        Examples:
            >>> table = TableWidget().add_row(["Project A", "80%", TableCell("In Progress", status=StatusType.INFO)])
        """
        self._rows.append(row)
        return self

    def set_rows(self, rows: list[list[str | TableCell]]) -> "TableWidget":
        """Set all row data.

        Args:
            rows (List[List[Union[str, TableCell]]]): Row data list.

        Returns:
            TableWidget: Returns self to support method chaining.

        Examples:
            ```python
            rows = [
                ["Project A", "80%", TableCell("In Progress", status=StatusType.INFO)],
                ["Project B", "100%", TableCell("Completed", status=StatusType.SUCCESS)]
            ]
            table = TableWidget().set_rows(rows)
            ```
        """
        self._rows = rows
        return self

    def clear_rows(self) -> "TableWidget":
        """Clear row data.

        Returns:
            TableWidget: Returns self to support method chaining.

        Examples:
            >>> table = TableWidget().clear_rows()
        """
        self._rows.clear()
        return self

    def show_index(self, show: bool = True) -> "TableWidget":
        """Set whether to display index.

        Args:
            show (bool): Whether to display index, defaults to True.

        Returns:
            TableWidget: Returns self to support method chaining.

        Examples:
            >>> table = TableWidget().show_index(False)
        """
        self._show_index = show
        return self

    def set_striped(self, striped: bool = True) -> "TableWidget":
        """Set whether to use striped pattern.

        Args:
            striped (bool): Whether to use striped pattern, defaults to True.

        Returns:
            TableWidget: Returns self to support method chaining.

        Examples:
            >>> table = TableWidget().set_striped(False)
        """
        self._striped = striped
        return self

    def set_bordered(self, bordered: bool = True) -> "TableWidget":
        """Set whether to display borders.

        Args:
            bordered (bool): Whether to display borders, defaults to True.

        Returns:
            TableWidget: Returns self to support method chaining.

        Examples:
            >>> table = TableWidget().set_bordered(False)
        """
        self._bordered = bordered
        return self

    def set_hover_effect(self, hover: bool = True) -> "TableWidget":
        """Set whether to enable hover effect.

        Args:
            hover (bool): Whether to enable hover effect, defaults to True.

        Returns:
            TableWidget: Returns self to support method chaining.

        Examples:
            >>> table = TableWidget().set_hover_effect(False)
        """
        self._hover_effect = hover
        return self

    def set_max_width(self, width: str) -> "TableWidget":
        """Set maximum width.

        Args:
            width (str): CSS width value.

        Returns:
            TableWidget: Returns self to support method chaining.

        Examples:
            >>> table = TableWidget().set_max_width("800px")
        """
        self._max_width = width
        return self

    def set_header_bg_color(self, color: str) -> "TableWidget":
        """Set header background color.

        Args:
            color (str): CSS color value.

        Returns:
            TableWidget: Returns self to support method chaining.

        Examples:
            >>> table = TableWidget().set_header_bg_color("#4CAF50")
        """
        self._header_bg_color = color
        return self

    def set_border_color(self, color: str) -> "TableWidget":
        """Set border color.

        Args:
            color (str): CSS color value.

        Returns:
            TableWidget: Returns self to support method chaining.

        Examples:
            >>> table = TableWidget().set_border_color("#ddd")
        """
        self._border_color = color
        return self

    def add_data_row(self, row_data: list) -> "TableWidget":
        """Add data row (based on DataFrame).

        This method is used to add a row of data to the table. If the table has been initialized through `set_dataframe`,
        the new row will be added to the existing DataFrame; otherwise, a new DataFrame will be created.

        Args:
            row_data (list): List containing row data. The length of the list should match the number of headers.

        Returns:
            TableWidget: Returns self to support method chaining.

        Raises:
            ImportError: If pandas library is not installed.

        Examples:
            >>> table = TableWidget().add_data_row(["New Project", "0%", "Started"])
        """
        check_optional_dependency("pandas")
        pd = import_optional_dependency("pandas")

        if self._dataframe is not None:
            # If DataFrame exists, add new row
            new_row = pd.Series(row_data, index=self._dataframe.columns)
            self._dataframe = pd.concat(
                [self._dataframe, new_row.to_frame().T], ignore_index=True
            )
        else:
            # If no DataFrame exists, create new one
            self._dataframe = pd.DataFrame([row_data])
        return self

    def clear_data(self) -> "TableWidget":
        """Clear table data.

        This method will clear all data added through `set_dataframe` or `add_data_row`,
        and reset the internal DataFrame and row data list.

        Returns:
            TableWidget: Returns self to support method chaining.

        Examples:
            >>> table = TableWidget().clear_data()
        """
        self._dataframe = None
        self._rows.clear()
        return self

    def set_column_width(self, column: str, width: str) -> "TableWidget":
        """Set column width"""
        if not hasattr(self, "_column_widths"):
            self._column_widths = {}
        self._column_widths[column] = width
        return self

    def add_status_cell(self, value: str, status: StatusType) -> TableCell:
        """Create status cell.

        This helper method is used to quickly create a `TableCell` object with a specific status (such as success, warning, error).
        Status cells automatically apply predefined color and background styles.

        Args:
            value (str): Value displayed in the cell.
            status (StatusType): Status type of the cell.

        Returns:
            TableCell: A configured `TableCell` object.

        Examples:
            >>> cell = table.add_status_cell("Success", StatusType.SUCCESS)
        """
        return TableCell(value=value, status=status)

    def add_colored_cell(
        self, value: str, color: str, bold: bool = False, align: str = "center"
    ) -> TableCell:
        """Create colored cell.

        This helper method is used to quickly create a `TableCell` object with custom color, font weight, and alignment.

        Args:
            value (str): Value displayed in the cell.
            color (str): Color of the cell text (CSS color value).
            bold (bool): Whether to bold, defaults to False.
            align (str): Alignment method, defaults to "center".

        Returns:
            TableCell: A configured `TableCell` object.

        Examples:
            >>> cell = table.add_colored_cell("Important", "#ff0000", bold=True)
        """
        return TableCell(value=value, color=color, bold=bold, align=align)

    def _get_status_style(self, status: StatusType) -> dict[str, str]:
        """Get status style"""
        styles = {
            StatusType.SUCCESS: {"color": "#107c10", "background": "#dff6dd"},
            StatusType.WARNING: {"color": "#ff8c00", "background": "#fff4e6"},
            StatusType.ERROR: {"color": "#d13438", "background": "#ffebee"},
            StatusType.INFO: {"color": "#0078d4", "background": "#e6f3ff"},
            StatusType.PRIMARY: {"color": "#0078d4", "background": "#e6f3ff"},
        }
        return styles.get(status, {"color": "#323130", "background": "#ffffff"})

    @property
    def dataframe(self) -> Optional["pd.DataFrame"]:
        """Get DataFrame data.

        Returns:
            Optional[pd.DataFrame]: DataFrame object or None.
        """
        return self._dataframe

    @property
    def title(self) -> str | None:
        """Get table title.

        Returns:
            Optional[str]: Title or None.
        """
        return self._title

    @property
    def headers(self) -> list[str]:
        """Get header list.

        Returns:
            List[str]: Header list.
        """
        return self._headers.copy()

    @property
    def rows(self) -> list[list[str | TableCell]]:
        """Get row data.

        Returns:
            List[List[Union[str, TableCell]]]: Row data list.
        """
        return self._rows.copy()

    def _get_template_name(self) -> str:
        return "table.html"

    def get_template_context(self) -> dict[str, Any]:
        """Get template context data required for rendering"""
        if not self._headers and not self._rows:
            return {}

        # Container style - center alignment, 5px left and right padding for margin effect
        container_style = "margin: 16px auto; width: 100%; max-width: 100%; padding: 0 5px; box-sizing: border-box;"
        if self._max_width:
            container_style += f" max-width: {self._max_width};"

        # Table style - email client compatible, center alignment
        table_style = """
            width: 100%;
            min-width: 400px;
            max-width: 100%;
            border-collapse: collapse;
            font-family: Arial, sans-serif;
            font-size: 14px;
            background: #ffffff;
            margin: 0;
            text-align: center;
        """

        if self._bordered:
            table_style += f" border: 1px solid {self._border_color};"

        # Header style
        header_style = f"""
            background: {self._header_bg_color};
            border-bottom: 2px solid {self._border_color};
        """

        # Header cell style - center alignment
        index_th_style = f"""
            padding: 12px 8px;
            text-align: center;
            font-weight: 600;
            color: #323130;
            border-right: 1px solid {self._border_color};
        """

        th_style = """
            padding: 12px 8px;
            text-align: center;
            font-weight: 600;
            color: #323130;
        """
        if self._bordered:
            th_style += f" border-right: 1px solid {self._border_color};"

        # Index column style - center alignment
        index_td_style = """
            padding: 8px;
            vertical-align: top;
            text-align: center;
            color: #605e5c;
        """
        if self._bordered:
            index_td_style += f" border-right: 1px solid {self._border_color};"

        # Process row data
        rows_data = []
        for idx, row in enumerate(self._rows):
            # Row style
            row_style = ""
            if self._striped and idx % 2 == 1:
                row_style = "background: #faf9f8;"
            if self._bordered:
                row_style += f" border-bottom: 1px solid {self._border_color};"

            # Process cell data
            cells_data = []
            for cell in row:
                td_style = "padding: 8px; vertical-align: top;"

                if isinstance(cell, TableCell):
                    # Handle TableCell
                    if cell.status:
                        status_style = self._get_status_style(cell.status)
                        td_style += f" color: {status_style['color']}; background: {status_style['background']};"

                    if cell.color:
                        td_style += f" color: {cell.color};"

                    if cell.bold:
                        td_style += " font-weight: bold;"

                    td_style += f" text-align: {cell.align};"

                    if self._bordered:
                        td_style += f" border-right: 1px solid {self._border_color};"

                    cells_data.append({"value": cell.value, "style": td_style})
                else:
                    # Handle regular strings - default center alignment
                    td_style += " color: #323130; text-align: center;"
                    if self._bordered:
                        td_style += f" border-right: 1px solid {self._border_color};"

                    cells_data.append({"value": cell, "style": td_style})

            rows_data.append(
                {"index": idx + 1, "row_style": row_style, "cells": cells_data}
            )

        return {
            "title": self._title,
            "container_style": container_style,
            "table_style": table_style,
            "header_style": header_style,
            "index_th_style": index_th_style,
            "th_style": th_style,
            "index_td_style": index_td_style,
            "headers": self._headers,
            "show_index": self._show_index,
            "rows_data": rows_data,
        }
