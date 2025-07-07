# ColumnWidget 列布局组件

<div style="background: #f0f8ff; border: 1px solid #4a90e2; border-radius: 8px; padding: 20px; margin: 20px 0;">
  <h3 style="color: #2c5282; margin-top: 0;">📐 列布局组件</h3>
  <table cellpadding="0" cellspacing="0" border="0" style="width: 100%; max-width: 100%; table-layout: fixed; border-collapse: separate; border-spacing: 20px 0; margin: 16px 0; font-family: Arial, sans-serif;">
    <tr>
      <td style="width: 33.33%; vertical-align: top; padding: 0; box-sizing: border-box;">
        <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px;">
          <h4 style="margin: 0 0 8px 0; color: #323130;">列 1</h4>
          <p style="margin: 0; color: #605e5c; font-size: 14px;">第一列内容展示</p>
        </div>
      </td>
      <td style="width: 33.33%; vertical-align: top; padding: 0; box-sizing: border-box;">
        <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px;">
          <h4 style="margin: 0 0 8px 0; color: #323130;">列 2</h4>
          <p style="margin: 0; color: #605e5c; font-size: 14px;">第二列内容展示</p>
        </div>
      </td>
      <td style="width: 33.33%; vertical-align: top; padding: 0; box-sizing: border-box;">
        <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px;">
          <h4 style="margin: 0 0 8px 0; color: #323130;">列 3</h4>
          <p style="margin: 0; color: #605e5c; font-size: 14px;">第三列内容展示</p>
        </div>
      </td>
    </tr>
  </table>
  <div style="display: flex; gap: 10px; margin-top: 15px;">
    <span style="background: #e8f4fd; color: #0078d4; padding: 4px 8px; border-radius: 4px; font-size: 12px;">多列布局</span>
    <span style="background: #e8f4fd; color: #0078d4; padding: 4px 8px; border-radius: 4px; font-size: 12px;">自动列数</span>
    <span style="background: #e8f4fd; color: #0078d4; padding: 4px 8px; border-radius: 4px; font-size: 12px;">邮件兼容</span>
  </div>
</div>

ColumnWidget是一个强大的布局组件，用于创建多列布局，将多个Widget按列排列。它支持自动列数模式和手动设置列数，使用table布局确保在各种邮件客户端中的兼容性。

## 🎯 主要功能

### 布局模式
- **自动列数**：根据Widget数量自动计算最优列数
- **手动列数**：支持1-4列的手动设置
- **响应式设计**：在不同邮件客户端中保持良好显示
- **邮件兼容**：使用table布局确保兼容性

### 自动列数规则
- **1个Widget**：1列
- **2个Widget**：2列
- **3个Widget**：3列
- **4个Widget**：2列（2×2布局）
- **5-6个Widget**：3列
- **7-8个Widget**：2列
- **9个以上Widget**：3列

### Widget管理
- **动态添加**：支持单个或批量添加Widget
- **动态移除**：支持按ID或索引移除Widget
- **灵活配置**：支持设置列间距和其他样式

## 📋 核心方法

### 基础使用

```python
from email_widget.widgets import ColumnWidget, TextWidget

# 创建列布局组件
column = ColumnWidget()

# 创建子组件
widget1 = TextWidget().set_content("第一列内容")
widget2 = TextWidget().set_content("第二列内容")
widget3 = TextWidget().set_content("第三列内容")

# 添加Widget
column.add_widgets([widget1, widget2, widget3])
```

### Widget管理方法

```python
# 添加单个Widget
column.add_widget(widget)

# 添加多个Widget
column.add_widgets([widget1, widget2, widget3])

# 移除Widget（按ID）
column.remove_widget("widget_id")

# 移除Widget（按索引）
column.remove_widget_by_index(0)

# 清空所有Widget
column.clear_widgets()

# 获取Widget数量
count = column.get_widget_count()
```

### 布局配置

```python
# 设置列数（1-4列，-1为自动模式）
column.set_columns(2)    # 固定2列
column.set_columns(-1)   # 自动模式

# 设置列间距
column.set_gap("20px")

# 检查是否为自动模式
is_auto = column.is_auto_mode()

# 获取当前列数
current_cols = column.get_current_columns()
```

## 💡 实用示例

### 自动列数布局

```python
from email_widget.widgets import ColumnWidget, CardWidget

# 创建自动列数布局
auto_column = ColumnWidget()  # 默认自动模式

# 创建多个卡片
cards = []
for i in range(6):
    card = CardWidget()
    card.set_title(f"卡片 {i+1}")
    card.set_content(f"这是第{i+1}个卡片的内容")
    cards.append(card)

# 添加到布局中（6个Widget自动使用3列）
auto_column.add_widgets(cards)

# 渲染布局
html = auto_column.render_html()
```

### 固定列数布局

```python
from email_widget.widgets import ColumnWidget, StatusWidget
from email_widget.core.enums import StatusType

# 创建固定2列布局
fixed_column = ColumnWidget().set_columns(2)

# 创建状态组件
status1 = StatusWidget()
status1.set_title("系统状态")
status1.add_status_item("CPU", "68%", StatusType.WARNING)
status1.add_status_item("内存", "4.2GB", StatusType.INFO)

status2 = StatusWidget()
status2.set_title("服务状态")
status2.add_status_item("Web服务", "运行中", StatusType.SUCCESS)
status2.add_status_item("数据库", "正常", StatusType.SUCCESS)

# 添加到2列布局
fixed_column.add_widgets([status1, status2])
```

### 混合组件布局

```python
from email_widget.widgets import (
    ColumnWidget, TextWidget, AlertWidget, 
    ProgressWidget, ImageWidget
)
from email_widget.core.enums import AlertType, ProgressTheme

# 创建混合组件布局
mixed_column = ColumnWidget().set_columns(3)

# 创建不同类型的组件
text_widget = TextWidget()
text_widget.set_content("欢迎使用EmailWidget组件库")

alert_widget = AlertWidget()
alert_widget.set_content("这是一个提示信息")
alert_widget.set_alert_type(AlertType.TIP)

progress_widget = ProgressWidget()
progress_widget.set_progress(75)
progress_widget.set_theme(ProgressTheme.SUCCESS)

# 添加到3列布局
mixed_column.add_widgets([text_widget, alert_widget, progress_widget])
```

### 响应式布局

```python
# 创建响应式布局函数
def create_responsive_layout(widgets):
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
widgets = [widget1, widget2, widget3, widget4]
responsive_layout = create_responsive_layout(widgets)
```

### 动态布局管理

```python
# 创建动态布局管理器
class DynamicLayoutManager:
    def __init__(self):
        self.column = ColumnWidget()
        self.widgets = []
    
    def add_widget(self, widget):
        self.widgets.append(widget)
        self._update_layout()
    
    def remove_widget(self, widget_id):
        self.widgets = [w for w in self.widgets if w.widget_id != widget_id]
        self._update_layout()
    
    def _update_layout(self):
        # 清空当前布局
        self.column.clear_widgets()
        
        # 根据Widget数量调整列数
        widget_count = len(self.widgets)
        if widget_count <= 2:
            self.column.set_columns(widget_count)
        elif widget_count <= 4:
            self.column.set_columns(2)
        else:
            self.column.set_columns(3)
        
        # 重新添加Widget
        self.column.add_widgets(self.widgets)
    
    def render(self):
        return self.column.render_html()

# 使用动态布局管理器
layout_manager = DynamicLayoutManager()
layout_manager.add_widget(widget1)
layout_manager.add_widget(widget2)
```

## 📐 自动列数算法详解

### 算法规则

| Widget数量 | 自动列数 | 布局说明 |
|-----------|----------|----------|
| 1 | 1列 | 单列全宽显示 |
| 2 | 2列 | 左右两列均匀分布 |
| 3 | 3列 | 三列均匀分布 |
| 4 | 2列 | 2×2网格布局 |
| 5-6 | 3列 | 三列布局，最后一行可能不满 |
| 7-8 | 2列 | 两列布局，多行显示 |
| 9+ | 3列 | 三列布局，多行显示 |

### 算法优势

```python
# 自动算法的优势
def demonstrate_auto_algorithm():
    column = ColumnWidget()  # 自动模式
    
    # 动态添加Widget，自动调整列数
    widgets = []
    for i in range(1, 10):
        widget = TextWidget().set_content(f"Widget {i}")
        widgets.append(widget)
        
        # 每次添加后检查列数变化
        column.clear_widgets()
        column.add_widgets(widgets[:i])
        print(f"{i}个Widget -> {column.get_current_columns()}列")
```

## 🎨 最佳实践

### 1. 选择合适的布局模式

```python
# 内容数量固定时使用手动模式
fixed_layout = ColumnWidget().set_columns(2)

# 内容数量动态变化时使用自动模式
dynamic_layout = ColumnWidget()  # 默认自动模式
```

### 2. 优化列间距

```python
# 根据内容类型调整间距
text_layout = ColumnWidget().set_gap("15px")    # 文本内容间距小
card_layout = ColumnWidget().set_gap("25px")    # 卡片内容间距大
image_layout = ColumnWidget().set_gap("10px")   # 图片内容间距更小
```

### 3. 组件类型搭配

```python
# 同类型组件组合
status_column = ColumnWidget().set_columns(2)
status_widgets = [status1, status2, status3, status4]
status_column.add_widgets(status_widgets)

# 混合类型组件组合
mixed_column = ColumnWidget().set_columns(3)
mixed_widgets = [text_widget, alert_widget, progress_widget]
mixed_column.add_widgets(mixed_widgets)
```

### 4. 邮件客户端兼容性

```python
# 确保邮件客户端兼容性
def create_email_compatible_layout(widgets):
    column = ColumnWidget()
    
    # 限制最大列数以确保兼容性
    max_columns = min(len(widgets), 3)
    column.set_columns(max_columns)
    
    # 设置适中的间距
    column.set_gap("20px")
    
    column.add_widgets(widgets)
    return column
```

### 5. 性能优化

```python
# 批量操作优化
def optimize_widget_management(column, new_widgets):
    # 一次性清空和添加，避免多次重新渲染
    column.clear_widgets()
    column.add_widgets(new_widgets)
    
    # 而不是逐个添加
    # for widget in new_widgets:
    #     column.add_widget(widget)  # 效率较低
```

## 🔧 常见问题

### Q: 如何确定最佳的列数？
A: 建议使用自动模式，系统会根据内容数量自动选择最优列数。

### Q: 在移动设备上如何显示？
A: 邮件客户端通常会自动调整为单列显示，无需特殊处理。

### Q: 如何处理不同高度的Widget？
A: 使用`vertical-align: top`确保所有Widget顶部对齐。

### Q: 列间距过大或过小怎么办？
A: 使用`set_gap()`方法调整间距，推荐15px-25px之间。

ColumnWidget为您提供了强大而灵活的布局解决方案，让复杂的多列布局变得简单易用！ 