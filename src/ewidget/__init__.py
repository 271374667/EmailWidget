"""EWidget - 面向对象的邮件HTML组件库

仿照QWidget设计的邮件HTML组件系统，支持Fluent Design风格
"""

from src.ewidget.email import Email
from src.ewidget.enums import (
    LogLevel, StatusType, AlertType, TextAlign, TextType,
    ProgressTheme, LayoutType, IconType
)
from src.ewidget.widgets.table_widget import TableWidget, TableCell
from src.ewidget.widgets.image_widget import ImageWidget
from src.ewidget.widgets.log_widget import LogWidget, LogEntry
from src.ewidget.widgets.alert_widget import AlertWidget
from src.ewidget.widgets.text_widget import TextWidget
from src.ewidget.widgets.progress_widget import ProgressWidget
from src.ewidget.widgets.circular_progress_widget import CircularProgressWidget
from src.ewidget.widgets.card_widget import CardWidget
from src.ewidget.widgets.status_widget import StatusWidget
from src.ewidget.widgets.quote_widget import QuoteWidget
from src.ewidget.widgets.column_widget import ColumnWidget
from src.ewidget.widgets.chart_widget import ChartWidget

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