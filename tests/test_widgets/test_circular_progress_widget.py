"""圆形进度条Widget测试模块"""

from unittest.mock import patch

import pytest

from email_widget.core.enums import ProgressTheme
from email_widget.core.validators import RangeValidator, SizeValidator
from email_widget.widgets.circular_progress_widget import CircularProgressWidget


class TestCircularProgressWidget:
    """CircularProgressWidget测试类"""

    def setup_method(self):
        """每个测试方法前的设置"""
        self.widget = CircularProgressWidget()

    def test_init(self):
        """测试初始化"""
        assert self.widget._value == 0.0
        assert self.widget._max_value == 100.0
        assert self.widget._label is None
        assert self.widget._theme == ProgressTheme.PRIMARY
        assert self.widget._size == "100px"
        assert self.widget._stroke_width == "8px"

        # 验证验证器初始化
        assert isinstance(self.widget._value_validator, RangeValidator)
        assert isinstance(self.widget._size_validator, SizeValidator)

    def test_init_with_widget_id(self):
        """测试使用widget_id初始化"""
        widget = CircularProgressWidget("test_id")
        assert widget.widget_id == "test_id"

    def test_set_value_valid(self):
        """测试设置有效值"""
        with patch.object(self.widget._value_validator, "validate", return_value=True):
            result = self.widget.set_value(50.0)

            assert result is self.widget  # 支持链式调用
            assert self.widget._value == 50.0

    def test_set_value_invalid(self):
        """测试设置无效值"""
        with patch.object(self.widget._value_validator, "validate", return_value=False):
            with patch.object(
                self.widget._value_validator,
                "get_error_message",
                return_value="值超出范围",
            ):
                with pytest.raises(ValueError, match="进度值验证失败: 值超出范围"):
                    self.widget.set_value(-10)

    def test_set_value_clamp_to_max(self):
        """测试值被限制在最大值内"""
        with patch.object(self.widget._value_validator, "validate", return_value=True):
            self.widget.set_max_value(80.0)
            self.widget.set_value(120.0)

            assert self.widget._value == 80.0  # 被限制在最大值

    def test_set_value_clamp_to_zero(self):
        """测试值被限制在0以上"""
        with patch.object(self.widget._value_validator, "validate", return_value=True):
            self.widget.set_value(-10.0)

            assert self.widget._value == 0.0  # 被限制在0

    def test_set_max_value(self):
        """测试设置最大值"""
        result = self.widget.set_max_value(200.0)

        assert result is self.widget
        assert self.widget._max_value == 200.0

    def test_set_label(self):
        """测试设置标签"""
        result = self.widget.set_label("进度标签")

        assert result is self.widget
        assert self.widget._label == "进度标签"

    def test_set_theme(self):
        """测试设置主题"""
        result = self.widget.set_theme(ProgressTheme.SUCCESS)

        assert result is self.widget
        assert self.widget._theme == ProgressTheme.SUCCESS

    def test_set_size_valid(self):
        """测试设置有效尺寸"""
        with patch.object(self.widget._size_validator, "validate", return_value=True):
            result = self.widget.set_size("150px")

            assert result is self.widget
            assert self.widget._size == "150px"

    def test_set_size_invalid(self):
        """测试设置无效尺寸"""
        with patch.object(self.widget._size_validator, "validate", return_value=False):
            with patch.object(
                self.widget._size_validator,
                "get_error_message",
                return_value="尺寸格式错误",
            ):
                with pytest.raises(ValueError, match="尺寸值验证失败: 尺寸格式错误"):
                    self.widget.set_size("invalid")

    def test_set_stroke_width(self):
        """测试设置线条宽度"""
        result = self.widget.set_stroke_width("12px")

        assert result is self.widget
        assert self.widget._stroke_width == "12px"

    def test_increment(self):
        """测试增加进度值"""
        self.widget._value = 30.0
        self.widget._max_value = 100.0

        result = self.widget.increment(20.0)

        assert result is self.widget
        assert self.widget._value == 50.0

    def test_increment_default_amount(self):
        """测试默认增加量"""
        self.widget._value = 30.0

        result = self.widget.increment()

        assert result is self.widget
        assert self.widget._value == 31.0

    def test_increment_clamp_to_max(self):
        """测试增加值被限制在最大值"""
        self.widget._value = 90.0
        self.widget._max_value = 100.0

        self.widget.increment(20.0)

        assert self.widget._value == 100.0

    def test_decrement(self):
        """测试减少进度值"""
        self.widget._value = 50.0

        result = self.widget.decrement(20.0)

        assert result is self.widget
        assert self.widget._value == 30.0

    def test_decrement_default_amount(self):
        """测试默认减少量"""
        self.widget._value = 30.0

        result = self.widget.decrement()

        assert result is self.widget
        assert self.widget._value == 29.0

    def test_decrement_clamp_to_zero(self):
        """测试减少值被限制在0"""
        self.widget._value = 10.0

        self.widget.decrement(20.0)

        assert self.widget._value == 0.0

    def test_reset(self):
        """测试重置进度"""
        self.widget._value = 75.0

        result = self.widget.reset()

        assert result is self.widget
        assert self.widget._value == 0.0

    def test_complete(self):
        """测试设置为完成状态"""
        self.widget._max_value = 100.0

        result = self.widget.complete()

        assert result is self.widget
        assert self.widget._value == 100.0

    def test_get_theme_color(self):
        """测试获取主题颜色"""
        # 测试不同主题的颜色
        test_cases = [
            (ProgressTheme.PRIMARY, "#0078d4"),
            (ProgressTheme.SUCCESS, "#107c10"),
            (ProgressTheme.WARNING, "#ff8c00"),
            (ProgressTheme.ERROR, "#d13438"),
            (ProgressTheme.INFO, "#0078d4"),
        ]

        for theme, expected_color in test_cases:
            self.widget._theme = theme
            color = self.widget._get_theme_color()
            assert color == expected_color

    def test_get_template_name(self):
        """测试获取模板名称"""
        assert self.widget._get_template_name() == "circular_progress.html"

    def test_get_template_context_basic(self):
        """测试基本模板上下文"""
        self.widget._value = 60.0
        self.widget._max_value = 100.0
        self.widget._size = "120px"
        self.widget._stroke_width = "10px"
        self.widget._theme = ProgressTheme.SUCCESS

        context = self.widget.get_template_context()

        # 验证基本数据
        assert context["percentage"] == "60.0"
        assert context["label"] is None

        # 验证样式存在
        assert "wrapper_style" in context
        assert "container_style" in context
        assert "inner_style" in context
        assert "label_style" in context

        # 验证主题颜色应用
        assert "#107c10" in context["container_style"]  # SUCCESS主题色

    def test_get_template_context_with_label(self):
        """测试带标签的模板上下文"""
        self.widget._value = 75.0
        self.widget._max_value = 100.0
        self.widget._label = "上传进度"

        context = self.widget.get_template_context()

        assert context["label"] == "上传进度"
        assert context["percentage"] == "75.0"

    def test_get_template_context_zero_max_value(self):
        """测试最大值为0的模板上下文"""
        self.widget._value = 50.0
        self.widget._max_value = 0.0

        context = self.widget.get_template_context()

        assert float(context["percentage"]) == float("0")  # 避免除零错误

    def test_get_template_context_percentage_calculation(self):
        """测试百分比计算"""
        test_cases = [
            (25.0, 100.0, "25.0"),
            (33.333, 100.0, "33.3"),
            (50.0, 200.0, "25.0"),
            (150.0, 300.0, "50.0"),
        ]

        for value, max_value, expected_percentage in test_cases:
            self.widget._value = value
            self.widget._max_value = max_value

            context = self.widget.get_template_context()
            assert context["percentage"] == expected_percentage


class TestCircularProgressWidgetIntegration:
    """CircularProgressWidget集成测试类"""

    def test_chaining_methods(self):
        """测试方法链式调用"""
        with patch(
            "email_widget.core.validators.RangeValidator.validate", return_value=True
        ):
            with patch(
                "email_widget.core.validators.SizeValidator.validate", return_value=True
            ):
                widget = (
                    CircularProgressWidget("test_id")
                    .set_value(75.0)
                    .set_max_value(100.0)
                    .set_label("下载进度")
                    .set_theme(ProgressTheme.WARNING)
                    .set_size("150px")
                    .set_stroke_width("12px")
                )

                assert widget.widget_id == "test_id"
                assert widget._value == 75.0
                assert widget._max_value == 100.0
                assert widget._label == "下载进度"
                assert widget._theme == ProgressTheme.WARNING
                assert widget._size == "150px"
                assert widget._stroke_width == "12px"

    def test_full_workflow(self):
        """测试完整工作流程"""
        with patch(
            "email_widget.core.validators.RangeValidator.validate", return_value=True
        ):
            widget = CircularProgressWidget()

            # 模拟进度更新流程
            widget.set_max_value(100.0)
            widget.set_label("文件处理")
            widget.set_theme(ProgressTheme.INFO)
            widget.set_size("120px")

            # 逐步更新进度
            widget.set_value(0.0)
            assert widget._value == 0.0

            widget.increment(25.0)
            assert widget._value == 25.0

            widget.increment(35.0)
            assert widget._value == 60.0

            widget.complete()
            assert widget._value == 100.0

            # 获取最终模板上下文
            context = widget.get_template_context()
            assert context["percentage"] == "100.0"
            assert context["label"] == "文件处理"

    def test_progress_operations(self):
        """测试进度操作"""
        widget = CircularProgressWidget()
        widget._max_value = 100.0

        # 测试各种进度操作
        widget.set_value(50.0)
        assert widget._value == 50.0

        widget.increment(20.0)
        assert widget._value == 70.0

        widget.decrement(10.0)
        assert widget._value == 60.0

        widget.reset()
        assert widget._value == 0.0

        widget.complete()
        assert widget._value == 100.0

    def test_validation_integration(self):
        """测试验证器集成"""
        widget = CircularProgressWidget()

        # 测试值验证失败
        with patch.object(widget._value_validator, "validate", return_value=False):
            with patch.object(
                widget._value_validator, "get_error_message", return_value="验证失败"
            ):
                with pytest.raises(ValueError):
                    widget.set_value(999999)

        # 测试尺寸验证失败
        with patch.object(widget._size_validator, "validate", return_value=False):
            with patch.object(
                widget._size_validator, "get_error_message", return_value="验证失败"
            ):
                with pytest.raises(ValueError):
                    widget.set_size("invalid")
