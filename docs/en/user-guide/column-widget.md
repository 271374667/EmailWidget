# ColumnWidget

ColumnWidget is a powerful layout component used to create multi-column layouts, arranging multiple widgets in columns. It supports automatic column mode and manual column setting, using table layout to ensure compatibility across various email clients, making it a core component for building complex email layouts.

## 🎯 Widget Preview

--8<-- "assets/column_widget_component_preview.html"

## ✨ Core Features

- **📏 Auto Layout**: Automatically calculates optimal column count based on widget quantity
- **🔧 Manual Control**: Supports manual setting of 1-4 columns
- **📧 Email Compatible**: Uses table layout to ensure email client compatibility
- **🎨 Flexible Configuration**: Supports column gap adjustment and responsive design
- **⚡ Dynamic Management**: Supports dynamic adding, removing, and updating of widgets
- **📱 Responsive**: Maintains good display across different email clients

## 🚀 Quick Start

### Basic Usage

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

### Advanced Usage

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

📚 **Complete API Documentation**: [ColumnWidget API](../api/column-widget.md)

## 🎨 Style Guide

### Auto Column Algorithm

| Widget Count | Auto Columns | Layout Description |
|--------------|--------------|--------------------|
| 1 | 1 column | Single column full width |
| 2 | 2 columns | Left and right columns evenly distributed |
| 3 | 3 columns | Three columns evenly distributed |
| 4 | 2 columns | 2×2 grid layout |
| 5-6 | 3 columns | Three column layout, last row may not be full |
| 7-8 | 2 columns | Two column layout, multi-row display |
| 9+ | 3 columns | Three column layout, multi-row display |

### Column Gap Recommendations

- **Text Content**: 15px - 20px
- **Card Components**: 20px - 25px  
- **Image Components**: 10px - 15px
- **Status Components**: 20px - 30px

## 📱 Best Practices

### 1. Auto Column Layout

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

### 2. Fixed Column Layout

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

### 3. Mixed Component Layout

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

### 4. Responsive Layout

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

## ⚡ Shortcut Methods

The Email class provides the `add_column` shortcut method:

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

## 🐛 Common Issues

### Q: How to determine the optimal column count?
A: Recommend using auto mode, the system will automatically choose based on content quantity:
```python
column = ColumnWidget()  # 自动模式，无需设置列数
```

### Q: How does it display on mobile devices?
A: Email clients usually automatically adjust to single column display:
```python
# 设置最大宽度确保移动端适配
column.set_gap("15px")  # 较小间距适合移动端
```

### Q: How to handle widgets with different heights?
A: Components automatically use `vertical-align: top` to ensure top alignment:
```python
# 不需要额外设置，组件会自动对齐
column.add_widgets([tall_widget, short_widget])
```

### Q: What if column gap is too large or too small?
A: Use the `set_gap()` method to adjust:
```python
column.set_gap("15px")  # 小间距
column.set_gap("25px")  # 大间距
```

### Q: How to dynamically update layout?
A: Use dynamic management methods:
```python
# 清空后重新添加
column.clear_widgets()
column.add_widgets(new_widgets)

# 或按索引移除
column.remove_widget_by_index(0)
```

## 🔗 Related Widgets

- [CardWidget](card-widget.md) - Card widgets commonly used in column layouts
- [StatusWidget](status-widget.md) - Status widgets suitable for multi-column display
- [MetricWidget](metric-widget.md) - Metric widgets suitable for side-by-side display
- [TextWidget](text-widget.md) - Basic text layout widgets
- [ImageWidget](image-widget.md) - Image grid layout widgets