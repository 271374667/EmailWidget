# TimelineWidget 时间线组件

TimelineWidget 是一个用于在邮件中展示时间序列事件的组件。它能够按时间顺序显示项目进展、系统日志、历史记录等信息，支持状态标记、时间戳显示和灵活的样式配置。

## 🎯 组件预览

--8<-- "assets/timeline_widget_component_preview.html"

## ✨ 核心特性

- **⏰ 时间排序**: 自动按时间顺序排列事件，支持正序和倒序
- **🎨 状态主题**: 基于StatusType的主题颜色配置，如成功、警告、错误等
- **📅 时间解析**: 智能解析多种时间格式，包括日期和时间戳
- **⚙️ 灵活配置**: 支持显示/隐藏时间戳、倒序排列等选项
- **📧 邮件兼容**: 使用邮件客户端兼容的HTML和CSS实现

## 🚀 快速开始

### 基础用法

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

### 进阶用法

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

📚 **完整API文档**: [TimelineWidget API](../api/timeline-widget.md)

## 🎨 样式指南

### 状态类型和主题颜色

- **success**: 绿色 (#107c10) - 成功完成的任务、里程碑达成
- **warning**: 橙色 (#ff8c00) - 需要注意的事件、性能警告
- **error**: 红色 (#d13438) - 错误、故障、失败事件
- **info**: 蓝色 (#0078d4) - 信息性事件、通知、发布
- **primary**: 蓝色 (#0078d4) - 重要事件、关键节点

## 📱 最佳实践

### 1. 项目进展时间线

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

### 2. 系统运维日志

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

## ⚡ 快捷方法

Email 类提供了 `add_timeline` 快捷方法：

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

## 🐛 常见问题

### Q: 时间格式有什么要求？
A: 支持多种时间格式，自动解析：
```python
timeline.add_event("事件1", "2024-01-01")              # 日期
timeline.add_event("事件2", "2024-01-01 15:30")        # 日期时间
timeline.add_event("事件3", datetime.now())            # datetime对象
```

### Q: 如何处理相同时间的事件？
A: 相同时间的事件按添加顺序排列。

### Q: 倒序和正序有什么区别？
A: 
- 正序 (False): 最早事件在上，最新事件在下
- 倒序 (True): 最新事件在上，最早事件在下

## 🔗 相关组件

- [ChecklistWidget](checklist-widget.md) - 任务进度展示
- [ProgressWidget](progress-widget.md) - 进度条显示
- [StatusWidget](status-widget.md) - 状态信息展示
- [LogWidget](log-widget.md) - 日志信息展示
- [CardWidget](card-widget.md) - 可以包含时间线的卡片