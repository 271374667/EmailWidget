"""圆形进度条Widget实现"""

from typing import Any

from email_widget.core.base import BaseWidget
from email_widget.core.enums import ProgressTheme
from email_widget.core.validators import RangeValidator, SizeValidator


class CircularProgressWidget(BaseWidget):
    """创建一个圆形的进度指示器。

    圆形进度条以紧凑且直观的方式展示任务的完成度、资源的占用率或任何
    可量化的百分比数据。它非常适合用在仪表盘或需要节省空间的报告中。

    核心功能:
        - **动态更新**: 支持设置、增加、减少、重置或直接完成进度。
        - **主题化**: 提供多种预设主题（如成功、警告、错误），以颜色直观反映状态。
        - **自定义外观**: 可以自由调整进度环的大小和线条粗细。

    Attributes:
        value (float): 当前的进度值。
        max_value (float): 进度的最大值，默认为 100。
        label (Optional[str]): 显示在进度环下方的说明文字。
        theme (ProgressTheme): 进度环的颜色主题。

    Examples:
        创建一个显示任务完成度的圆形进度条：

        ```python
        from email_widget.widgets import CircularProgressWidget
        from email_widget.core.enums import ProgressTheme

        # 创建一个表示 "成功" 状态的进度环
        task_progress = (CircularProgressWidget()
                         .set_value(85)
                         .set_label("数据处理进度")
                         .set_theme(ProgressTheme.SUCCESS)
                         .set_size("120px")
                         .set_stroke_width("10px"))

        # 创建一个表示 "警告" 状态的资源监控环
        disk_usage = (CircularProgressWidget()
                      .set_value(92)
                      .set_label("磁盘使用率")
                      .set_theme(ProgressTheme.WARNING)
                      .set_size("90px"))
        ```
    """

    # 模板定义
    TEMPLATE = """
    <div style="{{ wrapper_style }}">
        <div style="{{ container_style }}">
            <div style="{{ inner_style }}">{{ percentage }}%</div>
        </div>
        {% if label %}
            <div style="{{ label_style }}">{{ label }}</div>
        {% endif %}
    </div>
    """

    def __init__(self, widget_id: str | None = None):
        """初始化CircularProgressWidget。

        Args:
            widget_id (Optional[str]): 可选的Widget ID。
        """
        super().__init__(widget_id)
        self._value: float = 0.0
        self._max_value: float = 100.0
        self._label: str | None = None
        self._theme: ProgressTheme = ProgressTheme.PRIMARY
        self._size: str = "100px"
        self._stroke_width: str = "8px"

        # 初始化验证器
        self._value_validator = RangeValidator(0, 1000000)
        self._size_validator = SizeValidator()

    def set_value(self, value: float) -> "CircularProgressWidget":
        """设置当前的进度值。

        Args:
            value (float): 进度值，应在0到 `max_value` 之间。

        Returns:
            CircularProgressWidget: 返回self以支持链式调用。

        Raises:
            ValueError: 当值超出有效范围时。

        Examples:
            >>> widget = CircularProgressWidget().set_value(75)
        """
        if not self._value_validator.validate(value):
            raise ValueError(
                f"进度值验证失败: {self._value_validator.get_error_message(value)}"
            )

        self._value = max(0, min(value, self._max_value))
        return self

    def set_max_value(self, max_val: float) -> "CircularProgressWidget":
        """设置进度的最大值。

        Args:
            max_val (float): 进度的最大值。

        Returns:
            CircularProgressWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = CircularProgressWidget().set_max_value(200)
        """
        self._max_value = max_val
        return self

    def set_label(self, label: str) -> "CircularProgressWidget":
        """设置显示在进度环下方的说明性标签。

        Args:
            label (str): 标签文本。

        Returns:
            CircularProgressWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = CircularProgressWidget().set_label("任务完成度")
        """
        self._label = label
        return self

    def set_theme(self, theme: ProgressTheme) -> "CircularProgressWidget":
        """设置进度环的颜色主题。

        Args:
            theme (ProgressTheme): 进度环主题枚举值。

        Returns:
            CircularProgressWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = CircularProgressWidget().set_theme(ProgressTheme.SUCCESS)
        """
        self._theme = theme
        return self

    def set_size(self, size: str) -> "CircularProgressWidget":
        """设置圆形进度条的整体大小。

        Args:
            size (str): CSS尺寸值，如 "100px", "5em"。

        Returns:
            CircularProgressWidget: 返回self以支持链式调用。

        Raises:
            ValueError: 当尺寸格式无效时。

        Examples:
            >>> widget = CircularProgressWidget().set_size("120px")
        """
        if not self._size_validator.validate(size):
            raise ValueError(
                f"尺寸值验证失败: {self._size_validator.get_error_message(size)}"
            )

        self._size = size
        return self

    def set_stroke_width(self, width: str) -> "CircularProgressWidget":
        """设置圆形进度条的线条粗细。

        Args:
            width (str): CSS宽度值，如 "8px", "0.5em"。

        Returns:
            CircularProgressWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = CircularProgressWidget().set_stroke_width("12px")
        """
        self._stroke_width = width
        return self

    def increment(self, amount: float = 1.0) -> "CircularProgressWidget":
        """增加进度值。

        Args:
            amount (float): 增加的量，默认为1.0。

        Returns:
            CircularProgressWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = CircularProgressWidget().set_value(50).increment(10) # 进度变为60
        """
        self._value = min(self._max_value, self._value + amount)
        return self

    def decrement(self, amount: float = 1.0) -> "CircularProgressWidget":
        """减少进度值。

        Args:
            amount (float): 减少的量，默认为1.0。

        Returns:
            CircularProgressWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = CircularProgressWidget().set_value(50).decrement(5) # 进度变为45
        """
        self._value = max(0.0, self._value - amount)
        return self

    def reset(self) -> "CircularProgressWidget":
        """重置进度为0。

        Returns:
            CircularProgressWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = CircularProgressWidget().set_value(75).reset() # 进度变为0
        """
        self._value = 0.0
        return self

    def complete(self) -> "CircularProgressWidget":
        """将进度设置为最大值（100%）。

        Returns:
            CircularProgressWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = CircularProgressWidget().complete() # 进度变为100%
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

    def _get_template_name(self) -> str:
        return "circular_progress.html"

    def get_template_context(self) -> dict[str, Any]:
        """获取模板渲染所需的上下文数据"""
        percentage = (self._value / self._max_value) * 100 if self._max_value > 0 else 0
        theme_color = self._get_theme_color()

        # 外层包装样式
        wrapper_style = "text-align: center; margin: 16px 0;"

        # 由于邮箱环境限制，使用简化的圆形进度条
        container_style = f"""
            width: {self._size};
            height: {self._size};
            border-radius: 50%;
            background: conic-gradient({theme_color} {percentage * 3.6}deg, #e1dfdd 0deg);
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 16px auto;
            position: relative;
        """

        inner_style = f"""
            width: calc({self._size} - {self._stroke_width} * 2);
            height: calc({self._size} - {self._stroke_width} * 2);
            background: #ffffff;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
            font-size: 14px;
            font-weight: 600;
            color: #323130;
        """

        label_style = """
            text-align: center;
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
            font-size: 14px;
            color: #323130;
            margin-top: 8px;
        """

        return {
            "wrapper_style": wrapper_style,
            "container_style": container_style,
            "inner_style": inner_style,
            "percentage": f"{percentage:.1f}",
            "label": self._label,
            "label_style": label_style,
        }
