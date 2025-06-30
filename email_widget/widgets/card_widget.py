"""卡片Widget实现"""
from typing import Optional, Dict, Union, Any
from email_widget.core.base import BaseWidget
from email_widget.core.enums import StatusType, IconType
from email_widget.core.validators import (
    NonEmptyStringValidator, SizeValidator
)

class CardWidget(BaseWidget):
    """卡片Widget类"""
    
    # 模板定义
    TEMPLATE = """
    {% if title or content %}
        <div style="{{ card_style }}">
            {% if title %}
                <h3 style="{{ title_style }}">
                    {% if icon %}{{ icon }} {% endif %}{{ title }}
                </h3>
            {% endif %}
            {% if content %}
                <div style="{{ content_style }}">{{ content }}</div>
            {% endif %}
            {% if metadata %}
                <div style="{{ metadata_container_style }}">
                    {% for key, value in metadata.items() %}
                        <div style="{{ metadata_item_style }}">
                            <strong>{{ key }}:</strong> {{ value }}
                        </div>
                    {% endfor %}
                </div>
            {% endif %}
        </div>
    {% endif %}
    """
    
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
        
        # 初始化验证器
        self._text_validator = NonEmptyStringValidator()
        self._size_validator = SizeValidator()
    
    def set_title(self, title: str) -> 'CardWidget':
        """设置卡片标题
        
        Args:
            title: 卡片标题
            
        Raises:
            ValueError: 当标题为空时
        """
        if not self._text_validator.validate(title):
            raise ValueError(f"标题验证失败: {self._text_validator.get_error_message(title)}")
        
        self._title = title
        return self
    
    def set_content(self, content: str) -> 'CardWidget':
        """设置卡片内容
        
        Args:
            content: 卡片内容
            
        Raises:
            ValueError: 当内容为空时
        """
        if not self._text_validator.validate(content):
            raise ValueError(f"内容验证失败: {self._text_validator.get_error_message(content)}")
        
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
    
    def get_template_context(self) -> Dict[str, Any]:
        """获取模板渲染所需的上下文数据"""
        if not self._title and not self._content:
            return {}
        
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
        
        title_style = "font-size: 18px; font-weight: 600; color: #323130; margin-bottom: 8px;"
        content_style = "color: #323130; line-height: 1.5; font-size: 14px;"
        metadata_container_style = "margin-top: 12px; padding-top: 12px; border-top: 1px solid #e1dfdd;"
        metadata_item_style = "margin: 4px 0; font-size: 13px;"
        
        return {
            'title': self._title,
            'content': self._content,
            'icon': self._icon,
            'metadata': self._metadata if self._metadata else None,
            'card_style': card_style,
            'title_style': title_style,
            'content_style': content_style,
            'metadata_container_style': metadata_container_style,
            'metadata_item_style': metadata_item_style
        }