"""基础Widget类定义"""
from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING
import uuid

if TYPE_CHECKING:
    from src.ewidget.email import Email

class BaseWidget(ABC):
    """基础Widget类"""
    
    def __init__(self, widget_id: Optional[str] = None):
        self._widget_id: str = widget_id or self._generate_id()
        self._parent: Optional['Email'] = None
    
    @property
    def widget_id(self) -> str:
        """获取Widget ID"""
        return self._widget_id
    
    @property
    def parent(self) -> Optional['Email']:
        """获取父容器"""
        return self._parent
    
    def _set_parent(self, parent: 'Email') -> None:
        """设置父容器"""
        self._parent = parent
    
    def _generate_id(self) -> str:
        """生成唯一ID"""
        return f"{self.__class__.__name__.lower()}_{uuid.uuid4().hex[:8]}"
    
    @abstractmethod
    def _get_template_name(self) -> str:
        """获取模板名称"""
        pass
    
    @abstractmethod
    def render_html(self) -> str:
        """渲染为HTML"""
        pass
    
    def set_widget_id(self, widget_id: str) -> 'BaseWidget':
        """设置Widget ID"""
        self._widget_id = widget_id
        return self 