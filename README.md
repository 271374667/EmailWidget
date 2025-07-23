<div align="center">

**Language:** [English](README.md) | [简体中文](README_CN.md)

<h1>EmailWidget - Powerful Email Component Library</h1>

**🚀 A modern, easy-to-use Python email component library that lets you effortlessly create beautiful HTML email reports**

[![PyPI version](https://badge.fury.io/py/EmailWidget.svg)](https://badge.fury.io/py/EmailWidget)
[![Downloads](https://static.pepy.tech/badge/EmailWidget)](https://pepy.tech/project/EmailWidget)
[![Python versions](https://img.shields.io/badge/python-3.10%2B-blue)](https://pypi.org/project/EmailWidget/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Codecov](https://codecov.io/gh/271374667/EmailWidget/branch/master/graph/badge.svg)](https://codecov.io/gh/271374667/EmailWidget)

[📖 Documentation](https://271374667.github.io/EmailWidget) • [🚀 Quick Start](#-quick-start) • [💡 Examples](#-component-showcase)

</div>

---
## ✨ Features

- **Small & Lightweight**: Quick installation, no complex dependencies (less than 1MB)
- **Easy to Use**: Clear and simple API, create beautiful email templates with just a few lines of code
- **Complete Documentation**: Full documentation with type annotations, comprehensive IDE support
- **Rich Components**: Currently includes 17 beautiful display components, all following Fluent design principles
- **Fully Tested**: Core functionality thoroughly tested to ensure reliability
- **Completely Free**: MIT open source license, use freely in any commercial project

## ✨ Why Choose EmailWidget?

> **Want to send alerts or logs to email but don't know how to beautify them? Use EmailWidget to complete the final step of sending emails!**

5 lines of code saves you 30 minutes of dealing with various email CSS compatibility issues. Supports PC and mobile devices, making the once painful task of sending alert emails simple. You can build your unique email template like building blocks, send with one line of code, no heavyweight dependencies, completely open source and free for commercial use. Installation is less than 2MB. EmailWidget welcomes you to join your project anytime.

The email style below can be created with just **3 lines of code**, and the generated content can be sent directly as an email, with recipients seeing beautiful emails:

```python
from email_widget import Email

email = Email("Welcome to EmailWidget")

email.add_card("Python Version", "You need Python 3.10 or higher to use EmailWidget", metadata={"Python Version": "3.10+"})

email.add_quote("EmailWidget is a Python library for building and sending HTML emails.", "EmailWidget")

email.export_html('welcome_email.html')
```

![image-20250706200253564](https://271374667.github.io/picx-images-hosting/EmailWidget/image-20250706200253564.3k8ahgbqia.webp)

### 🎨 Rich Components - 17 Intuitive Components

```python
# One line of code, multiple components
email.add_widget(TextWidget().set_content("Title").set_type(TextType.TITLE_LARGE))
email.add_widget(TableWidget().set_dataframe(df)) # Supports pandas DataFrame
email.add_widget(ChartWidget().set_chart(plt)) # Supports matplotlib/seaborn charts
email.add_widget(ProgressWidget().set_value(85).set_theme(ProgressTheme.SUCCESS))

# Use shortcut methods to add components directly
email.add_progress(value=95, max_value=100)
```

| 🎯 **Component Type**            | 📝 **Features**                           | 🔧 **Use Cases**        |
|----------------------------------|--------------------------------------------|-------------------------|
| 📝 **TextWidget**                | 8 text styles, auto-numbering, section management | Titles, body text, descriptions |
| 📊 **TableWidget**               | DataFrame integration, status cells, color coding | Data tables, statistical reports |
| 📈 **ChartWidget**               | Native matplotlib/seaborn support, auto-encoding | Data visualization, trend charts |
| 📊 **ProgressWidget**            | 5 themes, increment/decrement, percentage display | Task progress, completion rates |
| ⭕ **CircularProgressWidget**     | Circular progress bars, multiple sizes, dynamic updates | KPI metrics, completion rates |
| 🎴 **CardWidget**                | Info cards, icon support, metadata management | Summary info, status display |
| ⚠️ **AlertWidget**               | 5 alert types, custom icons, message notifications | Notifications, warnings, tips |
| 🖼️ **ImageWidget**              | Multi-source support, size control, description text | Image display, logo display |
| 💬 **QuoteWidget**               | Quote styles, author info, source attribution | Quotes, comments, excerpts |
| 📊 **StatusWidget**              | Status item management, layout control, dynamic updates | System status, service monitoring |
| 📑 **ColumnWidget**              | Auto/manual columns, responsive layout, widget management | Multi-column layout, content grouping |
| 📋 **LogWidget**                 | Log levels, syntax highlighting, filtering | System logs, runtime records |
| 🔘 **ButtonWidget**              | Link buttons, custom styles, multiple themes | Action buttons, navigation links |
| 📏 **SeparatorWidget**           | Dividers, multiple styles, customizable colors | Content separation, area division |
| ✅ **ChecklistWidget**           | Task lists, status tracking, progress statistics | To-do items, checklists |
| ⏰ **TimelineWidget**            | Timeline display, event management, status markers | Progress tracking, history records |
| 📊 **MetricWidget**              | Data metrics, trend analysis, multiple layouts | KPI display, data monitoring |

## 🏃‍♂️ Quick Start

### 📦 Installation

#### Basic Installation (Recommended)
```bash
pip install EmailWidget
```

> 💡 **Installation Note**: Only requires jinja2 dependency, lightweight and fast. If you need DataFrame functionality for TableWidget or Matplotlib for ChartWidget, please install pandas or matplotlib/seaborn separately.

### 🎯 Create Your First Report in 30 Seconds

```python
from email_widget import Email, TextWidget, ProgressWidget
from email_widget.core.enums import TextType, ProgressTheme

# 1️⃣ Create email object
email = Email("📊 Daily Sales Report")

# 2️⃣ Add subtitle and footer
email.set_subtitle("Q1 2024 Performance Summary")
email.set_footer("This report is automatically generated by the data analysis team")

# 3️⃣ Add a large title
email.add_widget(
    TextWidget().set_content("📈 Sales Performance Overview").set_type(TextType.TITLE_LARGE)
)

# 4️⃣ Add progress indicators
email.add_widget(
    ProgressWidget()
    .set_value(92)
    .set_label("Quarterly Goal Completion Rate")
    .set_theme(ProgressTheme.SUCCESS)
)

# 5️⃣ Add data table (using convenience method, directly call email instead of creating widget then add_widget)
data = [
    ["iPhone 15", "1,250", "$1,875,000", "125%"],
    ["MacBook Pro", "580", "$1,740,000", "116%"],
    ["iPad Air", "920", "$552,000", "108%"],
]
email.add_table_from_data(
    data=data, headers=["Product", "Sales", "Revenue", "Achievement Rate"], title="🏆 Product Sales Details"
)

# 6️⃣ Export HTML file
file_path = email.export_html("daily_report.html")
# If you need to send email directly, export to string interface is also provided (images are automatically converted to base64 embedded in html)
# html_str: str = email.export_str()
print(f"🎉 Report generated: {file_path}")
```

<details>
<summary>🎨 Click to view generated effect</summary>

[![image-20250702215545140](./README.assets/image-20250702215545140.png)](https://271374667.github.io/picx-images-hosting/image-20250702215545140.6wr07lwngk.webp)

</details>

### Quick Send

EmailWidget includes a basic email sending function. You can quickly send emails through the `EmailSender` class, currently supporting **QQ Email** and **NetEase Email**.

Before using, you need to obtain the account and key from the respective email providers. Here's a simple example of sending an email by importing QQEmailSender and configuring the account and key:

```python
from email_widget import Email, QQEmailSender

email = Email("Test Email")
email.add_card("Test Card", "This is test card content.")
email.add_quote("This is a quote text.", "PythonImporter")
email.add_status_items(
    [{"label": "Status1", "value": "Complete"}, {"label": "Status2", "value": "In Progress"}],
    title="Test Status",
)
email.add_table_from_data(
    [["Column1", "Column2"], ["Data1", "Data2"]],
    title="Test Table",
)
QQEmailSender(username="your_email@qq.com", password="your_key").send(email)
print("Email sent successfully!")
```

## 🔧 Component Showcase

Below are displays of all currently available components (some features may not be updated timely, please refer to documentation if there are errors or inconsistencies):

<details>
<summary>🎨 Click to view component preview</summary>

![image-20250702215350732](https://271374667.github.io/picx-images-hosting/EmailWidget/PixPin_2025-07-12_10-02-42.7snhz8im11.webp)

</details>

## Actual Display in Email

### Desktop Web Version

<details>
<summary>🎨 Click to view desktop report</summary>

![Desktop Version](https://271374667.github.io/picx-images-hosting/image-20250704112531428.9o02gn5kp8.webp)

</details>

### Mobile Version

<details>
<summary>🎨 Click to view mobile report</summary>

![Mobile Version](https://271374667.github.io/picx-images-hosting/image-20250704112733193.4qrlmsrswe.webp)

</details>

## 🎨 Advanced Features

### 🎯 **Method Chaining Support**

```python
# Fluent API design
email = (Email("Project Progress Report")
         .set_subtitle("Q1 Summary")
         .set_footer("Generated by EmailWidget")
         .add_widget(TextWidget().set_content("Overview").set_type(TextType.TITLE_LARGE))
         .add_widget(ProgressWidget().set_value(78).set_label("Overall Progress")))
```

## 📚 Learning Resources

| 📖 **Resource Type** | 🔗 **Link**                                                                 | 📝 **Content**      |
|----------------------|-----------------------------------------------------------------------------|---------------------|
| 🚀 **Quick Start**   | [Installation Guide](https://271374667.github.io/EmailWidget/getting-started/installation/) | Environment setup, first email |
| 📘 **User Manual**   | [Component Guide](https://271374667.github.io/EmailWidget/user-guide/core-classes/) | Complete tutorial for 17 components |
| 🔧 **API Docs**      | [API Reference](https://271374667.github.io/EmailWidget/api/core/) | Complete class and method documentation |
| 💡 **Examples**      | [Use Cases](https://271374667.github.io/EmailWidget/examples/basic/) | Real-world scenario code |
| 🛠️ **Dev Guide**     | [Contributing](https://271374667.github.io/EmailWidget/development/contributing/) | Participate in project development |

## 🤝 Community & Contributing

### 🌟 **Participate in Open Source**

```bash
# Clone project
git clone https://github.com/271374667/EmailWidget.git

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/

# Submit code
git add .
git commit -m "feat: add new feature"
```

### 📞 **Contact Us**

- **🐛 Bug Reports**: [GitHub Issues](https://github.com/271374667/EmailWidget/issues)
- **💬 Discussion**: [GitHub Discussions](https://github.com/271374667/EmailWidget/discussions)
- **📧 Email**: 271374667@qq.com
- **📺 Video Tutorials**: [Bilibili Channel](https://space.bilibili.com/282527875)

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

<div align="center">

**⭐ If this project helps you, please give us a Star! ⭐**

Made with ❤️ by [Python 调包侠](https://github.com/271374667) | [Watch Tutorials](https://space.bilibili.com/282527875) | [View Documentation](https://271374667.github.io/EmailWidget/)

</div>