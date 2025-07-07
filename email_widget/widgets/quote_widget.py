"""引用样式Widget实现"""

from typing import Any

from email_widget.core.base import BaseWidget
from email_widget.core.enums import StatusType


class QuoteWidget(BaseWidget):
    """创建一个带有引述风格的文本块，用于突出显示引用的内容.

    该微件非常适合在邮件中引用名言、客户评价、重要声明或文献摘要.
    它通过在左侧添加一条彩色的竖线来与其他文本区分开，使其在视觉上更引人注目.

    核心功能:
        - **内容归属**: 支持设置引述的作者和来源.
        - **主题化**: 引述的左侧边框颜色可以根据状态类型（如 INFO, SUCCESS, WARNING）改变.

    Attributes:
        content (str): 被引用的主要文本内容.
        author (Optional[str]): 引述的作者.
        source (Optional[str]): 引述的出处或来源.
        quote_type (StatusType): 引述的类型，决定了左侧边框的颜色.

    Examples:
        创建一个经典的名人名言引述：

        ```python
        from email_widget.widgets import QuoteWidget
        from email_widget.core.enums import StatusType

        quote = (QuoteWidget()\
                 .set_content("The only way to do great work is to love what you do.")\
                 .set_author("Steve Jobs")\
                 .set_quote_type(StatusType.INFO))

        # 假设 email 是一个 Email 对象
        # email.add_widget(quote)
        ```

        创建一个用于展示客户好评的引述：

        ```python
        customer_feedback = (QuoteWidget()\
                             .set_content("This new feature has significantly improved our workflow!")\
                             .set_author("Satisfied Customer")\
                             .set_source("Feedback Survey")\
                             .set_quote_type(StatusType.SUCCESS))
        ```
    """

    # 模板定义
    TEMPLATE = """
    {% if content %}
        <!--[if mso]>
        <table width="100%" cellpadding="0" cellspacing="0" border="0">
            <tr>
                <td>
        <![endif]-->
        <blockquote style="{{ container_style }}">
            <p style="{{ content_style }}">"{{ content }}"</p>
            {% if citation %}
                <cite style="{{ citation_style }}">{{ citation }}</cite>
            {% endif %}
        </blockquote>
        <!--[if mso]>
                </td>
            </tr>
        </table>
        <![endif]-->
    {% endif %}
    """

    def __init__(self, widget_id: str | None = None):
        """初始化QuoteWidget.

        Args:
            widget_id (Optional[str]): 可选的Widget ID.
        """
        super().__init__(widget_id)
        self._content: str = ""
        self._author: str | None = None
        self._source: str | None = None
        self._quote_type: StatusType = StatusType.INFO

    def set_content(self, content: str) -> "QuoteWidget":
        """设置引用的主要文本内容.

        Args:
            content (str): 被引用的文本内容.

        Returns:
            QuoteWidget: 返回self以支持链式调用.

        Examples:
            >>> quote = QuoteWidget().set_content("知识就是力量.")
        """
        self._content = content
        return self

    def set_author(self, author: str) -> "QuoteWidget":
        """设置引用的作者.

        Args:
            author (str): 作者姓名.

        Returns:
            QuoteWidget: 返回self以支持链式调用.

        Examples:
            >>> quote = QuoteWidget().set_author("鲁迅")
        """
        self._author = author
        return self

    def set_source(self, source: str) -> "QuoteWidget":
        """设置引用的来源.

        Args:
            source (str): 来源描述（如书籍名称、网站、报告等）.

        Returns:
            QuoteWidget: 返回self以支持链式调用.

        Examples:
            >>> quote = QuoteWidget().set_source("《论语》")
        """
        self._source = source
        return self

    def set_quote_type(self, quote_type: StatusType) -> "QuoteWidget":
        """设置引用的类型.

        此类型决定了引用块左侧边框的颜色.

        Args:
            quote_type (StatusType): 引用类型枚举值.

        Returns:
            QuoteWidget: 返回self以支持链式调用.

        Examples:
            >>> quote = QuoteWidget().set_quote_type(StatusType.WARNING)
        """
        self._quote_type = quote_type
        return self

    def set_full_quote(
        self, content: str, author: str = None, source: str = None
    ) -> "QuoteWidget":
        """一次性设置完整的引用信息.

        此方法允许同时设置引用内容、作者和来源，方便快速配置.

        Args:
            content (str): 引用内容.
            author (str): 可选的作者姓名.
            source (str): 可选的来源描述.

        Returns:
            QuoteWidget: 返回self以支持链式调用.

        Examples:
            >>> quote = QuoteWidget().set_full_quote("天行健，君子以自强不息.", "《周易》")
        """
        self._content = content
        if author:
            self._author = author
        if source:
            self._source = source
        return self

    def clear_attribution(self) -> "QuoteWidget":
        """清空作者和来源信息.

        Returns:
            QuoteWidget: 返回self以支持链式调用.

        Examples:
            >>> quote = QuoteWidget().clear_attribution()
        """
        self._author = None
        self._source = None
        return self

    def _get_quote_color(self) -> str:
        """获取引用颜色"""
        colors = {
            StatusType.SUCCESS: "#107c10",
            StatusType.WARNING: "#ff8c00",
            StatusType.ERROR: "#d13438",
            StatusType.INFO: "#0078d4",
            StatusType.PRIMARY: "#0078d4",
        }
        return colors[self._quote_type]

    def _get_template_name(self) -> str:
        return "quote.html"

    def get_template_context(self) -> dict[str, Any]:
        """获取模板渲染所需的上下文数据"""
        if not self._content:
            return {}

        border_color = self._get_quote_color()

        container_style = f"""
            border-left: 4px solid {border_color};
            background: #faf9f8;
            padding: 16px 20px;
            margin: 16px 0;
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
            border-radius: 0 4px 4px 0;
        """

        content_style = """
            font-size: 16px;
            line-height: 1.6;
            color: #323130;
            margin: 0 0 12px 0;
            font-style: italic;
        """

        citation_style = """
            font-size: 14px;
            color: #605e5c;
            text-align: right;
            margin: 0;
        """

        # 处理引用信息
        citation = None
        if self._author or self._source:
            citation_text = ""
            if self._author:
                citation_text += f"— {self._author}"
            if self._source:
                if self._author:
                    citation_text += f", {self._source}"
                else:
                    citation_text += f"— {self._source}"
            citation = citation_text

        return {
            "content": self._content,
            "citation": citation,
            "container_style": container_style,
            "content_style": content_style,
            "citation_style": citation_style,
        }
