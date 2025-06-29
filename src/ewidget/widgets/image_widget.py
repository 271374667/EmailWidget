"""图片Widget实现"""
from typing import Optional, Union
from pathlib import Path

from src.ewidget.base import BaseWidget

class ImageWidget(BaseWidget):
    """图片Widget类"""
    
    def __init__(self, widget_id: Optional[str] = None):
        super().__init__(widget_id)
        self._image_url: Optional[str] = None
        self._title: Optional[str] = None
        self._description: Optional[str] = None
        self._alt_text: str = ""
        self._width: Optional[str] = None
        self._height: Optional[str] = None
        self._border_radius: str = "4px"
        self._show_caption: bool = True
        self._max_width: str = "100%"
    
    def set_image_url(self, image_url: Union[str, Path]) -> 'ImageWidget':
        """设置图片URL"""
        if isinstance(image_url, Path):
            self._image_url = str(image_url)
        else:
            self._image_url = image_url
        return self
    
    def set_title(self, title: str) -> 'ImageWidget':
        """设置图片标题"""
        self._title = title
        return self
    
    def set_description(self, description: str) -> 'ImageWidget':
        """设置图片描述"""
        self._description = description
        return self
    
    def set_alt_text(self, alt: str) -> 'ImageWidget':
        """设置替代文本"""
        self._alt_text = alt
        return self
    
    def set_size(self, width: Optional[str] = None, height: Optional[str] = None) -> 'ImageWidget':
        """设置图片尺寸"""
        self._width = width
        self._height = height
        return self
    
    def set_border_radius(self, radius: str) -> 'ImageWidget':
        """设置边框圆角"""
        self._border_radius = radius
        return self
    
    def set_max_width(self, max_width: str) -> 'ImageWidget':
        """设置最大宽度"""
        self._max_width = max_width
        return self
    
    def show_caption(self, show: bool = True) -> 'ImageWidget':
        """设置是否显示标题"""
        self._show_caption = show
        return self
    
    @property
    def image_url(self) -> Optional[str]:
        """获取图片URL"""
        return self._image_url
    
    @property
    def title(self) -> Optional[str]:
        """获取标题"""
        return self._title
    
    @property
    def description(self) -> Optional[str]:
        """获取描述"""
        return self._description
    
    @property
    def alt_text(self) -> str:
        """获取替代文本"""
        return self._alt_text
    
    @property
    def width(self) -> Optional[str]:
        """获取宽度"""
        return self._width
    
    @property
    def height(self) -> Optional[str]:
        """获取高度"""
        return self._height
    
    @property
    def border_radius(self) -> str:
        """获取边框圆角"""
        return self._border_radius
    
    @property
    def is_show_caption(self) -> bool:
        """是否显示标题"""
        return self._show_caption
    
    def _get_template_name(self) -> str:
        return "image.html"
    
    def render_html(self) -> str:
        """渲染为HTML"""
        if not self._image_url:
            return ""
        
        # 构建图片样式
        style_parts = [
            f"max-width: {self._max_width}",
            "height: auto",
            "display: block"
        ]
        
        if self._width:
            style_parts.append(f"width: {self._width}")
        if self._height:
            style_parts.append(f"height: {self._height}")
        if self._border_radius:
            style_parts.append(f"border-radius: {self._border_radius}")
        
        style_attr = f'style="{"; ".join(style_parts)}"'
        
        # 生成图片HTML
        html = f'<img src="{self._image_url}" alt="{self._alt_text}" {style_attr} />'
        
        # 添加标题和描述
        if self._show_caption and (self._title or self._description):
            caption_parts = []
            if self._title:
                caption_parts.append(f'<h4 style="margin: 8px 0 4px 0; font-size: 16px; font-weight: 600; color: #323130;">{self._title}</h4>')
            if self._description:
                caption_parts.append(f'<p style="margin: 4px 0 8px 0; font-size: 14px; color: #605e5c; line-height: 1.4;">{self._description}</p>')
            
            caption_html = ''.join(caption_parts)
            html = f'''<div style="margin: 16px 0; text-align: center;">
                {html}
                <div style="margin-top: 8px;">
                    {caption_html}
                </div>
            </div>'''
        else:
            html = f'<div style="margin: 16px 0; text-align: center;">{html}</div>'
        
        return html 