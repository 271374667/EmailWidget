"""Circular Progress Widget Implementation"""

from typing import Any

from email_widget.core.base import BaseWidget
from email_widget.core.enums import ProgressTheme
from email_widget.core.validators import RangeValidator, SizeValidator


class CircularProgressWidget(BaseWidget):
    """Create a circular progress indicator.

    Circular progress bars display task completion, resource utilization, or any
    quantifiable percentage data in a compact and intuitive way. They are perfect for dashboards or reports where space is limited.

    Core features:
        - **Dynamic updates**: Supports setting, increasing, decreasing, resetting, or directly completing progress.
        - **Theming**: Provides multiple preset themes (such as success, warning, error) to intuitively reflect status through colors.
        - **Custom appearance**: Can freely adjust the size and line thickness of the progress ring.

    Attributes:
        value (float): Current progress value.
        max_value (float): Maximum progress value, defaults to 100.
        label (Optional[str]): Descriptive text displayed below the progress ring.
        theme (ProgressTheme): Color theme of the progress ring.

    Examples:
        Create a circular progress bar showing task completion:

        ```python
        from email_widget.widgets import CircularProgressWidget
        from email_widget.core.enums import ProgressTheme

        # Create a progress ring representing "success" status
        task_progress = (CircularProgressWidget()
                         .set_value(85)
                         .set_label("Data Processing Progress")
                         .set_theme(ProgressTheme.SUCCESS)
                         .set_size("120px")
                         .set_stroke_width("10px"))

        # Create a resource monitoring ring representing "warning" status
        disk_usage = (CircularProgressWidget()
                      .set_value(92)
                      .set_label("Disk Usage")
                      .set_theme(ProgressTheme.WARNING)
                      .set_size("90px"))
        ```
    """

    # Template definition
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
        """Initialize CircularProgressWidget.

        Args:
            widget_id (Optional[str]): Optional Widget ID.
        """
        super().__init__(widget_id)
        self._value: float = 0.0
        self._max_value: float = 100.0
        self._label: str | None = None
        self._theme: ProgressTheme = ProgressTheme.PRIMARY
        self._size: str = "100px"
        self._stroke_width: str = "8px"

        # Initialize validator
        self._value_validator = RangeValidator(0, 1000000)
        self._size_validator = SizeValidator()

    def set_value(self, value: float) -> "CircularProgressWidget":
        """Set current progress value.

        Args:
            value (float): Progress value, should be between 0 and `max_value`.

        Returns:
            CircularProgressWidget: Returns self to support method chaining.

        Raises:
            ValueError: When value is out of valid range.

        Examples:
            >>> widget = CircularProgressWidget().set_value(75)
        """
        if not self._value_validator.validate(value):
            raise ValueError(
                f"Progress value validation failed: {self._value_validator.get_error_message(value)}"
            )

        self._value = max(0, min(value, self._max_value))
        return self

    def set_max_value(self, max_val: float) -> "CircularProgressWidget":
        """Set maximum value for progress.

        Args:
            max_val (float): Maximum value for progress.

        Returns:
            CircularProgressWidget: Returns self to support method chaining.

        Examples:
            >>> widget = CircularProgressWidget().set_max_value(200)
        """
        self._max_value = max_val
        return self

    def set_label(self, label: str) -> "CircularProgressWidget":
        """Set descriptive label displayed below the progress ring.

        Args:
            label (str): Label text.

        Returns:
            CircularProgressWidget: Returns self to support method chaining.

        Examples:
            >>> widget = CircularProgressWidget().set_label("Task Completion")
        """
        self._label = label
        return self

    def set_theme(self, theme: ProgressTheme) -> "CircularProgressWidget":
        """Set color theme for the progress ring.

        Args:
            theme (ProgressTheme): Progress ring theme enum value.

        Returns:
            CircularProgressWidget: Returns self to support method chaining.

        Examples:
            >>> widget = CircularProgressWidget().set_theme(ProgressTheme.SUCCESS)
        """
        self._theme = theme
        return self

    def set_size(self, size: str) -> "CircularProgressWidget":
        """Set overall size of the circular progress bar.

        Args:
            size (str): CSS size value, such as "100px", "5em".

        Returns:
            CircularProgressWidget: Returns self to support method chaining.

        Raises:
            ValueError: When size format is invalid.

        Examples:
            >>> widget = CircularProgressWidget().set_size("120px")
        """
        if not self._size_validator.validate(size):
            raise ValueError(
                f"Size value validation failed: {self._size_validator.get_error_message(size)}"
            )

        self._size = size
        return self

    def set_stroke_width(self, width: str) -> "CircularProgressWidget":
        """Set line thickness of the circular progress bar.

        Args:
            width (str): CSS width value, such as "8px", "0.5em".

        Returns:
            CircularProgressWidget: Returns self to support method chaining.

        Examples:
            >>> widget = CircularProgressWidget().set_stroke_width("12px")
        """
        self._stroke_width = width
        return self

    def increment(self, amount: float = 1.0) -> "CircularProgressWidget":
        """Increase progress value.

        Args:
            amount (float): Amount to increase, defaults to 1.0.

        Returns:
            CircularProgressWidget: Returns self to support method chaining.

        Examples:
            >>> widget = CircularProgressWidget().set_value(50).increment(10) # Progress becomes 60
        """
        self._value = min(self._max_value, self._value + amount)
        return self

    def decrement(self, amount: float = 1.0) -> "CircularProgressWidget":
        """Decrease progress value.

        Args:
            amount (float): Amount to decrease, defaults to 1.0.

        Returns:
            CircularProgressWidget: Returns self to support method chaining.

        Examples:
            >>> widget = CircularProgressWidget().set_value(50).decrement(5) # Progress becomes 45
        """
        self._value = max(0.0, self._value - amount)
        return self

    def reset(self) -> "CircularProgressWidget":
        """Reset progress to 0.

        Returns:
            CircularProgressWidget: Returns self to support method chaining.

        Examples:
            >>> widget = CircularProgressWidget().set_value(75).reset() # Progress becomes 0
        """
        self._value = 0.0
        return self

    def complete(self) -> "CircularProgressWidget":
        """Set progress to maximum value (100%).

        Returns:
            CircularProgressWidget: Returns self to support method chaining.

        Examples:
            >>> widget = CircularProgressWidget().complete() # Progress becomes 100%
        """
        self._value = self._max_value
        return self

    def _get_theme_color(self) -> str:
        """Get theme color"""
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
        """Get template context data required for rendering"""
        percentage = (self._value / self._max_value) * 100 if self._max_value > 0 else 0
        theme_color = self._get_theme_color()

        # Outer wrapper style
        wrapper_style = "text-align: center; margin: 16px 0;"

        # Use simplified circular progress bar due to email environment limitations
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
