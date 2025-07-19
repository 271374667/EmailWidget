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

# Create basic text
text = TextWidget()
text.set_content("This is a regular text")
text.set_type(TextType.BODY)

email = Email("Text Widget Example")
email.add_widget(text)
```

### Advanced Usage

```python
# Method chaining for style setting
styled_text = (TextWidget()
              .set_content("Important Title")
              .set_type(TextType.SECTION_H2)
              .set_color("#0078d4")
              .set_align("center"))

email.add_widget(styled_text)

# Using shortcut method
email.add_text("Text created with shortcut method", TextType.BODY)
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

# Create structured document
email = Email("Project Report")

# Main title
email.add_text("2024 Q1 Project Progress Report", TextType.TITLE_LARGE)

# Section title
email.add_text("Project Overview", TextType.SECTION_H2)
email.add_text("This quarter mainly completed the development of user system and data analysis modules.", TextType.BODY)

# Subsections
email.add_text("User System Module", TextType.SECTION_H3)
email.add_text("Implemented core functions including user registration, login, and permission management.", TextType.BODY)

email.add_text("Data Analysis Module", TextType.SECTION_H3)
email.add_text("Completed data collection, cleaning, and basic analysis functions.", TextType.BODY)

# Export
email.export_html("structured_document.html")
```

### 2. Emphasized and Formatted Text

```python
from email_widget import Email
from email_widget.widgets.text_widget import TextWidget
from email_widget.core.enums import TextType

email = Email("Formatted Text Example")

# Emphasize important information
important_text = (TextWidget()
                 .set_content("Important Notice: System maintenance will be performed tonight")
                 .set_type(TextType.BODY)
                 .set_color("#d13438")
                 .set_align("center"))
email.add_widget(important_text)

# Success information
success_text = (TextWidget()
               .set_content("✅ Project has been successfully deployed to production")
               .set_type(TextType.BODY)
               .set_color("#107c10"))
email.add_widget(success_text)

# HTML formatting
html_text = (TextWidget()
            .set_content("Supports <strong>bold</strong>, <em>italic</em> and <u>underline</u>")
            .set_type(TextType.BODY))
email.add_widget(html_text)
```

## ⚡ Shortcut Methods

The Email class provides the `add_text` shortcut method:

```python
# Basic shortcut method
email.add_text("This is a text")

# Shortcut method with type
email.add_text("This is a title", TextType.SECTION_H2)

# Shortcut method with style
email.add_text("Emphasized text", TextType.BODY, color="#0078d4", align="center")
```

## 🐛 Common Issues

### Q: How to create multi-line text?
A: Use line breaks or HTML `<br>` tags in the content:
```python
text.set_content("Line 1\nLine 2\nLine 3")
# or
text.set_content("Line 1<br>Line 2<br>Line 3")
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