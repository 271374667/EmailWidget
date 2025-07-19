# EmailWidget - Powerful Email Component Library

## ✨ Features

- **Lightweight & Compact**: Quick installation with no complex dependencies (under 1MB)
- **Easy to Use**: Clear and simple API, create beautiful email templates with just a few lines of code
- **Complete Documentation**: Project has comprehensive documentation and type annotations for full IDE support
- **Rich Components**: Currently includes 15+ beautiful display components, all following Fluent design, viewable below
- **Thoroughly Tested**: Core functionality is completely tested to ensure project reliability
- **Completely Free**: Project uses MIT open source license, you can use it freely in any commercial project

## ✨ Why Choose EmailWidget?

> **Want to send alerts or logs to email but don't know how to beautify them and they look ugly? Use EmailWidget to complete the last step of sending emails!**

Want a beautiful email template but don't know HTML/CSS or just too lazy to write? Online templates are difficult to reuse after modification and don't support mobile? Then welcome to try EmailWidget - reusable, responsive, complete type hints, comprehensive documentation, lightweight email component library to help you quickly build your own report templates.

EmailWidget is an email component library designed specifically for Python developers, allowing you to create beautiful HTML email reports with just a few lines of code without needing to understand HTML and CSS details for emails. The project is verified by **1000+ test cases** with **100% test coverage for core code**, ensuring stability and reliability.

The email style below can be created with just **3 lines of code**, and the generated content can be directly sent as email, recipients will also see beautiful emails.

```python
from email_widget import Email

email = Email("Welcome to EmailWidget")

email.add_card("Python Version", "You need Python 3.10 or above to use EmailWidget", metadata={"Python Version": "3.10+"})

email.add_quote("EmailWidget is a Python library for building and sending HTML emails.", "EmailWidget")

email.export_html('welcome_email.html')
```

![image-20250706200253564](https://271374667.github.io/picx-images-hosting/EmailWidget/image-20250706200253564.3k8ahgbqia.webp)

## 🚀 Quick Start

### 📦 Installation

```bash
pip install EmailWidget
```

### Create Professional Reports in 30 Seconds

```python
from email_widget import Email, TextWidget, ProgressWidget
from email_widget.core.enums import TextType, ProgressTheme

# Create email
email = Email("📊 Business Report")

# Add title
email.add_widget(
    TextWidget()
    .set_content("Quarterly Performance Summary")
    .set_type(TextType.TITLE_LARGE)
)

# Add progress indicator
email.add_widget(
    ProgressWidget()
    .set_value(92)
    .set_label("Goal Completion Rate")
    .set_theme(ProgressTheme.SUCCESS)
)

# Export HTML
email.export_html("report.html")
```

--8<-- "assets/index_html/demo1.html"


## 🎪 Use Cases

<div class="email-preview-wrapper">
<div style="margin: 40px 0; padding: 30px;">
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; margin-top: 30px;">

    <!-- Data Analysis Reports -->
    <div style="background: white; border-radius: 15px; padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); transition: transform 0.3s ease, box-shadow 0.3s ease; position: relative; overflow: hidden; border: 1px solid #f0f0f0;">
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, #FF6B6B, #4ECDC4);"></div>
      <div style="display: flex; align-items: center; margin-bottom: 15px;">
        <div style="width: 50px; height: 50px; background: linear-gradient(135deg, #FF6B6B, #FF8E8E); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-right: 15px; box-shadow: 0 5px 15px rgba(255,107,107,0.3);">
          <span style="font-size: 24px;">📊</span>
        </div>
        <h3 style="margin: 0; color: #2C3E50; font-size: 1.4em; font-weight: 700;">Data Analysis Reports</h3>
      </div>
      <p style="color: #666; line-height: 1.6; margin-bottom: 15px; font-size: 0.95em;">Create professional data visualization email reports for data analysts</p>
      <div style="margin-bottom: 15px;">
        <span style="background: #E8F4FD; color: #2980B9; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; margin-right: 8px; display: inline-block; margin-bottom: 5px;">Business Analysis</span>
        <span style="background: #E8F4FD; color: #2980B9; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; margin-right: 8px; display: inline-block; margin-bottom: 5px;">KPI Monitoring</span>
        <span style="background: #E8F4FD; color: #2980B9; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 5px;">Trend Analysis</span>
      </div>
      <div style="border-top: 1px solid #F0F0F0; padding-top: 15px;">
        <p style="margin: 0; color: #888; font-size: 0.9em;"><strong>Core Components:</strong> ChartWidget, TableWidget, ProgressWidget</p>
      </div>
    </div>
    
    <!-- System Monitoring Reports -->
    <div style="background: white; border-radius: 15px; padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); transition: transform 0.3s ease, box-shadow 0.3s ease; position: relative; overflow: hidden; border: 1px solid #f0f0f0;">
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, #4ECDC4, #44A08D);"></div>
      <div style="display: flex; align-items: center; margin-bottom: 15px;">
        <div style="width: 50px; height: 50px; background: linear-gradient(135deg, #4ECDC4, #5FDDD5); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-right: 15px; box-shadow: 0 5px 15px rgba(78,205,196,0.3);">
          <span style="font-size: 24px;">🖥️</span>
        </div>
        <h3 style="margin: 0; color: #2C3E50; font-size: 1.4em; font-weight: 700;">System Monitoring Reports</h3>
      </div>
      <p style="color: #666; line-height: 1.6; margin-bottom: 15px; font-size: 0.95em;">Server status, performance metrics and system operations monitoring emails</p>
      <div style="margin-bottom: 15px;">
        <span style="background: #E8F8F5; color: #27AE60; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; margin-right: 8px; display: inline-block; margin-bottom: 5px;">System Ops</span>
        <span style="background: #E8F8F5; color: #27AE60; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; margin-right: 8px; display: inline-block; margin-bottom: 5px;">Service Monitor</span>
        <span style="background: #E8F8F5; color: #27AE60; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 5px;">Alert System</span>
      </div>
      <div style="border-top: 1px solid #F0F0F0; padding-top: 15px;">
        <p style="margin: 0; color: #888; font-size: 0.9em;"><strong>Core Components:</strong> StatusWidget, AlertWidget, LogWidget</p>
      </div>
    </div>
    
    <!-- Web Scraping Reports -->
    <div style="background: white; border-radius: 15px; padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); transition: transform 0.3s ease, box-shadow 0.3s ease; position: relative; overflow: hidden; border: 1px solid #f0f0f0;">
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, #A8E6CF, #7FCDCD);"></div>
      <div style="display: flex; align-items: center; margin-bottom: 15px;">
        <div style="width: 50px; height: 50px; background: linear-gradient(135deg, #A8E6CF, #B8F2E6); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-right: 15px; box-shadow: 0 5px 15px rgba(168,230,207,0.3);">
          <span style="font-size: 24px;">🕷️</span>
        </div>
        <h3 style="margin: 0; color: #2C3E50; font-size: 1.4em; font-weight: 700;">Web Scraping Reports</h3>
      </div>
      <p style="color: #666; line-height: 1.6; margin-bottom: 15px; font-size: 0.95em;">Scraping task execution status and data collection statistics email reports</p>
      <div style="margin-bottom: 15px;">
        <span style="background: #F0F9F0; color: #16A085; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; margin-right: 8px; display: inline-block; margin-bottom: 5px;">Data Collection</span>
        <span style="background: #F0F9F0; color: #16A085; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; margin-right: 8px; display: inline-block; margin-bottom: 5px;">Task Monitoring</span>
        <span style="background: #F0F9F0; color: #16A085; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 5px;">Quality Reports</span>
      </div>
      <div style="border-top: 1px solid #F0F0F0; padding-top: 15px;">
        <p style="margin: 0; color: #888; font-size: 0.9em;"><strong>Core Components:</strong> ProgressWidget, TableWidget, LogWidget</p>
      </div>
    </div>
    
    <!-- Regular Business Communication -->
    <div style="background: white; border-radius: 15px; padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); transition: transform 0.3s ease, box-shadow 0.3s ease; position: relative; overflow: hidden; border: 1px solid #f0f0f0;">
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, #FFB6C1, #FFA07A);"></div>
      <div style="display: flex; align-items: center; margin-bottom: 15px;">
        <div style="width: 50px; height: 50px; background: linear-gradient(135deg, #FFB6C1, #FFC1CC); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-right: 15px; box-shadow: 0 5px 15px rgba(255,182,193,0.3);">
          <span style="font-size: 24px;">📧</span>
        </div>
        <h3 style="margin: 0; color: #2C3E50; font-size: 1.4em; font-weight: 700;">Regular Business Communication</h3>
      </div>
      <p style="color: #666; line-height: 1.6; margin-bottom: 15px; font-size: 0.95em;">Team weekly reports, project progress, business summaries and other regular emails</p>
      <div style="margin-bottom: 15px;">
        <span style="background: #FFF0F5; color: #E74C3C; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; margin-right: 8px; display: inline-block; margin-bottom: 5px;">Project Management</span>
        <span style="background: #FFF0F5; color: #E74C3C; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; margin-right: 8px; display: inline-block; margin-bottom: 5px;">Team Communication</span>
        <span style="background: #FFF0F5; color: #E74C3C; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 5px;">Business Reports</span>
      </div>
      <div style="border-top: 1px solid #F0F0F0; padding-top: 15px;">
        <p style="margin: 0; color: #888; font-size: 0.9em;"><strong>Core Components:</strong> TextWidget, CardWidget, QuoteWidget</p>
      </div>
    </div>

  </div>
</div>
</div>

<style>
  /* Hover effects */
  div[style*="background: white"]:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.15) !important;
  }
  /* Responsive layout */
  @media (max-width: 768px) {
    div[style*="display: grid"] {
      grid-template-columns: 1fr !important;
    }
  }
</style>

## 🎨 Component Gallery

### Basic Components

=== "Text Component"
    
    ```python
    # 8 preset styles
    email.add_widget(
        TextWidget()
        .set_content("Large Title")
        .set_type(TextType.TITLE_LARGE)
    )
    
    email.add_widget(
        TextWidget()
        .set_content("Section Title")
        .set_type(TextType.SECTION_H2)
    )
    
    email.add_widget(
        TextWidget()
        .set_content("Body content, supports multi-line text and automatic formatting.")
        .set_type(TextType.BODY)
    )
    ```
    
    <center>![image-20250702112724320](./index.assets/image-20250702112724320.png)</center>

=== "Table Component"

    ```python
    # Direct DataFrame import
    table = TableWidget().set_title("Sales Data")
    table.set_dataframe(df)
    
    # Manual row addition
    table = TableWidget()
    table.set_headers(["Product", "Sales", "Status"])
    table.add_row(["iPhone", "1000", "success"])
    table.add_row(["iPad", "800", "warning"])
    
    email.add_widget(table)
    ```

    <center>![image-20250702113233960](./index.assets/image-20250702113233960.png)</center>

=== "Chart Component"

    ```python
    # matplotlib charts
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
    ax.set_title("Trend Chart")
    
    email.add_widget(
        ChartWidget()
        .set_chart(plt)
        .set_title("Data Trends")
        .set_description("Shows business metric trends")
    )
    ```
    
    <center>![image-20250702113423501](./index.assets/image-20250702113423501.png)</center>

### Advanced Components

=== "Progress Component"
    
    ```python
    # Linear progress bar
    email.add_widget(
        ProgressWidget()
        .set_value(75)
        .set_label("Project Progress")
        .set_theme(ProgressTheme.PRIMARY)
    )
    
    # Circular progress bar
    email.add_widget(
        CircularProgressWidget()
        .set_value(85)
        .set_label("Completion Rate")
    )
    ```
    
    <center>![image-20250702113553794](./index.assets/image-20250702113553794.png)</center>

=== "Status Component"
    
    ```python
    # Status card
    email.add_widget(
        CardWidget()
        .set_title("System Status")
        .set_content("All services running normally")
        .set_icon("✅")
    )
    
    # Status list
    status_items = [
        {"label": "Database", "status": "success", "value": "Connection stable"},
        {"label": "API", "status": "warning", "value": "Response time high"}
    ]
    email.add_status_items(status_items)
    ```
    
    <center>![image-20250702113934973](./index.assets/image-20250702113934973.png)</center>

=== "Notification Component"
    
    ```python
    # Alert box
    email.add_widget(
        AlertWidget()
        .set_content("System maintenance notification")
        .set_alert_type(AlertType.WARNING)
        .set_title("Important Notice")
    )
    
    # Quote style
    email.add_widget(
        QuoteWidget()
        .set_content("Data is the new oil")
        .set_author("Clive Humby")
        .set_source("Data Scientist")
    )
    ```
    
    <center>![image-20250702114027153](./index.assets/image-20250702114027153.png)</center>


## 📖 Documentation Navigation

<div class="grid cards" markdown>
- :material-rocket-launch: **[Quick Start](getting-started/installation.md)**
- :material-book-open: **[User Guide](user-guide/core-classes.md)**
- :octicons-device-camera-video-24: **[Component Preview](user-guide/widget-overview.md)**
- :material-api: **[API Reference](api/core.md)**
- :material-code-braces: **[Example Code](examples/basic.md)**
- :material-tools: **[Development Guide](development/contributing.md)**
</div>


## 🤝 Community & Support

### Getting Help

- **📚 Documentation Center**: [Complete Documentation](https://271374667.github.io/EmailWidget/)
- **🐛 Issue Feedback**: [GitHub Issues](https://github.com/271374667/EmailWidget/issues)
- **💬 Discussion**: [GitHub Discussions](https://github.com/271374667/EmailWidget/discussions)
- **📧 Email Support**: 271374667@qq.com

### Contributing

We recommend using uv as the package management tool for project management and development

```bash
# 1. Clone project
git clone https://github.com/271374667/EmailWidget.git

# 2. Install development environment
uv sync

# 3. Run tests
uv run pytest

# 4. Submit changes
git commit -m "Feature: Add new functionality"
```

### Social Media

- **GitHub**: [271374667/EmailWidget](https://github.com/271374667/EmailWidget)
- **Bilibili**: [Python调包侠](https://space.bilibili.com/282527875)
- **Email**: 271374667@qq.com

## 📄 License

This project uses the [MIT License](https://github.com/271374667/EmailWidget/blob/master/LICENSE) open source license.

---

<div align="center">
    <p>⭐ **If this project helps you, please give us a star!** ⭐</p>
    <p>Made with ❤️ by <a href="https://github.com/271374667">Python调包侠</a></p>
    <p><a href="https://space.bilibili.com/282527875">📺 Watch Video Tutorials</a> • <a href="https://271374667.github.io/EmailWidget/">📖 View Complete Documentation</a></p>
</div>