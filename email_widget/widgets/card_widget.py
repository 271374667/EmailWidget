"""卡片Widget实现"""

from typing import Any

from email_widget.core.base import BaseWidget
from email_widget.core.enums import IconType, StatusType
from email_widget.core.validators import NonEmptyStringValidator, SizeValidator


class CardWidget(BaseWidget):
    """创建一个内容卡片，用于以结构化的方式展示信息.

    卡片是组织和呈现信息的理想选择，常用于展示数据摘要、状态更新、个人资料等.
    它支持标题、主要内容、图标以及一个或多个元数据条目.

    Attributes:
        title (Optional[str]): 卡片的标题.
        content (str): 卡片的主要内容文本.
        icon (Optional[str]): 显示在标题前的图标，可以是 Emoji 或其他字符.
        metadata (Dict[str, str]): 一个键值对字典，用于在卡片底部显示额外信息.

    Examples:
        创建一个用于展示服务状态的卡片：

        ```python
        from email_widget.widgets import CardWidget

        card = CardWidget()
        card.set_title("API 服务监控")
        card.set_content("所有服务均运行正常，平均响应时间为 50ms.")
        card.set_icon("✅")
        card.add_metadata("最后检查时间", "2024-07-07 10:30:00")
        card.add_metadata("在线率", "99.99%")

        # 使用链式调用可以使代码更紧凑：
        server_status_card = (CardWidget()\
                              .set_title("数据库服务器")\
                              .set_content("连接正常，磁盘空间充足.")\
                              .set_icon("🗄️")\
                              .set_metadata({
                                  "CPU 使用率": "15%",
                                  "内存占用": "2.5 GB / 16 GB"
                              }))
        ```
    """

    # 模板定义
    TEMPLATE = """
    {% if title or content %}
        <div style="{{ card_style }}">
            {% if title %}
                <h3 style="{{ title_style }}">
                    {% if icon %}{{ icon }} {% endif %}{{ title }}
                </h3>
            {% endif %}
            {% if content %}
                <div style="{{ content_style }}">{{ content }}</div>
            {% endif %}
            {% if metadata %}
                <div style="{{ metadata_container_style }}">
                    {% for key, value in metadata.items() %}
                        <div style="{{ metadata_item_style }}">
                            <strong>{{ key }}:</strong> {{ value }}
                        </div>
                    {% endfor %}
                </div>
            {% endif %}
        </div>
    {% endif %}
    """

    def __init__(self, widget_id: str | None = None):
        """初始化CardWidget.

        Args:
            widget_id (Optional[str]): 可选的Widget ID.
        """
        super().__init__(widget_id)
        self._title: str | None = None
        self._content: str = ""
        self._status: StatusType | None = None
        self._icon: str | None = IconType.INFO.value  # 默认Info图标
        self._metadata: dict[str, str] = {}
        self._elevated: bool = True
        self._padding: str = "16px"
        self._border_radius: str = "4px"

        # 初始化验证器
        self._text_validator = NonEmptyStringValidator()
        self._size_validator = SizeValidator()

    def set_title(self, title: str) -> "CardWidget":
        """设置卡片的标题.

        Args:
            title (str): 卡片标题文本.

        Returns:
            CardWidget: 返回self以支持链式调用.

        Raises:
            ValueError: 当标题为空时.

        Examples:
            >>> card = CardWidget().set_title("系统状态")
        """
        if not self._text_validator.validate(title):
            raise ValueError(
                f"标题验证失败: {self._text_validator.get_error_message(title)}"
            )

        self._title = title
        return self

    def set_content(self, content: str) -> "CardWidget":
        """设置卡片的主要内容文本.

        Args:
            content (str): 卡片内容文本.

        Returns:
            CardWidget: 返回self以支持链式调用.

        Raises:
            ValueError: 当内容为空时.

        Examples:
            >>> card = CardWidget().set_content("所有服务运行正常.")
        """
        if not self._text_validator.validate(content):
            raise ValueError(
                f"内容验证失败: {self._text_validator.get_error_message(content)}"
            )

        self._content = content
        return self

    def set_status(self, status: StatusType) -> "CardWidget":
        """设置卡片的状态.

        此状态通常用于内部逻辑或未来可能的视觉指示，目前不直接影响卡片外观.

        Args:
            status (StatusType): 卡片的状态类型.

        Returns:
            CardWidget: 返回self以支持链式调用.

        Examples:
            >>> card = CardWidget().set_status(StatusType.SUCCESS)
        """
        self._status = status
        return self

    def set_icon(self, icon: str | IconType) -> "CardWidget":
        """设置显示在标题前的图标.

        图标可以是任何字符串（如Emoji字符）或 `IconType` 枚举值.

        Args:
            icon (Union[str, IconType]): 图标字符串或 `IconType` 枚举.

        Returns:
            CardWidget: 返回self以支持链式调用.

        Examples:
            >>> card = CardWidget().set_icon("✅")
            >>> card = CardWidget().set_icon(IconType.DATA)
        """
        if isinstance(icon, IconType):
            self._icon = icon.value
        else:
            self._icon = icon
        return self

    def add_metadata(self, key: str, value: str) -> "CardWidget":
        """向卡片添加一个元数据条目.

        元数据以键值对的形式显示在卡片底部.

        Args:
            key (str): 元数据项的键（名称）.
            value (str): 元数据项的值.

        Returns:
            CardWidget: 返回self以支持链式调用.

        Examples:
            >>> card = CardWidget().add_metadata("版本", "1.0.0")
        """
        self._metadata[key] = value
        return self

    def set_metadata(self, metadata: dict[str, str]) -> "CardWidget":
        """设置卡片的所有元数据.

        此方法会替换所有现有的元数据.

        Args:
            metadata (Dict[str, str]): 包含所有元数据项的字典.

        Returns:
            CardWidget: 返回self以支持链式调用.

        Examples:
            >>> card = CardWidget().set_metadata({"CPU": "15%", "内存": "60%"})
        """
        self._metadata = metadata.copy()
        return self

    def clear_metadata(self) -> "CardWidget":
        """清空卡片的所有元数据.

        Returns:
            CardWidget: 返回self以支持链式调用.

        Examples:
            >>> card = CardWidget().clear_metadata()
        """
        self._metadata.clear()
        return self

    def _get_template_name(self) -> str:
        return "card.html"

    def get_template_context(self) -> dict[str, Any]:
        """获取模板渲染所需的上下文数据"""
        if not self._title and not self._content:
            return {}

        card_style = f"""
            background: #ffffff;
            border: 1px solid #e1dfdd;
            border-radius: {self._border_radius};
            padding: {self._padding};
            margin: 16px 0;
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
        """

        if self._elevated:
            card_style += " box-shadow: 0 2px 4px rgba(0,0,0,0.1);"

        title_style = (
            "font-size: 18px; font-weight: 600; color: #323130; margin-bottom: 8px;"
        )
        content_style = "color: #323130; line-height: 1.5; font-size: 14px;"
        metadata_container_style = (
            "margin-top: 12px; padding-top: 12px; border-top: 1px solid #e1dfdd;"
        )
        metadata_item_style = "margin: 4px 0; font-size: 13px;"

        return {
            "title": self._title,
            "content": self._content,
            "icon": self._icon,
            "metadata": self._metadata if self._metadata else None,
            "card_style": card_style,
            "title_style": title_style,
            "content_style": content_style,
            "metadata_container_style": metadata_container_style,
            "metadata_item_style": metadata_item_style,
        }
