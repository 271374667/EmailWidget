# LogWidget

LogWidget is a professional log display component that supports automatic parsing of loguru format logs, providing level filtering, dark themes, and scrolling display features. It is an important tool for development debugging and operation monitoring, capable of clearly displaying system running status and troubleshooting information.

## 🎯 Widget Preview

--8<-- "assets/log_widget_component_preview.html"

## ✨ Core Features

- **📝 Log Parsing**: Supports automatic log parsing in loguru standard format
- **🎨 Level Filtering**: Supports filtering display by log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- **🎭 Dark Theme**: Professional dark background, suitable for long-term viewing
- **📏 Scrolling Display**: Can set maximum height, excess content scrolls automatically
- **⚙️ Flexible Configuration**: Optional display of timestamps, level identifiers, source information
- **📧 Email Compatible**: Implemented using email client-compatible HTML and CSS

## 🚀 Quick Start

### Basic Usage

```python
from email_widget import Email
from email_widget.widgets import LogWidget
from email_widget.core.enums import LogLevel

# Create log widget
log = LogWidget()
log.set_title("Application Log")
log.add_log_entry("Application started successfully", LogLevel.INFO)
log.add_log_entry("Configuration file loaded", LogLevel.DEBUG)
log.add_log_entry("Database connection failed", LogLevel.ERROR)

email = Email("System Log Report")
email.add_widget(log)
```

### Advanced Usage

```python
# Parse loguru format logs
log = LogWidget()
log.set_title("System Running Log")

# loguru format log strings
loguru_logs = [
    "2024-01-15 10:30:25.123 | DEBUG | app:main:15 - Debug information",
    "2024-01-15 10:30:26.456 | INFO | config:load:42 - Configuration loaded",
    "2024-01-15 10:30:27.789 | WARNING | db:connect:88 - Database connection slow",
    "2024-01-15 10:30:28.012 | ERROR | api:request:156 - API request failed"
]

log.set_logs(loguru_logs)
log.filter_by_level(LogLevel.WARNING)  # Only show WARNING and above levels
log.show_timestamp(True)
log.set_max_height("400px")

email.add_widget(log)
```

📚 **Complete API Documentation**: [LogWidget API](../api/log-widget.md)

## 🎨 Style Guide

### Log Levels and Colors

- **DEBUG**: Gray (#888888) - Debug information, detailed tracking
- **INFO**: Blue (#4fc3f7) - General information, normal flow
- **WARNING**: Orange (#ffb74d) - Warning information, needs attention
- **ERROR**: Red (#f44336) - Error information, functional anomalies
- **CRITICAL**: Dark red (#d32f2f) - Severe errors, system crashes

### Filter Level Description

Setting filter level will display that level and all higher levels:
- `LogLevel.DEBUG`: Show all levels
- `LogLevel.INFO`: Show INFO and above (INFO, WARNING, ERROR, CRITICAL)
- `LogLevel.WARNING`: Show WARNING and above (WARNING, ERROR, CRITICAL)
- `LogLevel.ERROR`: Only show ERROR and CRITICAL

## 📱 Best Practices

### 1. Application Startup Log

```python
from email_widget import Email
from email_widget.widgets import LogWidget
from email_widget.core.enums import LogLevel
from datetime import datetime

email = Email("Application Startup Report")

# Startup process log
startup_log = LogWidget()
startup_log.set_title("Application Startup Log")
startup_log.add_log_entry("Starting application", LogLevel.INFO, datetime.now())
startup_log.add_log_entry("Loading configuration file", LogLevel.DEBUG, datetime.now())
startup_log.add_log_entry("Initializing database connection", LogLevel.INFO, datetime.now())
startup_log.add_log_entry("Starting web server", LogLevel.INFO, datetime.now())
startup_log.add_log_entry("Application startup complete", LogLevel.INFO, datetime.now())
startup_log.show_timestamp(True)

email.add_widget(startup_log)
```

--8<-- "assets/temp/log_application_startup.html"

### 2. Error Log Monitoring

```python
from email_widget import Email
from email_widget.widgets import LogWidget
from email_widget.core.enums import LogLevel

email = Email("Error Log Report")

# Only show error level logs
error_log = LogWidget()
error_log.set_title("Error Log Monitoring")
error_log.filter_by_level(LogLevel.ERROR)  # Only show ERROR and CRITICAL

# Add error logs
error_log.add_log_entry("Database connection timeout", LogLevel.ERROR, datetime.now(), "database", "connect", 88)
error_log.add_log_entry("API request failed", LogLevel.ERROR, datetime.now(), "api", "request", 156)
error_log.add_log_entry("System memory insufficient", LogLevel.CRITICAL, datetime.now(), "system", "memory", 200)

error_log.show_timestamp(True)
error_log.show_source(True)
error_log.set_max_height("300px")

email.add_widget(error_log)
```

--8<-- "assets/temp/log_error_monitoring.html"

### 3. System Operations Log

```python
from email_widget import Email
from email_widget.widgets import LogWidget

email = Email("System Operations Daily Report")

# System event log
ops_log = LogWidget()
ops_log.set_title("Operations Event Log")

# Batch set loguru format logs
ops_logs = [
    "2024-01-15 08:00:00 | INFO | system:startup:10 - Server startup complete",
    "2024-01-15 12:00:00 | INFO | backup:auto:25 - Database auto backup complete",
    "2024-01-15 14:30:00 | WARNING | monitor:memory:45 - Memory usage reached 85%",
    "2024-01-15 15:45:00 | ERROR | service:redis:88 - Redis connection timeout",
    "2024-01-15 16:15:00 | INFO | service:redis:92 - Redis service restarted, connection restored"
]

ops_log.set_logs(ops_logs)
ops_log.show_timestamps(True)
ops_log.set_reverse_order(True)  # Latest logs first
ops_log.set_max_height("500px")

email.add_widget(ops_log)
```

--8<-- "assets/temp/log_system_operations.html"

## ⚡ Shortcut Methods

The Email class provides the `add_log` shortcut method:

```python
# Quick add log widget
email.add_log(
    title="System Log",
    logs=[
        ("Application started", "info"),
        ("Configuration loaded", "debug"),
        ("Connection error", "error")
    ],
    show_time=True,
    max_height="400px"
)

# Add loguru format logs
email.add_log(
    title="Running Log",
    loguru_logs=[
        "2024-01-15 10:30:25 | INFO | app:main:15 - Application running normally",
        "2024-01-15 10:30:26 | WARNING | db:query:42 - Query taking too long"
    ],
    filter_level="warning"
)
```

## 🐛 Common Issues

### Q: How to handle large amounts of log data?
A: Set reasonable maximum height and log entry limits:
```python
log.set_max_height("400px")
log.filter_by_level(LogLevel.WARNING)  # Only show important logs
```

### Q: Can log time format be customized?
A: Currently uses fixed format, can pre-format when adding:
```python
formatted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log.add_log_entry("Message", LogLevel.INFO, formatted_time)
```

### Q: How to implement real-time log updates?
A: Achieved by periodically calling add methods:
```python
# Periodically add new logs
log.add_log_entry("New event", LogLevel.INFO)
log.append_log("2024-01-15 10:30:25 | INFO | app:event:15 - New event occurred")
```

### Q: How to search logs with specific content?
A: Filter content before adding:
```python
keyword = "database"
if keyword in log_message:
    log.add_log_entry(log_message, LogLevel.INFO)
```

## 🔗 Related Widgets

- [StatusWidget](status-widget.md) - System status information display
- [AlertWidget](alert-widget.md) - Important log alert information
- [TextWidget](text-widget.md) - Simple text log display
- [CardWidget](card-widget.md) - Card that can contain logs
- [ColumnWidget](column-widget.md) - Used for laying out multiple log widgets