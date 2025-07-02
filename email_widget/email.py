"""Email主类实现

这个模块提供了EmailWidget库的核心功能，负责管理和渲染邮件内容。
"""

from typing import List, Optional, Dict, TYPE_CHECKING
from pathlib import Path
import datetime

from email_widget.core.base import BaseWidget
from email_widget.core.config import EmailConfig
from email_widget.core.template_engine import TemplateEngine
from email_widget.core.logger import get_project_logger

if TYPE_CHECKING:
    from email_widget import (
        TextWidget,
        TableWidget,
        ChartWidget,
        TextType,
        AlertType,
        LayoutType,
        ProgressTheme,
    )


class Email:
    """邮件主类，负责管理和渲染邮件内容。

    这个类是EmailWidget库的核心，用于创建和管理邮件报告。
    它可以包含多个Widget，并将它们渲染成美观的HTML邮件。

    主要功能：
    - 管理Widget集合
    - 渲染HTML邮件
    - 导出邮件文件
    - 配置邮件样式
    - 支持自定义副标题和脚注

    Attributes:
        title: 邮件标题
        subtitle: 邮件副标题
        footer_text: 脚注文本
        widgets: Widget列表
        config: 配置管理器
        _created_at: 创建时间
        _template_engine: 模板引擎
        _logger: 日志记录器

    Examples:
        >>> # 创建邮件对象
        >>> email = Email("每日报告")

        >>> # 设置副标题和脚注
        >>> email.set_subtitle("数据统计报告")
        >>> email.set_footer("本报告由数据团队生成")

        >>> # 添加Widget
        >>> from email_widget.widgets import TextWidget
        >>> text_widget = TextWidget().set_content("Hello World")
        >>> email.add_widget(text_widget)

        >>> # 导出HTML文件
        >>> file_path = email.export_html("report.html")
        >>> print(f"邮件已保存到: {file_path}")

        >>> # 获取HTML内容
        >>> html_content = email.export_str()
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

    def __init__(self, title: str = "邮件报告"):
        """初始化Email对象。

        Args:
            title: 邮件标题，默认为"邮件报告"
        """
        self.title = title
        self.subtitle: Optional[str] = None
        self.footer_text: Optional[str] = None
        self.widgets: List[BaseWidget] = []
        self.config = EmailConfig()
        self._created_at = datetime.datetime.now()
        self._template_engine = TemplateEngine()
        self._logger = get_project_logger()

    def add_widget(self, widget: BaseWidget) -> "Email":
        """添加单个Widget到邮件中。

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

    def add_widgets(self, widgets: List[BaseWidget]) -> "Email":
        """批量添加多个Widget到邮件中。

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
        """清空所有Widget。

        Returns:
            返回self以支持链式调用
        """
        self.widgets.clear()
        return self

    def remove_widget(self, widget_id: str) -> "Email":
        """根据ID移除指定的Widget。

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

    def get_widget(self, widget_id: str) -> Optional[BaseWidget]:
        """根据ID获取指定的Widget。

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
        """设置邮件标题。

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

    def set_subtitle(self, subtitle: Optional[str]) -> "Email":
        """设置邮件副标题。

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

    def set_footer(self, footer_text: Optional[str]) -> "Email":
        """设置邮件脚注。

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

    def add_title(self, text: str, text_type: "TextType" = None) -> "Email":
        """快速添加标题Widget。

        Args:
            text: 标题文本
            text_type: 文本类型，默认为TITLE_LARGE

        Returns:
            返回self以支持链式调用

        Examples:
            >>> email = Email()
            >>> email.add_title("每日数据报告")
            >>> # 或指定类型
            >>> email.add_title("小节标题", TextType.SECTION_H2)
        """
        from email_widget.core.enums import TextType
        from email_widget.widgets.text_widget import TextWidget

        if text_type is None:
            text_type = TextType.TITLE_LARGE

        widget = TextWidget().set_content(text).set_type(text_type)
        return self.add_widget(widget)

    def add_text(self, content: str, **kwargs) -> "Email":
        """快速添加文本Widget。

        Args:
            content: 文本内容
            **kwargs: 其他文本属性，如 color, font_size, align 等

        Returns:
            返回self以支持链式调用

        Examples:
            >>> email = Email()
            >>> email.add_text("这是一段普通文本")
            >>> # 带样式的文本
            >>> email.add_text("重要提示", color="#ff0000", font_size="18px")
        """
        from email_widget.widgets.text_widget import TextWidget

        widget = TextWidget().set_content(content)

        # 应用额外的样式参数
        for key, value in kwargs.items():
            method_name = f"set_{key}"
            if hasattr(widget, method_name):
                getattr(widget, method_name)(value)

        return self.add_widget(widget)

    def add_table_from_data(
        self,
        data: List[List[str]],
        headers: Optional[List[str]] = None,
        title: Optional[str] = None,
        **kwargs,
    ) -> "Email":
        """快速添加表格Widget。

        Args:
            data: 表格数据，二维列表
            headers: 表头列表，可选
            title: 表格标题，可选
            **kwargs: 其他表格属性

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

        # 应用额外的样式参数
        for key, value in kwargs.items():
            method_name = f"set_{key}"
            if hasattr(widget, method_name):
                getattr(widget, method_name)(value)

        return self.add_widget(widget)

    def add_table_from_df(
        self, df: "pd.DataFrame", title: Optional[str] = None, **kwargs
    ) -> "Email":
        """快速添加来自DataFrame的表格Widget。

        Args:
            df: pandas DataFrame对象
            title: 表格标题，可选
            **kwargs: 其他表格属性

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

        # 应用额外的样式参数
        for key, value in kwargs.items():
            method_name = f"set_{key}"
            if hasattr(widget, method_name):
                getattr(widget, method_name)(value)

        return self.add_widget(widget)

    def add_alert(
        self, content: str, alert_type: "AlertType" = None, title: Optional[str] = None
    ) -> "Email":
        """快速添加警告框Widget。

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
        label: Optional[str] = None,
        max_value: float = 100.0,
        theme: "ProgressTheme" = None,
    ) -> "Email":
        """快速添加进度条Widget。

        Args:
            value: 当前进度值
            label: 进度条标签，可选
            max_value: 最大值，默认100
            theme: 主题，默认为PRIMARY

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
            ProgressWidget().set_value(value).set_max_value(max_value).set_theme(theme)
        )

        if label:
            widget.set_label(label)

        return self.add_widget(widget)

    def add_card(
        self,
        title: str,
        content: str,
        icon: Optional[str] = None,
        metadata: Optional[dict[str, str]] = None,
    ) -> "Email":
        """快速添加卡片Widget。

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
        title: Optional[str] = None,
        description: Optional[str] = None,
        data_summary: Optional[str] = None,
    ) -> "Email":
        """快速添加matplotlib图表Widget。

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
        check_optional_dependency("matplotlib")

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
        items: List[Dict[str, str]],
        title: Optional[str] = None,
        layout: "LayoutType" = None,
    ) -> "Email":
        """快速添加状态信息Widget。

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

    def _generate_css_styles(self) -> str:
        """生成内联CSS样式。

        根据配置生成邮件的CSS样式，包括布局、颜色、字体等。

        Returns:
            包含CSS样式的HTML字符串
        """
        primary_color = self.config.get_primary_color()
        font_family = self.config.get_font_family()
        max_width = self.config.get_max_width()

        return f"""
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
            
            /* MSO条件注释样式 - 针对Outlook */
            <!--[if mso]>
            <style type="text/css">
                .email-container {{
                    width: 600px !important;
                }}
                .responsive-table {{
                    display: table !important;
                }}
            </style>
            <![endif]-->
        </style>
        """

    def _render_email(self) -> str:
        """渲染完整的邮件HTML内容。

        将所有Widget渲染成完整的HTML邮件，包括头部、主体和尾部。

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

    def _get_template_context(self, widget_content: str) -> dict:
        """获取模板上下文数据。

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
        self, filename: Optional[str] = None, output_dir: Optional[str] = None
    ) -> Path:
        """导出邮件为HTML文件。

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
        """导出邮件为HTML文本。

        Returns:
            完整的HTML邮件字符串

        Examples:
            >>> email = Email("预览测试")
            >>> html = email.export_str()
            >>> print(html[:100])  # 打印前100个字符
        """
        return self._render_email()

    def get_widget_count(self) -> int:
        """获取当前邮件中Widget的数量。

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
        """支持len()函数获取Widget数量。
        
        Returns:
            Widget数量
            
        Examples:
            >>> email = Email()
            >>> email.add_widget(TextWidget())
            >>> print(len(email))  # 输出: 1
        """
        return len(self.widgets)
    
    def __str__(self) -> str:
        """返回邮件对象的字符串表示。
        
        Returns:
            包含标题和Widget数量的字符串
            
        Examples:
            >>> email = Email("测试邮件")
            >>> print(str(email))  # 输出: Email(title='测试邮件', widgets=0)
        """
        return f"Email(title='{self.title}', widgets={len(self.widgets)})" 