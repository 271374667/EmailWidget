# 📚 Basic Concepts

Before diving into EmailWidget, understanding its core concepts will help you build better email reports. This chapter introduces EmailWidget's design philosophy and key concepts.

## 📧 Email Class Overview

### Basic Concepts

The `Email` class is the core of EmailWidget, serving as the container and manager for all Widgets:

```python
from email_widget import Email, TextWidget

# Create email object
email = Email(title="Report Title")

# Set metadata
email.set_subtitle("Subtitle")
email.set_footer("Footer Information")

# Manage Widgets
email.add_widget(TextWidget('Hello, World!'))
email.remove_widget("Hello, World!")
email.clear_widgets()

# Export results
html_content = email.export_str()
file_path = email.export_html("report.html")
```

### Lifecycle

The typical lifecycle of an Email object:

1. **Creation** - Initialize email object
2. **Configuration** - Set title, subtitle, footer, etc.
3. **Content Addition** - Add various Widget components
4. **Rendering** - Generate HTML content
5. **Export** - Save to file or get string

### Features

=== "Convenience Methods"
    
    ```python
    # Directly add common content
    email.add_text("Title", text_type="title_large")
    email.add_table_from_data(data, headers)
    email.add_progress(75, "Completion")
    email.add_chart_from_plt(title="Chart")
    ```

=== "Widget Management"
    
    ```python
    # Get Widget
    widget = email.get_widget("my_widget_id")
    
    # Remove Widget
    email.remove_widget("widget_id")
    
    # Clear all Widgets
    email.clear_widgets()
    
    # Get Widget count
    count = email.get_widget_count()
    ```

=== "Method Chaining"
    
    ```python
    # Fluent API design
    email = (Email("Title")
             .set_subtitle("Subtitle")
             .set_footer("Footer")
             .add_widget(widget1)
             .add_widget(widget2))
    ```

## 🧩 Widget Component System

### Design Philosophy

All Widget components inherit from `BaseWidget`, ensuring API consistency:

```python
from email_widget.core.base import BaseWidget

class MyCustomWidget(BaseWidget):
    def __init__(self):
        super().__init__()
        self.widget_type = "custom"
    
    def render(self) -> str:
        # Rendering logic
        return self._render_template("custom.html", context)
```

### Common Features

All Widgets share the following common features:

=== "ID Management"
    
    ```python
    # Set unique ID
    widget.set_widget_id("my_unique_id")
    
    # Get ID
    widget_id = widget.widget_id
    
    # Get type
    widget_type = widget.widget_type
    ```

=== "Template Rendering"
    
    ```python
    # Get rendering context
    context = widget.get_template_context()
    
    # Render to HTML
    html = widget.render_html()
    ```

### Widget Categories

EmailWidget provides 12 professional components, categorized by function:

#### 📝 Content Components
- **TextWidget** - Text content, 8 styles
- **ImageWidget** - Image display, multi-source support
- **QuoteWidget** - Quote style, author information

#### 📊 Data Components  
- **TableWidget** - Data tables, DataFrame integration
- **ChartWidget** - Chart display, matplotlib support
- **LogWidget** - Log display, level classification

#### 📈 Metric Components
- **ProgressWidget** - Linear progress bar, 5 themes
- **CircularProgressWidget** - Circular progress, multiple sizes
- **StatusWidget** - Status management, dynamic updates

#### 🎨 Interface Components
- **AlertWidget** - Alert reminders, 5 types
- **CardWidget** - Information cards, icon support
- **ColumnWidget** - Layout container, responsive design


## 🎯 Best Practices

### Code Organization

Recommended code organization:

```python
# 1. Import necessary libraries
from email_widget import Email, TextWidget, TableWidget, EmailConfig
from email_widget.core.enums import TextType


# 2. Data preparation
def prepare_data():
    return {"sales": [100, 200, 300]}


# 3. Email building
def build_email(data):
    email = Email("Sales Report")
    # Add content
    email.add_widget(
        TextWidget().set_content("Sales Data Analysis").set_type(TextType.TITLE_LARGE)
    )

    return email


# 4. Main function
def main():
    data = prepare_data()
    email = build_email(data)
    email.export_html("report.html")
```

## 🚀 Next Steps

Now that you understand EmailWidget's core concepts, you can:

- Check out [User Guide](../user-guide/index.md) to learn detailed component usage
- Browse [API Reference](../api/index.md) to understand the complete API
- Study [Example Code](../examples/index.md) to learn practical applications
- Read [Development Guide](../development/index.md) to participate in project development