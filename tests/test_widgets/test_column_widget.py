"""列布局Widget测试模块"""

from unittest.mock import Mock

from email_widget.core.base import BaseWidget
from email_widget.widgets.column_widget import ColumnWidget


class MockWidget(BaseWidget):
    """测试用的Mock Widget"""

    def __init__(self, widget_id: str = None):
        super().__init__(widget_id)

    def _get_template_name(self) -> str:
        return "mock.html"

    def get_template_context(self) -> dict:
        return {"content": f"mock_{self.widget_id}"}


class TestColumnWidget:
    """ColumnWidget测试类"""

    def setup_method(self):
        """每个测试方法前的设置"""
        self.widget = ColumnWidget()

    def test_init(self):
        """测试初始化"""
        assert self.widget._widgets == []
        assert self.widget._columns == -1  # 自动模式
        assert self.widget._gap == "20px"

    def test_init_with_widget_id(self):
        """测试使用widget_id初始化"""
        widget = ColumnWidget("test_id")
        assert widget.widget_id == "test_id"

    def test_add_widget(self):
        """测试添加单个Widget"""
        mock_widget = MockWidget("widget1")
        result = self.widget.add_widget(mock_widget)

        assert result is self.widget  # 支持链式调用
        assert len(self.widget._widgets) == 1
        assert self.widget._widgets[0] is mock_widget

    def test_add_widgets(self):
        """测试添加多个Widget"""
        widgets = [MockWidget("widget1"), MockWidget("widget2"), MockWidget("widget3")]
        result = self.widget.add_widgets(widgets)

        assert result is self.widget
        assert len(self.widget._widgets) == 3
        assert self.widget._widgets == widgets

    def test_set_columns_auto_mode(self):
        """测试设置自动列数模式"""
        result = self.widget.set_columns(-1)

        assert result is self.widget
        assert self.widget._columns == -1

    def test_set_columns_manual_mode(self):
        """测试设置手动列数模式"""
        result = self.widget.set_columns(3)

        assert result is self.widget
        assert self.widget._columns == 3

    def test_set_columns_clamp_range(self):
        """测试列数被限制在1-4范围内"""
        # 测试小于1的值
        self.widget.set_columns(0)
        assert self.widget._columns == 1

        # 测试大于4的值
        self.widget.set_columns(6)
        assert self.widget._columns == 4

    def test_set_gap(self):
        """测试设置间隔"""
        result = self.widget.set_gap("30px")

        assert result is self.widget
        assert self.widget._gap == "30px"

    def test_clear_widgets(self):
        """测试清空Widget"""
        widgets = [MockWidget("widget1"), MockWidget("widget2")]
        self.widget.add_widgets(widgets)

        result = self.widget.clear_widgets()

        assert result is self.widget
        assert len(self.widget._widgets) == 0

    def test_remove_widget(self):
        """测试移除Widget"""
        widget1 = MockWidget("widget1")
        widget2 = MockWidget("widget2")
        widget3 = MockWidget("widget3")
        self.widget.add_widgets([widget1, widget2, widget3])

        result = self.widget.remove_widget("widget2")

        assert result is self.widget
        assert len(self.widget._widgets) == 2
        assert widget2 not in self.widget._widgets
        assert widget1 in self.widget._widgets
        assert widget3 in self.widget._widgets

    def test_remove_widget_by_index(self):
        """测试按索引移除Widget"""
        widgets = [MockWidget("widget1"), MockWidget("widget2"), MockWidget("widget3")]
        self.widget.add_widgets(widgets)

        result = self.widget.remove_widget_by_index(1)

        assert result is self.widget
        assert len(self.widget._widgets) == 2
        assert self.widget._widgets[0].widget_id == "widget1"
        assert self.widget._widgets[1].widget_id == "widget3"

    def test_remove_widget_by_index_invalid(self):
        """测试移除无效索引的Widget"""
        widgets = [MockWidget("widget1"), MockWidget("widget2")]
        self.widget.add_widgets(widgets)

        # 测试负索引
        self.widget.remove_widget_by_index(-1)
        assert len(self.widget._widgets) == 2

        # 测试超出范围的索引
        self.widget.remove_widget_by_index(5)
        assert len(self.widget._widgets) == 2

    def test_get_widget_count(self):
        """测试获取Widget数量"""
        assert self.widget.get_widget_count() == 0

        self.widget.add_widget(MockWidget("widget1"))
        assert self.widget.get_widget_count() == 1

        self.widget.add_widgets([MockWidget("widget2"), MockWidget("widget3")])
        assert self.widget.get_widget_count() == 3

    def test_is_auto_mode(self):
        """测试检查是否为自动模式"""
        assert self.widget.is_auto_mode() is True

        self.widget.set_columns(2)
        assert self.widget.is_auto_mode() is False

        self.widget.set_columns(-1)
        assert self.widget.is_auto_mode() is True

    def test_calculate_auto_columns(self):
        """测试自动列数计算"""
        test_cases = [
            (0, 1),  # 0个widget -> 1列
            (1, 1),  # 1个widget -> 1列
            (2, 2),  # 2个widget -> 2列
            (3, 3),  # 3个widget -> 3列
            (4, 2),  # 4个widget -> 2列
            (5, 3),  # 5个widget -> 3列
            (6, 3),  # 6个widget -> 3列
            (7, 2),  # 7个widget -> 2列
            (8, 2),  # 8个widget -> 2列
            (9, 3),  # 9个widget -> 3列
            (12, 3),  # 12个widget -> 3列
        ]

        for widget_count, expected_columns in test_cases:
            actual_columns = self.widget._calculate_auto_columns(widget_count)
            assert actual_columns == expected_columns, (
                f"Widget数量 {widget_count} 应该得到 {expected_columns} 列，实际得到 {actual_columns} 列"
            )

    def test_get_effective_columns_auto_mode(self):
        """测试自动模式下的有效列数"""
        # 测试自动模式
        self.widget.set_columns(-1)

        # 添加不同数量的widget测试
        widgets = [MockWidget(f"widget{i}") for i in range(5)]
        self.widget.add_widgets(widgets)

        effective_columns = self.widget.get_effective_columns()
        assert effective_columns == 3  # 5个widget应该是3列

    def test_get_effective_columns_manual_mode(self):
        """测试手动模式下的有效列数"""
        self.widget.set_columns(2)

        # 添加widget
        widgets = [MockWidget(f"widget{i}") for i in range(6)]
        self.widget.add_widgets(widgets)

        effective_columns = self.widget.get_effective_columns()
        assert effective_columns == 2  # 手动设置为2列

    def test_get_current_columns(self):
        """测试获取当前列数"""
        # 测试自动模式
        widgets = [MockWidget(f"widget{i}") for i in range(4)]
        self.widget.add_widgets(widgets)

        current_columns = self.widget.get_current_columns()
        assert current_columns == 2  # 4个widget应该是2列

        # 测试手动模式
        self.widget.set_columns(3)
        current_columns = self.widget.get_current_columns()
        assert current_columns == 3

    def test_set_equal_width(self):
        """测试设置等宽"""
        result = self.widget.set_equal_width(True)

        assert result is self.widget
        assert self.widget._equal_width is True

        # 测试默认值
        result = self.widget.set_equal_width()
        assert self.widget._equal_width is True

    def test_get_template_name(self):
        """测试获取模板名称"""
        assert self.widget._get_template_name() == "column.html"

    def test_get_template_context_empty(self):
        """测试空Widget列表的模板上下文"""
        context = self.widget.get_template_context()
        assert context == {}

    def test_get_template_context_with_widgets(self):
        """测试有Widget的模板上下文"""
        # 创建mock widget并设置渲染方法
        widgets = []
        for i in range(3):
            widget = MockWidget(f"widget{i}")
            # Mock render方法
            widget.render = Mock(return_value=f"<div>Widget {i}</div>")
            widgets.append(widget)

        self.widget.add_widgets(widgets)
        self.widget.set_columns(2)  # 设置为2列
        self.widget.set_gap("25px")

        context = self.widget.get_template_context()

        # 验证基本结构
        assert "widget_groups" in context
        assert "table_style" in context
        assert "cell_style" in context
        assert "empty_cell_style" in context
        assert "empty_columns" in context

        # 验证样式包含间隔
        assert "border-spacing: 25px 0" in context["table_style"]

        # 验证列宽计算
        assert "width: 50.00%" in context["cell_style"]  # 2列时每列50%

    def test_get_template_context_column_width_calculation(self):
        """测试列宽计算"""
        widgets = [MockWidget(f"widget{i}") for i in range(4)]
        for widget in widgets:
            widget.render = Mock(return_value=f"<div>{widget.widget_id}</div>")

        self.widget.add_widgets(widgets)

        # 测试不同列数的宽度计算
        test_cases = [
            (1, "100.00%"),
            (2, "50.00%"),
            (3, "33.33%"),
            (4, "25.00%"),
        ]

        for columns, expected_width in test_cases:
            self.widget.set_columns(columns)
            context = self.widget.get_template_context()
            assert expected_width in context["cell_style"]


class TestColumnWidgetIntegration:
    """ColumnWidget集成测试类"""

    def test_chaining_methods(self):
        """测试方法链式调用"""
        widgets = [MockWidget(f"widget{i}") for i in range(3)]

        widget = (
            ColumnWidget("test_id")
            .add_widgets(widgets)
            .set_columns(2)
            .set_gap("30px")
            .set_equal_width(True)
        )

        assert widget.widget_id == "test_id"
        assert len(widget._widgets) == 3
        assert widget._columns == 2
        assert widget._gap == "30px"
        assert widget._equal_width is True

    def test_full_workflow_auto_mode(self):
        """测试自动模式完整工作流程"""
        column_widget = ColumnWidget()

        # 逐步添加widget
        widgets = []
        for i in range(6):
            widget = MockWidget(f"widget{i}")
            widget.render = Mock(return_value=f"<div>Content {i}</div>")
            widgets.append(widget)
            column_widget.add_widget(widget)

        # 验证自动列数计算
        assert column_widget.is_auto_mode()
        assert column_widget.get_current_columns() == 3  # 6个widget应该是3列

        # 获取模板上下文
        context = column_widget.get_template_context()
        assert "widget_groups" in context

    def test_full_workflow_manual_mode(self):
        """测试手动模式完整工作流程"""
        column_widget = ColumnWidget()

        # 添加widget
        widgets = []
        for i in range(5):
            widget = MockWidget(f"widget{i}")
            widget.render = Mock(return_value=f"<div>Content {i}</div>")
            widgets.append(widget)

        column_widget.add_widgets(widgets)
        column_widget.set_columns(2)  # 手动设置2列

        # 验证设置
        assert not column_widget.is_auto_mode()
        assert column_widget.get_current_columns() == 2

        # 获取模板上下文
        context = column_widget.get_template_context()
        assert "widget_groups" in context

    def test_widget_management_operations(self):
        """测试Widget管理操作"""
        column_widget = ColumnWidget()

        # 添加多个widget
        widgets = [MockWidget(f"widget{i}") for i in range(5)]
        column_widget.add_widgets(widgets)
        assert column_widget.get_widget_count() == 5

        # 移除widget
        column_widget.remove_widget("widget2")
        assert column_widget.get_widget_count() == 4

        # 按索引移除
        column_widget.remove_widget_by_index(0)
        assert column_widget.get_widget_count() == 3

        # 清空所有widget
        column_widget.clear_widgets()
        assert column_widget.get_widget_count() == 0

    def test_mode_switching(self):
        """测试模式切换"""
        column_widget = ColumnWidget()
        widgets = [MockWidget(f"widget{i}") for i in range(4)]
        column_widget.add_widgets(widgets)

        # 开始是自动模式
        assert column_widget.is_auto_mode()
        assert column_widget.get_current_columns() == 2  # 4个widget -> 2列

        # 切换到手动模式
        column_widget.set_columns(3)
        assert not column_widget.is_auto_mode()
        assert column_widget.get_current_columns() == 3

        # 切换回自动模式
        column_widget.set_columns(-1)
        assert column_widget.is_auto_mode()
        assert column_widget.get_current_columns() == 2
