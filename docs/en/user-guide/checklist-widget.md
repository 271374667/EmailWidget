# ChecklistWidget

ChecklistWidget is a component for creating task lists, to-do items, or checklists in emails. It supports multiple status displays, progress statistics, and flexible style configurations, helping users clearly present project progress and task completion status.

## 🎯 Widget Preview

--8<-- "assets/checklist_widget_component_preview.html"

## ✨ Core Features

- **📝 Multiple Statuses**: Supports completed, incomplete, skipped, and other item statuses
- **🎨 Status Themes**: Theme color configuration based on StatusType, such as success, warning, error, etc.
- **📊 Progress Statistics**: Optional progress bar and completion percentage display
- **🔧 Flexible Configuration**: Supports compact mode, custom descriptions, status text, etc.
- **📧 Email Compatible**: Implemented using email client-compatible HTML and CSS

## 🚀 Quick Start

### Basic Usage

```python
from email_widget import Email
from email_widget.widgets import ChecklistWidget

# 创建基础清单
checklist = ChecklistWidget()
checklist.set_title("开发任务")
checklist.add_item("完成需求分析", True)
checklist.add_item("设计数据库", True)
checklist.add_item("编写代码", False)

email = Email("项目进度报告")
email.add_widget(checklist)
```

### Advanced Usage

```python
# 带进度统计和状态的清单
checklist = ChecklistWidget()
checklist.set_title("项目里程碑")
checklist.add_item("项目启动", True, "success", "项目已正式启动")
checklist.add_item("需求确认", True, "success", "所有需求已确认")
checklist.add_item("设计评审", False, "warning", "设计方案待审核")
checklist.add_item("开发实施", False, "pending", "等待开发团队")
checklist.show_progress_stats(True)
checklist.set_compact_mode(True)

email.add_widget(checklist)
```

📚 **Complete API Documentation**: [ChecklistWidget API](../api/checklist-widget.md)

## 🎨 Style Guide

### Status Types and Theme Colors

- **success**: Green (#107c10) - Completed important tasks
- **warning**: Orange (#ff8c00) - Items needing attention
- **error**: Red (#d13438) - Failed or blocked tasks
- **info**: Blue (#0078d4) - Informational or reference items
- **primary**: Blue (#0078d4) - Important ongoing tasks

## 📱 Best Practices

### 1. Project Management Checklist

```python
from email_widget import Email
from email_widget.widgets.checklist_widget import ChecklistWidget

# 创建项目管理报告邮件
email = Email("项目管理报告")

# 主要里程碑
checklist1 = ChecklistWidget()
checklist1.set_title("项目里程碑")
checklist1.add_item("项目启动", True, "success")
checklist1.add_item("需求分析", True, "success")
checklist1.add_item("概要设计", True, "success")
checklist1.add_item("详细设计", False, "warning")
checklist1.add_item("开发实施", False, "pending")
checklist1.show_progress_stats(True)

email.add_widget(checklist1)

# 导出HTML文件
email.export_html("project_management_report.html")
```

--8<-- "assets/checklist_project_management.html"

### 2. System Operations Checklist

```python
from email_widget import Email
from email_widget.widgets.checklist_widget import ChecklistWidget

# 创建系统运维日报邮件
email = Email("系统运维日报")

# 日常检查清单
checklist = ChecklistWidget()
checklist.set_title("系统健康检查")
checklist.add_item("服务器状态", True, "success")
checklist.add_item("数据库连接", True, "success")
checklist.add_item("磁盘空间", False, "warning", "需要关注")
checklist.add_item("内存使用", True, "success")
checklist.add_item("网络连通", True, "success")
checklist.show_progress_stats(True)

email.add_widget(checklist)
```

--8<-- "assets/checklist_system_ops.html"

## ⚡ Shortcut Methods

The Email class provides the `add_checklist` shortcut method:

```python
# 带参数的快捷方法
email.add_checklist(
    title="任务清单",
    items=[
        ("任务1", True),
        ("任务2", False),
        ("任务3", False)
    ],
    show_progress=True,
    compact_mode=True
)
```

## 🐛 Common Issues

### Q: How to create tasks with different priorities?
A: Use different status_type values to represent priorities:
```python
checklist.add_item("高优先级", False, "error")    # 红色-紧急
checklist.add_item("中优先级", False, "warning")  # 橙色-重要
checklist.add_item("低优先级", False, "info")     # 蓝色-普通
```

### Q: What's the difference between skipped and incomplete status?
A: 
- Incomplete (False): Counted in total progress, tasks that need completion
- Skipped (None): Not counted in progress statistics, skipped tasks

### Q: Why doesn't the progress bar show?
A: Make sure you called the `show_progress_stats(True)` method.

## 🔗 Related Widgets

- [ProgressWidget](progress-widget.md) - Single item progress display
- [StatusWidget](status-widget.md) - Status information display
- [CardWidget](card-widget.md) - Card that can contain checklists
- [AlertWidget](alert-widget.md) - Alerts that can be used with checklists