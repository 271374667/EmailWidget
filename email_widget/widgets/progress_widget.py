"""进度条Widget实现"""

from typing import Any

from email_widget.core.base import BaseWidget
from email_widget.core.enums import ProgressTheme
from email_widget.core.validators import ColorValidator, RangeValidator, SizeValidator


class ProgressWidget(BaseWidget):
    """创建一个线性的进度条，用于可视化地展示任务的完成情况。

    线性进度条是展示任务进度、数据加载、步骤完成度等场景的经典方式。
    它清晰地传达了从起点到终点的过程。

    核心功能:
        - **动态更新**: 支持设置、增加、减少、重置或直接完成进度。
        - **主题化**: 提供多种预设主题（如成功、警告、错误），以颜色直观反映状态。
        - **文本标签**: 可以在进度条上方添加说明性标签。
        - **百分比显示**: 可选择在进度条内部显示精确的完成百分比。
        - **自定义外观**: 可以自由调整进度条的宽度、高度、圆角和背景色。

    Attributes:
        value (float): 当前的进度值。
        max_value (float): 进度的最大值，默认为 100。
        label (Optional[str]): 显示在进度条上方的说明文字。
        theme (ProgressTheme): 进度条的颜色主题。

    Examples:
        创建一个表示文件下载进度的进度条：

        ```python
        from email_widget.widgets import ProgressWidget
        from email_widget.core.enums import ProgressTheme

        download_progress = (ProgressWidget()
                             .set_label("文件下载进度")
                             .set_value(75)
                             .set_theme(ProgressTheme.PRIMARY)
                             .set_height("24px"))

        # 假设 email 是一个 Email 对象
        # email.add_widget(download_progress)
        ```

        创建一个表示存储空间使用率的进度条，并标记为警告状态：

        ```python
        storage_usage = (ProgressWidget()
                         .set_label("存储空间使用率")
                         .set_value(95)
                         .set_theme(ProgressTheme.WARNING)
                         .show_percentage(True))
        ```
    """

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

    def __init__(self, widget_id: str | None = None):
        """初始化ProgressWidget。

        Args:
            widget_id (Optional[str]): 可选的Widget ID。
        """
        super().__init__(widget_id)
        self._value: float = 0.0
        self._max_value: float = 100.0
        self._label: str | None = None
        self._theme: ProgressTheme = ProgressTheme.PRIMARY
        self._show_percentage: bool = True
        self._width: str = "100%"
        self._height: str = "20px"
        self._border_radius: str = "10px"
        self._background_color: str = "#e1dfdd"

        # 初始化验证器
        self._value_validator = RangeValidator(0, 1000000)  # 支持大范围的值
        self._size_validator = SizeValidator()
        self._color_validator = ColorValidator()

    def set_value(self, value: float) -> "ProgressWidget":
        """设置当前的进度值。

        Args:
            value (float): 进度值，应在0到 `max_value` 之间。

        Returns:
            ProgressWidget: 返回self以支持链式调用。

        Raises:
            ValueError: 当值超出有效范围时。

        Examples:
            >>> widget = ProgressWidget().set_value(75)
        """
        if not self._value_validator.validate(value):
            raise ValueError(
                f"进度值验证失败: {self._value_validator.get_error_message(value)}"
            )

        self._value = max(0, min(value, self._max_value))
        return self

    def set_max_value(self, max_val: float) -> "ProgressWidget":
        """设置进度的最大值。

        Args:
            max_val (float): 进度的最大值。

        Returns:
            ProgressWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = ProgressWidget().set_max_value(200)
        """
        self._max_value = max_val
        if self._value > max_val:
            self._value = max_val
        return self

    def set_label(self, label: str) -> "ProgressWidget":
        """设置显示在进度条上方的说明性标签。

        Args:
            label (str): 标签文本。

        Returns:
            ProgressWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = ProgressWidget().set_label("任务完成度")
        """
        self._label = label
        return self

    def set_theme(self, theme: ProgressTheme) -> "ProgressWidget":
        """设置进度条的颜色主题。

        Args:
            theme (ProgressTheme): 进度条主题枚举值。

        Returns:
            ProgressWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = ProgressWidget().set_theme(ProgressTheme.SUCCESS)
        """
        self._theme = theme
        return self

    def show_percentage(self, show: bool = True) -> "ProgressWidget":
        """设置是否在进度条内部显示百分比文本。

        Args:
            show (bool): 是否显示百分比，默认为True。

        Returns:
            ProgressWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = ProgressWidget().show_percentage(False) # 隐藏百分比
        """
        self._show_percentage = show
        return self

    def set_width(self, width: str) -> "ProgressWidget":
        """设置进度条的宽度。

        Args:
            width (str): CSS宽度值，如 "100%", "500px"。

        Returns:
            ProgressWidget: 返回self以支持链式调用。

        Raises:
            ValueError: 当宽度格式无效时。

        Examples:
            >>> widget = ProgressWidget().set_width("80%")
        """
        if not self._size_validator.validate(width):
            raise ValueError(
                f"宽度值验证失败: {self._size_validator.get_error_message(width)}"
            )

        self._width = width
        return self

    def set_height(self, height: str) -> "ProgressWidget":
        """设置进度条的高度。

        Args:
            height (str): CSS高度值，如 "20px", "1em"。

        Returns:
            ProgressWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = ProgressWidget().set_height("24px")
        """
        self._height = height
        return self

    def set_border_radius(self, radius: str) -> "ProgressWidget":
        """设置进度条的边框圆角。

        Args:
            radius (str): CSS边框圆角值，如 "10px", "50%"。

        Returns:
            ProgressWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = ProgressWidget().set_border_radius("5px")
        """
        self._border_radius = radius
        return self

    def set_background_color(self, color: str) -> "ProgressWidget":
        """设置进度条的背景颜色。

        Args:
            color (str): CSS颜色值，如 "#e0e0e0", "lightgray"。

        Returns:
            ProgressWidget: 返回self以支持链式调用。

        Raises:
            ValueError: 当颜色格式无效时。

        Examples:
            >>> widget = ProgressWidget().set_background_color("#f0f0f0")
        """
        if not self._color_validator.validate(color):
            raise ValueError(
                f"背景颜色验证失败: {self._color_validator.get_error_message(color)}"
            )

        self._background_color = color
        return self

    def increment(self, amount: float = 1.0) -> "ProgressWidget":
        """增加进度值。

        Args:
            amount (float): 增加的量，默认为1.0。

        Returns:
            ProgressWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = ProgressWidget().set_value(50).increment(10) # 进度变为60
        """
        self._value = min(self._max_value, self._value + amount)
        return self

    def decrement(self, amount: float = 1.0) -> "ProgressWidget":
        """减少进度值。

        Args:
            amount (float): 减少的量，默认为1.0。

        Returns:
            ProgressWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = ProgressWidget().set_value(50).decrement(5) # 进度变为45
        """
        self._value = max(0.0, self._value - amount)
        return self

    def reset(self) -> "ProgressWidget":
        """重置进度为0。

        Returns:
            ProgressWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = ProgressWidget().set_value(75).reset() # 进度变为0
        """
        self._value = 0.0
        return self

    def complete(self) -> "ProgressWidget":
        """将进度设置为最大值（100%）。

        Returns:
            ProgressWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = ProgressWidget().complete() # 进度变为100%
        """
        self._value = self._max_value
        return self

    def _get_theme_color(self) -> str:
        """获取主题颜色"""
        colors = {
            ProgressTheme.PRIMARY: "#0078d4",
            ProgressTheme.SUCCESS: "#107c10",
            ProgressTheme.WARNING: "#ff8c00",
            ProgressTheme.ERROR: "#d13438",
            ProgressTheme.INFO: "#0078d4",
        }
        return colors[self._theme]

    def _get_percentage(self) -> float:
        """获取百分比"""
        if self._max_value == 0:
            return 0
        return (self._value / self._max_value) * 100

    @property
    def value(self) -> float:
        """获取当前的进度值。

        Returns:
            float: 当前的进度值。
        """
        return self._value

    @property
    def max_value(self) -> float:
        """获取进度的最大值。

        Returns:
            float: 进度的最大值。
        """
        return self._max_value

    @property
    def percentage(self) -> float:
        """获取当前进度的百分比。

        Returns:
            float: 当前进度的百分比（0-100）。
        """
        return self._get_percentage()

    def _get_template_name(self) -> str:
        return "progress.html"

    def get_template_context(self) -> dict[str, Any]:
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
            color: {"#ffffff" if percentage > 50 else "#323130"};
            text-shadow: 0 1px 2px rgba(0,0,0,0.1);
        """

        return {
            "container_style": container_style,
            "label": self._label,
            "label_style": label_style,
            "progress_container_style": progress_container_style,
            "progress_fill_style": progress_fill_style,
            "show_percentage": self._show_percentage,
            "percentage": f"{percentage:.1f}",
            "percentage_style": percentage_style,
        }
