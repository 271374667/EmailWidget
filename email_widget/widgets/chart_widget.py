"""Chart Widget Implementation

This module provides chart display functionality widget, supporting embedded display of matplotlib/seaborn charts.
"""

import base64
import io
from pathlib import Path
from typing import TYPE_CHECKING, Any

from email_widget.core.base import BaseWidget
from email_widget.core.config import EmailConfig
from email_widget.utils.image_utils import ImageUtils
from email_widget.utils.optional_deps import (
    ChartMixin,
    check_optional_dependency,
)

if TYPE_CHECKING:
    pass


class ChartWidget(BaseWidget, ChartMixin):
    """Embed charts in emails, supporting `matplotlib` and `seaborn`.

    This widget can seamlessly embed dynamically generated charts (such as `matplotlib` or `seaborn` chart objects)
    or static image files (local or URL) into email content. It automatically handles chart
    rendering, Base64 encoding, and Chinese character display issues, greatly facilitating the creation of data visualization reports.

    Core features:
        - **Dynamic chart support**: Directly accepts `matplotlib.pyplot` or `seaborn` chart objects.
        - **Static image support**: Can load images through URL or local file paths.
        - **Automatic Chinese fonts**: Automatically detects and configures appropriate Chinese fonts to ensure normal display of Chinese text in charts.
        - **Content enhancement**: Supports adding titles, descriptions, and data summaries to charts.

    Examples:
        Use `matplotlib` to create a simple bar chart and add it to an email:

        ```python
        import matplotlib.pyplot as plt
        from email_widget.widgets import ChartWidget

        # 1. Create a matplotlib chart
        plt.figure(figsize=(10, 6))
        categories = ['Q1', 'Q2', 'Q3', 'Q4']
        sales = [120, 150, 130, 180]
        plt.bar(categories, sales, color='skyblue')
        plt.title('Annual Sales (10k Yuan)')
        plt.ylabel('Sales')

        # 2. Create ChartWidget and set chart
        chart = (ChartWidget()\
                 .set_chart(plt)  # Pass plt object
                 .set_title("2024 Annual Sales Performance")\
                 .set_description("Quarterly sales comparison chart showing annual sales trends.")\
                 .set_data_summary("Total Sales: 5.8 million yuan, Highest Quarter: Q4"))

        # Assuming email is an Email object
        # email.add_widget(chart)
        ```

        Using external image URL:

        ```python
        chart_from_url = (ChartWidget()\
                          .set_image_url("https://www.example.com/charts/monthly_trends.png")\
                          .set_title("Monthly Trend Chart")\
                          .set_alt_text("A line chart showing monthly growth trends"))
        ```
    """

    # Template definition
    TEMPLATE = """
    {% if image_url %}
        <!--[if mso]>
        <table width="100%" cellpadding="0" cellspacing="0" border="0">
            <tr>
                <td align="center">
        <![endif]-->
        <div style="{{ container_style }}">
            {% if title %}
                <h3 style="{{ title_style }}">{{ title }}</h3>
            {% endif %}
            <div style="width: 100%; max-width: 100%; overflow-x: auto; text-align: center;">
                <img src="{{ image_url }}" alt="{{ alt_text }}" 
                     style="{{ img_style }}" 
                     width="{{ img_width }}" 
                     height="{{ img_height }}" />
            </div>
            {% if description %}
                <p style="{{ desc_style }}">{{ description }}</p>
            {% endif %}
            {% if data_summary %}
                <div style="{{ summary_style }}">Data Summary: {{ data_summary }}</div>
            {% endif %}
        </div>
        <!--[if mso]>
                </td>
            </tr>
        </table>
        <![endif]-->
    {% endif %}
    """

    def __init__(self, widget_id: str | None = None):
        """Initialize ChartWidget.

        Args:
            widget_id (Optional[str]): Optional Widget ID.
        """
        super().__init__(widget_id)
        self._image_url: str | None = None
        self._title: str | None = None
        self._description: str | None = None
        self._alt_text: str = "Chart"
        self._data_summary: str | None = None
        self._max_width: str = "100%"

    def set_image_url(self, image_url: str | Path, cache: bool = True) -> "ChartWidget":
        """Set chart image URL or file path.

        This method supports loading images from network URLs or local file paths. Images are
        automatically processed and converted to Base64-encoded data URIs, directly embedded
        into HTML to ensure compatibility in email clients.

        Args:
            image_url (Union[str, Path]): Image URL string or local file Path object.
            cache (bool): Whether to cache network images, defaults to True.

        Returns:
            ChartWidget: Returns self to support method chaining.

        Raises:
            ValueError: If image URL or path is invalid, or image processing fails.

        Examples:
            >>> # Using URL
            >>> chart = ChartWidget().set_image_url("https://example.com/chart.png")

            >>> # Using local file path
            >>> from pathlib import Path
            >>> chart = ChartWidget().set_image_url(Path("./charts/sales.png"))
        """
        # Validate path existence (for local paths only)
        if isinstance(image_url, (str, Path)):
            path_obj = (
                Path(image_url)
                if isinstance(image_url, str)
                and not image_url.startswith(("http://", "https://", "data:"))
                else None
            )
            if path_obj and not path_obj.exists():
                self._logger.error(f"Image file does not exist: {path_obj}")
                self._image_url = None
                return self

        # Use ImageUtils for unified processing
        self._image_url = ImageUtils.process_image_source(image_url, cache=cache)
        return self

    def set_title(self, title: str) -> "ChartWidget":
        """Set chart title.

        Args:
            title (str): Chart title text.

        Returns:
            ChartWidget: Returns self to support method chaining.

        Examples:
            >>> chart = ChartWidget().set_title("2024 Sales Trends")
        """
        self._title = title
        return self

    def set_description(self, description: str) -> "ChartWidget":
        """Set chart description.

        Args:
            description (str): Chart description text.

        Returns:
            ChartWidget: Returns self to support method chaining.

        Examples:
            >>> chart = ChartWidget().set_description("Shows sales comparison by region")
        """
        self._description = description
        return self

    def set_alt_text(self, alt: str) -> "ChartWidget":
        """Set image alternative text.

        Used for accessibility and when image loading fails.

        Args:
            alt (str): Alternative text.

        Returns:
            ChartWidget: Returns self to support method chaining.

        Examples:
            >>> chart = ChartWidget().set_alt_text("Sales data bar chart")
        """
        self._alt_text = alt
        return self

    def set_data_summary(self, summary: str) -> "ChartWidget":
        """Set data summary.

        Display key data summary information below the chart.

        Args:
            summary (str): Data summary text.

        Returns:
            ChartWidget: Returns self to support method chaining.

        Examples:
            >>> chart = ChartWidget().set_data_summary("Average growth rate: 15.3%, Peak value: ¥500k")
        """
        self._data_summary = summary
        return self

    def set_max_width(self, max_width: str) -> "ChartWidget":
        """Set maximum width of chart container.

        Args:
            max_width (str): CSS maximum width value.

        Returns:
            ChartWidget: Returns self to support method chaining.

        Examples:
            >>> chart = ChartWidget().set_max_width("800px")
            >>> chart = ChartWidget().set_max_width("90%")
        """
        self._max_width = max_width
        return self

    def set_chart(self, plt_obj: Any) -> "ChartWidget":
        """Set matplotlib/seaborn chart object.

        Convert chart object to Base64-encoded PNG image embedded in email.
        Automatically configure Chinese font support.

        Args:
            plt_obj (Any): matplotlib pyplot object or figure object.

        Returns:
            ChartWidget: Returns self to support method chaining.

        Raises:
            ImportError: If matplotlib library is not installed.
            Exception: If chart conversion fails.

        Examples:
            ```python
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.bar(['Q1', 'Q2', 'Q3', 'Q4'], [100, 120, 140, 110])
            ax.set_title('Quarterly Sales')
            chart = ChartWidget().set_chart(plt)

            # Using seaborn
            import seaborn as sns
            sns.barplot(data=df, x='month', y='sales')
            chart = ChartWidget().set_chart(plt)
            ```

        Note:
            After calling this method, the original chart object will be closed to free memory.
            If conversion fails, the image URL will be set to None.
        """
        # Check matplotlib dependency
        check_optional_dependency("matplotlib")

        try:
            # Set Chinese font
            self._configure_chinese_font()

            # Save chart to in-memory byte stream
            img_buffer = io.BytesIO()
            plt_obj.savefig(img_buffer, format="png", bbox_inches="tight", dpi=150)
            img_buffer.seek(0)

            # Convert to base64
            img_base64 = base64.b64encode(img_buffer.getvalue()).decode("utf-8")
            self._image_url = f"data:image/png;base64,{img_base64}"

            # Close chart to free memory
            plt_obj.close()

            img_buffer.close()
        except Exception as e:
            self._logger.error(f"Failed to convert chart: {e}")
            self._image_url = None

        return self

    def _configure_chinese_font(self):
        """Configure matplotlib Chinese font support.

        Get font list from configuration file and automatically select available Chinese fonts.
        If no Chinese fonts are found, use default font and output warning.

        Note:
            This is an internal method, automatically called when set_chart is used.
        """
        try:
            # Import matplotlib modules
            plt = self._import_matplotlib_pyplot()
            fm = self._import_matplotlib_font_manager()

            # Get font list from configuration file
            config = EmailConfig()
            font_list = config.get_chart_fonts()

            # Find available Chinese fonts
            available_fonts = [f.name for f in fm.fontManager.ttflist]

            for font_name in font_list:
                if font_name in available_fonts:
                    plt.rcParams["font.sans-serif"] = [font_name]
                    plt.rcParams["axes.unicode_minus"] = False  # Fix negative sign display issue
                    self._logger.info(f"Using font: {font_name}")
                    break
            else:
                # If no Chinese font found, try using system default
                self._logger.warning("No suitable Chinese font found, may not display Chinese correctly")
                plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
                plt.rcParams["axes.unicode_minus"] = False

        except Exception as e:
            self._logger.error(f"Failed to configure Chinese font: {e}")

    def _get_template_name(self) -> str:
        """Get template name.

        Returns:
            Template file name
        """
        return "chart.html"

    def get_template_context(self) -> dict[str, Any]:
        """Get context data required for template rendering"""
        if not self._image_url:
            return {}

        # Container styles
        container_style = f"""
            background: #ffffff;
            border: 1px solid #e1dfdd;
            border-radius: 4px;
            padding: 16px;
            margin: 16px 0;
            text-align: center;
            max-width: {self._max_width};
        """

        # Title styles
        title_style = """
            font-size: 18px;
            font-weight: 600;
            color: #323130;
            margin-bottom: 12px;
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
        """

        # Image styles
        img_style = """
            max-width: 100%;
            height: auto;
            border-radius: 4px;
            margin: 8px 0;
        """

        # Description styles
        desc_style = """
            font-size: 14px;
            color: #605e5c;
            margin: 12px 0;
            line-height: 1.5;
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
        """

        # Data summary styles
        summary_style = """
            font-size: 13px;
            color: #8e8e93;
            margin-top: 12px;
            padding-top: 12px;
            border-top: 1px solid #f3f2f1;
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
        """

        return {
            "image_url": self._image_url,
            "alt_text": self._alt_text,
            "container_style": container_style,
            "title": self._title,
            "title_style": title_style,
            "img_style": img_style,
            "description": self._description,
            "desc_style": desc_style,
            "data_summary": self._data_summary,
            "summary_style": summary_style,
        }
