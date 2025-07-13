# ColumnWidget 列布局组件

ColumnWidget是一个强大的布局组件，用于创建多列布局，将多个Widget按列排列。它支持自动列数模式和手动设置列数，使用table布局确保在各种邮件客户端中的兼容性，是构建复杂邮件布局的核心组件。

## 🎯 组件预览

--8<-- "assets/column_widget_component_preview.html"

## ✨ 核心特性

- **📐 自动布局**: 根据Widget数量自动计算最优列数
- **🔧 手动控制**: 支持1-4列的手动设置
- **📧 邮件兼容**: 使用table布局确保邮件客户端兼容性
- **🎨 灵活配置**: 支持列间距调整和响应式设计
- **⚡ 动态管理**: 支持动态添加、移除和更新Widget
- **📱 响应式**: 在不同邮件客户端中保持良好显示

## 🚀 快速开始

### 基础用法

```python
from email_widget import Email
from email_widget.widgets import ColumnWidget, TextWidget

# 创建列布局组件
column = ColumnWidget()

# 创建子组件
widget1 = TextWidget().set_content("第一列内容")
widget2 = TextWidget().set_content("第二列内容")  
widget3 = TextWidget().set_content("第三列内容")

# 添加到布局中（3个Widget自动使用3列）
column.add_widgets([widget1, widget2, widget3])

email = Email("多列布局示例")
email.add_widget(column)
```

### 进阶用法

```python
# 固定列数布局
column = ColumnWidget()
column.set_columns(2)  # 固定使用2列
column.set_gap("25px")  # 设置列间距

# 创建多个组件
from email_widget.widgets import StatusWidget, MetricWidget

status = StatusWidget().set_title("系统状态")
status.add_status("CPU", "68%", "warning")
status.add_status("内存", "4.2GB", "info")

metric = MetricWidget().set_title("核心指标")
metric.add_metric("用户数", 12345, "人", "+15.6%", "success")

column.add_widgets([status, metric])
email.add_widget(column)
```

📚 **完整API文档**: [ColumnWidget API](../api/column-widget.md)

## 🎨 样式指南

### 自动列数算法

| Widget数量 | 自动列数 | 布局说明 |
|-----------|----------|----------|
| 1 | 1列 | 单列全宽显示 |
| 2 | 2列 | 左右两列均匀分布 |
| 3 | 3列 | 三列均匀分布 |
| 4 | 2列 | 2×2网格布局 |
| 5-6 | 3列 | 三列布局，最后一行可能不满 |
| 7-8 | 2列 | 两列布局，多行显示 |
| 9+ | 3列 | 三列布局，多行显示 |

### 列间距建议

- **文本内容**: 15px - 20px
- **卡片组件**: 20px - 25px  
- **图片组件**: 10px - 15px
- **状态组件**: 20px - 30px

## 📱 最佳实践

### 1. 自动列数布局

```python
from email_widget import Email
from email_widget.widgets import ColumnWidget, CardWidget

email = Email("仪表板报告")

# 创建自动列数布局
auto_column = ColumnWidget()  # 默认自动模式

# 创建多个卡片（6个Widget自动使用3列）
cards = []
for i in range(6):
    card = CardWidget()
    card.set_title(f"指标 {i+1}")
    card.set_content(f"这是第{i+1}个指标的数据展示")
    cards.append(card)

auto_column.add_widgets(cards)
email.add_widget(auto_column)
```

--8<-- "assets/temp/column_auto_layout.html"

### 2. 固定列数布局

```python
from email_widget import Email
from email_widget.widgets import ColumnWidget, StatusWidget

email = Email("系统监控报告")

# 创建固定2列布局
fixed_column = ColumnWidget().set_columns(2)
fixed_column.set_gap("30px")

# 系统状态组件
system_status = StatusWidget()
system_status.set_title("系统资源")
system_status.add_status("CPU使用率", "68%", "success")
system_status.add_status("内存使用", "85%", "warning")

# 服务状态组件
service_status = StatusWidget()
service_status.set_title("服务状态")
service_status.add_status("Web服务", "运行中", "success")
service_status.add_status("数据库", "正常", "success")

fixed_column.add_widgets([system_status, service_status])
email.add_widget(fixed_column)
```

--8<-- "assets/temp/column_fixed_layout.html"

### 3. 混合组件布局

```python
from email_widget import Email
from email_widget.widgets import (
    ColumnWidget, TextWidget, AlertWidget, 
    ProgressWidget, ImageWidget
)

email = Email("综合报告")

# 创建混合组件布局
mixed_column = ColumnWidget().set_columns(3)

# 不同类型的组件
text_widget = TextWidget().set_content("欢迎查看本月报告")
alert_widget = AlertWidget().set_content("注意：系统将于今晚维护").set_alert_type("warning")
progress_widget = ProgressWidget().set_progress(75).set_label("项目进度")

mixed_column.add_widgets([text_widget, alert_widget, progress_widget])
email.add_widget(mixed_column)
```

--8<-- "assets/temp/column_mixed_layout.html"

### 4. 响应式布局

```python
from email_widget import Email
from email_widget.widgets import ColumnWidget

def create_responsive_layout(widgets):
    """创建响应式布局"""
    column = ColumnWidget()  # 使用自动模式
    
    # 根据Widget数量设置间距
    if len(widgets) <= 2:
        column.set_gap("30px")  # 少量Widget时增加间距
    elif len(widgets) <= 4:
        column.set_gap("20px")  # 中等数量使用默认间距
    else:
        column.set_gap("15px")  # 大量Widget时减少间距
    
    column.add_widgets(widgets)
    return column

# 使用响应式布局
email = Email("响应式布局示例")
widgets = [widget1, widget2, widget3, widget4]
responsive_layout = create_responsive_layout(widgets)
email.add_widget(responsive_layout)
```

--8<-- "assets/temp/column_responsive_layout.html"

## ⚡ 快捷方法

Email 类提供了 `add_column` 快捷方法：

```python
# 自动列数快捷方法
email.add_column([widget1, widget2, widget3])

# 指定列数的快捷方法
email.add_column(
    widgets=[widget1, widget2, widget3, widget4],
    columns=2,
    gap="25px"
)

# 响应式列布局
email.add_column(
    widgets=[widget1, widget2, widget3],
    auto_columns=True,
    gap="20px"
)
```

## 🐛 常见问题

### Q: 如何确定最佳的列数？
A: 建议使用自动模式，系统会根据内容数量自动选择：
```python
column = ColumnWidget()  # 自动模式，无需设置列数
```

### Q: 在移动设备上如何显示？
A: 邮件客户端通常会自动调整为单列显示：
```python
# 设置最大宽度确保移动端适配
column.set_gap("15px")  # 较小间距适合移动端
```

### Q: 如何处理不同高度的Widget？
A: 组件自动使用`vertical-align: top`确保顶部对齐：
```python
# 不需要额外设置，组件会自动对齐
column.add_widgets([tall_widget, short_widget])
```

### Q: 列间距过大或过小怎么办？
A: 使用`set_gap()`方法调整：
```python
column.set_gap("15px")  # 小间距
column.set_gap("25px")  # 大间距
```

### Q: 如何动态更新布局？
A: 使用动态管理方法：
```python
# 清空后重新添加
column.clear_widgets()
column.add_widgets(new_widgets)

# 或按索引移除
column.remove_widget_by_index(0)
```

## 🔗 相关组件

- [CardWidget](card-widget.md) - 常用于列布局的卡片组件
- [StatusWidget](status-widget.md) - 适合多列展示的状态组件
- [MetricWidget](metric-widget.md) - 适合并排显示的指标组件
- [TextWidget](text-widget.md) - 基础文本布局组件
- [ImageWidget](image-widget.md) - 图片网格布局组件