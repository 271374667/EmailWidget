# ImageWidget

ImageWidget is a component specifically designed for displaying images in emails, supporting multiple image sources and automatically converting to email-compatible formats. It can handle local files, network images, and Base64 data, making it an important component for displaying report charts, product images, and visual content.

## 🎯 Widget Preview

--8<-- "assets/image_widget_component_preview.html"

## ✨ Core Features

- **📁 Multiple Sources**: Supports various image sources including local files, network URLs, Base64 data
- **🔄 Auto Conversion**: Automatically converts to email-compatible base64 embedded format
- **🎨 Style Control**: Supports size, border radius, max width and other style settings
- **📝 Title Description**: Supports image title and detailed description display
- **♿ Accessibility**: Supports alternative text for accessibility
- **📧 Email Compatible**: Implemented using email client-compatible HTML and CSS

## 🚀 Quick Start

### Basic Usage

```python
from email_widget import Email
from email_widget.widgets import ImageWidget

# Create basic image widget
image = ImageWidget()
image.set_image_url("./charts/sales.png")
image.set_title("Sales Data Chart")
image.set_description("2024 quarterly sales data comparison analysis")

email = Email("Data Report")
email.add_widget(image)
```

### Advanced Usage

```python
# Image with styling and cache control
image = (ImageWidget()
         .set_image_url("https://example.com/chart.png", cache=True)
         .set_title("Online Chart")
         .set_size(width="600px")
         .set_border_radius("8px")
         .set_max_width("100%")
         .set_alt_text("Sales trend chart"))

email.add_widget(image)

# Local file image
local_image = (ImageWidget()
               .set_image_url("./reports/monthly_report.jpg")
               .set_title("Monthly Report")
               .set_size(width="400px", height="300px"))
```

📚 **Complete API Documentation**: [ImageWidget API](../api/image-widget.md)

## 🎨 Style Guide

### Image Size Recommendations

- **Small Icons**: 50px - 100px, suitable for status icons
- **Regular Images**: 300px - 600px, suitable for content display
- **Large Banners**: 800px+, suitable for main display content
- **Responsive**: Use `max_width="100%"` to ensure email compatibility

### File Format Support

- **PNG**: Best quality, supports transparent background
- **JPEG**: Suitable for photos, smaller file size
- **GIF**: Supports animation effects
- **WebP**: Modern format, small size but poor compatibility

## 📱 Best Practices

### 1. Report Chart Display

```python
from email_widget import Email
from email_widget.widgets import ImageWidget

email = Email("Business Data Report")

# Main data chart
main_chart = (ImageWidget()
              .set_image_url("./charts/sales_trend.png")
              .set_title("Sales Trend Analysis")
              .set_description("Sales data change trends over the past 12 months")
              .set_size(width="700px")
              .set_border_radius("6px"))

email.add_widget(main_chart)

# Supporting chart
support_chart = (ImageWidget()
                 .set_image_url("./charts/region_comparison.png")
                 .set_title("Regional Comparison")
                 .set_description("Sales performance comparison by region")
                 .set_size(width="500px"))

email.add_widget(support_chart)
```

### 2. Product Showcase

```python
from email_widget import Email
from email_widget.widgets import ImageWidget

email = Email("New Product Launch")

# Product main image
product_image = (ImageWidget()
                 .set_image_url("./products/new_product.jpg")
                 .set_title("New Product Showcase")
                 .set_description("Our latest revolutionary product")
                 .set_size(width="400px", height="300px")
                 .set_border_radius("10px")
                 .set_alt_text("New product appearance image"))

email.add_widget(product_image)
```

## ⚡ Shortcut Methods

The Email class provides the `add_image` shortcut method:

```python
# Basic shortcut method
email.add_image(
    image_url="./charts/data.png",
    title="Data Chart",
    description="Key business metrics display"
)

# Shortcut method with styling
email.add_image(
    image_url="./assets/logo.png",
    title="Company Logo",
    width="200px",
    border_radius="8px",
    alt_text="Company logo"
)
```

## 🐛 Common Issues

### Q: What to do when images don't display in emails?
A: Check the following:
- Ensure image file path is correct
- Network image URLs are accessible
- Image format is common format (PNG, JPEG, etc.)

### Q: How to control image size?
A: Use `set_size()` and `set_max_width()`:
```python
image.set_size(width="600px").set_max_width("100%")
```

### Q: Are dynamic images supported?
A: Yes, use `cache=False` to disable caching:
```python
image.set_image_url("./dynamic/chart.png", cache=False)
```

### Q: How to ensure accessibility?
A: Always set meaningful alternative text:
```python
image.set_alt_text("2024 sales data bar chart")
```

## 🔗 Related Widgets

- [ChartWidget](chart-widget.md) - Component specifically for displaying charts
- [CardWidget](card-widget.md) - Card component that can contain images
- [ColumnWidget](column-widget.md) - Used for laying out multiple image components
- [TextWidget](text-widget.md) - Text component that can be used with images