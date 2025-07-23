"""EmailWidget - Powerful Email Component Library

A modern, easy-to-use Python email component library that allows you to effortlessly create beautiful HTML email reports.

Key Features:
- Rich widget component library
- Jinja2-based template system
- Support for matplotlib/seaborn charts
- Responsive design
- Email client compatibility

Examples:
    >>> from email_widget import Email, TextWidget, TableWidget
    >>> from email_widget import TextType, AlertType
    >>>
    >>> email = Email("Daily Report")
    >>> email.add_widget(TextWidget().set_content("Hello").set_type(TextType.TITLE_LARGE))
    >>> email.export_html("report.html")
"""

# Core classes
# Base classes (for advanced users to extend)
from email_widget.core.base import BaseWidget

# Configuration classes
from email_widget.core.config import EmailConfig

# Enums and types
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

# Validator system (for advanced users)
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

# Email sender classes
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

# All widget components
from email_widget.widgets.text_widget import TextWidget
from email_widget.widgets.timeline_widget import TimelineWidget

# Version information
__version__ = "0.23.1"
__author__ = "PythonImporter"
__email__ = "271374667@qq.com"

# Export all public interfaces
__all__ = [
    # Core classes
    "Email",
    "BaseWidget",
    "EmailConfig",
    # Email senders
    "EmailSender",
    "QQEmailSender",
    "NetEaseEmailSender",
    "create_email_sender",
    # Widget components
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
    # Enum types
    "TextType",
    "TextAlign",
    "AlertType",
    "StatusType",
    "ProgressTheme",
    "SeparatorType",
    "LayoutType",
    "LogLevel",
    "IconType",
    # Validators (for advanced users)
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
    # Version information
    "__version__",
    "__author__",
    "__email__",
]
