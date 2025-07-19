# SeparatorWidget 分隔符组件

SeparatorWidget 是一个用于在邮件中创建视觉分隔线的组件。它支持多种样式的分隔线，包括实线、虚线和点线，帮助组织邮件内容的层次结构，提升可读性。

## 🎯 组件预览

--8<-- "assets/separator_component_preview.html"

## ✨ 核心特性

- **📏 多种样式**: 支持实线、虚线、点线三种分隔符样式
- **🎨 颜色主题**: 支持基于StatusType的主题颜色配置
- **🔧 灵活配置**: 可自定义颜色、粗细、宽度和边距
- **📧 邮件兼容**: 使用邮件客户端兼容的CSS实现

## 🚀 快速开始

### 基础用法

```python
from email_widget import Email
from email_widget.widgets import SeparatorWidget
from email_widget.core.enums import SeparatorType, TextType

# 创建邮件
email = Email("分隔符示例")

# 添加标题
email.add_text("分隔符演示", TextType.TITLE_LARGE)

# 添加内容
email.add_text("这是分隔符上方的内容")

# 创建基础分隔符
separator = SeparatorWidget().set_type(SeparatorType.SOLID)
email.add_widget(separator)

# 添加更多内容
email.add_text("这是分隔符下方的内容")

# 使用快捷方法
email.add_separator()

# 导出HTML
email.export_html("separator_demo.html")
```

### 进阶用法

```python
from email_widget import Email
from email_widget.widgets import SeparatorWidget
from email_widget.core.enums import SeparatorType, TextType

email = Email("自定义分隔符样式")

# 创建带样式的虚线分隔符
email.add_text("虚线分隔符示例", TextType.SECTION_H2)
dashed_separator = (SeparatorWidget()
    .set_type(SeparatorType.DASHED)
    .set_color("#0078d4")
    .set_thickness("2px")
    .set_width("80%")
    .set_margin("20px"))

email.add_widget(dashed_separator)

# 使用快捷方法创建点线分隔符
email.add_text("点线分隔符示例", TextType.SECTION_H2)
email.add_separator(
    separator_type=SeparatorType.DOTTED,
    color="#ff8c00",
    thickness="3px",
    width="50%"
)

email.export_html("custom_separator_demo.html")
```

📚 **完整API文档**: [SeparatorWidget API](../api/separator-widget.md)

## 🎨 样式指南

### 分隔符类型

- **实线分隔符 (SOLID)**: 适用于主要内容区域的分割、章节间的清晰分隔
- **虚线分隔符 (DASHED)**: 适用于次要内容的分割、相关内容的分组
- **点线分隔符 (DOTTED)**: 适用于装饰性分割、轻量级的内容分隔

### 推荐配色

#### 主题色系
- **主要分隔符**: #0078d4 (蓝色)
- **成功分隔符**: #107c10 (绿色)
- **警告分隔符**: #ff8c00 (橙色)
- **错误分隔符**: #d13438 (红色)

#### 中性色系
- **默认灰色**: #e1dfdd
- **深灰色**: #8e8e93
- **浅灰色**: #f3f2f1

### 尺寸建议

#### 粗细建议
- **细分隔符**: 1px - 适用于密集内容
- **标准分隔符**: 2px - 通用场景
- **粗分隔符**: 3px - 重要分割

#### 宽度建议
- **全宽分隔符**: 100%
- **居中分隔符**: 80%
- **装饰性分隔符**: 50%

## 📱 最佳实践

### 1. 内容层次分割

```python
from email_widget import Email
from email_widget.core.enums import SeparatorType, TextType

email = Email("层次化内容")

# 主要章节间用粗实线
email.add_text("第一章", TextType.TITLE_LARGE)
email.add_text("章节内容...")
email.add_separator(
    separator_type=SeparatorType.SOLID,
    thickness="2px",
    margin="30px"
)

# 子节间用细虚线
email.add_text("1.1 小节", TextType.SECTION_H2)
email.add_text("小节内容...")
email.add_separator(
    separator_type=SeparatorType.DASHED,
    thickness="1px",
    margin="20px"
)

email.export_html("hierarchical_content.html")
```

--8<-- "assets/separator_hierarchical_content.html"

### 2. 主题化分割

```python
from email_widget import Email
from email_widget.core.enums import SeparatorType, AlertType

email = Email("主题化分隔符")

# 成功状态后的分隔
email.add_alert("任务完成", AlertType.TIP)
email.add_separator(
    separator_type=SeparatorType.SOLID,
    color="#107c10",
    thickness="2px"
)

# 警告状态后的分隔
email.add_alert("注意事项", AlertType.WARNING)
email.add_separator(
    separator_type=SeparatorType.DASHED,
    color="#ff8c00",
    thickness="2px"
)

email.export_html("themed_separators.html")
```

--8<-- "assets/separator_themed_separators.html"

### 3. 系统监控邮件

```python
from email_widget import Email
from email_widget.core.enums import SeparatorType

email = Email("系统状态监控")

# 正常服务
email.add_text("Web服务: 正常")
email.add_separator(
    separator_type=SeparatorType.SOLID,
    color="#107c10",
    thickness="1px"
)

# 警告服务
email.add_text("数据库: 警告")
email.add_separator(
    separator_type=SeparatorType.DASHED,
    color="#ff8c00",
    thickness="2px"
)

# 错误服务
email.add_text("缓存: 故障")
email.add_separator(
    separator_type=SeparatorType.SOLID,
    color="#d13438",
    thickness="2px"
)

email.export_html("system_monitoring.html")
```

--8<-- "assets/temp/separator_system_monitoring.html"

## ⚡ 快捷方法

Email 类提供了 `add_separator` 快捷方法：

```python
# 基础快捷方法
email.add_separator()

# 带参数的快捷方法
email.add_separator(
    separator_type=SeparatorType.DASHED,
    color="#0078d4",
    thickness="2px",
    width="80%",
    margin="20px"
)
```

## 🐛 常见问题

### Q: 分隔符在某些邮件客户端中不显示？
A: 确保使用标准的 CSS 边框样式，避免使用复杂的 CSS 属性。SeparatorWidget 已经针对主流邮件客户端进行了优化。

### Q: 如何创建渐变色分隔符？
A: 由于邮件客户端的限制，建议使用纯色。如果需要视觉层次，可以使用不同的颜色深浅。

### Q: 分隔符太细或太粗？
A: 调整 `thickness` 属性，推荐使用 1px-3px 之间的值以确保良好的显示效果。

### Q: 如何让分隔符居中显示？
A: 分隔符默认居中显示，可以通过调整 `width` 属性来控制宽度，如 `set_width("80%")` 创建居中的80%宽度分隔符。

## 🔗 相关组件

- [TextWidget](text-widget.md) - 用于分隔符前后的标题文字
- [CardWidget](card-widget.md) - 可以在卡片间使用分隔符
- [ColumnWidget](column-widget.md) - 用于多列布局中的分隔
- [AlertWidget](alert-widget.md) - 可与分隔符组合使用的提示信息