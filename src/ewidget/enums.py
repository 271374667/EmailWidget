"""枚举类定义模块"""
from enum import Enum

class LogLevel(Enum):
    """日志级别枚举"""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

class StatusType(Enum):
    """状态类型枚举"""
    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"
    INFO = "info"
    PRIMARY = "primary"

class AlertType(Enum):
    """警告类型枚举"""
    NOTE = "note"
    TIP = "tip"
    IMPORTANT = "important"
    WARNING = "warning"
    CAUTION = "caution"

class TextAlign(Enum):
    """文本对齐枚举"""
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"

class ProgressTheme(Enum):
    """进度条主题枚举"""
    PRIMARY = "primary"
    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"
    INFO = "info"

class LayoutType(Enum):
    """布局类型枚举"""
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical" 