"""状态信息Widget测试模块"""

from email_widget.core.enums import LayoutType, StatusType
from email_widget.widgets.status_widget import StatusItem, StatusWidget


class TestStatusItem:
    """StatusItem测试类"""

    def test_init_default(self):
        """测试默认初始化"""
        item = StatusItem("标签", "值")

        assert item.label == "标签"
        assert item.value == "值"
        assert item.status is None

    def test_init_with_status(self):
        """测试带状态的初始化"""
        item = StatusItem("状态", "成功", StatusType.SUCCESS)

        assert item.label == "状态"
        assert item.value == "成功"
        assert item.status == StatusType.SUCCESS


class TestStatusWidget:
    """StatusWidget测试类"""

    def setup_method(self):
        """每个测试方法前的设置"""
        self.widget = StatusWidget()

    def test_init(self):
        """测试初始化"""
        assert self.widget._items == []
        assert self.widget._title is None
        assert self.widget._layout == LayoutType.VERTICAL

    def test_init_with_widget_id(self):
        """测试使用widget_id初始化"""
        widget = StatusWidget("test_id")
        assert widget.widget_id == "test_id"

    def test_add_status_item_without_status(self):
        """测试添加无状态的状态项"""
        result = self.widget.add_status_item("CPU使用率", "15%")

        assert result is self.widget  # 支持链式调用
        assert len(self.widget._items) == 1

        item = self.widget._items[0]
        assert item.label == "CPU使用率"
        assert item.value == "15%"
        assert item.status is None

    def test_add_status_item_with_status(self):
        """测试添加带状态的状态项"""
        result = self.widget.add_status_item("系统状态", "正常", StatusType.SUCCESS)

        assert result is self.widget
        assert len(self.widget._items) == 1

        item = self.widget._items[0]
        assert item.label == "系统状态"
        assert item.value == "正常"
        assert item.status == StatusType.SUCCESS

    def test_set_title(self):
        """测试设置标题"""
        result = self.widget.set_title("系统监控")

        assert result is self.widget
        assert self.widget._title == "系统监控"

    def test_set_layout_vertical(self):
        """测试设置垂直布局"""
        result = self.widget.set_layout(LayoutType.VERTICAL)

        assert result is self.widget
        assert self.widget._layout == LayoutType.VERTICAL

    def test_set_layout_horizontal(self):
        """测试设置水平布局"""
        result = self.widget.set_layout(LayoutType.HORIZONTAL)

        assert result is self.widget
        assert self.widget._layout == LayoutType.HORIZONTAL

    def test_clear_items(self):
        """测试清空状态项"""
        # 先添加一些项目
        self.widget.add_status_item("项目1", "值1")
        self.widget.add_status_item("项目2", "值2")

        result = self.widget.clear_items()

        assert result is self.widget
        assert len(self.widget._items) == 0

    def test_remove_item(self):
        """测试移除指定标签的状态项"""
        self.widget.add_status_item("项目1", "值1")
        self.widget.add_status_item("项目2", "值2")
        self.widget.add_status_item("项目3", "值3")

        result = self.widget.remove_item("项目2")

        assert result is self.widget
        assert len(self.widget._items) == 2

        # 验证正确的项目被移除
        labels = [item.label for item in self.widget._items]
        assert "项目1" in labels
        assert "项目3" in labels
        assert "项目2" not in labels

    def test_remove_item_not_found(self):
        """测试移除不存在的状态项"""
        self.widget.add_status_item("项目1", "值1")

        result = self.widget.remove_item("不存在的项目")

        assert result is self.widget
        assert len(self.widget._items) == 1  # 没有变化

    def test_update_item_existing(self):
        """测试更新现有状态项"""
        self.widget.add_status_item("CPU", "15%", StatusType.INFO)

        result = self.widget.update_item("CPU", "85%", StatusType.WARNING)

        assert result is self.widget
        assert len(self.widget._items) == 1

        item = self.widget._items[0]
        assert item.label == "CPU"
        assert item.value == "85%"
        assert item.status == StatusType.WARNING

    def test_update_item_without_status(self):
        """测试更新状态项但不改变状态"""
        self.widget.add_status_item("内存", "50%", StatusType.SUCCESS)

        result = self.widget.update_item("内存", "60%")

        assert result is self.widget

        item = self.widget._items[0]
        assert item.value == "60%"
        assert item.status == StatusType.SUCCESS  # 状态未改变

    def test_update_item_not_found(self):
        """测试更新不存在的状态项"""
        self.widget.add_status_item("项目1", "值1")

        result = self.widget.update_item("不存在的项目", "新值")

        assert result is self.widget
        assert len(self.widget._items) == 1  # 没有新增项目

    def test_get_item_count(self):
        """测试获取状态项数量"""
        assert self.widget.get_item_count() == 0

        self.widget.add_status_item("项目1", "值1")
        assert self.widget.get_item_count() == 1

        self.widget.add_status_item("项目2", "值2")
        self.widget.add_status_item("项目3", "值3")
        assert self.widget.get_item_count() == 3

    def test_get_status_color(self):
        """测试获取状态颜色"""
        test_cases = [
            (StatusType.SUCCESS, "#107c10"),
            (StatusType.WARNING, "#ff8c00"),
            (StatusType.ERROR, "#d13438"),
            (StatusType.INFO, "#0078d4"),
            (StatusType.PRIMARY, "#0078d4"),
        ]

        for status_type, expected_color in test_cases:
            color = self.widget._get_status_color(status_type)
            assert color == expected_color

    def test_get_template_name(self):
        """测试获取模板名称"""
        assert self.widget._get_template_name() == "status_info.html"

    def test_get_template_context_empty(self):
        """测试空状态的模板上下文"""
        context = self.widget.get_template_context()
        assert context == {}

    def test_get_template_context_with_items(self):
        """测试有状态项的模板上下文"""
        self.widget.set_title("系统状态")
        self.widget.add_status_item("CPU", "25%", StatusType.SUCCESS)
        self.widget.add_status_item("内存", "60%", StatusType.WARNING)

        context = self.widget.get_template_context()

        # 验证基本数据
        assert context["title"] == "系统状态"
        assert context["layout"] == "vertical"  # 默认垂直布局

        # 验证状态项
        assert "items" in context
        assert len(context["items"]) == 2

        # 验证样式
        assert "container_style" in context
        assert "title_style" in context

    def test_get_template_context_horizontal_layout(self):
        """测试水平布局的模板上下文"""
        self.widget.set_layout(LayoutType.HORIZONTAL)
        self.widget.add_status_item("状态", "正常")

        context = self.widget.get_template_context()

        assert context["layout"] == "horizontal"

    def test_get_template_context_item_styles(self):
        """测试状态项样式"""
        self.widget.add_status_item("错误数", "5", StatusType.ERROR)
        self.widget.add_status_item("正常项", "OK")

        context = self.widget.get_template_context()

        items = context["items"]

        # 第一个项目有错误状态
        error_item = items[0]
        assert error_item["label"] == "错误数"
        assert error_item["value"] == "5"
        assert "#d13438" in error_item["value_style"]  # 错误颜色
        assert "font-weight: 600" in error_item["value_style"]

        # 第二个项目没有状态
        normal_item = items[1]
        assert normal_item["label"] == "正常项"
        assert normal_item["value"] == "OK"
        assert "#d13438" not in normal_item["value_style"]  # 无错误颜色


class TestStatusWidgetIntegration:
    """StatusWidget集成测试类"""

    def test_chaining_methods(self):
        """测试方法链式调用"""
        widget = (
            StatusWidget("test_id")
            .set_title("服务器监控")
            .set_layout(LayoutType.HORIZONTAL)
            .add_status_item("CPU", "25%", StatusType.SUCCESS)
            .add_status_item("内存", "70%", StatusType.WARNING)
            .add_status_item("磁盘", "90%", StatusType.ERROR)
        )

        assert widget.widget_id == "test_id"
        assert widget._title == "服务器监控"
        assert widget._layout == LayoutType.HORIZONTAL
        assert widget.get_item_count() == 3

    def test_full_workflow(self):
        """测试完整工作流程"""
        widget = StatusWidget()

        # 配置状态监控
        widget.set_title("应用程序状态")
        widget.set_layout(LayoutType.VERTICAL)

        # 添加各种状态项
        widget.add_status_item("数据库连接", "正常", StatusType.SUCCESS)
        widget.add_status_item("Redis缓存", "连接超时", StatusType.ERROR)
        widget.add_status_item("API响应时间", "150ms", StatusType.WARNING)
        widget.add_status_item("活跃用户", "1,234")

        # 获取模板上下文
        context = widget.get_template_context()

        # 验证完整配置
        assert context["title"] == "应用程序状态"
        assert context["layout"] == "vertical"
        assert len(context["items"]) == 4

        # 验证各种状态项的样式
        items = context["items"]
        db_item = next(item for item in items if item["label"] == "数据库连接")
        assert "#107c10" in db_item["value_style"]  # SUCCESS颜色

        redis_item = next(item for item in items if item["label"] == "Redis缓存")
        assert "#d13438" in redis_item["value_style"]  # ERROR颜色

    def test_item_management_operations(self):
        """测试状态项管理操作"""
        widget = StatusWidget()

        # 添加多个状态项
        widget.add_status_item("CPU", "10%", StatusType.SUCCESS)
        widget.add_status_item("内存", "50%", StatusType.INFO)
        widget.add_status_item("磁盘", "80%", StatusType.WARNING)
        assert widget.get_item_count() == 3

        # 更新状态项
        widget.update_item("CPU", "85%", StatusType.ERROR)
        context = widget.get_template_context()
        cpu_item = next(item for item in context["items"] if item["label"] == "CPU")
        assert cpu_item["value"] == "85%"
        assert "#d13438" in cpu_item["value_style"]  # ERROR颜色

        # 移除状态项
        widget.remove_item("内存")
        assert widget.get_item_count() == 2

        # 清空所有状态项
        widget.clear_items()
        assert widget.get_item_count() == 0

    def test_layout_comparison(self):
        """测试不同布局的比较"""
        widget = StatusWidget()
        widget.add_status_item("测试项", "测试值")

        # 测试垂直布局
        widget.set_layout(LayoutType.VERTICAL)
        v_context = widget.get_template_context()
        assert v_context["layout"] == "vertical"

        # 测试水平布局
        widget.set_layout(LayoutType.HORIZONTAL)
        h_context = widget.get_template_context()
        assert h_context["layout"] == "horizontal"

    def test_status_color_effects(self):
        """测试状态颜色效果"""
        widget = StatusWidget()

        # 添加不同状态的项目
        status_tests = [
            ("成功项", "OK", StatusType.SUCCESS, "#107c10"),
            ("警告项", "注意", StatusType.WARNING, "#ff8c00"),
            ("错误项", "失败", StatusType.ERROR, "#d13438"),
            ("信息项", "提示", StatusType.INFO, "#0078d4"),
            ("普通项", "正常", None, None),
        ]

        for label, value, status, expected_color in status_tests:
            widget.clear_items()
            widget.add_status_item(label, value, status)

            context = widget.get_template_context()
            item = context["items"][0]

            if expected_color:
                assert expected_color in item["value_style"]
                assert "font-weight: 600" in item["value_style"]
            else:
                # 普通项不应该有状态颜色
                assert "#107c10" not in item["value_style"]
                assert "#ff8c00" not in item["value_style"]
                assert "#d13438" not in item["value_style"]
                assert "#0078d4" not in item["value_style"]
