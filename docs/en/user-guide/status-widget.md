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

# 创建基础状态组件
status = StatusWidget()
status.set_title("系统状态")
status.add_status("CPU使用率", "68%")
status.add_status("内存使用", "4.2GB / 8GB")
status.add_status("磁盘空间", "256GB / 512GB")

email = Email("状态报告")
email.add_widget(status)
```

### Advanced Usage

```python
# 带状态类型的详细状态
status = StatusWidget()
status.set_title("服务监控")
status.add_status("API服务", "运行中", "success")
status.add_status("数据库", "连接正常", "success")
status.add_status("缓存服务", "响应慢", "warning")
status.add_status("网络状态", "断开连接", "error")
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

email = Email("系统监控报告")

# 系统资源状态
system_status = StatusWidget()
system_status.set_title("系统资源")
system_status.add_status("CPU使用率", "68%", "success")
system_status.add_status("内存使用", "85%", "warning")
system_status.add_status("磁盘空间", "256GB / 512GB", "success")
system_status.add_status("网络状态", "断开连接", "error")
system_status.set_layout("vertical")

email.add_widget(system_status)

# 服务状态
service_status = StatusWidget()
service_status.set_title("服务状态")
service_status.add_status("Web服务", "运行中", "success")
service_status.add_status("数据库", "连接正常", "success")
service_status.add_status("缓存服务", "响应慢", "warning")
service_status.add_status("消息队列", "队列积压", "warning")

email.add_widget(service_status)
```

--8<-- "assets/temp/status_system_monitoring.html"

### 2. Project Configuration Information

```python
from email_widget import Email
from email_widget.widgets import StatusWidget

email = Email("项目配置报告")

# 环境配置
config_status = StatusWidget()
config_status.set_title("环境配置")
config_status.add_status("环境", "生产环境", "info")
config_status.add_status("版本", "v2.1.0", "info")
config_status.add_status("部署时间", "2024-07-11 15:30", "info")
config_status.add_status("负责人", "开发团队", "info")
config_status.set_layout("horizontal")

email.add_widget(config_status)
```

## ⚡ Shortcut Methods

The Email class provides the `add_status` shortcut method:

```python
# 带参数的快捷方法
email.add_status(
    title="系统状态",
    statuses=[
        ("CPU", "68%", "success"),
        ("内存", "85%", "warning"),
        ("磁盘", "50%", "success")
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
status.update_status("CPU使用率", "75%", "warning")
```

### Q: Can status values contain HTML?
A: Plain text is recommended to ensure correct display in all email clients.

## 🔗 Related Widgets

- [MetricWidget](metric-widget.md) - Data metrics display
- [ProgressWidget](progress-widget.md) - Progress status display
- [AlertWidget](alert-widget.md) - Status alert information
- [CardWidget](card-widget.md) - Card containing status
- [TableWidget](table-widget.md) - Tabular status display