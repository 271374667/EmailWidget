"""文本Widget实现"""
from typing import Optional
from src.ewidget.base import BaseWidget
from src.ewidget.enums import TextAlign

class TextWidget(BaseWidget):
    """文本Widget类"""
    
    def __init__(self, widget_id: Optional[str] = None):
        super().__init__(widget_id)
        self._content: str = ""
        self._font_size: str = "14px"
        self._align: TextAlign = TextAlign.LEFT
        self._color: str = "#323130"
        self._line_height: str = "1.5"
        self._font_weight: str = "normal"
        self._font_family: str = "'Segoe UI', Tahoma, Arial, sans-serif"
        self._margin: str = "16px 0"
        self._max_width: Optional[str] = None
    
    def set_content(self, content: str) -> 'TextWidget':
        """设置文本内容"""
        self._content = content
        return self
    
    def set_font_size(self, size: str) -> 'TextWidget':
        """设置字体大小"""
        self._font_size = size
        return self
    
    def set_align(self, align: TextAlign) -> 'TextWidget':
        """设置文本对齐方式"""
        self._align = align
        return self
    
    def set_color(self, color: str) -> 'TextWidget':
        """设置文本颜色"""
        self._color = color
        return self
    
    def set_line_height(self, height: str) -> 'TextWidget':
        """设置行高"""
        self._line_height = height
        return self
    
    def set_font_weight(self, weight: str) -> 'TextWidget':
        """设置字体粗细"""
        self._font_weight = weight
        return self
    
    def set_font_family(self, family: str) -> 'TextWidget':
        """设置字体族"""
        self._font_family = family
        return self
    
    def set_margin(self, margin: str) -> 'TextWidget':
        """设置外边距"""
        self._margin = margin
        return self
    
    def set_max_width(self, max_width: str) -> 'TextWidget':
        """设置最大宽度"""
        self._max_width = max_width
        return self
    
    def set_bold(self, bold: bool = True) -> 'TextWidget':
        """设置粗体"""
        self._font_weight = "bold" if bold else "normal"
        return self
    
    def set_italic(self, italic: bool = True) -> 'TextWidget':
        """设置斜体"""
        # 这里可以扩展支持斜体样式
        return self
    
    @property
    def content(self) -> str:
        """获取内容"""
        return self._content
    
    @property
    def font_size(self) -> str:
        """获取字体大小"""
        return self._font_size
    
    @property
    def align(self) -> TextAlign:
        """获取对齐方式"""
        return self._align
    
    @property
    def color(self) -> str:
        """获取颜色"""
        return self._color
    
    def _get_template_name(self) -> str:
        return "text.html"
    
    def render_html(self) -> str:
        """渲染为HTML"""
        if not self._content:
            return ""
        
        # 构建样式
        style_parts = [
            f"font-size: {self._font_size}",
            f"text-align: {self._align.value}",
            f"color: {self._color}",
            f"line-height: {self._line_height}",
            f"font-weight: {self._font_weight}",
            f"font-family: {self._font_family}",
            f"margin: {self._margin}"
        ]
        
        if self._max_width:
            style_parts.append(f"max-width: {self._max_width}")
        
        style_attr = "; ".join(style_parts)
        
        # 处理多行文本
        content_lines = self._content.split('\n')
        if len(content_lines) > 1:
            # 多行文本使用div包装
            html = f'<div style="{style_attr}">'
            for line in content_lines:
                if line.strip():
                    html += f'<p style="margin: 4px 0;">{line.strip()}</p>'
                else:
                    html += '<br/>'
            html += '</div>'
        else:
            # 单行文本使用p标签
            html = f'<p style="{style_attr}">{self._content}</p>'
        
        return html 