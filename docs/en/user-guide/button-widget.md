# ButtonWidget

ButtonWidget is a component specifically designed for creating clickable buttons in emails. It provides powerful customization features, supports various styles, colors, and alignment options, and is fully compatible with major email clients.

## 🎯 Widget Preview

--8<-- "assets/button_widget_component_preview.html"

## ✨ Core Features

- **📱 Email Client Compatible**: Optimized for major email clients (Outlook, Gmail, Apple Mail, etc.)
- **🎨 Style Customization**: Supports background color, text color, width, alignment, and many other style options
- **🔗 Link Navigation**: Supports various link types including web links, email links, etc.
- **📐 Flexible Alignment**: Supports left, center, and right alignment
- **🎯 Responsive Design**: Automatically adapts to different devices and email client displays

## 🚀 Quick Start

### Basic Usage

```python
from email_widget import Email
from email_widget.widgets import ButtonWidget

# Create email
email = Email("Button Example")

# Create basic button
button = ButtonWidget().set_text("Click to Visit").set_href("https://example.com")
email.add_widget(button)

# Using shortcut method
email.add_button("Buy Now", "https://shop.example.com")

# Export HTML
email.export_html("button_demo.html")
```

### Advanced Usage

```python
# Create styled button
styled_button = (ButtonWidget()
    .set_text("Get Started")
    .set_href("https://app.example.com/start")
    .set_background_color("#22c55e")  # Green background
    .set_text_color("#ffffff")        # White text
    .set_width("200px")               # Fixed width
    .set_align("center"))             # Center alignment

email.add_widget(styled_button)

# Multi-style button combination
primary_button = (ButtonWidget()
    .set_text("Primary Action")
    .set_href("https://example.com/primary")
    .set_background_color("#3b82f6")
    .set_text_color("#ffffff")
    .set_width("180px"))

secondary_button = (ButtonWidget()
    .set_text("Secondary Action")
    .set_href("https://example.com/secondary")
    .set_background_color("#6b7280")
    .set_text_color("#ffffff")
    .set_width("150px"))

email.add_widget(primary_button)
email.add_widget(secondary_button)
```

📚 **Complete API Documentation**: [ButtonWidget API](../api/button-widget.md)

## 🎨 Style Guide

### Recommended Color Combinations

#### Primary Button
- **Background**: #3b82f6 (Blue)
- **Text**: #ffffff (White)
- **Usage**: Main actions, important buttons

#### Success Button
- **Background**: #22c55e (Green)
- **Text**: #ffffff (White)
- **Usage**: Confirm actions, purchase buttons

#### Warning Button
- **Background**: #f59e0b (Orange)
- **Text**: #ffffff (White)
- **Usage**: Actions requiring attention

#### Danger Button
- **Background**: #ef4444 (Red)
- **Text**: #ffffff (White)
- **Usage**: Delete actions, unsubscribe

#### Secondary Button
- **Background**: #6b7280 (Gray)
- **Text**: #ffffff (White)
- **Usage**: Auxiliary actions, learn more

### Size Recommendations

- **Small Button**: 120px - for auxiliary actions
- **Medium Button**: 180px - standard button size
- **Large Button**: 250px - important actions
- **Full-width Button**: 100% - mobile-friendly

## 📱 Best Practices

### 1. E-commerce Marketing Email

```python
from email_widget import Email
from email_widget.widgets import ButtonWidget

email = Email("Limited Time Sale")

# Primary purchase button
buy_button = (ButtonWidget()
    .set_text("Buy Now")
    .set_href("https://shop.example.com/sale")
    .set_background_color("#ef4444")
    .set_text_color("#ffffff")
    .set_width("100%")
    .set_align("center"))

email.add_widget(buy_button)

# Secondary info button
info_button = (ButtonWidget()
    .set_text("View Details")
    .set_href("https://shop.example.com/products")
    .set_background_color("#6b7280")
    .set_text_color("#ffffff")
    .set_width("150px")
    .set_align("center"))

email.add_widget(info_button)
```

--8<-- "assets/temp/button_ecommerce_email.html"

### 2. System Notification Email

```python
from email_widget import Email
from email_widget.widgets import ButtonWidget

email = Email("System Maintenance Notice")

email.add_text("System will undergo maintenance tonight, estimated duration: 2 hours.")

# View details button
detail_button = (ButtonWidget()
    .set_text("View Maintenance Details")
    .set_href("https://status.example.com/maintenance")
    .set_background_color("#3b82f6")
    .set_text_color("#ffffff")
    .set_width("180px")
    .set_align("center"))

email.add_widget(detail_button)
```

--8<-- "assets/temp/button_system_notification.html"

### 3. Product Introduction Email

```python
from email_widget import Email
from email_widget.widgets import ButtonWidget, ColumnWidget

email = Email("Product Feature Introduction")

# Use column layout for side-by-side buttons
column = ColumnWidget().set_columns(2)

# Free trial button
trial_button = (ButtonWidget()
    .set_text("Free Trial")
    .set_href("https://app.example.com/trial")
    .set_background_color("#22c55e")
    .set_text_color("#ffffff")
    .set_width("100%"))

# View pricing button
pricing_button = (ButtonWidget()
    .set_text("View Pricing")
    .set_href("https://example.com/pricing")
    .set_background_color("#3b82f6")
    .set_text_color("#ffffff")
    .set_width("100%"))

column.add_widgets([trial_button, pricing_button])
email.add_widget(column)
```

--8<-- "assets/temp/button_product_introduction.html"

### 4. Email Client Compatibility Optimization

```python
from email_widget import Email
from email_widget.widgets import ButtonWidget

email = Email("Compatibility Optimization Example")

# Recommended approach
compatible_button = (ButtonWidget()
    .set_text("Visit Now")
    .set_href("https://example.com")
    .set_background_color("#3b82f6")  # Use specific color values
    .set_text_color("#ffffff")        # Ensure high contrast
    .set_width("180px")               # Set explicit width
    .set_align("center"))

email.add_widget(compatible_button)
```

--8<-- "assets/temp/button_compatibility_optimization.html"

## ⚡ Shortcut Methods

The Email class provides the `add_button` shortcut method:

```python
# Basic shortcut method
email.add_button("Button Text", "Link URL")

# Shortcut method with styling
email.add_button(
    "Buy Now",
    "https://shop.example.com",
    background_color="#22c55e",
    text_color="#ffffff", 
    width="200px",
    align="center"
)

# Different types of links
email.add_button("Send Email", "mailto:contact@example.com")
email.add_button("Call Phone", "tel:+1234567890")
email.add_button("Visit Website", "https://example.com")
```

## 🐛 Common Issues

### Q: Button displays abnormally in some email clients?
A: Ensure using recommended style settings, avoid complex CSS properties:
```python
# Recommended approach
button.set_background_color("#3b82f6")  # Specific color values
button.set_width("180px")               # Explicit width
```

### Q: How to ensure button text is clear and readable?
A: Ensure sufficient contrast between text and background:
```python
# High contrast combinations
button.set_background_color("#1f2937").set_text_color("#ffffff")  # ✅
# Avoid low contrast
# button.set_background_color("#e5e7eb").set_text_color("#f3f4f6")  # ❌
```

### Q: Can icons be added to buttons?
A: Yes, use Unicode icon characters:
```python
button.set_text("📧 Send Email")
button.set_text("🛒 Buy Now")
button.set_text("📞 Contact Us")
```

### Q: How to design mobile-friendly buttons?
A: Use appropriate sizes and full-width design:
```python
mobile_button = (ButtonWidget()
    .set_text("Mobile Button")
    .set_width("100%")          # Full width adaptation
    .set_align("center"))       # Center alignment
```

### Q: Button link security considerations?
A: Always use HTTPS links to ensure security:
```python
button.set_href("https://example.com")  # ✅ Secure
# button.set_href("http://example.com")   # ❌ Insecure
```

## 🔗 Related Widgets

- [TextWidget](text-widget.md) - For explanatory text around buttons
- [ColumnWidget](column-widget.md) - For multi-button layout management
- [CardWidget](card-widget.md) - Card container that can contain buttons
- [AlertWidget](alert-widget.md) - Alert information that can be combined with buttons