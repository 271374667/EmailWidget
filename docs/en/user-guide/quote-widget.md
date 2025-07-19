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

# Create basic quote
quote = QuoteWidget()
quote.set_content("Knowledge is power, learning is endless.")
quote.set_author("Francis Bacon")
quote.set_source("Essays")

email = Email("Quote Example")
email.add_widget(quote)
```

### Advanced Usage

```python
# Quote with theme
quote = QuoteWidget()
quote.set_content("Success is not final, failure is not fatal: it is the courage to continue that counts.")
quote.set_author("Winston Churchill")
quote.set_theme("success")

email.add_widget(quote)

# Set all information at once
quote2 = QuoteWidget()
quote2.set_quote(
    content="Code is poetry, simple and elegant.",
    author="A Programmer",
    source="Programming Insights"
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

email = Email("User Feedback Summary")

# Positive feedback
positive_quote = QuoteWidget()
positive_quote.set_content("This product is really great! The interface is clean, powerful features, completely meets our needs.")
positive_quote.set_author("Manager Li")
positive_quote.set_source("Company Customer")
positive_quote.set_theme("success")

email.add_widget(positive_quote)

# Improvement suggestions
suggestion_quote = QuoteWidget()
suggestion_quote.set_content("The product is good overall, but there's room for improvement in mobile experience.")
suggestion_quote.set_author("Director Zhang")
suggestion_quote.set_source("User Research")
suggestion_quote.set_theme("warning")

email.add_widget(suggestion_quote)
```

--8<-- "assets/temp/quote_user_feedback.html"

### 2. Important Statements in Documentation

```python
from email_widget import Email
from email_widget.widgets import QuoteWidget

email = Email("Project Documentation")

# Important statement
important_quote = QuoteWidget()
important_quote.set_content("This system involves sensitive data, all operators must strictly follow data security regulations.")
important_quote.set_author("Technical Department")
important_quote.set_source("Security Regulation Document")
important_quote.set_theme("error")

email.add_widget(important_quote)
```

--8<-- "assets/temp/quote_important_statement.html"

## ⚡ Shortcut Methods

The Email class provides the `add_quote` shortcut method:

```python
# Shortcut method with parameters
email.add_quote(
    content="Innovation is the driving force of enterprise development",
    author="A CEO", 
    source="Annual Report",
    theme="info"
)
```

## 🐛 Common Issues

### Q: Can I set only content without setting author?
A: Yes, both author and source are optional:
```python
quote.set_content("This is an unsigned quote.")
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