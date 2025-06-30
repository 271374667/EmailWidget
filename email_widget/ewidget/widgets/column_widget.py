"""列布局Widget实现"""
from typing import List, Union, Optional
from email_widget.ewidget.base import BaseWidget

class ColumnWidget(BaseWidget):
    """列布局Widget类"""
    
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
    
    def render_html(self) -> str:
        """渲染为HTML"""
        if not self._widgets:
            return ""
        
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
        
        html = f'<table style="{table_style}">'
        
        # 分组处理Widget
        widget_groups = []
        for i in range(0, len(self._widgets), self._columns):
            widget_groups.append(self._widgets[i:i + self._columns])
        
        for group in widget_groups:
            html += '<tr>'
            
            for widget in group:
                cell_style = f"""
                    width: {column_width};
                    vertical-align: top;
                    padding: 0;
                """
                widget_html = widget.render_html()
                html += f'<td style="{cell_style}">{widget_html}</td>'
            
            # 填充空列
            empty_columns = self._columns - len(group)
            for _ in range(empty_columns):
                html += f'<td style="width: {column_width}; vertical-align: top; padding: 0;"></td>'
            
            html += '</tr>'
        
        html += '</table>'
        return html 