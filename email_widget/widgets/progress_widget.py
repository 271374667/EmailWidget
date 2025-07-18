"""Progress Widget Implementation"""

from typing import Any

from email_widget.core.base import BaseWidget
from email_widget.core.enums import ProgressTheme
from email_widget.core.validators import ColorValidator, RangeValidator, SizeValidator


class ProgressWidget(BaseWidget):
    """Create a linear progress bar to visually display task completion status.

    Linear progress bars are a classic way to display task progress, data loading, step completion, and other scenarios.
    They clearly communicate the process from start to finish.

    Core Features:
        - **Dynamic Updates**: Support setting, increasing, decreasing, resetting, or directly completing progress.
        - **Themed**: Provides multiple preset themes (such as success, warning, error) to visually reflect status through color.
        - **Text Labels**: Can add descriptive labels above the progress bar.
        - **Percentage Display**: Option to show precise completion percentage inside the progress bar.
        - **Custom Appearance**: Freely adjust the width, height, border radius, and background color of the progress bar.

    Attributes:
        value (float): Current progress value.
        max_value (float): Maximum progress value, default is 100.
        label (Optional[str]): Descriptive text displayed above the progress bar.
        theme (ProgressTheme): Color theme of the progress bar.

    Examples:
        Create a progress bar showing file download progress:

        ```python
        from email_widget.widgets import ProgressWidget
        from email_widget.core.enums import ProgressTheme

        download_progress = (ProgressWidget()
                             .set_label("File Download Progress")
                             .set_value(75)
                             .set_theme(ProgressTheme.PRIMARY)
                             .set_height("24px"))

        # Assuming email is an Email object
        # email.add_widget(download_progress)
        ```

        Create a progress bar showing storage usage with warning status:

        ```python
        storage_usage = (ProgressWidget()
                         .set_label("Storage Usage")
                         .set_value(95)
                         .set_theme(ProgressTheme.WARNING)
                         .show_percentage(True))
        ```
    """

    # Template definition
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
        """Initialize ProgressWidget.

        Args:
            widget_id (Optional[str]): Optional Widget ID.
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

        # Initialize validators
        self._value_validator = RangeValidator(0, 1000000)  # Support large range of values
        self._size_validator = SizeValidator()
        self._color_validator = ColorValidator()

    def set_value(self, value: float) -> "ProgressWidget":
        """Set the current progress value.

        Args:
            value (float): Progress value, should be between 0 and `max_value`.

        Returns:
            ProgressWidget: Returns self to support method chaining.

        Raises:
            ValueError: When the value is outside the valid range.

        Examples:
            >>> widget = ProgressWidget().set_value(75)
        """
        if not self._value_validator.validate(value):
            raise ValueError(
                f"Progress value validation failed: {self._value_validator.get_error_message(value)}"
            )

        self._value = max(0, min(value, self._max_value))
        return self

    def set_max_value(self, max_val: float) -> "ProgressWidget":
        """Set the maximum progress value.

        Args:
            max_val (float): Maximum progress value.

        Returns:
            ProgressWidget: Returns self to support method chaining.

        Examples:
            >>> widget = ProgressWidget().set_max_value(200)
        """
        self._max_value = max_val
        if self._value > max_val:
            self._value = max_val
        return self

    def set_label(self, label: str) -> "ProgressWidget":
        """Set the descriptive label displayed above the progress bar.

        Args:
            label (str): Label text.

        Returns:
            ProgressWidget: Returns self to support method chaining.

        Examples:
            >>> widget = ProgressWidget().set_label("Task Completion")
        """
        self._label = label
        return self

    def set_theme(self, theme: ProgressTheme) -> "ProgressWidget":
        """Set the color theme of the progress bar.

        Args:
            theme (ProgressTheme): Progress bar theme enum value.

        Returns:
            ProgressWidget: Returns self to support method chaining.

        Examples:
            >>> widget = ProgressWidget().set_theme(ProgressTheme.SUCCESS)
        """
        self._theme = theme
        return self

    def show_percentage(self, show: bool = True) -> "ProgressWidget":
        """Set whether to display percentage text inside the progress bar.

        Args:
            show (bool): Whether to show percentage, default is True.

        Returns:
            ProgressWidget: Returns self to support method chaining.

        Examples:
            >>> widget = ProgressWidget().show_percentage(False) # Hide percentage
        """
        self._show_percentage = show
        return self

    def set_width(self, width: str) -> "ProgressWidget":
        """Set the width of the progress bar.

        Args:
            width (str): CSS width value, such as "100%", "500px".

        Returns:
            ProgressWidget: Returns self to support method chaining.

        Raises:
            ValueError: When the width format is invalid.

        Examples:
            >>> widget = ProgressWidget().set_width("80%")
        """
        if not self._size_validator.validate(width):
            raise ValueError(
                f"Width value validation failed: {self._size_validator.get_error_message(width)}"
            )

        self._width = width
        return self

    def set_height(self, height: str) -> "ProgressWidget":
        """Set the height of the progress bar.

        Args:
            height (str): CSS height value, such as "20px", "1em".

        Returns:
            ProgressWidget: Returns self to support method chaining.

        Examples:
            >>> widget = ProgressWidget().set_height("24px")
        """
        self._height = height
        return self

    def set_border_radius(self, radius: str) -> "ProgressWidget":
        """Set the border radius of the progress bar.

        Args:
            radius (str): CSS border radius value, such as "10px", "50%".

        Returns:
            ProgressWidget: Returns self to support method chaining.

        Examples:
            >>> widget = ProgressWidget().set_border_radius("5px")
        """
        self._border_radius = radius
        return self

    def set_background_color(self, color: str) -> "ProgressWidget":
        """Set the background color of the progress bar.

        Args:
            color (str): CSS color value, such as "#e0e0e0", "lightgray".

        Returns:
            ProgressWidget: Returns self to support method chaining.

        Raises:
            ValueError: When the color format is invalid.

        Examples:
            >>> widget = ProgressWidget().set_background_color("#f0f0f0")
        """
        if not self._color_validator.validate(color):
            raise ValueError(
                f"Background color validation failed: {self._color_validator.get_error_message(color)}"
            )

        self._background_color = color
        return self

    def increment(self, amount: float = 1.0) -> "ProgressWidget":
        """Increase the progress value.

        Args:
            amount (float): Amount to increase, default is 1.0.

        Returns:
            ProgressWidget: Returns self to support method chaining.

        Examples:
            >>> widget = ProgressWidget().set_value(50).increment(10) # Progress becomes 60
        """
        self._value = min(self._max_value, self._value + amount)
        return self

    def decrement(self, amount: float = 1.0) -> "ProgressWidget":
        """Decrease the progress value.

        Args:
            amount (float): Amount to decrease, default is 1.0.

        Returns:
            ProgressWidget: Returns self to support method chaining.

        Examples:
            >>> widget = ProgressWidget().set_value(50).decrement(5) # Progress becomes 45
        """
        self._value = max(0.0, self._value - amount)
        return self

    def reset(self) -> "ProgressWidget":
        """Reset progress to 0.

        Returns:
            ProgressWidget: Returns self to support method chaining.

        Examples:
            >>> widget = ProgressWidget().set_value(75).reset() # Progress becomes 0
        """
        self._value = 0.0
        return self

    def complete(self) -> "ProgressWidget":
        """Set progress to maximum value (100%).

        Returns:
            ProgressWidget: Returns self to support method chaining.

        Examples:
            >>> widget = ProgressWidget().complete() # Progress becomes 100%
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

    def _get_percentage(self) -> float:
        """Get percentage"""
        if self._max_value == 0:
            return 0
        return (self._value / self._max_value) * 100

    @property
    def value(self) -> float:
        """Get the current progress value.

        Returns:
            float: Current progress value.
        """
        return self._value

    @property
    def max_value(self) -> float:
        """Get the maximum progress value.

        Returns:
            float: Maximum progress value.
        """
        return self._max_value

    @property
    def percentage(self) -> float:
        """Get the percentage of current progress.

        Returns:
            float: Current progress percentage (0-100).
        """
        return self._get_percentage()

    def _get_template_name(self) -> str:
        return "progress.html"

    def get_template_context(self) -> dict[str, Any]:
        """Get the context data required for template rendering"""
        percentage = self._get_percentage()
        theme_color = self._get_theme_color()

        # Container style
        container_style = "margin: 16px 0;"

        # Label style
        label_style = """
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
            font-size: 14px;
            font-weight: 600;
            color: #323130;
            margin-bottom: 8px;
        """

        # Progress container style
        progress_container_style = f"""
            width: {self._width};
            height: {self._height};
            background: {self._background_color};
            border-radius: {self._border_radius};
            overflow: hidden;
            position: relative;
        """

        # Progress fill style
        progress_fill_style = f"""
            width: {percentage}%;
            height: 100%;
            background: {theme_color};
            border-radius: {self._border_radius};
            transition: width 0.3s ease;
        """

        # Percentage style
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
