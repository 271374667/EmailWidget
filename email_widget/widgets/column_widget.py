"""列布局Widget实现"""

from typing import Any

from email_widget.core.base import BaseWidget


class ColumnWidget(BaseWidget):
    """创建一个多列布局容器，用于水平排列多个微件。

    该微件使用 `<table>` 元素来确保在各种邮件客户端中的最大兼容性。
    你可以将任何其他微件（如 `TextWidget`, `CardWidget`, `ChartWidget` 等）
    放入列布局中，以创建复杂且美观的邮件版式。

    核心功能:
        - **自动列数**: 默认情况下，它会根据内部微件的数量智能地计算出最佳列数。
        - **手动列数**: 你也可以手动指定1到4之间的固定列数。
        - **响应式**: 布局会根据屏幕宽度自动调整，确保在桌面和移动设备上都有良好体验。
        - **间隔控制**: 可以自定义列与列之间的水平间距。

    自动列数规则:
        - 1个微件: 1列
        - 2个微件: 2列
        - 3个微件: 3列
        - 4个微件: 2列 (2x2 网格)
        - 5-6个微件: 3列
        - 7-8个微件: 2列
        - 9个及以上: 3列

    Examples:
        创建一个两列布局，左侧是卡片，右侧是图表：

        ```python
        from email_widget.widgets import ColumnWidget, CardWidget, ChartWidget
        import matplotlib.pyplot as plt

        # 准备左侧卡片
        left_card = (CardWidget()
                     .set_title("关键指标")
                     .add_metadata("用户增长", "+15%")
                     .add_metadata("收入", "+12%"))

        # 准备右侧图表
        plt.figure()
        plt.plot([1, 2, 3], [4, 5, 2])
        right_chart = ChartWidget().set_chart(plt)

        # 创建2列布局并添加微件
        two_column_layout = (ColumnWidget()
                             .set_columns(2)
                             .set_gap("24px")
                             .add_widget(left_card)
                             .add_widget(right_chart))

        # 假设 email 是一个 Email 对象
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
        """初始化ColumnWidget。

        Args:
            widget_id (Optional[str]): 可选的Widget ID。
        """
        super().__init__(widget_id)
        self._widgets: list[BaseWidget] = []
        self._columns: int = -1  # -1表示自动模式
        self._gap: str = "20px"

    def add_widget(self, widget: BaseWidget) -> "ColumnWidget":
        """向列布局中添加一个微件。

        Args:
            widget (BaseWidget): 要添加的微件实例。

        Returns:
            ColumnWidget: 返回self以支持链式调用。

        Examples:
            >>> column = ColumnWidget().add_widget(TextWidget().set_content("左侧内容"))
        """
        self._widgets.append(widget)
        return self

    def add_widgets(self, widgets: list[BaseWidget]) -> "ColumnWidget":
        """向列布局中添加多个微件。

        Args:
            widgets (List[BaseWidget]): 要添加的微件实例列表。

        Returns:
            ColumnWidget: 返回self以支持链式调用。

        Examples:
            >>> column = ColumnWidget().add_widgets([TextWidget(), ImageWidget()])
        """
        self._widgets.extend(widgets)
        return self

    def set_columns(self, columns: int) -> "ColumnWidget":
        """设置列布局的列数。

        Args:
            columns (int): 列数。-1表示自动模式，其他值限制在1到4列之间。

        Returns:
            ColumnWidget: 返回self以支持链式调用。

        Examples:
            >>> column = ColumnWidget().set_columns(2) # 设置为2列
            >>> column = ColumnWidget().set_columns(-1) # 自动模式
        """
        if columns == -1:
            self._columns = -1  # 自动模式
        else:
            self._columns = max(1, min(columns, 4))  # 限制1-4列
        return self

    def set_gap(self, gap: str) -> "ColumnWidget":
        """设置列之间的水平间距。

        Args:
            gap (str): CSS间距值，如 "20px", "1em"。

        Returns:
            ColumnWidget: 返回self以支持链式调用。

        Examples:
            >>> column = ColumnWidget().set_gap("16px")
        """
        self._gap = gap
        return self

    def clear_widgets(self) -> "ColumnWidget":
        """清空列布局中的所有微件。

        Returns:
            ColumnWidget: 返回self以支持链式调用。

        Examples:
            >>> column = ColumnWidget().clear_widgets()
        """
        self._widgets.clear()
        return self

    def remove_widget(self, widget_id: str) -> "ColumnWidget":
        """根据微件ID移除指定的微件。

        Args:
            widget_id (str): 要移除的微件的ID。

        Returns:
            ColumnWidget: 返回self以支持链式调用。

        Examples:
            >>> column = ColumnWidget().remove_widget("my_text_widget")
        """
        self._widgets = [w for w in self._widgets if w.widget_id != widget_id]
        return self

    def remove_widget_by_index(self, index: int) -> "ColumnWidget":
        """移除指定索引的微件。

        Args:
            index (int): 要移除的微件的索引。

        Returns:
            ColumnWidget: 返回self以支持链式调用。

        Raises:
            IndexError: 如果索引超出范围。

        Examples:
            >>> column = ColumnWidget().remove_widget_by_index(0) # 移除第一个微件
        """
        if 0 <= index < len(self._widgets):
            self._widgets.pop(index)
        return self

    def get_widget_count(self) -> int:
        """获取列布局中微件的数量。

        Returns:
            int: 微件的数量。

        Examples:
            >>> count = ColumnWidget().add_widget(TextWidget()).get_widget_count()
            >>> print(count) # 输出: 1
        """
        return len(self._widgets)

    def is_auto_mode(self) -> bool:
        """检查当前是否为自动列数模式。

        Returns:
            bool: 如果是自动模式则为True，否则为False。

        Examples:
            >>> column = ColumnWidget().is_auto_mode() # 默认为True
        """
        return self._columns == -1

    def get_current_columns(self) -> int:
        """获取当前实际使用的列数。

        如果处于自动模式，则返回根据微件数量计算出的列数；否则返回手动设置的列数。

        Returns:
            int: 实际使用的列数。

        Examples:
            >>> column = ColumnWidget().add_widgets([TextWidget(), TextWidget()])
            >>> column.get_current_columns() # 自动模式下，2个微件返回2列
        """
        return self.get_effective_columns()

    def set_equal_width(self, equal: bool = True) -> "ColumnWidget":
        """设置列是否等宽。

        Args:
            equal (bool): 是否等宽，默认为True。

        Returns:
            ColumnWidget: 返回self以支持链式调用。

        Note:
            此方法目前仅为预留接口，实际渲染中列宽始终等分。

        Examples:
            >>> column = ColumnWidget().set_equal_width(False)
        """
        self._equal_width = equal
        return self

    def _calculate_auto_columns(self, widget_count: int) -> int:
        """根据微件数量自动计算合适的列数。

        Args:
            widget_count (int): 微件的数量。

        Returns:
            int: 自动计算出的列数。
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
            return 2  # 4个widget用2列，每列2个
        elif widget_count <= 6:
            return 3  # 5-6个widget用3列
        elif widget_count <= 8:
            return 2  # 7-8个widget用2列
        else:
            return 3  # 超过8个widget用3列

    def get_effective_columns(self) -> int:
        """获取实际生效的列数。

        如果设置为自动模式，则根据当前微件数量计算；否则返回手动设置的列数。

        Returns:
            int: 实际使用的列数。
        """
        if self._columns == -1:
            return self._calculate_auto_columns(len(self._widgets))
        else:
            return self._columns

    def _get_template_name(self) -> str:
        return "column.html"

    def get_template_context(self) -> dict[str, Any]:
        """获取模板渲染所需的上下文数据"""
        if not self._widgets:
            return {}

        # 获取有效列数（处理自动模式）
        effective_columns = self.get_effective_columns()

        # 计算列宽度
        column_width = f"{100 / effective_columns:.2f}%"

        # 使用table布局实现列效果 - 邮件客户端兼容
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

        # 分组处理Widget
        widget_groups = []
        for i in range(0, len(self._widgets), effective_columns):
            group = self._widgets[i : i + effective_columns]
            group_html = []
            for widget in group:
                try:
                    widget_html = widget.render_html()
                    group_html.append(widget_html)
                except Exception as e:
                    self._logger.error(f"渲染Widget失败: {e}")
                    group_html.append("<p style='color: red;'>Widget渲染错误</p>")
            widget_groups.append(group_html)

        # 计算最后一行的空列数
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
