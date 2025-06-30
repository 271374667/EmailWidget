"""表格Widget实现"""
from typing import Optional, List, Dict, Any, Union, TYPE_CHECKING

from email_widget.core.base import BaseWidget
from email_widget.core.enums import StatusType
from email_widget.utils.optional_deps import check_optional_dependency, import_optional_dependency

if TYPE_CHECKING:
    import pandas as pd

class TableCell:
    """表格单元格类"""
    
    def __init__(self, 
                 value: Any,
                 status: Optional[StatusType] = None,
                 color: Optional[str] = None,
                 bold: bool = False,
                 align: str = "center"):
        self.value = value
        self.status = status
        self.color = color
        self.bold = bold
        self.align = align

class TableWidget(BaseWidget):
    """表格Widget类"""
    
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
    
    def __init__(self, widget_id: Optional[str] = None):
        super().__init__(widget_id)
        self._dataframe: Optional["pd.DataFrame"] = None
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
    
    def set_dataframe(self, df: "pd.DataFrame") -> 'TableWidget':
        """设置DataFrame数据"""
        check_optional_dependency("pandas", "pandas")
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
    
    def add_data_row(self, row_data: list) -> 'TableWidget':
        """添加数据行（基于DataFrame）"""
        check_optional_dependency("pandas", "pandas")
        pd = import_optional_dependency("pandas", "pandas")
        
        if self._dataframe is not None:
            # 如果已有DataFrame，添加新行
            new_row = pd.Series(row_data, index=self._dataframe.columns)
            self._dataframe = pd.concat([self._dataframe, new_row.to_frame().T], ignore_index=True)
        else:
            # 如果没有DataFrame，创建新的
            self._dataframe = pd.DataFrame([row_data])
        return self
    
    def clear_data(self) -> 'TableWidget':
        """清空表格数据"""
        self._dataframe = None
        self._rows.clear()
        return self
    
    def set_column_width(self, column: str, width: str) -> 'TableWidget':
        """设置列宽度"""
        if not hasattr(self, '_column_widths'):
            self._column_widths = {}
        self._column_widths[column] = width
        return self
    
    def add_status_cell(self, value: str, status: StatusType) -> TableCell:
        """创建状态单元格"""
        return TableCell(value=value, status=status)
    
    def add_colored_cell(self, value: str, color: str, bold: bool = False, align: str = "center") -> TableCell:
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
    def dataframe(self) -> Optional["pd.DataFrame"]:
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
    
    def get_template_context(self) -> Dict[str, Any]:
        """获取模板渲染所需的上下文数据"""
        if not self._headers and not self._rows:
            return {}
        
        # 容器样式 - 居中对齐，左右内边距5px实现边距效果
        container_style = "margin: 16px auto; width: 100%; max-width: 100%; padding: 0 5px; box-sizing: border-box;"
        if self._max_width:
            container_style += f" max-width: {self._max_width};"
        
        # 表格样式 - 邮件客户端兼容，居中对齐
        table_style = f"""
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
        
        th_style = f"""
            padding: 12px 8px;
            text-align: center;
            font-weight: 600;
            color: #323130;
        """
        if self._bordered:
            th_style += f" border-right: 1px solid {self._border_color};"
        
        # 索引列样式 - 居中对齐
        index_td_style = f"""
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
                    
                    cells_data.append({
                        'value': cell.value,
                        'style': td_style
                    })
                else:
                    # 处理普通字符串 - 默认居中对齐
                    td_style += " color: #323130; text-align: center;"
                    if self._bordered:
                        td_style += f" border-right: 1px solid {self._border_color};"
                    
                    cells_data.append({
                        'value': cell,
                        'style': td_style
                    })
            
            rows_data.append({
                'index': idx + 1,
                'row_style': row_style,
                'cells': cells_data
            })
        
        return {
            'title': self._title,
            'container_style': container_style,
            'table_style': table_style,
            'header_style': header_style,
            'index_th_style': index_th_style,
            'th_style': th_style,
            'index_td_style': index_td_style,
            'headers': self._headers,
            'show_index': self._show_index,
            'rows_data': rows_data
        }