"""
这个模块提供了EmailWidget库的核心功能，负责管理和渲染邮件内容.
"""

import datetime
from pathlib import Path
from typing import TYPE_CHECKING

from email_widget.core.base import BaseWidget
from email_widget.core.config import EmailConfig
from email_widget.core.logger import get_project_logger
from email_widget.core.template_engine import TemplateEngine

if TYPE_CHECKING:
    from email_widget.core.enums import (
        AlertType,
        LayoutType,
        LogLevel,
        ProgressTheme,
        StatusType,
        TextAlign,
        TextType,
    )


class Email:
    """邮件主类，负责管理和渲染邮件内容.

    这个类是 EmailWidget 库的核心，用于创建和管理HTML邮件报告.
    它作为一个功能强大的容器，可以添加、管理和编排各种“微件”（Widget），
    最终将它们渲染成一个美观、专业的HTML邮件.

    核心功能:
        - **微件管理**: 轻松添加、移除、查找和迭代处理各种内容组件（如文本、表格、图表等）.
        - **邮件属性配置**: 自定义邮件的标题、副标题和页脚.
        - **快捷方法**: 提供一系列 `add_*` 方法，用于快速创建和添加常用微件，简化代码.
        - **内容导出**: 支持将邮件导出为独立的 HTML 文件或获取其 HTML 字符串内容.
        - **样式配置**: 通过 `EmailConfig` 对象，可以自定义邮件的主题颜色、字体和布局宽度.

    Attributes:
        title (str): 邮件的主标题.
        subtitle (Optional[str]): 邮件的副标题，显示在主标题下方.
        footer_text (Optional[str]): 邮件的页脚文本.
        widgets (List[BaseWidget]): 存储所有已添加微件的列表.
        config (EmailConfig): 邮件的配置对象，用于控制样式和行为.

    Examples:
        一个基本的邮件创建和导出流程：

        ```python
        from email_widget import Email
        from email_widget.core.enums import TextType, AlertType

        # 1. 创建一个邮件对象
        email = Email("季度销售报告")

        # 2. 设置邮件的元数据
        email.set_subtitle("2024年第一季度")
        email.set_footer("本报告由销售部分析团队生成")

        # 3. 使用快捷方法添加内容
        email.add_text("核心摘要", text_type=TextType.TITLE_LARGE)
        email.add_text("本季度总销售额达到 1,234,567 元，同比增长 15%.")
        email.add_alert("注意：数据仍在初步核算中.", alert_type=AlertType.WARNING)
        email.add_progress(85, label="季度KPI完成率", theme="success")

        # 4. 导出为HTML文件
        # 将在默认输出目录（通常是 ./output）下生成 "quarterly_report.html"
        file_path = email.export_html("quarterly_report.html")

        print(f"报告已成功生成于: {file_path}")

        # 你也可以直接获取HTML字符串
        html_content = email.export_str()
        # print(html_content)
        ```
    """

    # 邮件模板
    TEMPLATE = """<!DOCTYPE html>
<html lang="{{ lang }}">
<head>
    <meta charset="{{ charset }}">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    {{ styles|safe }}
</head>
<body>
    <div class="email-container">
        <div class="email-header">
            <h1>{{ title }}</h1>
            {{ subtitle|safe }}
        </div>
        
        <div class="email-body">
            {{ widget_content|safe }}
        </div>
        
        <div class="email-footer">
            {{ footer_text|safe }}
        </div>
    </div>
</body>
</html>"""

    def __init__(self, title: str = "邮件报告") -> None:
        """初始化Email对象.

        Args:
            title: 邮件标题，默认为"邮件报告"
        """
        self.title = title
        self.subtitle: str | None = None
        self.footer_text: str | None = None
        self.widgets: list[BaseWidget] = []
        self.config = EmailConfig()
        self._created_at = datetime.datetime.now()
        self._template_engine = TemplateEngine()
        self._logger = get_project_logger()

    def add_widget(self, widget: BaseWidget) -> "Email":
        """添加单个Widget到邮件中.

        Args:
            widget: 要添加的Widget对象

        Returns:
            返回self以支持链式调用

        Examples:
            >>> email = Email()
            >>> text_widget = TextWidget().set_content("Hello")
            >>> email.add_widget(text_widget)
        """
        widget._set_parent(self)
        self.widgets.append(widget)
        return self

    def add_widgets(self, widgets: list[BaseWidget]) -> "Email":
        """批量添加多个Widget到邮件中.

        Args:
            widgets: Widget对象列表

        Returns:
            返回self以支持链式调用

        Examples:
            >>> email = Email()
            >>> widgets = [TextWidget(), TableWidget(), ChartWidget()]
            >>> email.add_widgets(widgets)
        """
        for widget in widgets:
            widget._set_parent(self)
            self.widgets.append(widget)
        return self

    def clear_widgets(self) -> "Email":
        """清空所有Widget.

        Returns:
            返回self以支持链式调用
        """
        self.widgets.clear()
        return self

    def remove_widget(self, widget_id: str) -> "Email":
        """根据ID移除指定的Widget.

        Args:
            widget_id: 要移除的Widget的ID

        Returns:
            返回self以支持链式调用

        Examples:
            >>> email = Email()
            >>> widget = TextWidget().set_widget_id("my_text")
            >>> email.add_widget(widget)
            >>> email.remove_widget("my_text")
        """
        self.widgets = [w for w in self.widgets if w.widget_id != widget_id]
        return self

    def get_widget(self, widget_id: str) -> BaseWidget | None:
        """根据ID获取指定的Widget.

        Args:
            widget_id: Widget的ID

        Returns:
            找到的Widget对象，如果不存在则返回None

        Examples:
            >>> email = Email()
            >>> widget = TextWidget().set_widget_id("my_text")
            >>> email.add_widget(widget)
            >>> found_widget = email.get_widget("my_text")
        """
        for widget in self.widgets:
            if widget.widget_id == widget_id:
                return widget
        return None

    def set_title(self, title: str) -> "Email":
        """设置邮件标题.

        Args:
            title: 新的邮件标题

        Returns:
            返回self以支持链式调用

        Examples:
            >>> email = Email()
            >>> email.set_title("每日数据报告 - 2024-01-01")
        """
        self.title = title
        return self

    def set_subtitle(self, subtitle: str | None) -> "Email":
        """设置邮件副标题.

        Args:
            subtitle: 副标题文本，如果为None则使用默认的时间戳

        Returns:
            返回self以支持链式调用

        Examples:
            >>> email = Email()
            >>> email.set_subtitle("数据统计报告")
        """
        self.subtitle = subtitle
        return self

    def set_footer(self, footer_text: str | None) -> "Email":
        """设置邮件脚注.

        Args:
            footer_text: 脚注文本，如果为None则使用默认文本

        Returns:
            返回self以支持链式调用

        Examples:
            >>> email = Email()
            >>> email.set_footer("本报告由数据团队自动生成")
        """
        self.footer_text = footer_text
        return self

    # ===== 便捷构造方法 =====

    def add_text(
        self,
        content: str,
        text_type: "TextType" = None,
        color: str | None = None,
        font_size: str | None = None,
        align: "TextAlign" = None,
        font_weight: str | None = None,
    ) -> "Email":
        """快速添加文本Widget.

        Args:
            content: 文本内容
            text_type: 文本类型，默认为TextType.BODY
            color: 文本颜色，如"#ff0000"
            font_size: 字体大小，如"18px"
            align: 文本对齐方式
            font_weight: 字体粗细，如"bold"

        Returns:
            返回self以支持链式调用

        Examples:
            >>> email = Email()
            >>> # 普通正文
            >>> email.add_text("这是一段普通文本")
            >>> # 大标题
            >>> email.add_text("重要标题", TextType.TITLE_LARGE)
            >>> # 带样式的文本
            >>> email.add_text("重要提示", color="#ff0000", font_size="18px")
        """
        from email_widget.core.enums import TextType
        from email_widget.widgets.text_widget import TextWidget

        if text_type is None:
            text_type = TextType.BODY

        widget = TextWidget().set_content(content).set_type(text_type)

        if color is not None:
            widget.set_color(color)
        if font_size is not None:
            widget.set_font_size(font_size)
        if align is not None:
            widget.set_align(align)
        if font_weight is not None:
            widget.set_font_weight(font_weight)

        return self.add_widget(widget)

    def add_table_from_data(
        self,
        data: list[list[str]],
        headers: list[str] | None = None,
        title: str | None = None,
        show_index: bool = False,
        striped: bool = True,
        bordered: bool = True,
        hoverable: bool = True,
    ) -> "Email":
        """快速添加表格Widget.

        Args:
            data: 表格数据，二维列表
            headers: 表头列表，可选
            title: 表格标题，可选
            show_index: 是否显示行索引
            striped: 是否使用条纹样式
            bordered: 是否显示边框
            hoverable: 是否支持悬停效果

        Returns:
            返回self以支持链式调用

        Examples:
            >>> email = Email()
            >>> data = [["张三", "100", "优秀"], ["李四", "95", "良好"]]
            >>> headers = ["姓名", "分数", "等级"]
            >>> email.add_table_from_data(data, headers, "成绩单")
        """
        from email_widget.widgets.table_widget import TableWidget

        widget = TableWidget()

        if title:
            widget.set_title(title)
        if headers:
            widget.set_headers(headers)

        for row in data:
            widget.add_row(row)

        widget.show_index(show_index)
        widget.set_striped(striped)
        widget.set_bordered(bordered)
        widget.set_hover_effect(hoverable)

        return self.add_widget(widget)

    def add_table_from_df(
        self,
        df: "pd.DataFrame",
        title: str | None = None,
        show_index: bool = False,
        striped: bool = True,
        bordered: bool = True,
        hoverable: bool = True,
    ) -> "Email":
        """快速添加来自DataFrame的表格Widget.

        Args:
            df: pandas DataFrame对象
            title: 表格标题，可选
            show_index: 是否显示行索引
            striped: 是否使用条纹样式
            bordered: 是否显示边框
            hoverable: 是否支持悬停效果

        Returns:
            返回self以支持链式调用

        Examples:
            >>> import pandas as pd
            >>> df = pd.DataFrame({"姓名": ["张三", "李四"], "分数": [100, 95]})
            >>> email = Email()
            >>> email.add_table_from_df(df, "成绩统计")
        """
        from email_widget.utils.optional_deps import check_optional_dependency
        from email_widget.widgets.table_widget import TableWidget

        # 检查pandas依赖
        check_optional_dependency("pandas", "pandas")

        widget = TableWidget()

        if title:
            widget.set_title(title)

        widget.set_dataframe(df)
        widget.show_index(show_index)
        widget.set_striped(striped)
        widget.set_bordered(bordered)
        widget.set_hover_effect(hoverable)

        return self.add_widget(widget)

    def add_alert(
        self, content: str, alert_type: "AlertType" = None, title: str | None = None
    ) -> "Email":
        """快速添加警告框Widget.

        Args:
            content: 警告内容
            alert_type: 警告类型，默认为NOTE
            title: 自定义标题，可选

        Returns:
            返回self以支持链式调用

        Examples:
            >>> email = Email()
            >>> email.add_alert("任务执行成功！", AlertType.TIP)
            >>> email.add_alert("注意检查数据", AlertType.WARNING, "重要提醒")
        """
        from email_widget.core.enums import AlertType
        from email_widget.widgets.alert_widget import AlertWidget

        if alert_type is None:
            alert_type = AlertType.NOTE

        widget = AlertWidget().set_content(content).set_alert_type(alert_type)

        if title:
            widget.set_title(title)

        return self.add_widget(widget)

    def add_progress(
        self,
        value: float,
        label: str | None = None,
        max_value: float = 100.0,
        theme: "ProgressTheme" = None,
        show_percentage: bool = True,
    ) -> "Email":
        """快速添加进度条Widget.

        Args:
            value: 当前进度值
            label: 进度条标签，可选
            max_value: 最大值，默认100
            theme: 主题，默认为PRIMARY
            show_percentage: 是否显示百分比

        Returns:
            返回self以支持链式调用

        Examples:
            >>> email = Email()
            >>> email.add_progress(75, "任务完成度")
            >>> email.add_progress(100, "下载进度", theme=ProgressTheme.SUCCESS)
        """
        from email_widget.core.enums import ProgressTheme
        from email_widget.widgets.progress_widget import ProgressWidget

        if theme is None:
            theme = ProgressTheme.PRIMARY

        widget = (
            ProgressWidget()
            .set_value(value)
            .set_max_value(max_value)
            .set_theme(theme)
            .show_percentage(show_percentage)
        )

        if label:
            widget.set_label(label)

        return self.add_widget(widget)

    def add_card(
        self,
        title: str,
        content: str,
        icon: str | None = None,
        metadata: dict[str, str] | None = None,
    ) -> "Email":
        """快速添加卡片Widget.

        Args:
            title: 卡片标题
            content: 卡片内容
            icon: 图标，可选
            metadata: 元数据字典，可选

        Returns:
            返回self以支持链式调用

        Examples:
            >>> email = Email()
            >>> email.add_card("系统状态", "所有服务运行正常", "✅")
            >>> # 带元数据的卡片
            >>> metadata = {"CPU": "15%", "内存": "60%"}
            >>> email.add_card("服务器监控", "资源使用情况", "🖥️", metadata)
        """
        from email_widget.widgets.card_widget import CardWidget

        widget = CardWidget().set_title(title).set_content(content)

        if icon:
            widget.set_icon(icon)

        if metadata:
            for key, value in metadata.items():
                widget.add_metadata(key, value)

        return self.add_widget(widget)

    def add_chart_from_plt(
        self,
        title: str | None = None,
        description: str | None = None,
        data_summary: str | None = None,
    ) -> "Email":
        """快速添加matplotlib图表Widget.

        Args:
            title: 图表标题，可选
            description: 图表描述，可选
            data_summary: 数据摘要，可选

        Returns:
            返回self以支持链式调用

        Examples:
            >>> import matplotlib.pyplot as plt
            >>> plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
            >>> plt.title("销售趋势")
            >>>
            >>> email = Email()
            >>> email.add_chart_from_plt("月度销售", "显示销售趋势变化")
        """
        from email_widget.utils.optional_deps import check_optional_dependency

        check_optional_dependency("matplotlib", "matplotlib")

        import matplotlib.pyplot as plt

        from email_widget.widgets.chart_widget import ChartWidget

        widget = ChartWidget().set_chart(plt)

        if title:
            widget.set_title(title)
        if description:
            widget.set_description(description)
        if data_summary:
            widget.set_data_summary(data_summary)

        return self.add_widget(widget)

    def add_status_items(
        self,
        items: list[dict[str, str]],
        title: str | None = None,
        layout: "LayoutType" = None,
    ) -> "Email":
        """快速添加状态信息Widget.

        Args:
            items: 状态项列表，每项包含 label, value, status(可选)
            title: 状态组标题，可选
            layout: 布局类型，默认为VERTICAL

        Returns:
            返回self以支持链式调用

        Examples:
            >>> items = [
            ...     {"label": "CPU使用率", "value": "15%"},
            ...     {"label": "内存使用率", "value": "60%"},
            ...     {"label": "磁盘空间", "value": "80%"}
            ... ]
            >>> email = Email()
            >>> email.add_status_items(items, "系统监控")
        """
        from email_widget.core.enums import LayoutType, StatusType
        from email_widget.widgets.status_widget import StatusWidget

        if layout is None:
            layout = LayoutType.VERTICAL

        widget = StatusWidget().set_layout(layout)

        if title:
            widget.set_title(title)

        for item in items:
            status = None
            if "status" in item:
                # 尝试转换字符串为StatusType
                status_str = item["status"].upper()
                if hasattr(StatusType, status_str):
                    status = getattr(StatusType, status_str)

            widget.add_status_item(item["label"], item["value"], status)

        return self.add_widget(widget)

    def add_quote(
        self,
        content: str,
        author: str | None = None,
        source: str | None = None,
        quote_type: "StatusType" = None,
    ) -> "Email":
        """快速添加引用Widget.

        Args:
            content: 引用内容
            author: 作者，可选
            source: 来源，可选
            quote_type: 引用类型，默认为INFO

        Returns:
            返回self以支持链式调用

        Examples:
            >>> email = Email()
            >>> email.add_quote("成功不是终点，失败不是致命的", "丘吉尔")
            >>> email.add_quote("数据是新时代的石油", source="《经济学人》")
        """
        from email_widget.core.enums import StatusType
        from email_widget.widgets.quote_widget import QuoteWidget

        if quote_type is None:
            quote_type = StatusType.INFO

        widget = QuoteWidget().set_content(content).set_quote_type(quote_type)

        if author:
            widget.set_author(author)
        if source:
            widget.set_source(source)

        return self.add_widget(widget)

    def add_circular_progress(
        self,
        value: float,
        max_value: float = 100.0,
        label: str | None = None,
        theme: "ProgressTheme" = None,
        size: str = "100px",
    ) -> "Email":
        """快速添加圆形进度条Widget.

        Args:
            value: 当前进度值
            max_value: 最大值，默认100
            label: 进度条标签，可选
            theme: 主题，默认为PRIMARY
            size: 圆形大小，默认"100px"

        Returns:
            返回self以支持链式调用

        Examples:
            >>> email = Email()
            >>> email.add_circular_progress(85, label="整体完成度")
            >>> email.add_circular_progress(100, theme=ProgressTheme.SUCCESS, size="120px")
        """
        from email_widget.core.enums import ProgressTheme
        from email_widget.widgets.circular_progress_widget import CircularProgressWidget

        if theme is None:
            theme = ProgressTheme.PRIMARY

        widget = (
            CircularProgressWidget()
            .set_value(value)
            .set_max_value(max_value)
            .set_theme(theme)
            .set_size(size)
        )

        if label:
            widget.set_label(label)

        return self.add_widget(widget)

    def add_log(
        self,
        logs: list[str],
        title: str | None = None,
        show_timestamp: bool = True,
        show_level: bool = True,
        filter_level: "LogLevel" = None,
        max_height: str = "400px",
    ) -> "Email":
        """快速添加日志Widget.

        Args:
            logs: 日志列表
            title: 日志标题，可选
            show_timestamp: 是否显示时间戳
            show_level: 是否显示日志级别
            filter_level: 过滤级别，可选
            max_height: 最大高度，默认"400px"

        Returns:
            返回self以支持链式调用

        Examples:
            >>> email = Email()
            >>> logs = [
            ...     "2024-01-01 10:00:00.000 | INFO | main:process:10 - 任务开始",
            ...     "2024-01-01 10:00:01.000 | WARNING | main:check:20 - 发现异常数据",
            ...     "2024-01-01 10:00:02.000 | INFO | main:finish:30 - 任务完成"
            ... ]
            >>> email.add_log(logs, "执行日志")
        """
        from email_widget.widgets.log_widget import LogWidget

        widget = (
            LogWidget()
            .set_logs(logs)
            .show_timestamp(show_timestamp)
            .show_level(show_level)
            .set_max_height(max_height)
        )

        if title:
            widget.set_title(title)
        if filter_level:
            widget.filter_by_level(filter_level)

        return self.add_widget(widget)

    def add_button(
        self,
        text: str,
        href: str,
        background_color: str | None = None,
        text_color: str | None = None,
        width: str | None = None,
        align: str = "left",
    ) -> "Email":
        """快速添加按钮Widget.

        Args:
            text: 按钮显示的文本
            href: 点击按钮后跳转的链接地址
            background_color: 按钮背景颜色，可选
            text_color: 按钮文字颜色，可选
            width: 按钮宽度，可选
            align: 按钮对齐方式，默认"left"

        Returns:
            返回self以支持链式调用

        Examples:
            >>> email = Email()
            >>> # 基本按钮
            >>> email.add_button("查看详情", "https://example.com/details")
            >>> # 自定义样式的按钮
            >>> email.add_button("立即购买", "https://shop.example.com",
            ...                  background_color="#22c55e", text_color="#ffffff",
            ...                  width="200px", align="center")
        """
        from email_widget.widgets.button_widget import ButtonWidget

        widget = ButtonWidget().set_text(text).set_href(href).set_align(align)

        if background_color is not None:
            widget.set_background_color(background_color)
        if text_color is not None:
            widget.set_text_color(text_color)
        if width is not None:
            widget.set_width(width)

        return self.add_widget(widget)

    def add_separator(
        self,
        separator_type: "SeparatorType" = None,
        color: str | None = None,
        thickness: str | None = None,
        width: str | None = None,
        margin: str | None = None,
    ) -> "Email":
        """快速添加分隔符Widget.

        Args:
            separator_type: 分隔符类型，默认为SOLID
            color: 分隔符颜色，可选
            thickness: 分隔符粗细，可选
            width: 分隔符宽度，可选
            margin: 上下边距，可选

        Returns:
            返回self以支持链式调用

        Examples:
            >>> email = Email()
            >>> # 基本分隔符
            >>> email.add_separator()
            >>> # 自定义样式的分隔符
            >>> email.add_separator(
            ...     separator_type=SeparatorType.DASHED,
            ...     color="#0078d4",
            ...     thickness="2px",
            ...     width="80%"
            ... )
        """
        from email_widget.core.enums import SeparatorType
        from email_widget.widgets.separator_widget import SeparatorWidget

        if separator_type is None:
            separator_type = SeparatorType.SOLID

        widget = SeparatorWidget().set_type(separator_type)

        if color is not None:
            widget.set_color(color)
        if thickness is not None:
            widget.set_thickness(thickness)
        if width is not None:
            widget.set_width(width)
        if margin is not None:
            widget.set_margin(margin)

        return self.add_widget(widget)

    def add_checklist(
        self,
        title: str = "",
        items: list[tuple[str, bool]] | None = None,
        show_progress: bool = False,
        compact_mode: bool = False,
    ) -> "Email":
        """快速添加清单Widget.

        Args:
            title: 清单标题，可选
            items: 清单项目列表，格式为[(text, completed), ...]，可选
            show_progress: 是否显示进度统计，默认False
            compact_mode: 是否使用紧凑模式，默认False

        Returns:
            返回self以支持链式调用

        Examples:
            >>> email = Email()
            >>> # 基本清单
            >>> email.add_checklist("任务清单", [
            ...     ("完成设计", True),
            ...     ("代码审查", False),
            ...     ("部署测试", False)
            ... ])
            >>> # 带进度统计的清单
            >>> email.add_checklist("项目进度", [
            ...     ("需求分析", True),
            ...     ("开发实现", True),
            ...     ("测试验证", False)
            ... ], show_progress=True)
        """
        from email_widget.widgets.checklist_widget import ChecklistWidget

        widget = ChecklistWidget()

        if title:
            widget.set_title(title)

        if items:
            for item in items:
                if len(item) >= 2:
                    text, completed = item[0], item[1]
                    widget.add_item(text, completed)

        if show_progress:
            widget.show_progress_stats(True)

        if compact_mode:
            widget.set_compact_mode(True)

        return self.add_widget(widget)

    def add_timeline(
        self,
        title: str = "",
        events: list[tuple] | None = None,
        show_time: bool = False,
        reverse_order: bool = False,
    ) -> "Email":
        """快速添加时间线Widget.

        Args:
            title: 时间线标题，可选
            events: 事件列表，格式为[(title, time, description, status_type), ...]，可选
            show_time: 是否显示时间戳，默认False
            reverse_order: 是否倒序排列，默认False

        Returns:
            返回self以支持链式调用

        Examples:
            >>> email = Email()
            >>> # 基本时间线
            >>> email.add_timeline("项目进度", [
            ...     ("项目启动", "2024-01-01", "项目正式开始"),
            ...     ("需求确认", "2024-01-15", "完成需求分析"),
            ...     ("开发完成", "2024-02-28", "代码开发完成")
            ... ])
            >>> # 带时间戳的时间线
            >>> email.add_timeline("系统日志", [
            ...     ("系统启动", "2024-01-01 09:00", "服务启动", "success"),
            ...     ("发现问题", "2024-01-01 10:30", "发现bug", "error"),
            ...     ("问题修复", "2024-01-01 11:00", "修复完成", "success")
            ... ], show_time=True, reverse_order=True)
        """
        from email_widget.widgets.timeline_widget import TimelineWidget

        widget = TimelineWidget()

        if title:
            widget.set_title(title)

        if events:
            for event in events:
                if len(event) >= 1:
                    title_text = event[0]
                    time = event[1] if len(event) > 1 else None
                    description = event[2] if len(event) > 2 else ""
                    status_type = event[3] if len(event) > 3 else None
                    widget.add_event(title_text, time, description, status_type)

        if show_time:
            widget.show_timestamps(True)

        if reverse_order:
            widget.set_reverse_order(True)

        return self.add_widget(widget)

    def add_metric(
        self,
        title: str = "",
        metrics: list[tuple] | None = None,
        layout: str = "horizontal",
        show_trends: bool = True,
    ) -> "Email":
        """快速添加指标Widget.

        Args:
            title: 指标组标题，可选
            metrics: 指标列表，格式为[(label, value, unit, trend, trend_type, description), ...]，可选
            layout: 布局方式，'horizontal' 或 'vertical'，默认'horizontal'
            show_trends: 是否显示趋势信息，默认True

        Returns:
            返回self以支持链式调用

        Examples:
            >>> email = Email()
            >>> # 基本指标
            >>> email.add_metric("核心指标", [
            ...     ("用户数", 12345, "人"),
            ...     ("增长率", "15.6", "%", "+2.3%", "success"),
            ...     ("收入", "¥1,250,000", "", "+12.3%", "success")
            ... ])
            >>> # 带完整选项的指标
            >>> email.add_metric(
            ...     title="系统性能",
            ...     metrics=[
            ...         ("CPU使用率", "45.2", "%", "+2.1%", "warning", "需要关注"),
            ...         ("内存使用", "78.5", "%", "-1.3%", "success", "表现良好"),
            ...         ("磁盘空间", "23.8", "GB", "+5.2GB", "info", "正常范围")
            ...     ],
            ...     layout="vertical",
            ...     show_trends=True
            ... )
        """
        from email_widget.widgets.metric_widget import MetricWidget

        widget = MetricWidget()

        if title:
            widget.set_title(title)

        if metrics:
            for metric in metrics:
                if len(metric) >= 2:
                    label = metric[0]
                    value = metric[1]
                    unit = metric[2] if len(metric) > 2 else ""
                    trend = metric[3] if len(metric) > 3 else ""
                    trend_type = metric[4] if len(metric) > 4 else None
                    description = metric[5] if len(metric) > 5 else ""
                    widget.add_metric(
                        label, value, unit, trend, trend_type, description
                    )

        widget.set_layout(layout)
        widget.show_trends(show_trends)

        return self.add_widget(widget)

    def add_image(
        self,
        image_url: str | Path,
        title: str | None = None,
        description: str | None = None,
        alt_text: str | None = None,
        width: str | None = None,
        height: str | None = None,
        max_width: str | None = None,
        border_radius: str | None = None,
        cache: bool = True,
        embed: bool = True,
        show_caption: bool = True,
    ) -> "Email":
        """快速添加图片Widget.

        Args:
            image_url: 图片的URL字符串或本地文件Path对象
            title: 图片标题，可选
            description: 图片描述，可选
            alt_text: 图片替代文本，可选
            width: 图片宽度，如\"300px\"、\"100%\"
            height: 图片高度，如\"200px\"、\"auto\"
            max_width: 图片最大宽度，如\"600px\"
            border_radius: 边框圆角，如\"8px\"、\"50%\"
            cache: 是否缓存网络图片，默认True
            embed: 是否嵌入图片，默认True
            show_caption: 是否显示标题和描述，默认True

        Returns:
            返回self以支持链式调用

        Examples:
            >>> email = Email()
            >>> # 基本用法
            >>> email.add_image("https://example.com/image.png")
            >>> # 本地图片
            >>> from pathlib import Path
            >>> email.add_image(Path("./assets/logo.png"), title="公司Logo")
            >>> # 完整选项
            >>> email.add_image(
            ...     "https://example.com/product.jpg",
            ...     title="产品展示",
            ...     description="最新款产品的展示图片",
            ...     alt_text="产品图片",
            ...     width="100%",
            ...     max_width="600px",
            ...     border_radius="8px"
            ... )
        """
        from pathlib import Path

        from email_widget.widgets.image_widget import ImageWidget

        widget = ImageWidget().set_image_url(image_url, cache=cache, embed=embed)

        if title is not None:
            widget.set_title(title)
        if description is not None:
            widget.set_description(description)
        if alt_text is not None:
            widget.set_alt_text(alt_text)
        if width is not None or height is not None:
            widget.set_size(width=width, height=height)
        if max_width is not None:
            widget.set_max_width(max_width)
        if border_radius is not None:
            widget.set_border_radius(border_radius)

        widget.show_caption(show_caption)

        return self.add_widget(widget)

    def _generate_css_styles(self) -> str:
        """生成内联CSS样式.

        根据配置生成邮件的CSS样式，包括布局、颜色、字体等.

        Returns:
            包含CSS样式的HTML字符串
        """
        primary_color = self.config.get_primary_color()
        font_family = self.config.get_font_family()
        max_width = self.config.get_max_width()

        # 主要CSS样式
        main_styles = f"""
        <style>
            body {{
                margin: 0;
                padding: 20px;
                font-family: {font_family};
                line-height: 1.6;
                color: #323130;
                background-color: #faf9f8;
            }}

            .email-container {{
                max-width: {max_width};
                margin: 0 auto;
                background: #ffffff;
                border: 1px solid #e1dfdd;
                border-radius: 8px;
                overflow: hidden;
            }}

            .email-header {{
                background: {primary_color};
                color: #ffffff;
                padding: 24px;
                text-align: center;
            }}

            .email-header h1 {{
                margin: 0;
                font-size: 24px;
                font-weight: 600;
            }}

            .email-header .timestamp {{
                margin-top: 8px;
                font-size: 14px;
                opacity: 0.9;
            }}

            .email-header .subtitle {{
                margin-top: 8px;
                font-size: 16px;
                opacity: 0.95;
                font-weight: 400;
            }}

            .email-body {{
                padding: 24px;
            }}

            .email-footer {{
                background: #f3f2f1;
                padding: 16px 24px;
                text-align: center;
                font-size: 12px;
                color: #605e5c;
                border-top: 1px solid #e1dfdd;
            }}

            /* 通用样式 */
            .fluent-card {{
                background: #ffffff;
                border: 1px solid #e1dfdd;
                border-radius: 4px;
                margin: 16px 0;
                overflow: hidden;
            }}

            .fluent-card-elevated {{
                border: 1px solid #d2d0ce;
                box-shadow: 0 1.6px 3.6px 0 rgba(0,0,0,0.132), 0 0.3px 0.9px 0 rgba(0,0,0,0.108);
            }}

            /* 响应式设计 - 使用邮件客户端兼容的方式 */

            /* 通用响应式样式 */
            .email-container {{
                width: 100%;
                max-width: {max_width};
                min-width: 320px;
            }}

            /* 表格响应式样式 */
            .responsive-table {{
                width: 100%;
                max-width: 100%;
                overflow-x: auto;
                display: block;
                white-space: nowrap;
            }}

            .responsive-table table {{
                width: 100%;
                min-width: 400px;
                border-collapse: collapse;
            }}

            /* 图片响应式样式 */
            .responsive-image {{
                width: 100%;
                max-width: 100%;
                height: auto;
                display: block;
            }}

            /* 内容区域响应式 */
            .responsive-content {{
                width: 100%;
                max-width: 100%;
                box-sizing: border-box;
                padding: 16px;
            }}

            /* 移动端优化的文字大小 */
            .mobile-text {{
                font-size: 14px;
                line-height: 1.4;
            }}
        </style>"""

        # MSO条件注释样式 - 单独处理
        mso_styles = """
        <!-- MSO条件注释样式 - 针对Outlook -->
        <!--[if mso]>
        <style type="text/css">
            .email-container {
                width: 600px !important;
            }
            .responsive-table {
                display: table !important;
            }
        </style>
        <![endif]-->
        """

        return main_styles + mso_styles

    def _render_email(self) -> str:
        """渲染完整的邮件HTML内容.

        将所有Widget渲染成完整的HTML邮件，包括头部、主体和尾部.

        Returns:
            完整的HTML邮件字符串
        """
        try:
            # 生成Widget内容
            widget_content = ""
            for widget in self.widgets:
                try:
                    widget_html = widget.render_html()
                    if widget_html:
                        widget_content += widget_html + "\n"
                except Exception as e:
                    self._logger.error(f"渲染Widget失败: {e}")
                    continue

            # 准备模板数据
            context = self._get_template_context(widget_content)

            # 使用模板引擎渲染
            return self._template_engine.render_safe(self.TEMPLATE, context)

        except Exception as e:
            self._logger.error(f"渲染邮件失败: {e}")
            return f"<html><body><h1>渲染错误</h1><p>{str(e)}</p></body></html>"

    def _get_template_context(self, widget_content: str) -> dict[str, str]:
        """获取模板上下文数据.

        Args:
            widget_content: 已渲染的Widget内容

        Returns:
            模板上下文字典
        """
        timestamp = self._created_at.strftime("%Y年%m月%d日 %H:%M:%S")

        # 生成副标题HTML
        if self.subtitle:
            subtitle_html = f'<div class="subtitle">{self.subtitle}</div>'
        else:
            subtitle_html = f'<div class="timestamp">生成时间: {timestamp}</div>'

        # 生成脚注HTML
        if self.footer_text:
            footer_html = f"<p>{self.footer_text}</p>"
        else:
            footer_html = "<p>此邮件由 EmailWidget 自动生成</p>"

        return {
            "title": self.title,
            "subtitle": subtitle_html,
            "footer_text": footer_html,
            "widget_content": widget_content,
            "styles": self._generate_css_styles(),
            "charset": self.config.get_email_charset(),
            "lang": self.config.get_email_lang(),
        }

    def export_html(
        self, filename: str | None = None, output_dir: str | None = None
    ) -> Path:
        """导出邮件为HTML文件.

        Args:
            filename: 可选的文件名，如果不提供则自动生成
            output_dir: 可选的输出目录，如果不提供则使用配置中的默认目录

        Returns:
            导出文件的完整路径

        Examples:
            >>> email = Email("报告")
            >>> # 使用默认文件名
            >>> path = email.export_html()
            >>>
            >>> # 指定文件名和目录
            >>> path = email.export_html("my_report.html", "./reports")
        """
        try:
            output_dir = output_dir or self.config.get_output_dir()

            if filename is None:
                timestamp = self._created_at.strftime("%Y%m%d_%H%M%S")
                filename = f"{self.title}_{timestamp}.html"

            # 确保文件名以.html结尾
            if not filename.endswith(".html"):
                filename += ".html"

            output_path = Path(output_dir) / filename
            output_path.parent.mkdir(parents=True, exist_ok=True)

            html_content = self.export_str()

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(html_content)

            self._logger.info(f"邮件已导出到: {output_path}")
            return output_path

        except Exception as e:
            self._logger.error(f"导出HTML文件失败: {e}")
            raise

    def export_str(self) -> str:
        """导出邮件为HTML文本.

        Returns:
            完整的HTML邮件字符串

        Examples:
            >>> email = Email("预览测试")
            >>> html = email.export_str()
            >>> print(html[:100])  # 打印前100个字符
        """
        return self._render_email()

    def get_widget_count(self) -> int:
        """获取当前邮件中Widget的数量.

        Returns:
            Widget数量

        Examples:
            >>> email = Email()
            >>> email.add_widget(TextWidget())
            >>> email.add_widget(TableWidget())
            >>> print(email.get_widget_count())  # 输出: 2
        """
        return len(self.widgets)

    def __len__(self) -> int:
        """支持len()函数获取Widget数量.

        Returns:
            Widget数量

        Examples:
            >>> email = Email()
            >>> email.add_widget(TextWidget())
            >>> print(len(email))  # 输出: 1
        """
        return len(self.widgets)

    def __str__(self) -> str:
        """返回邮件对象的字符串表示.

        Returns:
            包含标题和Widget数量的字符串

        Examples:
            >>> email = Email("测试邮件")
            >>> print(str(email))  # 输出: Email(title='测试邮件', widgets=0)
        """
        return f"Email(title='{self.title}', widgets={len(self.widgets)})"
