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

# Create basic checklist
checklist = ChecklistWidget()
checklist.set_title("Development Tasks")
checklist.add_item("Complete requirements analysis", True)
checklist.add_item("Design database", True)
checklist.add_item("Write code", False)

email = Email("Project Progress Report")
email.add_widget(checklist)
```

### Advanced Usage

```python
# Checklist with progress statistics and status
checklist = ChecklistWidget()
checklist.set_title("Project Milestones")
checklist.add_item("Project launch", True, "success", "Project officially started")
checklist.add_item("Requirements confirmation", True, "success", "All requirements confirmed")
checklist.add_item("Design review", False, "warning", "Design proposal pending review")
checklist.add_item("Development implementation", False, "pending", "Waiting for development team")
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

# Create project management report email
email = Email("Project Management Report")

# Major milestones
checklist1 = ChecklistWidget()
checklist1.set_title("Project Milestones")
checklist1.add_item("Project launch", True, "success")
checklist1.add_item("Requirements analysis", True, "success")
checklist1.add_item("High-level design", True, "success")
checklist1.add_item("Detailed design", False, "warning")
checklist1.add_item("Development implementation", False, "pending")
checklist1.show_progress_stats(True)

email.add_widget(checklist1)

# Export HTML file
email.export_html("project_management_report.html")
```

--8<-- "assets/checklist_project_management.html"

### 2. System Operations Checklist

```python
from email_widget import Email
from email_widget.widgets.checklist_widget import ChecklistWidget

# Create system operations daily report email
email = Email("System Operations Daily Report")

# Daily check checklist
checklist = ChecklistWidget()
checklist.set_title("System Health Check")
checklist.add_item("Server status", True, "success")
checklist.add_item("Database connection", True, "success")
checklist.add_item("Disk space", False, "warning", "Needs attention")
checklist.add_item("Memory usage", True, "success")
checklist.add_item("Network connectivity", True, "success")
checklist.show_progress_stats(True)

email.add_widget(checklist)
```

--8<-- "assets/checklist_system_ops.html"

## ⚡ Shortcut Methods

The Email class provides the `add_checklist` shortcut method:

```python
# Shortcut method with parameters
email.add_checklist(
    title="Task List",
    items=[
        ("Task 1", True),
        ("Task 2", False),
        ("Task 3", False)
    ],
    show_progress=True,
    compact_mode=True
)
```

## 🐛 Common Issues

### Q: How to create tasks with different priorities?
A: Use different status_type values to represent priorities:
```python
checklist.add_item("High priority", False, "error")    # Red - urgent
checklist.add_item("Medium priority", False, "warning")  # Orange - important
checklist.add_item("Low priority", False, "info")     # Blue - normal
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