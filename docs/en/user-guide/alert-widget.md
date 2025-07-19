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

# 创建邮件
email = Email("警告组件示例")

# 创建不同类型的警告框
note = AlertWidget().set_content("请注意查收邮件中的附件").set_alert_type(AlertType.NOTE)
email.add_widget(note)

tip = AlertWidget().set_content("使用快捷键 Ctrl+S 可以快速保存").set_alert_type(AlertType.TIP)
email.add_widget(tip)

# 使用快捷方法
email.add_alert("系统将在今晚22:00进行升级维护", AlertType.IMPORTANT)

# 导出HTML
email.export_html("alert_demo.html")
```

### Advanced Usage

```python
# 自定义标题和图标
custom_alert = (AlertWidget()
    .set_content("新版本已发布，包含重要安全更新")
    .set_alert_type(AlertType.IMPORTANT)
    .set_title("版本更新通知")
    .set_icon("🚀"))

email.add_widget(custom_alert)

# 隐藏图标
text_only = (AlertWidget()
    .set_content("纯文本警告信息")
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

# 创建系统通知邮件
email = Email("系统通知邮件")

# 重要系统维护通知
email.add_alert(
    "系统将在今晚22:00-24:00进行维护升级，期间服务将暂停使用",
    AlertType.IMPORTANT,
    "系统维护通知"
)

# 备份提醒
email.add_alert(
    "建议在维护前备份您的重要数据",
    AlertType.TIP,
    "数据备份建议"
)

# 紧急联系方式
email.add_alert(
    "如遇紧急问题，请联系技术支持：400-123-4567",
    AlertType.WARNING,
    "紧急联系方式"
)

# 导出HTML文件
email.export_html("system_notification.html")
```

--8<-- "assets/temp/alert_system_notification.html"

### 2. Product Release Announcement

```python
# 创建产品发布公告邮件
email = Email("产品发布公告")

# 新功能发布
email.add_alert(
    "EmailWidget v2.0正式发布！新增时间线和指标组件，提升邮件展示效果",
    AlertType.TIP,
    "新版本发布"
)

# 重要变更提醒
email.add_alert(
    "本次更新包含重要的安全修复，建议所有用户尽快升级",
    AlertType.IMPORTANT,
    "安全更新"
)

# 兼容性警告
email.add_alert(
    "新版本要求Python 3.8+，请检查您的运行环境",
    AlertType.WARNING,
    "兼容性要求"
)

email.export_html("product_release_announcement.html")
```

--8<-- "assets/temp/alert_product_release.html"

### 3. Learning Guide Email

```python
# 创建学习指南邮件
email = Email("EmailWidget学习指南")

# 学习提示
email.add_alert(
    "建议从基础组件开始学习，逐步掌握高级功能",
    AlertType.TIP,
    "学习建议"
)

# 文档链接
email.add_alert(
    "完整的API文档和示例代码可在官网查看",
    AlertType.NOTE,
    "文档资源"
)

# 注意事项
email.add_alert(
    "在生产环境使用前，请充分测试邮件在不同客户端的显示效果",
    AlertType.CAUTION,
    "使用注意"
)

email.export_html("learning_guide.html")
```

--8<-- "assets/temp/alert_learning_guide.html"

## ⚡ Shortcut Methods

The Email class provides the `add_alert` shortcut method:

```python
# 基础快捷方法
email.add_alert("提示内容", AlertType.NOTE)

# 带标题的快捷方法
email.add_alert("重要通知内容", AlertType.IMPORTANT, "通知标题")

# 批量添加警告
alerts = [
    ("系统维护通知", AlertType.WARNING, "维护提醒"),
    ("新功能发布", AlertType.TIP, "功能更新"), 
    ("安全更新", AlertType.IMPORTANT, "安全提醒")
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