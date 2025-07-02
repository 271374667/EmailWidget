# 进度组件 (Progress Widgets)

EmailWidget 提供了两种进度组件：线性进度条(ProgressWidget)和圆形进度条(CircularProgressWidget)，用于展示任务完成度、系统负载、KPI达成率等进度信息。

## 🚀 快速开始

### 线性进度条

```python
from email_widget.widgets import ProgressWidget
from email_widget.core.enums import ProgressTheme

# 基本进度条
progress = ProgressWidget()
progress.set_value(75)
progress.set_label("项目完成进度")
progress.set_theme(ProgressTheme.SUCCESS)
```

<div style="margin: 16px 0;">
    <div style="font-family: 'Segoe UI', Tahoma, Arial, sans-serif; font-size: 14px; font-weight: 600; color: #323130; margin-bottom: 8px;">项目完成进度</div>
    <div style="width: 100%; height: 20px; background: #e1dfdd; border-radius: 10px; overflow: hidden; position: relative;">
        <div style="width: 75%; height: 100%; background: #107c10; border-radius: 10px;"></div>
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-family: 'Segoe UI', Tahoma, Arial, sans-serif; font-size: 12px; font-weight: 600; color: #ffffff;">75.0%</div>
    </div>
</div>

### 圆形进度条

```python
from email_widget.widgets import CircularProgressWidget

# 基本圆形进度条
circular = CircularProgressWidget()
circular.set_value(88)
circular.set_label("系统性能指标")
circular.set_size("120px")
```

<div style="text-align: center; margin: 16px 0;">
    <div style="width: 120px; height: 120px; border-radius: 50%; background: conic-gradient(#0078d4 0deg, #0078d4 316.8deg, #e1dfdd 316.8deg); margin: 0 auto; display: flex; align-items: center; justify-content: center;">
        <div style="width: 80px; height: 80px; background: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; color: #323130;">88%</div>
    </div>
    <div style="margin-top: 8px; font-size: 14px; color: #323130;">系统性能指标</div>
</div>

## 📊 线性进度条 (ProgressWidget)

### 基本配置

```python
# 设置进度值和最大值
progress = ProgressWidget()
progress.set_value(450)      # 当前值
progress.set_max_value(600)  # 最大值
progress.set_label("月度销售目标")

# 显示选项
progress.set_show_percentage(True)   # 显示百分比
progress.set_width("100%")           # 进度条宽度
progress.set_height("24px")          # 进度条高度
```

### 主题样式

```python
from email_widget.core.enums import ProgressTheme

# 不同主题的进度条
themes_demo = [
    (ProgressTheme.PRIMARY, "主要进度", 75),
    (ProgressTheme.SUCCESS, "成功状态", 90),
    (ProgressTheme.WARNING, "警告状态", 60),
    (ProgressTheme.ERROR, "错误状态", 25)
]

for theme, label, value in themes_demo:
    progress = ProgressWidget()
    progress.set_value(value)
    progress.set_label(label)
    progress.set_theme(theme)
```

<div style="margin: 16px 0; padding: 16px; background: #f8f9fa; border-radius: 4px;">
    <div style="margin: 12px 0;">
        <div style="font-size: 14px; font-weight: 600; color: #323130; margin-bottom: 8px;">主要进度</div>
        <div style="width: 100%; height: 20px; background: #e1dfdd; border-radius: 10px; overflow: hidden; position: relative;">
            <div style="width: 75%; height: 100%; background: #0078d4; border-radius: 10px;"></div>
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 12px; font-weight: 600; color: #ffffff;">75%</div>
        </div>
    </div>
    <div style="margin: 12px 0;">
        <div style="font-size: 14px; font-weight: 600; color: #323130; margin-bottom: 8px;">成功状态</div>
        <div style="width: 100%; height: 20px; background: #e1dfdd; border-radius: 10px; overflow: hidden; position: relative;">
            <div style="width: 90%; height: 100%; background: #107c10; border-radius: 10px;"></div>
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 12px; font-weight: 600; color: #ffffff;">90%</div>
        </div>
    </div>
    <div style="margin: 12px 0;">
        <div style="font-size: 14px; font-weight: 600; color: #323130; margin-bottom: 8px;">警告状态</div>
        <div style="width: 100%; height: 20px; background: #e1dfdd; border-radius: 10px; overflow: hidden; position: relative;">
            <div style="width: 60%; height: 100%; background: #ff8c00; border-radius: 10px;"></div>
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 12px; font-weight: 600; color: #ffffff;">60%</div>
        </div>
    </div>
    <div style="margin: 12px 0;">
        <div style="font-size: 14px; font-weight: 600; color: #323130; margin-bottom: 8px;">错误状态</div>
        <div style="width: 100%; height: 20px; background: #e1dfdd; border-radius: 10px; overflow: hidden; position: relative;">
            <div style="width: 25%; height: 100%; background: #d13438; border-radius: 10px;"></div>
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 12px; font-weight: 600; color: #323130;">25%</div>
        </div>
    </div>
</div>

### 自定义样式

```python
# 自定义颜色和尺寸
custom_progress = ProgressWidget()
custom_progress.set_value(65)
custom_progress.set_label("自定义进度条")
custom_progress.set_width("400px")         # 自定义宽度
custom_progress.set_height("16px")         # 自定义高度
custom_progress.set_border_radius("8px")   # 自定义圆角
custom_progress.set_background_color("#f0f0f0")  # 背景色
```

### 动态更新

```python
# 支持增量操作
progress = ProgressWidget()
progress.set_value(50)
progress.set_label("任务进度")

# 增加进度
progress.increment(10)  # 进度 +10
progress.increment_percentage(5)  # 百分比 +5%

# 减少进度
progress.decrement(5)   # 进度 -5
progress.decrement_percentage(2)  # 百分比 -2%
```

## ⭕ 圆形进度条 (CircularProgressWidget)

### 基本配置

```python
# 基本圆形进度条
circular = CircularProgressWidget()
circular.set_value(75)
circular.set_label("完成度")
circular.set_size("100px")            # 圆形尺寸
circular.set_stroke_width("8px")      # 线条粗细
```

### 不同尺寸展示

```python
# 小号进度圆
small_circle = CircularProgressWidget()
small_circle.set_value(60)
small_circle.set_label("CPU使用率")
small_circle.set_size("80px")

# 中号进度圆
medium_circle = CircularProgressWidget()
medium_circle.set_value(85)
medium_circle.set_label("内存使用率")
medium_circle.set_size("120px")

# 大号进度圆
large_circle = CircularProgressWidget()
large_circle.set_value(72)
large_circle.set_label("总体性能")
large_circle.set_size("160px")
```

<div style="display: flex; justify-content: space-around; align-items: center; margin: 20px 0; flex-wrap: wrap; gap: 20px;">
    <div style="text-align: center;">
        <div style="width: 80px; height: 80px; border-radius: 50%; background: conic-gradient(#0078d4 0deg, #0078d4 216deg, #e1dfdd 216deg); margin: 0 auto; display: flex; align-items: center; justify-content: center;">
            <div style="width: 56px; height: 56px; background: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; color: #323130; font-size: 11px;">60%</div>
        </div>
        <div style="margin-top: 8px; font-size: 12px; color: #323130;">CPU使用率</div>
    </div>
    <div style="text-align: center;">
        <div style="width: 120px; height: 120px; border-radius: 50%; background: conic-gradient(#0078d4 0deg, #0078d4 306deg, #e1dfdd 306deg); margin: 0 auto; display: flex; align-items: center; justify-content: center;">
            <div style="width: 88px; height: 88px; background: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; color: #323130; font-size: 14px;">85%</div>
        </div>
        <div style="margin-top: 8px; font-size: 14px; color: #323130;">内存使用率</div>
    </div>
    <div style="text-align: center;">
        <div style="width: 160px; height: 160px; border-radius: 50%; background: conic-gradient(#0078d4 0deg, #0078d4 259.2deg, #e1dfdd 259.2deg); margin: 0 auto; display: flex; align-items: center; justify-content: center;">
            <div style="width: 120px; height: 120px; background: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; color: #323130; font-size: 16px;">72%</div>
        </div>
        <div style="margin-top: 8px; font-size: 16px; color: #323130;">总体性能</div>
    </div>
</div>

### 主题和颜色

```python
from email_widget.core.enums import ProgressTheme

# 不同主题的圆形进度条
success_circle = CircularProgressWidget()
success_circle.set_value(95)
success_circle.set_theme(ProgressTheme.SUCCESS)
success_circle.set_label("任务完成")

warning_circle = CircularProgressWidget()
warning_circle.set_value(68)
warning_circle.set_theme(ProgressTheme.WARNING)
warning_circle.set_label("注意监控")

error_circle = CircularProgressWidget()
error_circle.set_value(15)
error_circle.set_theme(ProgressTheme.ERROR)
error_circle.set_label("需要处理")
```

## 📋 实际应用示例

### 系统监控仪表板

```python
from email_widget import Email
from email_widget.widgets import ProgressWidget, CircularProgressWidget, TextWidget
from email_widget.core.enums import ProgressTheme, TextType

# 创建监控仪表板
dashboard = Email("系统监控仪表板")

# 标题
dashboard.add_widget(
    TextWidget()
    .set_content("系统性能监控")
    .set_text_type(TextType.SECTION_H2)
    .set_align(TextAlign.CENTER)
)

# 主要性能指标 - 圆形进度条
cpu_usage = CircularProgressWidget()
cpu_usage.set_value(45)
cpu_usage.set_label("CPU使用率")
cpu_usage.set_theme(ProgressTheme.SUCCESS)
cpu_usage.set_size("120px")

memory_usage = CircularProgressWidget()
memory_usage.set_value(78)
memory_usage.set_label("内存使用率")
memory_usage.set_theme(ProgressTheme.WARNING)
memory_usage.set_size("120px")

disk_usage = CircularProgressWidget()
disk_usage.set_value(92)
disk_usage.set_label("磁盘使用率")
disk_usage.set_theme(ProgressTheme.ERROR)
disk_usage.set_size("120px")

# 具体服务状态 - 线性进度条
web_service = ProgressWidget()
web_service.set_value(150)
web_service.set_max_value(200)
web_service.set_label("Web服务负载 (150/200)")
web_service.set_theme(ProgressTheme.SUCCESS)

db_service = ProgressWidget()
db_service.set_value(180)
db_service.set_max_value(200)
db_service.set_label("数据库负载 (180/200)")
db_service.set_theme(ProgressTheme.WARNING)

cache_service = ProgressWidget()
cache_service.set_value(45)
cache_service.set_max_value(100)
cache_service.set_label("缓存命中率 (45%)")
cache_service.set_theme(ProgressTheme.ERROR)

# 添加到仪表板
dashboard.add_widgets([
    cpu_usage, memory_usage, disk_usage,
    web_service, db_service, cache_service
])
```

### 项目进度报告

```python
# 项目管理进度报告
project_report = Email("项目进度报告")

# 总体进度
overall_progress = ProgressWidget()
overall_progress.set_value(680)
overall_progress.set_max_value(1000)
overall_progress.set_label("项目总体进度 (680/1000 任务点)")
overall_progress.set_theme(ProgressTheme.PRIMARY)
overall_progress.set_height("28px")

# 各阶段进度
phases = [
    ("需求分析", 100, 100, ProgressTheme.SUCCESS),
    ("设计阶段", 85, 100, ProgressTheme.SUCCESS), 
    ("开发阶段", 420, 600, ProgressTheme.PRIMARY),
    ("测试阶段", 75, 150, ProgressTheme.WARNING),
    ("部署上线", 0, 50, ProgressTheme.ERROR)
]

project_report.add_widget(overall_progress)

for phase_name, current, total, theme in phases:
    phase_progress = ProgressWidget()
    phase_progress.set_value(current)
    phase_progress.set_max_value(total)
    phase_progress.set_label(f"{phase_name} ({current}/{total})")
    phase_progress.set_theme(theme)
    project_report.add_widget(phase_progress)
```

### KPI达成情况

```python
# KPI达成率展示
kpi_report = Email("KPI达成情况")

kpi_indicators = [
    ("月度销售目标", 115, 100, "已超额完成", ProgressTheme.SUCCESS),
    ("客户满意度", 88, 90, "接近目标", ProgressTheme.WARNING),
    ("新用户获取", 72, 100, "需要加强", ProgressTheme.ERROR),
    ("成本控制", 95, 100, "良好控制", ProgressTheme.SUCCESS)
]

for name, current, target, status, theme in kpi_indicators:
    # 使用圆形进度条展示KPI
    kpi_circle = CircularProgressWidget()
    kpi_circle.set_value(min(current, 100))  # 限制在100%以内显示
    kpi_circle.set_label(f"{name}\n{current}% ({status})")
    kpi_circle.set_theme(theme)
    kpi_circle.set_size("140px")
    
    kpi_report.add_widget(kpi_circle)
```

## ⚙️ API 参考

### ProgressWidget API

#### 核心方法
| 方法 | 参数 | 说明 | 示例 |
|------|------|------|------|
| `set_value()` | `value: float` | 设置当前值 | `.set_value(75)` |
| `set_max_value()` | `max_val: float` | 设置最大值 | `.set_max_value(100)` |
| `set_label()` | `label: str` | 设置标签 | `.set_label("进度")` |
| `set_theme()` | `theme: ProgressTheme` | 设置主题 | `.set_theme(ProgressTheme.SUCCESS)` |

#### 样式方法
| 方法 | 参数 | 说明 | 默认值 |
|------|------|------|--------|
| `set_show_percentage()` | `show: bool` | 显示百分比 | `True` |
| `set_width()` | `width: str` | 设置宽度 | `"100%"` |
| `set_height()` | `height: str` | 设置高度 | `"20px"` |
| `set_border_radius()` | `radius: str` | 设置圆角 | `"10px"` |
| `set_background_color()` | `color: str` | 设置背景色 | `"#e1dfdd"` |

#### 操作方法
| 方法 | 参数 | 说明 |
|------|------|------|
| `increment()` | `amount: float` | 增加数值 |
| `decrement()` | `amount: float` | 减少数值 |
| `increment_percentage()` | `percent: float` | 增加百分比 |
| `decrement_percentage()` | `percent: float` | 减少百分比 |

### CircularProgressWidget API

#### 核心方法
| 方法 | 参数 | 说明 | 示例 |
|------|------|------|------|
| `set_value()` | `value: float` | 设置当前值 | `.set_value(75)` |
| `set_max_value()` | `max_val: float` | 设置最大值 | `.set_max_value(100)` |
| `set_label()` | `label: str` | 设置标签 | `.set_label("性能")` |
| `set_size()` | `size: str` | 设置尺寸 | `.set_size("120px")` |
| `set_stroke_width()` | `width: str` | 设置线条粗细 | `.set_stroke_width("8px")` |
| `set_theme()` | `theme: ProgressTheme` | 设置主题颜色 | `.set_theme(ProgressTheme.PRIMARY)` |

### 主题枚举

```python
from email_widget.core.enums import ProgressTheme

ProgressTheme.PRIMARY   # 蓝色 (#0078d4)
ProgressTheme.SUCCESS   # 绿色 (#107c10)
ProgressTheme.WARNING   # 橙色 (#ff8c00)
ProgressTheme.ERROR     # 红色 (#d13438)
```

## 🎯 最佳实践

### 1. 选择合适的进度组件
```python
# 线性进度条 - 适合展示任务进度、下载进度等
task_progress = ProgressWidget().set_label("任务完成度")

# 圆形进度条 - 适合展示百分比、性能指标等
performance = CircularProgressWidget().set_label("系统性能")
```

### 2. 合理使用主题颜色
```python
# 根据数值范围自动选择主题
def get_progress_theme(percentage):
    if percentage >= 80:
        return ProgressTheme.SUCCESS
    elif percentage >= 60:
        return ProgressTheme.WARNING
    else:
        return ProgressTheme.ERROR

progress.set_theme(get_progress_theme(75))
```

### 3. 提供清晰的标签说明
```python
# 推荐：包含具体数值和单位
progress.set_label("内存使用率 (3.2GB / 8GB)")

# 推荐：说明进度含义
progress.set_label("项目完成度 (第3阶段/共5阶段)")
```

### 4. 合理设置数值范围
```python
# 推荐：设置合理的最大值
progress.set_max_value(100)  # 百分比
progress.set_max_value(1000) # 任务点数
progress.set_max_value(8192) # 内存MB
```

## 🚨 注意事项

1. **数值有效性**: 确保progress值在0到max_value之间
2. **百分比显示**: 当值超过100%时，百分比文字颜色会自动调整
3. **移动适配**: 圆形进度条在小屏幕上可能需要调整尺寸
4. **主题一致性**: 在同一邮件中保持主题颜色的一致性
5. **性能考虑**: 避免在同一页面使用过多的进度组件

---

**下一步**: 了解 [状态组件](status-widgets.md) 学习如何展示详细的状态信息。 