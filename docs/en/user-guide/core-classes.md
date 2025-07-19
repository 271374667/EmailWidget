# Core Classes

The core architecture of EmailWidget consists of two main classes: the `Email` class and the `BaseWidget` abstract base class. Understanding these two classes is key to mastering EmailWidget.

## 📧 Email Class

The `Email` class is the container for the entire email system, responsible for managing all widgets and generating the final HTML email.

### 🏗️ Basic Structure

```python
from email_widget import Email

# 创建邮件对象
email = Email(title="我的邮件Title")

# 设置副Title和页脚
email.set_subtitle("这是副Title")
email.set_footer("自定义页脚Info")

# 生成HTML
html_content = email.render_html()
```

### 📝 Main Methods

#### Creation and Configuration

```python
# 基本创建
email = Email("Data报告")

# 设置副Title
email.set_subtitle("2024年度业务Data分析")

# 设置页脚Text
email.set_footer("本报告由Data团队生成 © 2024")
```

#### Adding Widgets

```python
from email_widget.widgets import TextWidget, TableWidget

# 添加单个组件
text_widget = TextWidget().set_content("欢迎查看本周Data")
email.add_widget(text_widget)

# 添加多个组件
widgets = [
    TextWidget().set_content("Title1"),
    TableWidget().set_headers(["列1", "列2"]),
    TextWidget().set_content("总结")
]
email.add_widgets(widgets)

# 链式调用
email.add_widget(
    TextWidget()
    .set_content("重要Notification")
    .set_text_type(TextType.SECTION_H2)
    .set_color("#d13438")
)
```

#### Rendering and Output

```python
# 渲染为HTML字符串
html = email.render_html()

# 渲染并保存到文件
email.render_to_file("report.html")

# 渲染并发送邮件
email.render_and_send(
    smtp_config={
        "host": "smtp.gmail.com",
        "port": 587,
        "username": "your@email.com",
        "password": "your_password"
    },
    to_emails=["recipient@email.com"]
)
```

### 🎨 Email Template Structure

The Email class uses a built-in HTML template with the following structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <!-- Inline CSS styles -->
</head>
<body>
    <div class="email-container">
        <!-- Email header -->
        <div class="email-header">
            <h1>{{ title }}</h1>
            {{ subtitle }}
        </div>
        
        <!-- Email body -->
        <div class="email-body">
            {{ widget_content }}
        </div>
        
        <!-- Email footer -->
        <div class="email-footer">
            {{ footer_text }}
        </div>
    </div>
</body>
</html>
```

## 🧩 BaseWidget Abstract Base Class

All widgets inherit from the `BaseWidget` abstract base class, which defines the basic behavior and interface for widgets.

### 🏗️ Basic Features

```python
from email_widget.core.base import BaseWidget

class MyCustomWidget(BaseWidget):
    # 模板定义
    TEMPLATE = """
    <div class="email-preview-wrapper">
<div style="padding: 16px; border: 1px solid #ccc;">
        <h3>{{ title }}</h3>
        <p>{{ content }}</p>
    </div>
</div>
    """
    
    def __init__(self, widget_id=None):
        super().__init__(widget_id)
        self._title = ""
        self._content = ""
    
    def get_template_context(self):
        return {
            'title': self._title,
            'content': self._content
        }
    
    def set_title(self, title):
        self._title = title
        return self
    
    def set_content(self, content):
        self._content = content
        return self
```

### 🔑 Core Properties

#### Widget ID
Each widget has a unique ID:

```python
widget = TextWidget()
print(widget.widget_id)  # 输出: textwidget_a1b2c3d4

# 自定义ID
widget = TextWidget(widget_id="my_text_widget")
print(widget.widget_id)  # 输出: my_text_widget
```

#### Parent Container Reference
Widgets can access their parent email container:

```python
email = Email("测试邮件")
widget = TextWidget().set_content("测试内容")
email.add_widget(widget)

print(widget.parent)  # 输出: <email_widget.email.Email object>
print(widget.parent.title)  # 输出: 测试邮件
```

### 🎨 Template System

Each widget uses Jinja2 templates for rendering:

#### Template Definition
```python
class MyWidget(BaseWidget):
    TEMPLATE = """
    <div class="email-preview-wrapper">
<div style="{{ container_style }}">
        {% if title %}
            <h3 style="{{ title_style }}">{{ title }}</h3>
        {% endif %}
        {% for item in items %}
            <p>{{ item.name }}: {{ item.value }}</p>
        {% endfor %}
    </div>
</div>
    """
```

#### Context Data
```python
def get_template_context(self):
    return {
        'title': self._title,
        'container_style': 'padding: 16px; border: 1px solid #e1dfdd;',
        'title_style': 'color: #323130; font-weight: 600;',
        'items': self._items
    }
```

### 🛡️ Error Handling

BaseWidget provides comprehensive error handling mechanisms:

```python
# 当渲染失败时，会显示错误Info而不是崩溃
try:
    html = widget.render_html()
except Exception as e:
    # Widget会自动处理错误，返回错误TipHTML
    print("Widget渲染失败，但不会影响其他组件")
```

Error output example:
```html
<div class="email-preview-wrapper">
<div style="border: 2px solid #d13438; background: #ffebee; color: #d13438; padding: 12px;">
    <strong>Widget Rendering Error:</strong> MyWidget (mywidget_a1b2c3d4)
    <br/>Error Details: Template rendering failed
</div>
</div>
```

### 🔧 Best Practices

#### 1. Inherit from BaseWidget
```python
class CustomWidget(BaseWidget):
    def __init__(self, widget_id=None):
        super().__init__(widget_id)  # 必须调用父类初始化
        # 初始化自定义属性
```

#### 2. Implement Required Methods
```python
def get_template_context(self):
    """必须实现此方法"""
    return {
        'key': 'value'
    }
```

#### 3. Support Method Chaining
```python
def set_property(self, value):
    self._property = value
    return self  # 返回self支持链式调用
```

#### 4. Input Validation
```python
from email_widget.core.validators import NonEmptyStringValidator

def set_content(self, content):
    validator = NonEmptyStringValidator()
    if not validator.validate(content):
        raise ValueError(f"内容验证失败: {validator.get_error_message(content)}")
    self._content = content
    return self
```

## 🔄 Widget Lifecycle

Understanding the widget lifecycle helps you use EmailWidget more effectively:

1. **Creation Phase**: `__init__()` - Initialize widget properties
2. **Configuration Phase**: `set_*()` methods - Set widget properties
3. **Addition Phase**: `email.add_widget()` - Add to email container
4. **Rendering Phase**: `render_html()` - Generate HTML content

```python
# 1. 创建
widget = TextWidget()

# 2. 配置  
widget.set_content("Hello").set_color("#0078d4")

# 3. 添加
email.add_widget(widget)

# 4. 渲染
html = email.render_html()
```

## 📊 Performance Considerations

### Template Caching
- Templates are automatically cached for better performance on repeated renders
- Recommended to reuse widget instances rather than creating them frequently

### Memory Management
- Widgets maintain weak references to parent containers to avoid circular references
- Clean up unnecessary widget references promptly

---

**Next Step**: Learn about [Widget Overview](widget-overview.md) to see all available widget types.