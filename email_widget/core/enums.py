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
    """文本对齐方式枚举.

    | 枚举值 | 描述 |
    |--------|------|
    | `LEFT` | 左对齐 |
    | `CENTER` | 居中对齐 |
    | `RIGHT` | 右对齐 |
    | `JUSTIFY` | 两端对齐 |
    """

    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"


class TextType(Enum):
    """文本类型枚举，定义了不同的文本样式和语义级别.

    | 枚举值 | 描述 | 默认字体大小 |
    |--------|------|-------------|
    | `TITLE_LARGE` | 大标题 | 24px |
    | `TITLE_SMALL` | 小标题 | 20px |
    | `BODY` | 正文 | 14px |
    | `CAPTION` | 说明文字 | 12px |
    | `SECTION_H2` | 二级标题 | 18px |
    | `SECTION_H3` | 三级标题 | 16px |
    | `SECTION_H4` | 四级标题 | 15px |
    | `SECTION_H5` | 五级标题 | 14px |
    """

    TITLE_LARGE = "title_large"
    TITLE_SMALL = "title_small"
    BODY = "body"
    CAPTION = "caption"
    SECTION_H2 = "section_h2"
    SECTION_H3 = "section_h3"
    SECTION_H4 = "section_h4"
    SECTION_H5 = "section_h5"


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


class SeparatorType(Enum):
    """分隔符类型枚举"""

    SOLID = "solid"  # 实线
    DASHED = "dashed"  # 虚线
    DOTTED = "dotted"  # 点线


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
