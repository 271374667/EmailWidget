# ProgressWidget

ProgressWidget is a linear progress bar component used to display task or process completion progress. It supports multiple theme colors, percentage display, and flexible style configuration, suitable for displaying various progress information.

## Widget Preview

<div class="email-preview-wrapper">
<div style="margin: 20px 0; padding: 20px; background: #ffffff; border: 1px solid #e1dfdd; border-radius: 8px;">
        <!-- Basic Progress Bar -->
        <div style="margin: 16px 0;">
            <div style="font-size: 14px; font-weight: 600; color: #323130; margin-bottom: 8px;">Project Completion Progress</div>
            <div style="width: 100%; height: 20px; background: #e1dfdd; border-radius: 10px; overflow: hidden; position: relative;">
                <div style="width: 75%; height: 100%; background: #0078d4; border-radius: 10px;"></div>
                <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 12px; font-weight: 600; color: #ffffff;">75%</div>
            </div>
        </div>
        
        <!-- Success Theme -->
        <div style="margin: 16px 0;">
            <div style="font-size: 14px; font-weight: 600; color: #323130; margin-bottom: 8px;">Task Success Rate</div>
            <div style="width: 100%; height: 20px; background: #e1dfdd; border-radius: 10px; overflow: hidden; position: relative;">
                <div style="width: 92%; height: 100%; background: #107c10; border-radius: 10px;"></div>
                <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 12px; font-weight: 600; color: #ffffff;">92%</div>
            </div>
        </div>
        
        <!-- Warning Theme -->
        <div style="margin: 16px 0;">
            <div style="font-size: 14px; font-weight: 600; color: #323130; margin-bottom: 8px;">Disk Usage</div>
            <div style="width: 100%; height: 20px; background: #e1dfdd; border-radius: 10px; overflow: hidden; position: relative;">
                <div style="width: 85%; height: 100%; background: #ff8c00; border-radius: 10px;"></div>
                <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 12px; font-weight: 600; color: #ffffff;">85%</div>
            </div>
        </div>
    </div>
</div>

## Main Features

### 🎨 Multiple Theme Colors
- **PRIMARY** (Primary): General progress, default status
- **SUCCESS** (Success green): Successful progress, healthy status  
- **WARNING** (Warning orange): Warning progress, attention status
- **ERROR** (Error red): Error progress, danger status
- **INFO** (Info blue): Information progress, neutral status

### 📊 Progress Management
- Supports custom maximum and current values
- Automatic percentage calculation
- Provides increment/decrement operations
- Supports reset and complete operations

### ⚙️ Style Configuration
- Customizable width, height, border radius
- Supports show/hide percentage text
- Can set background color
- Supports label display

## Core Methods

### `set_value(value: float)`
Sets the current progress value.

```python
from email_widget.widgets import ProgressWidget

progress = ProgressWidget().set_value(75.5)
```

### `set_max_value(max_val: float)`
Sets the maximum value, default is 100.

```python
progress = ProgressWidget().set_value(850).set_max_value(1000)  # 85%
```

### `set_label(label: str)`
Sets the progress bar label.

```python
progress = (ProgressWidget()
    .set_value(60)
    .set_label("下载Progress"))
```

### `set_theme(theme: ProgressTheme)`
Sets the progress bar theme color.

```python
from email_widget.core.enums import ProgressTheme

# 不同主题的Progress条
primary = ProgressWidget().set_value(50).set_theme(ProgressTheme.PRIMARY)
success = ProgressWidget().set_value(95).set_theme(ProgressTheme.SUCCESS)
warning = ProgressWidget().set_value(80).set_theme(ProgressTheme.WARNING)
error = ProgressWidget().set_value(15).set_theme(ProgressTheme.ERROR)
```

### `show_percentage(show: bool = True)`
Controls whether to display percentage text.

```python
# 隐藏Percentage
progress = (ProgressWidget()
    .set_value(45)
    .set_label("处理Progress")
    .show_percentage(False))
```

### `increment(amount: float = 1.0)`
Increases progress value.

```python
progress = ProgressWidget().set_value(50)
progress.increment(10)  # 现在是60
progress.increment()    # 现在是61（默认增加1）
```

### `decrement(amount: float = 1.0)`
Decreases progress value.

```python
progress = ProgressWidget().set_value(50)
progress.decrement(5)   # 现在是45
```

### `reset()`
Resets progress to 0.

```python
progress = ProgressWidget().set_value(80)
progress.reset()  # 现在是0
```

### `complete()`
Sets to complete status (100%).

```python
progress = ProgressWidget().set_value(80)
progress.complete()  # 现在是100%
```

## Practical Examples

### Basic Usage

```python
from email_widget.widgets import ProgressWidget
from email_widget.core.enums import ProgressTheme

# 基本Progress条
basic = (ProgressWidget()
    .set_value(65)
    .set_label("TaskComplete度")
    .set_theme(ProgressTheme.PRIMARY))

# 成功StatusProgress条
success = (ProgressWidget()
    .set_value(95)
    .set_label("测试通过率")
    .set_theme(ProgressTheme.SUCCESS))

# AlertStatusProgress条
warning = (ProgressWidget()
    .set_value(85)
    .set_label("内存使用率")
    .set_theme(ProgressTheme.WARNING))
```

### Custom Styling

```python
# 自定义尺寸和颜色
custom = (ProgressWidget()
    .set_value(70)
    .set_label("自定义Progress条")
    .set_width("80%")
    .set_height("24px")
    .set_border_radius("12px")
    .set_background_color("#f0f0f0"))

# 无Percentage显示
no_percent = (ProgressWidget()
    .set_value(40)
    .set_label("静默Progress")
    .show_percentage(False)
    .set_theme(ProgressTheme.INFO))
```

### System Monitoring Scenarios

```python
# CPU使用率
cpu_usage = (ProgressWidget()
    .set_value(45)
    .set_label("CPU使用率")
    .set_theme(ProgressTheme.SUCCESS))

# 内存使用率（AlertStatus）
memory_usage = (ProgressWidget()
    .set_value(78)
    .set_label("内存使用率")
    .set_theme(ProgressTheme.WARNING))

# 磁盘使用率（危险Status）
disk_usage = (ProgressWidget()
    .set_value(92)
    .set_label("磁盘使用率")
    .set_theme(ProgressTheme.ERROR))
```

### Task Progress Management

```python
# ProjectProgress
project_progress = (ProgressWidget()
    .set_value(0)
    .set_label("Project总Progress")
    .set_theme(ProgressTheme.PRIMARY))

# 模拟TaskProgress更新
project_progress.increment(25)  # 25%
project_progress.increment(30)  # 55%
project_progress.increment(20)  # 75%

# Data处理Progress
data_processing = (ProgressWidget()
    .set_value(1250)
    .set_max_value(2000)
    .set_label("Data处理Progress")
    .set_theme(ProgressTheme.INFO))  # 62.5%
```

### Business Metrics Display

```python
# 销售目标Complete度
sales_target = (ProgressWidget()
    .set_value(1250000)
    .set_max_value(1000000)  # 超额Complete
    .set_label("月度销售目标")
    .set_theme(ProgressTheme.SUCCESS))  # 125%

# 用户满意度
satisfaction = (ProgressWidget()
    .set_value(88)
    .set_label("用户满意度")
    .set_theme(ProgressTheme.SUCCESS))

# TaskComplete率
task_completion = (ProgressWidget()
    .set_value(156)
    .set_max_value(200)
    .set_label("本周TaskComplete率")
    .set_theme(ProgressTheme.PRIMARY))  # 78%
```

## Progress Theme Details

### ProgressTheme Enum Values

| Theme | Color | Hex | Use Cases |
|-------|-------|-----|----------|
| `PRIMARY` | Primary blue | `#0078d4` | General progress, default status, project progress |
| `SUCCESS` | Success green | `#107c10` | Successful progress, healthy status, high completion rate |
| `WARNING` | Warning orange | `#ff8c00` | Warning progress, attention status, medium risk |
| `ERROR` | Error red | `#d13438` | Error progress, danger status, high risk |
| `INFO` | Info blue | `#0078d4` | Information progress, neutral status, data display |

### Theme Selection Guide

```python
# 根据Progress值选择合适的主题
def get_progress_theme(value, max_value=100):
    percentage = (value / max_value) * 100
    
    if percentage >= 90:
        return ProgressTheme.SUCCESS
    elif percentage >= 70:
        return ProgressTheme.PRIMARY
    elif percentage >= 50:
        return ProgressTheme.WARNING
    else:
        return ProgressTheme.ERROR

# 使用示例
progress_value = 85
theme = get_progress_theme(progress_value)
progress = ProgressWidget().set_value(progress_value).set_theme(theme)
```

## Best Practices

### 1. Choose Appropriate Theme
```python
# ✅ 好的做法：根据ProgressStatus选择主题
low_progress = ProgressWidget().set_value(25).set_theme(ProgressTheme.ERROR)
medium_progress = ProgressWidget().set_value(60).set_theme(ProgressTheme.WARNING)
high_progress = ProgressWidget().set_value(90).set_theme(ProgressTheme.SUCCESS)

# ❌ 避免：所有Progress条都使用同一主题
```

### 2. Provide Clear Labels
```python
# ✅ 好的做法：描述性的标签
progress = ProgressWidget().set_value(75).set_label("Data同步Progress")

# ❌ 避免：模糊的标签
progress = ProgressWidget().set_value(75).set_label("Progress")
```

### 3. Set Reasonable Maximum Values
```python
# ✅ 好的做法：根据实际场景设置最大值
file_progress = ProgressWidget().set_value(512).set_max_value(1024).set_label("文件下载")  # MB
task_progress = ProgressWidget().set_value(8).set_max_value(10).set_label("TaskComplete")      # 个

# ✅ 好的做法：Percentage场景使用默认最大值100
percent_progress = ProgressWidget().set_value(85).set_label("Complete率")
```

### 4. Show Percentage Appropriately
```python
# ✅ 好的做法：重要Progress显示Percentage
important = ProgressWidget().set_value(90).set_label("关键Task").show_percentage(True)

# ✅ 好的做法：装饰性Progress隐藏Percentage
decorative = ProgressWidget().set_value(60).set_label("整体Status").show_percentage(False)
```

## Common Issues

### Q: How to implement progress over 100%?
A: Set a larger maximum value, e.g., `set_max_value(120)` then `set_value(110)`.

### Q: Can progress bars display negative values?
A: No, progress values are limited between 0 and maximum value.

### Q: How to implement dynamic progress updates?
A: Use `increment()` in code or directly update `set_value()`, but need to re-render the email.

### Q: Can progress bar colors be fully customized?
A: Current version only supports 5 predefined themes, does not support fully custom colors.

## Use Cases

### 📊 System Monitoring
- CPU, memory, disk usage
- Network bandwidth usage
- Service health status

### 📋 Task Management
- Project completion progress
- Task execution status
- Workflow progress

### 📈 Business Metrics
- Sales target achievement rate
- User satisfaction
- KPI completion status

### 🔧 Technical Metrics
- Code coverage
- Test pass rate
- Deployment progress

## Related Components

- [CircularProgressWidget](circular-progress-widget.md) - Circular progress bar
- [StatusWidget](status-widget.md) - Status information display
- [CardWidget](card-widget.md) - Card container

## Next Steps

After learning the basic usage of ProgressWidget, consider continuing with:
- [CircularProgressWidget](circular-progress-widget.md) - Learn circular progress bar usage
- [StatusWidget](status-widget.md) - Learn how to display multiple status items