"""Quote Style Widget Implementation"""

from typing import Any

from email_widget.core.base import BaseWidget
from email_widget.core.enums import StatusType


class QuoteWidget(BaseWidget):
    """Create a quote-style text block for highlighting quoted content.

    This widget is perfect for quoting famous sayings, customer reviews, important statements, or literature excerpts in emails.
    It distinguishes itself from other text by adding a colored vertical line on the left side, making it visually more prominent.

    Core features:
        - **Content attribution**: Supports setting the author and source of the quote.
        - **Theming**: The left border color of the quote can change based on status type (such as INFO, SUCCESS, WARNING).

    Attributes:
        content (str): The main text content being quoted.
        author (Optional[str]): Author of the quote.
        source (Optional[str]): Source or origin of the quote.
        quote_type (StatusType): Type of quote, determines the color of the left border.

    Examples:
        Create a classic famous quote:

        ```python
        from email_widget.widgets import QuoteWidget
        from email_widget.core.enums import StatusType

        quote = (QuoteWidget()\
                 .set_content("The only way to do great work is to love what you do.")\
                 .set_author("Steve Jobs")\
                 .set_quote_type(StatusType.INFO))

        # Assuming email is an Email object
        # email.add_widget(quote)
        ```

        Create a quote for showcasing customer testimonials:

        ```python
        customer_feedback = (QuoteWidget()\
                             .set_content("This new feature has significantly improved our workflow!")\
                             .set_author("Satisfied Customer")\
                             .set_source("Feedback Survey")\
                             .set_quote_type(StatusType.SUCCESS))
        ```
    """

    # Template definition
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
        """Initialize QuoteWidget.

        Args:
            widget_id (Optional[str]): Optional Widget ID.
        """
        super().__init__(widget_id)
        self._content: str = ""
        self._author: str | None = None
        self._source: str | None = None
        self._quote_type: StatusType = StatusType.INFO

    def set_content(self, content: str) -> "QuoteWidget":
        """Set the main text content of the quote.

        Args:
            content (str): The text content to be quoted.

        Returns:
            QuoteWidget: Returns self to support method chaining.

        Examples:
            >>> quote = QuoteWidget().set_content("Knowledge is power.")
        """
        self._content = content
        return self

    def set_author(self, author: str) -> "QuoteWidget":
        """Set the author of the quote.

        Args:
            author (str): Author name.

        Returns:
            QuoteWidget: Returns self to support method chaining.

        Examples:
            >>> quote = QuoteWidget().set_author("Lu Xun")
        """
        self._author = author
        return self

    def set_source(self, source: str) -> "QuoteWidget":
        """Set the source of the quote.

        Args:
            source (str): Source description (such as book name, website, report, etc.).

        Returns:
            QuoteWidget: Returns self to support method chaining.

        Examples:
            >>> quote = QuoteWidget().set_source("The Analects")
        """
        self._source = source
        return self

    def set_quote_type(self, quote_type: StatusType) -> "QuoteWidget":
        """Set the type of the quote.

        This type determines the color of the left border of the quote block.

        Args:
            quote_type (StatusType): Quote type enum value.

        Returns:
            QuoteWidget: Returns self to support method chaining.

        Examples:
            >>> quote = QuoteWidget().set_quote_type(StatusType.WARNING)
        """
        self._quote_type = quote_type
        return self

    def set_full_quote(
        self, content: str, author: str = None, source: str = None
    ) -> "QuoteWidget":
        """Set complete quote information at once.

        This method allows you to set quote content, author, and source simultaneously for quick configuration.

        Args:
            content (str): Quote content.
            author (str): Optional author name.
            source (str): Optional source description.

        Returns:
            QuoteWidget: Returns self to support method chaining.

        Examples:
            >>> quote = QuoteWidget().set_full_quote("Heaven is vigorous, and the gentleman strives for self-improvement.", "I Ching")
        """
        self._content = content
        if author:
            self._author = author
        if source:
            self._source = source
        return self

    def clear_attribution(self) -> "QuoteWidget":
        """Clear author and source information.

        Returns:
            QuoteWidget: Returns self to support method chaining.

        Examples:
            >>> quote = QuoteWidget().clear_attribution()
        """
        self._author = None
        self._source = None
        return self

    def _get_quote_color(self) -> str:
        """Get quote color"""
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
        """Get template context data required for rendering"""
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

        # Process quote information
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
