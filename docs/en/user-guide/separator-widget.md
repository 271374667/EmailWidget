# SeparatorWidget

SeparatorWidget is a component for creating visual separator lines in emails. It supports multiple separator styles including solid, dashed, and dotted lines, helping organize email content hierarchy and improve readability.

## 🎯 Widget Preview

--8<-- "assets/separator_component_preview.html"

## ✨ Core Features

- **📏 Multiple Styles**: Supports solid, dashed, and dotted separator styles
- **🎨 Color Themes**: Supports theme color configuration based on StatusType
- **🔧 Flexible Configuration**: Customizable color, thickness, width, and margins
- **📧 Email Compatible**: Implemented using email client-compatible CSS

## 🚀 Quick Start

### Basic Usage

```python
from email_widget import Email
from email_widget.widgets import SeparatorWidget
from email_widget.core.enums import SeparatorType, TextType

# Create email
email = Email("Separator Example")

# Add title
email.add_text("Separator Demo", TextType.TITLE_LARGE)

# Add content
email.add_text("This is content above the separator")

# Create basic separator
separator = SeparatorWidget().set_type(SeparatorType.SOLID)
email.add_widget(separator)

# Add more content
email.add_text("This is content below the separator")

# Use shortcut method
email.add_separator()

# Export HTML
email.export_html("separator_demo.html")
```

### Advanced Usage

```python
from email_widget import Email
from email_widget.widgets import SeparatorWidget
from email_widget.core.enums import SeparatorType, TextType

email = Email("Custom Separator Styles")

# Create styled dashed separator
email.add_text("Dashed Separator Example", TextType.SECTION_H2)
dashed_separator = (SeparatorWidget()
    .set_type(SeparatorType.DASHED)
    .set_color("#0078d4")
    .set_thickness("2px")
    .set_width("80%")
    .set_margin("20px"))

email.add_widget(dashed_separator)

# Use shortcut method to create dotted separator
email.add_text("Dotted Separator Example", TextType.SECTION_H2)
email.add_separator(
    separator_type=SeparatorType.DOTTED,
    color="#ff8c00",
    thickness="3px",
    width="50%"
)

email.export_html("custom_separator_demo.html")
```

📚 **Complete API Documentation**: [SeparatorWidget API](../api/separator-widget.md)

## 🎨 Style Guide

### Separator Types

- **Solid Separator (SOLID)**: Suitable for main content area division, clear section separation
- **Dashed Separator (DASHED)**: Suitable for secondary content division, related content grouping
- **Dotted Separator (DOTTED)**: Suitable for decorative division, lightweight content separation

### Recommended Colors

#### Theme Colors
- **Primary Separator**: #0078d4 (Blue)
- **Success Separator**: #107c10 (Green)
- **Warning Separator**: #ff8c00 (Orange)
- **Error Separator**: #d13438 (Red)

#### Neutral Colors
- **Default Gray**: #e1dfdd
- **Dark Gray**: #8e8e93
- **Light Gray**: #f3f2f1

### Size Recommendations

#### Thickness Recommendations
- **Thin Separator**: 1px - for dense content
- **Standard Separator**: 2px - general scenarios
- **Thick Separator**: 3px - important divisions

#### Width Recommendations
- **Full-width Separator**: 100%
- **Centered Separator**: 80%
- **Decorative Separator**: 50%

## 📱 Best Practices

### 1. Content Hierarchy Division

```python
from email_widget import Email
from email_widget.core.enums import SeparatorType, TextType

email = Email("Hierarchical Content")

# Thick solid lines between main sections
email.add_text("Chapter 1", TextType.TITLE_LARGE)
email.add_text("Chapter content...")
email.add_separator(
    separator_type=SeparatorType.SOLID,
    thickness="2px",
    margin="30px"
)

# Thin dashed lines between subsections
email.add_text("1.1 Subsection", TextType.SECTION_H2)
email.add_text("Subsection content...")
email.add_separator(
    separator_type=SeparatorType.DASHED,
    thickness="1px",
    margin="20px"
)

email.export_html("hierarchical_content.html")
```

--8<-- "assets/separator_hierarchical_content.html"

### 2. Themed Separation

```python
from email_widget import Email
from email_widget.core.enums import SeparatorType, AlertType

email = Email("Themed Separators")

# Separator after success status
email.add_alert("Task Complete", AlertType.TIP)
email.add_separator(
    separator_type=SeparatorType.SOLID,
    color="#107c10",
    thickness="2px"
)

# Separator after warning status
email.add_alert("Important Notice", AlertType.WARNING)
email.add_separator(
    separator_type=SeparatorType.DASHED,
    color="#ff8c00",
    thickness="2px"
)

email.export_html("themed_separators.html")
```

--8<-- "assets/separator_themed_separators.html"

### 3. System Monitoring Email

```python
from email_widget import Email
from email_widget.core.enums import SeparatorType

email = Email("System Status Monitoring")

# Normal service
email.add_text("Web Service: Normal")
email.add_separator(
    separator_type=SeparatorType.SOLID,
    color="#107c10",
    thickness="1px"
)

# Warning service
email.add_text("Database: Warning")
email.add_separator(
    separator_type=SeparatorType.DASHED,
    color="#ff8c00",
    thickness="2px"
)

# Error service
email.add_text("Cache: Error")
email.add_separator(
    separator_type=SeparatorType.SOLID,
    color="#d13438",
    thickness="2px"
)

email.export_html("system_monitoring.html")
```

--8<-- "assets/temp/separator_system_monitoring.html"

## ⚡ Shortcut Methods

The Email class provides the `add_separator` shortcut method:

```python
# Basic shortcut method
email.add_separator()

# Shortcut method with parameters
email.add_separator(
    separator_type=SeparatorType.DASHED,
    color="#0078d4",
    thickness="2px",
    width="80%",
    margin="20px"
)
```

## 🐛 Common Issues

### Q: Separator doesn't display in some email clients?
A: Make sure to use standard CSS border styles, avoid complex CSS properties. SeparatorWidget has been optimized for mainstream email clients.

### Q: How to create gradient separators?
A: Due to email client limitations, solid colors are recommended. For visual hierarchy, use different color shades.

### Q: Separator too thin or too thick?
A: Adjust the `thickness` property, recommend using values between 1px-3px for good display.

### Q: How to center the separator?
A: Separators are centered by default, you can control width through the `width` property, e.g., `set_width("80%")` creates a centered 80% width separator.

## 🔗 Related Widgets

- [TextWidget](text-widget.md) - For title text before and after separators
- [CardWidget](card-widget.md) - Can use separators between cards
- [ColumnWidget](column-widget.md) - For separation in multi-column layouts
- [AlertWidget](alert-widget.md) - Alert information that can be combined with separators