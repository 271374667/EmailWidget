"""列布局Widget实现"""
from typing import List, Optional, Dict, Any
from email_widget.core.base import BaseWidget

class ColumnWidget(BaseWidget):
    """列布局Widget类"""
    
    # 模板定义
    TEMPLATE = """
    {% if widget_groups %}
        <table style="{{ table_style }}">
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
    {% endif %}
    """
    
    def __init__(self, widget_id: Optional[str] = None):
        super().__init__(widget_id)
        self._widgets: List[BaseWidget] = []
        self._columns: int = 2
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
        """设置列数"""
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
    
    def set_equal_width(self, equal: bool = True) -> 'ColumnWidget':
        """设置是否等宽"""
        self._equal_width = equal
        return self
    
    def _get_template_name(self) -> str:
        return "column.html"
    
    def get_template_context(self) -> Dict[str, Any]:
        """获取模板渲染所需的上下文数据"""
        if not self._widgets:
            return {}
        
        # 计算列宽度
        column_width = f"{100 / self._columns:.2f}%"
        
        # 使用table布局实现列效果
        table_style = f"""
            width: 100%;
            table-layout: fixed;
            border-collapse: separate;
            border-spacing: {self._gap} 0;
            margin: 16px 0;
        """
        
        cell_style = f"""
            width: {column_width};
            vertical-align: top;
            padding: 0;
        """
        
        empty_cell_style = f"width: {column_width}; vertical-align: top; padding: 0;"
        
        # 分组处理Widget
        widget_groups = []
        for i in range(0, len(self._widgets), self._columns):
            group = self._widgets[i:i + self._columns]
            group_html = []
            for widget in group:
                widget_html = widget.render_html()
                group_html.append(widget_html)
            widget_groups.append(group_html)
        
        # 计算最后一行的空列数
        last_group_size = len(self._widgets) % self._columns
        empty_columns = (self._columns - last_group_size) if last_group_size > 0 else 0
        
        return {
            'widget_groups': widget_groups,
            'table_style': table_style,
            'cell_style': cell_style,
            'empty_cell_style': empty_cell_style,
            'empty_columns': empty_columns
        }