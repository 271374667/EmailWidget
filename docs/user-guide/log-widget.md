# LogWidget 日志组件

<div style="background: #f0f8ff; border: 1px solid #4a90e2; border-radius: 8px; padding: 20px; margin: 20px 0;">
  <h3 style="color: #2c5282; margin-top: 0;">📋 日志展示组件</h3>
  <div style="background: #1e1e1e; border: 1px solid #333333; border-radius: 4px; margin: 12px 0; padding: 16px; max-height: 300px; overflow-y: auto; font-family: 'Consolas', 'Monaco', 'Courier New', monospace; font-size: 13px; line-height: 1.4; color: #ffffff;">
    <h4 style="margin: 0 0 16px 0; font-size: 16px; font-weight: 600; color: #ffffff;">应用日志</h4>
    <div style="padding: 4px 0; margin: 2px 0; white-space: nowrap; color: #ffffff;">
      <span style="color: #888888; margin-right: 8px;">2024-01-15 10:30:25</span>
      <span style="color: #4fc3f7; font-weight: bold; margin-right: 8px;">[INFO]</span>
      <span style="color: #cccccc; margin-right: 8px;">(app.py:main:15)</span>
      <span style="color: #ffffff;">应用启动成功</span>
    </div>
    <div style="padding: 4px 0; margin: 2px 0; white-space: nowrap; color: #ffffff;">
      <span style="color: #888888; margin-right: 8px;">2024-01-15 10:30:26</span>
      <span style="color: #ffb74d; font-weight: bold; margin-right: 8px;">[WARNING]</span>
      <span style="color: #cccccc; margin-right: 8px;">(config.py:load:42)</span>
      <span style="color: #ffffff;">配置文件使用默认值</span>
    </div>
    <div style="padding: 4px 0; margin: 2px 0; white-space: nowrap; color: #ffffff;">
      <span style="color: #888888; margin-right: 8px;">2024-01-15 10:30:27</span>
      <span style="color: #f44336; font-weight: bold; margin-right: 8px;">[ERROR]</span>
      <span style="color: #cccccc; margin-right: 8px;">(db.py:connect:88)</span>
      <span style="color: #ffffff;">数据库连接失败</span>
    </div>
  </div>
  <div style="display: flex; gap: 10px; margin-top: 15px;">
    <span style="background: #e8f4fd; color: #0078d4; padding: 4px 8px; border-radius: 4px; font-size: 12px;">日志解析</span>
    <span style="background: #e8f4fd; color: #0078d4; padding: 4px 8px; border-radius: 4px; font-size: 12px;">级别过滤</span>
    <span style="background: #e8f4fd; color: #0078d4; padding: 4px 8px; border-radius: 4px; font-size: 12px;">深色主题</span>
  </div>
</div>

LogWidget是一个专业的日志展示组件，支持自动解析loguru格式的日志，提供级别过滤、深色主题和滚动显示等功能。它是开发调试和运维监控的重要工具。

## 🎯 主要功能

### 日志解析
- **自动解析**：支持loguru标准格式的日志解析
- **手动添加**：支持手动添加日志条目
- **批量处理**：支持批量设置日志列表
- **格式识别**：自动识别时间戳、级别、模块等信息

### 显示控制
- **级别过滤**：支持按日志级别过滤显示
- **元素控制**：可选择显示时间戳、级别、来源信息
- **高度限制**：可设置最大显示高度，超出部分滚动
- **深色主题**：专业的深色背景，适合长时间查看

### 日志级别
- **DEBUG**：调试信息（灰色）
- **INFO**：一般信息（蓝色）
- **WARNING**：警告信息（橙色）
- **ERROR**：错误信息（红色）
- **CRITICAL**：严重错误（深红色）

## 📋 核心方法

### 基础使用

```python
from email_widget.widgets import LogWidget
from email_widget.core.enums import LogLevel

# 创建日志组件
log = LogWidget()

# 设置标题
log.set_title("应用日志")

# 添加日志条目
log.add_log_entry("应用启动成功", LogLevel.INFO)
log.add_log_entry("配置文件加载完成", LogLevel.DEBUG)
log.add_log_entry("数据库连接失败", LogLevel.ERROR)
```

### 日志管理方法

```python
# 添加单条日志条目
log.add_log_entry(message, level, timestamp, module, function, line_number)

# 追加loguru格式日志
log.append_log("2024-01-15 10:30:25.123 | INFO | app:main:15 - 应用启动")

# 批量设置日志
log_lines = [
    "2024-01-15 10:30:25.123 | INFO | app:main:15 - 应用启动",
    "2024-01-15 10:30:26.456 | WARNING | config:load:42 - 使用默认配置"
]
log.set_logs(log_lines)

# 清空日志
log.clear()
```

### 显示配置

```python
# 设置显示选项
log.show_timestamp(True)    # 显示时间戳
log.show_level(True)        # 显示日志级别
log.show_source(True)       # 显示来源信息

# 设置过滤级别
log.filter_by_level(LogLevel.WARNING)  # 只显示WARNING及以上级别

# 设置最大高度
log.set_max_height("400px")
```

## 💡 实用示例

### 应用启动日志

```python
from email_widget.widgets import LogWidget
from email_widget.core.enums import LogLevel
from datetime import datetime

# 创建应用启动日志
startup_log = LogWidget()
startup_log.set_title("应用启动日志")

# 添加启动过程日志
startup_log.add_log_entry("开始启动应用", LogLevel.INFO, datetime.now())
startup_log.add_log_entry("加载配置文件", LogLevel.DEBUG, datetime.now())
startup_log.add_log_entry("初始化数据库连接", LogLevel.INFO, datetime.now())
startup_log.add_log_entry("启动Web服务器", LogLevel.INFO, datetime.now())
startup_log.add_log_entry("应用启动完成", LogLevel.INFO, datetime.now())

# 渲染日志
html = startup_log.render_html()
```

### 错误日志监控

```python
# 创建错误日志监控
error_log = LogWidget()
error_log.set_title("错误日志监控")
error_log.filter_by_level(LogLevel.ERROR)  # 只显示错误级别

# 添加错误日志
error_log.add_log_entry(
    "数据库连接超时",
    LogLevel.ERROR,
    datetime.now(),
    "database",
    "connect",
    88
)

error_log.add_log_entry(
    "API请求失败",
    LogLevel.ERROR,
    datetime.now(),
    "api",
    "request",
    156
)
```

### loguru格式日志解析

```python
# 解析loguru格式日志
loguru_log = LogWidget()
loguru_log.set_title("Loguru日志解析")

# loguru格式的日志字符串
loguru_logs = [
    "2024-01-15 10:30:25.123 | DEBUG | app:main:15 - 调试信息",
    "2024-01-15 10:30:26.456 | INFO | config:load:42 - 配置加载完成",
    "2024-01-15 10:30:27.789 | WARNING | db:connect:88 - 数据库连接慢",
    "2024-01-15 10:30:28.012 | ERROR | api:request:156 - API请求失败",
    "2024-01-15 10:30:29.345 | CRITICAL | system:crash:200 - 系统崩溃"
]

# 批量设置日志
loguru_log.set_logs(loguru_logs)
```

### 实时日志监控

```python
# 创建实时日志监控器
class RealTimeLogMonitor:
    def __init__(self):
        self.log_widget = LogWidget()
        self.log_widget.set_title("实时日志监控")
        self.log_widget.set_max_height("500px")
        self.max_entries = 100  # 最大日志条目数
    
    def add_log(self, message, level=LogLevel.INFO):
        # 添加新日志
        self.log_widget.add_log_entry(message, level, datetime.now())
        
        # 限制日志条目数量
        if len(self.log_widget.logs) > self.max_entries:
            # 移除最旧的日志（这里简化处理）
            self.log_widget.clear()
            # 实际应用中可能需要更复杂的队列管理
    
    def get_html(self):
        return self.log_widget.render_html()

# 使用实时监控器
monitor = RealTimeLogMonitor()
monitor.add_log("系统启动", LogLevel.INFO)
monitor.add_log("用户登录", LogLevel.INFO)
monitor.add_log("权限验证失败", LogLevel.WARNING)
```

### 分级日志展示

```python
# 创建分级日志展示
from email_widget.widgets import ColumnWidget

# 创建不同级别的日志组件
info_log = LogWidget()
info_log.set_title("信息日志")
info_log.filter_by_level(LogLevel.INFO)
info_log.show_level(False)  # 隐藏级别标识

warning_log = LogWidget()
warning_log.set_title("警告日志")
warning_log.filter_by_level(LogLevel.WARNING)
warning_log.show_level(False)

error_log = LogWidget()
error_log.set_title("错误日志")
error_log.filter_by_level(LogLevel.ERROR)
error_log.show_level(False)

# 添加日志到不同组件
logs = [
    ("应用启动成功", LogLevel.INFO),
    ("配置文件缺失", LogLevel.WARNING),
    ("数据库连接失败", LogLevel.ERROR),
    ("用户登录成功", LogLevel.INFO),
    ("磁盘空间不足", LogLevel.WARNING)
]

for message, level in logs:
    if level == LogLevel.INFO:
        info_log.add_log_entry(message, level)
    elif level == LogLevel.WARNING:
        warning_log.add_log_entry(message, level)
    elif level == LogLevel.ERROR:
        error_log.add_log_entry(message, level)

# 使用列布局组合显示
column = ColumnWidget().set_columns(3)
column.add_widgets([info_log, warning_log, error_log])
```

## 📊 日志级别详解

### 级别说明

| 级别 | 颜色 | 适用场景 |
|------|------|----------|
| `DEBUG` | 灰色 | 调试信息、详细追踪 |
| `INFO` | 蓝色 | 一般信息、正常流程 |
| `WARNING` | 橙色 | 警告信息、需要注意 |
| `ERROR` | 红色 | 错误信息、功能异常 |
| `CRITICAL` | 深红色 | 严重错误、系统崩溃 |

### 级别过滤

```python
# 设置不同的过滤级别
log.filter_by_level(LogLevel.DEBUG)    # 显示所有级别
log.filter_by_level(LogLevel.INFO)     # 显示INFO及以上
log.filter_by_level(LogLevel.WARNING)  # 显示WARNING及以上
log.filter_by_level(LogLevel.ERROR)    # 只显示ERROR和CRITICAL
log.filter_by_level(LogLevel.CRITICAL) # 只显示CRITICAL
```

## 🎨 最佳实践

### 1. 日志级别管理

```python
# 根据环境设置不同的日志级别
def create_environment_log(env="production"):
    log = LogWidget()
    
    if env == "development":
        log.filter_by_level(LogLevel.DEBUG)  # 开发环境显示所有
    elif env == "testing":
        log.filter_by_level(LogLevel.INFO)   # 测试环境显示INFO及以上
    else:
        log.filter_by_level(LogLevel.WARNING) # 生产环境只显示警告及以上
    
    return log
```

### 2. 日志条目限制

```python
# 限制日志条目数量以提高性能
class LimitedLogWidget(LogWidget):
    def __init__(self, max_entries=50):
        super().__init__()
        self.max_entries = max_entries
    
    def add_log_entry(self, *args, **kwargs):
        super().add_log_entry(*args, **kwargs)
        
        # 限制条目数量
        if len(self._logs) > self.max_entries:
            self._logs = self._logs[-self.max_entries:]
```

### 3. 日志格式化

```python
# 自定义日志格式化
def format_log_message(level, module, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"{timestamp} | {level.value} | {module} - {message}"

# 使用格式化函数
log = LogWidget()
formatted_message = format_log_message(LogLevel.INFO, "app", "应用启动")
log.append_log(formatted_message)
```

### 4. 日志搜索和过滤

```python
# 实现日志搜索功能
def search_logs(log_widget, keyword):
    matching_logs = []
    for log_entry in log_widget.logs:
        if keyword.lower() in log_entry.message.lower():
            matching_logs.append(log_entry)
    
    # 创建新的日志组件显示搜索结果
    result_log = LogWidget()
    result_log.set_title(f"搜索结果: {keyword}")
    result_log._logs = matching_logs
    
    return result_log
```

## 🔧 常见问题

### Q: 如何处理大量日志数据？
A: 设置合理的最大高度和日志条目限制，使用级别过滤减少显示内容。

### Q: 日志时间格式可以自定义吗？
A: 目前使用固定格式，如需自定义可以在添加日志条目时预先格式化。

### Q: 如何实现日志的实时更新？
A: 通过定期调用`add_log_entry()`或`append_log()`方法来添加新日志。

### Q: 日志组件支持导出功能吗？
A: 可以通过访问`logs`属性获取日志数据，然后自行实现导出功能。

LogWidget为您提供了专业的日志展示解决方案，让日志监控和问题排查变得更加高效！ 