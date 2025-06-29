"""圆形进度条Widget实现"""
from typing import Optional
from src.ewidget.base import BaseWidget
from src.ewidget.enums import ProgressTheme

class CircularProgressWidget(BaseWidget):
    """圆形进度条Widget类"""
    
    def __init__(self, widget_id: Optional[str] = None):
        super().__init__(widget_id)
        self._value: float = 0.0
        self._max_value: float = 100.0
        self._label: Optional[str] = None
        self._theme: ProgressTheme = ProgressTheme.PRIMARY
        self._size: str = "100px"
        self._stroke_width: str = "8px"
    
    def set_value(self, value: float) -> 'CircularProgressWidget':
        """设置当前值"""
        self._value = max(0, min(value, self._max_value))
        return self
    
    def set_max_value(self, max_val: float) -> 'CircularProgressWidget':
        """设置最大值"""
        self._max_value = max_val
        return self
    
    def set_label(self, label: str) -> 'CircularProgressWidget':
        """设置标签"""
        self._label = label
        return self
    
    def set_theme(self, theme: ProgressTheme) -> 'CircularProgressWidget':
        """设置主题"""
        self._theme = theme
        return self
    
    def set_size(self, size: str) -> 'CircularProgressWidget':
        """设置大小"""
        self._size = size
        return self
    
    def set_stroke_width(self, width: str) -> 'CircularProgressWidget':
        """设置线条宽度"""
        self._stroke_width = width
        return self
    
    def increment(self, amount: float = 1.0) -> 'CircularProgressWidget':
        """增加进度值"""
        self._value = min(self._max_value, self._value + amount)
        return self
    
    def decrement(self, amount: float = 1.0) -> 'CircularProgressWidget':
        """减少进度值"""
        self._value = max(0.0, self._value - amount)
        return self
    
    def reset(self) -> 'CircularProgressWidget':
        """重置进度为0"""
        self._value = 0.0
        return self
    
    def complete(self) -> 'CircularProgressWidget':
        """设置为完成状态（100%）"""
        self._value = self._max_value
        return self
    
    def _get_theme_color(self) -> str:
        """获取主题颜色"""
        colors = {
            ProgressTheme.PRIMARY: "#0078d4",
            ProgressTheme.SUCCESS: "#107c10",
            ProgressTheme.WARNING: "#ff8c00",
            ProgressTheme.ERROR: "#d13438",
            ProgressTheme.INFO: "#0078d4"
        }
        return colors[self._theme]
    
    def _get_template_name(self) -> str:
        return "circular_progress.html"
    
    def render_html(self) -> str:
        """渲染为HTML"""
        percentage = (self._value / self._max_value) * 100 if self._max_value > 0 else 0
        theme_color = self._get_theme_color()
        
        # 由于邮箱环境限制，使用简化的圆形进度条
        container_style = f"""
            width: {self._size};
            height: {self._size};
            border-radius: 50%;
            background: conic-gradient({theme_color} {percentage * 3.6}deg, #e1dfdd 0deg);
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 16px auto;
            position: relative;
        """
        
        inner_style = f"""
            width: calc({self._size} - {self._stroke_width} * 2);
            height: calc({self._size} - {self._stroke_width} * 2);
            background: #ffffff;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
            font-size: 14px;
            font-weight: 600;
            color: #323130;
        """
        
        html = f'<div style="{container_style}">'
        html += f'<div style="{inner_style}">{percentage:.1f}%</div>'
        html += '</div>'
        
        if self._label:
            label_style = """
                text-align: center;
                font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
                font-size: 14px;
                color: #323130;
                margin-top: 8px;
            """
            html += f'<div style="{label_style}">{self._label}</div>'
        
        return f'<div style="text-align: center; margin: 16px 0;">{html}</div>' 