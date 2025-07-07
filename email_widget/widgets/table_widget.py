"""表格Widget实现"""

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
    """表格单元格类.

    用于封装表格中单个单元格的数据和样式信息，支持设置单元格的值、状态、颜色、
    字体粗细和对齐方式.这使得表格能够展示更丰富、更具表现力的数据.

    Attributes:
        value (Any): 单元格的实际值，可以是任何类型，最终会转换为字符串显示.
        status (Optional[StatusType]): 单元格的状态类型，用于应用预定义的颜色和背景.
        color (Optional[str]): 单元格文本的自定义颜色（CSS颜色值）.
        bold (bool): 单元格文本是否加粗.
        align (str): 单元格文本的对齐方式（如 "left", "center", "right"）.

    Examples:
        ```python
        from email_widget.widgets import TableCell
        from email_widget.core.enums import StatusType

        # 创建一个成功状态的单元格
        success_cell = TableCell("成功", status=StatusType.SUCCESS, bold=True)

        # 创建一个自定义颜色的单元格
        red_text_cell = TableCell("警告", color="#FF0000", align="right")
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
        """初始化表格单元格.

        Args:
            value (Any): 单元格值.
            status (Optional[StatusType]): 状态类型，用于应用预定义的颜色和背景.
            color (Optional[str]): 文字颜色（CSS颜色值）.
            bold (bool): 是否粗体，默认为False.
            align (str): 对齐方式，默认为"center".

        Examples:
            >>> cell = TableCell("成功", status=StatusType.SUCCESS, bold=True)
        """
        self.value = value
        self.status = status
        self.color = color
        self.bold = bold
        self.align = align


class TableWidget(BaseWidget):
    """创建一个用于在邮件中展示表格数据的微件.

    该微件提供了灵活的方式来呈现结构化数据，无论是手动构建表格，
    还是直接从 `pandas.DataFrame` 导入数据.它支持多种样式选项，
    如斑马纹、边框、悬停效果，并能为特定单元格应用颜色和状态，
    以增强数据的可读性和视觉吸引力.

    核心功能:
        - **数据源多样**: 支持直接添加行数据，或从 `pandas.DataFrame` 导入.
        - **样式定制**: 可设置标题、表头、斑马纹、边框、悬停效果等.
        - **单元格样式**: 允许为单个单元格设置颜色、粗体和对齐方式，并支持状态着色.
        - **邮件兼容性**: 生成的 HTML 针对主流邮件客户端进行了优化，确保显示效果一致.

    Attributes:
        title (Optional[str]): 表格的标题.
        headers (List[str]): 表格的列头列表.
        rows (List[List[Union[str, TableCell]]]): 表格的行数据，每行包含字符串或 `TableCell` 对象.
        show_index (bool): 是否显示行索引.
        striped (bool): 是否启用斑马纹样式.
        bordered (bool): 是否显示所有单元格边框.
        hover_effect (bool): 是否启用鼠标悬停高亮效果.

    Examples:
        手动创建一个包含状态单元格的表格：

        ```python
        from email_widget.widgets import TableWidget, TableCell
        from email_widget.core.enums import StatusType

        project_status_table = (TableWidget()\
                                .set_title("项目进度概览")\
                                .set_headers(["项目名称", "负责人", "进度", "状态"])\
                                .add_row(["Website Redesign", "Alice", "85%",
                                          TableCell("进行中", status=StatusType.INFO)])\
                                .add_row(["Mobile App Dev", "Bob", "100%",
                                          TableCell("已完成", status=StatusType.SUCCESS)])\
                                .add_row(["Backend Optimization", "Charlie", "60%",
                                          TableCell("有风险", status=StatusType.WARNING)])\
                                .set_striped(True)\
                                .set_bordered(True))

        # 假设 email 是一个 Email 对象
        # email.add_widget(project_status_table)
        ```

        从 `pandas.DataFrame` 创建表格：

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
                       .set_title("产品销售数据")\
                       .show_index(False) # 不显示索引
                       .set_hover_effect(True))
        ```
    """

    # 模板定义
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
                                        <th style="{{ index_th_style }}">索引</th>
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
        """初始化TableWidget实例.

        Args:
            widget_id (Optional[str]): 可选的Widget ID.

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
        """设置DataFrame数据.

        Args:
            df (pd.DataFrame): pandas DataFrame对象.

        Returns:
            TableWidget: 返回self以支持链式调用.

        Raises:
            ImportError: 如果未安装pandas库.

        Examples:
            ```python
            import pandas as pd
            df = pd.DataFrame({'名称': ['项目A', '项目B'], '状态': ['完成', '进行中']})
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
                    # 处理状态类型数据
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
        """设置表格标题.

        Args:
            title (str): 表格标题.

        Returns:
            TableWidget: 返回self以支持链式调用.

        Examples:
            >>> table = TableWidget().set_title("项目进度表")
        """
        self._title = title
        return self

    def set_headers(self, headers: list[str]) -> "TableWidget":
        """设置表头.

        Args:
            headers (List[str]): 表头列表.

        Returns:
            TableWidget: 返回self以支持链式调用.

        Examples:
            >>> table = TableWidget().set_headers(["项目名称", "进度", "状态"])
        """
        self._headers = headers.copy()
        return self

    def add_row(self, row: list[str | TableCell]) -> "TableWidget":
        """添加行数据.

        Args:
            row (List[Union[str, TableCell]]): 行数据，可以是字符串或TableCell对象.

        Returns:
            TableWidget: 返回self以支持链式调用.

        Examples:
            >>> table = TableWidget().add_row(["项目A", "80%", TableCell("进行中", status=StatusType.INFO)])
        """
        self._rows.append(row)
        return self

    def set_rows(self, rows: list[list[str | TableCell]]) -> "TableWidget":
        """设置所有行数据.

        Args:
            rows (List[List[Union[str, TableCell]]]): 行数据列表.

        Returns:
            TableWidget: 返回self以支持链式调用.

        Examples:
            ```python
            rows = [
                ["项目A", "80%", TableCell("进行中", status=StatusType.INFO)],
                ["项目B", "100%", TableCell("完成", status=StatusType.SUCCESS)]
            ]
            table = TableWidget().set_rows(rows)
            ```
        """
        self._rows = rows
        return self

    def clear_rows(self) -> "TableWidget":
        """清空行数据.

        Returns:
            TableWidget: 返回self以支持链式调用.

        Examples:
            >>> table = TableWidget().clear_rows()
        """
        self._rows.clear()
        return self

    def show_index(self, show: bool = True) -> "TableWidget":
        """设置是否显示索引.

        Args:
            show (bool): 是否显示索引，默认为True.

        Returns:
            TableWidget: 返回self以支持链式调用.

        Examples:
            >>> table = TableWidget().show_index(False)
        """
        self._show_index = show
        return self

    def set_striped(self, striped: bool = True) -> "TableWidget":
        """设置是否使用斑马纹.

        Args:
            striped (bool): 是否使用斑马纹，默认为True.

        Returns:
            TableWidget: 返回self以支持链式调用.

        Examples:
            >>> table = TableWidget().set_striped(False)
        """
        self._striped = striped
        return self

    def set_bordered(self, bordered: bool = True) -> "TableWidget":
        """设置是否显示边框.

        Args:
            bordered (bool): 是否显示边框，默认为True.

        Returns:
            TableWidget: 返回self以支持链式调用.

        Examples:
            >>> table = TableWidget().set_bordered(False)
        """
        self._bordered = bordered
        return self

    def set_hover_effect(self, hover: bool = True) -> "TableWidget":
        """设置是否启用悬停效果.

        Args:
            hover (bool): 是否启用悬停效果，默认为True.

        Returns:
            TableWidget: 返回self以支持链式调用.

        Examples:
            >>> table = TableWidget().set_hover_effect(False)
        """
        self._hover_effect = hover
        return self

    def set_max_width(self, width: str) -> "TableWidget":
        """设置最大宽度.

        Args:
            width (str): CSS宽度值.

        Returns:
            TableWidget: 返回self以支持链式调用.

        Examples:
            >>> table = TableWidget().set_max_width("800px")
        """
        self._max_width = width
        return self

    def set_header_bg_color(self, color: str) -> "TableWidget":
        """设置表头背景色.

        Args:
            color (str): CSS颜色值.

        Returns:
            TableWidget: 返回self以支持链式调用.

        Examples:
            >>> table = TableWidget().set_header_bg_color("#4CAF50")
        """
        self._header_bg_color = color
        return self

    def set_border_color(self, color: str) -> "TableWidget":
        """设置边框颜色.

        Args:
            color (str): CSS颜色值.

        Returns:
            TableWidget: 返回self以支持链式调用.

        Examples:
            >>> table = TableWidget().set_border_color("#ddd")
        """
        self._border_color = color
        return self

    def add_data_row(self, row_data: list) -> "TableWidget":
        """添加数据行（基于DataFrame）.

        此方法用于向表格添加一行数据.如果表格已通过 `set_dataframe` 初始化，
        新行将添加到现有DataFrame中；否则，将创建一个新的DataFrame.

        Args:
            row_data (list): 包含行数据的列表.列表的长度应与表头数量匹配.

        Returns:
            TableWidget: 返回self以支持链式调用.

        Raises:
            ImportError: 如果未安装pandas库.

        Examples:
            >>> table = TableWidget().add_data_row(["新项目", "0%", "开始"])
        """
        check_optional_dependency("pandas")
        pd = import_optional_dependency("pandas")

        if self._dataframe is not None:
            # 如果已有DataFrame，添加新行
            new_row = pd.Series(row_data, index=self._dataframe.columns)
            self._dataframe = pd.concat(
                [self._dataframe, new_row.to_frame().T], ignore_index=True
            )
        else:
            # 如果没有DataFrame，创建新的
            self._dataframe = pd.DataFrame([row_data])
        return self

    def clear_data(self) -> "TableWidget":
        """清空表格数据.

        此方法将清除通过 `set_dataframe` 或 `add_data_row` 添加的所有数据，
        并重置内部的DataFrame和行数据列表.

        Returns:
            TableWidget: 返回self以支持链式调用.

        Examples:
            >>> table = TableWidget().clear_data()
        """
        self._dataframe = None
        self._rows.clear()
        return self

    def set_column_width(self, column: str, width: str) -> "TableWidget":
        """设置列宽度"""
        if not hasattr(self, "_column_widths"):
            self._column_widths = {}
        self._column_widths[column] = width
        return self

    def add_status_cell(self, value: str, status: StatusType) -> TableCell:
        """创建状态单元格.

        此辅助方法用于快速创建一个带有特定状态（如成功、警告、错误）的 `TableCell` 对象.
        状态单元格会自动应用预定义的颜色和背景样式.

        Args:
            value (str): 单元格显示的值.
            status (StatusType): 单元格的状态类型.

        Returns:
            TableCell: 一个配置好的 `TableCell` 对象.

        Examples:
            >>> cell = table.add_status_cell("成功", StatusType.SUCCESS)
        """
        return TableCell(value=value, status=status)

    def add_colored_cell(
        self, value: str, color: str, bold: bool = False, align: str = "center"
    ) -> TableCell:
        """创建彩色单元格.

        此辅助方法用于快速创建一个带有自定义颜色、字体粗细和对齐方式的 `TableCell` 对象.

        Args:
            value (str): 单元格显示的值.
            color (str): 单元格文本的颜色（CSS颜色值）.
            bold (bool): 是否加粗，默认为False.
            align (str): 对齐方式，默认为"center".

        Returns:
            TableCell: 一个配置好的 `TableCell` 对象.

        Examples:
            >>> cell = table.add_colored_cell("重要", "#ff0000", bold=True)
        """
        return TableCell(value=value, color=color, bold=bold, align=align)

    def _get_status_style(self, status: StatusType) -> dict[str, str]:
        """获取状态样式"""
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
        """获取DataFrame数据.

        Returns:
            Optional[pd.DataFrame]: DataFrame对象或None.
        """
        return self._dataframe

    @property
    def title(self) -> str | None:
        """获取表格标题.

        Returns:
            Optional[str]: 标题或None.
        """
        return self._title

    @property
    def headers(self) -> list[str]:
        """获取表头列表.

        Returns:
            List[str]: 表头列表.
        """
        return self._headers.copy()

    @property
    def rows(self) -> list[list[str | TableCell]]:
        """获取行数据.

        Returns:
            List[List[Union[str, TableCell]]]: 行数据列表.
        """
        return self._rows.copy()

    def _get_template_name(self) -> str:
        return "table.html"

    def get_template_context(self) -> dict[str, Any]:
        """获取模板渲染所需的上下文数据"""
        if not self._headers and not self._rows:
            return {}

        # 容器样式 - 居中对齐，左右内边距5px实现边距效果
        container_style = "margin: 16px auto; width: 100%; max-width: 100%; padding: 0 5px; box-sizing: border-box;"
        if self._max_width:
            container_style += f" max-width: {self._max_width};"

        # 表格样式 - 邮件客户端兼容，居中对齐
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

        # 表头样式
        header_style = f"""
            background: {self._header_bg_color};
            border-bottom: 2px solid {self._border_color};
        """

        # 表头单元格样式 - 居中对齐
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

        # 索引列样式 - 居中对齐
        index_td_style = """
            padding: 8px;
            vertical-align: top;
            text-align: center;
            color: #605e5c;
        """
        if self._bordered:
            index_td_style += f" border-right: 1px solid {self._border_color};"

        # 处理行数据
        rows_data = []
        for idx, row in enumerate(self._rows):
            # 行样式
            row_style = ""
            if self._striped and idx % 2 == 1:
                row_style = "background: #faf9f8;"
            if self._bordered:
                row_style += f" border-bottom: 1px solid {self._border_color};"

            # 处理单元格数据
            cells_data = []
            for cell in row:
                td_style = "padding: 8px; vertical-align: top;"

                if isinstance(cell, TableCell):
                    # 处理TableCell
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
                    # 处理普通字符串 - 默认居中对齐
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
