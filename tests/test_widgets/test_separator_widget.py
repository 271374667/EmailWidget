"""分隔符Widget测试模块"""

from email_widget.core.enums import SeparatorType, StatusType
from email_widget.widgets.separator_widget import SeparatorWidget


class TestSeparatorWidget:
    """SeparatorWidget测试类"""

    def setup_method(self):
        """每个测试方法前的设置"""
        self.widget = SeparatorWidget()

    def test_init(self):
        """测试初始化"""
        assert self.widget._separator_type == SeparatorType.SOLID
        assert self.widget._color == "#e1dfdd"
        assert self.widget._thickness == "1px"
        assert self.widget._width == "100%"
        assert self.widget._margin == "16px"

    def test_init_with_widget_id(self):
        """测试使用widget_id初始化"""
        widget = SeparatorWidget("test_id")
        assert widget.widget_id == "test_id"

    def test_set_type(self):
        """测试设置分隔符类型"""
        result = self.widget.set_type(SeparatorType.DASHED)

        assert result is self.widget  # 支持链式调用
        assert self.widget._separator_type == SeparatorType.DASHED

        # 测试所有类型
        self.widget.set_type(SeparatorType.SOLID)
        assert self.widget._separator_type == SeparatorType.SOLID

        self.widget.set_type(SeparatorType.DOTTED)
        assert self.widget._separator_type == SeparatorType.DOTTED

    def test_set_color(self):
        """测试设置分隔符颜色"""
        result = self.widget.set_color("#0078d4")

        assert result is self.widget
        assert self.widget._color == "#0078d4"

        # 测试不同颜色格式
        self.widget.set_color("blue")
        assert self.widget._color == "blue"

        self.widget.set_color("rgb(255, 0, 0)")
        assert self.widget._color == "rgb(255, 0, 0)"

    def test_set_thickness(self):
        """测试设置分隔符粗细"""
        result = self.widget.set_thickness("2px")

        assert result is self.widget
        assert self.widget._thickness == "2px"

        # 测试不同粗细
        self.widget.set_thickness("3px")
        assert self.widget._thickness == "3px"

    def test_set_width(self):
        """测试设置分隔符宽度"""
        result = self.widget.set_width("80%")

        assert result is self.widget
        assert self.widget._width == "80%"

        # 测试像素宽度
        self.widget.set_width("300px")
        assert self.widget._width == "300px"

    def test_set_margin(self):
        """测试设置分隔符边距"""
        result = self.widget.set_margin("20px")

        assert result is self.widget
        assert self.widget._margin == "20px"

        # 测试em单位
        self.widget.set_margin("1em")
        assert self.widget._margin == "1em"

    def test_set_theme_color(self):
        """测试设置主题颜色"""
        result = self.widget.set_theme_color(StatusType.SUCCESS)

        assert result is self.widget
        assert self.widget._color == "#107c10"

        # 测试所有主题颜色
        self.widget.set_theme_color(StatusType.WARNING)
        assert self.widget._color == "#ff8c00"

        self.widget.set_theme_color(StatusType.ERROR)
        assert self.widget._color == "#d13438"

        self.widget.set_theme_color(StatusType.INFO)
        assert self.widget._color == "#0078d4"

        self.widget.set_theme_color(StatusType.PRIMARY)
        assert self.widget._color == "#0078d4"

    def test_set_style(self):
        """测试一次性设置多个样式"""
        result = self.widget.set_style(
            separator_type=SeparatorType.DASHED,
            color="#ff8c00",
            thickness="3px",
            width="50%",
            margin="25px",
        )

        assert result is self.widget
        assert self.widget._separator_type == SeparatorType.DASHED
        assert self.widget._color == "#ff8c00"
        assert self.widget._thickness == "3px"
        assert self.widget._width == "50%"
        assert self.widget._margin == "25px"

    def test_set_style_partial(self):
        """测试部分设置样式"""
        # 只设置部分属性
        self.widget.set_style(color="#123456", thickness="5px")

        assert self.widget._separator_type == SeparatorType.SOLID  # 保持原值
        assert self.widget._color == "#123456"  # 新值
        assert self.widget._thickness == "5px"  # 新值
        assert self.widget._width == "100%"  # 保持原值
        assert self.widget._margin == "16px"  # 保持原值

    def test_reset_to_default(self):
        """测试重置为默认值"""
        # 先修改所有值
        self.widget.set_style(
            separator_type=SeparatorType.DOTTED,
            color="#ff0000",
            thickness="5px",
            width="30%",
            margin="50px",
        )

        # 重置
        result = self.widget.reset_to_default()

        assert result is self.widget
        assert self.widget._separator_type == SeparatorType.SOLID
        assert self.widget._color == "#e1dfdd"
        assert self.widget._thickness == "1px"
        assert self.widget._width == "100%"
        assert self.widget._margin == "16px"

    def test_get_border_style(self):
        """测试获取边框样式"""
        # 测试实线
        self.widget.set_type(SeparatorType.SOLID)
        assert self.widget._get_border_style() == "solid"

        # 测试虚线
        self.widget.set_type(SeparatorType.DASHED)
        assert self.widget._get_border_style() == "dashed"

        # 测试点线
        self.widget.set_type(SeparatorType.DOTTED)
        assert self.widget._get_border_style() == "dotted"

    def test_properties(self):
        """测试只读属性"""
        self.widget.set_style(
            separator_type=SeparatorType.DASHED,
            color="#123456",
            thickness="2px",
            width="75%",
            margin="10px",
        )

        assert self.widget.separator_type == SeparatorType.DASHED
        assert self.widget.color == "#123456"
        assert self.widget.thickness == "2px"
        assert self.widget.width == "75%"
        assert self.widget.margin == "10px"

    def test_get_template_name(self):
        """测试获取模板名称"""
        assert self.widget._get_template_name() == "separator.html"

    def test_get_template_context(self):
        """测试获取模板上下文"""
        context = self.widget.get_template_context()

        assert context["show_separator"] is True
        assert "container_style" in context
        assert "separator_style" in context

        # 验证样式内容
        container_style = context["container_style"]
        assert "text-align: center" in container_style
        assert "margin: 16px 0" in container_style

        separator_style = context["separator_style"]
        assert "width: 100%" in separator_style
        assert "border-top: 1px solid #e1dfdd" in separator_style

    def test_get_template_context_custom_style(self):
        """测试自定义样式的模板上下文"""
        self.widget.set_style(
            separator_type=SeparatorType.DASHED,
            color="#ff0000",
            thickness="3px",
            width="50%",
            margin="20px",
        )

        context = self.widget.get_template_context()

        container_style = context["container_style"]
        assert "margin: 20px 0" in container_style

        separator_style = context["separator_style"]
        assert "width: 50%" in separator_style
        assert "border-top: 3px dashed #ff0000" in separator_style

    def test_chain_calls(self):
        """测试链式调用"""
        result = (
            self.widget.set_type(SeparatorType.DOTTED)
            .set_color("#0078d4")
            .set_thickness("2px")
            .set_width("80%")
            .set_margin("25px")
        )

        assert result is self.widget
        assert self.widget._separator_type == SeparatorType.DOTTED
        assert self.widget._color == "#0078d4"
        assert self.widget._thickness == "2px"
        assert self.widget._width == "80%"
        assert self.widget._margin == "25px"

    def test_render_html_integration(self):
        """测试HTML渲染集成"""
        self.widget.set_style(
            separator_type=SeparatorType.SOLID, color="#0078d4", thickness="2px"
        )

        html = self.widget.render_html()

        # 基本检查HTML结构
        assert html is not None
        assert len(html.strip()) > 0

        # 检查是否包含预期的样式
        assert "border-top: 2px solid #0078d4" in html
        assert "text-align: center" in html
