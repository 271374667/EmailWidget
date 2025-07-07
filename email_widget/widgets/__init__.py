"""EWidget组件模块"""

from email_widget.widgets.alert_widget import AlertWidget
from email_widget.widgets.card_widget import CardWidget
from email_widget.widgets.chart_widget import ChartWidget
from email_widget.widgets.circular_progress_widget import CircularProgressWidget
from email_widget.widgets.column_widget import ColumnWidget
from email_widget.widgets.image_widget import ImageWidget
from email_widget.widgets.log_widget import LogEntry, LogWidget
from email_widget.widgets.progress_widget import ProgressWidget
from email_widget.widgets.quote_widget import QuoteWidget
from email_widget.widgets.status_widget import StatusWidget
from email_widget.widgets.table_widget import TableCell, TableWidget
from email_widget.widgets.text_widget import TextWidget

__all__ = [
    "TableWidget",
    "TableCell",
    "ImageWidget",
    "LogWidget",
    "LogEntry",
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
