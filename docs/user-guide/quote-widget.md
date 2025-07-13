# QuoteWidget 引用组件

QuoteWidget 是一个专门用于展示引用内容的组件，支持多种引用样式和主题颜色。它能够优雅地展示名人名言、用户反馈、重要声明等内容，是内容展示的重要补充。

## 🎯 组件预览

--8<-- "assets/quote_widget_component_preview.html"

## ✨ 核心特性

- **💬 引用展示**: 支持引用内容、作者、来源的完整展示
- **🎨 多种主题**: 支持INFO、SUCCESS、WARNING、ERROR等主题颜色
- **📝 灵活配置**: 作者和来源信息都是可选的，支持动态更新
- **🎯 突出显示**: 使用边框和背景色突出显示引用内容
- **📧 邮件兼容**: 使用邮件客户端兼容的HTML和CSS实现

## 🚀 快速开始

### 基础用法

```python
from email_widget import Email
from email_widget.widgets import QuoteWidget

# 创建基础引用
quote = QuoteWidget()
quote.set_content("知识就是力量，学习永无止境。")
quote.set_author("培根")
quote.set_source("《随笔集》")

email = Email("引用示例")
email.add_widget(quote)
```

### 进阶用法

```python
# 带主题的引用
quote = QuoteWidget()
quote.set_content("成功不是终点，失败不是致命的，重要的是继续前进的勇气。")
quote.set_author("温斯顿·丘吉尔")
quote.set_theme("success")

email.add_widget(quote)

# 一次性设置所有信息
quote2 = QuoteWidget()
quote2.set_quote(
    content="代码如诗，简洁而优雅。",
    author="某位程序员",
    source="编程感悟"
)
```

📚 **完整API文档**: [QuoteWidget API](../api/quote-widget.md)

## 🎨 样式指南

### 主题颜色

- **info**: 蓝色 (#0078d4) - 信息性引用、普通引言
- **success**: 绿色 (#107c10) - 成功案例、正面评价
- **warning**: 橙色 (#ff8c00) - 注意事项、重要提醒
- **error**: 红色 (#d13438) - 错误警告、负面反馈

## 📱 最佳实践

### 1. 用户反馈展示

```python
from email_widget import Email
from email_widget.widgets import QuoteWidget

email = Email("用户反馈汇总")

# 正面反馈
positive_quote = QuoteWidget()
positive_quote.set_content("这个产品真的很棒！界面简洁，功能强大，完全满足了我们的需求。")
positive_quote.set_author("李经理")
positive_quote.set_source("某公司客户")
positive_quote.set_theme("success")

email.add_widget(positive_quote)

# 改进建议
suggestion_quote = QuoteWidget()
suggestion_quote.set_content("产品整体不错，但是在移动端的体验还有提升空间。")
suggestion_quote.set_author("张总监")
suggestion_quote.set_source("用户调研")
suggestion_quote.set_theme("warning")

email.add_widget(suggestion_quote)
```

--8<-- "assets/temp/quote_user_feedback.html"

### 2. 文档中的重要声明

```python
from email_widget import Email
from email_widget.widgets import QuoteWidget

email = Email("项目文档")

# 重要声明
important_quote = QuoteWidget()
important_quote.set_content("本系统涉及敏感数据，所有操作人员必须严格遵守数据安全规范。")
important_quote.set_author("技术部")
important_quote.set_source("安全规范文档")
important_quote.set_theme("error")

email.add_widget(important_quote)
```

--8<-- "assets/temp/quote_important_statement.html"

## ⚡ 快捷方法

Email 类提供了 `add_quote` 快捷方法：

```python
# 带参数的快捷方法
email.add_quote(
    content="创新是企业发展的源动力",
    author="某CEO", 
    source="企业年报",
    theme="info"
)
```

## 🐛 常见问题

### Q: 可以只设置内容，不设置作者吗？
A: 可以，作者和来源都是可选的：
```python
quote.set_content("这是一句没有署名的引用。")
```

### Q: 如何清除已设置的作者信息？
A: 使用 `clear_author()` 方法：
```python
quote.clear_author()
quote.clear_source()
```

### Q: 引用内容可以包含HTML吗？
A: 支持基本的HTML标签，但建议使用简单的格式以确保邮件兼容性。

### Q: 不同主题有什么区别？
A: 主要是边框颜色和背景色的差异，用于表达不同的情感倾向或重要程度。

## 🔗 相关组件

- [AlertWidget](alert-widget.md) - 提醒信息展示
- [CardWidget](card-widget.md) - 包含引用的卡片
- [TextWidget](text-widget.md) - 基础文本组件
- [SeparatorWidget](separator-widget.md) - 内容分隔
- [StatusWidget](status-widget.md) - 状态信息展示