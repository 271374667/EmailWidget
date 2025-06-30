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

class TextType(Enum):
    """文本类型枚举"""
    TITLE_LARGE = "title_large"      # 大标题
    TITLE_SMALL = "title_small"      # 小标题
    BODY = "body"                    # 正文(默认)
    CAPTION = "caption"              # 正文补充
    SECTION_H2 = "section_h2"        # 二级章节标题
    SECTION_H3 = "section_h3"        # 三级章节标题
    SECTION_H4 = "section_h4"        # 四级章节标题
    SECTION_H5 = "section_h5"        # 五级章节标题

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

class IconType(Enum):
    """图标类型枚举 - 爬虫和数据处理领域常用图标"""
    # 数据相关
    DATA = "📊"
    DATABASE = "🗄️"
    CHART = "📈"
    TABLE = "📋"
    REPORT = "📄"
    
    # 爬虫相关
    SPIDER = "🕷️"
    WEB = "🌐"
    LINK = "🔗"
    SEARCH = "🔍"
    DOWNLOAD = "⬇️"
    
    # 系统相关
    SERVER = "🖥️"
    NETWORK = "🌐"
    STORAGE = "💾"
    MEMORY = "🧠"
    CPU = "⚡"
    
    # 状态相关
    SUCCESS = "✅"
    ERROR = "❌"
    WARNING = "⚠️"
    INFO = "ℹ️"
    PROCESSING = "⚙️"
    
    # 默认图标
    DEFAULT = "📋"