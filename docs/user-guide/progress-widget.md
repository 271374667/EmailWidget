# ProgressWidget 进度条组件

ProgressWidget 是一个线性进度条组件，用于显示任务或进程的完成进度。它支持多种主题颜色、百分比显示、以及灵活的样式配置，适合用于展示各种进度信息。

## 组件预览

<div class="component-preview">
    <div style="margin: 20px 0;">
        <!-- 基本进度条 -->
        <div style="margin: 16px 0;">
            <div style="font-size: 14px; font-weight: 600; color: #323130; margin-bottom: 8px;">项目完成进度</div>
            <div style="width: 100%; height: 20px; background: #e1dfdd; border-radius: 10px; overflow: hidden; position: relative;">
                <div style="width: 75%; height: 100%; background: #0078d4; border-radius: 10px;"></div>
                <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 12px; font-weight: 600; color: #ffffff;">75%</div>
            </div>
        </div>
        
        <!-- 成功主题 -->
        <div style="margin: 16px 0;">
            <div style="font-size: 14px; font-weight: 600; color: #323130; margin-bottom: 8px;">任务成功率</div>
            <div style="width: 100%; height: 20px; background: #e1dfdd; border-radius: 10px; overflow: hidden; position: relative;">
                <div style="width: 92%; height: 100%; background: #107c10; border-radius: 10px;"></div>
                <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 12px; font-weight: 600; color: #ffffff;">92%</div>
            </div>
        </div>
        
        <!-- 警告主题 -->
        <div style="margin: 16px 0;">
            <div style="font-size: 14px; font-weight: 600; color: #323130; margin-bottom: 8px;">磁盘使用率</div>
            <div style="width: 100%; height: 20px; background: #e1dfdd; border-radius: 10px; overflow: hidden; position: relative;">
                <div style="width: 85%; height: 100%; background: #ff8c00; border-radius: 10px;"></div>
                <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 12px; font-weight: 600; color: #ffffff;">85%</div>
            </div>
        </div>
    </div>
</div>

## 主要功能

### 🎨 多种主题颜色
- **PRIMARY** (主色调): 一般进度、默认状态
- **SUCCESS** (成功绿色): 成功进度、健康状态  
- **WARNING** (警告橙色): 警告进度、注意状态
- **ERROR** (错误红色): 错误进度、危险状态
- **INFO** (信息蓝色): 信息进度、中性状态

### 📊 进度管理
- 支持自定义最大值和当前值
- 自动计算百分比
- 提供增量/减量操作
- 支持重置和完成操作

### ⚙️ 样式配置
- 可自定义宽度、高度、圆角
- 支持显示/隐藏百分比文本
- 可设置背景颜色
- 支持标签显示

## 核心方法

### `set_value(value: float)`
设置当前进度值。

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
设置进度条标签。

```python
progress = (ProgressWidget()
    .set_value(60)
    .set_label("下载进度"))
```

### `set_theme(theme: ProgressTheme)`
设置进度条主题颜色。

```python
from email_widget.core.enums import ProgressTheme

# 不同主题的进度条
primary = ProgressWidget().set_value(50).set_theme(ProgressTheme.PRIMARY)
success = ProgressWidget().set_value(95).set_theme(ProgressTheme.SUCCESS)
warning = ProgressWidget().set_value(80).set_theme(ProgressTheme.WARNING)
error = ProgressWidget().set_value(15).set_theme(ProgressTheme.ERROR)
```

### `show_percentage(show: bool = True)`
控制是否显示百分比文本。

```python
# 隐藏百分比
progress = (ProgressWidget()
    .set_value(45)
    .set_label("处理进度")
    .show_percentage(False))
```

### `increment(amount: float = 1.0)`
增加进度值。

```python
progress = ProgressWidget().set_value(50)
progress.increment(10)  # 现在是60
progress.increment()    # 现在是61（默认增加1）
```

### `decrement(amount: float = 1.0)`
减少进度值。

```python
progress = ProgressWidget().set_value(50)
progress.decrement(5)   # 现在是45
```

### `reset()`
重置进度为0。

```python
progress = ProgressWidget().set_value(80)
progress.reset()  # 现在是0
```

### `complete()`
设置为完成状态（100%）。

```python
progress = ProgressWidget().set_value(80)
progress.complete()  # 现在是100%
```

## 实用示例

### 基础用法

```python
from email_widget.widgets import ProgressWidget
from email_widget.core.enums import ProgressTheme

# 基本进度条
basic = (ProgressWidget()
    .set_value(65)
    .set_label("任务完成度")
    .set_theme(ProgressTheme.PRIMARY))

# 成功状态进度条
success = (ProgressWidget()
    .set_value(95)
    .set_label("测试通过率")
    .set_theme(ProgressTheme.SUCCESS))

# 警告状态进度条
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
    .set_label("自定义进度条")
    .set_width("80%")
    .set_height("24px")
    .set_border_radius("12px")
    .set_background_color("#f0f0f0"))

# 无百分比显示
no_percent = (ProgressWidget()
    .set_value(40)
    .set_label("静默进度")
    .show_percentage(False)
    .set_theme(ProgressTheme.INFO))
```

### 系统监控场景

```python
# CPU使用率
cpu_usage = (ProgressWidget()
    .set_value(45)
    .set_label("CPU使用率")
    .set_theme(ProgressTheme.SUCCESS))

# 内存使用率（警告状态）
memory_usage = (ProgressWidget()
    .set_value(78)
    .set_label("内存使用率")
    .set_theme(ProgressTheme.WARNING))

# 磁盘使用率（危险状态）
disk_usage = (ProgressWidget()
    .set_value(92)
    .set_label("磁盘使用率")
    .set_theme(ProgressTheme.ERROR))
```

### 任务进度管理

```python
# 项目进度
project_progress = (ProgressWidget()
    .set_value(0)
    .set_label("项目总进度")
    .set_theme(ProgressTheme.PRIMARY))

# 模拟任务进度更新
project_progress.increment(25)  # 25%
project_progress.increment(30)  # 55%
project_progress.increment(20)  # 75%

# 数据处理进度
data_processing = (ProgressWidget()
    .set_value(1250)
    .set_max_value(2000)
    .set_label("数据处理进度")
    .set_theme(ProgressTheme.INFO))  # 62.5%
```

### 业务指标展示

```python
# 销售目标完成度
sales_target = (ProgressWidget()
    .set_value(1250000)
    .set_max_value(1000000)  # 超额完成
    .set_label("月度销售目标")
    .set_theme(ProgressTheme.SUCCESS))  # 125%

# 用户满意度
satisfaction = (ProgressWidget()
    .set_value(88)
    .set_label("用户满意度")
    .set_theme(ProgressTheme.SUCCESS))

# 任务完成率
task_completion = (ProgressWidget()
    .set_value(156)
    .set_max_value(200)
    .set_label("本周任务完成率")
    .set_theme(ProgressTheme.PRIMARY))  # 78%
```

## 进度主题详解

### ProgressTheme 枚举值

| 主题 | 颜色 | 十六进制 | 适用场景 |
|------|------|---------|----------|
| `PRIMARY` | 主色调蓝 | `#0078d4` | 一般进度、默认状态、项目进度 |
| `SUCCESS` | 成功绿色 | `#107c10` | 成功进度、健康状态、高完成率 |
| `WARNING` | 警告橙色 | `#ff8c00` | 警告进度、注意状态、中等风险 |
| `ERROR` | 错误红色 | `#d13438` | 错误进度、危险状态、高风险 |
| `INFO` | 信息蓝色 | `#0078d4` | 信息进度、中性状态、数据展示 |

### 主题选择指南

```python
# 根据进度值选择合适的主题
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
# ✅ 好的做法：根据进度状态选择主题
low_progress = ProgressWidget().set_value(25).set_theme(ProgressTheme.ERROR)
medium_progress = ProgressWidget().set_value(60).set_theme(ProgressTheme.WARNING)
high_progress = ProgressWidget().set_value(90).set_theme(ProgressTheme.SUCCESS)

# ❌ 避免：所有进度条都使用同一主题
```

### 2. 提供清晰的标签
```python
# ✅ 好的做法：描述性的标签
progress = ProgressWidget().set_value(75).set_label("数据同步进度")

# ❌ 避免：模糊的标签
progress = ProgressWidget().set_value(75).set_label("进度")
```

### 3. 合理设置最大值
```python
# ✅ 好的做法：根据实际场景设置最大值
file_progress = ProgressWidget().set_value(512).set_max_value(1024).set_label("文件下载")  # MB
task_progress = ProgressWidget().set_value(8).set_max_value(10).set_label("任务完成")      # 个

# ✅ 好的做法：百分比场景使用默认最大值100
percent_progress = ProgressWidget().set_value(85).set_label("完成率")
```

### 4. 适当显示百分比
```python
# ✅ 好的做法：重要进度显示百分比
important = ProgressWidget().set_value(90).set_label("关键任务").show_percentage(True)

# ✅ 好的做法：装饰性进度隐藏百分比
decorative = ProgressWidget().set_value(60).set_label("整体状态").show_percentage(False)
```

## 常见问题

### Q: 如何实现超过100%的进度？
A: 设置更大的最大值，如 `set_max_value(120)` 然后 `set_value(110)`。

### Q: 进度条可以显示负值吗？
A: 不可以，进度值会被限制在0到最大值之间。

### Q: 如何实现动态更新进度？
A: 在代码中使用 `increment()` 或直接更新 `set_value()`，但需要重新渲染邮件。

### Q: 可以自定义进度条的颜色吗？
A: 当前版本只支持预定义的5种主题，不支持完全自定义颜色。

## 适用场景

### 📊 系统监控
- CPU、内存、磁盘使用率
- 网络带宽使用情况
- 服务健康状态

### 📋 任务管理
- 项目完成进度
- 任务执行状态
- 工作流进度

### 📈 业务指标
- 销售目标达成率
- 用户满意度
- KPI完成情况

### 🔧 技术指标
- 代码覆盖率
- 测试通过率
- 部署进度

## 相关组件

- [CircularProgressWidget](circular-progress-widget.md) - 圆形进度条
- [StatusWidget](status-widget.md) - 状态信息展示
- [CardWidget](card-widget.md) - 卡片容器

## 下一步

了解了ProgressWidget的基本用法后，建议继续学习：
- [CircularProgressWidget](circular-progress-widget.md) - 学习圆形进度条的使用
- [StatusWidget](status-widget.md) - 学习如何展示多个状态项 