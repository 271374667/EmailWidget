"""基础Widget类定义

这个模块定义了所有Widget的基础抽象类，提供了Widget的基本功能和接口。
"""

import uuid
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Optional

from email_widget.core.logger import get_project_logger
from email_widget.core.template_engine import get_template_engine

if TYPE_CHECKING:
    from email_widget.email import Email


class BaseWidget(ABC):
    """所有Widget的基础抽象类。

    这个类定义了所有Widget必须实现的基本接口和通用功能。
    每个Widget都有一个唯一的ID，可以被添加到Email容器中。

    Attributes:
        widget_id (str): Widget的唯一标识符。
        parent (Optional[Email]): 包含此Widget的Email容器。

    Examples:
        ```python
        from abc import ABC, abstractmethod
        from email_widget.core.base import BaseWidget
        from typing import Dict, Any, Optional

        class MyCustomWidget(BaseWidget):
            TEMPLATE = "<div>Hello from Custom Widget!</div>"

            def _get_template_name(self) -> str:
                return "my_custom_widget.html"

            def get_template_context(self) -> Dict[str, Any]:
                return {"message": "This is a custom message.", "data": "some data"}

        # 实例化自定义Widget
        widget = MyCustomWidget()
        print(widget.widget_id) # 打印生成的唯一ID
        html_output = widget.render_html()
        print(html_output) # 打印渲染后的HTML
        ```
    """

    def __init__(self, widget_id: str | None = None):
        """初始化BaseWidget。

        Args:
            widget_id (Optional[str]): 可选的Widget ID，如果不提供则自动生成。
        """
        self._widget_id: str = widget_id or self._generate_id()
        self._parent: Email | None = None
        self._template_engine = get_template_engine()
        self._logger = get_project_logger()

    @property
    def widget_id(self) -> str:
        """获取Widget的唯一ID。

        Returns:
            str: Widget的唯一标识符字符串。
        """
        return self._widget_id

    @property
    def parent(self) -> Optional["Email"]:
        """获取包含此Widget的Email容器。

        Returns:
            Optional[Email]: 包含此Widget的Email对象，如果未被添加到容器中则返回None。
        """
        return self._parent

    def _set_parent(self, parent: "Email") -> None:
        """设置Widget的父容器。

        这是一个内部方法，当Widget被添加到Email容器时会自动调用。

        Args:
            parent (Email): Email容器对象。
        """
        self._parent = parent

    def _generate_id(self) -> str:
        """生成唯一的Widget ID。

        ID格式为: `{类名小写}_{8位随机十六进制字符}`。

        Returns:
            str: 生成的唯一ID字符串。
        """
        return f"{self.__class__.__name__.lower()}_{uuid.uuid4().hex[:8]}"

    @abstractmethod
    def _get_template_name(self) -> str:
        """获取Widget对应的模板名称。

        这是一个抽象方法，子类必须实现。

        Returns:
            str: 模板文件名称。
        """
        pass

    def render_html(self) -> str:
        """将Widget渲染为HTML字符串。

        使用模板引擎渲染Widget，包含完整的容错机制。如果渲染失败，会返回错误提示的HTML。

        Returns:
            str: 渲染后的HTML字符串。

        Examples:
            ```python
            class MyWidget(BaseWidget):
                TEMPLATE = "<div>{{ content }}</div>"

                def _get_template_name(self):
                    return "my_widget.html"

                def get_template_context(self):
                    return {"content": "Hello World"}

            widget = MyWidget()
            html = widget.render_html()
            print(html)  # <div>Hello World</div>
            ```
        """
        try:
            # 检查是否有模板定义
            if not hasattr(self, "TEMPLATE") or not self.TEMPLATE:
                self._logger.warning(
                    f"Widget {self.__class__.__name__} 没有定义TEMPLATE"
                )
                return self._render_error_fallback("模板未定义")

            # 获取模板上下文
            context = self.get_template_context()
            if not isinstance(context, dict):
                self._logger.error(
                    f"Widget {self.widget_id} 的get_template_context返回了非字典类型"
                )
                return self._render_error_fallback("上下文数据错误")

            # 渲染模板
            return self._template_engine.render_safe(
                self.TEMPLATE,
                context,
                fallback=self._render_error_fallback("模板渲染失败"),
            )

        except Exception as e:
            self._logger.error(f"Widget {self.widget_id} 渲染失败: {e}")
            return self._render_error_fallback(f"渲染异常: {e}")

    @abstractmethod
    def get_template_context(self) -> dict[str, Any]:
        """获取模板渲染所需的上下文数据。

        子类必须实现此方法，返回模板渲染所需的数据字典。

        Returns:
            Dict[str, Any]: 模板上下文数据字典。
        """
        pass

    def _render_error_fallback(self, error_msg: str = "") -> str:
        """渲染失败时的降级处理。

        Args:
            error_msg (str): 错误信息。

        Returns:
            str: 降级HTML字符串。
        """
        return f"""
        <div style="
            border: 2px solid #d13438;
            background: #ffebee;
            color: #d13438;
            padding: 12px;
            margin: 8px 0;
            border-radius: 4px;
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
            font-size: 14px;
        ">
            <strong>Widget渲染错误:</strong> {self.__class__.__name__} ({self.widget_id})
            {f"<br/>错误详情: {error_msg}" if error_msg else ""}
        </div>
        """

    def set_widget_id(self, widget_id: str) -> "BaseWidget":
        """设置Widget的ID。

        Args:
            widget_id (str): 新的Widget ID。

        Returns:
            BaseWidget: 返回self以支持链式调用。

        Examples:
            >>> widget.set_widget_id("my_custom_id")
            >>> print(widget.widget_id)  # 输出: my_custom_id
        """
        self._widget_id = widget_id
        return self
