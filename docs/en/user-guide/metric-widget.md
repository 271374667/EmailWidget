# MetricWidget

MetricWidget is a component for displaying key data metrics in emails. It can show KPIs, data trends, business metrics and other information, supporting trend analysis, number formatting, and multiple layout configurations, making it ideal for data reports and dashboard emails.

## 🎯 Widget Preview

--8<-- "assets/metric_widget_component_preview.html"

## ✨ Core Features

- **📊 Data Display**: Supports complete metric display including values, units, and trend changes
- **📈 Trend Analysis**: Automatically identifies trend direction, provides visual trend indicators
- **🎨 Status Themes**: Theme color configuration based on StatusType, such as success, warning, error, etc.
- **📏 Layout Options**: Supports horizontal and vertical layouts to adapt to different display needs
- **🔢 Number Formatting**: Automatically formats large numbers, using K, M suffixes to simplify display
- **📧 Email Compatible**: Implemented using email client-compatible HTML and CSS

## 🚀 Quick Start

### Basic Usage

```python
from email_widget import Email
from email_widget.widgets import MetricWidget

# Create basic metric widget
metric = MetricWidget()
metric.set_title("Key Metrics")
metric.add_metric("Active Users", 12345, "people")
metric.add_metric("Monthly Revenue", "¥1,250,000")
metric.add_metric("Conversion Rate", "3.2", "%")

email = Email("Business Data Report")
email.add_widget(metric)
```

### Advanced Usage

```python
# Create detailed metrics with trends
metric = MetricWidget()
metric.set_title("Business Key Metrics")
metric.add_metric("New User Registration", 1567, "people", "+15.6%", "success", "Significant growth compared to last month")
metric.add_metric("User Activity", "78.9", "%", "+2.3%", "success", "User engagement improved")
metric.add_metric("Average Response Time", "156", "ms", "+12ms", "warning", "Performance optimization needed")
metric.add_metric("Error Rate", "0.23", "%", "-0.1%", "success", "System stability improved")
metric.set_layout("horizontal")
metric.show_trends(True)

email.add_widget(metric)
```

📚 **Complete API Documentation**: [MetricWidget API](../api/metric-widget.md)

## 🎨 Style Guide

### Trend Status Types and Colors

- **success**: Green (#107c10) - Positive growth, target achieved, good performance
- **warning**: Orange (#ff8c00) - Needs attention, slight deterioration, approaching threshold
- **error**: Red (#d13438) - Negative change, exceeding threshold, serious problems
- **info**: Blue (#0078d4) - Neutral information, regular data, reference metrics
- **primary**: Blue (#0078d4) - Important metrics, key data, main KPIs

### Number Formatting Rules

- **1,000,000+**: Display as "1M", "1.2M"
- **1,000+**: Display as "1K", "5.3K"
- **Less than 1,000**: Display original number "123", "89.5"

## 📱 Best Practices

### 1. Business Dashboard

```python
from email_widget import Email
from email_widget.widgets.metric_widget import MetricWidget

# Create business data dashboard email
email = Email("Business Data Dashboard")

# Core business metrics
metric1 = MetricWidget()
metric1.set_title("Core KPIs")
metric1.add_metric("Monthly Active Users", 125436, "people", "+15.6%", "success", "Strong user growth")
metric1.add_metric("Monthly Revenue", 2850000, "yuan", "+18.2%", "success", "Revenue reaches historical high")
metric1.add_metric("Conversion Rate", "4.23", "%", "+0.8%", "success", "Conversion effectiveness improved")
metric1.add_metric("Average Order Value", "168.5", "yuan", "-2.3%", "warning", "Pricing strategy needs attention")
metric1.set_layout("horizontal")
metric1.show_trends(True)

email.add_widget(metric1)

# Export HTML file
email.export_html("business_dashboard.html")
```

--8<-- "assets/metric_business_dashboard.html"

### 2. System Performance Monitoring

```python
from email_widget import Email
from email_widget.widgets.metric_widget import MetricWidget

# Create system performance report email
email = Email("System Performance Report")

# System resource usage
metric = MetricWidget()
metric.set_title("System Resources")
metric.add_metric("CPU Usage", "45.2", "%", "+2.1%", "warning", "Load slightly increased")
metric.add_metric("Memory Usage", "78.5", "%", "-1.3%", "success", "Memory usage normal")
metric.add_metric("Disk I/O", "234", "MB/s", "+45MB/s", "info", "Read/write frequency increased")
metric.add_metric("Network Bandwidth", "1.2", "GB/s", "+0.3GB/s", "info", "Traffic growth stable")
metric.set_layout("horizontal")

email.add_widget(metric)
```

--8<-- "assets/metric_system_performance.html"

## ⚡ Shortcut Methods

The Email class provides the `add_metric` shortcut method:

```python
# Shortcut method with parameters
email.add_metric(
    title="Key Metrics",
    metrics=[
        ("Metric 1", 1234, "unit", "+10%", "success", "description"),
        ("Metric 2", "5.6", "%", "-2%", "warning"),
        ("Metric 3", "¥1,250,000", "", "+15%", "success")
    ],
    layout="horizontal",
    show_trends=True
)
```

## 🐛 Common Issues

### Q: Recommendations for choosing horizontal vs vertical layout?
A: 
- **Horizontal Layout**: Suitable for 3-5 core metrics, displayed in one row
- **Vertical Layout**: Suitable for detailed metric lists, each metric takes one row

### Q: How to customize number format?
A: Pass pre-formatted string as value:
```python
metric.add_metric("Custom", "1,234.56", "10K yuan")      # Custom format
metric.add_metric("Percentage", "99.95", "%")            # Keep decimals
```

### Q: Why don't trends show?
A: Make sure you called the `show_trends(True)` method.

## 🔗 Related Widgets

- [ProgressWidget](progress-widget.md) - Progress bar display
- [CircularProgressWidget](circular-progress-widget.md) - Circular progress metrics
- [StatusWidget](status-widget.md) - Status information display
- [CardWidget](card-widget.md) - Card that can contain metrics
- [TableWidget](table-widget.md) - Tabular data display