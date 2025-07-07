# 文本组件 (TextWidget)

TextWidget 是 EmailWidget 中最基础也是最常用的组件，用于显示各种文本内容。它支持多种文本类型、对齐方式和样式配置。

同时为了满足其充当标题的需求，二级标题到五级标题都会自动显示数字编号

## 🚀 快速开始

```python
from email_widget.widgets import TextWidget

# 创建基本文本
text = TextWidget()
text.set_content("这是一段普通文本")

# 链式调用设置样式
text = TextWidget().set_content("重要标题").set_text_type(TextType.SECTION_H2).set_color("#0078d4")
```

<div style="color: #0078d4; font-size: 20px; font-weight: 600; margin: 16px 0;">重要标题</div>

## 📝 基本用法

### 设置文本内容

```python
# 基本文本
text = TextWidget().set_content("Hello, World!")

# 多行文本
text = TextWidget().set_content("""
第一行内容
第二行内容
第三行内容
""")

# 支持HTML内容
text = TextWidget().set_content("包含 <strong>粗体</strong> 和 <em>斜体</em> 的文本")
```

### 文本类型设置

```python
from email_widget.core.enums import TextType

# 不同级别的标题
title_h2 = TextWidget().set_content("二级标题").set_text_type(TextType.SECTION_H2)
title_h3 = TextWidget().set_content("三级标题").set_text_type(TextType.SECTION_H3)
title_h4 = TextWidget().set_content("四级标题").set_text_type(TextType.SECTION_H4)

# 正文和其他类型
body = TextWidget().set_content("正文内容").set_text_type(TextType.BODY)
subtitle = TextWidget().set_content("副标题").set_text_type(TextType.SUBTITLE)
caption = TextWidget().set_content("图片说明").set_text_type(TextType.CAPTION)
```

<div style="margin: 16px 0;">
    <h2 style="font-size: 20px; font-weight: 600; color: #323130; margin: 16px 0;">二级标题</h2>
    <h3 style="font-size: 18px; font-weight: 600; color: #323130; margin: 16px 0;">三级标题</h3>
    <h4 style="font-size: 16px; font-weight: 600; color: #323130; margin: 16px 0;">四级标题</h4>
    <p style="font-size: 14px; color: #323130; margin: 16px 0;">正文内容</p>
    <p style="font-size: 16px; color: #605e5c; margin: 16px 0;">副标题</p>
    <p style="font-size: 12px; color: #8e8e93; margin: 16px 0;">图片说明</p>
</div>

## 🎨 样式配置

### 文本对齐

```python
from email_widget.core.enums import TextAlign

# 不同对齐方式
left_text = TextWidget().set_content("左对齐文本").set_align(TextAlign.LEFT)
center_text = TextWidget().set_content("居中文本").set_align(TextAlign.CENTER)
right_text = TextWidget().set_content("右对齐文本").set_align(TextAlign.RIGHT)
justify_text = TextWidget().set_content("两端对齐的长文本内容...").set_align(TextAlign.JUSTIFY)
```

<div style="margin: 16px 0; border: 1px solid #e1dfdd; padding: 16px;">
    <p style="text-align: left; margin: 8px 0;">左对齐文本</p>
    <p style="text-align: center; margin: 8px 0;">居中文本</p>
    <p style="text-align: right; margin: 8px 0;">右对齐文本</p>
    <p style="text-align: justify; margin: 8px 0;">两端对齐的长文本内容，当文本足够长时可以看到两端对齐的效果。</p>
</div>

### 颜色和字体

```python
# 设置文本颜色
red_text = TextWidget().set_content("红色文本").set_color("#d13438")
blue_text = TextWidget().set_content("蓝色文本").set_color("#0078d4")
green_text = TextWidget().set_content("绿色文本").set_color("#107c10")

# 设置字体大小
small_text = TextWidget().set_content("小号文本").set_font_size("12px")
normal_text = TextWidget().set_content("正常文本").set_font_size("14px")
large_text = TextWidget().set_content("大号文本").set_font_size("18px")

# 设置字体粗细
normal_weight = TextWidget().set_content("正常粗细").set_font_weight("normal")
bold_text = TextWidget().set_content("粗体文本").set_font_weight("bold")
light_text = TextWidget().set_content("细体文本").set_font_weight("300")
```

<div style="margin: 16px 0;">
    <p style="color: #d13438; margin: 4px 0;">红色文本</p>
    <p style="color: #0078d4; margin: 4px 0;">蓝色文本</p>
    <p style="color: #107c10; margin: 4px 0;">绿色文本</p>
    <p style="font-size: 12px; margin: 4px 0;">小号文本</p>
    <p style="font-size: 14px; margin: 4px 0;">正常文本</p>
    <p style="font-size: 18px; margin: 4px 0;">大号文本</p>
    <p style="font-weight: normal; margin: 4px 0;">正常粗细</p>
    <p style="font-weight: bold; margin: 4px 0;">粗体文本</p>
    <p style="font-weight: 300; margin: 4px 0;">细体文本</p>
</div>

### 高级样式

```python
# 行高设置
text = TextWidget()
text.set_content("这是一段需要设置行高的长文本内容，可以看到行间距的变化效果。")
text.set_line_height("1.8")

# 最大宽度限制
text = TextWidget()
text.set_content("这段文本设置了最大宽度限制")
text.set_max_width("300px")

# 自定义字体
text = TextWidget()
text.set_content("使用自定义字体")
text.set_font_family("Georgia, serif")

# 自定义边距
text = TextWidget()
text.set_content("自定义边距文本")
text.set_margin("24px 0")
```

## 🔢 章节编号

TextWidget 支持自动章节编号功能：

```python
from email_widget.widgets import TextWidget
from email_widget.core.enums import TextType

# 使用章节编号
h2_text = TextWidget()
h2_text.set_content("主要章节")
h2_text.set_text_type(TextType.SECTION_H2)
h2_text.set_auto_section_number(True)

h3_text = TextWidget()
h3_text.set_content("子章节")
h3_text.set_text_type(TextType.SECTION_H3)
h3_text.set_auto_section_number(True)

# 手动设置章节编号
manual_text = TextWidget()
manual_text.set_content("手动编号章节")
manual_text.set_section_number("1.1")
```

<div style="margin: 16px 0;">
    <h2 style="font-size: 20px; font-weight: 600; color: #323130; margin: 16px 0;">1. 主要章节</h2>
    <h3 style="font-size: 18px; font-weight: 600; color: #323130; margin: 16px 0;">1.1 子章节</h3>
    <h3 style="font-size: 18px; font-weight: 600; color: #323130; margin: 16px 0;">1.1 手动编号章节</h3>
</div>

## 📋 完整示例

```python
from email_widget import Email
from email_widget.widgets import TextWidget
from email_widget.core.enums import TextType, TextAlign

# 创建邮件
email = Email("文本组件示例")

# 添加各种文本组件
email.add_widgets([
    # 主标题
    TextWidget()
        .set_content("月度报告")
        .set_text_type(TextType.SECTION_H2)
        .set_align(TextAlign.CENTER)
        .set_color("#0078d4"),
    
    # 副标题
    TextWidget()
        .set_content("2024年1月数据分析")
        .set_text_type(TextType.SUBTITLE)
        .set_align(TextAlign.CENTER)
        .set_color("#605e5c"),
    
    # 正文段落
    TextWidget()
        .set_content("本月整体业务表现良好，各项指标均达到预期目标。")
        .set_text_type(TextType.BODY)
        .set_line_height("1.6"),
    
    # 章节标题
    TextWidget()
        .set_content("核心指标分析")
        .set_text_type(TextType.SECTION_H3)
        .set_auto_section_number(True),
    
    # 要点说明
    TextWidget()
        .set_content("• 用户增长率：+15%\n• 营收增长：+22%\n• 客户满意度：92%")
        .set_font_size("14px")
        .set_line_height("1.8"),
    
    # 重要提醒
    TextWidget()
        .set_content("注意：下月需要重点关注用户留存率指标")
        .set_color("#d13438")
        .set_font_weight("bold")
        .set_align(TextAlign.CENTER)
])

# 渲染邮件
html = email.render_html()
```

## ⚙️ API 参考

### 核心方法

| 方法 | 参数 | 说明 | 示例 |
|------|------|------|------|
| `set_content()` | `content: str` | 设置文本内容 | `.set_content("Hello")` |
| `set_text_type()` | `text_type: TextType` | 设置文本类型 | `.set_text_type(TextType.SECTION_H2)` |
| `set_align()` | `align: TextAlign` | 设置对齐方式 | `.set_align(TextAlign.CENTER)` |
| `set_color()` | `color: str` | 设置文本颜色 | `.set_color("#0078d4")` |
| `set_font_size()` | `size: str` | 设置字体大小 | `.set_font_size("16px")` |
| `set_font_weight()` | `weight: str` | 设置字体粗细 | `.set_font_weight("bold")` |
| `set_font_family()` | `family: str` | 设置字体族 | `.set_font_family("Arial")` |
| `set_line_height()` | `height: str` | 设置行高 | `.set_line_height("1.5")` |
| `set_margin()` | `margin: str` | 设置边距 | `.set_margin("16px 0")` |
| `set_max_width()` | `width: str` | 设置最大宽度 | `.set_max_width("600px")` |

### 章节编号方法

| 方法 | 参数 | 说明 |
|------|------|------|
| `set_auto_section_number()` | `auto: bool` | 启用自动编号 |
| `set_section_number()` | `number: str` | 手动设置编号 |
| `reset_section_numbers()` | 无 | 重置编号计数器 |

## 🎯 最佳实践

### 1. 保持层次结构清晰
```python
# 推荐：清晰的层次结构
h2_title = TextWidget().set_content("主标题").set_text_type(TextType.SECTION_H2)
h3_subtitle = TextWidget().set_content("副标题").set_text_type(TextType.SECTION_H3)
body_text = TextWidget().set_content("正文内容").set_text_type(TextType.BODY)
```

### 2. 合理使用颜色
```python
# 推荐：使用语义化颜色
success_text = TextWidget().set_content("操作成功").set_color("#107c10")
warning_text = TextWidget().set_content("注意事项").set_color("#ff8c00")
error_text = TextWidget().set_content("错误信息").set_color("#d13438")
```

### 3. 适当的文字大小和间距
```python
# 推荐：根据内容重要性设置大小
title = TextWidget().set_content("标题").set_font_size("18px").set_margin("24px 0 16px 0")
body = TextWidget().set_content("正文").set_font_size("14px").set_line_height("1.6")
caption = TextWidget().set_content("说明").set_font_size("12px").set_color("#8e8e93")
```

---

**下一步**: 了解 [表格组件](table-widget.md) 学习如何展示结构化数据。 