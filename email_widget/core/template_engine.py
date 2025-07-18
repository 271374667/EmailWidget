"""EmailWidget template engine

Lightweight template rendering engine based on Jinja2, supports template string rendering and error handling.
"""

from typing import Any

from jinja2 import BaseLoader, Environment, Template, TemplateError

from email_widget.core.logger import get_project_logger


class StringTemplateLoader(BaseLoader):
    """String template loader.

    Used to load templates directly from strings rather than from filesystem. This enables
    the template engine to handle dynamically generated or in-memory template strings.
    """

    def get_source(self, environment: Environment, template: str) -> tuple:
        """Get template source code.

        Args:
            environment (Environment): Jinja2 environment.
            template (str): Template string.

        Returns:
            tuple: (source code, template name, is_latest) tuple.
        """
        return template, None, lambda: True


class TemplateEngine:
    """Template rendering engine.

    Provides unified template rendering interface with template caching and error handling.

    Core Features:
        - **Template Rendering**: Uses Jinja2 to render Widget templates.
        - **Cache Management**: Template compilation caching improves performance.
        - **Error Handling**: Safe template rendering and error recovery.
        - **Context Processing**: Automatic handling of template context data.

    Examples:
        ```python
        from email_widget.core.template_engine import get_template_engine

        engine = get_template_engine()

        # Render a simple template
        html = engine.render_safe(
            "<div>Hello, {{ name }}!</div>",
            {"name": "EmailWidget"}
        )
        print(html) # Output: <div>Hello, EmailWidget!</div>

        # Render a template with errors and use fallback content
        error_html = engine.render_safe(
            "<div>{% for item in items %} {{ item.name }} {% endfor %}</div>",
            {"items": "not_a_list"}, # Intentionally pass wrong type
            fallback="<div>Rendering failed, please contact administrator.</div>"
        )
        print(error_html) # Output: <div>Rendering failed, please contact administrator.</div>
        ```
    """

    def __init__(self):
        """Initialize template engine."""
        self._logger = get_project_logger()

        # Create Jinja2 environment
        self._env = Environment(
            loader=StringTemplateLoader(),
            autoescape=False,  # Email HTML doesn't need auto-escaping
            trim_blocks=True,
            lstrip_blocks=True,
        )

        # Template cache {template_string: Template}
        self._template_cache: dict[str, Template] = {}

        self._logger.debug("Template engine initialization complete")

    def _get_template(self, template_string: str) -> Template:
        """Get compiled template object.

        Args:
            template_string (str): Template string.

        Returns:
            Template: Compiled Template object.

        Raises:
            TemplateError: Thrown when template compilation fails.
        """
        # Check cache
        if template_string in self._template_cache:
            return self._template_cache[template_string]

        try:
            # Compile template
            template = self._env.from_string(template_string)

            # Cache template
            self._template_cache[template_string] = template

            self._logger.debug(f"Compiled and cached template, length: {len(template_string)} characters")
            return template

        except TemplateError as e:
            self._logger.error(f"Template compilation failed: {e}")
            raise

    def render(self, template_string: str, context: dict[str, Any]) -> str:
        """Render template.

        Args:
            template_string (str): Template string.
            context (Dict[str, Any]): Template context data.

        Returns:
            str: Rendered HTML string.

        Raises:
            TemplateError: Thrown when template rendering fails.
        """
        try:
            template = self._get_template(template_string)
            result = template.render(**context)

            self._logger.debug(f"Template rendering successful, output length: {len(result)} characters")
            return result

        except TemplateError as e:
            self._logger.error(f"Template rendering failed: {e}")
            raise
        except Exception as e:
            self._logger.error(f"Template rendering encountered unknown error: {e}")
            raise TemplateError(f"Template rendering failed: {e}")

    def render_safe(
        self, template_string: str, context: dict[str, Any], fallback: str = ""
    ) -> str:
        """Safely render template.

        Returns fallback content instead of throwing exception on rendering failure.

        Args:
            template_string (str): Template string.
            context (Dict[str, Any]): Template context data.
            fallback (str): Fallback content on rendering failure.

        Returns:
            str: Rendered HTML string or fallback content.
        """
        try:
            return self.render(template_string, context)
        except Exception as e:
            self._logger.warning(f"Template safe rendering failed, using fallback content: {e}")
            return fallback

    def validate_template(self, template_string: str) -> bool:
        """Validate template syntax.

        Args:
            template_string (str): Template string.

        Returns:
            bool: Whether template syntax is correct.
        """
        try:
            self._env.from_string(template_string)
            return True
        except TemplateError:
            return False
        except Exception:
            return False

    def clear_cache(self) -> None:
        """Clear template cache."""
        self._template_cache.clear()
        self._logger.debug("Cleared template cache")

    def get_cache_stats(self) -> dict[str, Any]:
        """Get cache statistics.

        Returns:
            Dict[str, Any]: Cache statistics dictionary, including cached template count and total size (bytes).
        """
        return {
            "cached_templates": len(self._template_cache),
            "cache_size_bytes": sum(
                len(template_str) for template_str in self._template_cache.keys()
            ),
        }


# Global template engine instance
_global_template_engine: TemplateEngine | None = None


def get_template_engine() -> TemplateEngine:
    """Get global template engine instance.

    This function implements singleton pattern, ensuring only one `TemplateEngine` instance
    exists throughout the entire application.

    Returns:
        TemplateEngine: Globally unique `TemplateEngine` instance.

    Examples:
        ```python
        from email_widget.core.template_engine import get_template_engine

        engine1 = get_template_engine()
        engine2 = get_template_engine()
        assert engine1 is engine2 # True, both are the same instance
        ```
    """
    global _global_template_engine
    if _global_template_engine is None:
        _global_template_engine = TemplateEngine()
    return _global_template_engine
