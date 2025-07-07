"""ProgressWidget测试用例"""

import pytest

from email_widget.core.enums import ProgressTheme
from email_widget.widgets.progress_widget import ProgressWidget


class TestProgressWidget:
    """ProgressWidget测试类"""

    def setup_method(self):
        """每个测试方法执行前的设置"""
        self.widget = ProgressWidget()

    def test_init_default_values(self):
        """测试初始化默认值"""
        widget = ProgressWidget("test_id")
        assert widget._widget_id == "test_id"
        assert widget._value == 0.0
        assert widget._max_value == 100.0
        assert widget._label is None
        assert widget._theme == ProgressTheme.PRIMARY
        assert widget._show_percentage is True
        assert widget._width == "100%"
        assert widget._height == "20px"
        assert widget._border_radius == "10px"
        assert widget._background_color == "#e1dfdd"

    def test_init_validators(self):
        """测试验证器初始化"""
        widget = ProgressWidget()
        assert hasattr(widget, "_value_validator")
        assert hasattr(widget, "_size_validator")
        assert hasattr(widget, "_color_validator")

    @pytest.mark.parametrize(
        "value,should_pass",
        [
            (0, True),
            (50, True),
            (100, True),
            (150, True),  # 会被限制到max_value
            (-10, False),  # 会被限制到0
            ("invalid", False),
        ],
    )
    def test_set_value_validation(self, value, should_pass):
        """测试进度值验证"""
        if should_pass and isinstance(value, (int, float)):
            result = self.widget.set_value(value)
            assert result is self.widget
            expected_value = max(0, min(value, self.widget._max_value))
            assert self.widget._value == expected_value
        elif not should_pass:
            with pytest.raises(ValueError, match="进度值验证失败"):
                self.widget.set_value(value)

    def test_set_max_value(self):
        """测试设置最大值"""
        result = self.widget.set_max_value(200)
        assert result is self.widget
        assert self.widget._max_value == 200

        # 测试当前值超过新的最大值时的处理
        self.widget.set_value(150)
        self.widget.set_max_value(100)
        assert self.widget._value == 100

    def test_set_label(self):
        """测试设置标签"""
        label = "Loading progress"
        result = self.widget.set_label(label)
        assert result is self.widget
        assert self.widget._label == label

    @pytest.mark.parametrize(
        "theme",
        [
            ProgressTheme.PRIMARY,
            ProgressTheme.SUCCESS,
            ProgressTheme.WARNING,
            ProgressTheme.ERROR,
            ProgressTheme.INFO,
        ],
    )
    def test_set_theme(self, theme):
        """测试设置主题"""
        result = self.widget.set_theme(theme)
        assert result is self.widget
        assert self.widget._theme == theme

    @pytest.mark.parametrize("show", [True, False])
    def test_show_percentage(self, show):
        """测试显示百分比设置"""
        result = self.widget.show_percentage(show)
        assert result is self.widget
        assert self.widget._show_percentage == show

    @pytest.mark.parametrize(
        "width,should_pass",
        [
            ("100%", True),
            ("200px", True),
            ("50em", True),
            ("invalid_width", False),
            ("", False),
        ],
    )
    def test_set_width_validation(self, width, should_pass):
        """测试宽度验证"""
        if should_pass:
            result = self.widget.set_width(width)
            assert result is self.widget
            assert self.widget._width == width
        else:
            with pytest.raises(ValueError, match="宽度值验证失败"):
                self.widget.set_width(width)

    def test_set_height(self):
        """测试设置高度"""
        height = "30px"
        result = self.widget.set_height(height)
        assert result is self.widget
        assert self.widget._height == height

    def test_set_border_radius(self):
        """测试设置边框圆角"""
        radius = "5px"
        result = self.widget.set_border_radius(radius)
        assert result is self.widget
        assert self.widget._border_radius == radius

    @pytest.mark.parametrize(
        "color,should_pass",
        [
            ("#ff0000", True),
            ("red", True),
            ("rgb(255,0,0)", True),
            ("invalid_color", False),
            ("", False),
        ],
    )
    def test_set_background_color_validation(self, color, should_pass):
        """测试背景颜色验证"""
        if should_pass:
            result = self.widget.set_background_color(color)
            assert result is self.widget
            assert self.widget._background_color == color
        else:
            with pytest.raises(ValueError, match="背景颜色验证失败"):
                self.widget.set_background_color(color)

    def test_increment(self):
        """测试增加进度值"""
        self.widget.set_value(50)
        result = self.widget.increment(10)
        assert result is self.widget
        assert self.widget._value == 60

        # 测试增加到超过最大值
        self.widget.increment(50)
        assert self.widget._value == 100  # 应该被限制到max_value

    def test_decrement(self):
        """测试减少进度值"""
        self.widget.set_value(50)
        result = self.widget.decrement(10)
        assert result is self.widget
        assert self.widget._value == 40

        # 测试减少到小于0
        self.widget.decrement(50)
        assert self.widget._value == 0  # 应该被限制到0

    def test_reset(self):
        """测试重置进度"""
        self.widget.set_value(75)
        result = self.widget.reset()
        assert result is self.widget
        assert self.widget._value == 0

    def test_complete(self):
        """测试完成状态"""
        result = self.widget.complete()
        assert result is self.widget
        assert self.widget._value == self.widget._max_value

    @pytest.mark.parametrize(
        "theme,expected_color",
        [
            (ProgressTheme.PRIMARY, "#0078d4"),
            (ProgressTheme.SUCCESS, "#107c10"),
            (ProgressTheme.WARNING, "#ff8c00"),
            (ProgressTheme.ERROR, "#d13438"),
            (ProgressTheme.INFO, "#0078d4"),
        ],
    )
    def test_get_theme_color(self, theme, expected_color):
        """测试主题颜色获取"""
        self.widget.set_theme(theme)
        assert self.widget._get_theme_color() == expected_color

    @pytest.mark.parametrize(
        "value,max_value,expected_percentage",
        [
            (0, 100, 0),
            (50, 100, 50),
            (100, 100, 100),
            (75, 200, 37.5),
            (0, 0, 0),  # 边界情况
        ],
    )
    def test_get_percentage(self, value, max_value, expected_percentage):
        """测试百分比计算"""
        self.widget.set_max_value(max_value)
        self.widget.set_value(value)
        assert self.widget._get_percentage() == expected_percentage

    def test_properties(self):
        """测试属性获取"""
        self.widget.set_value(75)
        self.widget.set_max_value(150)

        assert self.widget.value == 75
        assert self.widget.max_value == 150
        assert self.widget.percentage == 50.0

    def test_get_template_name(self):
        """测试模板名称获取"""
        assert self.widget._get_template_name() == "progress.html"

    def test_get_template_context_basic(self):
        """测试基本模板上下文"""
        self.widget.set_value(60)
        self.widget.set_label("Loading...")

        context = self.widget.get_template_context()

        assert context["label"] == "Loading..."
        assert context["show_percentage"] is True
        assert context["percentage"] == "60.0"
        assert "container_style" in context
        assert "label_style" in context
        assert "progress_container_style" in context
        assert "progress_fill_style" in context
        assert "percentage_style" in context

    def test_get_template_context_styling(self):
        """测试样式生成"""
        self.widget.set_value(75)
        self.widget.set_width("300px")
        self.widget.set_height("25px")
        self.widget.set_border_radius("15px")
        self.widget.set_background_color("#f0f0f0")
        self.widget.set_theme(ProgressTheme.SUCCESS)

        context = self.widget.get_template_context()

        progress_container_style = context["progress_container_style"]
        progress_fill_style = context["progress_fill_style"]

        assert "width: 300px" in progress_container_style
        assert "height: 25px" in progress_container_style
        assert "background: #f0f0f0" in progress_container_style
        assert "border-radius: 15px" in progress_container_style

        assert "width: 75.0%" in progress_fill_style
        assert "background: #107c10" in progress_fill_style  # SUCCESS theme color

    def test_get_template_context_percentage_text_color(self):
        """测试百分比文字颜色"""
        # 测试进度超过50%时文字为白色
        self.widget.set_value(60)
        context = self.widget.get_template_context()
        assert "color: #ffffff" in context["percentage_style"]

        # 测试进度小于50%时文字为深色
        self.widget.set_value(40)
        context = self.widget.get_template_context()
        assert "color: #323130" in context["percentage_style"]

    def test_get_template_context_no_percentage(self):
        """测试不显示百分比"""
        self.widget.set_value(50)
        self.widget.show_percentage(False)

        context = self.widget.get_template_context()
        assert context["show_percentage"] is False

    def test_chain_methods(self):
        """测试方法链式调用"""
        result = (
            self.widget.set_value(80)
            .set_label("Progress")
            .set_theme(ProgressTheme.SUCCESS)
            .set_width("250px")
            .set_height("30px")
            .show_percentage(True)
        )

        assert result is self.widget
        assert self.widget._value == 80
        assert self.widget._label == "Progress"
        assert self.widget._theme == ProgressTheme.SUCCESS
        assert self.widget._width == "250px"
        assert self.widget._height == "30px"
        assert self.widget._show_percentage is True

    def test_edge_cases(self):
        """测试边界情况"""
        # 测试0值和最大值
        self.widget.set_value(0)
        assert self.widget._value == 0

        self.widget.set_value(1000)  # 超过默认max_value
        assert self.widget._value == 100

        # 测试负值
        with pytest.raises(ValueError):
            self.widget.set_value(-50)
            assert self.widget._value == 0

        # 测试最大值为0的情况
        self.widget.set_max_value(0)
        assert self.widget._get_percentage() == 0
