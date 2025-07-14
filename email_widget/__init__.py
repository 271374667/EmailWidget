"""EmailWidget - 强大的邮件组件库

这是一个现代化、易用的Python邮件组件库，让你轻松创建美观的HTML邮件报告。

主要功能：
- 丰富的Widget组件库
- 基于Jinja2的模板系统
- 支持matplotlib/seaborn图表
- 响应式设计
- 邮件客户端兼容

Examples:
    >>> from email_widget import Email, TextWidget, TableWidget
    >>> from email_widget import TextType, AlertType
    >>>
    >>> email = Email("每日报告")
    >>> email.add_widget(TextWidget().set_content("Hello").set_type(TextType.TITLE_LARGE))
    >>> email.export_html("report.html")
"""

# 核心类
# 基础类（供高级用户扩展使用）
from email_widget.core.base import BaseWidget

# 配置类
from email_widget.core.config import EmailConfig

# 枚举和类型
from email_widget.core.enums import (
    AlertType,
    IconType,
    LayoutType,
    LogLevel,
    ProgressTheme,
    SeparatorType,
    StatusType,
    TextAlign,
    TextType,
)

# 验证器系统（供高级用户使用）
from email_widget.core.validators import (
    BaseValidator,
    ChoicesValidator,
    ColorValidator,
    CompositeValidator,
    EmailValidator,
    LengthValidator,
    NonEmptyStringValidator,
    ProgressValidator,
    RangeValidator,
    SizeValidator,
    TypeValidator,
    UrlValidator,
)
from email_widget.email import Email

# 邮件发送器类
from email_widget.email_sender import (
    EmailSender,
    NetEaseEmailSender,
    QQEmailSender,
    create_email_sender,
)
from email_widget.widgets.alert_widget import AlertWidget
from email_widget.widgets.button_widget import ButtonWidget
from email_widget.widgets.card_widget import CardWidget
from email_widget.widgets.chart_widget import ChartWidget
from email_widget.widgets.checklist_widget import ChecklistWidget
from email_widget.widgets.circular_progress_widget import CircularProgressWidget
from email_widget.widgets.column_widget import ColumnWidget
from email_widget.widgets.image_widget import ImageWidget
from email_widget.widgets.log_widget import LogEntry, LogWidget
from email_widget.widgets.metric_widget import MetricWidget
from email_widget.widgets.progress_widget import ProgressWidget
from email_widget.widgets.quote_widget import QuoteWidget
from email_widget.widgets.separator_widget import SeparatorWidget
from email_widget.widgets.status_widget import StatusItem, StatusWidget
from email_widget.widgets.table_widget import TableCell, TableWidget

# 所有Widget组件
from email_widget.widgets.text_widget import TextWidget
from email_widget.widgets.timeline_widget import TimelineWidget

# 版本信息
__version__ = "0.22.1"
__author__ = "PythonImporter"
__email__ = "271374667@qq.com"

# 导出所有公共接口
__all__ = [
    # 核心类
    "Email",
    "BaseWidget",
    "EmailConfig",
    # 邮件发送器
    "EmailSender",
    "QQEmailSender",
    "NetEaseEmailSender",
    "create_email_sender",
    # Widget组件
    "TextWidget",
    "TableWidget",
    "TableCell",
    "ImageWidget",
    "ChartWidget",
    "AlertWidget",
    "ButtonWidget",
    "ChecklistWidget",
    "ProgressWidget",
    "CircularProgressWidget",
    "CardWidget",
    "MetricWidget",
    "StatusWidget",
    "StatusItem",
    "QuoteWidget",
    "SeparatorWidget",
    "TimelineWidget",
    "ColumnWidget",
    "LogWidget",
    "LogEntry",
    # 枚举类型
    "TextType",
    "TextAlign",
    "AlertType",
    "StatusType",
    "ProgressTheme",
    "SeparatorType",
    "LayoutType",
    "LogLevel",
    "IconType",
    # 验证器（供高级用户使用）
    "BaseValidator",
    "ColorValidator",
    "SizeValidator",
    "RangeValidator",
    "ProgressValidator",
    "UrlValidator",
    "EmailValidator",
    "NonEmptyStringValidator",
    "LengthValidator",
    "TypeValidator",
    "ChoicesValidator",
    "CompositeValidator",
    # 版本信息
    "__version__",
    "__author__",
    "__email__",
]
