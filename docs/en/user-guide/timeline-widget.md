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

# Create basic timeline
timeline = TimelineWidget()
timeline.set_title("Project Timeline")
timeline.add_event("Project Launch", "2024-01-01", "Project officially started")
timeline.add_event("Requirements Confirmed", "2024-01-15", "Completed requirements analysis")
timeline.add_event("Design Review", "2024-02-01", "UI design passed review")

email = Email("Project Progress Report")
email.add_widget(timeline)
```

### Advanced Usage

```python
# Detailed timeline with status and timestamps
timeline = TimelineWidget()
timeline.set_title("System Monitoring Log")
timeline.add_event("System Startup", "2024-01-01 09:00:00", "Server started successfully", "success")
timeline.add_event("User Login", "2024-01-01 09:15:30", "Administrator user logged in", "info")
timeline.add_event("Warning Detected", "2024-01-01 10:30:00", "High CPU usage detected", "warning")
timeline.add_event("Issue Resolved", "2024-01-01 11:00:00", "System performance restored to normal", "success")
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

# Create project progress report email
email = Email("Project Progress Report")

# Project key milestones
timeline1 = TimelineWidget()
timeline1.set_title("Project Milestones")
timeline1.add_event("Project Launch", "2024-01-01", "Project officially launched", "success")
timeline1.add_event("Requirements Confirmed", "2024-01-15", "Requirements document confirmation completed", "success")
timeline1.add_event("Design Review", "2024-02-01", "Technical architecture design approved", "success")
timeline1.add_event("Development Phase", "2024-02-15", "Entered development phase", "info")
timeline1.add_event("Testing Phase", "2024-03-15", "Functional testing started", "warning")
timeline1.show_timestamps(True)

email.add_widget(timeline1)

# Export HTML file
email.export_html("project_progress_report.html")
```

--8<-- "assets/timeline_project_progress.html"

### 2. System Operations Log

```python
from email_widget import Email
from email_widget.widgets.timeline_widget import TimelineWidget

# Create system operations daily report email
email = Email("System Operations Daily Report")

# System event timeline
timeline = TimelineWidget()
timeline.set_title("System Event Log")
timeline.add_event("System Startup", "2024-01-01 08:00:00", "Server restart completed", "success")
timeline.add_event("Scheduled Backup", "2024-01-01 12:00:00", "Database automatic backup", "info")
timeline.add_event("Memory Warning", "2024-01-01 14:30:00", "Memory usage reached 85%", "warning")
timeline.add_event("Service Exception", "2024-01-01 15:45:00", "Redis connection timeout", "error")
timeline.add_event("Issue Fixed", "2024-01-01 16:15:00", "Redis service restarted, connection restored", "success")
timeline.show_timestamps(True)
timeline.set_reverse_order(True)

email.add_widget(timeline)
```

--8<-- "assets/timeline_system_ops.html"

## ⚡ Shortcut Methods

The Email class provides the `add_timeline` shortcut method:

```python
# Shortcut method with parameters
email.add_timeline(
    title="Project Timeline",
    events=[
        ("Event 1", "2024-01-01", "Description 1"),
        ("Event 2", "2024-01-02", "Description 2", "success"),
        ("Event 3", "2024-01-03", "Description 3", "warning")
    ],
    show_time=True,
    reverse_order=True
)
```

## 🐛 Common Issues

### Q: What are the requirements for time formats?
A: Supports multiple time formats with automatic parsing:
```python
timeline.add_event("Event 1", "2024-01-01")              # Date
timeline.add_event("Event 2", "2024-01-01 15:30")        # Date and time
timeline.add_event("Event 3", datetime.now())            # datetime object
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