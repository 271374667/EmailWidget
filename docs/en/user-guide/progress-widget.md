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
    .set_label("Download Progress"))
```

### `set_theme(theme: ProgressTheme)`
Sets the progress bar theme color.

```python
from email_widget.core.enums import ProgressTheme

# Different themed progress bars
primary = ProgressWidget().set_value(50).set_theme(ProgressTheme.PRIMARY)
success = ProgressWidget().set_value(95).set_theme(ProgressTheme.SUCCESS)
warning = ProgressWidget().set_value(80).set_theme(ProgressTheme.WARNING)
error = ProgressWidget().set_value(15).set_theme(ProgressTheme.ERROR)
```

### `show_percentage(show: bool = True)`
Controls whether to display percentage text.

```python
# Hide percentage
progress = (ProgressWidget()
    .set_value(45)
    .set_label("Processing Progress")
    .show_percentage(False))
```

### `increment(amount: float = 1.0)`
Increases progress value.

```python
progress = ProgressWidget().set_value(50)
progress.increment(10)  # Now 60
progress.increment()    # Now 61 (default increase by 1)
```

### `decrement(amount: float = 1.0)`
Decreases progress value.

```python
progress = ProgressWidget().set_value(50)
progress.decrement(5)   # Now 45
```

### `reset()`
Resets progress to 0.

```python
progress = ProgressWidget().set_value(80)
progress.reset()  # Now 0
```

### `complete()`
Sets to complete status (100%).

```python
progress = ProgressWidget().set_value(80)
progress.complete()  # Now 100%
```

## Practical Examples

### Basic Usage

```python
from email_widget.widgets import ProgressWidget
from email_widget.core.enums import ProgressTheme

# Basic progress bar
basic = (ProgressWidget()
    .set_value(65)
    .set_label("Task Completion")
    .set_theme(ProgressTheme.PRIMARY))

# Success status progress bar
success = (ProgressWidget()
    .set_value(95)
    .set_label("Test Pass Rate")
    .set_theme(ProgressTheme.SUCCESS))

# Warning status progress bar
warning = (ProgressWidget()
    .set_value(85)
    .set_label("Memory Usage")
    .set_theme(ProgressTheme.WARNING))
```

### Custom Styling

```python
# Custom size and color
custom = (ProgressWidget()
    .set_value(70)
    .set_label("Custom Progress Bar")
    .set_width("80%")
    .set_height("24px")
    .set_border_radius("12px")
    .set_background_color("#f0f0f0"))

# No percentage display
no_percent = (ProgressWidget()
    .set_value(40)
    .set_label("Silent Progress")
    .show_percentage(False)
    .set_theme(ProgressTheme.INFO))
```

### System Monitoring Scenarios

```python
# CPU usage
cpu_usage = (ProgressWidget()
    .set_value(45)
    .set_label("CPU Usage")
    .set_theme(ProgressTheme.SUCCESS))

# Memory usage (warning status)
memory_usage = (ProgressWidget()
    .set_value(78)
    .set_label("Memory Usage")
    .set_theme(ProgressTheme.WARNING))

# Disk usage (danger status)
disk_usage = (ProgressWidget()
    .set_value(92)
    .set_label("Disk Usage")
    .set_theme(ProgressTheme.ERROR))
```

### Task Progress Management

```python
# Project progress
project_progress = (ProgressWidget()
    .set_value(0)
    .set_label("Project Total Progress")
    .set_theme(ProgressTheme.PRIMARY))

# Simulate task progress updates
project_progress.increment(25)  # 25%
project_progress.increment(30)  # 55%
project_progress.increment(20)  # 75%

# Data processing progress
data_processing = (ProgressWidget()
    .set_value(1250)
    .set_max_value(2000)
    .set_label("Data Processing Progress")
    .set_theme(ProgressTheme.INFO))  # 62.5%
```

### Business Metrics Display

```python
# Sales target completion
sales_target = (ProgressWidget()
    .set_value(1250000)
    .set_max_value(1000000)  # Over-achieved
    .set_label("Monthly Sales Target")
    .set_theme(ProgressTheme.SUCCESS))  # 125%

# User satisfaction
satisfaction = (ProgressWidget()
    .set_value(88)
    .set_label("User Satisfaction")
    .set_theme(ProgressTheme.SUCCESS))

# Task completion rate
task_completion = (ProgressWidget()
    .set_value(156)
    .set_max_value(200)
    .set_label("Weekly Task Completion Rate")
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
# Choose appropriate theme based on progress value
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

# Usage example
progress_value = 85
theme = get_progress_theme(progress_value)
progress = ProgressWidget().set_value(progress_value).set_theme(theme)
```

## Best Practices

### 1. Choose Appropriate Theme
```python
# ✅ Good practice: Choose theme based on progress status
low_progress = ProgressWidget().set_value(25).set_theme(ProgressTheme.ERROR)
medium_progress = ProgressWidget().set_value(60).set_theme(ProgressTheme.WARNING)
high_progress = ProgressWidget().set_value(90).set_theme(ProgressTheme.SUCCESS)

# ❌ Avoid: Using same theme for all progress bars
```

### 2. Provide Clear Labels
```python
# ✅ Good practice: Descriptive labels
progress = ProgressWidget().set_value(75).set_label("Data Sync Progress")

# ❌ Avoid: Vague labels
progress = ProgressWidget().set_value(75).set_label("Progress")
```

### 3. Set Reasonable Maximum Values
```python
# ✅ Good practice: Set maximum value based on actual scenario
file_progress = ProgressWidget().set_value(512).set_max_value(1024).set_label("File Download")  # MB
task_progress = ProgressWidget().set_value(8).set_max_value(10).set_label("Task Completion")      # count

# ✅ Good practice: Use default maximum value 100 for percentage scenarios
percent_progress = ProgressWidget().set_value(85).set_label("Completion Rate")
```

### 4. Show Percentage Appropriately
```python
# ✅ Good practice: Show percentage for important progress
important = ProgressWidget().set_value(90).set_label("Critical Task").show_percentage(True)

# ✅ Good practice: Hide percentage for decorative progress
decorative = ProgressWidget().set_value(60).set_label("Overall Status").show_percentage(False)
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