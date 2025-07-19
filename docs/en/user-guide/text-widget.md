# TextWidget

TextWidget is the most basic and commonly used widget in EmailWidget, designed to display various text content. It supports multiple text types, alignment options, and style configurations, making it the core component for building email content.

## 🎯 Widget Preview

--8<-- "assets/text_widget_component_preview.html"

## ✨ Core Features

- **📝 Multiple Types**: Supports various text types including titles, body text, and captions
- **🎨 Style Customization**: Supports custom colors, alignment, font styles, and more
- **📊 Auto Numbering**: Automatically displays numeric numbering for H2 to H5 headings
- **🔗 HTML Support**: Supports basic HTML tags and formatted text
- **📧 Email Compatible**: Implemented using email client-compatible HTML and CSS

## 🚀 Quick Start

### Basic Usage

```python
from email_widget import Email
from email_widget.widgets import TextWidget
from email_widget.core.enums import TextType

# 创建基本文本
text = TextWidget()
text.set_content("这是一段普通文本")
text.set_type(TextType.BODY)

email = Email("文本组件示例")
email.add_widget(text)
```

### Advanced Usage

```python
# 链式调用设置样式
styled_text = (TextWidget()
              .set_content("重要标题")
              .set_type(TextType.SECTION_H2)
              .set_color("#0078d4")
              .set_align("center"))

email.add_widget(styled_text)

# 使用快捷方法
email.add_text("快捷方法创建的文本", TextType.BODY)
```

📚 **Complete API Documentation**: [TextWidget API](../api/text-widget.md)

## 🎨 Style Guide

### Text Types and Hierarchy

- **TITLE_LARGE**: Large title - for main email title
- **TITLE_SMALL**: Small title - for subtitle
- **SECTION_H2**: H2 heading - auto-numbered (1. Title)
- **SECTION_H3**: H3 heading - auto-numbered (1.1. Title)
- **SECTION_H4**: H4 heading - auto-numbered (1.1.1. Title)
- **SECTION_H5**: H5 heading - auto-numbered (1.1.1.1. Title)
- **BODY**: Body text - paragraph content
- **CAPTION**: Caption text - image captions, supplementary information

### Color Recommendations

- **Primary Content**: #323130 (Dark Gray)
- **Emphasis Content**: #0078d4 (Blue)
- **Success Information**: #107c10 (Green)
- **Warning Information**: #ff8c00 (Orange)
- **Error Information**: #d13438 (Red)

## 📱 Best Practices

### 1. Structured Document Content

```python
from email_widget import Email
from email_widget.widgets.text_widget import TextWidget
from email_widget.core.enums import TextType

# 创建结构化文档
email = Email("项目报告")

# 主标题
email.add_text("2024年Q1项目进展报告", TextType.TITLE_LARGE)

# 章节标题
email.add_text("项目概述", TextType.SECTION_H2)
email.add_text("本季度主要完成了用户系统和数据分析模块的开发工作。", TextType.BODY)

# 子章节
email.add_text("用户系统模块", TextType.SECTION_H3)
email.add_text("实现了用户注册、登录、权限管理等核心功能。", TextType.BODY)

email.add_text("数据分析模块", TextType.SECTION_H3)
email.add_text("完成了数据采集、清洗和基础分析功能。", TextType.BODY)

# 导出
email.export_html("structured_document.html")
```

### 2. Emphasized and Formatted Text

```python
from email_widget import Email
from email_widget.widgets.text_widget import TextWidget
from email_widget.core.enums import TextType

email = Email("格式化文本示例")

# 强调重要信息
important_text = (TextWidget()
                 .set_content("重要通知：系统将于今晚进行维护")
                 .set_type(TextType.BODY)
                 .set_color("#d13438")
                 .set_align("center"))
email.add_widget(important_text)

# 成功信息
success_text = (TextWidget()
               .set_content("✅ 项目已成功部署到生产环境")
               .set_type(TextType.BODY)
               .set_color("#107c10"))
email.add_widget(success_text)

# HTML格式化
html_text = (TextWidget()
            .set_content("支持 <strong>粗体</strong>、<em>斜体</em> 和 <u>下划线</u>")
            .set_type(TextType.BODY))
email.add_widget(html_text)
```

## ⚡ Shortcut Methods

The Email class provides the `add_text` shortcut method:

```python
# 基础快捷方法
email.add_text("这是一段文本")

# 带类型的快捷方法
email.add_text("这是标题", TextType.SECTION_H2)

# 带样式的快捷方法
email.add_text("强调文本", TextType.BODY, color="#0078d4", align="center")
```

## 🐛 Common Issues

### Q: How to create multi-line text?
A: Use line breaks or HTML `<br>` tags in the content:
```python
text.set_content("第一行\n第二行\n第三行")
# 或者
text.set_content("第一行<br>第二行<br>第三行")
```

### Q: How does title numbering work?
A: H2 to H5 headings are automatically numbered by hierarchy:
- H2: 1. Title
- H3: 1.1. Title  
- H4: 1.1.1. Title
- H5: 1.1.1.1. Title

### Q: What HTML tags are supported?
A: Basic formatting tags like `<strong>`, `<em>`, `<u>`, `<br>` are supported, but simple tags are recommended to ensure email client compatibility.

## 🔗 Related Widgets

- [SeparatorWidget](separator-widget.md) - Content separator lines
- [AlertWidget](alert-widget.md) - Alert information text
- [CardWidget](card-widget.md) - Cards containing text
- [QuoteWidget](quote-widget.md) - Quoted text
- [ButtonWidget](button-widget.md) - Button text