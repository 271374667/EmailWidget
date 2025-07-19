# User Guide

Welcome to the EmailWidget User Guide! This comprehensive guide will help you master all features of EmailWidget, from basic concepts to advanced usage.

## 📚 Learning Path

### 🚀 Quick Start
If you're a new user, we recommend reading in the following order:

1. **[Core Classes](core-classes.md)** - Understand the basic architecture of EmailWidget
2. **[Widget Overview](widget-overview.md)** - Learn about all available widget types
3. **[Text Widget](text-widget.md)** - Start with the most basic text widget

## 🏗️ System Architecture

EmailWidget uses a component-based architecture that allows you to flexibly build various types of email content:

```python
from email_widget import Email
from email_widget.widgets import TextWidget, TableWidget, ChartWidget, ButtonWidget

# 创建邮件容器
email = Email("数据报告")

# 添加组件
email.add_widget(TextWidget().set_content("本周数据概览"))
email.add_widget(TableWidget().set_headers(["项目", "数值"]))
email.add_widget(ChartWidget().set_image_url("chart.png"))
email.add_button("查看完整报告", "https://dashboard.example.com")

# 生成HTML
html = email.render_html()
```

## 📊 Widget Types Overview

| Widget Type | Purpose | Example Use Cases |
|-------------|---------|-------------------|
| **Text Widget** | Display text content | Titles, descriptions, notes |
| **Table Widget** | Show structured data | Data reports, statistical tables |
| **Chart Widget** | Visualize data | Trend charts, bar charts, pie charts |
| **Progress Widget** | Show progress status | Task completion, system load |
| **Status Widget** | Display status information | System monitoring, health checks |
| **Layout Widget** | Organize page layout | Multi-column layout, grouped display |
| **Button Widget** | User interaction | Link navigation, action buttons |
| **Other Widgets** | Special features | Quotes, alerts, cards |

## 🎨 Design Philosophy

EmailWidget follows these design principles:

### 📱 Email Compatibility First
- Use table-based layout to ensure correct display in various email clients
- Avoid modern CSS features to ensure broad compatibility
- Inline styles guarantee consistent rendering

### 🔧 Simple and Easy to Use
- Chain API design for clean and intuitive code
- Reasonable default configurations for out-of-the-box usage
- Rich configuration options to meet customization needs

### 🛡️ Secure and Reliable
- Input validation ensures data security
- Error handling ensures system stability
- Logging facilitates troubleshooting

## 🔧 Core Features

### ✨ Template Engine
- Powerful template system based on Jinja2
- Support for conditional rendering and loops
- Template caching improves performance

### 🖼️ Image Processing
- Smart image caching mechanism
- Support for multiple image formats
- Automatic image size optimization

### 📝 Logging System
- Hierarchical log recording
- Environment variable control
- Convenient for debugging and monitoring

### ⚡ Performance Optimization
- LRU caching strategy
- Template precompilation
- Memory usage optimization

## 🎯 Best Practices

### 📝 Content Organization
1. **Logical Layering**: Organize content by importance
2. **Moderate Segmentation**: Avoid excessive content in single widgets
3. **Clear Titles**: Use hierarchical title structure

### 🎨 Visual Design
1. **Maintain Consistency**: Unified font and color scheme
2. **Reasonable Whitespace**: Appropriate spacing improves reading experience
3. **Highlight Key Points**: Use color and font weight to emphasize important information

### 🔧 Code Quality
1. **Parameter Validation**: Use built-in validators to ensure data validity
2. **Error Handling**: Properly handle exceptional situations
3. **Performance Considerations**: Avoid creating large numbers of objects in loops

## 🆘 Getting Help

If you encounter problems during use:

1. 📖 Check [FAQ](../getting-started/faq.md)
2. 🔍 Search [API Reference](../api/index.md) for detailed information
3. 💡 Refer to [Example Code](../examples/index.md) for inspiration
4. 🐛 Submit issues on [GitHub](https://github.com/271374667/EmailWidget)

---

Now start your EmailWidget learning journey! We recommend beginning with [Core Classes](core-classes.md).