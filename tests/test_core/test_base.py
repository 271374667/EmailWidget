"""BaseWidget组件的完整测试套件。

测试覆盖：
- Widget抽象基类功能
- 模板渲染机制
- ID生成和管理
- Widget生命周期
"""

from unittest.mock import Mock, patch

import pytest

from email_widget.core.base import BaseWidget


class ConcreteWidget(BaseWidget):
    """用于测试的具体Widget实现"""

    TEMPLATE = "<div class='test-widget'>{{ test_data }}</div>"

    def _get_template_name(self) -> str:
        return "test_widget.html"

    def get_template_context(self) -> dict:
        return {"test_data": "test_value"}


class TestBaseWidgetInitialization:
    """BaseWidget初始化测试"""

    def test_init_without_id(self):
        """测试无ID初始化"""
        widget = ConcreteWidget()

        assert widget.widget_id is not None
        assert isinstance(widget.widget_id, str)
        assert len(widget.widget_id) > 0
        assert widget.parent is None

    def test_init_with_custom_id(self):
        """测试自定义ID初始化"""
        custom_id = "custom_widget_123"
        widget = ConcreteWidget(widget_id=custom_id)

        assert widget.widget_id == custom_id
        assert widget.parent is None

    def test_multiple_widgets_unique_ids(self):
        """测试多个Widget有唯一ID"""
        widgets = [ConcreteWidget() for _ in range(10)]
        ids = [w.widget_id for w in widgets]

        # 所有ID应该唯一
        assert len(set(ids)) == len(ids)

    def test_generate_id_format(self):
        """测试生成ID的格式"""
        widget = ConcreteWidget()

        # ID格式应该是 {类名小写}_{8位随机十六进制字符}
        assert widget.widget_id.startswith("concretewidget_")
        parts = widget.widget_id.split("_")
        assert len(parts) == 2
        assert len(parts[1]) == 8  # 8位十六进制字符


class TestBaseWidgetAbstractMethods:
    """BaseWidget抽象方法测试"""

    def test_abstract_base_cannot_instantiate(self):
        """测试抽象基类不能直接实例化"""
        with pytest.raises(TypeError):
            BaseWidget()

    def test_subclass_must_implement_get_template_name(self):
        """测试子类必须实现get_template_name"""

        class IncompleteWidget(BaseWidget):
            def get_template_context(self):
                return {}

        with pytest.raises(TypeError):
            IncompleteWidget()

    def test_subclass_must_implement_get_template_context(self):
        """测试子类必须实现get_template_context"""

        class IncompleteWidget(BaseWidget):
            def _get_template_name(self):
                return "test.html"

        with pytest.raises(TypeError):
            IncompleteWidget()

    def test_valid_subclass_implementation(self):
        """测试有效子类实现"""
        widget = ConcreteWidget()
        assert widget._get_template_name() == "test_widget.html"
        assert widget.get_template_context() == {"test_data": "test_value"}


class TestBaseWidgetProperties:
    """BaseWidget属性测试"""

    def test_widget_id_property(self):
        """测试widget_id属性"""
        widget = ConcreteWidget()
        assert hasattr(widget, "widget_id")
        assert isinstance(widget.widget_id, str)

    def test_parent_property(self):
        """测试parent属性"""
        widget = ConcreteWidget()
        assert hasattr(widget, "parent")
        assert widget.parent is None

    def test_set_widget_id_method(self):
        """测试set_widget_id方法"""
        widget = ConcreteWidget()
        original_id = widget.widget_id

        new_id = "new_test_id"
        result = widget.set_widget_id(new_id)

        # 验证链式调用
        assert result is widget
        # 验证ID被更新
        assert widget.widget_id == new_id
        assert widget.widget_id != original_id

    def test_set_parent_method(self):
        """测试_set_parent方法"""
        widget = ConcreteWidget()
        mock_email = Mock()

        widget._set_parent(mock_email)
        assert widget.parent is mock_email


class TestBaseWidgetTemplateRendering:
    """BaseWidget模板渲染测试"""

    def test_render_html_method_exists(self):
        """测试render_html方法存在"""
        widget = ConcreteWidget()
        assert hasattr(widget, "render_html")
        assert callable(widget.render_html)

    @patch("email_widget.core.base.get_template_engine")
    def test_render_html_calls_template_engine(self, mock_get_template_engine):
        """测试render_html调用模板引擎"""
        mock_engine = Mock()
        mock_get_template_engine.return_value = mock_engine
        mock_engine.render_safe.return_value = "<div>test</div>"

        widget = ConcreteWidget()
        result = widget.render_html()

        mock_engine.render_safe.assert_called_once()
        assert result == "<div>test</div>"

    def test_render_html_without_template(self):
        """测试没有TEMPLATE属性时的渲染"""

        class NoTemplateWidget(BaseWidget):
            def _get_template_name(self):
                return "no_template.html"

            def get_template_context(self):
                return {}

        widget = NoTemplateWidget()
        result = widget.render_html()

        # 应该返回错误回退HTML
        assert "Widget渲染错误" in result
        assert "NoTemplateWidget" in result

    def test_render_html_with_invalid_context(self):
        """测试get_template_context返回非字典时的处理"""

        class InvalidContextWidget(BaseWidget):
            TEMPLATE = "<div>test</div>"

            def _get_template_name(self):
                return "invalid.html"

            def get_template_context(self):
                return "not a dict"  # 返回非字典

        widget = InvalidContextWidget()
        result = widget.render_html()

        # 应该返回错误回退HTML
        assert "Widget渲染错误" in result
        assert "上下文数据错误" in result

    @patch("email_widget.core.base.get_template_engine")
    def test_render_html_template_engine_exception(self, mock_get_template_engine):
        """测试模板引擎抛出异常时的处理"""
        mock_engine = Mock()
        mock_get_template_engine.return_value = mock_engine
        mock_engine.render_safe.side_effect = Exception("模板错误")

        widget = ConcreteWidget()
        result = widget.render_html()

        # 应该返回错误回退HTML
        assert "Widget渲染错误" in result
        assert "ConcreteWidget" in result


class TestBaseWidgetErrorHandling:
    """BaseWidget错误处理测试"""

    def test_render_error_fallback(self):
        """测试渲染错误回退方法"""
        widget = ConcreteWidget()
        error_msg = "测试错误"

        result = widget._render_error_fallback(error_msg)

        assert "Widget渲染错误" in result
        assert "ConcreteWidget" in result
        assert widget.widget_id in result
        assert error_msg in result

    def test_render_error_fallback_no_message(self):
        """测试渲染错误回退方法（无错误消息）"""
        widget = ConcreteWidget()

        result = widget._render_error_fallback()

        assert "Widget渲染错误" in result
        assert "ConcreteWidget" in result
        assert widget.widget_id in result

    def test_exception_in_get_template_context(self):
        """测试get_template_context抛出异常的处理"""

        class ExceptionWidget(BaseWidget):
            TEMPLATE = "<div>test</div>"

            def _get_template_name(self):
                return "exception.html"

            def get_template_context(self):
                raise ValueError("上下文错误")

        widget = ExceptionWidget()
        result = widget.render_html()

        # 应该返回错误回退HTML
        assert "Widget渲染错误" in result
        assert "ExceptionWidget" in result


class TestBaseWidgetUtilityMethods:
    """BaseWidget工具方法测试"""

    def test_widget_has_logger(self):
        """测试Widget有logger属性"""
        widget = ConcreteWidget()
        assert hasattr(widget, "_logger")

    def test_widget_has_template_engine(self):
        """测试Widget有template_engine属性"""
        widget = ConcreteWidget()
        assert hasattr(widget, "_template_engine")

    def test_generate_id_method(self):
        """测试生成ID方法"""
        widget = ConcreteWidget()

        # 生成新ID
        new_id = widget._generate_id()

        assert isinstance(new_id, str)
        assert new_id.startswith("concretewidget_")
        assert len(new_id.split("_")[1]) == 8


class TestBaseWidgetValidation:
    """BaseWidget验证测试"""

    def test_validate_widget_id_format(self):
        """测试Widget ID格式验证"""
        # 有效ID格式
        valid_ids = ["widget_123", "test-widget", "widget.1", "widget_test_123"]
        for valid_id in valid_ids:
            widget = ConcreteWidget(widget_id=valid_id)
            assert widget.widget_id == valid_id

    def test_validate_template_context_type(self):
        """测试模板上下文类型验证"""
        widget = ConcreteWidget()
        context = widget.get_template_context()

        assert isinstance(context, dict)

        # 上下文值应该是可序列化的类型
        for key, value in context.items():
            assert isinstance(key, str)
            # value应该是JSON可序列化的类型
            assert value is None or isinstance(
                value, (str, int, float, bool, list, dict)
            )

    def test_template_attribute_exists(self):
        """测试TEMPLATE属性存在"""
        widget = ConcreteWidget()
        assert hasattr(widget, "TEMPLATE")
        assert isinstance(widget.TEMPLATE, str)
        assert len(widget.TEMPLATE) > 0


class TestBaseWidgetIntegration:
    """BaseWidget集成测试"""

    @patch("email_widget.core.base.get_template_engine")
    def test_complete_widget_workflow(self, mock_get_template_engine):
        """测试完整Widget工作流程"""
        mock_engine = Mock()
        mock_get_template_engine.return_value = mock_engine
        mock_engine.render_safe.return_value = (
            "<div class='test-widget'>test_value</div>"
        )

        # 创建Widget
        widget = ConcreteWidget(widget_id="test_widget")

        # 验证初始化
        assert widget.widget_id == "test_widget"
        assert widget.parent is None

        # 模拟设置父容器
        mock_email = Mock()
        widget._set_parent(mock_email)
        assert widget.parent is mock_email

        # 渲染Widget
        html = widget.render_html()
        assert html == "<div class='test-widget'>test_value</div>"

        # 验证模板引擎被正确调用
        mock_engine.render_safe.assert_called_once()
        call_args = mock_engine.render_safe.call_args
        assert call_args[0][0] == widget.TEMPLATE  # 模板字符串
        assert call_args[0][1] == {"test_data": "test_value"}  # 上下文

    def test_widget_factory_pattern(self):
        """测试Widget工厂模式"""

        class WidgetFactory:
            @staticmethod
            def create_widget(widget_type, widget_id=None):
                if widget_type == "test":
                    return ConcreteWidget(widget_id)
                else:
                    raise ValueError(f"未知Widget类型: {widget_type}")

        # 使用工厂创建Widget
        widget = WidgetFactory.create_widget("test", "factory_widget")
        assert isinstance(widget, ConcreteWidget)
        assert widget.widget_id == "factory_widget"

        # 测试未知类型
        with pytest.raises(ValueError):
            WidgetFactory.create_widget("unknown")

    def test_widget_serialization_concept(self):
        """测试Widget序列化概念"""
        widget = ConcreteWidget(widget_id="serializable_widget")

        # 获取Widget的基本信息
        widget_info = {
            "id": widget.widget_id,
            "type": widget.__class__.__name__,
            "template": widget._get_template_name(),
            "context": widget.get_template_context(),
        }

        assert widget_info["id"] == "serializable_widget"
        assert widget_info["type"] == "ConcreteWidget"
        assert widget_info["template"] == "test_widget.html"
        assert widget_info["context"] == {"test_data": "test_value"}

    def test_multiple_widgets_independence(self):
        """测试多个Widget的独立性"""
        widget1 = ConcreteWidget(widget_id="widget1")
        widget2 = ConcreteWidget(widget_id="widget2")

        # 验证每个Widget独立
        assert widget1.widget_id != widget2.widget_id
        assert widget1._template_engine is not None
        assert widget2._template_engine is not None

        # 修改一个Widget不应影响另一个
        widget1.set_widget_id("modified_widget")
        assert widget1.widget_id == "modified_widget"
        assert widget2.widget_id == "widget2"
