"""文本Widget实现"""
from typing import Optional, Dict, List
from src.ewidget.base import BaseWidget
from src.ewidget.enums import TextAlign, TextType

class SectionNumberManager:
    """章节编号管理器"""
    _instance = None
    _counters: Dict[int, int] = {}  # 级别 -> 计数器
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._counters = {2: 0, 3: 0, 4: 0, 5: 0}
        return cls._instance
    
    def get_next_number(self, level: int) -> str:
        """获取下一个章节编号"""
        # 重置低级别计数器
        for l in range(level + 1, 6):
            self._counters[l] = 0
        
        # 增加当前级别计数器
        self._counters[level] += 1
        
        # 生成编号字符串
        numbers = []
        for l in range(2, level + 1):
            if self._counters[l] > 0:
                numbers.append(str(self._counters[l]))
        
        return '.'.join(numbers) + '.'
    
    def reset(self):
        """重置所有计数器"""
        self._counters = {2: 0, 3: 0, 4: 0, 5: 0}

class TextWidget(BaseWidget):
    """文本Widget类"""
    
    def __init__(self, widget_id: Optional[str] = None):
        super().__init__(widget_id)
        self._content: str = ""
        self._text_type: TextType = TextType.BODY
        self._font_size: str = "14px"
        self._align: TextAlign = TextAlign.LEFT
        self._color: str = "#323130"
        self._line_height: str = "1.5"
        self._font_weight: str = "normal"
        self._font_family: str = "'Segoe UI', Tahoma, Arial, sans-serif"
        self._margin: str = "16px 0"
        self._max_width: Optional[str] = None
        self._section_number: Optional[str] = None
        self._section_manager = SectionNumberManager()
    
    def set_content(self, content: str) -> 'TextWidget':
        """设置文本内容"""
        self._content = content
        return self
    
    def set_type(self, text_type: TextType) -> 'TextWidget':
        """设置文本类型"""
        self._text_type = text_type
        self._apply_type_styles()
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
    
    @staticmethod
    def reset_section_numbers():
        """重置章节编号"""
        manager = SectionNumberManager()
        manager.reset()
    
    def _apply_type_styles(self) -> None:
        """根据文本类型应用样式"""
        if self._text_type == TextType.TITLE_LARGE:
            self._font_size = "28px"
            self._font_weight = "bold"
            self._color = "#323130"
            self._align = TextAlign.CENTER
            self._margin = "24px 0 16px 0"
        elif self._text_type == TextType.TITLE_SMALL:
            self._font_size = "20px"
            self._font_weight = "600"
            self._color = "#605e5c"
            self._align = TextAlign.CENTER
            self._margin = "20px 0 12px 0"
        elif self._text_type == TextType.BODY:
            self._font_size = "14px"
            self._font_weight = "normal"
            self._color = "#323130"
            self._align = TextAlign.LEFT
            self._margin = "16px 0"
        elif self._text_type == TextType.CAPTION:
            self._font_size = "12px"
            self._font_weight = "normal"
            self._color = "#8e8e93"
            self._align = TextAlign.LEFT
            self._margin = "8px 0"
        elif self._text_type == TextType.SECTION_H2:
            self._font_size = "24px"
            self._font_weight = "bold"
            self._color = "#323130"
            self._align = TextAlign.LEFT
            self._margin = "20px 0 12px 0"
            self._section_number = self._section_manager.get_next_number(2)
        elif self._text_type == TextType.SECTION_H3:
            self._font_size = "20px"
            self._font_weight = "600"
            self._color = "#323130"
            self._align = TextAlign.LEFT
            self._margin = "18px 0 10px 0"
            self._section_number = self._section_manager.get_next_number(3)
        elif self._text_type == TextType.SECTION_H4:
            self._font_size = "18px"
            self._font_weight = "600"
            self._color = "#323130"
            self._align = TextAlign.LEFT
            self._margin = "16px 0 8px 0"
            self._section_number = self._section_manager.get_next_number(4)
        elif self._text_type == TextType.SECTION_H5:
            self._font_size = "16px"
            self._font_weight = "500"
            self._color = "#323130"
            self._align = TextAlign.LEFT
            self._margin = "14px 0 6px 0"
            self._section_number = self._section_manager.get_next_number(5)
    
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
        
        # 处理内容，如果是章节标题则添加编号
        content = self._content
        if self._section_number:
            content = f"{self._section_number} {content}"
        
        # 处理多行文本
        content_lines = content.split('\n')
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
            html = f'<p style="{style_attr}">{content}</p>'
        
        return html 