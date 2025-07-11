"""图片Widget实现"""

from pathlib import Path
from typing import Any

from email_widget.core.base import BaseWidget
from email_widget.core.validators import (
    NonEmptyStringValidator,
    SizeValidator,
    UrlValidator,
)
from email_widget.utils.image_utils import ImageUtils


class ImageWidget(BaseWidget):
    """在邮件中嵌入图片，并可选择性地附带标题和描述。

    该微件简化了在邮件中添加图片的过程。它能够处理来自网络 URL 或本地文件
    的图片，并自动将其转换为 Base64 编码的 data URI，以确保图片能在绝大多数
    邮件客户端中正确显示，无需依赖外部链接。

    核心功能:
        - **多源支持**: 可加载来自 URL 或本地文件路径的图片。
        - **自动内联**: 所有图片都会被自动转换为 Base64 并嵌入 HTML，提高兼容性。
        - **图文并茂**: 支持为图片添加标题和描述，形成图文说明。
        - **样式控制**: 可以自定义图片的尺寸、最大宽度和边框圆角。

    Attributes:
        image_url (Optional[str]): 处理后的图片来源，通常为 Base64 data URI。
        title (Optional[str]): 图片下方的标题。
        description (Optional[str]): 图片标题下方的详细描述。
        alt_text (str): 图片的替代文本，用于可访问性（Accessibility）。

    Examples:
        从网络 URL 加载一张图片并添加说明：

        ```python
        from email_widget.widgets import ImageWidget

        image_from_url = (ImageWidget()
                          .set_image_url("https://www.example.com/images/product_photo.jpg")
                          .set_title("最新产品展示")
                          .set_description("展示了我们最新型号的设计和功能。")
                          .set_alt_text("最新产品的正面照片")
                          .set_size(width="100%", height="auto")
                          .set_max_width("600px")
                          .set_border_radius("8px"))

        # 假设 email 是一个 Email 对象
        # email.add_widget(image_from_url)
        ```

        从本地文件加载图片：

        ```python
        from pathlib import Path

        local_image_path = Path("./assets/company_logo.png")
        logo_image = ImageWidget().set_image_url(local_image_path)
        ```
    """

    # 模板定义
    TEMPLATE = """
    {% if image_url %}
        <!--[if mso]>
        <table width="100%" cellpadding="0" cellspacing="0" border="0">
            <tr>
                <td align="center">
        <![endif]-->
        <div style="{{ container_style }}">
            <img src="{{ image_url }}" alt="{{ alt_text }}" 
                 style="{{ img_style }}" 
                 width="{{ img_width }}" 
                 height="{{ img_height }}" />
            {% if show_caption and (title or description) %}
                <div style="margin-top: 8px; width: 100%; max-width: 100%;">
                    {% if title %}
                        <h4 style="margin: 8px 0 4px 0; font-size: 16px; font-weight: 600; color: #323130; text-align: center; font-family: Arial, sans-serif;">{{ title }}</h4>
                    {% endif %}
                    {% if description %}
                        <p style="margin: 4px 0 8px 0; font-size: 14px; color: #605e5c; line-height: 1.4; text-align: center; font-family: Arial, sans-serif;">{{ description }}</p>
                    {% endif %}
                </div>
            {% endif %}
        </div>
        <!--[if mso]>
                </td>
            </tr>
        </table>
        <![endif]-->
    {% endif %}
    """

    def __init__(self, widget_id: str | None = None):
        """初始化ImageWidget。

        Args:
            widget_id (Optional[str]): 可选的Widget ID。
        """
        super().__init__(widget_id)
        self._image_url: str | None = None
        self._title: str | None = None
        self._description: str | None = None
        self._alt_text: str = ""
        self._width: str | None = None
        self._height: str | None = None
        self._border_radius: str = "4px"
        self._show_caption: bool = True
        self._max_width: str = "100%"

        # 初始化验证器
        self._size_validator = SizeValidator()
        self._url_validator = UrlValidator()
        self._text_validator = NonEmptyStringValidator()

    def set_image_url(
        self, image_url: str | Path, cache: bool = True, embed: bool = True
    ) -> "ImageWidget":
        """设置图片来源URL或本地路径。

        此方法支持从网络URL或本地文件路径加载图片。默认情况下，图片会被自动处理并转换为
        Base64编码的data URI，直接嵌入到HTML中，以确保在邮件客户端中的兼容性。

        Args:
            image_url (Union[str, Path]): 图片的URL字符串或本地文件Path对象。
            cache (bool): 是否缓存网络图片，默认为True。
            embed (bool): 是否嵌入图片，默认为True。如果为False，网络URL将直接使用链接，
                         本地文件会给出警告并强制嵌入。

        Returns:
            ImageWidget: 返回self以支持链式调用。

        Raises:
            ValueError: 如果图片URL或路径无效，或图片处理失败。

        Examples:
            >>> widget = ImageWidget().set_image_url("https://example.com/image.png")
            >>> from pathlib import Path
            >>> widget = ImageWidget().set_image_url(Path("local/image.jpg"))
            >>> # 使用外部链接而不嵌入
            >>> widget = ImageWidget().set_image_url("https://example.com/image.png", embed=False)
        """
        self._image_url = ImageUtils.process_image_source(
            image_url, cache=cache, embed=embed
        )
        return self

    def _get_mime_type(self, ext: str) -> str:
        """根据文件扩展名获取MIME类型"""
        mime_types = {
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".gif": "image/gif",
            ".bmp": "image/bmp",
            ".webp": "image/webp",
            ".svg": "image/svg+xml",
        }
        return mime_types.get(ext, "image/png")

    def set_title(self, title: str) -> "ImageWidget":
        """设置图片标题。

        Args:
            title (str): 图片下方的标题文本。

        Returns:
            ImageWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = ImageWidget().set_title("产品销售趋势图")
        """
        self._title = title
        return self

    def set_description(self, description: str) -> "ImageWidget":
        """设置图片描述。

        Args:
            description (str): 图片标题下方的详细描述文本。

        Returns:
            ImageWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = ImageWidget().set_description("此图展示了过去一年的销售数据变化。")
        """
        self._description = description
        return self

    def set_alt_text(self, alt: str) -> "ImageWidget":
        """设置图片的替代文本。

        替代文本在图片无法显示时提供描述，对可访问性（Accessibility）非常重要。

        Args:
            alt (str): 图片的替代文本。

        Returns:
            ImageWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = ImageWidget().set_alt_text("公司Logo")
        """
        self._alt_text = alt
        return self

    def set_size(
        self, width: str | None = None, height: str | None = None
    ) -> "ImageWidget":
        """设置图片的宽度和高度。

        Args:
            width (Optional[str]): 图片的宽度，如 "100px", "50%", "auto"。
            height (Optional[str]): 图片的高度，如 "200px", "auto"。

        Returns:
            ImageWidget: 返回self以支持链式调用。

        Raises:
            ValueError: 当尺寸格式无效时。

        Examples:
            >>> widget = ImageWidget().set_size(width="300px", height="200px")
            >>> widget = ImageWidget().set_size(width="100%", height="auto")
        """
        if width is not None and not self._size_validator.validate(width):
            raise ValueError(
                f"宽度值验证失败: {self._size_validator.get_error_message(width)}"
            )
        if height is not None and not self._size_validator.validate(height):
            raise ValueError(
                f"高度值验证失败: {self._size_validator.get_error_message(height)}"
            )

        self._width = width
        self._height = height
        return self

    def set_border_radius(self, radius: str) -> "ImageWidget":
        """设置图片的边框圆角。

        Args:
            radius (str): CSS边框圆角值，如 "8px", "50%"。

        Returns:
            ImageWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = ImageWidget().set_border_radius("8px")
            >>> widget = ImageWidget().set_border_radius("50%") # 圆形图片
        """
        self._border_radius = radius
        return self

    def set_max_width(self, max_width: str) -> "ImageWidget":
        """设置图片的最大宽度。

        Args:
            max_width (str): CSS最大宽度值，如 "600px", "100%"。

        Returns:
            ImageWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = ImageWidget().set_max_width("600px")
        """
        self._max_width = max_width
        return self

    def show_caption(self, show: bool = True) -> "ImageWidget":
        """设置是否显示图片标题和描述。

        Args:
            show (bool): 是否显示标题和描述，默认为True。

        Returns:
            ImageWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = ImageWidget().show_caption(False) # 隐藏标题和描述
        """
        self._show_caption = show
        return self

    @property
    def image_url(self) -> str | None:
        """获取处理后的图片URL（通常为Base64 data URI）。

        Returns:
            Optional[str]: 图片的Base64 data URI或None。
        """
        return self._image_url

    @property
    def title(self) -> str | None:
        """获取图片标题。

        Returns:
            Optional[str]: 图片标题或None。
        """
        return self._title

    @property
    def description(self) -> str | None:
        """获取图片描述。

        Returns:
            Optional[str]: 图片描述或None。
        """
        return self._description

    @property
    def alt_text(self) -> str:
        """获取图片的替代文本。

        Returns:
            str: 图片的替代文本。
        """
        return self._alt_text

    @property
    def width(self) -> str | None:
        """获取图片宽度。

        Returns:
            Optional[str]: 图片宽度或None。
        """
        return self._width

    @property
    def height(self) -> str | None:
        """获取图片高度。

        Returns:
            Optional[str]: 图片高度或None。
        """
        return self._height

    @property
    def border_radius(self) -> str:
        """获取边框圆角。

        Returns:
            str: 边框圆角值。
        """
        return self._border_radius

    @property
    def is_show_caption(self) -> bool:
        """判断是否显示标题和描述。

        Returns:
            bool: 如果显示标题和描述则为True，否则为False。
        """
        return self._show_caption

    def _get_template_name(self) -> str:
        return "image.html"

    def get_template_context(self) -> dict[str, Any]:
        """获取模板渲染所需的上下文数据"""
        if not self._image_url:
            return {}

        # 构建图片样式 - 邮件客户端兼容
        img_style_parts = [
            f"max-width: {self._max_width}",
            "width: 100%",
            "height: auto",
            "display: block",
            "margin: 0 auto",  # 居中对齐
            "border: 0",  # 移除默认边框
            "outline: none",  # 移除轮廓
        ]

        # 图片尺寸属性（邮件客户端更好支持）
        img_width = "auto"
        img_height = "auto"

        if self._width:
            img_style_parts.append(f"width: {self._width}")
            img_width = (
                self._width.replace("px", "")
                if "px" in str(self._width)
                else self._width
            )
        if self._height:
            img_style_parts.append(f"height: {self._height}")
            img_height = (
                self._height.replace("px", "")
                if "px" in str(self._height)
                else self._height
            )
        if self._border_radius:
            img_style_parts.append(f"border-radius: {self._border_radius}")

        # 容器样式 - 邮件客户端兼容
        container_style = (
            "margin: 16px 0; text-align: center; width: 100%; max-width: 100%;"
        )

        return {
            "image_url": self._image_url,
            "alt_text": self._alt_text,
            "img_style": "; ".join(img_style_parts),
            "img_width": img_width,
            "img_height": img_height,
            "container_style": container_style,
            "title": self._title,
            "description": self._description,
            "show_caption": self._show_caption,
        }
