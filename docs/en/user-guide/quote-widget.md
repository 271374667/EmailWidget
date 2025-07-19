# QuoteWidget

QuoteWidget is a component specifically designed for displaying quoted content, supporting multiple quote styles and theme colors. It can elegantly display famous quotes, user feedback, important statements, and other content, serving as an important complement to content presentation.

## 🎯 Widget Preview

--8<-- "assets/quote_widget_component_preview.html"

## ✨ Core Features

- **💬 Quote Display**: Supports complete display of quoted content, author, and source
- **🎨 Multiple Themes**: Supports theme colors like INFO, SUCCESS, WARNING, ERROR
- **📝 Flexible Configuration**: Author and source information are optional, supports dynamic updates
- **🎯 Highlighting**: Uses borders and background colors to highlight quoted content
- **📧 Email Compatible**: Implemented using email client-compatible HTML and CSS

## 🚀 Quick Start

### Basic Usage

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

### Advanced Usage

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

📚 **Complete API Documentation**: [QuoteWidget API](../api/quote-widget.md)

## 🎨 Style Guide

### Theme Colors

- **info**: Blue (#0078d4) - Informational quotes, general sayings
- **success**: Green (#107c10) - Success stories, positive reviews
- **warning**: Orange (#ff8c00) - Precautions, important reminders
- **error**: Red (#d13438) - Error warnings, negative feedback

## 📱 Best Practices

### 1. User Feedback Display

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

### 2. Important Statements in Documentation

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

## ⚡ Shortcut Methods

The Email class provides the `add_quote` shortcut method:

```python
# 带参数的快捷方法
email.add_quote(
    content="创新是企业发展的源动力",
    author="某CEO", 
    source="企业年报",
    theme="info"
)
```

## 🐛 Common Issues

### Q: Can I set only content without setting author?
A: Yes, both author and source are optional:
```python
quote.set_content("这是一句没有署名的引用。")
```

### Q: How to clear already set author information?
A: Use the `clear_author()` method:
```python
quote.clear_author()
quote.clear_source()
```

### Q: Can quoted content include HTML?
A: Basic HTML tags are supported, but simple formatting is recommended to ensure email compatibility.

### Q: What's the difference between different themes?
A: Mainly differences in border colors and background colors, used to express different emotional tendencies or importance levels.

## 🔗 Related Widgets

- [AlertWidget](alert-widget.md) - Alert information display
- [CardWidget](card-widget.md) - Card containing quotes
- [TextWidget](text-widget.md) - Basic text component
- [SeparatorWidget](separator-widget.md) - Content separation
- [StatusWidget](status-widget.md) - Status information display