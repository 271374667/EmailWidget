# 文本组件 (TextWidget)

TextWidget 是 EmailWidget 中最基础也是最常用的组件，用于显示各种文本内容。它支持多种文本类型、对齐方式和样式配置。

同时为了满足其充当标题的需求，二级标题到五级标题都会自动显示数字编号。

## 🎯 组件预览

--8<-- "assets/text_widget_component_preview.html"

## 🚀 快速开始

```python
from email_widget import Email
from email_widget.widgets.text_widget import TextWidget
from email_widget.core.enums import TextType

# 创建邮件
email = Email("文本组件示例")

# 创建基本文本
text = TextWidget().set_content("这是一段普通文本")
email.add_widget(text)

# 链式调用设置样式
styled_text = (TextWidget()
              .set_content("重要标题")
              .set_type(TextType.SECTION_H2)
              .set_color("#0078d4"))
email.add_widget(styled_text)

# 使用快捷方法
email.add_text("快捷方法创建的文本", TextType.BODY)

# 导出HTML
email.export_html("text_demo.html")
```

## 📝 基本用法

### 设置文本内容

```python
from email_widget import Email
from email_widget.widgets.text_widget import TextWidget

email = Email("文本内容示例")

# 基本文本
text = TextWidget().set_content("Hello, World!")
email.add_widget(text)

# 多行文本
multi_line_text = TextWidget().set_content("""
第一行内容
第二行内容
第三行内容
""")
email.add_widget(multi_line_text)

# 支持HTML内容
html_text = TextWidget().set_content("包含 <strong>粗体</strong> 和 <em>斜体</em> 的文本")
email.add_widget(html_text)

email.export_html("text_content_demo.html")
```

### 文本类型设置

```python
from email_widget import Email
from email_widget.widgets.text_widget import TextWidget
from email_widget.core.enums import TextType

email = Email("文本类型示例")

# 不同级别的标题
title_large = TextWidget().set_content("大标题").set_type(TextType.TITLE_LARGE)
email.add_widget(title_large)

title_small = TextWidget().set_content("小标题").set_type(TextType.TITLE_SMALL)
email.add_widget(title_small)

# 章节标题（会自动编号）
section_h2 = TextWidget().set_content("二级标题").set_type(TextType.SECTION_H2)
email.add_widget(section_h2)

section_h3 = TextWidget().set_content("三级标题").set_type(TextType.SECTION_H3)
email.add_widget(section_h3)

section_h4 = TextWidget().set_content("四级标题").set_type(TextType.SECTION_H4)
email.add_widget(section_h4)

section_h5 = TextWidget().set_content("五级标题").set_type(TextType.SECTION_H5)
email.add_widget(section_h5)

# 正文和说明文字
body_text = TextWidget().set_content("这是正文内容，适用于段落描述").set_type(TextType.BODY)
email.add_widget(body_text)

caption_text = TextWidget().set_content("这是说明文字，通常用于图片说明").set_type(TextType.CAPTION)
email.add_widget(caption_text)

email.export_html("text_types_demo.html")
```

## 📖 API 参考

### 基本方法

#### `set_content(content: str) -> TextWidget`
设置文本内容。

**参数:**
- `content (str)`: 文本内容，支持HTML标记

**示例:**
```python
text = TextWidget().set_content("Hello World")
text = TextWidget().set_content("支持<strong>HTML</strong>标记")
```

#### `set_type(text_type: TextType) -> TextWidget`
设置文本类型。

**参数:**
- `text_type (TextType)`: 文本类型枚举值

**示例:**
```python
text.set_type(TextType.TITLE_LARGE)    # 大标题
text.set_type(TextType.SECTION_H2)     # 二级标题
text.set_type(TextType.BODY)           # 正文
text.set_type(TextType.CAPTION)        # 说明文字
```

#### `set_align(align: TextAlign) -> TextWidget`
设置文本对齐方式。

**参数:**
- `align (TextAlign)`: 对齐方式枚举值

**示例:**
```python
from email_widget.core.enums import TextAlign

text.set_align(TextAlign.LEFT)      # 左对齐
text.set_align(TextAlign.CENTER)    # 居中对齐
text.set_align(TextAlign.RIGHT)     # 右对齐
text.set_align(TextAlign.JUSTIFY)   # 两端对齐
```

#### `set_color(color: str) -> TextWidget`
设置文本颜色。

**参数:**
- `color (str)`: CSS颜色值

**示例:**
```python
text.set_color("#0078d4")           # 十六进制蓝色
text.set_color("red")               # 颜色名称
text.set_color("rgb(255, 0, 0)")    # RGB格式
```

### 高级样式方法

#### `set_font_size(size: str) -> TextWidget`
设置字体大小。

**参数:**
- `size (str)`: CSS字体大小值

**示例:**
```python
text.set_font_size("16px")  # 像素值
text.set_font_size("1.2em") # em单位
text.set_font_size("large") # CSS关键字
```

#### `set_font_weight(weight: str) -> TextWidget`
设置字体粗细。

**参数:**
- `weight (str)`: CSS字体粗细值

**示例:**
```python
text.set_font_weight("normal")  # 正常
text.set_font_weight("bold")    # 粗体
text.set_font_weight("600")     # 数值
```

#### `set_font_family(family: str) -> TextWidget`
设置字体系列。

**参数:**
- `family (str)`: CSS字体系列值

**示例:**
```python
text.set_font_family("Arial, sans-serif")
text.set_font_family("'Microsoft YaHei', SimHei, sans-serif")
```

#### `set_line_height(height: str) -> TextWidget`
设置行高。

**参数:**
- `height (str)`: CSS行高值

**示例:**
```python
text.set_line_height("1.5")    # 倍数
text.set_line_height("24px")   # 像素值
text.set_line_height("normal") # 关键字
```

#### `set_margin(margin: str) -> TextWidget`
设置外边距。

**参数:**
- `margin (str)`: CSS外边距值

**示例:**
```python
text.set_margin("16px")           # 四周相同
text.set_margin("10px 20px")      # 上下 左右
text.set_margin("5px 10px 15px 20px")  # 上 右 下 左
```

#### `set_max_width(max_width: str) -> TextWidget`
设置最大宽度。

**参数:**
- `max_width (str)`: CSS最大宽度值

**示例:**
```python
text.set_max_width("600px")   # 像素值
text.set_max_width("80%")     # 百分比
text.set_max_width("none")    # 不限制
```

### 只读属性

- `content`: 获取文本内容
- `text_type`: 获取文本类型
- `text_align`: 获取对齐方式
- `color`: 获取文本颜色

```python
print(f"文本内容: {text.content}")
print(f"文本类型: {text.text_type}")
```

## 🎨 文本类型详解

### 标题类型

#### 大标题 (TITLE_LARGE)
```python
text = TextWidget().set_content("主要标题").set_type(TextType.TITLE_LARGE)
```
- 默认字体大小: 24px
- 适用场景: 邮件主标题、重要章节标题

#### 小标题 (TITLE_SMALL)
```python
text = TextWidget().set_content("次要标题").set_type(TextType.TITLE_SMALL)
```
- 默认字体大小: 20px
- 适用场景: 子标题、分组标题

### 章节标题（自动编号）

#### 二级标题 (SECTION_H2)
```python
text = TextWidget().set_content("重要章节").set_type(TextType.SECTION_H2)
```
- 默认字体大小: 18px
- 自动编号: "1.", "2.", "3."...

#### 三级标题 (SECTION_H3)
```python
text = TextWidget().set_content("子章节").set_type(TextType.SECTION_H3)
```
- 默认字体大小: 16px
- 自动编号: "1.1.", "1.2.", "2.1."...

#### 四级标题 (SECTION_H4)
```python
text = TextWidget().set_content("小节").set_type(TextType.SECTION_H4)
```
- 默认字体大小: 15px
- 自动编号: "1.1.1.", "1.1.2."...

#### 五级标题 (SECTION_H5)
```python
text = TextWidget().set_content("细分小节").set_type(TextType.SECTION_H5)
```
- 默认字体大小: 14px
- 自动编号: "1.1.1.1.", "1.1.1.2."...

### 正文类型

#### 正文 (BODY)
```python
text = TextWidget().set_content("这是正文内容").set_type(TextType.BODY)
```
- 默认字体大小: 14px
- 适用场景: 段落文字、描述内容

#### 说明文字 (CAPTION)
```python
text = TextWidget().set_content("这是说明文字").set_type(TextType.CAPTION)
```
- 默认字体大小: 12px
- 适用场景: 图片说明、补充信息、版权声明

## 🎨 样式设计指南

### 对齐方式使用建议

```python
from email_widget.core.enums import TextAlign

# 左对齐 - 默认，适用于大部分文本
text.set_align(TextAlign.LEFT)

# 居中对齐 - 适用于标题、重要信息
text.set_align(TextAlign.CENTER)

# 右对齐 - 适用于签名、日期
text.set_align(TextAlign.RIGHT)

# 两端对齐 - 适用于较长的段落文字
text.set_align(TextAlign.JUSTIFY)
```

### 推荐颜色方案

```python
# 主题色系
text.set_color("#0078d4")  # 主要蓝色
text.set_color("#107c10")  # 成功绿色
text.set_color("#ff8c00")  # 警告橙色
text.set_color("#d13438")  # 错误红色

# 中性色系
text.set_color("#323130")  # 主要文字
text.set_color("#605e5c")  # 次要文字
text.set_color("#8a8886")  # 辅助文字
text.set_color("#c8c6c4")  # 占位文字
```

### 字体大小建议

```python
# 标题系列
text.set_font_size("24px")  # 主标题
text.set_font_size("20px")  # 副标题
text.set_font_size("18px")  # 章节标题

# 正文系列
text.set_font_size("16px")  # 重要正文
text.set_font_size("14px")  # 标准正文
text.set_font_size("12px")  # 说明文字
```

## 📱 最佳实践

### 1. 文档结构化
```python
from email_widget import Email
from email_widget.core.enums import TextType

email = Email("结构化文档")

# 主标题
email.add_text("月度工作报告", TextType.TITLE_LARGE)

# 章节
email.add_text("工作概述", TextType.SECTION_H2)
email.add_text("本月主要完成了以下工作...", TextType.BODY)

email.add_text("具体成果", TextType.SECTION_H3)
email.add_text("详细的成果描述...", TextType.BODY)

# 结论
email.add_text("总结", TextType.SECTION_H2)
email.add_text("综合来看...", TextType.BODY)

email.export_html("structured_document.html")
```

### 2. 强调重要信息
```python
# 使用颜色强调
important_text = (TextWidget()
                 .set_content("重要通知: 系统将于明日维护")
                 .set_type(TextType.BODY)
                 .set_color("#d13438")
                 .set_font_weight("bold"))
email.add_widget(important_text)

# 使用居中对齐突出显示
highlighted_text = (TextWidget()
                   .set_content("关键结论")
                   .set_type(TextType.TITLE_SMALL)
                   .set_align(TextAlign.CENTER)
                   .set_color("#0078d4"))
email.add_widget(highlighted_text)
```

### 3. 响应式文本
```python
# 设置最大宽度确保移动端适配
responsive_text = (TextWidget()
                  .set_content("这是一段较长的文本内容...")
                  .set_type(TextType.BODY)
                  .set_max_width("100%")
                  .set_line_height("1.6"))
email.add_widget(responsive_text)
```

### 4. 多语言支持
```python
# 中文字体
chinese_text = (TextWidget()
                .set_content("中文内容")
                .set_font_family("'Microsoft YaHei', SimHei, sans-serif"))

# 英文字体
english_text = (TextWidget()
                .set_content("English Content")
                .set_font_family("Arial, Helvetica, sans-serif"))
```

## ⚡ 快捷方法

Email 类提供了 `add_text` 快捷方法：

```python
# 等价于创建 TextWidget 然后添加
email.add_text("快捷文本", TextType.BODY)

# 完整的 TextWidget 创建方式
text_widget = TextWidget().set_content("完整文本").set_type(TextType.BODY)
email.add_widget(text_widget)
```

## 🔗 实际应用场景

### 邮件报告
```python
from email_widget import Email
from email_widget.core.enums import TextType

email = Email("销售报告")

# 报告标题
email.add_text("2024年第一季度销售报告", TextType.TITLE_LARGE)

# 执行摘要
email.add_text("执行摘要", TextType.SECTION_H2)
email.add_text("本季度销售业绩超出预期，总销售额达到500万元，同比增长25%。", TextType.BODY)

# 详细分析
email.add_text("详细分析", TextType.SECTION_H2)
email.add_text("产品A销售情况", TextType.SECTION_H3)
email.add_text("产品A本季度销售额为200万元，占总销售额的40%。", TextType.BODY)

email.export_html("sales_report.html")
```

### 系统通知
```python
email = Email("系统维护通知")

# 通知标题
title = (TextWidget()
         .set_content("系统维护通知")
         .set_type(TextType.TITLE_LARGE)
         .set_align(TextAlign.CENTER)
         .set_color("#d13438"))
email.add_widget(title)

# 维护时间
email.add_text("维护时间", TextType.SECTION_H2)
time_text = (TextWidget()
             .set_content("2024年3月15日 02:00 - 06:00")
             .set_type(TextType.BODY)
             .set_font_weight("bold")
             .set_color("#0078d4"))
email.add_widget(time_text)

# 影响范围
email.add_text("影响范围", TextType.SECTION_H2)
email.add_text("维护期间，所有在线服务将暂停使用。", TextType.BODY)

email.export_html("maintenance_notice.html")
```

## 🐛 常见问题

### Q: 章节编号不正确怎么办？
A: 章节编号是自动管理的，如果需要重置编号，可以在代码中重新开始使用章节标题。

### Q: 如何让文本在邮件客户端中正确显示？
A: 使用标准的CSS属性，避免使用复杂的样式。建议使用预定义的文本类型。

### Q: 支持自定义字体吗？
A: 支持，但建议使用系统通用字体，确保在不同邮件客户端中的兼容性。

### Q: 如何处理长文本的显示？
A: 使用 `set_max_width()` 设置最大宽度，使用 `set_line_height()` 改善可读性。

## 🔗 相关组件

- [AlertWidget](alert-widget.md) - 用于显示警告和提示信息
- [CardWidget](card-widget.md) - 可以包含文本内容的卡片组件
- [QuoteWidget](quote-widget.md) - 用于显示引用文本
- [SeparatorWidget](separator-widget.md) - 用于在文本间添加分隔线