"""引用Widget测试模块"""

from email_widget.core.enums import StatusType
from email_widget.widgets.quote_widget import QuoteWidget


class TestQuoteWidget:
    """QuoteWidget测试类"""

    def setup_method(self):
        """每个测试方法前的设置"""
        self.widget = QuoteWidget()

    def test_init(self):
        """测试初始化"""
        assert self.widget._content == ""
        assert self.widget._author is None
        assert self.widget._source is None
        assert self.widget._quote_type == StatusType.INFO

    def test_init_with_widget_id(self):
        """测试使用widget_id初始化"""
        widget = QuoteWidget("test_id")
        assert widget.widget_id == "test_id"

    def test_set_content(self):
        """测试设置内容"""
        result = self.widget.set_content("这是一个引用内容")

        assert result is self.widget  # 支持链式调用
        assert self.widget._content == "这是一个引用内容"

    def test_set_author(self):
        """测试设置作者"""
        result = self.widget.set_author("张三")

        assert result is self.widget
        assert self.widget._author == "张三"

    def test_set_source(self):
        """测试设置来源"""
        result = self.widget.set_source("《论语》")

        assert result is self.widget
        assert self.widget._source == "《论语》"

    def test_set_quote_type(self):
        """测试设置引用类型"""
        result = self.widget.set_quote_type(StatusType.WARNING)

        assert result is self.widget
        assert self.widget._quote_type == StatusType.WARNING

    def test_set_full_quote_with_all_params(self):
        """测试一次性设置完整引用信息"""
        result = self.widget.set_full_quote(
            content="知识就是力量", author="培根", source="《新工具》"
        )

        assert result is self.widget
        assert self.widget._content == "知识就是力量"
        assert self.widget._author == "培根"
        assert self.widget._source == "《新工具》"

    def test_set_full_quote_content_only(self):
        """测试只设置内容的完整引用"""
        result = self.widget.set_full_quote("只设置内容")

        assert result is self.widget
        assert self.widget._content == "只设置内容"
        assert self.widget._author is None
        assert self.widget._source is None

    def test_set_full_quote_with_author_only(self):
        """测试设置内容和作者"""
        result = self.widget.set_full_quote("内容", author="作者")

        assert result is self.widget
        assert self.widget._content == "内容"
        assert self.widget._author == "作者"
        assert self.widget._source is None

    def test_clear_attribution(self):
        """测试清空作者和来源"""
        # 先设置一些数据
        self.widget.set_author("作者")
        self.widget.set_source("来源")

        result = self.widget.clear_attribution()

        assert result is self.widget
        assert self.widget._author is None
        assert self.widget._source is None

    def test_get_quote_color(self):
        """测试获取引用颜色"""
        test_cases = [
            (StatusType.SUCCESS, "#107c10"),
            (StatusType.WARNING, "#ff8c00"),
            (StatusType.ERROR, "#d13438"),
            (StatusType.INFO, "#0078d4"),
            (StatusType.PRIMARY, "#0078d4"),
        ]

        for status_type, expected_color in test_cases:
            self.widget._quote_type = status_type
            color = self.widget._get_quote_color()
            assert color == expected_color

    def test_get_template_name(self):
        """测试获取模板名称"""
        assert self.widget._get_template_name() == "quote.html"

    def test_get_template_context_empty(self):
        """测试空引用的模板上下文"""
        context = self.widget.get_template_context()
        assert context == {}

    def test_get_template_context_content_only(self):
        """测试只有内容的引用"""
        self.widget.set_content("简单的引用内容")

        context = self.widget.get_template_context()

        assert context["content"] == "简单的引用内容"
        assert context["citation"] is None
        assert "container_style" in context
        assert "content_style" in context
        assert "citation_style" in context

    def test_get_template_context_with_author_only(self):
        """测试有作者的引用"""
        self.widget.set_content("有作者的引用")
        self.widget.set_author("作者名")

        context = self.widget.get_template_context()

        assert context["content"] == "有作者的引用"
        assert context["citation"] == "— 作者名"

    def test_get_template_context_with_source_only(self):
        """测试只有来源的引用"""
        self.widget.set_content("有来源的引用")
        self.widget.set_source("来源书籍")

        context = self.widget.get_template_context()

        assert context["content"] == "有来源的引用"
        assert context["citation"] == "— 来源书籍"

    def test_get_template_context_with_author_and_source(self):
        """测试有作者和来源的引用"""
        self.widget.set_content("完整的引用")
        self.widget.set_author("作者名")
        self.widget.set_source("来源书籍")

        context = self.widget.get_template_context()

        assert context["content"] == "完整的引用"
        assert context["citation"] == "— 作者名, 来源书籍"

    def test_get_template_context_with_different_quote_types(self):
        """测试不同引用类型的样式"""
        self.widget.set_content("测试引用")

        # 测试不同类型的边框颜色
        test_cases = [
            (StatusType.SUCCESS, "#107c10"),
            (StatusType.WARNING, "#ff8c00"),
            (StatusType.ERROR, "#d13438"),
        ]

        for quote_type, expected_color in test_cases:
            self.widget.set_quote_type(quote_type)
            context = self.widget.get_template_context()

            assert expected_color in context["container_style"]

    def test_get_template_context_style_structure(self):
        """测试样式结构"""
        self.widget.set_content("测试样式")
        self.widget.set_quote_type(StatusType.INFO)

        context = self.widget.get_template_context()

        # 验证样式包含必要的CSS属性
        container_style = context["container_style"]
        assert "border-left:" in container_style
        assert "background:" in container_style
        assert "padding:" in container_style
        assert "margin:" in container_style

        content_style = context["content_style"]
        assert "font-size:" in content_style
        assert "line-height:" in content_style
        assert "font-style: italic" in content_style

        citation_style = context["citation_style"]
        assert "text-align: right" in citation_style


class TestQuoteWidgetIntegration:
    """QuoteWidget集成测试类"""

    def test_chaining_methods(self):
        """测试方法链式调用"""
        widget = (
            QuoteWidget("test_id")
            .set_content("生命不在于长短，而在于精彩")
            .set_author("李白")
            .set_source("唐诗")
            .set_quote_type(StatusType.SUCCESS)
        )

        assert widget.widget_id == "test_id"
        assert widget._content == "生命不在于长短，而在于精彩"
        assert widget._author == "李白"
        assert widget._source == "唐诗"
        assert widget._quote_type == StatusType.SUCCESS

    def test_full_workflow(self):
        """测试完整工作流程"""
        widget = QuoteWidget()

        # 设置引用信息
        widget.set_content("学而时习之，不亦说乎")
        widget.set_author("孔子")
        widget.set_source("《论语》")
        widget.set_quote_type(StatusType.INFO)

        # 获取模板上下文
        context = widget.get_template_context()

        # 验证完整上下文
        assert context["content"] == "学而时习之，不亦说乎"
        assert context["citation"] == "— 孔子, 《论语》"

        # 验证样式包含INFO类型的颜色
        assert "#0078d4" in context["container_style"]

    def test_set_full_quote_workflow(self):
        """测试使用set_full_quote的工作流程"""
        widget = QuoteWidget()

        # 使用set_full_quote一次性设置
        widget.set_full_quote(
            "天行健，君子以自强不息", author="《易经》", source="乾卦"
        )
        widget.set_quote_type(StatusType.WARNING)

        # 验证设置结果
        context = widget.get_template_context()
        assert context["content"] == "天行健，君子以自强不息"
        assert context["citation"] == "— 《易经》, 乾卦"
        assert "#ff8c00" in context["container_style"]  # WARNING颜色

    def test_attribution_operations(self):
        """测试归属信息操作"""
        widget = QuoteWidget()
        widget.set_content("测试内容")

        # 设置完整归属信息
        widget.set_author("作者A")
        widget.set_source("来源A")
        context = widget.get_template_context()
        assert "作者A" in context["citation"]
        assert "来源A" in context["citation"]

        # 清空归属信息
        widget.clear_attribution()
        context = widget.get_template_context()
        assert context["citation"] is None

        # 重新设置部分信息
        widget.set_author("新作者")
        context = widget.get_template_context()
        assert context["citation"] == "— 新作者"

    def test_quote_type_effects(self):
        """测试引用类型效果"""
        widget = QuoteWidget()
        widget.set_content("测试不同类型的引用效果")

        # 测试所有引用类型
        quote_types = [
            StatusType.SUCCESS,
            StatusType.WARNING,
            StatusType.ERROR,
            StatusType.INFO,
            StatusType.PRIMARY,
        ]

        for quote_type in quote_types:
            widget.set_quote_type(quote_type)
            context = widget.get_template_context()

            # 每种类型都应该有对应的颜色
            expected_color = widget._get_quote_color()
            assert expected_color in context["container_style"]
