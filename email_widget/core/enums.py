"""Enum class definition module"""

from enum import Enum


class LogLevel(Enum):
    """Log level enumeration"""

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class StatusType(Enum):
    """Status type enumeration"""

    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"
    INFO = "info"
    PRIMARY = "primary"


class AlertType(Enum):
    """Alert type enumeration"""

    NOTE = "note"
    TIP = "tip"
    IMPORTANT = "important"
    WARNING = "warning"
    CAUTION = "caution"


class TextAlign(Enum):
    """Text alignment enumeration.

    | Enum Value | Description |
    |------------|-------------|
    | `LEFT` | Left alignment |
    | `CENTER` | Center alignment |
    | `RIGHT` | Right alignment |
    | `JUSTIFY` | Justified alignment |
    """

    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"


class TextType(Enum):
    """Text type enumeration, defining different text styles and semantic levels.

    | Enum Value | Description | Default Font Size |
    |------------|-------------|------------------|
    | `TITLE_LARGE` | Large title | 24px |
    | `TITLE_SMALL` | Small title | 20px |
    | `BODY` | Body text | 14px |
    | `CAPTION` | Caption text | 12px |
    | `SECTION_H2` | Second-level heading | 18px |
    | `SECTION_H3` | Third-level heading | 16px |
    | `SECTION_H4` | Fourth-level heading | 15px |
    | `SECTION_H5` | Fifth-level heading | 14px |
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
    """Progress bar theme enumeration"""

    PRIMARY = "primary"
    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"
    INFO = "info"


class LayoutType(Enum):
    """Layout type enumeration"""

    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"


class SeparatorType(Enum):
    """Separator type enumeration"""

    SOLID = "solid"  # Solid line
    DASHED = "dashed"  # Dashed line
    DOTTED = "dotted"  # Dotted line


class IconType(Enum):
    """Icon type enumeration - Common icons for web scraping and data processing"""

    # Data-related
    DATA = "📊"
    DATABASE = "🗄️"
    CHART = "📈"
    TABLE = "📋"
    REPORT = "📄"

    # Web scraping-related
    SPIDER = "🕷️"
    WEB = "🌐"
    LINK = "🔗"
    SEARCH = "🔍"
    DOWNLOAD = "⬇️"

    # System-related
    SERVER = "🖥️"
    NETWORK = "🌐"
    STORAGE = "💾"
    MEMORY = "🧠"
    CPU = "⚡"

    # Status-related
    SUCCESS = "✅"
    ERROR = "❌"
    WARNING = "⚠️"
    INFO = "ℹ️"
    PROCESSING = "⚙️"

    # Default icon
    DEFAULT = "📋"
