"""Email主类实现"""
from typing import List, Union, Optional
from pathlib import Path
import datetime

from src.ewidget.base import BaseWidget
from src.ewidget.config import EmailConfig

class Email:
    """邮件主类"""
    
    def __init__(self, 
                 title: str = "邮件报告",
                 config_path: Optional[str] = None):
        self.title = title
        self.widgets: List[BaseWidget] = []
        self.config = EmailConfig(config_path)
        self._created_at = datetime.datetime.now()
    
    def add_widget(self, widget: BaseWidget) -> 'Email':
        """添加单个Widget"""
        widget._set_parent(self)
        self.widgets.append(widget)
        return self
    
    def add_widgets(self, widgets: List[BaseWidget]) -> 'Email':
        """添加多个Widget"""
        for widget in widgets:
            widget._set_parent(self)
            self.widgets.append(widget)
        return self
    
    def clear_widgets(self) -> 'Email':
        """清空所有Widget"""
        self.widgets.clear()
        return self
    
    def remove_widget(self, widget_id: str) -> 'Email':
        """根据ID移除Widget"""
        self.widgets = [w for w in self.widgets if w.widget_id != widget_id]
        return self
    
    def get_widget(self, widget_id: str) -> Optional[BaseWidget]:
        """根据ID获取Widget"""
        for widget in self.widgets:
            if widget.widget_id == widget_id:
                return widget
        return None
    
    def set_title(self, title: str) -> 'Email':
        """设置邮件标题"""
        self.title = title
        return self
    
    def _generate_css_styles(self) -> str:
        """生成内联CSS样式"""
        primary_color = self.config.get_primary_color()
        font_family = self.config.get_font_family()
        max_width = self.config.get_max_width()
        
        return f"""
        <style>
            body {{
                margin: 0;
                padding: 20px;
                font-family: {font_family};
                line-height: 1.6;
                color: #323130;
                background-color: #faf9f8;
            }}
            
            .email-container {{
                max-width: {max_width};
                margin: 0 auto;
                background: #ffffff;
                border: 1px solid #e1dfdd;
                border-radius: 8px;
                overflow: hidden;
            }}
            
            .email-header {{
                background: {primary_color};
                color: #ffffff;
                padding: 24px;
                text-align: center;
            }}
            
            .email-header h1 {{
                margin: 0;
                font-size: 24px;
                font-weight: 600;
            }}
            
            .email-header .timestamp {{
                margin-top: 8px;
                font-size: 14px;
                opacity: 0.9;
            }}
            
            .email-body {{
                padding: 24px;
            }}
            
            .email-footer {{
                background: #f3f2f1;
                padding: 16px 24px;
                text-align: center;
                font-size: 12px;
                color: #605e5c;
                border-top: 1px solid #e1dfdd;
            }}
            
            /* 通用样式 */
            .fluent-card {{
                background: #ffffff;
                border: 1px solid #e1dfdd;
                border-radius: 4px;
                margin: 16px 0;
                overflow: hidden;
            }}
            
            .fluent-card-elevated {{
                border: 1px solid #d2d0ce;
                box-shadow: 0 1.6px 3.6px 0 rgba(0,0,0,0.132), 0 0.3px 0.9px 0 rgba(0,0,0,0.108);
            }}
            
            /* 响应式设计 */
            @media only screen and (max-width: 600px) {{
                .email-container {{
                    margin: 0;
                    border-radius: 0;
                }}
                
                .email-header, .email-body, .email-footer {{
                    padding: 16px;
                }}
            }}
        </style>
        """
    
    def _render_email(self) -> str:
        """渲染完整邮件HTML"""
        timestamp = self._created_at.strftime("%Y年%m月%d日 %H:%M:%S")
        
        # 生成样式
        styles = self._generate_css_styles()
        
        # 生成Widget内容
        widget_content = ""
        for widget in self.widgets:
            widget_html = widget.render_html()
            if widget_html:
                widget_content += widget_html + "\n"
        
        # 构建完整HTML
        html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.title}</title>
    {styles}
</head>
<body>
    <div class="email-container">
        <div class="email-header">
            <h1>{self.title}</h1>
            <div class="timestamp">生成时间: {timestamp}</div>
        </div>
        
        <div class="email-body">
            {widget_content}
        </div>
        
        <div class="email-footer">
            <p>此邮件由 EWidget 自动生成 | SpiderDaily 项目</p>
        </div>
    </div>
</body>
</html>"""
        
        return html
    
    def export(self, 
               filename: Optional[str] = None,
               output_dir: Optional[str] = None) -> str:
        """导出HTML文件"""
        output_dir = output_dir or self.config.get_output_dir()
        
        if filename is None:
            timestamp = self._created_at.strftime("%Y%m%d_%H%M%S")
            filename = f"{self.title}_{timestamp}.html"
        
        # 确保文件名以.html结尾
        if not filename.endswith('.html'):
            filename += '.html'
        
        output_path = Path(output_dir) / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        html_content = self._render_email()
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return str(output_path)
    
    def preview_html(self) -> str:
        """预览HTML内容"""
        return self._render_email()
    
    def get_widget_count(self) -> int:
        """获取Widget数量"""
        return len(self.widgets)
    
    def __len__(self) -> int:
        """支持len()函数"""
        return len(self.widgets)
    
    def __str__(self) -> str:
        """字符串表示"""
        return f"Email(title='{self.title}', widgets={len(self.widgets)})" 