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

# 创建日志组件
log = LogWidget()
log.set_title("应用日志")
log.add_log_entry("应用启动成功", LogLevel.INFO)
log.add_log_entry("配置文件加载完成", LogLevel.DEBUG)
log.add_log_entry("数据库连接失败", LogLevel.ERROR)

email = Email("系统日志报告")
email.add_widget(log)
```

### Advanced Usage

```python
# 解析loguru格式日志
log = LogWidget()
log.set_title("系统运行日志")

# loguru格式的日志字符串
loguru_logs = [
    "2024-01-15 10:30:25.123 | DEBUG | app:main:15 - 调试信息",
    "2024-01-15 10:30:26.456 | INFO | config:load:42 - 配置加载完成",
    "2024-01-15 10:30:27.789 | WARNING | db:connect:88 - 数据库连接慢",
    "2024-01-15 10:30:28.012 | ERROR | api:request:156 - API请求失败"
]

log.set_logs(loguru_logs)
log.filter_by_level(LogLevel.WARNING)  # 只显示WARNING及以上级别
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

email = Email("应用启动报告")

# 启动过程日志
startup_log = LogWidget()
startup_log.set_title("应用启动日志")
startup_log.add_log_entry("开始启动应用", LogLevel.INFO, datetime.now())
startup_log.add_log_entry("加载配置文件", LogLevel.DEBUG, datetime.now())
startup_log.add_log_entry("初始化数据库连接", LogLevel.INFO, datetime.now())
startup_log.add_log_entry("启动Web服务器", LogLevel.INFO, datetime.now())
startup_log.add_log_entry("应用启动完成", LogLevel.INFO, datetime.now())
startup_log.show_timestamp(True)

email.add_widget(startup_log)
```

--8<-- "assets/temp/log_application_startup.html"

### 2. Error Log Monitoring

```python
from email_widget import Email
from email_widget.widgets import LogWidget
from email_widget.core.enums import LogLevel

email = Email("错误日志报告")

# 只显示错误级别日志
error_log = LogWidget()
error_log.set_title("错误日志监控")
error_log.filter_by_level(LogLevel.ERROR)  # 只显示ERROR和CRITICAL

# 添加错误日志
error_log.add_log_entry("数据库连接超时", LogLevel.ERROR, datetime.now(), "database", "connect", 88)
error_log.add_log_entry("API请求失败", LogLevel.ERROR, datetime.now(), "api", "request", 156)
error_log.add_log_entry("系统内存不足", LogLevel.CRITICAL, datetime.now(), "system", "memory", 200)

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

email = Email("系统运维日报")

# 系统事件日志
ops_log = LogWidget()
ops_log.set_title("运维事件日志")

# 批量设置loguru格式日志
ops_logs = [
    "2024-01-15 08:00:00 | INFO | system:startup:10 - 服务器启动完成",
    "2024-01-15 12:00:00 | INFO | backup:auto:25 - 数据库自动备份完成",
    "2024-01-15 14:30:00 | WARNING | monitor:memory:45 - 内存使用率达到85%",
    "2024-01-15 15:45:00 | ERROR | service:redis:88 - Redis连接超时",
    "2024-01-15 16:15:00 | INFO | service:redis:92 - Redis服务重启，连接恢复"
]

ops_log.set_logs(ops_logs)
ops_log.show_timestamps(True)
ops_log.set_reverse_order(True)  # 最新日志在前
ops_log.set_max_height("500px")

email.add_widget(ops_log)
```

--8<-- "assets/temp/log_system_operations.html"

## ⚡ Shortcut Methods

The Email class provides the `add_log` shortcut method:

```python
# 快捷添加日志组件
email.add_log(
    title="系统日志",
    logs=[
        ("应用启动", "info"),
        ("配置加载", "debug"),
        ("连接异常", "error")
    ],
    show_time=True,
    max_height="400px"
)

# 添加loguru格式日志
email.add_log(
    title="运行日志",
    loguru_logs=[
        "2024-01-15 10:30:25 | INFO | app:main:15 - 应用运行正常",
        "2024-01-15 10:30:26 | WARNING | db:query:42 - 查询耗时较长"
    ],
    filter_level="warning"
)
```

## 🐛 Common Issues

### Q: How to handle large amounts of log data?
A: Set reasonable maximum height and log entry limits:
```python
log.set_max_height("400px")
log.filter_by_level(LogLevel.WARNING)  # 只显示重要日志
```

### Q: Can log time format be customized?
A: Currently uses fixed format, can pre-format when adding:
```python
formatted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log.add_log_entry("消息", LogLevel.INFO, formatted_time)
```

### Q: How to implement real-time log updates?
A: Achieved by periodically calling add methods:
```python
# 定期添加新日志
log.add_log_entry("新事件", LogLevel.INFO)
log.append_log("2024-01-15 10:30:25 | INFO | app:event:15 - 新事件发生")
```

### Q: How to search logs with specific content?
A: Filter content before adding:
```python
keyword = "数据库"
if keyword in log_message:
    log.add_log_entry(log_message, LogLevel.INFO)
```

## 🔗 Related Widgets

- [StatusWidget](status-widget.md) - System status information display
- [AlertWidget](alert-widget.md) - Important log alert information
- [TextWidget](text-widget.md) - Simple text log display
- [CardWidget](card-widget.md) - Card that can contain logs
- [ColumnWidget](column-widget.md) - Used for laying out multiple log widgets