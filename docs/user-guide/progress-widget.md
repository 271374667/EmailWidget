# ProgressWidget Progress条组件

ProgressWidget 是一个线性Progress条组件，用于显示Task或进程的CompleteProgress。它支持多种主题颜色、Percentage显示、以及灵活的样式配置，适合用于Display各种ProgressInfo。

## 组件预览

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

## 主要功能

### 🎨 多种主题颜色
- **PRIMARY** (主色调): 一般Progress、默认Status
- **SUCCESS** (成功绿色): 成功Progress、健康Status  
- **WARNING** (Alert橙色): AlertProgress、注意Status
- **ERROR** (错误红色): 错误Progress、危险Status
- **INFO** (Info蓝色): InfoProgress、中性Status

### 📊 Progress管理
- 支持自定义最大值和当前值
- 自动计算Percentage
- 提供增量/减量操作
- 支持重置和Complete操作

### ⚙️ 样式配置
- 可自定义宽度、高度、圆角
- 支持显示/隐藏PercentageText
- 可设置背景颜色
- 支持标签显示

## 核心方法

### `set_value(value: float)`
设置当前Progress值。

```python
from email_widget.widgets import ProgressWidget

progress = ProgressWidget().set_value(75.5)
```

### `set_max_value(max_val: float)`
设置最大值，默认为100。

```python
progress = ProgressWidget().set_value(850).set_max_value(1000)  # 85%
```

### `set_label(label: str)`
设置Progress条标签。

```python
progress = (ProgressWidget()
    .set_value(60)
    .set_label("下载Progress"))
```

### `set_theme(theme: ProgressTheme)`
设置Progress条主题颜色。

```python
from email_widget.core.enums import ProgressTheme

# 不同主题的Progress条
primary = ProgressWidget().set_value(50).set_theme(ProgressTheme.PRIMARY)
success = ProgressWidget().set_value(95).set_theme(ProgressTheme.SUCCESS)
warning = ProgressWidget().set_value(80).set_theme(ProgressTheme.WARNING)
error = ProgressWidget().set_value(15).set_theme(ProgressTheme.ERROR)
```

### `show_percentage(show: bool = True)`
控制是否显示PercentageText。

```python
# 隐藏Percentage
progress = (ProgressWidget()
    .set_value(45)
    .set_label("处理Progress")
    .show_percentage(False))
```

### `increment(amount: float = 1.0)`
增加Progress值。

```python
progress = ProgressWidget().set_value(50)
progress.increment(10)  # 现在是60
progress.increment()    # 现在是61（默认增加1）
```

### `decrement(amount: float = 1.0)`
减少Progress值。

```python
progress = ProgressWidget().set_value(50)
progress.decrement(5)   # 现在是45
```

### `reset()`
重置Progress为0。

```python
progress = ProgressWidget().set_value(80)
progress.reset()  # 现在是0
```

### `complete()`
设置为CompleteStatus（100%）。

```python
progress = ProgressWidget().set_value(80)
progress.complete()  # 现在是100%
```

## 实用示例

### 基础用法

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

### 自定义样式

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

### SystemMonitor场景

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

### TaskProgress管理

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

### 业务MetricDisplay

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

## Progress主题详解

### ProgressTheme 枚举值

| 主题 | 颜色 | 十六进制 | 适用场景 |
|------|------|---------|----------|
| `PRIMARY` | 主色调蓝 | `#0078d4` | 一般Progress、默认Status、ProjectProgress |
| `SUCCESS` | 成功绿色 | `#107c10` | 成功Progress、健康Status、高Complete率 |
| `WARNING` | Alert橙色 | `#ff8c00` | AlertProgress、注意Status、中等风险 |
| `ERROR` | 错误红色 | `#d13438` | 错误Progress、危险Status、高风险 |
| `INFO` | Info蓝色 | `#0078d4` | InfoProgress、中性Status、DataDisplay |

### 主题选择指南

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

## 最佳实践

### 1. 选择合适的主题
```python
# ✅ 好的做法：根据ProgressStatus选择主题
low_progress = ProgressWidget().set_value(25).set_theme(ProgressTheme.ERROR)
medium_progress = ProgressWidget().set_value(60).set_theme(ProgressTheme.WARNING)
high_progress = ProgressWidget().set_value(90).set_theme(ProgressTheme.SUCCESS)

# ❌ 避免：所有Progress条都使用同一主题
```

### 2. 提供清晰的标签
```python
# ✅ 好的做法：描述性的标签
progress = ProgressWidget().set_value(75).set_label("Data同步Progress")

# ❌ 避免：模糊的标签
progress = ProgressWidget().set_value(75).set_label("Progress")
```

### 3. 合理设置最大值
```python
# ✅ 好的做法：根据实际场景设置最大值
file_progress = ProgressWidget().set_value(512).set_max_value(1024).set_label("文件下载")  # MB
task_progress = ProgressWidget().set_value(8).set_max_value(10).set_label("TaskComplete")      # 个

# ✅ 好的做法：Percentage场景使用默认最大值100
percent_progress = ProgressWidget().set_value(85).set_label("Complete率")
```

### 4. 适当显示Percentage
```python
# ✅ 好的做法：重要Progress显示Percentage
important = ProgressWidget().set_value(90).set_label("关键Task").show_percentage(True)

# ✅ 好的做法：装饰性Progress隐藏Percentage
decorative = ProgressWidget().set_value(60).set_label("整体Status").show_percentage(False)
```

## 常见问题

### Q: 如何实现超过100%的Progress？
A: 设置更大的最大值，如 `set_max_value(120)` 然后 `set_value(110)`。

### Q: Progress条可以显示负值吗？
A: 不可以，Progress值会被限制在0到最大值之间。

### Q: 如何实现动态更新Progress？
A: 在代码中使用 `increment()` 或直接更新 `set_value()`，但需要重新渲染邮件。

### Q: 可以自定义Progress条的颜色吗？
A: 当前版本只支持预定义的5种主题，不支持完全自定义颜色。

## 适用场景

### 📊 SystemMonitor
- CPU、内存、磁盘使用率
- 网络带宽使用情况
- Service健康Status

### 📋 Task管理
- Project Completion Progress
- Task执行Status
- 工作流Progress

### 📈 业务Metric
- 销售目标达成率
- 用户满意度
- KPIComplete情况

### 🔧 技术Metric
- 代码覆盖率
- 测试通过率
- 部署Progress

## 相关组件

- [CircularProgressWidget](circular-progress-widget.md) - CircularProgress条
- [StatusWidget](status-widget.md) - StatusInfoDisplay
- [CardWidget](card-widget.md) - CardContainer

## 下一步

了解了ProgressWidget的基本用法后，建议继续学习：
- [CircularProgressWidget](circular-progress-widget.md) - 学习CircularProgress条的使用
- [StatusWidget](status-widget.md) - 学习如何Display多个Status项 