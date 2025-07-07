"""卡片Widget测试模块"""

from unittest.mock import patch

import pytest

from email_widget.core.enums import IconType, StatusType
from email_widget.core.validators import NonEmptyStringValidator, SizeValidator
from email_widget.widgets.card_widget import CardWidget


class TestCardWidget:
    """CardWidget测试类"""

    def setup_method(self):
        """每个测试方法前的设置"""
        self.widget = CardWidget()

    def test_init(self):
        """测试初始化"""
        assert self.widget._title is None
        assert self.widget._content == ""
        assert self.widget._status is None
        assert self.widget._icon == IconType.INFO.value
        assert self.widget._metadata == {}
        assert self.widget._elevated is True
        assert self.widget._padding == "16px"
        assert self.widget._border_radius == "4px"

        # 验证验证器初始化
        assert isinstance(self.widget._text_validator, NonEmptyStringValidator)
        assert isinstance(self.widget._size_validator, SizeValidator)

    def test_init_with_widget_id(self):
        """测试使用widget_id初始化"""
        widget = CardWidget("test_id")
        assert widget.widget_id == "test_id"

    def test_set_title_valid(self):
        """测试设置有效标题"""
        with patch.object(self.widget._text_validator, "validate", return_value=True):
            result = self.widget.set_title("测试标题")

            assert result is self.widget  # 支持链式调用
            assert self.widget._title == "测试标题"

    def test_set_title_invalid(self):
        """测试设置无效标题"""
        with patch.object(self.widget._text_validator, "validate", return_value=False):
            with patch.object(
                self.widget._text_validator,
                "get_error_message",
                return_value="标题不能为空",
            ):
                with pytest.raises(ValueError, match="标题验证失败: 标题不能为空"):
                    self.widget.set_title("")

    def test_set_content_valid(self):
        """测试设置有效内容"""
        with patch.object(self.widget._text_validator, "validate", return_value=True):
            result = self.widget.set_content("测试内容")

            assert result is self.widget
            assert self.widget._content == "测试内容"

    def test_set_content_invalid(self):
        """测试设置无效内容"""
        with patch.object(self.widget._text_validator, "validate", return_value=False):
            with patch.object(
                self.widget._text_validator,
                "get_error_message",
                return_value="内容不能为空",
            ):
                with pytest.raises(ValueError, match="内容验证失败: 内容不能为空"):
                    self.widget.set_content("")

    def test_set_status(self):
        """测试设置状态"""
        result = self.widget.set_status(StatusType.SUCCESS)

        assert result is self.widget
        assert self.widget._status == StatusType.SUCCESS

    def test_set_icon_with_icon_type(self):
        """测试使用IconType设置图标"""
        result = self.widget.set_icon(IconType.SUCCESS)

        assert result is self.widget
        assert self.widget._icon == IconType.SUCCESS.value

    def test_set_icon_with_string(self):
        """测试使用字符串设置图标"""
        result = self.widget.set_icon("custom_icon")

        assert result is self.widget
        assert self.widget._icon == "custom_icon"

    def test_add_metadata(self):
        """测试添加元数据"""
        result = self.widget.add_metadata("key1", "value1")

        assert result is self.widget
        assert self.widget._metadata == {"key1": "value1"}

        # 添加更多元数据
        self.widget.add_metadata("key2", "value2")
        assert self.widget._metadata == {"key1": "value1", "key2": "value2"}

    def test_set_metadata(self):
        """测试设置元数据"""
        metadata = {"key1": "value1", "key2": "value2"}
        result = self.widget.set_metadata(metadata)

        assert result is self.widget
        assert self.widget._metadata == {"key1": "value1", "key2": "value2"}

        # 验证是拷贝而非引用
        metadata["key3"] = "value3"
        assert "key3" not in self.widget._metadata

    def test_clear_metadata(self):
        """测试清空元数据"""
        self.widget._metadata = {"key1": "value1", "key2": "value2"}
        result = self.widget.clear_metadata()

        assert result is self.widget
        assert self.widget._metadata == {}

    def test_get_template_name(self):
        """测试获取模板名称"""
        assert self.widget._get_template_name() == "card.html"

    def test_get_template_context_empty(self):
        """测试空卡片的模板上下文"""
        context = self.widget.get_template_context()
        assert context == {}

    def test_get_template_context_with_title_only(self):
        """测试只有标题的模板上下文"""
        self.widget._title = "测试标题"

        context = self.widget.get_template_context()

        assert context["title"] == "测试标题"
        assert context["content"] == ""
        assert context["icon"] == IconType.INFO.value
        assert context["metadata"] is None
        assert "card_style" in context
        assert "title_style" in context
        assert "content_style" in context

    def test_get_template_context_with_content_only(self):
        """测试只有内容的模板上下文"""
        self.widget._content = "测试内容"

        context = self.widget.get_template_context()

        assert context["title"] is None
        assert context["content"] == "测试内容"

    def test_get_template_context_full(self):
        """测试完整卡片的模板上下文"""
        self.widget._title = "测试标题"
        self.widget._content = "测试内容"
        self.widget._icon = "test_icon"
        self.widget._metadata = {"key1": "value1", "key2": "value2"}
        self.widget._elevated = True
        self.widget._padding = "20px"
        self.widget._border_radius = "8px"

        context = self.widget.get_template_context()

        assert context["title"] == "测试标题"
        assert context["content"] == "测试内容"
        assert context["icon"] == "test_icon"
        assert context["metadata"] == {"key1": "value1", "key2": "value2"}

        # 验证样式包含elevation
        assert "box-shadow" in context["card_style"]
        assert "padding: 20px" in context["card_style"]
        assert "border-radius: 8px" in context["card_style"]

    def test_get_template_context_no_elevation(self):
        """测试无阴影效果的模板上下文"""
        self.widget._title = "测试标题"
        self.widget._elevated = False

        context = self.widget.get_template_context()

        # 验证样式不包含box-shadow
        assert "box-shadow" not in context["card_style"]

    def test_get_template_context_no_metadata(self):
        """测试无元数据的模板上下文"""
        self.widget._title = "测试标题"
        self.widget._metadata = {}

        context = self.widget.get_template_context()

        assert context["metadata"] is None


class TestCardWidgetIntegration:
    """CardWidget集成测试类"""

    def test_chaining_methods(self):
        """测试方法链式调用"""
        with patch(
            "email_widget.core.validators.NonEmptyStringValidator.validate",
            return_value=True,
        ):
            widget = (
                CardWidget("test_id")
                .set_title("测试标题")
                .set_content("测试内容")
                .set_status(StatusType.SUCCESS)
                .set_icon(IconType.SUCCESS)
                .add_metadata("key1", "value1")
                .add_metadata("key2", "value2")
            )

            assert widget.widget_id == "test_id"
            assert widget._title == "测试标题"
            assert widget._content == "测试内容"
            assert widget._status == StatusType.SUCCESS
            assert widget._icon == IconType.SUCCESS.value
            assert widget._metadata == {"key1": "value1", "key2": "value2"}

    def test_full_workflow(self):
        """测试完整工作流程"""
        with patch(
            "email_widget.core.validators.NonEmptyStringValidator.validate",
            return_value=True,
        ):
            widget = CardWidget()

            # 配置卡片
            widget.set_title("项目状态")
            widget.set_content("项目进展顺利，预计下周完成。")
            widget.set_status(StatusType.SUCCESS)
            widget.set_icon(IconType.SUCCESS)
            widget.add_metadata("负责人", "张三")
            widget.add_metadata("截止日期", "2024-01-15")

            # 获取模板上下文
            context = widget.get_template_context()

            # 验证完整上下文
            assert context["title"] == "项目状态"
            assert context["content"] == "项目进展顺利，预计下周完成。"
            assert context["icon"] == IconType.SUCCESS.value
            assert context["metadata"] == {"负责人": "张三", "截止日期": "2024-01-15"}

            # 验证样式存在
            assert "card_style" in context
            assert "title_style" in context
            assert "content_style" in context
            assert "metadata_container_style" in context
            assert "metadata_item_style" in context

    def test_metadata_operations(self):
        """测试元数据操作"""
        widget = CardWidget()

        # 添加元数据
        widget.add_metadata("key1", "value1")
        widget.add_metadata("key2", "value2")
        assert widget._metadata == {"key1": "value1", "key2": "value2"}

        # 设置新的元数据（覆盖）
        new_metadata = {"key3": "value3", "key4": "value4"}
        widget.set_metadata(new_metadata)
        assert widget._metadata == {"key3": "value3", "key4": "value4"}

        # 清空元数据
        widget.clear_metadata()
        assert widget._metadata == {}

    def test_validation_integration(self):
        """测试验证器集成"""
        widget = CardWidget()

        # 测试标题验证失败
        with patch.object(widget._text_validator, "validate", return_value=False):
            with patch.object(
                widget._text_validator, "get_error_message", return_value="验证失败"
            ):
                with pytest.raises(ValueError):
                    widget.set_title("")

        # 测试内容验证失败
        with patch.object(widget._text_validator, "validate", return_value=False):
            with patch.object(
                widget._text_validator, "get_error_message", return_value="验证失败"
            ):
                with pytest.raises(ValueError):
                    widget.set_content("")
