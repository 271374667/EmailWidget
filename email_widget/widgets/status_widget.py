"""状态信息Widget实现"""
from typing import List, Optional, Dict, Any
from email_widget.core.base import BaseWidget
from email_widget.core.enums import StatusType, LayoutType

class StatusItem:
    """状态项类"""
    
    def __init__(self, label: str, value: str, status: Optional[StatusType] = None):
        self.label = label
        self.value = value
        self.status = status

class StatusWidget(BaseWidget):
    """状态信息Widget类"""
    
    # 模板定义
    TEMPLATE = """
    {% if items %}
        <div style="{{ container_style }}">
            {% if title %}
                <h3 style="{{ title_style }}">{{ title }}</h3>
            {% endif %}
            {% for item in items %}
                <div style="{{ item.item_style }}">
                    {% if layout == 'horizontal' %}
                        <span style="{{ item.label_style }}">{{ item.label }}</span>
                        <span style="{{ item.value_style }}">{{ item.value }}</span>
                    {% else %}
                        <div style="{{ item.label_style }}">{{ item.label }}</div>
                        <div style="{{ item.value_style }}">{{ item.value }}</div>
                    {% endif %}
                </div>
            {% endfor %}
        </div>
    {% endif %}
    """
    
    def __init__(self, widget_id: Optional[str] = None):
        super().__init__(widget_id)
        self._items: List[StatusItem] = []
        self._title: Optional[str] = None
        self._layout: LayoutType = LayoutType.VERTICAL
    
    def add_status_item(self, label: str, value: str, status: Optional[StatusType] = None) -> 'StatusWidget':
        """添加状态项"""
        self._items.append(StatusItem(label, value, status))
        return self
    
    def set_title(self, title: str) -> 'StatusWidget':
        """设置标题"""
        self._title = title
        return self
    
    def set_layout(self, layout: LayoutType) -> 'StatusWidget':
        """设置布局"""
        self._layout = layout
        return self
    
    def clear_items(self) -> 'StatusWidget':
        """清空状态项"""
        self._items.clear()
        return self
    
    def remove_item(self, label: str) -> 'StatusWidget':
        """移除指定标签的状态项"""
        self._items = [item for item in self._items if item.label != label]
        return self
    
    def update_item(self, label: str, value: str, status: StatusType = None) -> 'StatusWidget':
        """更新指定标签的状态项"""
        for item in self._items:
            if item.label == label:
                item.value = value
                if status:
                    item.status = status
                break
        return self
    
    def get_item_count(self) -> int:
        """获取状态项数量"""
        return len(self._items)
    
    def _get_status_color(self, status: StatusType) -> str:
        """获取状态颜色"""
        colors = {
            StatusType.SUCCESS: "#107c10",
            StatusType.WARNING: "#ff8c00",
            StatusType.ERROR: "#d13438",
            StatusType.INFO: "#0078d4",
            StatusType.PRIMARY: "#0078d4"
        }
        return colors[status]
    
    def _get_template_name(self) -> str:
        return "status_info.html"
    
    def get_template_context(self) -> Dict[str, Any]:
        """获取模板渲染所需的上下文数据"""
        if not self._items:
            return {}
        
        container_style = """
            background: #ffffff;
            border: 1px solid #e1dfdd;
            border-radius: 4px;
            padding: 16px;
            margin: 16px 0;
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
        """
        
        title_style = "font-size: 16px; font-weight: 600; color: #323130; margin-bottom: 12px;"
        
        # 处理状态项
        items_data = []
        for item in self._items:
            if self._layout == LayoutType.HORIZONTAL:
                item_style = """
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin: 8px 0;
                    padding: 8px 0;
                    border-bottom: 1px solid #f3f2f1;
                """
            else:
                item_style = "margin: 8px 0; padding: 8px 0; border-bottom: 1px solid #f3f2f1;"
            
            label_style = "font-weight: 500; color: #605e5c; font-size: 14px;"
            value_style = "color: #323130; font-size: 14px;"
            
            if item.status:
                status_color = self._get_status_color(item.status)
                value_style += f" color: {status_color}; font-weight: 600;"
            
            items_data.append({
                'label': item.label,
                'value': item.value,
                'item_style': item_style,
                'label_style': label_style,
                'value_style': value_style
            })
        
        return {
            'items': items_data,
            'title': self._title,
            'layout': 'horizontal' if self._layout == LayoutType.HORIZONTAL else 'vertical',
            'container_style': container_style,
            'title_style': title_style
        }