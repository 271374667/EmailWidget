# ButtonWidget 按钮组件

ButtonWidget 是一个专门用于在邮件中创建可点击按钮的组件。它提供了强大的定制功能，支持多种样式、颜色和对齐方式，完全兼容各大邮件客户端。

## 🎯 组件预览

--8<-- "assets/button_widget_component_preview.html"

## ✨ 核心特性

- **📱 邮件客户端兼容**: 专为各大邮件客户端（Outlook、Gmail、Apple Mail等）优化
- **🎨 样式定制**: 支持背景颜色、文字颜色、宽度、对齐方式等多种样式选项
- **🔗 链接跳转**: 支持各种链接类型，包括网页链接、邮件链接等
- **📐 灵活对齐**: 支持左对齐、居中、右对齐三种对齐方式
- **🎯 响应式设计**: 自动适配不同设备和邮件客户端的显示效果

## 🚀 快速开始

### 基础用法

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

### 进阶用法

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

📚 **完整API文档**: [ButtonWidget API](../api/button-widget.md)

## 🎨 样式指南

### 推荐颜色搭配

#### 主要按钮（Primary）
- **背景色**: #3b82f6 (蓝色)
- **文字色**: #ffffff (白色)
- **用途**: 主要操作、重要按钮

#### 成功按钮（Success）
- **背景色**: #22c55e (绿色)
- **文字色**: #ffffff (白色)
- **用途**: 确认操作、购买按钮

#### 警告按钮（Warning）
- **背景色**: #f59e0b (橙色)
- **文字色**: #ffffff (白色)
- **用途**: 需要注意的操作

#### 危险按钮（Danger）
- **背景色**: #ef4444 (红色)
- **文字色**: #ffffff (白色)
- **用途**: 删除操作、取消订阅

#### 次要按钮（Secondary）
- **背景色**: #6b7280 (灰色)
- **文字色**: #ffffff (白色)
- **用途**: 辅助操作、了解更多

### 尺寸建议

- **小按钮**: 120px - 适合辅助操作
- **中等按钮**: 180px - 标准按钮尺寸
- **大按钮**: 250px - 重要操作
- **全宽按钮**: 100% - 移动端友好

## 📱 最佳实践

### 1. 电商营销邮件

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

### 2. 系统通知邮件

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

### 3. 产品介绍邮件

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

### 4. 邮件客户端兼容性优化

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

## ⚡ 快捷方法

Email 类提供了 `add_button` 快捷方法：

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

## 🐛 常见问题

### Q: 按钮在某些邮件客户端中显示异常？
A: 确保使用推荐的样式设置，避免使用复杂的 CSS 属性：
```python
# 推荐做法
button.set_background_color("#3b82f6")  # 具体颜色值
button.set_width("180px")               # 明确宽度
```

### Q: 如何确保按钮文字清晰可读？
A: 确保文字和背景有足够的对比度：
```python
# 高对比度组合
button.set_background_color("#1f2937").set_text_color("#ffffff")  # ✅
# 避免低对比度
# button.set_background_color("#e5e7eb").set_text_color("#f3f4f6")  # ❌
```

### Q: 可以在按钮中添加图标吗？
A: 可以使用 Unicode 图标字符：
```python
button.set_text("📧 发送邮件")
button.set_text("🛒 立即购买")
button.set_text("📞 联系我们")
```

### Q: 如何设计适合移动端的按钮？
A: 使用合适的尺寸和全宽设计：
```python
mobile_button = (ButtonWidget()
    .set_text("移动端按钮")
    .set_width("100%")          # 全宽适配
    .set_align("center"))       # 居中对齐
```

### Q: 按钮链接安全注意事项？
A: 始终使用 HTTPS 链接，确保链接安全：
```python
button.set_href("https://example.com")  # ✅ 安全
# button.set_href("http://example.com")   # ❌ 不安全
```

## 🔗 相关组件

- [TextWidget](text-widget.md) - 用于按钮周围的说明文字
- [ColumnWidget](column-widget.md) - 用于多按钮的布局管理
- [CardWidget](card-widget.md) - 可以包含按钮的卡片容器
- [AlertWidget](alert-widget.md) - 可与按钮组合使用的提示信息