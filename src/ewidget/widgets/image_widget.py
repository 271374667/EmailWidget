"""图片Widget实现"""
import base64
import requests
from typing import Optional, Union
from pathlib import Path
from urllib.parse import urlparse

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
        """设置图片URL，自动转换为base64嵌入"""
        try:
            if isinstance(image_url, Path):
                # 本地文件路径
                if image_url.exists():
                    with open(image_url, 'rb') as f:
                        img_data = f.read()
                    img_base64 = base64.b64encode(img_data).decode('utf-8')
                    # 根据文件扩展名确定MIME类型
                    ext = image_url.suffix.lower()
                    mime_type = self._get_mime_type(ext)
                    self._image_url = f"data:{mime_type};base64,{img_base64}"
                else:
                    print(f"图片文件不存在: {image_url}")
                    self._image_url = None
            else:
                # URL字符串
                if image_url.startswith('data:'):
                    # 已经是base64格式
                    self._image_url = image_url
                elif image_url.startswith(('http://', 'https://')):
                    # 网络URL，下载并转换
                    response = requests.get(image_url, timeout=10)
                    if response.status_code == 200:
                        img_data = response.content
                        img_base64 = base64.b64encode(img_data).decode('utf-8')
                        # 从Content-Type获取MIME类型
                        content_type = response.headers.get('content-type', 'image/png')
                        self._image_url = f"data:{content_type};base64,{img_base64}"
                    else:
                        print(f"下载图片失败: {image_url}")
                        self._image_url = None
                else:
                    # 本地文件路径字符串
                    local_path = Path(image_url)
                    return self.set_image_url(local_path)
        except Exception as e:
            print(f"处理图片失败: {e}")
            self._image_url = None
        
        return self
    
    def _get_mime_type(self, ext: str) -> str:
        """根据文件扩展名获取MIME类型"""
        mime_types = {
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.gif': 'image/gif',
            '.bmp': 'image/bmp',
            '.webp': 'image/webp',
            '.svg': 'image/svg+xml'
        }
        return mime_types.get(ext, 'image/png')
    
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