"""列布局Widget实现"""
from typing import List, Optional, Dict, Any
from email_widget.core.base import BaseWidget

class ColumnWidget(BaseWidget):
    """列布局Widget类
    
    用于创建多列布局，将多个Widget按列排列。支持自动列数模式和手动设置列数。
    
    主要功能：
    - 自动列数模式：根据Widget数量自动计算合适的列数
    - 手动列数模式：指定固定的列数（1-4列）
    - 响应式设计：在邮件客户端中保持良好的显示效果
    - 邮件客户端兼容：使用table布局确保在各种邮件客户端中正确显示
    
    自动列数规则：
    - 1个Widget：1列
    - 2个Widget：2列
    - 3个Widget：3列
    - 4个Widget：2列（2×2布局）
    - 5-6个Widget：3列
    - 7-8个Widget：2列
    - 9个以上Widget：3列
    
    Examples:
        >>> # 自动列数模式（默认）
        >>> column = ColumnWidget()
        >>> column.add_widgets([widget1, widget2, widget3])
        >>> print(column.get_current_columns())  # 输出: 3
        
        >>> # 手动设置列数
        >>> column = ColumnWidget().set_columns(2)
        >>> column.add_widgets([widget1, widget2, widget3, widget4])
        >>> print(column.get_current_columns())  # 输出: 2
        
        >>> # 切换回自动模式
        >>> column.set_columns(-1)
        >>> print(column.is_auto_mode())  # 输出: True
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
    
    def __init__(self, widget_id: Optional[str] = None):
        super().__init__(widget_id)
        self._widgets: List[BaseWidget] = []
        self._columns: int = -1  # -1表示自动模式
        self._gap: str = "20px"
    
    def add_widget(self, widget: BaseWidget) -> 'ColumnWidget':
        """添加Widget"""
        self._widgets.append(widget)
        return self
    
    def add_widgets(self, widgets: List[BaseWidget]) -> 'ColumnWidget':
        """添加多个Widget"""
        self._widgets.extend(widgets)
        return self
    
    def set_columns(self, columns: int) -> 'ColumnWidget':
        """设置列数
        
        Args:
            columns: 列数，-1表示自动模式，其他值限制在1-4列
        """
        if columns == -1:
            self._columns = -1  # 自动模式
        else:
            self._columns = max(1, min(columns, 4))  # 限制1-4列
        return self
    
    def set_gap(self, gap: str) -> 'ColumnWidget':
        """设置间隔"""
        self._gap = gap
        return self
    
    def clear_widgets(self) -> 'ColumnWidget':
        """清空Widget"""
        self._widgets.clear()
        return self
    
    def remove_widget(self, widget_id: str) -> 'ColumnWidget':
        """移除Widget"""
        self._widgets = [w for w in self._widgets if w.widget_id != widget_id]
        return self
    
    def remove_widget_by_index(self, index: int) -> 'ColumnWidget':
        """移除指定索引的Widget"""
        if 0 <= index < len(self._widgets):
            self._widgets.pop(index)
        return self
    
    def get_widget_count(self) -> int:
        """获取Widget数量"""
        return len(self._widgets)
    
    def is_auto_mode(self) -> bool:
        """检查是否为自动列数模式"""
        return self._columns == -1
    
    def get_current_columns(self) -> int:
        """获取当前使用的列数（包括自动计算的）"""
        return self.get_effective_columns()
    
    def set_equal_width(self, equal: bool = True) -> 'ColumnWidget':
        """设置是否等宽"""
        self._equal_width = equal
        return self
    
    def _calculate_auto_columns(self, widget_count: int) -> int:
        """根据Widget数量自动计算合适的列数
        
        Args:
            widget_count: Widget数量
            
        Returns:
            合适的列数
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
        """获取有效的列数（处理自动模式）
        
        Returns:
            实际使用的列数
        """
        if self._columns == -1:
            return self._calculate_auto_columns(len(self._widgets))
        else:
            return self._columns
    
    def _get_template_name(self) -> str:
        return "column.html"
    
    def get_template_context(self) -> Dict[str, Any]:
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
            group = self._widgets[i:i + effective_columns]
            group_html = []
            for widget in group:
                try:
                    widget_html = widget.render_html()
                    group_html.append(widget_html)
                except Exception as e:
                    self._logger.error(f"渲染Widget失败: {e}")
                    group_html.append(f"<p style='color: red;'>Widget渲染错误</p>")
            widget_groups.append(group_html)
        
        # 计算最后一行的空列数
        last_group_size = len(self._widgets) % effective_columns
        empty_columns = (effective_columns - last_group_size) if last_group_size > 0 else 0
        
        return {
            'widget_groups': widget_groups,
            'table_style': table_style,
            'cell_style': cell_style,
            'empty_cell_style': empty_cell_style,
            'empty_columns': empty_columns
        }