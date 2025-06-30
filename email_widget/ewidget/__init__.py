"""EWidget - 面向对象的邮件HTML组件库

仿照QWidget设计的邮件HTML组件系统，支持Fluent Design风格
"""

from email_widget.ewidget.email import Email
from email_widget.ewidget.enums import (
    LogLevel, StatusType, AlertType, TextAlign, TextType,
    ProgressTheme, LayoutType, IconType
)
from email_widget.ewidget.widgets.table_widget import TableWidget, TableCell
from email_widget.ewidget.widgets.image_widget import ImageWidget
from email_widget.ewidget.widgets.log_widget import LogWidget, LogEntry
from email_widget.ewidget.widgets.alert_widget import AlertWidget
from email_widget.ewidget.widgets.text_widget import TextWidget
from email_widget.ewidget.widgets.progress_widget import ProgressWidget
from email_widget.ewidget.widgets.circular_progress_widget import CircularProgressWidget
from email_widget.ewidget.widgets.card_widget import CardWidget
from email_widget.ewidget.widgets.status_widget import StatusWidget
from email_widget.ewidget.widgets.quote_widget import QuoteWidget
from email_widget.ewidget.widgets.column_widget import ColumnWidget
from email_widget.ewidget.widgets.chart_widget import ChartWidget

__version__ = "0.1.0"
__author__ = "SpiderDaily"

__all__ = [
    # 主类
    "Email",
    
    # 枚举
    "LogLevel", "StatusType", "AlertType", "TextAlign", "TextType",
    "ProgressTheme", "LayoutType", "IconType",
    
    # Widget类
    "TableWidget", "TableCell",
    "ImageWidget",
    "LogWidget", "LogEntry",
    "AlertWidget",
    "TextWidget",
    "ProgressWidget",
    "CircularProgressWidget",
    "CardWidget",
    "StatusWidget",
    "QuoteWidget",
    "ColumnWidget",
    "ChartWidget",
] 