# AlertWidget 警告组件

AlertWidget 是一个GitHub风格的警告框组件，用于显示各种类型的提示信息。它支持多种警告级别，每种类型都有对应的颜色主题和图标，能够有效地吸引用户注意力并传达重要信息。

## 🎯 组件预览

--8<-- "assets/alert_widget_component_preview.html"

## ✨ 核心特性

- **🎨 多种警告类型**: 支持NOTE、TIP、IMPORTANT、WARNING、CAUTION五种类型
- **🎯 GitHub风格设计**: 统一的视觉风格和颜色主题，每种类型都有专属图标
- **⚙️ 灵活配置**: 自定义标题和图标，可控制图标显示/隐藏
- **📧 邮件兼容**: 使用邮件客户端兼容的HTML和CSS实现
- **🔗 链式调用**: 支持方法链式调用，代码简洁易读

## 🚀 快速开始

### 基础用法

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

### 进阶用法

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

📚 **完整API文档**: [AlertWidget API](../api/alert-widget.md)

## 🎨 样式指南

### 警告类型和主题颜色

- **NOTE (注意)**: 蓝色 (#3b82f6) - 一般提示信息、说明、备注
- **TIP (提示)**: 绿色 (#22c55e) - 有用的建议、小贴士、技巧  
- **IMPORTANT (重要)**: 紫色 (#8b5cf6) - 重要通知、关键信息
- **WARNING (警告)**: 橙色 (#f97316) - 警告信息、风险提示
- **CAUTION (危险)**: 红色 (#ef4444) - 严重警告、危险操作提示

### 使用建议

- **NOTE**: 用于一般性说明和参考信息
- **TIP**: 用于提供有用的建议和优化建议
- **IMPORTANT**: 用于强调重要信息和必须关注的内容
- **WARNING**: 用于警告用户注意风险和潜在问题
- **CAUTION**: 用于严重警告和危险操作提示

## 📱 最佳实践

### 1. 系统通知邮件

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

### 2. 产品发布公告

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

### 3. 学习指南邮件

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

## ⚡ 快捷方法

Email 类提供了 `add_alert` 快捷方法：

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

## 🐛 常见问题

### Q: 警告框在某些邮件客户端中样式异常？
A: AlertWidget 采用了邮件客户端兼容的CSS实现，支持主流邮件客户端。如遇问题，请检查是否使用了自定义CSS覆盖了组件样式。

### Q: 如何自定义警告框的颜色？
A: 建议使用预定义的AlertType类型以确保一致性。如需自定义，可以通过CSS覆盖的方式实现。

### Q: 能否在一个警告框中显示多行内容？
A: 支持多行内容，在content中使用`\n`或HTML的`<br>`标签进行换行。

### Q: 如何隐藏或自定义图标？
A: 使用 `show_icon(False)` 隐藏图标，或使用 `set_icon("🎉")` 设置自定义图标。

## 🔗 相关组件

- [CardWidget](card-widget.md) - 可以在卡片中使用警告框
- [TextWidget](text-widget.md) - 用于配合警告框的正文内容
- [SeparatorWidget](separator-widget.md) - 用于分隔不同类型的警告信息
- [ButtonWidget](button-widget.md) - 可以在警告框后添加操作按钮