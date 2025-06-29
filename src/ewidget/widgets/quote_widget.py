"""引用样式Widget实现"""
from typing import Optional
from src.ewidget.base import BaseWidget
from src.ewidget.enums import StatusType

class QuoteWidget(BaseWidget):
    """引用样式Widget类"""
    
    def __init__(self, widget_id: Optional[str] = None):
        super().__init__(widget_id)
        self._content: str = ""
        self._author: Optional[str] = None
        self._source: Optional[str] = None
        self._quote_type: StatusType = StatusType.INFO
    
    def set_content(self, content: str) -> 'QuoteWidget':
        """设置引用内容"""
        self._content = content
        return self
    
    def set_author(self, author: str) -> 'QuoteWidget':
        """设置作者"""
        self._author = author
        return self
    
    def set_source(self, source: str) -> 'QuoteWidget':
        """设置来源"""
        self._source = source
        return self
    
    def set_quote_type(self, quote_type: StatusType) -> 'QuoteWidget':
        """设置引用类型"""
        self._quote_type = quote_type
        return self
    
    def _get_quote_color(self) -> str:
        """获取引用颜色"""
        colors = {
            StatusType.SUCCESS: "#107c10",
            StatusType.WARNING: "#ff8c00",
            StatusType.ERROR: "#d13438",
            StatusType.INFO: "#0078d4",
            StatusType.PRIMARY: "#0078d4"
        }
        return colors[self._quote_type]
    
    def _get_template_name(self) -> str:
        return "quote.html"
    
    def render_html(self) -> str:
        """渲染为HTML"""
        if not self._content:
            return ""
        
        border_color = self._get_quote_color()
        
        container_style = f"""
            border-left: 4px solid {border_color};
            background: #faf9f8;
            padding: 16px 20px;
            margin: 16px 0;
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
            border-radius: 0 4px 4px 0;
        """
        
        html = f'<blockquote style="{container_style}">'
        
        # 引用内容
        content_style = """
            font-size: 16px;
            line-height: 1.6;
            color: #323130;
            margin: 0 0 12px 0;
            font-style: italic;
        """
        html += f'<p style="{content_style}">"{self._content}"</p>'
        
        # 作者和来源
        if self._author or self._source:
            citation_style = """
                font-size: 14px;
                color: #605e5c;
                text-align: right;
                margin: 0;
            """
            
            citation = ""
            if self._author:
                citation += f"— {self._author}"
            if self._source:
                if self._author:
                    citation += f", {self._source}"
                else:
                    citation += f"— {self._source}"
            
            html += f'<cite style="{citation_style}">{citation}</cite>'
        
        html += '</blockquote>'
        return html 