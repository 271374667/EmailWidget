# TextWidget 文本组件

TextWidget 是 EmailWidget 中最基础也是最常用的组件，用于显示各种文本内容。它支持多种文本类型、对齐方式和样式配置，是构建邮件内容的核心组件。

## 🎯 组件预览

--8<-- "assets/text_widget_component_preview.html"

## ✨ 核心特性

- **📝 多种类型**: 支持标题、正文、说明文字等多种文本类型
- **🎨 样式定制**: 支持颜色、对齐方式、字体样式等自定义配置
- **📊 自动编号**: 二级到五级标题自动显示数字编号
- **🔗 HTML支持**: 支持基本的HTML标签和格式化文本
- **📧 邮件兼容**: 使用邮件客户端兼容的HTML和CSS实现

## 🚀 快速开始

### 基础用法

```python
from email_widget import Email
from email_widget.widgets import TextWidget
from email_widget.core.enums import TextType

# 创建基本文本
text = TextWidget()
text.set_content("这是一段普通文本")
text.set_type(TextType.BODY)

email = Email("文本组件示例")
email.add_widget(text)
```

### 进阶用法

```python
# 链式调用设置样式
styled_text = (TextWidget()
              .set_content("重要标题")
              .set_type(TextType.SECTION_H2)
              .set_color("#0078d4")
              .set_align("center"))

email.add_widget(styled_text)

# 使用快捷方法
email.add_text("快捷方法创建的文本", TextType.BODY)
```

📚 **完整API文档**: [TextWidget API](../api/text-widget.md)

## 🎨 样式指南

### 文本类型和层级

- **TITLE_LARGE**: 大标题 - 用于邮件主标题
- **TITLE_SMALL**: 小标题 - 用于副标题
- **SECTION_H2**: 二级标题 - 自动编号 (1. 标题)
- **SECTION_H3**: 三级标题 - 自动编号 (1.1. 标题)
- **SECTION_H4**: 四级标题 - 自动编号 (1.1.1. 标题)
- **SECTION_H5**: 五级标题 - 自动编号 (1.1.1.1. 标题)
- **BODY**: 正文 - 段落内容
- **CAPTION**: 说明文字 - 图片说明、补充信息

### 颜色建议

- **主要内容**: #323130 (深灰色)
- **强调内容**: #0078d4 (蓝色)
- **成功信息**: #107c10 (绿色)
- **警告信息**: #ff8c00 (橙色)
- **错误信息**: #d13438 (红色)

## 📱 最佳实践

### 1. 文档结构化内容

```python
from email_widget import Email
from email_widget.widgets.text_widget import TextWidget
from email_widget.core.enums import TextType

# 创建结构化文档
email = Email("项目报告")

# 主标题
email.add_text("2024年Q1项目进展报告", TextType.TITLE_LARGE)

# 章节标题
email.add_text("项目概述", TextType.SECTION_H2)
email.add_text("本季度主要完成了用户系统和数据分析模块的开发工作。", TextType.BODY)

# 子章节
email.add_text("用户系统模块", TextType.SECTION_H3)
email.add_text("实现了用户注册、登录、权限管理等核心功能。", TextType.BODY)

email.add_text("数据分析模块", TextType.SECTION_H3)
email.add_text("完成了数据采集、清洗和基础分析功能。", TextType.BODY)

# 导出
email.export_html("structured_document.html")
```

### 2. 强调和格式化文本

```python
from email_widget import Email
from email_widget.widgets.text_widget import TextWidget
from email_widget.core.enums import TextType

email = Email("格式化文本示例")

# 强调重要信息
important_text = (TextWidget()
                 .set_content("重要通知：系统将于今晚进行维护")
                 .set_type(TextType.BODY)
                 .set_color("#d13438")
                 .set_align("center"))
email.add_widget(important_text)

# 成功信息
success_text = (TextWidget()
               .set_content("✅ 项目已成功部署到生产环境")
               .set_type(TextType.BODY)
               .set_color("#107c10"))
email.add_widget(success_text)

# HTML格式化
html_text = (TextWidget()
            .set_content("支持 <strong>粗体</strong>、<em>斜体</em> 和 <u>下划线</u>")
            .set_type(TextType.BODY))
email.add_widget(html_text)
```

## ⚡ 快捷方法

Email 类提供了 `add_text` 快捷方法：

```python
# 基础快捷方法
email.add_text("这是一段文本")

# 带类型的快捷方法
email.add_text("这是标题", TextType.SECTION_H2)

# 带样式的快捷方法
email.add_text("强调文本", TextType.BODY, color="#0078d4", align="center")
```

## 🐛 常见问题

### Q: 如何创建多行文本？
A: 在内容中使用换行符或HTML的`<br>`标签：
```python
text.set_content("第一行\n第二行\n第三行")
# 或者
text.set_content("第一行<br>第二行<br>第三行")
```

### Q: 标题编号是如何工作的？
A: 二级到五级标题会自动按层级编号：
- H2: 1. 标题
- H3: 1.1. 标题  
- H4: 1.1.1. 标题
- H5: 1.1.1.1. 标题

### Q: 支持哪些HTML标签？
A: 支持基本的格式化标签如`<strong>`、`<em>`、`<u>`、`<br>`等，但建议使用简单的标签以确保邮件客户端兼容性。

## 🔗 相关组件

- [SeparatorWidget](separator-widget.md) - 内容分隔线
- [AlertWidget](alert-widget.md) - 提醒信息文本
- [CardWidget](card-widget.md) - 包含文本的卡片
- [QuoteWidget](quote-widget.md) - 引用文本
- [ButtonWidget](button-widget.md) - 按钮文本