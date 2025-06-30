"""警告框Widget实现"""
from typing import Optional, Dict, Any
from email_widget.ewidget.base import BaseWidget
from email_widget.ewidget.enums import AlertType

class AlertWidget(BaseWidget):
    """警告框Widget类 (GitHub风格)"""
    
    def __init__(self, widget_id: Optional[str] = None):
        super().__init__(widget_id)
        self._content: str = ""
        self._alert_type: AlertType = AlertType.NOTE
        self._title: Optional[str] = None
        self._icon: Optional[str] = None
        self._show_icon: bool = True
        self._border_radius: str = "6px"
        self._padding: str = "16px"
    
    def set_content(self, content: str) -> 'AlertWidget':
        """设置警告内容"""
        self._content = content
        return self
    
    def set_alert_type(self, alert_type: AlertType) -> 'AlertWidget':
        """设置警告类型"""
        self._alert_type = alert_type
        return self
    
    def set_title(self, title: str) -> 'AlertWidget':
        """设置标题"""
        self._title = title
        return self
    
    def set_full_alert(self, content: str, alert_type: AlertType, title: str = None) -> 'AlertWidget':
        """一次性设置完整警告信息"""
        self._content = content
        self._alert_type = alert_type
        if title:
            self._title = title
        return self
    
    def clear_title(self) -> 'AlertWidget':
        """清空标题"""
        self._title = None
        return self
    
    def set_icon(self, icon: str) -> 'AlertWidget':
        """设置图标"""
        self._icon = icon
        return self
    
    def show_icon(self, show: bool = True) -> 'AlertWidget':
        """设置是否显示图标"""
        self._show_icon = show
        return self
    
    def _get_default_title(self) -> str:
        """获取默认标题"""
        titles = {
            AlertType.NOTE: "注意",
            AlertType.TIP: "提示", 
            AlertType.IMPORTANT: "重要",
            AlertType.WARNING: "警告",
            AlertType.CAUTION: "小心"
        }
        return titles[self._alert_type]
    
    def _get_default_icon(self) -> str:
        """获取默认图标"""
        icons = {
            AlertType.NOTE: "ℹ️",
            AlertType.TIP: "💡",
            AlertType.IMPORTANT: "❗",
            AlertType.WARNING: "⚠️", 
            AlertType.CAUTION: "🚨"
        }
        return icons[self._alert_type]
    
    def _get_alert_styles(self) -> Dict[str, str]:
        """获取警告框样式"""
        styles = {
            AlertType.NOTE: {
                "background": "#dbeafe",
                "border": "#3b82f6",
                "color": "#1e40af"
            },
            AlertType.TIP: {
                "background": "#dcfce7", 
                "border": "#22c55e",
                "color": "#15803d"
            },
            AlertType.IMPORTANT: {
                "background": "#fef3c7",
                "border": "#f59e0b", 
                "color": "#d97706"
            },
            AlertType.WARNING: {
                "background": "#fed7aa",
                "border": "#f97316",
                "color": "#ea580c"
            },
            AlertType.CAUTION: {
                "background": "#fecaca",
                "border": "#ef4444",
                "color": "#dc2626"
            }
        }
        return styles[self._alert_type]
    
    def _get_template_name(self) -> str:
        return "alert.html"
    
    def render_html(self) -> str:
        """渲染为HTML"""
        if not self._content:
            return ""
        
        styles = self._get_alert_styles()
        title = self._title or self._get_default_title()
        icon = self._icon or self._get_default_icon()
        
        container_style = f"""
            background: {styles['background']};
            border: 1px solid {styles['border']};
            border-left: 4px solid {styles['border']};
            border-radius: {self._border_radius};
            padding: {self._padding};
            margin: 16px 0;
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
            color: {styles['color']};
        """
        
        html = f'<div style="{container_style}">'
        
        # 标题行
        if self._show_icon:
            html += f'<div style="display: flex; align-items: center; margin-bottom: 8px; font-weight: 600; font-size: 16px;">'
            html += f'<span style="margin-right: 8px; font-size: 18px;">{icon}</span>'
            html += f'<span>{title}</span></div>'
        else:
            html += f'<div style="margin-bottom: 8px; font-weight: 600; font-size: 16px;">{title}</div>'
        
        # 内容
        html += f'<div style="line-height: 1.5; font-size: 14px;">{self._content}</div>'
        html += '</div>'
        
        return html 