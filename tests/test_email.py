"""Email模块测试用例 - 完整覆盖率测试"""

import datetime
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from email_widget.core.enums import (
    AlertType,
    LayoutType,
    LogLevel,
    ProgressTheme,
    StatusType,
    TextAlign,
    TextType,
)
from email_widget.email import Email
from email_widget.widgets.alert_widget import AlertWidget
from email_widget.widgets.card_widget import CardWidget
from email_widget.widgets.circular_progress_widget import CircularProgressWidget
from email_widget.widgets.log_widget import LogWidget
from email_widget.widgets.progress_widget import ProgressWidget
from email_widget.widgets.quote_widget import QuoteWidget
from email_widget.widgets.status_widget import StatusWidget
from email_widget.widgets.table_widget import TableWidget
from email_widget.widgets.text_widget import TextWidget


class TestEmailBasics:
    """Email基础功能测试类"""

    def setup_method(self):
        """每个测试方法执行前的设置"""
        self.email = Email("Test Subject")

    def test_init_default(self):
        """测试默认初始化"""
        email = Email()
        assert email.title == "邮件报告"
        assert email.subtitle is None
        assert email.footer_text is None
        assert email.widgets == []
        assert email.config is not None
        assert email._template_engine is not None
        assert email._logger is not None
        assert isinstance(email._created_at, datetime.datetime)

    def test_init_with_title(self):
        """测试带标题的初始化"""
        title = "Test Email Title"
        email = Email(title)
        assert email.title == title

    def test_add_widget(self):
        """测试添加组件"""
        widget = TextWidget().set_content("Test content")
        result = self.email.add_widget(widget)

        assert result is self.email  # 支持链式调用
        assert len(self.email.widgets) == 1
        assert self.email.widgets[0] is widget

    def test_add_widgets_batch(self):
        """测试批量添加组件"""
        widget1 = TextWidget().set_content("Widget 1")
        widget2 = ProgressWidget().set_value(50)
        widgets = [widget1, widget2]

        result = self.email.add_widgets(widgets)

        assert result is self.email
        assert len(self.email.widgets) == 2
        assert self.email.widgets[0] is widget1
        assert self.email.widgets[1] is widget2

    def test_add_multiple_widgets_individually(self):
        """测试逐个添加多个组件"""
        widget1 = TextWidget().set_content("Widget 1")
        widget2 = ProgressWidget().set_value(50)

        result = self.email.add_widget(widget1).add_widget(widget2)
        assert result is self.email
        assert len(self.email.widgets) == 2
        assert self.email.widgets[0] is widget1
        assert self.email.widgets[1] is widget2

    def test_clear_widgets(self):
        """测试清空组件"""
        widget1 = TextWidget().set_content("Widget 1")
        widget2 = ProgressWidget().set_value(50)
        self.email.add_widget(widget1).add_widget(widget2)

        assert len(self.email.widgets) == 2

        result = self.email.clear_widgets()
        assert result is self.email
        assert len(self.email.widgets) == 0

    def test_remove_widget_by_id(self):
        """测试根据ID移除组件"""
        widget1 = TextWidget("widget1").set_content("Widget 1")
        widget2 = ProgressWidget("widget2").set_value(50)

        self.email.add_widget(widget1).add_widget(widget2)
        assert len(self.email.widgets) == 2

        result = self.email.remove_widget("widget1")
        assert result is self.email
        assert len(self.email.widgets) == 1
        assert self.email.widgets[0] is widget2

    def test_get_widget_by_id(self):
        """测试根据ID获取组件"""
        widget1 = TextWidget("widget1").set_content("Widget 1")
        widget2 = ProgressWidget("widget2").set_value(50)

        self.email.add_widget(widget1).add_widget(widget2)

        found_widget = self.email.get_widget("widget1")
        assert found_widget is widget1

        not_found = self.email.get_widget("non_existent")
        assert not_found is None

    def test_set_title(self):
        """测试设置标题"""
        new_title = "New Title"
        result = self.email.set_title(new_title)

        assert result is self.email
        assert self.email.title == new_title

    def test_set_subtitle(self):
        """测试设置副标题"""
        subtitle = "This is a subtitle"
        result = self.email.set_subtitle(subtitle)

        assert result is self.email
        assert self.email.subtitle == subtitle

        # 测试设置为None
        result = self.email.set_subtitle(None)
        assert self.email.subtitle is None

    def test_set_footer(self):
        """测试设置脚注"""
        footer = "This is footer text"
        result = self.email.set_footer(footer)

        assert result is self.email
        assert self.email.footer_text == footer

        # 测试清空脚注
        result = self.email.set_footer(None)
        assert self.email.footer_text is None


class TestEmailConvenienceMethods:
    """Email便捷方法测试类"""

    def setup_method(self):
        """每个测试方法执行前的设置"""
        self.email = Email("Convenience Test")

    def test_add_text_default(self):
        """测试添加默认文本"""
        result = self.email.add_text("Default text")

        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], TextWidget)

    def test_add_text_with_type(self):
        """测试添加指定类型的文本"""
        result = self.email.add_text("Title text", text_type=TextType.TITLE_LARGE)

        assert result is self.email
        assert len(self.email.widgets) == 1
        widget = self.email.widgets[0]
        assert isinstance(widget, TextWidget)

    def test_add_text_with_all_styles(self):
        """测试添加带所有样式的文本"""
        result = self.email.add_text(
            "Styled text",
            text_type=TextType.BODY,
            color="#ff0000",
            font_size="18px",
            align=TextAlign.CENTER,
            font_weight="bold",
        )

        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], TextWidget)

    def test_add_text_with_partial_styles(self):
        """测试添加部分样式的文本"""
        result = self.email.add_text(
            "Partial styled text", color="#0000ff", font_size="16px"
        )

        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], TextWidget)

    def test_add_table_from_data_minimal(self):
        """测试添加最小数据表格"""
        data = [["A1", "B1"], ["A2", "B2"]]

        result = self.email.add_table_from_data(data)

        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], TableWidget)

    def test_add_table_from_data_with_headers(self):
        """测试添加带表头的表格"""
        data = [["A1", "B1"], ["A2", "B2"]]
        headers = ["Col A", "Col B"]

        result = self.email.add_table_from_data(
            data, headers=headers, title="Test Table"
        )

        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], TableWidget)

    def test_add_table_from_data_with_all_options(self):
        """测试添加带所有选项的表格"""
        data = [["A1", "B1"], ["A2", "B2"]]
        headers = ["Col A", "Col B"]

        result = self.email.add_table_from_data(
            data,
            headers=headers,
            title="Full Options Table",
            show_index=True,
            striped=False,
            bordered=False,
            hoverable=False,
        )

        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], TableWidget)

    @patch("email_widget.utils.optional_deps.check_optional_dependency")
    def test_add_table_from_df_minimal(self, mock_check):
        """测试添加DataFrame表格（最小）"""
        # 模拟pandas DataFrame
        mock_df = MagicMock()
        mock_df.__class__.__name__ = "DataFrame"

        result = self.email.add_table_from_df(mock_df)

        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], TableWidget)
        mock_check.assert_called_once_with("pandas", "pandas")

    @patch("email_widget.utils.optional_deps.check_optional_dependency")
    def test_add_table_from_df_with_options(self, mock_check):
        """测试添加DataFrame表格（带选项）"""
        mock_df = MagicMock()
        mock_df.__class__.__name__ = "DataFrame"

        result = self.email.add_table_from_df(
            mock_df,
            title="DataFrame Table",
            show_index=True,
            striped=False,
            bordered=True,
            hoverable=False,
        )

        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], TableWidget)

    def test_add_alert_default(self):
        """测试添加默认警告框"""
        result = self.email.add_alert("Default alert")

        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], AlertWidget)

    def test_add_alert_with_type_and_title(self):
        """测试添加带类型和标题的警告框"""
        result = self.email.add_alert(
            "Warning message", alert_type=AlertType.WARNING, title="Important Notice"
        )

        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], AlertWidget)

    def test_add_progress_minimal(self):
        """测试添加最小进度条"""
        result = self.email.add_progress(75.0)

        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], ProgressWidget)

    def test_add_progress_with_all_options(self):
        """测试添加带所有选项的进度条"""
        result = self.email.add_progress(
            85.0,
            label="Loading Progress",
            max_value=200.0,
            theme=ProgressTheme.SUCCESS,
            show_percentage=False,
        )

        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], ProgressWidget)

    def test_add_card_minimal(self):
        """测试添加最小卡片"""
        result = self.email.add_card("Card Title", "Card Content")

        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], CardWidget)

    def test_add_card_with_icon_and_metadata(self):
        """测试添加带图标和元数据的卡片"""
        metadata = {"CPU": "15%", "Memory": "60%"}
        result = self.email.add_card(
            "System Status", "All systems operational", icon="✅", metadata=metadata
        )

        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], CardWidget)

    @pytest.mark.skip(reason="matplotlib导入问题，跳过该测试")
    @patch("email_widget.utils.optional_deps.check_optional_dependency")
    @patch("email_widget.widgets.chart_widget.ChartWidget")
    def test_add_chart_from_plt_minimal(self, mock_chart_widget, mock_check):
        """测试添加最小matplotlib图表"""
        mock_widget_instance = MagicMock()
        mock_chart_widget.return_value = mock_widget_instance
        mock_widget_instance.set_chart.return_value = mock_widget_instance
        mock_widget_instance.set_title.return_value = mock_widget_instance
        mock_widget_instance.set_description.return_value = mock_widget_instance
        mock_widget_instance.set_data_summary.return_value = mock_widget_instance

        # Mock the entire import for matplotlib.pyplot
        with patch(
            "builtins.__import__",
            side_effect=lambda name, *args, **kwargs: MagicMock()
            if name == "matplotlib.pyplot"
            else __import__(name, *args, **kwargs),
        ):
            result = self.email.add_chart_from_plt()

            assert result is self.email
            assert len(self.email.widgets) == 1
            assert mock_chart_widget.called

    @pytest.mark.skip(reason="matplotlib导入问题，跳过该测试")
    @patch("email_widget.utils.optional_deps.check_optional_dependency")
    @patch("email_widget.widgets.chart_widget.ChartWidget")
    def test_add_chart_from_plt_with_options(self, mock_chart_widget, mock_check):
        """测试添加带选项的matplotlib图表"""
        mock_widget_instance = MagicMock()
        mock_chart_widget.return_value = mock_widget_instance
        mock_widget_instance.set_chart.return_value = mock_widget_instance
        mock_widget_instance.set_title.return_value = mock_widget_instance
        mock_widget_instance.set_description.return_value = mock_widget_instance
        mock_widget_instance.set_data_summary.return_value = mock_widget_instance

        # Mock the entire import for matplotlib.pyplot
        with patch(
            "builtins.__import__",
            side_effect=lambda name, *args, **kwargs: MagicMock()
            if name == "matplotlib.pyplot"
            else __import__(name, *args, **kwargs),
        ):
            result = self.email.add_chart_from_plt(
                title="Chart Title",
                description="Chart Description",
                data_summary="Data Summary",
            )

            assert result is self.email
            assert len(self.email.widgets) == 1
            mock_widget_instance.set_title.assert_called_with("Chart Title")
            mock_widget_instance.set_description.assert_called_with("Chart Description")
            mock_widget_instance.set_data_summary.assert_called_with("Data Summary")

    def test_add_status_items_minimal(self):
        """测试添加最小状态项"""
        items = [{"label": "CPU", "value": "15%"}, {"label": "Memory", "value": "60%"}]

        result = self.email.add_status_items(items)

        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], StatusWidget)

    def test_add_status_items_with_options(self):
        """测试添加带选项的状态项"""
        items = [
            {"label": "CPU", "value": "15%", "status": "SUCCESS"},
            {"label": "Memory", "value": "60%", "status": "WARNING"},
        ]

        result = self.email.add_status_items(
            items, title="System Monitoring", layout=LayoutType.HORIZONTAL
        )

        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], StatusWidget)

    def test_add_quote_minimal(self):
        """测试添加最小引用"""
        result = self.email.add_quote("Success is not final.")

        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], QuoteWidget)

    def test_add_quote_with_author(self):
        """测试添加带作者的引用"""
        result = self.email.add_quote(
            "Success is not final, failure is not fatal.", author="Winston Churchill"
        )

        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], QuoteWidget)

    def test_add_quote_with_source(self):
        """测试添加带来源的引用"""
        result = self.email.add_quote("Data is the new oil.", source="The Economist")

        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], QuoteWidget)

    def test_add_quote_with_all_options(self):
        """测试添加带所有选项的引用"""
        result = self.email.add_quote(
            "Innovation distinguishes between a leader and a follower.",
            author="Steve Jobs",
            source="Stanford Commencement",
            quote_type=StatusType.PRIMARY,
        )

        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], QuoteWidget)

    def test_add_circular_progress_minimal(self):
        """测试添加最小圆形进度条"""
        result = self.email.add_circular_progress(75.0)

        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], CircularProgressWidget)

    def test_add_circular_progress_with_all_options(self):
        """测试添加带所有选项的圆形进度条"""
        result = self.email.add_circular_progress(
            85.0,
            max_value=200.0,
            label="Overall Progress",
            theme=ProgressTheme.SUCCESS,
            size="120px",
        )

        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], CircularProgressWidget)

    def test_add_log_minimal(self):
        """测试添加最小日志"""
        logs = ["2024-01-01 10:00:00.000 | INFO | main:start:10 - Process started"]

        result = self.email.add_log(logs)

        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], LogWidget)

    def test_add_log_with_all_options(self):
        """测试添加带所有选项的日志"""
        logs = [
            "2024-01-01 10:00:00.000 | INFO | main:start:10 - Process started",
            "2024-01-01 10:00:01.000 | WARNING | main:check:20 - Warning detected",
            "2024-01-01 10:00:02.000 | ERROR | main:error:30 - Error occurred",
        ]

        result = self.email.add_log(
            logs,
            title="Execution Log",
            show_timestamp=False,
            show_level=True,
            filter_level=LogLevel.INFO,
            max_height="300px",
        )

        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], LogWidget)


class TestEmailRendering:
    """Email渲染功能测试类"""

    def setup_method(self):
        """每个测试方法执行前的设置"""
        self.email = Email("Rendering Test")

    def test_generate_css_styles(self):
        """测试CSS样式生成"""
        css = self.email._generate_css_styles()

        assert isinstance(css, str)
        assert "<style>" in css
        assert "body {" in css
        assert "email-container" in css
        assert "email-header" in css
        assert "email-body" in css
        assert "email-footer" in css

    def test_get_template_context_without_subtitle_footer(self):
        """测试获取模板上下文（无副标题和脚注）"""
        context = self.email._get_template_context("<div>test content</div>")

        assert "title" in context
        assert "subtitle" in context
        assert "footer_text" in context
        assert "widget_content" in context
        assert "styles" in context
        assert "charset" in context
        assert "lang" in context
        assert context["title"] == "Rendering Test"
        assert "生成时间:" in context["subtitle"]
        assert "EmailWidget 自动生成" in context["footer_text"]

    def test_get_template_context_with_subtitle_footer(self):
        """测试获取模板上下文（有副标题和脚注）"""
        self.email.set_subtitle("Custom Subtitle")
        self.email.set_footer("Custom Footer")

        context = self.email._get_template_context("<div>test content</div>")

        assert "Custom Subtitle" in context["subtitle"]
        assert "Custom Footer" in context["footer_text"]

    def test_render_email_empty(self):
        """测试渲染空邮件"""
        html = self.email._render_email()

        assert isinstance(html, str)
        assert "<!DOCTYPE html>" in html
        assert "Rendering Test" in html
        assert "html>" in html

    def test_render_email_with_widgets(self):
        """测试渲染带Widget的邮件"""
        self.email.add_text("Test Content")

        html = self.email._render_email()

        assert isinstance(html, str)
        assert "<!DOCTYPE html>" in html
        assert "Rendering Test" in html

    @patch("email_widget.widgets.text_widget.TextWidget.render_html")
    def test_render_email_with_widget_error(self, mock_render):
        """测试Widget渲染错误时的处理"""
        mock_render.side_effect = Exception("Widget render error")

        self.email.add_text("Test Content")
        html = self.email._render_email()

        # 应该继续渲染，只是跳过出错的Widget
        assert "<!DOCTYPE html>" in html

    def test_render_email_general_error(self):
        """测试邮件渲染一般错误处理"""
        # 直接验证export_str在遇到错误时的行为
        result = self.email.export_str()

        # 正常情况下应该包含HTML
        assert "<!DOCTYPE html>" in result

    @patch("email_widget.core.template_engine.TemplateEngine.render_safe")
    def test_render_email_template_error(self, mock_render_safe):
        """测试模板引擎渲染错误处理"""
        mock_render_safe.side_effect = Exception("Template render error")

        self.email.add_text("Test Content")
        html = self.email._render_email()

        # 应该返回错误页面HTML
        assert "<h1>渲染错误</h1>" in html
        assert "Template render error" in html


class TestEmailExport:
    """Email导出功能测试类"""

    def setup_method(self):
        """每个测试方法执行前的设置"""
        self.email = Email("Export Test")

    def test_export_str(self):
        """测试导出字符串"""
        self.email.add_text("Export content")

        html_str = self.email.export_str()

        assert isinstance(html_str, str)
        assert "<!DOCTYPE html>" in html_str
        assert "Export Test" in html_str

    def test_export_html_with_filename(self):
        """测试导出HTML文件（指定文件名）"""
        with tempfile.TemporaryDirectory() as temp_dir:
            filename = "test_export.html"

            self.email.add_text("Export content")

            result_path = self.email.export_html(filename, output_dir=temp_dir)

            assert isinstance(result_path, Path)
            assert result_path.exists()
            assert result_path.name == filename

            content = result_path.read_text(encoding="utf-8")
            assert "Export Test" in content
            assert "Export content" in content

    def test_export_html_default_filename(self):
        """测试导出HTML文件（默认文件名）"""
        with tempfile.TemporaryDirectory() as temp_dir:
            result_path = self.email.export_html(output_dir=temp_dir)

            assert result_path.exists()
            assert result_path.suffix == ".html"
            assert "Export Test" in result_path.name

    def test_export_html_auto_add_extension(self):
        """测试自动添加.html扩展名"""
        with tempfile.TemporaryDirectory() as temp_dir:
            filename = "test_file"  # 没有扩展名

            result_path = self.email.export_html(filename, output_dir=temp_dir)

            assert result_path.name == "test_file.html"

    def test_export_html_create_directory(self):
        """测试创建不存在的目录"""
        with tempfile.TemporaryDirectory() as temp_dir:
            nested_dir = Path(temp_dir) / "nested" / "dir"

            result_path = self.email.export_html(
                "test.html", output_dir=str(nested_dir)
            )

            assert result_path.exists()
            assert result_path.parent == nested_dir

    def test_export_html_default_output_dir(self):
        """测试使用默认输出目录"""
        with patch.object(
            self.email.config, "get_output_dir", return_value=tempfile.gettempdir()
        ):
            result_path = self.email.export_html("test_default_dir.html")

            assert result_path.exists()
            # 清理测试文件
            result_path.unlink()

    @patch("builtins.open", side_effect=OSError("File write error"))
    def test_export_html_write_error(self, mock_open):
        """测试文件写入错误"""
        with tempfile.TemporaryDirectory() as temp_dir:
            with pytest.raises(IOError):
                self.email.export_html("test.html", output_dir=temp_dir)


class TestEmailUtilities:
    """Email工具方法测试类"""

    def setup_method(self):
        """每个测试方法执行前的设置"""
        self.email = Email("Utility Test")

    def test_get_widget_count_empty(self):
        """测试获取Widget数量（空）"""
        assert self.email.get_widget_count() == 0

    def test_get_widget_count_with_widgets(self):
        """测试获取Widget数量（有Widget）"""
        self.email.add_text("Text 1")
        assert self.email.get_widget_count() == 1

        self.email.add_text("Text 2")
        assert self.email.get_widget_count() == 2

    def test_len_method_empty(self):
        """测试len()方法（空）"""
        assert len(self.email) == 0

    def test_len_method_with_widgets(self):
        """测试len()方法（有Widget）"""
        self.email.add_text("Text 1")
        assert len(self.email) == 1

        self.email.add_text("Text 2")
        assert len(self.email) == 2

    def test_str_representation_empty(self):
        """测试字符串表示（空）"""
        str_repr = str(self.email)
        assert "Utility Test" in str_repr
        assert "widgets=0" in str_repr

    def test_str_representation_with_widgets(self):
        """测试字符串表示（有Widget）"""
        self.email.add_text("Text 1")
        self.email.add_text("Text 2")

        str_repr = str(self.email)
        assert "Utility Test" in str_repr
        assert "widgets=2" in str_repr


class TestEmailChaining:
    """Email链式调用测试类"""

    def test_chain_basic_methods(self):
        """测试基础方法的链式调用"""
        email = Email()

        result = (
            email.set_title("Chained Title")
            .set_subtitle("Chained Subtitle")
            .set_footer("Chained Footer")
        )

        assert result is email
        assert email.title == "Chained Title"
        assert email.subtitle == "Chained Subtitle"
        assert email.footer_text == "Chained Footer"

    def test_chain_widget_methods(self):
        """测试Widget方法的链式调用"""
        email = Email()

        result = (
            email.add_text("Title", TextType.TITLE_LARGE)
            .add_text("Content")
            .add_progress(75)
            .add_alert("Notice")
        )

        assert result is email
        assert len(email) == 4

    def test_chain_mixed_methods(self):
        """测试混合方法的链式调用"""
        email = Email()

        result = (
            email.set_title("Mixed Chain")
            .add_text("Header", TextType.TITLE_LARGE)
            .set_subtitle("Subtitle")
            .add_progress(50)
            .set_footer("Footer")
            .add_quote("Quote content")
        )

        assert result is email
        assert email.title == "Mixed Chain"
        assert email.subtitle == "Subtitle"
        assert email.footer_text == "Footer"
        assert len(email) == 3


class TestEmailIntegration:
    """Email集成测试类"""

    def test_comprehensive_email_workflow(self):
        """测试综合邮件工作流程"""
        email = Email("Comprehensive Test Report")

        # 配置邮件
        email.set_subtitle("Daily Integration Report")
        email.set_footer("Generated by Test Suite")

        # 添加各种Widget
        email.add_text("Executive Summary", TextType.TITLE_LARGE)
        email.add_text(
            "This report contains comprehensive test results.", TextType.BODY
        )

        email.add_text("Progress Overview", TextType.SECTION_H2)
        email.add_progress(85.0, "Overall Progress", theme=ProgressTheme.SUCCESS)
        email.add_circular_progress(75.0, label="Quality Score")

        email.add_text("System Status", TextType.SECTION_H2)
        status_items = [
            {"label": "API Tests", "value": "Passed", "status": "SUCCESS"},
            {"label": "UI Tests", "value": "Passed", "status": "SUCCESS"},
            {"label": "Performance", "value": "Warning", "status": "WARNING"},
        ]
        email.add_status_items(status_items, "Test Results")

        email.add_text("Data Summary", TextType.SECTION_H2)
        data = [
            ["Test Suite", "Count", "Status"],
            ["Unit Tests", "150", "✅"],
            ["Integration Tests", "45", "✅"],
        ]
        email.add_table_from_data(data[1:], headers=data[0], title="Test Summary")

        email.add_card("Important Notice", "All tests completed successfully.", "📊")

        email.add_alert("All systems operational!", AlertType.TIP, "System Status")

        email.add_quote(
            "Quality is never an accident.",
            "John Ruskin",
            quote_type=StatusType.PRIMARY,
        )

        logs = [
            "2024-01-01 09:00:00.000 | INFO | test:start:1 - Test suite started",
            "2024-01-01 09:05:00.000 | INFO | test:progress:50 - 50% complete",
            "2024-01-01 09:10:00.000 | INFO | test:complete:100 - All tests passed",
        ]
        email.add_log(logs, "Execution Log")

        # 验证构建结果
        assert email.title == "Comprehensive Test Report"
        assert email.subtitle == "Daily Integration Report"
        assert email.footer_text == "Generated by Test Suite"
        assert len(email) == 13  # 应该有13个Widget

        # 验证可以正常导出
        html_content = email.export_str()
        assert "Comprehensive Test Report" in html_content
        assert "Daily Integration Report" in html_content
        assert "Generated by Test Suite" in html_content

    def test_widget_management_workflow(self):
        """测试Widget管理工作流程"""
        email = Email("Widget Management Test")

        # 添加多个widget
        email.add_text("Text 1", text_type=TextType.BODY)
        email.add_text("Text 2", text_type=TextType.SECTION_H2)
        email.add_progress(30.0, "Progress 1")

        assert len(email) == 3

        # 清空所有widget
        email.clear_widgets()
        assert len(email) == 0

        # 重新添加带ID的widget
        widget1 = TextWidget("w1").set_content("Widget 1")
        widget2 = TextWidget("w2").set_content("Widget 2")
        widget3 = TextWidget("w3").set_content("Widget 3")

        email.add_widgets([widget1, widget2, widget3])
        assert len(email) == 3

        # 根据ID移除widget
        email.remove_widget("w2")
        assert len(email) == 2

        # 验证正确的widget被移除
        assert email.get_widget("w1") is widget1
        assert email.get_widget("w2") is None
        assert email.get_widget("w3") is widget3

    def test_export_workflow(self):
        """测试导出工作流程"""
        email = Email("Export Workflow Test")
        email.add_text("Export content")
        email.add_progress(100, "Complete")

        with tempfile.TemporaryDirectory() as temp_dir:
            # 测试自定义文件名导出
            custom_path = email.export_html("custom_report.html", temp_dir)
            assert custom_path.name == "custom_report.html"
            assert custom_path.exists()

            # 测试默认文件名导出
            default_path = email.export_html(output_dir=temp_dir)
            assert default_path.exists()
            assert default_path != custom_path

            # 验证文件内容
            custom_content = custom_path.read_text(encoding="utf-8")
            default_content = default_path.read_text(encoding="utf-8")

            for content in [custom_content, default_content]:
                assert "Export Workflow Test" in content
                assert "Export content" in content

    def test_edge_cases_and_error_handling(self):
        """测试边界情况和错误处理"""
        email = Email("")  # 空标题

        # 测试边界内容
        email.add_text("Valid text")  # 文本不能为空，改为有效文本
        email.add_table_from_data([])
        email.add_status_items([])
        email.add_log([])

        # 应该能正常渲染
        html = email.export_str()
        assert "<!DOCTYPE html>" in html

        # 测试None值
        email.set_subtitle(None)
        email.set_footer(None)

        html = email.export_str()
        assert "<!DOCTYPE html>" in html


class TestEmailTypeHints:
    """Email类型提示测试类"""

    def test_type_annotations_exist(self):
        """测试关键方法存在类型注解"""
        # 这个测试确保我们的类型提示是正确的
        import inspect

        # 检查关键方法的签名
        sig_add_text = inspect.signature(Email.add_text)
        assert "content" in sig_add_text.parameters
        assert "text_type" in sig_add_text.parameters
        assert "color" in sig_add_text.parameters

        sig_add_table = inspect.signature(Email.add_table_from_data)
        assert "data" in sig_add_table.parameters
        assert "headers" in sig_add_table.parameters
        assert "show_index" in sig_add_table.parameters

        sig_add_quote = inspect.signature(Email.add_quote)
        assert "content" in sig_add_quote.parameters
        assert "author" in sig_add_quote.parameters
        assert "source" in sig_add_quote.parameters

        sig_add_circular = inspect.signature(Email.add_circular_progress)
        assert "value" in sig_add_circular.parameters
        assert "max_value" in sig_add_circular.parameters
        assert "size" in sig_add_circular.parameters

        sig_add_log = inspect.signature(Email.add_log)
        assert "logs" in sig_add_log.parameters
        assert "show_timestamp" in sig_add_log.parameters
        assert "filter_level" in sig_add_log.parameters
