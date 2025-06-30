"""引用样式Widget实现"""
from typing import Optional, Dict, Any
from email_widget.core.base import BaseWidget
from email_widget.core.enums import StatusType

class QuoteWidget(BaseWidget):
    """引用样式Widget类"""
    
    # 模板定义
    TEMPLATE = """
    {% if content %}
        <blockquote style="{{ container_style }}">
            <p style="{{ content_style }}">"{{ content }}"</p>
            {% if citation %}
                <cite style="{{ citation_style }}">{{ citation }}</cite>
            {% endif %}
        </blockquote>
    {% endif %}
    """
    
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
    
    def set_full_quote(self, content: str, author: str = None, source: str = None) -> 'QuoteWidget':
        """一次性设置完整引用信息"""
        self._content = content
        if author:
            self._author = author
        if source:
            self._source = source
        return self
    
    def clear_attribution(self) -> 'QuoteWidget':
        """清空作者和来源信息"""
        self._author = None
        self._source = None
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
    
    def get_template_context(self) -> Dict[str, Any]:
        """获取模板渲染所需的上下文数据"""
        if not self._content:
            return {}
        
        border_color = self._get_quote_color()
        
        container_style = f"""
            border-left: 4px solid {border_color};
            background: #faf9f8;
            padding: 16px 20px;
            margin: 16px 0;
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
            border-radius: 0 4px 4px 0;
        """
        
        content_style = """
            font-size: 16px;
            line-height: 1.6;
            color: #323130;
            margin: 0 0 12px 0;
            font-style: italic;
        """
        
        citation_style = """
            font-size: 14px;
            color: #605e5c;
            text-align: right;
            margin: 0;
        """
        
        # 处理引用信息
        citation = None
        if self._author or self._source:
            citation_text = ""
            if self._author:
                citation_text += f"— {self._author}"
            if self._source:
                if self._author:
                    citation_text += f", {self._source}"
                else:
                    citation_text += f"— {self._source}"
            citation = citation_text
        
        return {
            'content': self._content,
            'citation': citation,
            'container_style': container_style,
            'content_style': content_style,
            'citation_style': citation_style
        }