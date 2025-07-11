"""ChecklistWidget测试模块"""

import pytest

from email_widget.core.enums import StatusType
from email_widget.widgets.checklist_widget import ChecklistWidget


class TestChecklistWidget:
    """ChecklistWidget测试类"""

    def test_init(self):
        """测试初始化"""
        widget = ChecklistWidget()
        assert widget.item_count == 0
        assert widget.title == ""
        assert not widget._show_progress
        assert not widget._compact_mode
        assert widget.completed_count == 0
        assert widget.pending_count == 0
        assert widget.skipped_count == 0
        assert widget.completion_percentage == 0.0

    def test_add_item_basic(self):
        """测试添加基本项目"""
        widget = ChecklistWidget()

        # 添加已完成项目
        widget.add_item("完成设计", True)
        assert widget.item_count == 1
        assert widget.completed_count == 1
        assert widget.pending_count == 0

        # 添加未完成项目
        widget.add_item("代码审查", False)
        assert widget.item_count == 2
        assert widget.completed_count == 1
        assert widget.pending_count == 1

        # 添加跳过项目
        widget.add_item("性能测试", None)
        assert widget.item_count == 3
        assert widget.completed_count == 1
        assert widget.pending_count == 1
        assert widget.skipped_count == 1

    def test_add_item_with_status_type(self):
        """测试添加带状态类型的项目"""
        widget = ChecklistWidget()

        # 使用StatusType枚举
        widget.add_item("数据备份", True, StatusType.SUCCESS)
        widget.add_item("服务检查", False, StatusType.WARNING)
        widget.add_item("错误处理", False, StatusType.ERROR)

        # 使用字符串
        widget.add_item("信息收集", True, "info")
        widget.add_item("主要任务", False, "primary")

        assert widget.item_count == 5
        items = widget.items

        # 验证状态映射正确
        assert items[0]["status_color"] == "#107c10"  # success
        assert items[1]["status_color"] == "#ff8c00"  # warning
        assert items[2]["status_color"] == "#d13438"  # error
        assert items[3]["status_color"] == "#0078d4"  # info
        assert items[4]["status_color"] == "#0078d4"  # primary

    def test_add_item_with_description_and_status_text(self):
        """测试添加带描述和状态文本的项目"""
        widget = ChecklistWidget()

        widget.add_item("完成UI设计", True, "success", "所有页面设计已完成", "已验收")

        items = widget.items
        assert len(items) == 1
        assert items[0]["text"] == "完成UI设计"
        assert items[0]["description"] == "所有页面设计已完成"
        assert items[0]["status_text"] == "已验收"
        assert items[0]["is_completed"] is True

    def test_add_item_invalid_status_type(self):
        """测试添加无效状态类型的项目"""
        widget = ChecklistWidget()

        # 无效状态类型应该使用默认状态
        widget.add_item("测试项目", False, "invalid_status")

        items = widget.items
        assert len(items) == 1
        # 应该使用默认的pending状态
        assert items[0]["status_color"] == "#8e8e93"

    def test_set_title(self):
        """测试设置标题"""
        widget = ChecklistWidget()

        result = widget.set_title("项目检查清单")
        assert result is widget  # 测试链式调用
        assert widget.title == "项目检查清单"

    def test_show_progress_stats(self):
        """测试设置进度统计"""
        widget = ChecklistWidget()

        result = widget.show_progress_stats(True)
        assert result is widget  # 测试链式调用
        assert widget._show_progress is True

        widget.show_progress_stats(False)
        assert widget._show_progress is False

    def test_set_compact_mode(self):
        """测试设置紧凑模式"""
        widget = ChecklistWidget()

        result = widget.set_compact_mode(True)
        assert result is widget  # 测试链式调用
        assert widget._compact_mode is True

        widget.set_compact_mode(False)
        assert widget._compact_mode is False

    def test_clear_items(self):
        """测试清空项目"""
        widget = ChecklistWidget()
        widget.add_item("项目1", True)
        widget.add_item("项目2", False)

        assert widget.item_count == 2

        result = widget.clear_items()
        assert result is widget  # 测试链式调用
        assert widget.item_count == 0
        assert widget.completed_count == 0
        assert widget.pending_count == 0

    def test_remove_item(self):
        """测试移除项目"""
        widget = ChecklistWidget()
        widget.add_item("项目1", True)
        widget.add_item("项目2", False)
        widget.add_item("项目3", True)

        assert widget.item_count == 3

        # 移除中间项目
        result = widget.remove_item(1)
        assert result is widget  # 测试链式调用
        assert widget.item_count == 2

        items = widget.items
        assert items[0]["text"] == "项目1"
        assert items[1]["text"] == "项目3"

    def test_remove_item_invalid_index(self):
        """测试移除无效索引项目"""
        widget = ChecklistWidget()
        widget.add_item("项目1", True)

        # 测试超出范围的索引
        with pytest.raises(IndexError):
            widget.remove_item(5)

        # 测试负数索引
        with pytest.raises(IndexError):
            widget.remove_item(-1)

    def test_update_item_status(self):
        """测试更新项目状态"""
        widget = ChecklistWidget()
        widget.add_item("项目1", False, "pending", "描述1", "状态1")
        widget.add_item("项目2", True, "success")

        # 更新第一个项目状态
        result = widget.update_item_status(0, True, "success")
        assert result is widget  # 测试链式调用

        items = widget.items
        assert items[0]["is_completed"] is True
        assert items[0]["text"] == "项目1"  # 确保其他属性保持不变
        assert items[0]["description"] == "描述1"

    def test_update_item_status_invalid_index(self):
        """测试更新无效索引项目状态"""
        widget = ChecklistWidget()
        widget.add_item("项目1", False)

        # 无效索引应该不做任何操作
        result = widget.update_item_status(5, True)
        assert result is widget
        assert widget.item_count == 1

    def test_completion_percentage(self):
        """测试完成百分比计算"""
        widget = ChecklistWidget()

        # 空清单
        assert widget.completion_percentage == 0.0

        # 添加项目
        widget.add_item("项目1", True)  # 完成
        widget.add_item("项目2", False)  # 未完成
        widget.add_item("项目3", True)  # 完成
        widget.add_item("项目4", None)  # 跳过

        # 应该是2/3 = 66.7% (跳过的不计入)
        assert widget.completion_percentage == 66.7

        # 全部跳过的情况
        widget.clear_items()
        widget.add_item("跳过1", None)
        widget.add_item("跳过2", None)
        assert widget.completion_percentage == 100.0

    def test_chain_calls(self):
        """测试链式调用"""
        widget = (
            ChecklistWidget()
            .set_title("测试清单")
            .add_item("项目1", True)
            .add_item("项目2", False)
            .show_progress_stats(True)
            .set_compact_mode(True)
        )

        assert widget.title == "测试清单"
        assert widget.item_count == 2
        assert widget._show_progress is True
        assert widget._compact_mode is True

    def test_properties(self):
        """测试属性访问"""
        widget = ChecklistWidget()
        widget.add_item("完成1", True)
        widget.add_item("完成2", True)
        widget.add_item("未完成1", False)
        widget.add_item("跳过1", None)

        assert widget.item_count == 4
        assert widget.completed_count == 2
        assert widget.pending_count == 1
        assert widget.skipped_count == 1

        # 测试items属性返回副本
        items = widget.items
        items.clear()  # 修改副本
        assert widget.item_count == 4  # 原数据不受影响

    def test_get_template_context(self):
        """测试获取模板上下文"""
        widget = ChecklistWidget()
        widget.set_title("测试清单")
        widget.show_progress_stats(True)
        widget.set_compact_mode(True)
        widget.add_item("完成项目", True, "success")
        widget.add_item("进行中项目", False, "warning")
        widget.add_item("跳过项目", None, "info")

        context = widget.get_template_context()

        assert context["title"] == "测试清单"
        assert context["show_progress"] is True
        assert context["compact_mode"] is True
        assert len(context["items"]) == 3
        assert context["completed_count"] == 1
        assert context["total_count"] == 2  # 不包含跳过的项目
        assert context["progress_percentage"] == 50.0
        assert context["progress_color"] == "#ff8c00"  # 50%应该是橙色

    def test_progress_color_mapping(self):
        """测试进度条颜色映射"""
        widget = ChecklistWidget()

        # 90%以上 - 绿色
        for i in range(10):
            widget.add_item(f"项目{i}", i < 9)  # 9/10 = 90%

        context = widget.get_template_context()
        assert context["progress_color"] == "#107c10"  # 绿色

        # 重置测试70%以上 - 蓝色
        widget.clear_items()
        for i in range(10):
            widget.add_item(f"项目{i}", i < 8)  # 8/10 = 80%

        context = widget.get_template_context()
        assert context["progress_color"] == "#0078d4"  # 蓝色

        # 重置测试50%以上 - 橙色
        widget.clear_items()
        for i in range(10):
            widget.add_item(f"项目{i}", i < 6)  # 6/10 = 60%

        context = widget.get_template_context()
        assert context["progress_color"] == "#ff8c00"  # 橙色

        # 重置测试50%以下 - 灰色
        widget.clear_items()
        for i in range(10):
            widget.add_item(f"项目{i}", i < 3)  # 3/10 = 30%

        context = widget.get_template_context()
        assert context["progress_color"] == "#8e8e93"  # 灰色

    def test_render_html(self):
        """测试HTML渲染"""
        widget = ChecklistWidget()
        widget.set_title("测试清单")
        widget.add_item("已完成项目", True, "success", "这是描述")
        widget.add_item("未完成项目", False, "warning")

        html = widget.render_html()

        assert isinstance(html, str)
        assert len(html) > 0
        assert "测试清单" in html
        assert "已完成项目" in html
        assert "未完成项目" in html
        assert "这是描述" in html

    def test_render_html_empty(self):
        """测试空清单HTML渲染"""
        widget = ChecklistWidget()

        html = widget.render_html()

        assert isinstance(html, str)
        assert len(html) > 0
        # 应该能正常渲染，即使没有项目

    def test_render_html_with_progress(self):
        """测试带进度的HTML渲染"""
        widget = ChecklistWidget()
        widget.set_title("进度测试")
        widget.show_progress_stats(True)
        widget.add_item("项目1", True)
        widget.add_item("项目2", False)

        html = widget.render_html()

        assert "进度测试" in html
        assert "完成进度" in html
        assert "50.0%" in html

    def test_type_validation(self):
        """测试类型验证"""
        widget = ChecklistWidget()

        # 测试text参数验证
        with pytest.raises(TypeError):
            widget.add_item(123, True)

        # 测试title参数验证
        with pytest.raises(TypeError):
            widget.set_title(123)

        # 测试show参数验证
        with pytest.raises(TypeError):
            widget.show_progress_stats("true")

        # 测试compact参数验证
        with pytest.raises(TypeError):
            widget.set_compact_mode("false")

        # 测试index参数验证
        with pytest.raises(TypeError):
            widget.remove_item("0")

    def test_widget_id_and_template_name(self):
        """测试widget ID和模板名称"""
        widget = ChecklistWidget()

        assert widget.widget_id.startswith("checklistwidget_")
        assert len(widget.widget_id.split("_")[1]) == 8  # 8位十六进制
        assert widget._get_template_name() == "checklist_widget.html"
