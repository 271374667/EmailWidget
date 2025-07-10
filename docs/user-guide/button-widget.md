# ButtonWidget 按钮组件

ButtonWidget 是一个专门用于在邮件中创建可点击按钮的组件。它提供了强大的定制功能，支持多种样式、颜色和对齐方式，完全兼容各大邮件客户端。

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

### 自定义样式

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
```

## 📖 API 参考

### 核心方法

#### `set_text(text: str) -> ButtonWidget`
设置按钮显示的文本内容。

**参数:**
- `text (str)`: 按钮文本内容

**示例:**
```python
button.set_text("点击我")
button.set_text("立即购买")
button.set_text("了解更多")
```

#### `set_href(href: str) -> ButtonWidget`
设置按钮点击后跳转的链接地址。

**参数:**
- `href (str)`: 链接地址，支持 http/https 链接、邮件地址等

**示例:**
```python
button.set_href("https://example.com")
button.set_href("mailto:contact@example.com")
button.set_href("tel:+1234567890")
```

### 样式定制

#### `set_background_color(color: str) -> ButtonWidget`
设置按钮的背景颜色。

**参数:**
- `color (str)`: CSS 颜色值（十六进制、RGB、颜色名称等）

**示例:**
```python
button.set_background_color("#3b82f6")    # 蓝色
button.set_background_color("#ef4444")    # 红色
button.set_background_color("#22c55e")    # 绿色
button.set_background_color("orange")     # 橙色
```

#### `set_text_color(color: str) -> ButtonWidget`
设置按钮文字的颜色。

**参数:**
- `color (str)`: CSS 颜色值

**示例:**
```python
button.set_text_color("#ffffff")  # 白色文字
button.set_text_color("#000000")  # 黑色文字
button.set_text_color("#1f2937")  # 深灰色文字
```

#### `set_width(width: str) -> ButtonWidget`
设置按钮的宽度。

**参数:**
- `width (str)`: CSS 宽度值（像素、百分比、auto等）

**示例:**
```python
button.set_width("150px")    # 固定宽度
button.set_width("100%")     # 全宽
button.set_width("auto")     # 自动宽度
```

#### `set_align(align: str) -> ButtonWidget`
设置按钮的对齐方式。

**参数:**
- `align (str)`: 对齐方式，支持 "left"、"center"、"right"

**示例:**
```python
button.set_align("left")     # 左对齐
button.set_align("center")   # 居中对齐
button.set_align("right")    # 右对齐
```

### 属性访问

#### 只读属性
- `text`: 获取按钮文本
- `href`: 获取链接地址
- `background_color`: 获取背景颜色
- `text_color`: 获取文字颜色
- `width`: 获取宽度设置
- `align`: 获取对齐方式

```python
print(f"按钮文本: {button.text}")
print(f"链接地址: {button.href}")
print(f"背景颜色: {button.background_color}")
```

## 🎨 样式指南

### 推荐颜色搭配

#### 主要按钮（Primary）
```python
button.set_background_color("#3b82f6").set_text_color("#ffffff")  # 蓝色主题
```

#### 成功按钮（Success）
```python
button.set_background_color("#22c55e").set_text_color("#ffffff")  # 绿色主题
```

#### 警告按钮（Warning）
```python
button.set_background_color("#f59e0b").set_text_color("#ffffff")  # 橙色主题
```

#### 危险按钮（Danger）
```python
button.set_background_color("#ef4444").set_text_color("#ffffff")  # 红色主题
```

#### 次要按钮（Secondary）
```python
button.set_background_color("#6b7280").set_text_color("#ffffff")  # 灰色主题
```

### 尺寸建议

#### 小按钮
```python
button.set_width("120px")
```

#### 中等按钮
```python
button.set_width("180px")
```

#### 大按钮
```python
button.set_width("250px")
```

#### 全宽按钮
```python
button.set_width("100%")
```

## 📱 最佳实践

### 1. 邮件客户端兼容性
```python
# 推荐：使用具体的颜色值而非 CSS 变量
button.set_background_color("#3b82f6")  # ✅ 好
# button.set_background_color("var(--primary)")  # ❌ 避免

# 推荐：设置明确的宽度
button.set_width("180px")  # ✅ 好，在所有客户端表现一致
```

### 2. 可访问性
```python
# 确保文字和背景有足够的对比度
button.set_background_color("#1f2937").set_text_color("#ffffff")  # ✅ 高对比度
# button.set_background_color("#e5e7eb").set_text_color("#f3f4f6")  # ❌ 对比度太低
```

### 3. 语义化文本
```python
# 使用明确的行动指向文本
button.set_text("立即购买")     # ✅ 好
button.set_text("了解更多")     # ✅ 好
button.set_text("点击这里")     # ❌ 模糊
```

### 4. 链接安全
```python
# 使用 HTTPS 链接
button.set_href("https://example.com")  # ✅ 安全
# button.set_href("http://example.com")   # ❌ 不安全
```

## 🔗 实际应用场景

### 电商邮件
```python
email = Email("新品上市通知")

# 主要行动按钮
email.add_button(
    "立即购买", 
    "https://shop.example.com/products/new",
    background_color="#22c55e",
    text_color="#ffffff",
    width="200px",
    align="center"
)

# 次要按钮
email.add_button(
    "查看详情", 
    "https://shop.example.com/products/new/details",
    background_color="#6b7280",
    text_color="#ffffff",
    width="150px",
    align="center"
)
```

### 服务通知
```python
email = Email("系统维护通知")

email.add_text("系统将于今晚进行维护，预计耗时2小时。")

# 了解详情按钮
email.add_button(
    "查看维护详情", 
    "https://status.example.com/maintenance",
    background_color="#3b82f6",
    text_color="#ffffff",
    width="180px",
    align="center"
)
```

### 营销活动
```python
email = Email("限时优惠活动")

# 突出的主要按钮
email.add_button(
    "立即抢购", 
    "https://shop.example.com/sale",
    background_color="#ef4444",
    text_color="#ffffff",
    width="100%",
    align="center"
)

# 次要的了解更多按钮
email.add_button(
    "活动规则", 
    "https://shop.example.com/sale/rules",
    background_color="#f3f4f6",
    text_color="#374151",
    width="150px",
    align="right"
)
```

### 多按钮布局
```python
from email_widget.widgets import ColumnWidget

email = Email("产品介绍")

# 使用列布局并排显示按钮
column = ColumnWidget()

# 左列按钮
left_button = (ButtonWidget()
    .set_text("免费试用")
    .set_href("https://app.example.com/trial")
    .set_background_color("#22c55e")
    .set_text_color("#ffffff")
    .set_width("100%")
    .set_align("center"))

# 右列按钮
right_button = (ButtonWidget()
    .set_text("了解定价")
    .set_href("https://example.com/pricing")
    .set_background_color("#3b82f6")
    .set_text_color("#ffffff")
    .set_width("100%")
    .set_align("center"))

column.add_widget(left_button, 0).add_widget(right_button, 1)
email.add_widget(column)
```

## ⚡ 快捷方法

`Email` 类提供了 `add_button` 快捷方法，简化按钮的创建过程：

```python
# 等价于创建 ButtonWidget 然后添加
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
```

## 🐛 常见问题

### Q: 按钮在某些邮件客户端中显示异常？
A: 确保使用推荐的样式设置，避免使用复杂的 CSS 属性。ButtonWidget 已经针对主流邮件客户端进行了优化。

### Q: 如何实现按钮的悬停效果？
A: 由于邮件客户端的限制，不建议使用悬停效果。ButtonWidget 专注于兼容性和可靠性。

### Q: 可以在按钮中添加图标吗？
A: 可以在按钮文本中包含 Unicode 图标字符，但不建议使用复杂的图片图标。

```python
button.set_text("📧 发送邮件")
button.set_text("🛒 立即购买")
```

### Q: 按钮不显示或样式错乱？
A: 检查链接地址是否正确，确保颜色值格式正确（如 "#3b82f6"），避免使用不支持的 CSS 属性。

## 🔗 相关组件

- [TextWidget](text-widget.md) - 用于按钮周围的说明文字
- [ColumnWidget](column-widget.md) - 用于多按钮的布局管理
- [CardWidget](card-widget.md) - 可以包含按钮的卡片容器
- [AlertWidget](alert-widget.md) - 可与按钮组合使用的提示信息