"""卡片Widget实现"""
from typing import Optional, Dict, Union
from src.ewidget.base import BaseWidget
from src.ewidget.enums import StatusType, IconType

class CardWidget(BaseWidget):
    """卡片Widget类"""
    
    def __init__(self, widget_id: Optional[str] = None):
        super().__init__(widget_id)
        self._title: Optional[str] = None
        self._content: str = ""
        self._status: Optional[StatusType] = None
        self._icon: Optional[str] = IconType.INFO.value  # 默认Info图标
        self._metadata: Dict[str, str] = {}
        self._elevated: bool = True
        self._padding: str = "16px"
        self._border_radius: str = "4px"
    
    def set_title(self, title: str) -> 'CardWidget':
        """设置卡片标题"""
        self._title = title
        return self
    
    def set_content(self, content: str) -> 'CardWidget':
        """设置卡片内容"""
        self._content = content
        return self
    
    def set_status(self, status: StatusType) -> 'CardWidget':
        """设置状态"""
        self._status = status
        return self
    
    def set_icon(self, icon: Union[str, IconType]) -> 'CardWidget':
        """设置图标"""
        if isinstance(icon, IconType):
            self._icon = icon.value
        else:
            self._icon = icon
        return self
    
    def add_metadata(self, key: str, value: str) -> 'CardWidget':
        """添加元数据"""
        self._metadata[key] = value
        return self
    
    def set_metadata(self, metadata: Dict[str, str]) -> 'CardWidget':
        """设置元数据"""
        self._metadata = metadata.copy()
        return self
    
    def clear_metadata(self) -> 'CardWidget':
        """清空元数据"""
        self._metadata.clear()
        return self
    
    def _get_template_name(self) -> str:
        return "card.html"
    
    def render_html(self) -> str:
        """渲染为HTML"""
        if not self._title and not self._content:
            return ""
        
        card_style = f"""
            background: #ffffff;
            border: 1px solid #e1dfdd;
            border-radius: {self._border_radius};
            padding: {self._padding};
            margin: 16px 0;
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
        """
        
        if self._elevated:
            card_style += " box-shadow: 0 2px 4px rgba(0,0,0,0.1);"
        
        html = f'<div style="{card_style}">'
        
        if self._title:
            title_style = "font-size: 18px; font-weight: 600; color: #323130; margin-bottom: 8px;"
            if self._icon:
                html += f'<h3 style="{title_style}">{self._icon} {self._title}</h3>'
            else:
                html += f'<h3 style="{title_style}">{self._title}</h3>'
        
        if self._content:
            content_style = "color: #323130; line-height: 1.5; font-size: 14px;"
            html += f'<div style="{content_style}">{self._content}</div>'
        
        if self._metadata:
            html += '<div style="margin-top: 12px; padding-top: 12px; border-top: 1px solid #e1dfdd;">'
            for key, value in self._metadata.items():
                html += f'<div style="margin: 4px 0; font-size: 13px;"><strong>{key}:</strong> {value}</div>'
            html += '</div>'
        
        html += '</div>'
        return html 