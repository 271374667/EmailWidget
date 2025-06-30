"""EmailWidget项目日志系统

提供统一的日志管理功能，支持环境变量控制和生产环境日志禁用。
"""
import logging
import os
from typing import Optional
from pathlib import Path


class EmailWidgetLogger:
    """EmailWidget项目专用日志器
    
    提供统一的日志接口，支持通过环境变量控制日志级别。
    在生产环境中可以完全禁用日志输出。
    """
    
    _instance: Optional['EmailWidgetLogger'] = None
    _logger: Optional[logging.Logger] = None
    
    def __new__(cls) -> 'EmailWidgetLogger':
        """单例模式确保全局唯一的日志器实例"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize_logger()
        return cls._instance
    
    def _initialize_logger(self) -> None:
        """初始化日志器配置"""
        self._logger = logging.getLogger('EmailWidget')
        
        # 避免重复添加处理器
        if self._logger.handlers:
            return
            
        # 从环境变量获取日志级别，默认为INFO
        log_level = os.getenv('EMAILWIDGET_LOG_LEVEL', 'INFO').upper()
        
        # 检查是否禁用日志（生产环境）
        if os.getenv('EMAILWIDGET_DISABLE_LOGGING', '').lower() in ('true', '1', 'yes'):
            self._logger.setLevel(logging.CRITICAL + 1)  # 禁用所有日志
            return
        
        # 设置日志级别
        try:
            level = getattr(logging, log_level)
            self._logger.setLevel(level)
        except AttributeError:
            self._logger.setLevel(logging.INFO)
        
        # 创建控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self._logger.level)
        
        # 设置日志格式
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(name)s:%(funcName)s:%(lineno)d - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_handler.setFormatter(formatter)
        
        # 添加处理器
        self._logger.addHandler(console_handler)
    
    def debug(self, message: str) -> None:
        """输出调试日志"""
        if self._logger:
            self._logger.debug(message)
    
    def info(self, message: str) -> None:
        """输出信息日志"""
        if self._logger:
            self._logger.info(message)
    
    def warning(self, message: str) -> None:
        """输出警告日志"""
        if self._logger:
            self._logger.warning(message)
    
    def error(self, message: str) -> None:
        """输出错误日志"""
        if self._logger:
            self._logger.error(message)
    
    def critical(self, message: str) -> None:
        """输出严重错误日志"""
        if self._logger:
            self._logger.critical(message)


# 全局日志器实例
_global_logger: Optional[EmailWidgetLogger] = None


def get_project_logger() -> EmailWidgetLogger:
    """获取项目日志器实例
    
    Returns:
        EmailWidgetLogger实例
    """
    global _global_logger
    if _global_logger is None:
        _global_logger = EmailWidgetLogger()
    return _global_logger


# 便捷函数
def debug(message: str) -> None:
    """输出调试日志"""
    get_project_logger().debug(message)


def info(message: str) -> None:
    """输出信息日志"""
    get_project_logger().info(message)


def warning(message: str) -> None:
    """输出警告日志"""
    get_project_logger().warning(message)


def error(message: str) -> None:
    """输出错误日志"""
    get_project_logger().error(message)


def critical(message: str) -> None:
    """输出严重错误日志"""
    get_project_logger().critical(message) 