# 📚 Basic Concepts

Before diving into EmailWidget, understanding its core concepts will help you build better email reports. This chapter introduces EmailWidget's design philosophy and key concepts.

## 📧 Email Class Overview

### Basic Concepts

The `Email` class is the core of EmailWidget, serving as the container and manager for all Widgets:

```python
from email_widget import Email, TextWidget

# 创建邮件对象
email = Email(title="报告标题")

# 设置元信息
email.set_subtitle("副标题")
email.set_footer("脚注信息")

# 管理Widget
email.add_widget(TextWidget('Hello, World!'))
email.remove_widget("Hello, World!")
email.clear_widgets()

# 导出结果
html_content = email.export_str()
file_path = email.export_html("report.html")
```

### Lifecycle

The typical lifecycle of an Email object:

1. **Creation** - Initialize email object
2. **Configuration** - Set title, subtitle, footer, etc.
3. **Content Addition** - Add various Widget components
4. **Rendering** - Generate HTML content
5. **Export** - Save to file or get string

### Features

=== "Convenience Methods"
    
    ```python
    # 直接添加常用内容
    email.add_text("标题", text_type="title_large")
    email.add_table_from_data(data, headers)
    email.add_progress(75, "完成度")
    email.add_chart_from_plt(title="图表")
    ```

=== "Widget Management"
    
    ```python
    # 获取Widget
    widget = email.get_widget("my_widget_id")
    
    # 移除Widget
    email.remove_widget("widget_id")
    
    # 清空所有Widget
    email.clear_widgets()
    
    # 获取Widget数量
    count = email.get_widget_count()
    ```

=== "Method Chaining"
    
    ```python
    # 流畅的API设计
    email = (Email("标题")
             .set_subtitle("副标题")
             .set_footer("脚注")
             .add_widget(widget1)
             .add_widget(widget2))
    ```

## 🧩 Widget Component System

### Design Philosophy

All Widget components inherit from `BaseWidget`, ensuring API consistency:

```python
from email_widget.core.base import BaseWidget

class MyCustomWidget(BaseWidget):
    def __init__(self):
        super().__init__()
        self.widget_type = "custom"
    
    def render(self) -> str:
        # 渲染逻辑
        return self._render_template("custom.html", context)
```

### Common Features

All Widgets share the following common features:

=== "ID Management"
    
    ```python
    # 设置唯一ID
    widget.set_widget_id("my_unique_id")
    
    # 获取ID
    widget_id = widget.widget_id
    
    # 获取类型
    widget_type = widget.widget_type
    ```

=== "Template Rendering"
    
    ```python
    # 获取渲染上下文
    context = widget.get_template_context()
    
    # 渲染为HTML
    html = widget.render_html()
    ```

### Widget Categories

EmailWidget provides 12 professional components, categorized by function:

#### 📝 Content Components
- **TextWidget** - Text content, 8 styles
- **ImageWidget** - Image display, multi-source support
- **QuoteWidget** - Quote style, author information

#### 📊 Data Components  
- **TableWidget** - Data tables, DataFrame integration
- **ChartWidget** - Chart display, matplotlib support
- **LogWidget** - Log display, level classification

#### 📈 Metric Components
- **ProgressWidget** - Linear progress bar, 5 themes
- **CircularProgressWidget** - Circular progress, multiple sizes
- **StatusWidget** - Status management, dynamic updates

#### 🎨 Interface Components
- **AlertWidget** - Alert reminders, 5 types
- **CardWidget** - Information cards, icon support
- **ColumnWidget** - Layout container, responsive design


## 🎯 Best Practices

### Code Organization

Recommended code organization:

```python
# 1. 导入必要的库
from email_widget import Email, TextWidget, TableWidget, EmailConfig
from email_widget.core.enums import TextType


# 2. 数据准备
def prepare_data():
    return {"sales": [100, 200, 300]}


# 3. 邮件构建
def build_email(data):
    email = Email("销售报告")
    # 添加内容
    email.add_widget(
        TextWidget().set_content("销售数据分析").set_type(TextType.TITLE_LARGE)
    )

    return email


# 4. 主函数
def main():
    data = prepare_data()
    email = build_email(data)
    email.export_html("report.html")
```

## 🚀 Next Steps

Now that you understand EmailWidget's core concepts, you can:

- Check out [User Guide](../user-guide/index.md) to learn detailed component usage
- Browse [API Reference](../api/index.md) to understand the complete API
- Study [Example Code](../examples/index.md) to learn practical applications
- Read [Development Guide](../development/index.md) to participate in project development