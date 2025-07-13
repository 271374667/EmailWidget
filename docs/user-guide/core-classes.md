# 核心类

EmailWidget 的核心架构由两个主要类组成：`Email` 类和 `BaseWidget` 抽象基类。理解这两个类是掌握 EmailWidget 的关键。

## 📧 Email 类

`Email` 类是整个邮件System的Container，负责管理所有的组件（Widget）并生成最终的HTML邮件。

### 🏗️ 基本结构

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

### 📝 主要方法

#### 创建和配置

```python
# 基本创建
email = Email("Data报告")

# 设置副Title
email.set_subtitle("2024年度业务Data分析")

# 设置页脚Text
email.set_footer("本报告由Data团队生成 © 2024")
```

#### 添加组件

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

#### 渲染和输出

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

### 🎨 邮件模板结构

Email 类使用内置的HTML模板，结构如下：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <!-- 内联CSS样式 -->
</head>
<body>
    <div class="email-container">
        <!-- 邮件头部 -->
        <div class="email-header">
            <h1>{{ title }}</h1>
            {{ subtitle }}
        </div>
        
        <!-- 邮件主体 -->
        <div class="email-body">
            {{ widget_content }}
        </div>
        
        <!-- 邮件页脚 -->
        <div class="email-footer">
            {{ footer_text }}
        </div>
    </div>
</body>
</html>
```

## 🧩 BaseWidget 抽象基类

所有的组件都继承自 `BaseWidget` 抽象基类，它定义了组件的基本行为和接口。

### 🏗️ 基本特性

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

### 🔑 核心属性

#### Widget ID
每个Widget都有唯一的ID：

```python
widget = TextWidget()
print(widget.widget_id)  # 输出: textwidget_a1b2c3d4

# 自定义ID
widget = TextWidget(widget_id="my_text_widget")
print(widget.widget_id)  # 输出: my_text_widget
```

#### 父ContainerQuote
Widget可以访问其父EmailContainer：

```python
email = Email("测试邮件")
widget = TextWidget().set_content("测试内容")
email.add_widget(widget)

print(widget.parent)  # 输出: <email_widget.email.Email object>
print(widget.parent.title)  # 输出: 测试邮件
```

### 🎨 模板System

每个Widget使用Jinja2模板进行渲染：

#### 模板定义
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

#### 上下文Data
```python
def get_template_context(self):
    return {
        'title': self._title,
        'container_style': 'padding: 16px; border: 1px solid #e1dfdd;',
        'title_style': 'color: #323130; font-weight: 600;',
        'items': self._items
    }
```

### 🛡️ 错误处理

BaseWidget 提供了完善的错误处理机制：

```python
# 当渲染失败时，会显示错误Info而不是崩溃
try:
    html = widget.render_html()
except Exception as e:
    # Widget会自动处理错误，返回错误TipHTML
    print("Widget渲染失败，但不会影响其他组件")
```

错误输出示例：
```html
<div class="email-preview-wrapper">
<div style="border: 2px solid #d13438; background: #ffebee; color: #d13438; padding: 12px;">
    <strong>Widget渲染错误:</strong> MyWidget (mywidget_a1b2c3d4)
    <br/>错误详情: 模板渲染失败
</div>
</div>
```

### 🔧 最佳实践

#### 1. 继承BaseWidget
```python
class CustomWidget(BaseWidget):
    def __init__(self, widget_id=None):
        super().__init__(widget_id)  # 必须调用父类初始化
        # 初始化自定义属性
```

#### 2. 实现必需方法
```python
def get_template_context(self):
    """必须实现此方法"""
    return {
        'key': 'value'
    }
```

#### 3. 支持链式调用
```python
def set_property(self, value):
    self._property = value
    return self  # 返回self支持链式调用
```

#### 4. 输入验证
```python
from email_widget.core.validators import NonEmptyStringValidator

def set_content(self, content):
    validator = NonEmptyStringValidator()
    if not validator.validate(content):
        raise ValueError(f"内容验证失败: {validator.get_error_message(content)}")
    self._content = content
    return self
```

## 🔄 组件生命周期

理解组件的生命周期有助于更好地使用EmailWidget：

1. **创建阶段**: `__init__()` - 初始化组件属性
2. **配置阶段**: `set_*()` 方法 - 设置组件属性
3. **添加阶段**: `email.add_widget()` - 添加到邮件Container
4. **渲染阶段**: `render_html()` - 生成HTML内容

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

## 📊 性能考虑

### 模板缓存
- 模板会自动缓存，重复渲染时性能更好
- 建议复用Widget实例而不是频繁创建

### 内存管理
- Widget保持对父Container的弱Quote，避免循环Quote
- 及时清理不需要的WidgetQuote

---

**下一步**: 了解 [组件概览](widget-overview.md) 查看所有可用的组件类型。 