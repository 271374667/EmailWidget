# ColumnWidget

ColumnWidget is a powerful layout component used to create multi-column layouts, arranging multiple widgets in columns. It supports automatic column mode and manual column setting, using table layout to ensure compatibility across various email clients, making it a core component for building complex email layouts.

## 🎯 Widget Preview

--8<-- "assets/column_widget_component_preview.html"

## ✨ Core Features

- **📏 Auto Layout**: Automatically calculates optimal column count based on widget quantity
- **🔧 Manual Control**: Supports manual setting of 1-4 columns
- **📧 Email Compatible**: Uses table layout to ensure email client compatibility
- **🎨 Flexible Configuration**: Supports column gap adjustment and responsive design
- **⚡ Dynamic Management**: Supports dynamic adding, removing, and updating of widgets
- **📱 Responsive**: Maintains good display across different email clients

## 🚀 Quick Start

### Basic Usage

```python
from email_widget import Email
from email_widget.widgets import ColumnWidget, TextWidget

# Create column layout widget
column = ColumnWidget()

# Create child widgets
widget1 = TextWidget().set_content("First column content")
widget2 = TextWidget().set_content("Second column content")  
widget3 = TextWidget().set_content("Third column content")

# Add to layout (3 widgets automatically use 3 columns)
column.add_widgets([widget1, widget2, widget3])

email = Email("Multi-column Layout Example")
email.add_widget(column)
```

### Advanced Usage

```python
# Fixed column layout
column = ColumnWidget()
column.set_columns(2)  # Fixed 2 columns
column.set_gap("25px")  # Set column gap

# Create multiple widgets
from email_widget.widgets import StatusWidget, MetricWidget

status = StatusWidget().set_title("System Status")
status.add_status("CPU", "68%", "warning")
status.add_status("Memory", "4.2GB", "info")

metric = MetricWidget().set_title("Key Metrics")
metric.add_metric("Users", 12345, "people", "+15.6%", "success")

column.add_widgets([status, metric])
email.add_widget(column)
```

📚 **Complete API Documentation**: [ColumnWidget API](../api/column-widget.md)

## 🎨 Style Guide

### Auto Column Algorithm

| Widget Count | Auto Columns | Layout Description |
|--------------|--------------|--------------------|
| 1 | 1 column | Single column full width |
| 2 | 2 columns | Left and right columns evenly distributed |
| 3 | 3 columns | Three columns evenly distributed |
| 4 | 2 columns | 2×2 grid layout |
| 5-6 | 3 columns | Three column layout, last row may not be full |
| 7-8 | 2 columns | Two column layout, multi-row display |
| 9+ | 3 columns | Three column layout, multi-row display |

### Column Gap Recommendations

- **Text Content**: 15px - 20px
- **Card Components**: 20px - 25px  
- **Image Components**: 10px - 15px
- **Status Components**: 20px - 30px

## 📱 Best Practices

### 1. Auto Column Layout

```python
from email_widget import Email
from email_widget.widgets import ColumnWidget, CardWidget

email = Email("Dashboard Report")

# Create auto column layout
auto_column = ColumnWidget()  # Default auto mode

# Create multiple cards (6 widgets automatically use 3 columns)
cards = []
for i in range(6):
    card = CardWidget()
    card.set_title(f"Metric {i+1}")
    card.set_content(f"This is data display for metric {i+1}")
    cards.append(card)

auto_column.add_widgets(cards)
email.add_widget(auto_column)
```

--8<-- "assets/temp/column_auto_layout.html"

### 2. Fixed Column Layout

```python
from email_widget import Email
from email_widget.widgets import ColumnWidget, StatusWidget

email = Email("System Monitoring Report")

# Create fixed 2-column layout
fixed_column = ColumnWidget().set_columns(2)
fixed_column.set_gap("30px")

# System status widget
system_status = StatusWidget()
system_status.set_title("System Resources")
system_status.add_status("CPU Usage", "68%", "success")
system_status.add_status("Memory Usage", "85%", "warning")

# Service status widget
service_status = StatusWidget()
service_status.set_title("Service Status")
service_status.add_status("Web Service", "Running", "success")
service_status.add_status("Database", "Normal", "success")

fixed_column.add_widgets([system_status, service_status])
email.add_widget(fixed_column)
```

--8<-- "assets/temp/column_fixed_layout.html"

### 3. Mixed Component Layout

```python
from email_widget import Email
from email_widget.widgets import (
    ColumnWidget, TextWidget, AlertWidget, 
    ProgressWidget, ImageWidget
)

email = Email("Comprehensive Report")

# Create mixed component layout
mixed_column = ColumnWidget().set_columns(3)

# Different types of widgets
text_widget = TextWidget().set_content("Welcome to this month's report")
alert_widget = AlertWidget().set_content("Note: System maintenance tonight").set_alert_type("warning")
progress_widget = ProgressWidget().set_progress(75).set_label("Project Progress")

mixed_column.add_widgets([text_widget, alert_widget, progress_widget])
email.add_widget(mixed_column)
```

--8<-- "assets/temp/column_mixed_layout.html"

### 4. Responsive Layout

```python
from email_widget import Email
from email_widget.widgets import ColumnWidget

def create_responsive_layout(widgets):
    """Create responsive layout"""
    column = ColumnWidget()  # Use auto mode
    
    # Set gap based on widget count
    if len(widgets) <= 2:
        column.set_gap("30px")  # Increase gap for few widgets
    elif len(widgets) <= 4:
        column.set_gap("20px")  # Default gap for medium count
    else:
        column.set_gap("15px")  # Reduce gap for many widgets
    
    column.add_widgets(widgets)
    return column

# Use responsive layout
email = Email("Responsive Layout Example")
widgets = [widget1, widget2, widget3, widget4]
responsive_layout = create_responsive_layout(widgets)
email.add_widget(responsive_layout)
```

--8<-- "assets/temp/column_responsive_layout.html"

## ⚡ Shortcut Methods

The Email class provides the `add_column` shortcut method:

```python
# Auto column shortcut method
email.add_column([widget1, widget2, widget3])

# Specified column shortcut method
email.add_column(
    widgets=[widget1, widget2, widget3, widget4],
    columns=2,
    gap="25px"
)

# Responsive column layout
email.add_column(
    widgets=[widget1, widget2, widget3],
    auto_columns=True,
    gap="20px"
)
```

## 🐛 Common Issues

### Q: How to determine the optimal column count?
A: Recommend using auto mode, the system will automatically choose based on content quantity:
```python
column = ColumnWidget()  # Auto mode, no need to set column count
```

### Q: How does it display on mobile devices?
A: Email clients usually automatically adjust to single column display:
```python
# Set smaller gap for mobile adaptation
column.set_gap("15px")  # Smaller gap suitable for mobile
```

### Q: How to handle widgets with different heights?
A: Components automatically use `vertical-align: top` to ensure top alignment:
```python
# No additional settings needed, components auto-align
column.add_widgets([tall_widget, short_widget])
```

### Q: What if column gap is too large or too small?
A: Use the `set_gap()` method to adjust:
```python
column.set_gap("15px")  # Small gap
column.set_gap("25px")  # Large gap
```

### Q: How to dynamically update layout?
A: Use dynamic management methods:
```python
# Clear and re-add
column.clear_widgets()
column.add_widgets(new_widgets)

# Or remove by index
column.remove_widget_by_index(0)
```

## 🔗 Related Widgets

- [CardWidget](card-widget.md) - Card widgets commonly used in column layouts
- [StatusWidget](status-widget.md) - Status widgets suitable for multi-column display
- [MetricWidget](metric-widget.md) - Metric widgets suitable for side-by-side display
- [TextWidget](text-widget.md) - Basic text layout widgets
- [ImageWidget](image-widget.md) - Image grid layout widgets