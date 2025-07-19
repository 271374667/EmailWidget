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

# 创建邮件
email = Email("按钮示例")

# 创建基础按钮
button = ButtonWidget().set_text("点击访问").set_href("https://example.com")
email.add_widget(button)

# 使用快捷方法
email.add_button("立即购买", "https://shop.example.com")

# 导出HTML
email.export_html("button_demo.html")
```

### Advanced Usage

```python
# 创建带样式的按钮
styled_button = (ButtonWidget()
    .set_text("立即开始")
    .set_href("https://app.example.com/start")
    .set_background_color("#22c55e")  # 绿色背景
    .set_text_color("#ffffff")        # 白色文字
    .set_width("200px")               # 固定宽度
    .set_align("center"))             # 居中对齐

email.add_widget(styled_button)

# 多样式按钮组合
primary_button = (ButtonWidget()
    .set_text("主要操作")
    .set_href("https://example.com/primary")
    .set_background_color("#3b82f6")
    .set_text_color("#ffffff")
    .set_width("180px"))

secondary_button = (ButtonWidget()
    .set_text("次要操作")
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

email = Email("限时特惠活动")

# 主要购买按钮
buy_button = (ButtonWidget()
    .set_text("立即抢购")
    .set_href("https://shop.example.com/sale")
    .set_background_color("#ef4444")
    .set_text_color("#ffffff")
    .set_width("100%")
    .set_align("center"))

email.add_widget(buy_button)

# 次要了解按钮
info_button = (ButtonWidget()
    .set_text("查看详情")
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

email = Email("系统维护通知")

email.add_text("系统将于今晚进行维护，预计耗时2小时。")

# 查看详情按钮
detail_button = (ButtonWidget()
    .set_text("查看维护详情")
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

email = Email("产品功能介绍")

# 使用列布局并排显示按钮
column = ColumnWidget().set_columns(2)

# 免费试用按钮
trial_button = (ButtonWidget()
    .set_text("免费试用")
    .set_href("https://app.example.com/trial")
    .set_background_color("#22c55e")
    .set_text_color("#ffffff")
    .set_width("100%"))

# 查看定价按钮
pricing_button = (ButtonWidget()
    .set_text("查看定价")
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

email = Email("兼容性优化示例")

# 推荐做法
compatible_button = (ButtonWidget()
    .set_text("立即访问")
    .set_href("https://example.com")
    .set_background_color("#3b82f6")  # 使用具体颜色值
    .set_text_color("#ffffff")        # 确保高对比度
    .set_width("180px")               # 设置明确宽度
    .set_align("center"))

email.add_widget(compatible_button)
```

--8<-- "assets/temp/button_compatibility_optimization.html"

## ⚡ Shortcut Methods

The Email class provides the `add_button` shortcut method:

```python
# 基础快捷方法
email.add_button("按钮文本", "链接地址")

# 带样式的快捷方法
email.add_button(
    "立即购买",
    "https://shop.example.com",
    background_color="#22c55e",
    text_color="#ffffff", 
    width="200px",
    align="center"
)

# 不同类型的链接
email.add_button("发送邮件", "mailto:contact@example.com")
email.add_button("拨打电话", "tel:+1234567890")
email.add_button("访问网站", "https://example.com")
```

## 🐛 Common Issues

### Q: Button displays abnormally in some email clients?
A: Ensure using recommended style settings, avoid complex CSS properties:
```python
# 推荐做法
button.set_background_color("#3b82f6")  # 具体颜色值
button.set_width("180px")               # 明确宽度
```

### Q: How to ensure button text is clear and readable?
A: Ensure sufficient contrast between text and background:
```python
# 高对比度组合
button.set_background_color("#1f2937").set_text_color("#ffffff")  # ✅
# 避免低对比度
# button.set_background_color("#e5e7eb").set_text_color("#f3f4f6")  # ❌
```

### Q: Can icons be added to buttons?
A: Yes, use Unicode icon characters:
```python
button.set_text("📧 发送邮件")
button.set_text("🛒 立即购买")
button.set_text("📞 联系我们")
```

### Q: How to design mobile-friendly buttons?
A: Use appropriate sizes and full-width design:
```python
mobile_button = (ButtonWidget()
    .set_text("移动端按钮")
    .set_width("100%")          # 全宽适配
    .set_align("center"))       # 居中对齐
```

### Q: Button link security considerations?
A: Always use HTTPS links to ensure security:
```python
button.set_href("https://example.com")  # ✅ 安全
# button.set_href("http://example.com")   # ❌ 不安全
```

## 🔗 Related Widgets

- [TextWidget](text-widget.md) - For explanatory text around buttons
- [ColumnWidget](column-widget.md) - For multi-button layout management
- [CardWidget](card-widget.md) - Card container that can contain buttons
- [AlertWidget](alert-widget.md) - Alert information that can be combined with buttons