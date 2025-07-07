"""警告框Widget实现"""

from typing import Any

from email_widget.core.base import BaseWidget
from email_widget.core.enums import AlertType
from email_widget.core.validators import NonEmptyStringValidator, SizeValidator


class AlertWidget(BaseWidget):
    """创建一个类似 GitHub 风格的警告框（Admonition）。

    该微件用于在邮件中突出显示特定信息，例如注释、提示、警告或重要提醒。
    它支持多种预设的警告类型，每种类型都有独特的颜色和图标，以吸引读者的注意力。

    Attributes:
        content (str): 警告框中显示的主要文本内容。
        alert_type (AlertType): 警告的类型，决定了其外观（颜色和图标）。
        title (Optional[str]): 警告框的自定义标题。如果未设置，将使用基于 `alert_type` 的默认标题。

    Examples:
        一个基本用法，创建一个警告类型的警告框：

        ```python
        from email_widget.widgets import AlertWidget
        from email_widget.core.enums import AlertType

        alert = AlertWidget()
        alert.set_content("系统将在5分钟后进行维护，请及时保存您的工作。")
        alert.set_alert_type(AlertType.WARNING)
        alert.set_title("系统维护通知")

        # 你也可以使用链式调用来简化代码：
        alert_chained = (AlertWidget()
                         .set_content("新功能已上线，快去体验吧！")
                         .set_alert_type(AlertType.TIP)
                         .set_title("产品更新")
                         .set_icon("🎉"))
        ```
    """

    # 模板定义
    TEMPLATE = """
    {% if content %}
        <div style="{{ container_style }}">
            <!-- 标题行 -->
            {% if show_icon %}
                <div style="display: flex; align-items: center; margin-bottom: 8px; font-weight: 600; font-size: 16px;">
                    <span style="margin-right: 8px; font-size: 18px;">{{ icon }}</span>
                    <span>{{ title }}</span>
                </div>
            {% else %}
                <div style="margin-bottom: 8px; font-weight: 600; font-size: 16px;">{{ title }}</div>
            {% endif %}
            
            <!-- 内容 -->
            <div style="line-height: 1.5; font-size: 14px;">{{ content }}</div>
        </div>
    {% endif %}
    """

    def __init__(self, widget_id: str | None = None):
        """初始化AlertWidget。

        Args:
            widget_id (Optional[str]): 可选的Widget ID。
        """
        super().__init__(widget_id)
        self._content: str = ""
        self._alert_type: AlertType = AlertType.NOTE
        self._title: str | None = None
        self._icon: str | None = None
        self._show_icon: bool = True
        self._border_radius: str = "6px"
        self._padding: str = "16px"

        # 初始化验证器
        self._content_validator = NonEmptyStringValidator()
        self._size_validator = SizeValidator()

    def set_content(self, content: str) -> "AlertWidget":
        """设置警告框中显示的主要文本内容。

        Args:
            content (str): 警告内容。

        Returns:
            AlertWidget: 返回self以支持链式调用。

        Raises:
            ValueError: 当内容为空时。

        Examples:
            >>> alert = AlertWidget().set_content("这是一个重要的通知。")
        """
        if not self._content_validator.validate(content):
            raise ValueError(
                f"警告内容验证失败: {self._content_validator.get_error_message(content)}"
            )

        self._content = content
        return self

    def set_alert_type(self, alert_type: AlertType) -> "AlertWidget":
        """设置警告的类型。

        不同的警告类型会应用不同的颜色和图标。

        Args:
            alert_type (AlertType): 警告类型枚举值。

        Returns:
            AlertWidget: 返回self以支持链式调用。

        Examples:
            >>> alert = AlertWidget().set_alert_type(AlertType.WARNING)
        """
        self._alert_type = alert_type
        return self

    def set_title(self, title: str) -> "AlertWidget":
        """设置警告框的自定义标题。

        如果未设置，将使用基于 `alert_type` 的默认标题。

        Args:
            title (str): 自定义标题文本。

        Returns:
            AlertWidget: 返回self以支持链式调用。

        Examples:
            >>> alert = AlertWidget().set_title("重要通知")
        """
        self._title = title
        return self

    def set_full_alert(
        self, content: str, alert_type: AlertType, title: str = None
    ) -> "AlertWidget":
        """一次性设置完整的警告信息。

        此方法允许同时设置警告内容、类型和可选标题，方便快速配置。

        Args:
            content (str): 警告内容。
            alert_type (AlertType): 警告类型。
            title (str): 可选的自定义标题。

        Returns:
            AlertWidget: 返回self以支持链式调用。

        Examples:
            >>> alert = AlertWidget().set_full_alert("操作成功！", AlertType.TIP, "完成")
        """
        self._content = content
        self._alert_type = alert_type
        if title:
            self._title = title
        return self

    def clear_title(self) -> "AlertWidget":
        """清空警告框的自定义标题。

        调用此方法后，警告框将显示基于 `alert_type` 的默认标题。

        Returns:
            AlertWidget: 返回self以支持链式调用。

        Examples:
            >>> alert = AlertWidget().set_title("自定义标题").clear_title()
        """
        self._title = None
        return self

    def set_icon(self, icon: str) -> "AlertWidget":
        """设置警告框的自定义图标。

        Args:
            icon (str): 图标字符（如表情符号或Unicode字符）。

        Returns:
            AlertWidget: 返回self以支持链式调用。

        Examples:
            >>> alert = AlertWidget().set_icon("🚀")
        """
        self._icon = icon
        return self

    def show_icon(self, show: bool = True) -> "AlertWidget":
        """设置是否显示警告框的图标。

        Args:
            show (bool): 是否显示图标，默认为True。

        Returns:
            AlertWidget: 返回self以支持链式调用。

        Examples:
            >>> alert = AlertWidget().show_icon(False) # 隐藏图标
        """
        self._show_icon = show
        return self

    def _get_default_title(self) -> str:
        """获取默认标题"""
        titles = {
            AlertType.NOTE: "注意",
            AlertType.TIP: "提示",
            AlertType.IMPORTANT: "重要",
            AlertType.WARNING: "警告",
            AlertType.CAUTION: "危险",
        }
        return titles[self._alert_type]

    def _get_default_icon(self) -> str:
        """获取默认图标"""
        icons = {
            AlertType.NOTE: "ℹ️",
            AlertType.TIP: "💡",
            AlertType.IMPORTANT: "❗",
            AlertType.WARNING: "⚠️",
            AlertType.CAUTION: "🚨",
        }
        return icons[self._alert_type]

    def _get_alert_styles(self) -> dict[str, str]:
        """获取警告框样式"""
        styles = {
            AlertType.NOTE: {
                "background": "#dbeafe",
                "border": "#3b82f6",
                "color": "#1e40af",
            },
            AlertType.TIP: {
                "background": "#dcfce7",
                "border": "#22c55e",
                "color": "#15803d",
            },
            AlertType.IMPORTANT: {
                "background": "#fef3c7",
                "border": "#f59e0b",
                "color": "#d97706",
            },
            AlertType.WARNING: {
                "background": "#fed7aa",
                "border": "#f97316",
                "color": "#ea580c",
            },
            AlertType.CAUTION: {
                "background": "#fecaca",
                "border": "#ef4444",
                "color": "#dc2626",
            },
        }
        return styles[self._alert_type]

    def _get_template_name(self) -> str:
        return "alert.html"

    def get_template_context(self) -> dict[str, Any]:
        """获取模板渲染所需的上下文数据"""
        if not self._content:
            return {}

        styles = self._get_alert_styles()
        title = self._title or self._get_default_title()
        icon = self._icon or self._get_default_icon()

        container_style = f"""
            background: {styles["background"]};
            border: 1px solid {styles["border"]};
            border-left: 4px solid {styles["border"]};
            border-radius: {self._border_radius};
            padding: {self._padding};
            margin: 16px 0;
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
            color: {styles["color"]};
        """

        return {
            "content": self._content,
            "container_style": container_style,
            "show_icon": self._show_icon,
            "title": title,
            "icon": icon,
        }
