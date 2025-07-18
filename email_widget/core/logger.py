"""EmailWidget project logging system

Provides unified logging management functionality with environment variable control and production environment log disabling.
"""

import logging
import os
from typing import Optional


class EmailWidgetLogger:
    """EmailWidget project dedicated logger.

    Provides unified logging interface with environment variable control for log levels.
    Can completely disable log output in production environment.

    Log Levels:
        - `DEBUG`: Debug information, detailed information during development stage.
        - `INFO`: General information, normal operation records.
        - `WARNING`: Warning information, potential problem alerts.
        - `ERROR`: Error information, errors but not fatal problems.
        - `CRITICAL`: Critical errors, system-level serious problems.

    Environment Variable Configuration:
        - `EMAILWIDGET_LOG_LEVEL`: Set log level, e.g., `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`.
        - `EMAILWIDGET_DISABLE_LOGGING`: Set to `true`, `1`, `yes` to completely disable log output.

    Examples:
        ```python
        from email_widget.core.logger import get_project_logger

        logger = get_project_logger()

        # Log different levels
        logger.debug("Debug info: template rendering started")
        logger.info("Email created successfully")
        logger.warning("Used deprecated method")
        logger.error("Widget rendering failed")
        logger.critical("System memory insufficient")
        ```

        You can also use convenience functions directly:

        ```python
        from email_widget.core.logger import info, error

        info("This is an info log.")
        error("This is an error log.")
        ```
    """

    _instance: Optional["EmailWidgetLogger"] = None
    _logger: logging.Logger | None = None

    def __new__(cls) -> "EmailWidgetLogger":
        """Singleton pattern ensures globally unique logger instance.

        Returns:
            EmailWidgetLogger: Globally unique logger instance.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize_logger()
        return cls._instance

    def _initialize_logger(self) -> None:
        """Initialize logger configuration.

        This method configures log level and output behavior based on environment variables
        `EMAILWIDGET_LOG_LEVEL` and `EMAILWIDGET_DISABLE_LOGGING`. It ensures the logger
        is only initialized once.
        """
        self._logger = logging.getLogger("EmailWidget")

        # Avoid adding duplicate handlers
        if self._logger.handlers:
            return

        # Get log level from environment variable, default to INFO
        log_level = os.getenv("EMAILWIDGET_LOG_LEVEL", "INFO").upper()

        # Check if logging is disabled (production environment)
        if os.getenv("EMAILWIDGET_DISABLE_LOGGING", "").lower() in ("true", "1", "yes"):
            self._logger.setLevel(logging.CRITICAL + 1)  # Disable all logging
            return

        # Set log level
        try:
            level = getattr(logging, log_level)
            self._logger.setLevel(level)
        except AttributeError:
            self._logger.setLevel(logging.INFO)

        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self._logger.level)

        # Set log format
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s:%(funcName)s:%(lineno)d - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        console_handler.setFormatter(formatter)

        # Add handler
        self._logger.addHandler(console_handler)

    def debug(self, message: str) -> None:
        """Output debug log.

        Args:
            message (str): Log message.
        """
        if self._logger:
            self._logger.debug(message)

    def info(self, message: str) -> None:
        """Output info log.

        Args:
            message (str): Log message.
        """
        if self._logger:
            self._logger.info(message)

    def warning(self, message: str) -> None:
        """Output warning log.

        Args:
            message (str): Log message.
        """
        if self._logger:
            self._logger.warning(message)

    def error(self, message: str) -> None:
        """Output error log.

        Args:
            message (str): Log message.
        """
        if self._logger:
            self._logger.error(message)

    def critical(self, message: str) -> None:
        """Output critical error log.

        Args:
            message (str): Log message.
        """
        if self._logger:
            self._logger.critical(message)


# Global logger instance
_global_logger: EmailWidgetLogger | None = None


def get_project_logger() -> EmailWidgetLogger:
    """Get project logger instance.

    This function implements singleton pattern, ensuring only one `EmailWidgetLogger` instance
    exists throughout the entire application.

    Returns:
        EmailWidgetLogger: Globally unique `EmailWidgetLogger` instance.

    Examples:
        ```python
        from email_widget.core.logger import get_project_logger

        logger1 = get_project_logger()
        logger2 = get_project_logger()
        assert logger1 is logger2 # True, both are the same instance
        ```
    """
    global _global_logger
    if _global_logger is None:
        _global_logger = EmailWidgetLogger()
    return _global_logger


# Convenience functions
def debug(message: str) -> None:
    """Output debug log.

    Args:
        message (str): Log message.
    """
    get_project_logger().debug(message)


def info(message: str) -> None:
    """Output info log.

    Args:
        message (str): Log message.
    """
    get_project_logger().info(message)


def warning(message: str) -> None:
    """Output warning log.

    Args:
        message (str): Log message.
    """
    get_project_logger().warning(message)


def error(message: str) -> None:
    """Output error log.

    Args:
        message (str): Log message.
    """
    get_project_logger().error(message)


def critical(message: str) -> None:
    """Output critical error log.

    Args:
        message (str): Log message.
    """
    get_project_logger().critical(message)
