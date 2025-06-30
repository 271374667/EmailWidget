"""进度条Widget实现"""
from typing import Optional, Dict, Any
from email_widget.core.base import BaseWidget
from email_widget.core.enums import ProgressTheme

class ProgressWidget(BaseWidget):
    """进度条Widget类"""
    
    # 模板定义
    TEMPLATE = """
    <div style="{{ container_style }}">
        {% if label %}
            <div style="{{ label_style }}">{{ label }}</div>
        {% endif %}
        <div style="{{ progress_container_style }}">
            <div style="{{ progress_fill_style }}"></div>
            {% if show_percentage %}
                <div style="{{ percentage_style }}">{{ percentage }}%</div>
            {% endif %}
        </div>
    </div>
    """
    
    def __init__(self, widget_id: Optional[str] = None):
        super().__init__(widget_id)
        self._value: float = 0.0
        self._max_value: float = 100.0
        self._label: Optional[str] = None
        self._theme: ProgressTheme = ProgressTheme.PRIMARY
        self._show_percentage: bool = True
        self._width: str = "100%"
        self._height: str = "20px"
        self._border_radius: str = "10px"
        self._background_color: str = "#e1dfdd"
    
    def set_value(self, value: float) -> 'ProgressWidget':
        """设置当前值"""
        self._value = max(0, min(value, self._max_value))
        return self
    
    def set_max_value(self, max_val: float) -> 'ProgressWidget':
        """设置最大值"""
        self._max_value = max_val
        if self._value > max_val:
            self._value = max_val
        return self
    
    def set_label(self, label: str) -> 'ProgressWidget':
        """设置标签"""
        self._label = label
        return self
    
    def set_theme(self, theme: ProgressTheme) -> 'ProgressWidget':
        """设置主题"""
        self._theme = theme
        return self
    
    def show_percentage(self, show: bool = True) -> 'ProgressWidget':
        """设置是否显示百分比"""
        self._show_percentage = show
        return self
    
    def set_width(self, width: str) -> 'ProgressWidget':
        """设置宽度"""
        self._width = width
        return self
    
    def set_height(self, height: str) -> 'ProgressWidget':
        """设置高度"""
        self._height = height
        return self
    
    def set_border_radius(self, radius: str) -> 'ProgressWidget':
        """设置边框圆角"""
        self._border_radius = radius
        return self
    
    def set_background_color(self, color: str) -> 'ProgressWidget':
        """设置背景颜色"""
        self._background_color = color
        return self
    
    def increment(self, amount: float = 1.0) -> 'ProgressWidget':
        """增加进度值"""
        self._value = min(self._max_value, self._value + amount)
        return self
    
    def decrement(self, amount: float = 1.0) -> 'ProgressWidget':
        """减少进度值"""
        self._value = max(0.0, self._value - amount)
        return self
    
    def reset(self) -> 'ProgressWidget':
        """重置进度为0"""
        self._value = 0.0
        return self
    
    def complete(self) -> 'ProgressWidget':
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
    
    def _get_percentage(self) -> float:
        """获取百分比"""
        if self._max_value == 0:
            return 0
        return (self._value / self._max_value) * 100
    
    @property
    def value(self) -> float:
        """获取当前值"""
        return self._value
    
    @property
    def max_value(self) -> float:
        """获取最大值"""
        return self._max_value
    
    @property
    def percentage(self) -> float:
        """获取百分比"""
        return self._get_percentage()
    
    def _get_template_name(self) -> str:
        return "progress.html"
    
    def get_template_context(self) -> Dict[str, Any]:
        """获取模板渲染所需的上下文数据"""
        percentage = self._get_percentage()
        theme_color = self._get_theme_color()
        
        # 容器样式
        container_style = "margin: 16px 0;"
        
        # 标签样式
        label_style = """
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
            font-size: 14px;
            font-weight: 600;
            color: #323130;
            margin-bottom: 8px;
        """
        
        # 进度条容器样式
        progress_container_style = f"""
            width: {self._width};
            height: {self._height};
            background: {self._background_color};
            border-radius: {self._border_radius};
            overflow: hidden;
            position: relative;
        """
        
        # 进度条填充样式
        progress_fill_style = f"""
            width: {percentage}%;
            height: 100%;
            background: {theme_color};
            border-radius: {self._border_radius};
            transition: width 0.3s ease;
        """
        
        # 百分比样式
        percentage_style = f"""
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
            font-size: 12px;
            font-weight: 600;
            color: {'#ffffff' if percentage > 50 else '#323130'};
            text-shadow: 0 1px 2px rgba(0,0,0,0.1);
        """
        
        return {
            'container_style': container_style,
            'label': self._label,
            'label_style': label_style,
            'progress_container_style': progress_container_style,
            'progress_fill_style': progress_fill_style,
            'show_percentage': self._show_percentage,
            'percentage': f"{percentage:.1f}",
            'percentage_style': percentage_style
        }