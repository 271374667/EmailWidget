# 圆形进度组件 (CircularProgressWidget)

`CircularProgressWidget` 是一个用于显示圆形进度条的组件，提供比线性进度条更紧凑的视觉效果，适合在有限空间内展示进度信息。

## 🎯 组件预览

<div class="widget-preview">
<div class="preview-item">
<div class="preview-header">
<h4>⭕ 圆形进度条</h4>
<span class="preview-tag progress">进度组件</span>
</div>
<div class="preview-content">
<div style="display: flex; justify-content: space-around; padding: 20px; background: #f6f8fa; border-radius: 6px;">
<div style="text-align: center;">
<div style="width: 80px; height: 80px; border: 6px solid #e1e4e8; border-top: 6px solid #28a745; border-radius: 50%; margin: 0 auto 10px; position: relative;">
<div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-weight: bold; color: #28a745;">75%</div>
</div>
<div style="font-size: 12px; color: #586069;">任务进度</div>
</div>
<div style="text-align: center;">
<div style="width: 80px; height: 80px; border: 6px solid #e1e4e8; border-top: 6px solid #fd7e14; border-radius: 50%; margin: 0 auto 10px; position: relative;">
<div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-weight: bold; color: #fd7e14;">60%</div>
</div>
<div style="font-size: 12px; color: #586069;">CPU使用率</div>
</div>
<div style="text-align: center;">
<div style="width: 80px; height: 80px; border: 6px solid #e1e4e8; border-top: 6px solid #dc3545; border-radius: 50%; margin: 0 auto 10px; position: relative;">
<div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-weight: bold; color: #dc3545;">90%</div>
</div>
<div style="font-size: 12px; color: #586069;">磁盘空间</div>
</div>
</div>
</div>
</div>
</div>

## ✨ 主要功能

### 🎨 多种主题颜色
- **PRIMARY** - 主色调蓝色
- **SUCCESS** - 成功绿色  
- **WARNING** - 警告橙色
- **ERROR** - 错误红色
- **INFO** - 信息蓝色

### 📊 进度管理
- **数值设置** - 支持浮点数进度值
- **增减操作** - 便捷的增减方法
- **完成重置** - 快速完成和重置功能
- **最大值设置** - 自定义进度范围

### 🔧 样式定制
- **尺寸控制** - 灵活的大小设置
- **线条宽度** - 可调节的进度条粗细
- **标签显示** - 可选的进度标签

## 🛠️ 核心方法详解

### 进度设置方法

#### `set_value(value)` 和 `set_max_value(max_val)`
设置当前进度值和最大值。

```python
from email_widget.widgets import CircularProgressWidget

# 设置进度值
progress = CircularProgressWidget().set_value(75.5)

# 设置最大值（默认为100）
progress = (CircularProgressWidget()
            .set_max_value(200)
            .set_value(150))  # 75%
```

#### `set_label(label)` 和 `set_theme(theme)`
设置标签和主题颜色。

```python
from email_widget.core.enums import ProgressTheme

progress = (CircularProgressWidget()
            .set_value(80)
            .set_label("任务完成度")
            .set_theme(ProgressTheme.SUCCESS))
```

### 样式设置方法

#### `set_size(size)` 和 `set_stroke_width(width)`
设置圆形进度条的大小和线条宽度。

```python
# 设置大小和线条宽度
progress = (CircularProgressWidget()
            .set_value(65)
            .set_size("120px")
            .set_stroke_width("10px"))
```

### 进度管理方法

#### `increment(amount)` 和 `decrement(amount)`
增加或减少进度值。

```python
progress = CircularProgressWidget().set_value(50)

# 增加进度
progress.increment(10)  # 现在是60%
progress.increment(5)   # 现在是65%

# 减少进度
progress.decrement(15)  # 现在是50%
```

#### `complete()` 和 `reset()`
快速设置为完成状态或重置。

```python
progress = CircularProgressWidget()

# 设置为100%完成
progress.complete()

# 重置为0%
progress.reset()
```

## 💡 实用示例

### 基础进度显示

```python
from email_widget.widgets import CircularProgressWidget
from email_widget.core.enums import ProgressTheme

# 创建基础圆形进度条
progress = (CircularProgressWidget()
            .set_value(65)
            .set_label("下载进度"))
```

### 系统监控指标

```python
# CPU使用率监控
cpu_progress = (CircularProgressWidget()
                .set_value(35)
                .set_label("CPU使用率")
                .set_theme(ProgressTheme.SUCCESS)
                .set_size("100px")
                .set_stroke_width("8px"))

# 内存使用率监控
memory_progress = (CircularProgressWidget()
                   .set_value(68)
                   .set_label("内存使用率")
                   .set_theme(ProgressTheme.WARNING)
                   .set_size("100px")
                   .set_stroke_width("8px"))

# 磁盘使用率监控
disk_progress = (CircularProgressWidget()
                 .set_value(85)
                 .set_label("磁盘使用率")
                 .set_theme(ProgressTheme.ERROR)
                 .set_size("100px")
                 .set_stroke_width("8px"))
```

### 任务完成度展示

```python
# 项目任务进度
task_progress = (CircularProgressWidget()
                 .set_value(75)
                 .set_label("项目进度")
                 .set_theme(ProgressTheme.INFO)
                 .set_size("150px")
                 .set_stroke_width("12px"))

# 学习进度
learning_progress = (CircularProgressWidget()
                     .set_value(90)
                     .set_label("课程完成")
                     .set_theme(ProgressTheme.SUCCESS)
                     .set_size("120px"))
```

### 不同尺寸的进度条

```python
# 小尺寸进度条
small_progress = (CircularProgressWidget()
                  .set_value(60)
                  .set_label("同步")
                  .set_size("60px")
                  .set_stroke_width("4px"))

# 中等尺寸进度条
medium_progress = (CircularProgressWidget()
                   .set_value(75)
                   .set_label("处理中")
                   .set_size("100px")
                   .set_stroke_width("8px"))

# 大尺寸进度条
large_progress = (CircularProgressWidget()
                  .set_value(85)
                  .set_label("主要任务")
                  .set_size("200px")
                  .set_stroke_width("15px"))
```

## 🎨 主题样式

### 不同主题的进度条

```python
# 成功主题（绿色）
success_progress = (CircularProgressWidget()
                    .set_value(100)
                    .set_label("任务完成")
                    .set_theme(ProgressTheme.SUCCESS))

# 警告主题（橙色）
warning_progress = (CircularProgressWidget()
                    .set_value(75)
                    .set_label("存储空间")
                    .set_theme(ProgressTheme.WARNING))

# 错误主题（红色）
error_progress = (CircularProgressWidget()
                  .set_value(90)
                  .set_label("CPU负载")
                  .set_theme(ProgressTheme.ERROR))

# 信息主题（蓝色）
info_progress = (CircularProgressWidget()
                 .set_value(45)
                 .set_label("网络使用")
                 .set_theme(ProgressTheme.INFO))

# 主色调主题
primary_progress = (CircularProgressWidget()
                    .set_value(60)
                    .set_label("总体进度")
                    .set_theme(ProgressTheme.PRIMARY))
```

## 🔧 高级用法

### 动态进度更新

```python
def create_dynamic_progress(initial_value=0):
    """创建可动态更新的进度条"""
    progress = (CircularProgressWidget()
                .set_value(initial_value)
                .set_label("处理进度")
                .set_theme(ProgressTheme.PRIMARY))
    
    return progress

# 模拟进度更新
progress = create_dynamic_progress()
for i in range(0, 101, 10):
    progress.set_value(i)
    # 在实际应用中，这里可能是处理某个任务
```

### 条件主题切换

```python
def get_progress_theme(value):
    """根据进度值选择合适的主题"""
    if value >= 90:
        return ProgressTheme.ERROR    # 高负载用红色
    elif value >= 70:
        return ProgressTheme.WARNING  # 中等负载用橙色
    else:
        return ProgressTheme.SUCCESS  # 正常负载用绿色

# 应用条件主题
cpu_usage = 85
cpu_progress = (CircularProgressWidget()
                .set_value(cpu_usage)
                .set_label("CPU使用率")
                .set_theme(get_progress_theme(cpu_usage)))
```

### 非百分比进度

```python
# 处理记录数进度
records_progress = (CircularProgressWidget()
                    .set_max_value(1000)      # 总共1000条记录
                    .set_value(750)           # 已处理750条
                    .set_label("数据处理")     # 显示75%
                    .set_theme(ProgressTheme.INFO))

# 文件下载进度（MB）
download_progress = (CircularProgressWidget()
                     .set_max_value(500)      # 总大小500MB
                     .set_value(350)          # 已下载350MB
                     .set_label("文件下载")    # 显示70%
                     .set_theme(ProgressTheme.PRIMARY))
```

## 📊 组合使用

### 多指标监控面板

```python
from email_widget.widgets import ColumnWidget

# 创建多个监控指标
metrics = [
    CircularProgressWidget()
    .set_value(45).set_label("CPU").set_theme(ProgressTheme.SUCCESS)
    .set_size("80px").set_stroke_width("6px"),
    
    CircularProgressWidget()
    .set_value(72).set_label("内存").set_theme(ProgressTheme.WARNING)
    .set_size("80px").set_stroke_width("6px"),
    
    CircularProgressWidget()
    .set_value(28).set_label("网络").set_theme(ProgressTheme.INFO)
    .set_size("80px").set_stroke_width("6px"),
    
    CircularProgressWidget()
    .set_value(91).set_label("磁盘").set_theme(ProgressTheme.ERROR)
    .set_size("80px").set_stroke_width("6px")
]

# 使用列布局排列
dashboard = ColumnWidget().set_columns(4).add_widgets(metrics)
```

## 📝 最佳实践

### 1. 合适的尺寸选择
```python
# 小型指标使用小尺寸
small_metric = (CircularProgressWidget()
                .set_size("60px")
                .set_stroke_width("4px"))

# 重要指标使用大尺寸
important_metric = (CircularProgressWidget()
                    .set_size("150px")
                    .set_stroke_width("12px"))
```

### 2. 主题颜色的合理使用
```python
# 根据数值范围选择主题
def get_appropriate_theme(value):
    if value < 50:
        return ProgressTheme.SUCCESS
    elif value < 80:
        return ProgressTheme.WARNING
    else:
        return ProgressTheme.ERROR
```

### 3. 标签的有效性
```python
# 使用简洁明了的标签
progress = (CircularProgressWidget()
            .set_label("CPU")          # 简洁
            .set_label("内存使用"))     # 明确
```

### 4. 线条宽度的协调性
```python
# 保持同一组进度条的线条宽度一致
standard_width = "8px"
progress1 = CircularProgressWidget().set_stroke_width(standard_width)
progress2 = CircularProgressWidget().set_stroke_width(standard_width)
```

## ⚠️ 注意事项

1. **值范围** - 进度值会自动限制在0到max_value之间
2. **百分比计算** - 显示的百分比基于value/max_value计算
3. **邮件兼容性** - 在邮件客户端中使用简化的CSS实现
4. **尺寸设置** - 过小的尺寸可能影响百分比数字的显示
5. **线条宽度** - 线条太粗可能影响内部百分比的显示空间
6. **主题一致性** - 建议在同一报告中保持主题颜色的一致性
7. **标签长度** - 过长的标签可能影响整体布局

## 🔗 相关组件

- **[ProgressWidget](progress-widget.md)** - 线性进度条组件
- **[StatusWidget](status-widget.md)** - 状态信息展示组件
- **[CardWidget](card-widget.md)** - 可以包含进度条的卡片组件
- **[ColumnWidget](column-widget.md)** - 用于布局多个进度条组件 