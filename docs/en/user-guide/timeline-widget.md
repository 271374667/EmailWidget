# TimelineWidget

TimelineWidget is a component for displaying time-series events in emails. It can display project progress, system logs, historical records, and other information in chronological order, supporting status markers, timestamp display, and flexible style configuration.

## 🎯 Widget Preview

--8<-- "assets/timeline_widget_component_preview.html"

## ✨ Core Features

- **⏰ Time Ordering**: Automatically arranges events in chronological order, supports ascending and descending order
- **🎨 Status Themes**: Theme color configuration based on StatusType, such as success, warning, error, etc.
- **📅 Time Parsing**: Intelligently parses multiple time formats, including dates and timestamps
- **⚙️ Flexible Configuration**: Supports showing/hiding timestamps, reverse ordering, and other options
- **📧 Email Compatible**: Implemented using email client-compatible HTML and CSS

## 🚀 Quick Start

### Basic Usage

```python
from email_widget import Email
from email_widget.widgets import TimelineWidget

# 创建基础时间线
timeline = TimelineWidget()
timeline.set_title("项目历程")
timeline.add_event("项目启动", "2024-01-01", "项目正式开始")
timeline.add_event("需求确认", "2024-01-15", "完成需求分析")
timeline.add_event("设计评审", "2024-02-01", "UI设计通过评审")

email = Email("项目进展报告")
email.add_widget(timeline)
```

### Advanced Usage

```python
# 带状态和时间戳的详细时间线
timeline = TimelineWidget()
timeline.set_title("系统监控日志")
timeline.add_event("系统启动", "2024-01-01 09:00:00", "服务器启动成功", "success")
timeline.add_event("用户登录", "2024-01-01 09:15:30", "管理员用户登录", "info")
timeline.add_event("发现警告", "2024-01-01 10:30:00", "CPU使用率过高", "warning")
timeline.add_event("问题解决", "2024-01-01 11:00:00", "系统性能恢复正常", "success")
timeline.show_timestamps(True)
timeline.set_reverse_order(True)

email.add_widget(timeline)
```

📚 **Complete API Documentation**: [TimelineWidget API](../api/timeline-widget.md)

## 🎨 Style Guide

### Status Types and Theme Colors

- **success**: Green (#107c10) - Successfully completed tasks, milestone achievements
- **warning**: Orange (#ff8c00) - Events requiring attention, performance warnings
- **error**: Red (#d13438) - Errors, failures, exception events
- **info**: Blue (#0078d4) - Informational events, notifications, releases
- **primary**: Blue (#0078d4) - Important events, key milestones

## 📱 Best Practices

### 1. Project Progress Timeline

```python
from email_widget import Email
from email_widget.widgets.timeline_widget import TimelineWidget

# 创建项目进展报告邮件
email = Email("项目进展报告")

# 项目关键里程碑
timeline1 = TimelineWidget()
timeline1.set_title("项目里程碑")
timeline1.add_event("项目启动", "2024-01-01", "项目正式启动", "success")
timeline1.add_event("需求确认", "2024-01-15", "需求文档确认完成", "success")
timeline1.add_event("设计评审", "2024-02-01", "技术架构设计通过", "success")
timeline1.add_event("开发阶段", "2024-02-15", "进入开发阶段", "info")
timeline1.add_event("测试阶段", "2024-03-15", "功能测试开始", "warning")
timeline1.show_timestamps(True)

email.add_widget(timeline1)

# 导出HTML文件
email.export_html("project_progress_report.html")
```

--8<-- "assets/timeline_project_progress.html"

### 2. System Operations Log

```python
from email_widget import Email
from email_widget.widgets.timeline_widget import TimelineWidget

# 创建系统运维日报邮件
email = Email("系统运维日报")

# 系统事件时间线
timeline = TimelineWidget()
timeline.set_title("系统事件日志")
timeline.add_event("系统启动", "2024-01-01 08:00:00", "服务器重启完成", "success")
timeline.add_event("定时备份", "2024-01-01 12:00:00", "数据库自动备份", "info")
timeline.add_event("内存警告", "2024-01-01 14:30:00", "内存使用率达到85%", "warning")
timeline.add_event("服务异常", "2024-01-01 15:45:00", "Redis连接超时", "error")
timeline.add_event("问题修复", "2024-01-01 16:15:00", "Redis服务重启，连接恢复", "success")
timeline.show_timestamps(True)
timeline.set_reverse_order(True)

email.add_widget(timeline)
```

--8<-- "assets/timeline_system_ops.html"

## ⚡ Shortcut Methods

The Email class provides the `add_timeline` shortcut method:

```python
# 带参数的快捷方法
email.add_timeline(
    title="项目时间线",
    events=[
        ("事件1", "2024-01-01", "描述1"),
        ("事件2", "2024-01-02", "描述2", "success"),
        ("事件3", "2024-01-03", "描述3", "warning")
    ],
    show_time=True,
    reverse_order=True
)
```

## 🐛 Common Issues

### Q: What are the requirements for time formats?
A: Supports multiple time formats with automatic parsing:
```python
timeline.add_event("事件1", "2024-01-01")              # 日期
timeline.add_event("事件2", "2024-01-01 15:30")        # 日期时间
timeline.add_event("事件3", datetime.now())            # datetime对象
```

### Q: How to handle events with the same time?
A: Events with the same time are arranged in the order they were added.

### Q: What's the difference between reverse and normal order?
A: 
- Normal order (False): Earliest events at top, latest events at bottom
- Reverse order (True): Latest events at top, earliest events at bottom

## 🔗 Related Widgets

- [ChecklistWidget](checklist-widget.md) - Task progress display
- [ProgressWidget](progress-widget.md) - Progress bar display
- [StatusWidget](status-widget.md) - Status information display
- [LogWidget](log-widget.md) - Log information display
- [CardWidget](card-widget.md) - Cards that can contain timelines