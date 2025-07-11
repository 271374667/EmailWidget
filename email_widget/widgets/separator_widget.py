"""分隔符Widget实现"""

from typing import Any

from email_widget.core.base import BaseWidget
from email_widget.core.enums import SeparatorType, StatusType


class SeparatorWidget(BaseWidget):
    """创建一个分隔符，用于在邮件中分割不同的内容区块.

    该微件可以创建不同样式的分隔线，包括实线、虚线和点线，
    帮助组织邮件内容的层次结构，提升可读性。

    核心功能:
        - **多种样式**: 支持实线、虚线、点线三种分隔符样式.
        - **颜色主题**: 支持基于StatusType的主题颜色配置.
        - **灵活配置**: 可自定义颜色、粗细、宽度和边距.
        - **邮件兼容**: 使用邮件客户端兼容的CSS实现.

    Attributes:
        separator_type (SeparatorType): 分隔符类型.
        color (str): 分隔符颜色.
        thickness (str): 分隔符粗细.
        width (str): 分隔符宽度.
        margin (str): 上下边距.

    Examples:
        创建一个基础的实线分隔符：

        ```python
        from email_widget.widgets import SeparatorWidget
        from email_widget.core.enums import SeparatorType

        separator = SeparatorWidget().set_type(SeparatorType.SOLID)

        # 假设 email 是一个 Email 对象
        # email.add_widget(separator)
        ```

        创建一个带颜色的虚线分隔符：

        ```python
        colorful_separator = (SeparatorWidget()
                               .set_type(SeparatorType.DASHED)
                               .set_color("#ff8c00")
                               .set_thickness("3px"))
        ```

        创建一个占据50%宽度的点线分隔符：

        ```python
        narrow_separator = (SeparatorWidget()
                            .set_type(SeparatorType.DOTTED)
                            .set_width("50%")
                            .set_margin("30px"))
        ```
    """

    # 模板定义
    TEMPLATE = """
    {% if show_separator %}
        <!--[if mso]>
        <table width="100%" cellpadding="0" cellspacing="0" border="0">
            <tr>
                <td>
        <![endif]-->
        <div style="{{ container_style }}">
            <div style="{{ separator_style }}"></div>
        </div>
        <!--[if mso]>
                </td>
            </tr>
        </table>
        <![endif]-->
    {% endif %}
    """

    def __init__(self, widget_id: str | None = None):
        """初始化SeparatorWidget.

        Args:
            widget_id (Optional[str]): 可选的Widget ID.
        """
        super().__init__(widget_id)
        self._separator_type: SeparatorType = SeparatorType.SOLID
        self._color: str = "#e1dfdd"
        self._thickness: str = "1px"
        self._width: str = "100%"
        self._margin: str = "16px"

    def set_type(self, separator_type: SeparatorType) -> "SeparatorWidget":
        """设置分隔符类型.

        Args:
            separator_type (SeparatorType): 分隔符类型枚举值.

        Returns:
            SeparatorWidget: 返回self以支持链式调用.

        Examples:
            >>> separator = SeparatorWidget().set_type(SeparatorType.DASHED)
        """
        self._separator_type = separator_type
        return self

    def set_color(self, color: str) -> "SeparatorWidget":
        """设置分隔符颜色.

        Args:
            color (str): CSS颜色值，支持十六进制、RGB、颜色名称等.

        Returns:
            SeparatorWidget: 返回self以支持链式调用.

        Examples:
            >>> separator = SeparatorWidget().set_color("#0078d4")
            >>> separator = SeparatorWidget().set_color("blue")
            >>> separator = SeparatorWidget().set_color("rgb(0, 120, 212)")
        """
        self._color = color
        return self

    def set_thickness(self, thickness: str) -> "SeparatorWidget":
        """设置分隔符粗细.

        Args:
            thickness (str): CSS长度值，如 "1px", "2px", "3px" 等.

        Returns:
            SeparatorWidget: 返回self以支持链式调用.

        Examples:
            >>> separator = SeparatorWidget().set_thickness("2px")
        """
        self._thickness = thickness
        return self

    def set_width(self, width: str) -> "SeparatorWidget":
        """设置分隔符宽度.

        Args:
            width (str): CSS宽度值，如 "100%", "50%", "200px" 等.

        Returns:
            SeparatorWidget: 返回self以支持链式调用.

        Examples:
            >>> separator = SeparatorWidget().set_width("80%")
            >>> separator = SeparatorWidget().set_width("300px")
        """
        self._width = width
        return self

    def set_margin(self, margin: str) -> "SeparatorWidget":
        """设置分隔符上下边距.

        Args:
            margin (str): CSS边距值，如 "16px", "20px", "1em" 等.

        Returns:
            SeparatorWidget: 返回self以支持链式调用.

        Examples:
            >>> separator = SeparatorWidget().set_margin("20px")
        """
        self._margin = margin
        return self

    def set_theme_color(self, status_type: StatusType) -> "SeparatorWidget":
        """根据状态类型设置主题颜色.

        Args:
            status_type (StatusType): 状态类型枚举值.

        Returns:
            SeparatorWidget: 返回self以支持链式调用.

        Examples:
            >>> separator = SeparatorWidget().set_theme_color(StatusType.SUCCESS)
        """
        colors = {
            StatusType.SUCCESS: "#107c10",
            StatusType.WARNING: "#ff8c00",
            StatusType.ERROR: "#d13438",
            StatusType.INFO: "#0078d4",
            StatusType.PRIMARY: "#0078d4",
        }
        self._color = colors[status_type]
        return self

    def set_style(
        self,
        separator_type: SeparatorType = None,
        color: str = None,
        thickness: str = None,
        width: str = None,
        margin: str = None,
    ) -> "SeparatorWidget":
        """一次性设置分隔符的多个样式属性.

        Args:
            separator_type (SeparatorType, optional): 分隔符类型.
            color (str, optional): 分隔符颜色.
            thickness (str, optional): 分隔符粗细.
            width (str, optional): 分隔符宽度.
            margin (str, optional): 上下边距.

        Returns:
            SeparatorWidget: 返回self以支持链式调用.

        Examples:
            >>> separator = SeparatorWidget().set_style(
            ...     separator_type=SeparatorType.DASHED,
            ...     color="#ff8c00",
            ...     thickness="2px",
            ...     width="80%",
            ...     margin="20px"
            ... )
        """
        if separator_type is not None:
            self._separator_type = separator_type
        if color is not None:
            self._color = color
        if thickness is not None:
            self._thickness = thickness
        if width is not None:
            self._width = width
        if margin is not None:
            self._margin = margin
        return self

    def reset_to_default(self) -> "SeparatorWidget":
        """重置所有样式为默认值.

        Returns:
            SeparatorWidget: 返回self以支持链式调用.

        Examples:
            >>> separator = SeparatorWidget().reset_to_default()
        """
        self._separator_type = SeparatorType.SOLID
        self._color = "#e1dfdd"
        self._thickness = "1px"
        self._width = "100%"
        self._margin = "16px"
        return self

    def _get_border_style(self) -> str:
        """根据分隔符类型获取CSS边框样式"""
        if self._separator_type == SeparatorType.SOLID:
            return "solid"
        elif self._separator_type == SeparatorType.DASHED:
            return "dashed"
        elif self._separator_type == SeparatorType.DOTTED:
            return "dotted"
        else:
            return "solid"

    def _get_template_name(self) -> str:
        return "separator.html"

    def get_template_context(self) -> dict[str, Any]:
        """获取模板渲染所需的上下文数据"""

        container_style = f"""
            text-align: center;
            margin: {self._margin} 0;
            width: 100%;
        """

        border_style = self._get_border_style()

        separator_style = f"""
            width: {self._width};
            height: 0;
            border-top: {self._thickness} {border_style} {self._color};
            margin: 0 auto;
            display: inline-block;
        """

        return {
            "show_separator": True,
            "container_style": container_style,
            "separator_style": separator_style,
        }

    # 只读属性
    @property
    def separator_type(self) -> SeparatorType:
        """获取分隔符类型"""
        return self._separator_type

    @property
    def color(self) -> str:
        """获取分隔符颜色"""
        return self._color

    @property
    def thickness(self) -> str:
        """获取分隔符粗细"""
        return self._thickness

    @property
    def width(self) -> str:
        """获取分隔符宽度"""
        return self._width

    @property
    def margin(self) -> str:
        """获取分隔符边距"""
        return self._margin
