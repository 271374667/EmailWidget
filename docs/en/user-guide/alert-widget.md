# AlertWidget

AlertWidget is a GitHub-style alert box component used to display various types of notification messages. It supports multiple alert levels, each with corresponding color themes and icons, effectively capturing user attention and conveying important information.

## 🎯 Widget Preview

--8<-- "assets/alert_widget_component_preview.html"

## ✨ Core Features

- **🎨 Multiple Alert Types**: Supports NOTE, TIP, IMPORTANT, WARNING, and CAUTION types
- **🎯 GitHub-Style Design**: Unified visual style and color themes, with dedicated icons for each type
- **⚙️ Flexible Configuration**: Custom titles and icons, with controllable icon display/hide
- **📧 Email Compatible**: Implemented using email client-compatible HTML and CSS
- **🔗 Method Chaining**: Supports method chaining for clean and readable code

## 🚀 Quick Start

### Basic Usage

```python
from email_widget import Email
from email_widget.widgets import AlertWidget
from email_widget.core.enums import AlertType

# Create email
email = Email("Alert Widget Example")

# Create different types of alert boxes
note = AlertWidget().set_content("Please check the attachments in the email").set_alert_type(AlertType.NOTE)
email.add_widget(note)

tip = AlertWidget().set_content("Use Ctrl+S shortcut to save quickly").set_alert_type(AlertType.TIP)
email.add_widget(tip)

# Using shortcut method
email.add_alert("System will undergo maintenance upgrade tonight at 22:00", AlertType.IMPORTANT)

# Export HTML
email.export_html("alert_demo.html")
```

### Advanced Usage

```python
# Custom title and icon
custom_alert = (AlertWidget()
    .set_content("New version released with important security updates")
    .set_alert_type(AlertType.IMPORTANT)
    .set_title("Version Update Notice")
    .set_icon("🚀"))

email.add_widget(custom_alert)

# Hide icon
text_only = (AlertWidget()
    .set_content("Plain text alert message")
    .set_alert_type(AlertType.NOTE)
    .show_icon(False))

email.add_widget(text_only)
```

📚 **Complete API Documentation**: [AlertWidget API](../api/alert-widget.md)

## 🎨 Style Guide

### Alert Types and Theme Colors

- **NOTE**: Blue (#3b82f6) - General tips, explanations, remarks
- **TIP**: Green (#22c55e) - Useful suggestions, tips, tricks  
- **IMPORTANT**: Purple (#8b5cf6) - Important notices, key information
- **WARNING**: Orange (#f97316) - Warning information, risk alerts
- **CAUTION**: Red (#ef4444) - Serious warnings, dangerous operation alerts

### Usage Recommendations

- **NOTE**: For general explanations and reference information
- **TIP**: For providing useful suggestions and optimization tips
- **IMPORTANT**: For emphasizing important information and must-know content
- **WARNING**: For alerting users to risks and potential issues
- **CAUTION**: For serious warnings and dangerous operation alerts

## 📱 Best Practices

### 1. System Notification Email

```python
from email_widget import Email
from email_widget.widgets import AlertWidget
from email_widget.core.enums import AlertType

# Create system notification email
email = Email("System Notification Email")

# Important system maintenance notice
email.add_alert(
    "System will undergo maintenance upgrade from 22:00-24:00 tonight, service will be temporarily unavailable",
    AlertType.IMPORTANT,
    "System Maintenance Notice"
)

# Backup reminder
email.add_alert(
    "We recommend backing up your important data before maintenance",
    AlertType.TIP,
    "Data Backup Suggestion"
)

# Emergency contact information
email.add_alert(
    "For urgent issues, please contact technical support: 400-123-4567",
    AlertType.WARNING,
    "Emergency Contact"
)

# Export HTML file
email.export_html("system_notification.html")
```

--8<-- "assets/temp/alert_system_notification.html"

### 2. Product Release Announcement

```python
# Create product release announcement email
email = Email("Product Release Announcement")

# New feature release
email.add_alert(
    "EmailWidget v2.0 officially released! Added timeline and metric widgets to enhance email display",
    AlertType.TIP,
    "New Version Release"
)

# Important change reminder
email.add_alert(
    "This update includes important security fixes, all users are recommended to upgrade promptly",
    AlertType.IMPORTANT,
    "Security Update"
)

# Compatibility warning
email.add_alert(
    "New version requires Python 3.8+, please check your runtime environment",
    AlertType.WARNING,
    "Compatibility Requirements"
)

email.export_html("product_release_announcement.html")
```

--8<-- "assets/temp/alert_product_release.html"

### 3. Learning Guide Email

```python
# Create learning guide email
email = Email("EmailWidget Learning Guide")

# Learning tips
email.add_alert(
    "Recommend starting with basic widgets and gradually mastering advanced features",
    AlertType.TIP,
    "Learning Suggestions"
)

# Documentation links
email.add_alert(
    "Complete API documentation and sample code are available on the official website",
    AlertType.NOTE,
    "Documentation Resources"
)

# Precautions
email.add_alert(
    "Before using in production, thoroughly test email display in different clients",
    AlertType.CAUTION,
    "Usage Precautions"
)

email.export_html("learning_guide.html")
```

--8<-- "assets/temp/alert_learning_guide.html"

## ⚡ Shortcut Methods

The Email class provides the `add_alert` shortcut method:

```python
# Basic shortcut method
email.add_alert("Alert content", AlertType.NOTE)

# Shortcut method with title
email.add_alert("Important notice content", AlertType.IMPORTANT, "Notice Title")

# Batch add alerts
alerts = [
    ("System maintenance notice", AlertType.WARNING, "Maintenance Reminder"),
    ("New feature release", AlertType.TIP, "Feature Update"), 
    ("Security update", AlertType.IMPORTANT, "Security Alert")
]

for content, alert_type, title in alerts:
    email.add_alert(content, alert_type, title)
```

## 🐛 Common Issues

### Q: Alert box displays abnormally in some email clients?
A: AlertWidget uses email client-compatible CSS implementation, supporting mainstream email clients. If issues occur, please check if custom CSS has overridden component styles.

### Q: How to customize alert box colors?
A: We recommend using predefined AlertType types for consistency. If customization is needed, it can be achieved through CSS override methods.

### Q: Can multiple lines be displayed in one alert box?
A: Multi-line content is supported. Use `\n` or HTML `<br>` tags for line breaks in the content.

### Q: How to hide or customize icons?
A: Use `show_icon(False)` to hide icons, or use `set_icon("🎉")` to set custom icons.

## 🔗 Related Widgets

- [CardWidget](card-widget.md) - Can use alert boxes within cards
- [TextWidget](text-widget.md) - For body content accompanying alert boxes
- [SeparatorWidget](separator-widget.md) - For separating different types of alert information
- [ButtonWidget](button-widget.md) - Can add action buttons after alert boxes