"""Logger测试用例"""

import logging
import os
from unittest.mock import MagicMock, patch

from email_widget.core.logger import EmailWidgetLogger, get_project_logger


class TestEmailWidgetLogger:
    """EmailWidgetLogger测试类"""

    def setup_method(self):
        """每个测试方法执行前的设置"""
        # 重置单例实例
        EmailWidgetLogger._instance = None
        EmailWidgetLogger._logger = None
        # 清理环境变量
        if "EMAILWIDGET_LOG_LEVEL" in os.environ:
            del os.environ["EMAILWIDGET_LOG_LEVEL"]
        if "EMAILWIDGET_DISABLE_LOGGING" in os.environ:
            del os.environ["EMAILWIDGET_DISABLE_LOGGING"]
        # 清理全局logger
        import email_widget.core.logger

        email_widget.core.logger._global_logger = None

    def test_singleton_pattern(self):
        """测试单例模式"""
        logger1 = EmailWidgetLogger()
        logger2 = EmailWidgetLogger()
        assert logger1 is logger2

    def test_default_initialization(self):
        """测试默认初始化"""
        logger = EmailWidgetLogger()
        assert logger._logger is not None
        assert logger._logger.name == "EmailWidget"
        assert logger._logger.level == logging.INFO

    def test_logger_methods(self):
        """测试日志方法"""
        logger = EmailWidgetLogger()

        # 测试所有日志方法都存在且可调用
        assert hasattr(logger, "debug")
        assert hasattr(logger, "info")
        assert hasattr(logger, "warning")
        assert hasattr(logger, "error")
        assert hasattr(logger, "critical")

        # 测试方法调用不会抛出异常
        logger.debug("test debug")
        logger.info("test info")
        logger.warning("test warning")
        logger.error("test error")
        logger.critical("test critical")

    @patch("email_widget.core.logger.logging.getLogger")
    def test_logger_initialization_once(self, mock_get_logger):
        """测试logger只初始化一次"""
        mock_logger = MagicMock()
        mock_logger.handlers = []  # 第一次调用时handlers为空
        mock_logger.level = logging.INFO  # 设置一个具体的level值
        mock_get_logger.return_value = mock_logger

        logger = EmailWidgetLogger()
        # 再次获取同一个实例
        logger2 = EmailWidgetLogger()

        # logging.getLogger应该只被调用一次
        assert mock_get_logger.call_count == 1
        assert logger is logger2

    @patch("email_widget.core.logger.logging.getLogger")
    def test_avoid_duplicate_handlers(self, mock_get_logger):
        """测试避免重复添加处理器"""
        mock_logger = MagicMock()
        # 模拟已经有处理器的情况
        mock_logger.handlers = [MagicMock()]
        mock_get_logger.return_value = mock_logger

        EmailWidgetLogger()

        # 由于已有处理器，不应该添加新的处理器
        mock_logger.addHandler.assert_not_called()

    def test_logger_formatter(self):
        """测试日志格式化器"""
        logger = EmailWidgetLogger()

        # 检查是否有处理器
        assert len(logger._logger.handlers) > 0

        # 检查处理器是否有格式化器
        handler = logger._logger.handlers[0]
        assert handler.formatter is not None

        # 检查格式化器的格式
        formatter = handler.formatter
        assert "levelname" in formatter._fmt
        assert "name" in formatter._fmt
        assert "funcName" in formatter._fmt
        assert "lineno" in formatter._fmt
        assert "message" in formatter._fmt


class TestGetProjectLogger:
    """get_project_logger函数测试类"""

    def setup_method(self):
        """每个测试方法执行前的设置"""
        # 重置全局变量
        import email_widget.core.logger

        email_widget.core.logger._global_logger = None
        # 重置单例实例
        EmailWidgetLogger._instance = None
        EmailWidgetLogger._logger = None

    def test_get_project_logger_returns_same_instance(self):
        """测试get_project_logger返回相同实例"""
        logger1 = get_project_logger()
        logger2 = get_project_logger()
        assert logger1 is logger2
        assert isinstance(logger1, EmailWidgetLogger)

    def test_get_project_logger_functionality(self):
        """测试get_project_logger返回的实例功能正常"""
        logger = get_project_logger()

        # 测试所有方法都可用
        logger.debug("test")
        logger.info("test")
        logger.warning("test")
        logger.error("test")
        logger.critical("test")


class TestConvenienceFunctions:
    """便捷函数测试类"""

    def setup_method(self):
        """每个测试方法执行前的设置"""
        import email_widget.core.logger

        email_widget.core.logger._global_logger = None
        EmailWidgetLogger._instance = None
        EmailWidgetLogger._logger = None

    @patch("email_widget.core.logger.get_project_logger")
    def test_debug_function(self, mock_get_logger):
        """测试debug便捷函数"""
        from email_widget.core.logger import debug

        mock_logger_instance = MagicMock()
        mock_get_logger.return_value = mock_logger_instance

        debug("test message")

        mock_get_logger.assert_called_once()
        mock_logger_instance.debug.assert_called_once_with("test message")

    @patch("email_widget.core.logger.get_project_logger")
    def test_info_function(self, mock_get_logger):
        """测试info便捷函数"""
        from email_widget.core.logger import info

        mock_logger_instance = MagicMock()
        mock_get_logger.return_value = mock_logger_instance

        info("test message")

        mock_get_logger.assert_called_once()
        mock_logger_instance.info.assert_called_once_with("test message")

    @patch("email_widget.core.logger.get_project_logger")
    def test_warning_function(self, mock_get_logger):
        """测试warning便捷函数"""
        from email_widget.core.logger import warning

        mock_logger_instance = MagicMock()
        mock_get_logger.return_value = mock_logger_instance

        warning("test message")

        mock_get_logger.assert_called_once()
        mock_logger_instance.warning.assert_called_once_with("test message")

    @patch("email_widget.core.logger.get_project_logger")
    def test_error_function(self, mock_get_logger):
        """测试error便捷函数"""
        from email_widget.core.logger import error

        mock_logger_instance = MagicMock()
        mock_get_logger.return_value = mock_logger_instance

        error("test message")

        mock_get_logger.assert_called_once()
        mock_logger_instance.error.assert_called_once_with("test message")

    @patch("email_widget.core.logger.get_project_logger")
    def test_critical_function(self, mock_get_logger):
        """测试critical便捷函数"""
        from email_widget.core.logger import critical

        mock_logger_instance = MagicMock()
        mock_get_logger.return_value = mock_logger_instance

        critical("test message")

        mock_get_logger.assert_called_once()
        mock_logger_instance.critical.assert_called_once_with("test message")


class TestLoggerIntegration:
    """日志器集成测试"""

    def setup_method(self):
        """每个测试方法执行前的设置"""
        EmailWidgetLogger._instance = None
        EmailWidgetLogger._logger = None
        import email_widget.core.logger

        email_widget.core.logger._global_logger = None

    def test_end_to_end_logging(self):
        """测试端到端日志记录"""
        from email_widget.core.logger import critical, debug, error, info, warning

        # 这些调用不应该抛出异常
        info("Integration test info")
        debug("Integration test debug")
        warning("Integration test warning")
        error("Integration test error")
        critical("Integration test critical")

    def test_logger_instance_consistency(self):
        """测试logger实例一致性"""
        from email_widget.core.logger import get_project_logger

        # 通过不同方式获取的logger应该是同一个实例
        logger1 = EmailWidgetLogger()
        logger2 = get_project_logger()

        # 它们应该是同一个对象
        assert logger1 is logger2
