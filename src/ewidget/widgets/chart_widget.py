"""图表Widget实现"""
from typing import Optional, Union
from pathlib import Path
from src.ewidget.base import BaseWidget

class ChartWidget(BaseWidget):
    """图表Widget类 (实际上是图片形式)"""
    
    def __init__(self, widget_id: Optional[str] = None):
        super().__init__(widget_id)
        self._image_url: Optional[str] = None
        self._title: Optional[str] = None
        self._description: Optional[str] = None
        self._alt_text: str = "图表"
        self._data_summary: Optional[str] = None
        self._max_width: str = "100%"
    
    def set_image_url(self, image_url: Union[str, Path]) -> 'ChartWidget':
        """设置图表图片URL"""
        if isinstance(image_url, Path):
            self._image_url = str(image_url)
        else:
            self._image_url = image_url
        return self
    
    def set_title(self, title: str) -> 'ChartWidget':
        """设置图表标题"""
        self._title = title
        return self
    
    def set_description(self, description: str) -> 'ChartWidget':
        """设置图表描述"""
        self._description = description
        return self
    
    def set_alt_text(self, alt: str) -> 'ChartWidget':
        """设置替代文本"""
        self._alt_text = alt
        return self
    
    def set_data_summary(self, summary: str) -> 'ChartWidget':
        """设置数据摘要"""
        self._data_summary = summary
        return self
    
    def set_max_width(self, max_width: str) -> 'ChartWidget':
        """设置最大宽度"""
        self._max_width = max_width
        return self
    
    def _get_template_name(self) -> str:
        return "chart.html"
    
    def render_html(self) -> str:
        """渲染为HTML"""
        if not self._image_url:
            return ""
        
        container_style = f"""
            background: #ffffff;
            border: 1px solid #e1dfdd;
            border-radius: 4px;
            padding: 16px;
            margin: 16px 0;
            text-align: center;
            max-width: {self._max_width};
        """
        
        html = f'<div style="{container_style}">'
        
        # 标题
        if self._title:
            title_style = """
                font-size: 18px;
                font-weight: 600;
                color: #323130;
                margin-bottom: 12px;
                font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
            """
            html += f'<h3 style="{title_style}">{self._title}</h3>'
        
        # 图表图片
        img_style = f"""
            max-width: 100%;
            height: auto;
            border-radius: 4px;
            margin: 8px 0;
        """
        html += f'<img src="{self._image_url}" alt="{self._alt_text}" style="{img_style}" />'
        
        # 描述
        if self._description:
            desc_style = """
                font-size: 14px;
                color: #605e5c;
                margin: 12px 0;
                line-height: 1.5;
                font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
            """
            html += f'<p style="{desc_style}">{self._description}</p>'
        
        # 数据摘要
        if self._data_summary:
            summary_style = """
                font-size: 13px;
                color: #8e8e93;
                margin-top: 12px;
                padding-top: 12px;
                border-top: 1px solid #f3f2f1;
                font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
            """
            html += f'<div style="{summary_style}">数据摘要: {self._data_summary}</div>'
        
        html += '</div>'
        return html 