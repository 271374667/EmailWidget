# StatusWidget 状态组件

StatusWidget 是一个专门用于显示系统状态、配置信息或键值对数据的组件。它支持多种状态类型的颜色标识，提供灵活的布局选项，是监控面板和状态报告的理想选择。

## 🎯 组件预览

--8<-- "assets/status_widget_component_preview.html"

## ✨ 核心特性

- **📊 状态展示**: 支持键值对形式的状态信息展示
- **🎨 状态分类**: 支持SUCCESS、WARNING、ERROR、INFO等状态类型
- **📐 布局选择**: 支持垂直和水平两种布局方式
- **🔄 动态更新**: 支持动态添加、更新和移除状态项
- **📧 邮件兼容**: 使用邮件客户端兼容的HTML和CSS实现

## 🚀 快速开始

### 基础用法

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

### 进阶用法

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

📚 **完整API文档**: [StatusWidget API](../api/status-widget.md)

## 🎨 样式指南

### 状态类型和颜色

- **success**: 绿色 (#107c10) - 正常运行、成功状态
- **warning**: 橙色 (#ff8c00) - 需要注意、性能警告
- **error**: 红色 (#d13438) - 错误状态、服务异常
- **info**: 蓝色 (#0078d4) - 信息状态、配置项
- **neutral**: 灰色 (#8e8e93) - 中性状态、默认值

## 📱 最佳实践

### 1. 系统监控状态

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

### 2. 项目配置信息

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

## ⚡ 快捷方法

Email 类提供了 `add_status` 快捷方法：

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

## 🐛 常见问题

### Q: 如何选择垂直布局还是水平布局？
A: 
- **垂直布局**: 适合状态项较多或标签较长的情况
- **水平布局**: 适合快速浏览关键状态信息

### Q: 如何更新已存在的状态项？
A: 使用 `update_status` 方法：
```python
status.update_status("CPU使用率", "75%", "warning")
```

### Q: 状态值可以包含HTML吗？
A: 建议使用纯文本，以确保在所有邮件客户端中正确显示。

## 🔗 相关组件

- [MetricWidget](metric-widget.md) - 数据指标展示
- [ProgressWidget](progress-widget.md) - 进度状态显示
- [AlertWidget](alert-widget.md) - 状态提醒信息
- [CardWidget](card-widget.md) - 包含状态的卡片
- [TableWidget](table-widget.md) - 表格形式的状态展示