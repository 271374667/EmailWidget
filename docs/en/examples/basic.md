# Basic Examples

This page provides core functionality examples of EmailWidget, covering the most common use cases and best practices.

## 📚 Example Overview

| Example | Function | Components Involved | Difficulty |
|---------|----------|-------------------|------------|
| [Quick Start](#quick-start) | Create your first email report | TextWidget, AlertWidget | ⭐ |
| [Text Styles](#text-styles) | Various text types and colors | TextWidget, SeparatorWidget | ⭐ |
| [Data Display](#data-display) | Tables and progress bars | TableWidget, ProgressWidget | ⭐⭐ |
| [Comprehensive Application](#comprehensive) | Complete monitoring report | Multiple components | ⭐⭐⭐ |

---

## Quick Start {#quick-start}

### Create Your First Email Report

This is the simplest example, showing how to create a basic email with title, text, and alerts:

```python
from email_widget import Email
from email_widget.core.enums import TextType, AlertType

# Create email object
email = Email("My First Report")

# Add main title
email.add_text("Welcome to EmailWidget", TextType.TITLE_LARGE)

# Add description text
email.add_text("This is a simple email report example demonstrating basic functionality.", TextType.BODY)

# Add important tip
email.add_alert("EmailWidget makes creating beautiful HTML emails simple and fast!", AlertType.TIP)

# Export as HTML file
email.export_html("my_first_report.html")
print("✅ Email report generated: my_first_report.html")
```

--8<-- "examples/assets/basic_html/example_1_quick_start_fixed.html"

**Key Points:**
- Use `Email()` to create email container
- `add_text()` shortcut method to add text
- `add_alert()` shortcut method to add alert messages
- `export_html()` to export as HTML file

---

## Text Style Display {#text-styles}

### Various Text Types and Color Styles

Demonstrates all text types and color settings supported by EmailWidget:

```python
from email_widget import Email
from email_widget.widgets.text_widget import TextWidget
from email_widget.core.enums import TextType

email = Email("Text Style Display")

# Display different text types
email.add_text("Text Type Display", TextType.TITLE_LARGE)

email.add_text("This is a Large Title", TextType.TITLE_LARGE)
email.add_text("This is a Small Title", TextType.TITLE_SMALL)
email.add_text("This is a Level 2 Section Header", TextType.SECTION_H2)
email.add_text("This is a Level 3 Section Header", TextType.SECTION_H3)
email.add_text("This is body content, used for paragraph descriptions and detailed explanations.", TextType.BODY)
email.add_text("This is caption text, usually used for supplementary information.", TextType.CAPTION)

# Separator
email.add_separator()

# Colored text
email.add_text("Color Style Display", TextType.TITLE_SMALL)

blue_text = (TextWidget()
            .set_content("This is blue important text")
            .set_type(TextType.BODY)
            .set_color("#0078d4"))
email.add_widget(blue_text)

green_text = (TextWidget()
             .set_content("This is green success text")
             .set_type(TextType.BODY)
             .set_color("#107c10"))
email.add_widget(green_text)

red_text = (TextWidget()
           .set_content("This is red warning text")
           .set_type(TextType.BODY)
           .set_color("#d13438"))
email.add_widget(red_text)

email.export_html("text_styles.html")
```

--8<-- "examples/assets/basic_html/example_2_text_styles_fixed.html"

**Key Points:**
- Supports multiple predefined text types (titles, sections, body, caption)
- Section headers automatically add numbering
- Supports custom color settings
- Separators used to distinguish different content areas

---

## Data Display {#data-display}

### Table and Progress Bar Combination

Shows how to use tables and progress bars to display project data:

```python
from email_widget import Email
from email_widget.widgets.table_widget import TableWidget
from email_widget.core.enums import TextType, ProgressTheme

email = Email("Data Display Example")

# Title
email.add_text("Project Progress Report", TextType.TITLE_LARGE)

# Project overview
email.add_text("Project Overview", TextType.SECTION_H2)
email.add_text("Here's the progress of each project this month:", TextType.BODY)

# Create data table
table = TableWidget()
table.set_headers(["Project Name", "Lead", "Progress", "Status"])

# Add data rows
table_data = [
    ["Website Redesign", "John Smith", "85%", "In Progress"],
    ["Mobile App", "Jane Doe", "60%", "In Progress"],
    ["Data Analysis", "Bob Wilson", "100%", "Completed"],
    ["System Optimization", "Alice Brown", "30%", "Just Started"]
]

for row in table_data:
    table.add_row(row)

email.add_widget(table)

# Separator
email.add_separator()

# Overall progress
email.add_text("Overall Progress", TextType.SECTION_H2)

# Progress bar display
email.add_progress(68.7, label="Total Project Completion", theme=ProgressTheme.PRIMARY)
email.add_progress(85, label="Website Redesign", theme=ProgressTheme.SUCCESS)
email.add_progress(60, label="Mobile App", theme=ProgressTheme.PRIMARY)
email.add_progress(30, label="System Optimization", theme=ProgressTheme.PRIMARY)

# Conclusion
email.add_text("Summary", TextType.SECTION_H2)
email.add_text("Overall progress this month is good. The website redesign project is nearing completion, and we need to focus on the system optimization project progress.", TextType.BODY)

email.export_html("data_display.html")
```

--8<-- "examples/assets/basic_html/example_3_data_display_fixed.html"

**Key Points:**
- `TableWidget` for structured data display
- `add_progress()` shortcut method to create progress bars
- Different progress bar themes represent different statuses
- Combining multiple components enhances information expression

---

## Comprehensive Application {#comprehensive}

### Complete System Monitoring Report

This example shows how to combine multiple components to create a complete system monitoring report:

```python
from email_widget import Email
from email_widget.widgets.table_widget import TableWidget
from email_widget.core.enums import TextType, AlertType, ProgressTheme

email = Email("System Monitoring Weekly Report")

# Report title
email.add_text("System Monitoring Weekly Report", TextType.TITLE_LARGE)
email.add_text("Monitoring Period: July 8, 2024 - July 14, 2024", TextType.CAPTION)

# System status overview
email.add_text("System Status Overview", TextType.SECTION_H2)

# Normal services
email.add_alert("Web service running normally with stable response time", AlertType.TIP)
email.add_alert("Database connection good with excellent query performance", AlertType.TIP)

# Warning information
email.add_alert("Cache service occasionally has delays, recommend monitoring", AlertType.WARNING)

# Separator
email.add_separator()

# Performance metrics
email.add_text("Key Performance Indicators", TextType.SECTION_H2)

# Performance table
perf_table = TableWidget()
perf_table.set_headers(["Metric", "Current Value", "Target Value", "Status"])

perf_data = [
    ["CPU Usage", "65%", "< 80%", "Normal"],
    ["Memory Usage", "72%", "< 85%", "Normal"],
    ["Disk Usage", "45%", "< 90%", "Normal"],
    ["Response Time", "120ms", "< 200ms", "Excellent"]
]

for row in perf_data:
    perf_table.add_row(row)

email.add_widget(perf_table)

# Performance progress bars
email.add_text("Resource Usage", TextType.SECTION_H3)
email.add_progress(65, label="CPU Usage", theme=ProgressTheme.SUCCESS)
email.add_progress(72, label="Memory Usage", theme=ProgressTheme.SUCCESS)
email.add_progress(45, label="Disk Usage", theme=ProgressTheme.SUCCESS)

# Separator
email.add_separator()

# Summary and recommendations
email.add_text("Summary and Recommendations", TextType.SECTION_H2)
email.add_text("The system has been running stably this week, with all indicators within normal ranges. Recommendations:", TextType.BODY)

# Recommendation list
email.add_text("1. Continue monitoring cache service performance", TextType.BODY)
email.add_text("2. Optimize database queries to further improve response speed", TextType.BODY)
email.add_text("3. Regularly clean log files to maintain sufficient disk space", TextType.BODY)

# Important reminder
email.add_alert("System maintenance is planned for next week, please prepare in advance!", AlertType.IMPORTANT)

email.export_html("system_monitoring.html")
```

--8<-- "examples/assets/basic_html/example_4_comprehensive_fixed.html"

**Key Points:**
- Structured report layout from overview to detailed data
- Different types of alert messages convey different levels of importance
- Tables and progress bars combined to display quantitative data
- Proper use of separators to organize content hierarchy

---

## 🚀 Quick Run

### Environment Setup

```bash
# Install EmailWidget
pip install EmailWidget

# Or install from source
git clone https://github.com/271374667/EmailWidget.git
cd EmailWidget
pip install -e .
```

### Batch Run Examples

Save any of the above example code as a `.py` file, then run:

```bash
python your_example.py
```

Generated HTML files can be:
- Opened directly in browsers for preview
- Sent as email content
- Integrated into email sending systems

### Email Sending Integration

```python
from email_widget import Email, QQEmailSender

# Create email content
email = Email("Monitoring Report")
email.add_text("System Running Normally", TextType.TITLE_LARGE)

# Get HTML content
html_content = email.export_str()

# Send email (requires SMTP configuration)
sender = QQEmailSender(
    email_address="your_email@qq.com",
    password="your_password"  # Use app password
)

sender.send_email(
    to_emails=["recipient@example.com"],
    subject="System Monitoring Report",
    html_body=html_content
)
```

## 💡 Learning Suggestions

### Progressive Learning Path

1. **Beginner Stage** - Start with quick start example, master basic concepts
2. **Style Stage** - Learn text styles, understand component property settings
3. **Data Stage** - Master tables and progress bars, handle structured data
4. **Comprehensive Stage** - Combine multiple components, create complete applications

### Practice Recommendations

- 📝 **Hands-on Practice** - Copy code to run locally
- 🔄 **Modify Parameters** - Try changing colors, text, data
- 🎨 **Custom Styles** - Experiment with different component combinations
- 📧 **Real Applications** - Apply examples to actual projects

### Advanced Directions

After completing basic examples, you can explore:
- [Data Reports](data-reports.md) - In-depth data visualization
- [System Monitoring](system-monitoring.md) - Professional monitoring reports
- [Real-world Applications](real-world.md) - Complex business scenarios

---

**Next Step:** Try running these examples, then explore more features based on your needs!