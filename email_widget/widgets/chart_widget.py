"""图表Widget实现

这个模块提供了图表显示功能的Widget，支持matplotlib/seaborn图表的嵌入显示.
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
    """在邮件中嵌入图表，支持 `matplotlib` 和 `seaborn`.

    该微件能够将动态生成的图表（如 `matplotlib` 或 `seaborn` 的图表对象）
    或静态的图片文件（本地或URL）无缝嵌入到邮件内容中.它会自动处理图表的
    渲染、Base64 编码以及中文字符的显示问题，极大地方便了数据可视化报告的创建.

    核心功能:
        - **动态图表支持**: 直接接受 `matplotlib.pyplot` 或 `seaborn` 的图表对象.
        - **静态图片支持**: 可通过 URL 或本地文件路径加载图片.
        - **自动中文字体**: 自动检测并配置合适的中文字体，确保图表中的中文正常显示.
        - **内容增强**: 支持为图表添加标题、描述和数据摘要.

    Examples:
        使用 `matplotlib` 创建一个简单的柱状图并添加到邮件中：

        ```python
        import matplotlib.pyplot as plt
        from email_widget.widgets import ChartWidget

        # 1. 创建一个 matplotlib 图表
        plt.figure(figsize=(10, 6))
        categories = ['第一季度', '第二季度', '第三季度', '第四季度']
        sales = [120, 150, 130, 180]
        plt.bar(categories, sales, color='skyblue')
        plt.title('年度销售额（万元）')
        plt.ylabel('销售额')

        # 2. 创建 ChartWidget 并设置图表
        chart = (ChartWidget()\
                 .set_chart(plt)  # 将 plt 对象传入
                 .set_title("2024年度销售业绩")\
                 .set_description("各季度销售额对比图，展示了全年的销售趋势.")\
                 .set_data_summary("总销售额: 580万元, 最高季度: 第四季度"))

        # 假设 email 是一个 Email 对象
        # email.add_widget(chart)
        ```

        使用外部图片URL：

        ```python
        chart_from_url = (ChartWidget()\
                          .set_image_url("https://www.example.com/charts/monthly_trends.png")\
                          .set_title("月度趋势图")\
                          .set_alt_text("一张显示月度增长趋势的折线图"))
        ```
    """

    # 模板定义
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
                <div style="{{ summary_style }}">数据摘要: {{ data_summary }}</div>
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
        """初始化ChartWidget.

        Args:
            widget_id (Optional[str]): 可选的Widget ID.
        """
        super().__init__(widget_id)
        self._image_url: str | None = None
        self._title: str | None = None
        self._description: str | None = None
        self._alt_text: str = "图表"
        self._data_summary: str | None = None
        self._max_width: str = "100%"

    def set_image_url(self, image_url: str | Path, cache: bool = True) -> "ChartWidget":
        """设置图表图片URL或文件路径.

        此方法支持从网络URL或本地文件路径加载图片.图片会被自动处理并转换为
        Base64编码的data URI，直接嵌入到HTML中，以确保在邮件客户端中的兼容性.

        Args:
            image_url (Union[str, Path]): 图片的URL字符串或本地文件Path对象.
            cache (bool): 是否缓存网络图片，默认为True.

        Returns:
            ChartWidget: 返回self以支持链式调用.

        Raises:
            ValueError: 如果图片URL或路径无效，或图片处理失败.

        Examples:
            >>> # 使用URL
            >>> chart = ChartWidget().set_image_url("https://example.com/chart.png")

            >>> # 使用本地文件路径
            >>> from pathlib import Path
            >>> chart = ChartWidget().set_image_url(Path("./charts/sales.png"))
        """
        # 验证路径存在性（仅对本地路径）
        if isinstance(image_url, (str, Path)):
            path_obj = (
                Path(image_url)
                if isinstance(image_url, str)
                and not image_url.startswith(("http://", "https://", "data:"))
                else None
            )
            if path_obj and not path_obj.exists():
                self._logger.error(f"图片文件不存在: {path_obj}")
                self._image_url = None
                return self

        # 使用ImageUtils统一处理
        self._image_url = ImageUtils.process_image_source(image_url, cache=cache)
        return self

    def set_title(self, title: str) -> "ChartWidget":
        """设置图表标题.

        Args:
            title (str): 图表标题文本.

        Returns:
            ChartWidget: 返回self以支持链式调用.

        Examples:
            >>> chart = ChartWidget().set_title("2024年销售趋势")
        """
        self._title = title
        return self

    def set_description(self, description: str) -> "ChartWidget":
        """设置图表描述.

        Args:
            description (str): 图表描述文本.

        Returns:
            ChartWidget: 返回self以支持链式调用.

        Examples:
            >>> chart = ChartWidget().set_description("展示了各地区的销售对比情况")
        """
        self._description = description
        return self

    def set_alt_text(self, alt: str) -> "ChartWidget":
        """设置图片的替代文本.

        用于无障碍访问和图片加载失败时显示.

        Args:
            alt (str): 替代文本.

        Returns:
            ChartWidget: 返回self以支持链式调用.

        Examples:
            >>> chart = ChartWidget().set_alt_text("销售数据柱状图")
        """
        self._alt_text = alt
        return self

    def set_data_summary(self, summary: str) -> "ChartWidget":
        """设置数据摘要.

        在图表下方显示关键数据摘要信息.

        Args:
            summary (str): 数据摘要文本.

        Returns:
            ChartWidget: 返回self以支持链式调用.

        Examples:
            >>> chart = ChartWidget().set_data_summary("平均增长率: 15.3%, 最高值: ¥50万")
        """
        self._data_summary = summary
        return self

    def set_max_width(self, max_width: str) -> "ChartWidget":
        """设置图表容器的最大宽度.

        Args:
            max_width (str): CSS最大宽度值.

        Returns:
            ChartWidget: 返回self以支持链式调用.

        Examples:
            >>> chart = ChartWidget().set_max_width("800px")
            >>> chart = ChartWidget().set_max_width("90%")
        """
        self._max_width = max_width
        return self

    def set_chart(self, plt_obj: Any) -> "ChartWidget":
        """设置matplotlib/seaborn图表对象.

        将图表对象转换为Base64编码的PNG图片嵌入到邮件中.
        自动配置中文字体支持.

        Args:
            plt_obj (Any): matplotlib的pyplot对象或figure对象.

        Returns:
            ChartWidget: 返回self以支持链式调用.

        Raises:
            ImportError: 如果未安装matplotlib库.
            Exception: 如果图表转换失败.

        Examples:
            ```python
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.bar(['Q1', 'Q2', 'Q3', 'Q4'], [100, 120, 140, 110])
            ax.set_title('季度销售额')
            chart = ChartWidget().set_chart(plt)

            # 使用seaborn
            import seaborn as sns
            sns.barplot(data=df, x='month', y='sales')
            chart = ChartWidget().set_chart(plt)
            ```

        Note:
            调用此方法后，原图表对象会被关闭以释放内存.
            如果转换失败，图片URL会被设置为None.
        """
        # 检查matplotlib依赖
        check_optional_dependency("matplotlib")

        try:
            # 设置中文字体
            self._configure_chinese_font()

            # 保存图表到内存中的字节流
            img_buffer = io.BytesIO()
            plt_obj.savefig(img_buffer, format="png", bbox_inches="tight", dpi=150)
            img_buffer.seek(0)

            # 转换为base64
            img_base64 = base64.b64encode(img_buffer.getvalue()).decode("utf-8")
            self._image_url = f"data:image/png;base64,{img_base64}"

            # 关闭图表以释放内存
            plt_obj.close()

            img_buffer.close()
        except Exception as e:
            self._logger.error(f"转换图表失败: {e}")
            self._image_url = None

        return self

    def _configure_chinese_font(self):
        """配置matplotlib的中文字体支持.

        从配置文件获取字体列表，自动选择可用的中文字体.
        如果没有找到中文字体，会使用默认字体并输出警告.

        Note:
            这是一个内部方法，在set_chart时自动调用.
        """
        try:
            # 导入matplotlib模块
            plt = self._import_matplotlib_pyplot()
            fm = self._import_matplotlib_font_manager()

            # 从配置文件获取字体列表
            config = EmailConfig()
            font_list = config.get_chart_fonts()

            # 寻找可用的中文字体
            available_fonts = [f.name for f in fm.fontManager.ttflist]

            for font_name in font_list:
                if font_name in available_fonts:
                    plt.rcParams["font.sans-serif"] = [font_name]
                    plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题
                    self._logger.info(f"使用字体: {font_name}")
                    break
            else:
                # 如果没有找到中文字体，尝试使用系统默认
                self._logger.warning("未找到合适的中文字体，可能无法正确显示中文")
                plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
                plt.rcParams["axes.unicode_minus"] = False

        except Exception as e:
            self._logger.error(f"配置中文字体失败: {e}")

    def _get_template_name(self) -> str:
        """获取模板名称.

        Returns:
            模板文件名
        """
        return "chart.html"

    def get_template_context(self) -> dict[str, Any]:
        """获取模板渲染所需的上下文数据"""
        if not self._image_url:
            return {}

        # 容器样式
        container_style = f"""
            background: #ffffff;
            border: 1px solid #e1dfdd;
            border-radius: 4px;
            padding: 16px;
            margin: 16px 0;
            text-align: center;
            max-width: {self._max_width};
        """

        # 标题样式
        title_style = """
            font-size: 18px;
            font-weight: 600;
            color: #323130;
            margin-bottom: 12px;
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
        """

        # 图片样式
        img_style = """
            max-width: 100%;
            height: auto;
            border-radius: 4px;
            margin: 8px 0;
        """

        # 描述样式
        desc_style = """
            font-size: 14px;
            color: #605e5c;
            margin: 12px 0;
            line-height: 1.5;
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
        """

        # 数据摘要样式
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
