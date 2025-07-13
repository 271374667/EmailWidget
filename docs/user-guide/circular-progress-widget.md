# CircularProgressWidget 圆形进度组件

CircularProgressWidget是一个用于显示圆形进度条的组件，提供比线性进度条更紧凑的视觉效果，适合在有限空间内展示进度信息。它支持多种主题颜色、尺寸设置和进度管理功能，是系统监控和任务进度展示的理想选择。

## 🎯 组件预览

--8<-- "assets/circular_progress_widget_component_preview.html"

## ✨ 核心特性

- **🎨 多种主题**: 支持PRIMARY、SUCCESS、WARNING、ERROR、INFO等主题颜色
- **📊 进度管理**: 支持数值设置、增减操作、完成重置等便捷功能
- **🔧 样式定制**: 灵活的尺寸控制、线条宽度、标签显示设置
- **📈 非百分比**: 支持自定义最大值，不限于百分比显示
- **⚡ 便捷操作**: 提供increment、decrement、complete、reset等快捷方法
- **📧 邮件兼容**: 使用邮件客户端兼容的HTML和CSS实现

## 🚀 快速开始

### 基础用法

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

### 进阶用法

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

📚 **完整API文档**: [CircularProgressWidget API](../api/circular-progress-widget.md)

## 🎨 样式指南

### 主题颜色和应用场景

- **PRIMARY**: 蓝色 (#0078d4) - 主要进度、重要指标
- **SUCCESS**: 绿色 (#107c10) - 正常状态、成功完成
- **WARNING**: 橙色 (#ff8c00) - 需要注意、接近阈值
- **ERROR**: 红色 (#d13438) - 错误状态、超出限制
- **INFO**: 蓝色 (#0078d4) - 信息展示、参考数据

### 尺寸规格建议

- **小型指标**: 60px - 80px，适合集成显示
- **常规指标**: 100px - 120px，适合主要展示
- **重要指标**: 150px - 200px，适合突出显示
- **线条宽度**: 小尺寸用4-6px，大尺寸用8-12px

## 📱 最佳实践

### 1. 系统资源监控

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

### 2. 项目进度展示

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

### 3. 非百分比进度

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

## ⚡ 快捷方法

Email 类提供了 `add_circular_progress` 快捷方法：

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

## 🐛 常见问题

### Q: 如何根据数值自动选择主题？
A: 创建主题选择函数：
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

### Q: 如何实现动态进度更新？
A: 使用increment和decrement方法：
```python
progress = CircularProgressWidget().set_value(50)
progress.increment(10)  # 增加到60%
progress.decrement(5)   # 减少到55%
progress.complete()     # 设置为100%
progress.reset()        # 重置为0%
```

### Q: 圆形进度条太小或太大怎么办？
A: 调整尺寸和线条宽度：
```python
# 小尺寸
progress.set_size("60px").set_stroke_width("4px")
# 大尺寸
progress.set_size("200px").set_stroke_width("15px")
```

### Q: 进度值超出范围会怎样？
A: 值会自动限制在0到max_value之间：
```python
progress.set_max_value(100)
progress.set_value(150)  # 自动限制为100
progress.set_value(-10)  # 自动限制为0
```

### Q: 如何创建多个相同样式的进度条？
A: 使用配置函数：
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

## 🔗 相关组件

- [ProgressWidget](progress-widget.md) - 线性进度条组件
- [MetricWidget](metric-widget.md) - 数据指标展示组件
- [StatusWidget](status-widget.md) - 状态信息展示组件
- [CardWidget](card-widget.md) - 可以包含进度条的卡片组件
- [ColumnWidget](column-widget.md) - 用于布局多个进度条组件