"""Base Widget Class Definition

This module defines the abstract base class for all widgets, providing basic functionality and interfaces.
"""

import uuid
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Optional

from email_widget.core.logger import get_project_logger
from email_widget.core.template_engine import get_template_engine

if TYPE_CHECKING:
    from email_widget.email import Email


class BaseWidget(ABC):
    """Abstract base class for all widgets.

    This class defines the basic interface and common functionality that all widgets must implement.
    Each widget has a unique ID and can be added to an Email container.

    Attributes:
        widget_id (str): Unique identifier for the widget.
        parent (Optional[Email]): Email container that contains this widget.

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

        # Instantiate custom widget
        widget = MyCustomWidget()
        print(widget.widget_id) # Print generated unique ID
        html_output = widget.render_html()
        print(html_output) # Print rendered HTML
        ```
    """

    def __init__(self, widget_id: str | None = None):
        """Initialize BaseWidget.

        Args:
            widget_id (Optional[str]): Optional widget ID, automatically generated if not provided.
        """
        self._widget_id: str = widget_id or self._generate_id()
        self._parent: Email | None = None
        self._template_engine = get_template_engine()
        self._logger = get_project_logger()

    @property
    def widget_id(self) -> str:
        """Get the unique ID of the widget.

        Returns:
            str: Unique identifier string for the widget.
        """
        return self._widget_id

    @property
    def parent(self) -> Optional["Email"]:
        """Get the Email container that contains this widget.

        Returns:
            Optional[Email]: Email object containing this widget, or None if not added to a container.
        """
        return self._parent

    def _set_parent(self, parent: "Email") -> None:
        """Set the parent container for the widget.

        This is an internal method that is automatically called when the widget is added to an Email container.

        Args:
            parent (Email): Email container object.
        """
        self._parent = parent

    def _generate_id(self) -> str:
        """Generate a unique widget ID.

        ID format: `{lowercase_class_name}_{8_random_hex_chars}`.

        Returns:
            str: Generated unique ID string.
        """
        return f"{self.__class__.__name__.lower()}_{uuid.uuid4().hex[:8]}"

    @abstractmethod
    def _get_template_name(self) -> str:
        """Get the template name corresponding to the widget.

        This is an abstract method that must be implemented by subclasses.

        Returns:
            str: Template file name.
        """
        pass

    def render_html(self) -> str:
        """Render the widget as an HTML string.

        Uses the template engine to render the widget with comprehensive error handling.
        Returns error HTML if rendering fails.

        Returns:
            str: Rendered HTML string.

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
            # Check if template is defined
            if not hasattr(self, "TEMPLATE") or not self.TEMPLATE:
                self._logger.warning(
                    f"Widget {self.__class__.__name__} has no TEMPLATE defined"
                )
                return self._render_error_fallback("Template not defined")

            # Get template context
            context = self.get_template_context()
            if not isinstance(context, dict):
                self._logger.error(
                    f"Widget {self.widget_id} get_template_context returned non-dict type"
                )
                return self._render_error_fallback("Context data error")

            # Render template
            return self._template_engine.render_safe(
                self.TEMPLATE,
                context,
                fallback=self._render_error_fallback("Template rendering failed"),
            )

        except Exception as e:
            self._logger.error(f"Widget {self.widget_id} rendering failed: {e}")
            return self._render_error_fallback(f"Rendering exception: {e}")

    @abstractmethod
    def get_template_context(self) -> dict[str, Any]:
        """Get the context data required for template rendering.

        Subclasses must implement this method to return the data dictionary needed for template rendering.

        Returns:
            Dict[str, Any]: Template context data dictionary.
        """
        pass

    def _render_error_fallback(self, error_msg: str = "") -> str:
        """Fallback handling when rendering fails.

        Args:
            error_msg (str): Error message.

        Returns:
            str: Fallback HTML string.
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
            <strong>Widget Rendering Error:</strong> {self.__class__.__name__} ({self.widget_id})
            {f"<br/>Error Details: {error_msg}" if error_msg else ""}
        </div>
        """

    def set_widget_id(self, widget_id: str) -> "BaseWidget":
        """Set the widget ID.

        Args:
            widget_id (str): New widget ID.

        Returns:
            BaseWidget: Returns self to support method chaining.

        Examples:
            >>> widget.set_widget_id("my_custom_id")
            >>> print(widget.widget_id)  # Output: my_custom_id
        """
        self._widget_id = widget_id
        return self
