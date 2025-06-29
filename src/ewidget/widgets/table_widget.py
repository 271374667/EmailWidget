"""表格Widget实现"""
import pandas as pd
from typing import Optional, List, Dict, Any, Union
from pathlib import Path

from src.ewidget.base import BaseWidget
from src.ewidget.enums import StatusType

class TableCell:
    """表格单元格类"""
    
    def __init__(self, 
                 value: Any,
                 status: Optional[StatusType] = None,
                 color: Optional[str] = None,
                 bold: bool = False,
                 align: str = "left"):
        self.value = value
        self.status = status
        self.color = color
        self.bold = bold
        self.align = align

class TableWidget(BaseWidget):
    """表格Widget类"""
    
    def __init__(self, widget_id: Optional[str] = None):
        super().__init__(widget_id)
        self._dataframe: Optional[pd.DataFrame] = None
        self._title: Optional[str] = None
        self._headers: List[str] = []
        self._rows: List[List[Union[str, TableCell]]] = []
        self._show_index: bool = False
        self._striped: bool = True
        self._bordered: bool = True
        self._hover_effect: bool = True
        self._max_width: Optional[str] = None
        self._header_bg_color: str = "#f3f2f1"
        self._border_color: str = "#e1dfdd"
    
    def set_dataframe(self, df: pd.DataFrame) -> 'TableWidget':
        """设置DataFrame数据"""
        self._dataframe = df.copy()
        self._headers = list(df.columns)
        self._rows = []
        
        for _, row in df.iterrows():
            row_data = []
            for col in df.columns:
                value = row[col]
                if isinstance(value, dict) and 'status' in value:
                    # 处理状态类型数据
                    cell = TableCell(
                        value=value.get('text', str(value)),
                        status=StatusType(value['status']) if 'status' in value else None
                    )
                    row_data.append(cell)
                else:
                    row_data.append(str(value))
            self._rows.append(row_data)
        return self
    
    def set_title(self, title: str) -> 'TableWidget':
        """设置表格标题"""
        self._title = title
        return self
    
    def set_headers(self, headers: List[str]) -> 'TableWidget':
        """设置表头"""
        self._headers = headers.copy()
        return self
    
    def add_row(self, row: List[Union[str, TableCell]]) -> 'TableWidget':
        """添加行数据"""
        self._rows.append(row)
        return self
    
    def set_rows(self, rows: List[List[Union[str, TableCell]]]) -> 'TableWidget':
        """设置所有行数据"""
        self._rows = rows
        return self
    
    def clear_rows(self) -> 'TableWidget':
        """清空行数据"""
        self._rows.clear()
        return self
    
    def show_index(self, show: bool = True) -> 'TableWidget':
        """设置是否显示索引"""
        self._show_index = show
        return self
    
    def set_striped(self, striped: bool = True) -> 'TableWidget':
        """设置是否使用斑马纹"""
        self._striped = striped
        return self
    
    def set_bordered(self, bordered: bool = True) -> 'TableWidget':
        """设置是否显示边框"""
        self._bordered = bordered
        return self
    
    def set_hover_effect(self, hover: bool = True) -> 'TableWidget':
        """设置是否启用悬停效果"""
        self._hover_effect = hover
        return self
    
    def set_max_width(self, width: str) -> 'TableWidget':
        """设置最大宽度"""
        self._max_width = width
        return self
    
    def set_header_bg_color(self, color: str) -> 'TableWidget':
        """设置表头背景色"""
        self._header_bg_color = color
        return self
    
    def set_border_color(self, color: str) -> 'TableWidget':
        """设置边框颜色"""
        self._border_color = color
        return self
    
    def add_status_cell(self, value: str, status: StatusType) -> TableCell:
        """创建状态单元格"""
        return TableCell(value=value, status=status)
    
    def add_colored_cell(self, value: str, color: str, bold: bool = False, align: str = "left") -> TableCell:
        """创建彩色单元格"""
        return TableCell(value=value, color=color, bold=bold, align=align)
    
    def _get_status_style(self, status: StatusType) -> Dict[str, str]:
        """获取状态样式"""
        styles = {
            StatusType.SUCCESS: {"color": "#107c10", "background": "#dff6dd"},
            StatusType.WARNING: {"color": "#ff8c00", "background": "#fff4e6"},
            StatusType.ERROR: {"color": "#d13438", "background": "#ffebee"},
            StatusType.INFO: {"color": "#0078d4", "background": "#e6f3ff"},
            StatusType.PRIMARY: {"color": "#0078d4", "background": "#e6f3ff"}
        }
        return styles.get(status, {"color": "#323130", "background": "#ffffff"})
    
    @property
    def dataframe(self) -> Optional[pd.DataFrame]:
        """获取DataFrame"""
        return self._dataframe
    
    @property
    def title(self) -> Optional[str]:
        """获取标题"""
        return self._title
    
    @property
    def headers(self) -> List[str]:
        """获取表头"""
        return self._headers.copy()
    
    @property
    def rows(self) -> List[List[Union[str, TableCell]]]:
        """获取行数据"""
        return self._rows.copy()
    
    def _get_template_name(self) -> str:
        return "table.html"
    
    def render_html(self) -> str:
        """渲染为HTML"""
        if not self._headers and not self._rows:
            return ""
        
        # 容器样式
        container_style = "margin: 16px 0;"
        if self._max_width:
            container_style += f" max-width: {self._max_width};"
        
        # 表格样式
        table_style = f"""
            width: 100%;
            border-collapse: collapse;
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
            font-size: 14px;
            background: #ffffff;
        """
        
        if self._bordered:
            table_style += f" border: 1px solid {self._border_color};"
        
        html = f'<div style="{container_style}">'
        
        # 标题
        if self._title:
            html += f'<h3 style="margin: 0 0 16px 0; font-size: 18px; font-weight: 600; color: #323130;">{self._title}</h3>'
        
        html += f'<table style="{table_style}">'
        
        # 表头
        if self._headers:
            header_style = f"""
                background: {self._header_bg_color};
                border-bottom: 2px solid {self._border_color};
            """
            
            html += f'<thead style="{header_style}"><tr>'
            
            if self._show_index:
                th_style = f"""
                    padding: 12px 8px;
                    text-align: left;
                    font-weight: 600;
                    color: #323130;
                    border-right: 1px solid {self._border_color};
                """
                html += f'<th style="{th_style}">索引</th>'
            
            for header in self._headers:
                th_style = f"""
                    padding: 12px 8px;
                    text-align: left;
                    font-weight: 600;
                    color: #323130;
                """
                if self._bordered:
                    th_style += f" border-right: 1px solid {self._border_color};"
                
                html += f'<th style="{th_style}">{header}</th>'
            
            html += '</tr></thead>'
        
        # 表体
        html += '<tbody>'
        for idx, row in enumerate(self._rows):
            # 行样式
            row_style = ""
            if self._striped and idx % 2 == 1:
                row_style = "background: #faf9f8;"
            if self._bordered:
                row_style += f" border-bottom: 1px solid {self._border_color};"
            
            html += f'<tr style="{row_style}">'
            
            # 索引列
            if self._show_index:
                td_style = f"""
                    padding: 8px;
                    vertical-align: top;
                    color: #605e5c;
                """
                if self._bordered:
                    td_style += f" border-right: 1px solid {self._border_color};"
                
                html += f'<td style="{td_style}">{idx + 1}</td>'
            
            # 数据列
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
                    
                    html += f'<td style="{td_style}">{cell.value}</td>'
                else:
                    # 处理普通字符串
                    td_style += " color: #323130;"
                    if self._bordered:
                        td_style += f" border-right: 1px solid {self._border_color};"
                    
                    html += f'<td style="{td_style}">{cell}</td>'
            
            html += '</tr>'
        
        html += '</tbody></table></div>'
        return html 