"""图片Widget实现"""
from typing import Optional, Union, Dict, Any
from pathlib import Path

from email_widget.core.base import BaseWidget
from email_widget.utils.image_utils import ImageUtils

class ImageWidget(BaseWidget):
    """图片Widget类"""
    
    # 模板定义
    TEMPLATE = """
    {% if image_url %}
        <!--[if mso]>
        <table width="100%" cellpadding="0" cellspacing="0" border="0">
            <tr>
                <td align="center">
        <![endif]-->
        <div style="{{ container_style }}">
            <img src="{{ image_url }}" alt="{{ alt_text }}" 
                 style="{{ img_style }}" 
                 width="{{ img_width }}" 
                 height="{{ img_height }}" />
            {% if show_caption and (title or description) %}
                <div style="margin-top: 8px; width: 100%; max-width: 100%;">
                    {% if title %}
                        <h4 style="margin: 8px 0 4px 0; font-size: 16px; font-weight: 600; color: #323130; text-align: center; font-family: Arial, sans-serif;">{{ title }}</h4>
                    {% endif %}
                    {% if description %}
                        <p style="margin: 4px 0 8px 0; font-size: 14px; color: #605e5c; line-height: 1.4; text-align: center; font-family: Arial, sans-serif;">{{ description }}</p>
                    {% endif %}
                </div>
            {% endif %}
        </div>
        <!--[if mso]>
                </td>
            </tr>
        </table>
        <![endif]-->
    {% endif %}
    """
    
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
    
    def set_image_url(self, image_url: Union[str, Path], cache: bool = True) -> 'ImageWidget':
        """设置图片URL，自动转换为base64嵌入"""
        self._image_url = ImageUtils.process_image_source(image_url, cache=cache)
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
    
    def get_template_context(self) -> Dict[str, Any]:
        """获取模板渲染所需的上下文数据"""
        if not self._image_url:
            return {}
        
        # 构建图片样式 - 邮件客户端兼容
        img_style_parts = [
            f"max-width: {self._max_width}",
            "width: 100%",
            "height: auto",
            "display: block",
            "margin: 0 auto",  # 居中对齐
            "border: 0",  # 移除默认边框
            "outline: none"  # 移除轮廓
        ]
        
        # 图片尺寸属性（邮件客户端更好支持）
        img_width = "auto"
        img_height = "auto"
        
        if self._width:
            img_style_parts.append(f"width: {self._width}")
            img_width = self._width.replace("px", "") if "px" in str(self._width) else self._width
        if self._height:
            img_style_parts.append(f"height: {self._height}")
            img_height = self._height.replace("px", "") if "px" in str(self._height) else self._height
        if self._border_radius:
            img_style_parts.append(f"border-radius: {self._border_radius}")
        
        # 容器样式 - 邮件客户端兼容
        container_style = "margin: 16px 0; text-align: center; width: 100%; max-width: 100%;"
        
        return {
            'image_url': self._image_url,
            'alt_text': self._alt_text,
            'img_style': "; ".join(img_style_parts),
            'img_width': img_width,
            'img_height': img_height,
            'container_style': container_style,
            'title': self._title,
            'description': self._description,
            'show_caption': self._show_caption
        }