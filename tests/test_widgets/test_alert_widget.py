"""AlertWidget测试用例"""

import pytest

from email_widget.core.enums import AlertType
from email_widget.widgets.alert_widget import AlertWidget


class TestAlertWidget:
    """AlertWidget测试类"""

    def setup_method(self):
        """每个测试方法执行前的设置"""
        self.widget = AlertWidget()

    def test_init_default_values(self):
        """测试初始化默认值"""
        widget = AlertWidget("test_id")
        assert widget._widget_id == "test_id"
        assert widget._content == ""
        assert widget._alert_type == AlertType.NOTE
        assert widget._title is None
        assert widget._icon is None
        assert widget._show_icon is True
        assert widget._border_radius == "6px"
        assert widget._padding == "16px"

    def test_init_validators(self):
        """测试验证器初始化"""
        widget = AlertWidget()
        assert hasattr(widget, "_content_validator")
        assert hasattr(widget, "_size_validator")

    @pytest.mark.parametrize(
        "content,should_pass",
        [
            ("This is an alert", True),
            ("多行警告\n第二行内容", True),
            ("", False),
            ("   ", False),
        ],
    )
    def test_set_content_validation(self, content, should_pass):
        """测试内容验证"""
        if should_pass:
            result = self.widget.set_content(content)
            assert result is self.widget
            assert self.widget._content == content
        else:
            with pytest.raises(ValueError, match="警告内容验证失败"):
                self.widget.set_content(content)

    @pytest.mark.parametrize(
        "alert_type",
        [
            AlertType.NOTE,
            AlertType.TIP,
            AlertType.IMPORTANT,
            AlertType.WARNING,
            AlertType.CAUTION,
        ],
    )
    def test_set_alert_type(self, alert_type):
        """测试设置警告类型"""
        result = self.widget.set_alert_type(alert_type)
        assert result is self.widget
        assert self.widget._alert_type == alert_type

    def test_set_title(self):
        """测试设置标题"""
        title = "Custom Title"
        result = self.widget.set_title(title)
        assert result is self.widget
        assert self.widget._title == title

    def test_set_icon(self):
        """测试设置图标"""
        icon = "⚠️"
        result = self.widget.set_icon(icon)
        assert result is self.widget
        assert self.widget._icon == icon

    @pytest.mark.parametrize("show_icon", [True, False])
    def test_show_icon(self, show_icon):
        """测试显示图标设置"""
        result = self.widget.show_icon(show_icon)
        assert result is self.widget
        assert self.widget._show_icon == show_icon

    @pytest.mark.parametrize(
        "alert_type,expected_icon",
        [
            (AlertType.NOTE, "ℹ️"),
            (AlertType.TIP, "💡"),
            (AlertType.IMPORTANT, "❗"),
            (AlertType.WARNING, "⚠️"),
            (AlertType.CAUTION, "🚨"),
        ],
    )
    def test_get_default_icon(self, alert_type, expected_icon):
        """测试默认图标获取"""
        self.widget.set_alert_type(alert_type)
        assert self.widget._get_default_icon() == expected_icon

    @pytest.mark.parametrize(
        "alert_type,expected_title",
        [
            (AlertType.NOTE, "注意"),
            (AlertType.TIP, "提示"),
            (AlertType.IMPORTANT, "重要"),
            (AlertType.WARNING, "警告"),
            (AlertType.CAUTION, "危险"),
        ],
    )
    def test_get_default_title(self, alert_type, expected_title):
        """测试默认标题获取"""
        self.widget.set_alert_type(alert_type)
        assert self.widget._get_default_title() == expected_title

    @pytest.mark.parametrize(
        "alert_type,expected_styles",
        [
            (
                AlertType.NOTE,
                {"background": "#dbeafe", "border": "#3b82f6", "color": "#1e40af"},
            ),
            (
                AlertType.TIP,
                {"background": "#dcfce7", "border": "#22c55e", "color": "#15803d"},
            ),
            (
                AlertType.IMPORTANT,
                {"background": "#fef3c7", "border": "#f59e0b", "color": "#d97706"},
            ),
            (
                AlertType.WARNING,
                {"background": "#fed7aa", "border": "#f97316", "color": "#ea580c"},
            ),
            (
                AlertType.CAUTION,
                {"background": "#fecaca", "border": "#ef4444", "color": "#dc2626"},
            ),
        ],
    )
    def test_get_alert_styles(self, alert_type, expected_styles):
        """测试警告框样式获取"""
        self.widget.set_alert_type(alert_type)
        styles = self.widget._get_alert_styles()
        assert styles == expected_styles

    def test_get_template_name(self):
        """测试模板名称获取"""
        assert self.widget._get_template_name() == "alert.html"

    def test_get_template_context_empty_content(self):
        """测试空内容时的模板上下文"""
        context = self.widget.get_template_context()
        assert context == {}

    def test_get_template_context_basic(self):
        """测试基本模板上下文"""
        self.widget.set_content("This is a warning message")
        self.widget.set_alert_type(AlertType.WARNING)

        context = self.widget.get_template_context()

        assert context["content"] == "This is a warning message"
        assert context["show_icon"] is True
        assert context["title"] == "警告"  # 默认标题
        assert context["icon"] == "⚠️"  # 默认图标
        assert "container_style" in context

    def test_get_template_context_custom_title_icon(self):
        """测试自定义标题和图标"""
        self.widget.set_content("Custom alert")
        self.widget.set_title("自定义标题")
        self.widget.set_icon("🔥")

        context = self.widget.get_template_context()

        assert context["title"] == "自定义标题"
        assert context["icon"] == "🔥"

    def test_get_template_context_no_icon(self):
        """测试不显示图标"""
        self.widget.set_content("No icon alert")
        self.widget.show_icon(False)

        context = self.widget.get_template_context()

        assert context["show_icon"] is False

    def test_get_template_context_styling(self):
        """测试样式生成"""
        self.widget.set_content("Styled alert")
        self.widget.set_alert_type(AlertType.CAUTION)

        context = self.widget.get_template_context()
        container_style = context["container_style"]

        assert "background: #fecaca" in container_style  # CAUTION background
        assert "border: 1px solid #ef4444" in container_style  # CAUTION border
        assert "border-left: 4px solid #ef4444" in container_style
        assert "color: #dc2626" in container_style  # CAUTION color

    def test_chain_methods(self):
        """测试方法链式调用"""
        result = (
            self.widget.set_content("Chained alert")
            .set_alert_type(AlertType.TIP)
            .set_title("提示信息")
            .set_icon("💡")
            .show_icon(True)
        )

        assert result is self.widget
        assert self.widget._content == "Chained alert"
        assert self.widget._alert_type == AlertType.TIP
        assert self.widget._title == "提示信息"
        assert self.widget._icon == "💡"
        assert self.widget._show_icon is True
