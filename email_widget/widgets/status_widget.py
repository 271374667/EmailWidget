"""状态信息Widget实现"""

from typing import Any

from email_widget.core.base import BaseWidget
from email_widget.core.enums import LayoutType, StatusType


class StatusItem:
    """表示单个状态项的数据结构.

    每个状态项包含一个标签（描述）、一个值以及一个可选的状态类型，
    用于在 `StatusWidget` 中展示.

    Attributes:
        label (str): 状态项的描述性标签.
        value (str): 状态项的实际值.
        status (Optional[StatusType]): 状态项的类型，用于决定值的颜色.

    Examples:
        ```python
        from email_widget.widgets import StatusItem
        from email_widget.core.enums import StatusType

        # 创建一个成功状态的CPU使用率项
        cpu_status = StatusItem("CPU Usage", "15%", StatusType.SUCCESS)

        # 创建一个普通的信息项
        uptime_info = StatusItem("System Uptime", "30 days")
        ```
    """

    def __init__(self, label: str, value: str, status: StatusType | None = None):
        """初始化StatusItem.

        Args:
            label (str): 状态项的描述性标签.
            value (str): 状态项的实际值.
            status (Optional[StatusType]): 状态项的类型，用于决定值的颜色.
        """
        self.label = label
        self.value = value
        self.status = status


class StatusWidget(BaseWidget):
    """创建一个用于显示键值对状态信息的列表.

    该微件非常适合用于展示系统监控指标、服务状态、配置参数等一系列
    结构化的数据.每一项都由一个标签（Label）和一个值（Value）组成，并且
    可以根据状态（如成功、警告、错误）显示不同的颜色.

    核心功能:
        - **键值对列表**: 以清晰的列表形式展示多个状态项.
        - **布局切换**: 支持垂直（默认）和水平两种布局方式.
        **状态着色**: 可以为每个状态项的值设置不同的颜色，以直观反映其状态.
        - **动态管理**: 支持在运行时添加、更新或移除状态项.

    Attributes:
        items (List[StatusItem]): 包含所有状态项的列表.
        title (Optional[str]): 整个状态列表的标题.
        layout (LayoutType): 列表的布局方式（垂直或水平）

    Examples:
        创建一个垂直布局的系统监控状态列表：

        ```python
        from email_widget.widgets import StatusWidget
        from email_widget.core.enums import StatusType, LayoutType

        system_monitor = (StatusWidget()\
                          .set_title("System Health Check")\
                          .set_layout(LayoutType.VERTICAL)\
                          .add_status_item("CPU Usage", "15%", StatusType.SUCCESS)\
                          .add_status_item("Memory Usage", "78%", StatusType.WARNING)\
                          .add_status_item("Disk Space", "95%", StatusType.ERROR)\
                          .add_status_item("Uptime", "32 days"))

        # 假设 email 是一个 Email 对象
        # email.add_widget(system_monitor)
        ```

        创建一个水平布局的服务状态列表：

        ```python
        service_status = (StatusWidget()\
                          .set_title("Microservice Status")\
                          .set_layout(LayoutType.HORIZONTAL)\
                          .add_status_item("Authentication Service", "Online", StatusType.SUCCESS)\
                          .add_status_item("Payment Service", "Offline", StatusType.ERROR))
        ```
    """

    # 模板定义
    TEMPLATE = """
    {% if items %}
        <!--[if mso]>
        <table width="100%" cellpadding="0" cellspacing="0" border="0">
            <tr>
                <td>
        <![endif]-->
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
        <!--[if mso]>
                </td>
            </tr>
        </table>
        <![endif]-->
    {% endif %}
    """

    def __init__(self, widget_id: str | None = None):
        """初始化StatusWidget.

        Args:
            widget_id (Optional[str]): 可选的Widget ID.
        """
        super().__init__(widget_id)
        self._items: list[StatusItem] = []
        self._title: str | None = None
        self._layout: LayoutType = LayoutType.VERTICAL

    def add_status_item(
        self, label: str, value: str, status: StatusType | None = None
    ) -> "StatusWidget":
        """添加一个状态项到列表中.

        Args:
            label (str): 状态项的描述性标签.
            value (str): 状态项的实际值.
            status (Optional[StatusType]): 状态项的类型，用于决定值的颜色.

        Returns:
            StatusWidget: 返回self以支持链式调用.

        Examples:
            >>> widget = StatusWidget().add_status_item("服务状态", "运行中", StatusType.SUCCESS)
        """
        self._items.append(StatusItem(label, value, status))
        return self

    def set_title(self, title: str) -> "StatusWidget":
        """设置状态列表的标题.

        Args:
            title (str): 标题文本.

        Returns:
            StatusWidget: 返回self以支持链式调用.

        Examples:
            >>> widget = StatusWidget().set_title("服务器健康状态")
        """
        self._title = title
        return self

    def set_layout(self, layout: LayoutType) -> "StatusWidget":
        """设置状态项的布局方式.

        Args:
            layout (LayoutType): 布局类型，可以是 `LayoutType.VERTICAL` 或 `LayoutType.HORIZONTAL`.

        Returns:
            StatusWidget: 返回self以支持链式调用.

        Examples:
            >>> widget = StatusWidget().set_layout(LayoutType.HORIZONTAL)
        """
        self._layout = layout
        return self

    def clear_items(self) -> "StatusWidget":
        """清空所有状态项.

        Returns:
            StatusWidget: 返回self以支持链式调用.

        Examples:
            >>> widget = StatusWidget().clear_items()
        """
        self._items.clear()
        return self

    def remove_item(self, label: str) -> "StatusWidget":
        """根据标签移除指定的状态项.

        Args:
            label (str): 要移除的状态项的标签.

        Returns:
            StatusWidget: 返回self以支持链式调用.

        Examples:
            >>> widget = StatusWidget().remove_item("CPU Usage")
        """
        self._items = [item for item in self._items if item.label != label]
        return self

    def update_item(
        self, label: str, value: str, status: StatusType = None
    ) -> "StatusWidget":
        """更新指定标签的状态项的值和状态.

        如果找到匹配的标签，则更新其值和状态；否则不执行任何操作.

        Args:
            label (str): 要更新的状态项的标签.
            value (str): 新的值.
            status (StatusType): 可选的新状态类型.

        Returns:
            StatusWidget: 返回self以支持链式调用.

        Examples:
            >>> widget = StatusWidget().update_item("CPU Usage", "20%", StatusType.WARNING)
        """
        for item in self._items:
            if item.label == label:
                item.value = value
                if status:
                    item.status = status
                break
        return self

    def get_item_count(self) -> int:
        """获取当前状态项的数量.

        Returns:
            int: 状态项的数量.

        Examples:
            >>> count = StatusWidget().add_status_item("A", "1").get_item_count()
            >>> print(count) # 输出: 1
        """
        return len(self._items)

    def _get_status_color(self, status: StatusType) -> str:
        """获取状态颜色"""
        colors = {
            StatusType.SUCCESS: "#107c10",
            StatusType.WARNING: "#ff8c00",
            StatusType.ERROR: "#d13438",
            StatusType.INFO: "#0078d4",
            StatusType.PRIMARY: "#0078d4",
        }
        return colors[status]

    def _get_template_name(self) -> str:
        return "status_info.html"

    def get_template_context(self) -> dict[str, Any]:
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

        title_style = (
            "font-size: 16px; font-weight: 600; color: #323130; margin-bottom: 12px;"
        )

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
                item_style = (
                    "margin: 8px 0; padding: 8px 0; border-bottom: 1px solid #f3f2f1;"
                )

            label_style = "font-weight: 500; color: #605e5c; font-size: 14px;"
            value_style = "color: #323130; font-size: 14px;"

            if item.status:
                status_color = self._get_status_color(item.status)
                value_style += f" color: {status_color}; font-weight: 600;"

            items_data.append(
                {
                    "label": item.label,
                    "value": item.value,
                    "item_style": item_style,
                    "label_style": label_style,
                    "value_style": value_style,
                }
            )

        return {
            "items": items_data,
            "title": self._title,
            "layout": "horizontal"
            if self._layout == LayoutType.HORIZONTAL
            else "vertical",
            "container_style": container_style,
            "title_style": title_style,
        }
