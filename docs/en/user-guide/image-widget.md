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

# 创建基础图片组件
image = ImageWidget()
image.set_image_url("./charts/sales.png")
image.set_title("销售数据图表")
image.set_description("2024年各季度销售数据对比分析")

email = Email("数据报告")
email.add_widget(image)
```

### Advanced Usage

```python
# 带样式和缓存控制的图片
image = (ImageWidget()
         .set_image_url("https://example.com/chart.png", cache=True)
         .set_title("在线图表")
         .set_size(width="600px")
         .set_border_radius("8px")
         .set_max_width("100%")
         .set_alt_text("销售趋势图表"))

email.add_widget(image)

# 本地文件图片
local_image = (ImageWidget()
               .set_image_url("./reports/monthly_report.jpg")
               .set_title("月度报告")
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

email = Email("业务数据报告")

# 主要数据图表
main_chart = (ImageWidget()
              .set_image_url("./charts/sales_trend.png")
              .set_title("销售趋势分析")
              .set_description("过去12个月的销售数据变化趋势")
              .set_size(width="700px")
              .set_border_radius("6px"))

email.add_widget(main_chart)

# 补充图表
support_chart = (ImageWidget()
                 .set_image_url("./charts/region_comparison.png")
                 .set_title("地区对比")
                 .set_description("各地区销售表现对比")
                 .set_size(width="500px"))

email.add_widget(support_chart)
```

### 2. Product Showcase

```python
from email_widget import Email
from email_widget.widgets import ImageWidget

email = Email("新品发布")

# 产品主图
product_image = (ImageWidget()
                 .set_image_url("./products/new_product.jpg")
                 .set_title("新品展示")
                 .set_description("我们最新推出的革命性产品")
                 .set_size(width="400px", height="300px")
                 .set_border_radius("10px")
                 .set_alt_text("新产品外观图片"))

email.add_widget(product_image)
```

## ⚡ Shortcut Methods

The Email class provides the `add_image` shortcut method:

```python
# 基础快捷方法
email.add_image(
    image_url="./charts/data.png",
    title="数据图表",
    description="关键业务指标展示"
)

# 带样式的快捷方法
email.add_image(
    image_url="./assets/logo.png",
    title="公司Logo",
    width="200px",
    border_radius="8px",
    alt_text="公司标志"
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
image.set_alt_text("2024年销售数据柱状图")
```

## 🔗 Related Widgets

- [ChartWidget](chart-widget.md) - Component specifically for displaying charts
- [CardWidget](card-widget.md) - Card component that can contain images
- [ColumnWidget](column-widget.md) - Used for laying out multiple image components
- [TextWidget](text-widget.md) - Text component that can be used with images