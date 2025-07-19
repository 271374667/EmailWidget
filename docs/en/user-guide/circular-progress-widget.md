# CircularProgressWidget

CircularProgressWidget is a component for displaying circular progress bars, providing a more compact visual effect than linear progress bars, suitable for showing progress information in limited spaces. It supports multiple theme colors, size settings, and progress management functions, making it ideal for system monitoring and task progress display.

## 🎯 Widget Preview

--8<-- "assets/circular_progress_widget_component_preview.html"

## ✨ Core Features

- **🎨 Multiple Themes**: Supports PRIMARY, SUCCESS, WARNING, ERROR, INFO and other theme colors
- **📊 Progress Management**: Supports value setting, increment/decrement operations, completion reset and other convenient functions
- **🔧 Style Customization**: Flexible size control, line width, label display settings
- **📈 Non-percentage**: Supports custom maximum values, not limited to percentage display
- **⚡ Convenient Operations**: Provides increment, decrement, complete, reset and other shortcut methods
- **📧 Email Compatible**: Implemented using email client-compatible HTML and CSS

## 🚀 Quick Start

### Basic Usage

```python
from email_widget import Email
from email_widget.widgets import CircularProgressWidget
from email_widget.core.enums import ProgressTheme

# 创建基础圆形进度条
progress = CircularProgressWidget()
progress.set_value(65)
progress.set_label("下载进度")
progress.set_theme(ProgressTheme.PRIMARY)

email = Email("进度报告")
email.add_widget(progress)
```

### Advanced Usage

```python
# 系统监控指标组合
from email_widget.widgets import ColumnWidget

email = Email("系统监控仪表板")

# CPU使用率
cpu_progress = (CircularProgressWidget()
                .set_value(35)
                .set_label("CPU使用率")
                .set_theme(ProgressTheme.SUCCESS)
                .set_size("100px")
                .set_stroke_width("8px"))

# 内存使用率
memory_progress = (CircularProgressWidget()
                   .set_value(68)
                   .set_label("内存使用率")
                   .set_theme(ProgressTheme.WARNING)
                   .set_size("100px")
                   .set_stroke_width("8px"))

# 磁盘使用率
disk_progress = (CircularProgressWidget()
                 .set_value(85)
                 .set_label("磁盘使用率")
                 .set_theme(ProgressTheme.ERROR)
                 .set_size("100px")
                 .set_stroke_width("8px"))

# 使用列布局组合
column = ColumnWidget().set_columns(3)
column.add_widgets([cpu_progress, memory_progress, disk_progress])
email.add_widget(column)
```

📚 **Complete API Documentation**: [CircularProgressWidget API](../api/circular-progress-widget.md)

## 🎨 Style Guide

### Theme Colors and Application Scenarios

- **PRIMARY**: Blue (#0078d4) - Main progress, important metrics
- **SUCCESS**: Green (#107c10) - Normal status, successful completion
- **WARNING**: Orange (#ff8c00) - Needs attention, approaching threshold
- **ERROR**: Red (#d13438) - Error status, exceeding limits
- **INFO**: Blue (#0078d4) - Information display, reference data

### Size Specifications Recommendations

- **Small Metrics**: 60px - 80px, suitable for integrated display
- **Regular Metrics**: 100px - 120px, suitable for main display
- **Important Metrics**: 150px - 200px, suitable for prominent display
- **Line Width**: 4-6px for small sizes, 8-12px for large sizes

## 📱 Best Practices

### 1. System Resource Monitoring

```python
from email_widget import Email
from email_widget.widgets import CircularProgressWidget, ColumnWidget
from email_widget.core.enums import ProgressTheme

email = Email("系统资源监控")

# 根据数值选择合适主题
def get_theme_by_value(value):
    if value < 50:
        return ProgressTheme.SUCCESS
    elif value < 80:
        return ProgressTheme.WARNING
    else:
        return ProgressTheme.ERROR

# 创建监控指标
metrics = [
    {"label": "CPU", "value": 45, "size": "80px"},
    {"label": "内存", "value": 72, "size": "80px"},
    {"label": "网络", "value": 28, "size": "80px"},
    {"label": "磁盘", "value": 91, "size": "80px"}
]

progress_widgets = []
for metric in metrics:
    progress = (CircularProgressWidget()
                .set_value(metric["value"])
                .set_label(metric["label"])
                .set_theme(get_theme_by_value(metric["value"]))
                .set_size(metric["size"])
                .set_stroke_width("6px"))
    progress_widgets.append(progress)

# 使用4列布局
dashboard = ColumnWidget().set_columns(4)
dashboard.add_widgets(progress_widgets)
email.add_widget(dashboard)
```

--8<-- "assets/temp/circular_progress_system_monitoring.html"

### 2. Project Progress Display

```python
from email_widget import Email
from email_widget.widgets import CircularProgressWidget
from email_widget.core.enums import ProgressTheme

email = Email("项目进度报告")

# 主要项目进度
main_progress = (CircularProgressWidget()
                 .set_value(75)
                 .set_label("项目总体进度")
                 .set_theme(ProgressTheme.INFO)
                 .set_size("150px")
                 .set_stroke_width("12px"))

email.add_widget(main_progress)

# 各阶段进度
phases = [
    {"name": "需求分析", "progress": 100, "theme": ProgressTheme.SUCCESS},
    {"name": "系统设计", "progress": 100, "theme": ProgressTheme.SUCCESS},
    {"name": "开发实施", "progress": 80, "theme": ProgressTheme.WARNING},
    {"name": "测试验收", "progress": 30, "theme": ProgressTheme.INFO}
]

phase_widgets = []
for phase in phases:
    progress = (CircularProgressWidget()
                .set_value(phase["progress"])
                .set_label(phase["name"])
                .set_theme(phase["theme"])
                .set_size("100px")
                .set_stroke_width("8px"))
    phase_widgets.append(progress)

phases_column = ColumnWidget().set_columns(2)
phases_column.add_widgets(phase_widgets)
email.add_widget(phases_column)
```

--8<-- "assets/temp/circular_progress_project_display.html"

### 3. Non-percentage Progress

```python
from email_widget import Email
from email_widget.widgets import CircularProgressWidget
from email_widget.core.enums import ProgressTheme

email = Email("数据处理进度")

# 文件处理进度（以文件数为单位）
file_progress = (CircularProgressWidget()
                 .set_max_value(1000)      # 总共1000个文件
                 .set_value(750)           # 已处理750个
                 .set_label("文件处理")     # 显示75%
                 .set_theme(ProgressTheme.INFO)
                 .set_size("120px"))

email.add_widget(file_progress)

# 数据下载进度（以MB为单位）
download_progress = (CircularProgressWidget()
                     .set_max_value(500)      # 总大小500MB
                     .set_value(350)          # 已下载350MB
                     .set_label("数据下载")    # 显示70%
                     .set_theme(ProgressTheme.PRIMARY)
                     .set_size("120px"))

email.add_widget(download_progress)
```

--8<-- "assets/temp/circular_progress_non_percentage.html"

## ⚡ Shortcut Methods

The Email class provides the `add_circular_progress` shortcut method:

```python
# 基础快捷方法
email.add_circular_progress(
    value=75,
    label="任务进度",
    theme="success"
)

# 带样式的快捷方法
email.add_circular_progress(
    value=68,
    label="CPU使用率",
    theme="warning",
    size="100px",
    stroke_width="8px"
)

# 非百分比进度
email.add_circular_progress(
    value=750,
    max_value=1000,
    label="文件处理",
    theme="info",
    size="120px"
)
```

## 🐛 Common Issues

### Q: How to automatically choose theme based on value?
A: Create a theme selection function:
```python
def auto_theme(value):
    if value < 50:
        return ProgressTheme.SUCCESS
    elif value < 80:
        return ProgressTheme.WARNING
    else:
        return ProgressTheme.ERROR

progress.set_theme(auto_theme(85))  # 自动选择ERROR主题
```

### Q: How to implement dynamic progress updates?
A: Use increment and decrement methods:
```python
progress = CircularProgressWidget().set_value(50)
progress.increment(10)  # 增加到60%
progress.decrement(5)   # 减少到55%
progress.complete()     # 设置为100%
progress.reset()        # 重置为0%
```

### Q: What if circular progress bar is too small or too large?
A: Adjust size and line width:
```python
# 小尺寸
progress.set_size("60px").set_stroke_width("4px")
# 大尺寸
progress.set_size("200px").set_stroke_width("15px")
```

### Q: What happens when progress value exceeds range?
A: Values are automatically limited between 0 and max_value:
```python
progress.set_max_value(100)
progress.set_value(150)  # 自动限制为100
progress.set_value(-10)  # 自动限制为0
```

### Q: How to create multiple progress bars with same style?
A: Use configuration function:
```python
def create_standard_progress(value, label):
    return (CircularProgressWidget()
            .set_value(value)
            .set_label(label)
            .set_size("80px")
            .set_stroke_width("6px")
            .set_theme(get_theme_by_value(value)))

progress1 = create_standard_progress(60, "CPU")
progress2 = create_standard_progress(80, "内存")
```

## 🔗 Related Widgets

- [ProgressWidget](progress-widget.md) - Linear progress bar widget
- [MetricWidget](metric-widget.md) - Data metrics display widget
- [StatusWidget](status-widget.md) - Status information display widget
- [CardWidget](card-widget.md) - Card widget that can contain progress bars
- [ColumnWidget](column-widget.md) - Used for laying out multiple progress bar widgets