# LogWidget 日志组件

LogWidget是一个专业的日志展示组件，支持自动解析loguru格式的日志，提供级别过滤、深色主题和滚动显示等功能。它是开发调试和运维监控的重要工具，能够清晰地展示系统运行状态和问题排查信息。

## 🎯 组件预览

--8<-- "assets/log_widget_component_preview.html"

## ✨ 核心特性

- **📝 日志解析**: 支持loguru标准格式的自动日志解析
- **🎨 级别过滤**: 支持按日志级别过滤显示（DEBUG、INFO、WARNING、ERROR、CRITICAL）
- **🎭 深色主题**: 专业的深色背景，适合长时间查看
- **📏 滚动显示**: 可设置最大高度，超出部分自动滚动
- **⚙️ 灵活配置**: 可选择显示时间戳、级别标识、来源信息
- **📧 邮件兼容**: 使用邮件客户端兼容的HTML和CSS实现

## 🚀 快速开始

### 基础用法

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

### 进阶用法

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

📚 **完整API文档**: [LogWidget API](../api/log-widget.md)

## 🎨 样式指南

### 日志级别和颜色

- **DEBUG**: 灰色 (#888888) - 调试信息、详细追踪
- **INFO**: 蓝色 (#4fc3f7) - 一般信息、正常流程
- **WARNING**: 橙色 (#ffb74d) - 警告信息、需要注意
- **ERROR**: 红色 (#f44336) - 错误信息、功能异常
- **CRITICAL**: 深红色 (#d32f2f) - 严重错误、系统崩溃

### 过滤级别说明

设置过滤级别会显示该级别及以上的所有日志：
- `LogLevel.DEBUG`: 显示所有级别
- `LogLevel.INFO`: 显示INFO及以上（INFO、WARNING、ERROR、CRITICAL）
- `LogLevel.WARNING`: 显示WARNING及以上（WARNING、ERROR、CRITICAL）
- `LogLevel.ERROR`: 只显示ERROR和CRITICAL

## 📱 最佳实践

### 1. 应用启动日志

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

### 2. 错误日志监控

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

### 3. 系统运维日志

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

## ⚡ 快捷方法

Email 类提供了 `add_log` 快捷方法：

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

## 🐛 常见问题

### Q: 如何处理大量日志数据？
A: 设置合理的最大高度和日志条目限制：
```python
log.set_max_height("400px")
log.filter_by_level(LogLevel.WARNING)  # 只显示重要日志
```

### Q: 日志时间格式可以自定义吗？
A: 目前使用固定格式，可以在添加时预先格式化：
```python
formatted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log.add_log_entry("消息", LogLevel.INFO, formatted_time)
```

### Q: 如何实现日志的实时更新？
A: 通过定期调用添加方法来实现：
```python
# 定期添加新日志
log.add_log_entry("新事件", LogLevel.INFO)
log.append_log("2024-01-15 10:30:25 | INFO | app:event:15 - 新事件发生")
```

### Q: 如何搜索特定内容的日志？
A: 在添加前进行内容过滤：
```python
keyword = "数据库"
if keyword in log_message:
    log.add_log_entry(log_message, LogLevel.INFO)
```

## 🔗 相关组件

- [StatusWidget](status-widget.md) - 系统状态信息展示
- [AlertWidget](alert-widget.md) - 重要日志提醒信息
- [TextWidget](text-widget.md) - 简单文本日志显示
- [CardWidget](card-widget.md) - 可以包含日志的卡片
- [ColumnWidget](column-widget.md) - 用于布局多个日志组件