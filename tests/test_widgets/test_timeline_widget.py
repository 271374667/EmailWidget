"""TimelineWidget测试模块"""

from datetime import datetime

import pytest

from email_widget.core.enums import StatusType
from email_widget.widgets.timeline_widget import TimelineWidget


class TestTimelineWidget:
    """TimelineWidget测试类"""

    def test_init(self):
        """测试初始化"""
        widget = TimelineWidget()
        assert widget.event_count == 0
        assert widget.title == ""
        assert not widget._show_time
        assert not widget._reverse_order

    def test_add_event_basic(self):
        """测试添加基本事件"""
        widget = TimelineWidget()

        # 添加基本事件
        widget.add_event("项目启动", "2024-01-01", "项目正式开始")
        assert widget.event_count == 1

        # 添加更多事件
        widget.add_event("需求确认", "2024-01-15")
        widget.add_event("开发完成")  # 无时间和描述
        assert widget.event_count == 3

    def test_add_event_with_datetime(self):
        """测试使用datetime对象添加事件"""
        widget = TimelineWidget()
        dt = datetime(2024, 1, 1, 12, 30, 0)

        widget.add_event("重要事件", dt, "使用datetime对象")

        events = widget.events
        assert len(events) == 1
        assert events[0]["title"] == "重要事件"
        assert events[0]["time_display"] == "2024-01-01 12:30"

    def test_add_event_with_status_types(self):
        """测试添加带状态类型的事件"""
        widget = TimelineWidget()

        # 使用StatusType枚举
        widget.add_event("成功事件", status_type=StatusType.SUCCESS)
        widget.add_event("警告事件", status_type=StatusType.WARNING)
        widget.add_event("错误事件", status_type=StatusType.ERROR)

        # 使用字符串
        widget.add_event("信息事件", status_type="info")
        widget.add_event("主要事件", status_type="primary")

        assert widget.event_count == 5
        events = widget.events

        # 验证状态颜色映射
        assert events[0]["status_color"] == "#107c10"  # success
        assert events[1]["status_color"] == "#ff8c00"  # warning
        assert events[2]["status_color"] == "#d13438"  # error
        assert events[3]["status_color"] == "#0078d4"  # info
        assert events[4]["status_color"] == "#0078d4"  # primary

    def test_add_event_invalid_status_type(self):
        """测试添加无效状态类型的事件"""
        widget = TimelineWidget()

        # 无效状态类型应该使用默认状态
        widget.add_event("测试事件", status_type="invalid_status")

        events = widget.events
        assert len(events) == 1
        # 应该使用默认状态
        assert events[0]["status_color"] == "#8e8e93"

    def test_event_sorting(self):
        """测试事件排序"""
        widget = TimelineWidget()

        # 按非时间顺序添加事件
        widget.add_event("第三个", "2024-01-30")
        widget.add_event("第一个", "2024-01-01")
        widget.add_event("第二个", "2024-01-15")

        events = widget.events
        assert events[0]["title"] == "第一个"
        assert events[1]["title"] == "第二个"
        assert events[2]["title"] == "第三个"

    def test_reverse_order_sorting(self):
        """测试倒序排列"""
        widget = TimelineWidget()
        widget.set_reverse_order(True)

        # 添加事件
        widget.add_event("第一个", "2024-01-01")
        widget.add_event("第二个", "2024-01-15")
        widget.add_event("第三个", "2024-01-30")

        events = widget.events
        assert events[0]["title"] == "第三个"  # 最新的在前
        assert events[1]["title"] == "第二个"
        assert events[2]["title"] == "第一个"

    def test_set_title(self):
        """测试设置标题"""
        widget = TimelineWidget()

        result = widget.set_title("项目时间线")
        assert result is widget  # 测试链式调用
        assert widget.title == "项目时间线"

    def test_show_timestamps(self):
        """测试设置时间戳显示"""
        widget = TimelineWidget()

        result = widget.show_timestamps(True)
        assert result is widget  # 测试链式调用
        assert widget._show_time is True

        widget.show_timestamps(False)
        assert widget._show_time is False

    def test_set_reverse_order(self):
        """测试设置倒序排列"""
        widget = TimelineWidget()

        result = widget.set_reverse_order(True)
        assert result is widget  # 测试链式调用
        assert widget._reverse_order is True

        widget.set_reverse_order(False)
        assert widget._reverse_order is False

    def test_clear_events(self):
        """测试清空事件"""
        widget = TimelineWidget()
        widget.add_event("事件1")
        widget.add_event("事件2")

        assert widget.event_count == 2

        result = widget.clear_events()
        assert result is widget  # 测试链式调用
        assert widget.event_count == 0

    def test_remove_event(self):
        """测试移除事件"""
        widget = TimelineWidget()
        widget.add_event("事件1", "2024-01-01")
        widget.add_event("事件2", "2024-01-02")
        widget.add_event("事件3", "2024-01-03")

        assert widget.event_count == 3

        # 移除中间事件
        result = widget.remove_event(1)
        assert result is widget  # 测试链式调用
        assert widget.event_count == 2

        events = widget.events
        assert events[0]["title"] == "事件1"
        assert events[1]["title"] == "事件3"

    def test_remove_event_invalid_index(self):
        """测试移除无效索引事件"""
        widget = TimelineWidget()
        widget.add_event("事件1")

        # 测试超出范围的索引
        with pytest.raises(IndexError):
            widget.remove_event(5)

        # 测试负数索引
        with pytest.raises(IndexError):
            widget.remove_event(-1)

    def test_chain_calls(self):
        """测试链式调用"""
        widget = (
            TimelineWidget()
            .set_title("测试时间线")
            .add_event("事件1", "2024-01-01")
            .add_event("事件2", "2024-01-02")
            .show_timestamps(True)
            .set_reverse_order(True)
        )

        assert widget.title == "测试时间线"
        assert widget.event_count == 2
        assert widget._show_time is True
        assert widget._reverse_order is True

    def test_properties(self):
        """测试属性访问"""
        widget = TimelineWidget()
        widget.add_event("事件1", "2024-01-01", "描述1")
        widget.add_event("事件2", "2024-01-02", "描述2")

        assert widget.event_count == 2
        assert widget.title == ""

        # 测试events属性返回副本
        events = widget.events
        events.clear()  # 修改副本
        assert widget.event_count == 2  # 原数据不受影响

    def test_get_template_context(self):
        """测试获取模板上下文"""
        widget = TimelineWidget()
        widget.set_title("测试时间线")
        widget.show_timestamps(True)
        widget.set_reverse_order(True)
        widget.add_event("完成事件", "2024-01-01", "已完成的任务", "success")
        widget.add_event("进行中事件", "2024-01-02", "正在处理", "primary")

        context = widget.get_template_context()

        assert context["title"] == "测试时间线"
        assert context["show_time"] is True
        assert context["reverse_order"] is True
        assert len(context["events"]) == 2

        # 验证事件排序（倒序）
        events = context["events"]
        assert events[0]["title"] == "进行中事件"  # 最新的在前
        assert events[1]["title"] == "完成事件"

    def test_render_html(self):
        """测试HTML渲染"""
        widget = TimelineWidget()
        widget.set_title("测试时间线")
        widget.add_event("事件1", "2024-01-01", "第一个事件", "success")
        widget.add_event("事件2", "2024-01-02", "第二个事件", "warning")

        html = widget.render_html()

        assert isinstance(html, str)
        assert len(html) > 0
        assert "测试时间线" in html
        assert "事件1" in html
        assert "事件2" in html
        assert "第一个事件" in html

    def test_render_html_empty(self):
        """测试空时间线HTML渲染"""
        widget = TimelineWidget()

        html = widget.render_html()

        assert isinstance(html, str)
        assert len(html) > 0
        # 应该能正常渲染，即使没有事件

    def test_render_html_with_timestamps(self):
        """测试带时间戳的HTML渲染"""
        widget = TimelineWidget()
        widget.set_title("时间戳测试")
        widget.show_timestamps(True)
        widget.add_event("事件1", "2024-01-01 10:30")
        widget.add_event("事件2", "2024-01-02 15:45")

        html = widget.render_html()

        assert "时间戳测试" in html
        assert "2024-01-01 10:30" in html
        assert "2024-01-02 15:45" in html

    def test_time_parsing(self):
        """测试时间解析"""
        widget = TimelineWidget()

        # 测试不同时间格式
        widget.add_event("日期", "2024-01-01")
        widget.add_event("日期时间", "2024-01-02 15:30:00")
        widget.add_event("自定义格式", "Jan 1, 2024")  # 不标准格式，应该使用默认时间

        events = widget.events
        assert len(events) == 3

        # 验证时间显示
        assert events[0]["time_display"] == "2024-01-01"
        assert events[1]["time_display"] == "2024-01-02 15:30:00"
        assert events[2]["time_display"] == "Jan 1, 2024"

    def test_type_validation(self):
        """测试类型验证"""
        widget = TimelineWidget()

        # 测试title参数验证
        with pytest.raises(TypeError):
            widget.add_event(123)

        # 测试set_title参数验证
        with pytest.raises(TypeError):
            widget.set_title(123)

        # 测试show_timestamps参数验证
        with pytest.raises(TypeError):
            widget.show_timestamps("true")

        # 测试set_reverse_order参数验证
        with pytest.raises(TypeError):
            widget.set_reverse_order("false")

    def test_widget_id_and_template_name(self):
        """测试widget ID和模板名称"""
        widget = TimelineWidget()

        assert widget.widget_id.startswith("timelinewidget_")
        assert len(widget.widget_id.split("_")[1]) == 8  # 8位十六进制
        assert widget._get_template_name() == "timeline_widget.html"
