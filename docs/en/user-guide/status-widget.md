# StatusWidget

StatusWidget is a component specifically designed for displaying system status, configuration information, or key-value pair data. It supports color identification for multiple status types and provides flexible layout options, making it ideal for monitoring dashboards and status reports.

## 🎯 Widget Preview

--8<-- "assets/status_widget_component_preview.html"

## ✨ Core Features

- **📊 Status Display**: Supports key-value pair status information display
- **🎨 Status Classification**: Supports status types like SUCCESS, WARNING, ERROR, INFO
- **📏 Layout Options**: Supports both vertical and horizontal layouts
- **🔄 Dynamic Updates**: Supports dynamic adding, updating, and removing status items
- **📧 Email Compatible**: Implemented using email client-compatible HTML and CSS

## 🚀 Quick Start

### Basic Usage

```python
from email_widget import Email
from email_widget.widgets import StatusWidget

# Create basic status widget
status = StatusWidget()
status.set_title("System Status")
status.add_status("CPU Usage", "68%")
status.add_status("Memory Usage", "4.2GB / 8GB")
status.add_status("Disk Space", "256GB / 512GB")

email = Email("Status Report")
email.add_widget(status)
```

### Advanced Usage

```python
# Detailed status with status types
status = StatusWidget()
status.set_title("Service Monitoring")
status.add_status("API Service", "Running", "success")
status.add_status("Database", "Connection Normal", "success")
status.add_status("Cache Service", "Slow Response", "warning")
status.add_status("Network Status", "Disconnected", "error")
status.set_layout("horizontal")

email.add_widget(status)
```

📚 **Complete API Documentation**: [StatusWidget API](../api/status-widget.md)

## 🎨 Style Guide

### Status Types and Colors

- **success**: Green (#107c10) - Normal operation, successful status
- **warning**: Orange (#ff8c00) - Needs attention, performance warning
- **error**: Red (#d13438) - Error status, service exception
- **info**: Blue (#0078d4) - Information status, configuration items
- **neutral**: Gray (#8e8e93) - Neutral status, default values

## 📱 Best Practices

### 1. System Monitoring Status

```python
from email_widget import Email
from email_widget.widgets import StatusWidget

email = Email("System Monitoring Report")

# System resource status
system_status = StatusWidget()
system_status.set_title("System Resources")
system_status.add_status("CPU Usage", "68%", "success")
system_status.add_status("Memory Usage", "85%", "warning")
system_status.add_status("Disk Space", "256GB / 512GB", "success")
system_status.add_status("Network Status", "Disconnected", "error")
system_status.set_layout("vertical")

email.add_widget(system_status)

# Service status
service_status = StatusWidget()
service_status.set_title("Service Status")
service_status.add_status("Web Service", "Running", "success")
service_status.add_status("Database", "Connection Normal", "success")
service_status.add_status("Cache Service", "Slow Response", "warning")
service_status.add_status("Message Queue", "Queue Backlog", "warning")

email.add_widget(service_status)
```

--8<-- "assets/temp/status_system_monitoring.html"

### 2. Project Configuration Information

```python
from email_widget import Email
from email_widget.widgets import StatusWidget

email = Email("Project Configuration Report")

# Environment configuration
config_status = StatusWidget()
config_status.set_title("Environment Configuration")
config_status.add_status("Environment", "Production", "info")
config_status.add_status("Version", "v2.1.0", "info")
config_status.add_status("Deploy Time", "2024-07-11 15:30", "info")
config_status.add_status("Responsible", "Development Team", "info")
config_status.set_layout("horizontal")

email.add_widget(config_status)
```

## ⚡ Shortcut Methods

The Email class provides the `add_status` shortcut method:

```python
# Shortcut method with parameters
email.add_status(
    title="System Status",
    statuses=[
        ("CPU", "68%", "success"),
        ("Memory", "85%", "warning"),
        ("Disk", "50%", "success")
    ],
    layout="vertical"
)
```

## 🐛 Common Issues

### Q: How to choose between vertical and horizontal layout?
A: 
- **Vertical Layout**: Suitable for many status items or long labels
- **Horizontal Layout**: Suitable for quick browsing of key status information

### Q: How to update existing status items?
A: Use the `update_status` method:
```python
status.update_status("CPU Usage", "75%", "warning")
```

### Q: Can status values contain HTML?
A: Plain text is recommended to ensure correct display in all email clients.

## 🔗 Related Widgets

- [MetricWidget](metric-widget.md) - Data metrics display
- [ProgressWidget](progress-widget.md) - Progress status display
- [AlertWidget](alert-widget.md) - Status alert information
- [CardWidget](card-widget.md) - Card containing status
- [TableWidget](table-widget.md) - Tabular status display