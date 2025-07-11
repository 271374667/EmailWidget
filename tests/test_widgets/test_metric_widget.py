"""MetricWidget测试模块"""

import pytest

from email_widget.core.enums import StatusType
from email_widget.widgets.metric_widget import MetricWidget


class TestMetricWidget:
    """MetricWidget测试类"""

    def test_init(self):
        """测试初始化"""
        widget = MetricWidget()
        assert widget.metric_count == 0
        assert widget.title == ""
        assert widget.layout == "horizontal"
        assert widget._show_trend is True

    def test_add_metric_basic(self):
        """测试添加基本指标"""
        widget = MetricWidget()

        # 添加基本指标
        widget.add_metric("用户数", 12345, "人")
        assert widget.metric_count == 1

        # 添加更多指标
        widget.add_metric("增长率", "15.6", "%")
        widget.add_metric("收入", "¥1,250,000")  # 无单位
        assert widget.metric_count == 3

    def test_add_metric_with_trend(self):
        """测试添加带趋势的指标"""
        widget = MetricWidget()

        # 添加带趋势的指标
        widget.add_metric("销售额", "1250000", "元", "+12.3%", "success")
        widget.add_metric("订单量", "2456", "单", "-3.2%", "error")
        widget.add_metric("转化率", "3.2", "%", "+0.8%")  # 自动判断为success

        assert widget.metric_count == 3
        metrics = widget.metrics

        # 验证趋势颜色映射
        assert metrics[0]["trend_color"] == "#107c10"  # success
        assert metrics[1]["trend_color"] == "#d13438"  # error
        assert metrics[2]["trend_color"] == "#107c10"  # 自动判断为success

    def test_add_metric_with_status_types(self):
        """测试添加带状态类型的指标"""
        widget = MetricWidget()

        # 使用StatusType枚举
        widget.add_metric("成功指标", "100", "%", "+5%", StatusType.SUCCESS)
        widget.add_metric("警告指标", "75", "%", "+2%", StatusType.WARNING)
        widget.add_metric("错误指标", "25", "%", "-10%", StatusType.ERROR)

        # 使用字符串
        widget.add_metric("信息指标", "50", "%", "0%", "info")
        widget.add_metric("主要指标", "80", "%", "+3%", "primary")

        assert widget.metric_count == 5
        metrics = widget.metrics

        # 验证状态颜色映射
        assert metrics[0]["trend_color"] == "#107c10"  # success
        assert metrics[1]["trend_color"] == "#ff8c00"  # warning
        assert metrics[2]["trend_color"] == "#d13438"  # error
        assert metrics[3]["trend_color"] == "#0078d4"  # info
        assert metrics[4]["trend_color"] == "#0078d4"  # primary

    def test_add_metric_number_formatting(self):
        """测试数字格式化"""
        widget = MetricWidget()

        # 测试大数字格式化
        widget.add_metric("大数字", 1234567, "人")  # 应该显示为1M
        widget.add_metric("中等数字", 5432, "人")  # 应该显示为5K
        widget.add_metric("小数字", 123, "人")  # 应该显示为123
        widget.add_metric("小数", 1234.56, "元")  # 应该显示为1.2K

        metrics = widget.metrics
        assert metrics[0]["value"] == "1M"
        assert metrics[1]["value"] == "5K"
        assert metrics[2]["value"] == "123"
        assert metrics[3]["value"] == "1.2K"

    def test_add_metric_with_description(self):
        """测试添加带描述的指标"""
        widget = MetricWidget()

        widget.add_metric("活跃用户", 8456, "人", "+15.6%", "success", "较上月增长显著")

        metrics = widget.metrics
        assert len(metrics) == 1
        assert metrics[0]["label"] == "活跃用户"
        assert metrics[0]["description"] == "较上月增长显著"

    def test_add_metric_invalid_trend_type(self):
        """测试添加无效趋势类型的指标"""
        widget = MetricWidget()

        # 无效趋势类型应该使用默认状态
        widget.add_metric("测试指标", "100", "%", "+5%", "invalid_trend")

        metrics = widget.metrics
        assert len(metrics) == 1
        # 应该使用默认的neutral状态
        assert metrics[0]["trend_color"] == "#8e8e93"

    def test_auto_trend_detection(self):
        """测试自动趋势判断"""
        widget = MetricWidget()

        # 测试自动趋势判断
        widget.add_metric("上升", "100", "%", "+5%")  # 应该是success
        widget.add_metric("下降", "95", "%", "-3%")  # 应该是error
        widget.add_metric("平稳", "100", "%", "0%")  # 应该是neutral
        widget.add_metric("无符号", "100", "%", "5%")  # 应该是neutral

        metrics = widget.metrics
        assert metrics[0]["trend_color"] == "#107c10"  # success
        assert metrics[1]["trend_color"] == "#d13438"  # error
        assert metrics[2]["trend_color"] == "#8e8e93"  # neutral
        assert metrics[3]["trend_color"] == "#8e8e93"  # neutral

    def test_set_title(self):
        """测试设置标题"""
        widget = MetricWidget()

        result = widget.set_title("核心指标")
        assert result is widget  # 测试链式调用
        assert widget.title == "核心指标"

    def test_set_layout(self):
        """测试设置布局"""
        widget = MetricWidget()

        result = widget.set_layout("vertical")
        assert result is widget  # 测试链式调用
        assert widget.layout == "vertical"

        widget.set_layout("horizontal")
        assert widget.layout == "horizontal"

    def test_set_layout_invalid(self):
        """测试设置无效布局"""
        widget = MetricWidget()

        with pytest.raises(ValueError):
            widget.set_layout("invalid_layout")

    def test_show_trends(self):
        """测试设置趋势显示"""
        widget = MetricWidget()

        result = widget.show_trends(False)
        assert result is widget  # 测试链式调用
        assert widget._show_trend is False

        widget.show_trends(True)
        assert widget._show_trend is True

    def test_clear_metrics(self):
        """测试清空指标"""
        widget = MetricWidget()
        widget.add_metric("指标1", "100", "%")
        widget.add_metric("指标2", "200", "%")

        assert widget.metric_count == 2

        result = widget.clear_metrics()
        assert result is widget  # 测试链式调用
        assert widget.metric_count == 0

    def test_remove_metric(self):
        """测试移除指标"""
        widget = MetricWidget()
        widget.add_metric("指标1", "100", "%")
        widget.add_metric("指标2", "200", "%")
        widget.add_metric("指标3", "300", "%")

        assert widget.metric_count == 3

        # 移除中间指标
        result = widget.remove_metric(1)
        assert result is widget  # 测试链式调用
        assert widget.metric_count == 2

        metrics = widget.metrics
        assert metrics[0]["label"] == "指标1"
        assert metrics[1]["label"] == "指标3"

    def test_remove_metric_invalid_index(self):
        """测试移除无效索引指标"""
        widget = MetricWidget()
        widget.add_metric("指标1", "100", "%")

        # 测试超出范围的索引
        with pytest.raises(IndexError):
            widget.remove_metric(5)

        # 测试负数索引
        with pytest.raises(IndexError):
            widget.remove_metric(-1)

    def test_chain_calls(self):
        """测试链式调用"""
        widget = (
            MetricWidget()
            .set_title("测试指标")
            .add_metric("指标1", "100", "%", "+5%", "success")
            .add_metric("指标2", "200", "%", "-3%", "error")
            .set_layout("vertical")
            .show_trends(True)
        )

        assert widget.title == "测试指标"
        assert widget.metric_count == 2
        assert widget.layout == "vertical"
        assert widget._show_trend is True

    def test_properties(self):
        """测试属性访问"""
        widget = MetricWidget()
        widget.add_metric("指标1", "100", "%", "+5%")
        widget.add_metric("指标2", "200", "%", "-3%")

        assert widget.metric_count == 2
        assert widget.title == ""
        assert widget.layout == "horizontal"

        # 测试metrics属性返回副本
        metrics = widget.metrics
        metrics.clear()  # 修改副本
        assert widget.metric_count == 2  # 原数据不受影响

    def test_get_template_context(self):
        """测试获取模板上下文"""
        widget = MetricWidget()
        widget.set_title("测试指标")
        widget.set_layout("vertical")
        widget.show_trends(True)
        widget.add_metric("成功指标", "100", "%", "+5%", "success", "表现良好")
        widget.add_metric("警告指标", "75", "%", "+2%", "warning", "需要关注")

        context = widget.get_template_context()

        assert context["title"] == "测试指标"
        assert context["layout"] == "vertical"
        assert context["show_trend"] is True
        assert len(context["metrics"]) == 2

        # 验证指标内容
        metrics = context["metrics"]
        assert metrics[0]["label"] == "成功指标"
        assert metrics[0]["trend"] == "+5%"
        assert metrics[1]["label"] == "警告指标"
        assert metrics[1]["description"] == "需要关注"

    def test_get_template_context_no_trends(self):
        """测试获取模板上下文（不显示趋势）"""
        widget = MetricWidget()
        widget.show_trends(False)
        widget.add_metric("指标1", "100", "%", "+5%", "success")

        context = widget.get_template_context()

        assert context["show_trend"] is False
        # 趋势应该被过滤掉
        assert context["metrics"][0]["trend"] == ""

    def test_render_html(self):
        """测试HTML渲染"""
        widget = MetricWidget()
        widget.set_title("测试指标")
        widget.add_metric("用户数", "12345", "人", "+15.6%", "success")
        widget.add_metric("收入", "¥1,250,000", "", "+12.3%", "success")

        html = widget.render_html()

        assert isinstance(html, str)
        assert len(html) > 0
        assert "测试指标" in html
        assert "用户数" in html
        assert "12345" in html
        assert "+15.6%" in html

    def test_render_html_empty(self):
        """测试空指标HTML渲染"""
        widget = MetricWidget()

        html = widget.render_html()

        assert isinstance(html, str)
        assert len(html) > 0
        # 应该能正常渲染，即使没有指标

    def test_render_html_vertical_layout(self):
        """测试垂直布局HTML渲染"""
        widget = MetricWidget()
        widget.set_title("垂直布局测试")
        widget.set_layout("vertical")
        widget.add_metric("指标1", "100", "%")
        widget.add_metric("指标2", "200", "%")

        html = widget.render_html()

        assert "垂直布局测试" in html
        assert "指标1" in html
        assert "指标2" in html

    def test_type_validation(self):
        """测试类型验证"""
        widget = MetricWidget()

        # 测试label参数验证
        with pytest.raises(TypeError):
            widget.add_metric(123, "100", "%")

        # 测试set_title参数验证
        with pytest.raises(TypeError):
            widget.set_title(123)

        # 测试set_layout参数验证
        with pytest.raises(TypeError):
            widget.set_layout(123)

        # 测试show_trends参数验证
        with pytest.raises(TypeError):
            widget.show_trends("true")

        # 测试remove_metric参数验证
        with pytest.raises(TypeError):
            widget.remove_metric("0")

    def test_widget_id_and_template_name(self):
        """测试widget ID和模板名称"""
        widget = MetricWidget()

        assert widget.widget_id.startswith("metricwidget_")
        assert len(widget.widget_id.split("_")[1]) == 8  # 8位十六进制
        assert widget._get_template_name() == "metric_widget.html"
