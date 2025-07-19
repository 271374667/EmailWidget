# CardWidget

CardWidget is a versatile card container component used to display structured content information. It supports combined display of titles, content, icons, and metadata, making it ideal for building information panels, product showcases, and content summaries.

## 🎯 Widget Preview

--8<-- "assets/card_widget_component_preview.html"

## ✨ Core Features

- **📋 Content Display**: Supports combined display of titles, content, and icons
- **🏷️ Metadata Management**: Supports key-value pair metadata information display
- **🎨 Style Customization**: Optional card shadows, border radius, and padding adjustments
- **📱 Status Indication**: Supports visual feedback and status display for different states
- **📧 Email Compatible**: Implemented using email client-compatible HTML and CSS

## 🚀 Quick Start

### Basic Usage

```python
from email_widget import Email
from email_widget.widgets import CardWidget
from email_widget.core.enums import StatusType, IconType

# Create email
email = Email("Card Widget Example")

# Create basic card
card = CardWidget()
card.set_title("Product Introduction")
card.set_content("This is a powerful email widget library that provides rich UI components.")
card.set_icon(IconType.INFO)

email.add_widget(card)

# Using shortcut method
email.add_card("Quick Card", "Card component created with shortcut method")

# Export HTML
email.export_html("card_demo.html")
```

### Advanced Usage

```python
# Create detailed card with metadata
product_card = CardWidget()
product_card.set_title("EmailWidget Pro")
product_card.set_content("Professional Python email widget library providing rich UI components and powerful email rendering capabilities.")
product_card.set_icon(IconType.SUCCESS)
product_card.set_status(StatusType.SUCCESS)

# Add metadata information
product_card.add_metadata("Version", "v2.1.0")
product_card.add_metadata("License", "MIT")
product_card.add_metadata("Python Support", "3.8+")
product_card.add_metadata("Last Updated", "2024-01-15")

email.add_widget(product_card)

# Batch set metadata
metadata = {
    "Author": "Python Development Team",
    "Size": "2.5MB",
    "Downloads": "10K+"
}
product_card.set_metadata(metadata)
```

📚 **Complete API Documentation**: [CardWidget API](../api/card-widget.md)

## 🎨 Style Guide

### Status Types and Colors

- **SUCCESS**: Green (#107c10) - Success status, normal operation, completed status
- **WARNING**: Orange (#ff8c00) - Warning status, needs attention, pending
- **ERROR**: Red (#d13438) - Error status, failed status, exception situation
- **INFO**: Blue (#0078d4) - Information status, general information, tips
- **PRIMARY**: Blue (#0078d4) - Primary content, important information, core features

### Icon Usage Recommendations

- **IconType.INFO**: 📄 For information display, document descriptions
- **IconType.SUCCESS**: ✅ For success status, completed tasks
- **IconType.WARNING**: ⚠️ For warning information, precautions
- **IconType.ERROR**: ❌ For error information, failure status
- **Custom Icons**: 🎯 📊 🚀 etc., choose appropriate icons based on content

## 📱 Best Practices

### 1. Product Showcase Card

```python
from email_widget import Email
from email_widget.widgets import CardWidget
from email_widget.core.enums import StatusType, IconType

# Create product showcase email
email = Email("Product Showcase")

# Main product card
product_card = CardWidget()
product_card.set_title("EmailWidget Pro")
product_card.set_content("Professional Python email widget library providing rich UI components and powerful email rendering capabilities. Supports multiple widget types and perfectly adapts to various email clients.")
product_card.set_icon("🎯")
product_card.set_status(StatusType.SUCCESS)

# Add product information
product_card.add_metadata("Version", "v2.1.0")
product_card.add_metadata("License", "MIT")
product_card.add_metadata("Python Support", "3.8+")
product_card.add_metadata("Last Updated", "2024-01-15")

email.add_widget(product_card)

# Feature card
feature_card = CardWidget()
feature_card.set_title("Core Features")
feature_card.set_content("Provides 15+ beautiful widgets, supports tables, charts, progress bars, timelines, and other display methods to meet various email scenario needs.")
feature_card.set_icon("⚡")

email.add_widget(feature_card)

# Export HTML file
email.export_html("product_showcase.html")
```

--8<-- "assets/temp/card_product_showcase.html"

### 2. User Information Panel

```python
# Create user information panel email
email = Email("User Information Panel")

# User basic information card
user_card = CardWidget()
user_card.set_title("User Profile")
user_card.set_content("Senior Development Engineer, focusing on Python backend development and data analysis. Has 5+ years of project experience, familiar with multiple development frameworks and tools.")
user_card.set_icon("👤")
user_card.set_status(StatusType.SUCCESS)

# Add user detailed information
user_card.add_metadata("Name", "Li Developer")
user_card.add_metadata("Position", "Senior Engineer")
user_card.add_metadata("Department", "Technology Department")
user_card.add_metadata("Join Date", "2019-03-15")
user_card.add_metadata("Email", "li.dev@example.com")

email.add_widget(user_card)

# Skills display card
skill_card = CardWidget()
skill_card.set_title("Technical Skills")
skill_card.set_content("Proficient in Python, Django, FastAPI and other backend technology stacks, with rich experience in database design and API development.")
skill_card.set_icon("🛠️")

skill_card.add_metadata("Main Skills", "Python, Django, FastAPI")
skill_card.add_metadata("Database", "MySQL, PostgreSQL, Redis")
skill_card.add_metadata("Project Experience", "5+ years")

email.add_widget(skill_card)

email.export_html("user_profile.html")
```

--8<-- "assets/temp/card_user_profile.html"

### 3. Project Status Dashboard

```python
# Create project status dashboard email
email = Email("Project Status Dashboard")

# Project progress card
project_card = CardWidget()
project_card.set_title("Project Progress")
project_card.set_content("EmailWidget project development is progressing smoothly. Core functionality development is complete, currently in testing and documentation phase. Expected to release official version by the end of this month.")
project_card.set_icon("📊")
project_card.set_status(StatusType.SUCCESS)

project_card.add_metadata("Project Name", "EmailWidget")
project_card.add_metadata("Current Version", "v2.1.0-beta")
project_card.add_metadata("Completion", "85%")
project_card.add_metadata("Expected Release", "2024-01-30")

email.add_widget(project_card)

# Team status card
team_card = CardWidget()
team_card.set_title("Team Status")
team_card.set_content("Development team is running normally, all members are actively participating in project development. Currently conducting final testing and optimization.")
team_card.set_icon("👥")

team_card.add_metadata("Team Size", "6 people")
team_card.add_metadata("Developers", "4 people")
team_card.add_metadata("Testers", "2 people")

email.add_widget(team_card)

email.export_html("project_dashboard.html")
```

--8<-- "assets/temp/card_project_dashboard.html"

## ⚡ Shortcut Methods

The Email class provides the `add_card` shortcut method:

```python
# Basic shortcut method
email.add_card("Card Title", "Card Content")

# Shortcut method with icon
email.add_card("Product Introduction", "This is an excellent product", icon="🎯")

# Shortcut method with metadata
email.add_card(
    title="User Information",
    content="User detailed information display",
    metadata={
        "Name": "Zhang San",
        "Department": "Technology Department",
        "Position": "Engineer"
    }
)

# Shortcut method with status
email.add_card(
    title="System Status",
    content="System running normally",
    status=StatusType.SUCCESS,
    icon=IconType.SUCCESS
)
```

## 🐛 Common Issues

### Q: How to handle overly long card content?
A: CardWidget automatically handles line breaks and layout for long content. It's recommended to split overly long content into multiple cards or use metadata to organize information.

### Q: How to customize card styles?
A: You can change card theme colors by setting different StatusType values. For more customization, use CSS override methods.

### Q: What to do when metadata information is not fully displayed?
A: Check if metadata keys and values are too long. Recommend using short key names and appropriate value lengths. If there's a lot of information, display it across multiple cards.

### Q: Card displays abnormally in some email clients?
A: CardWidget uses email client-compatible layout methods. If issues occur, try simplifying card content or using alternative widgets.

### Q: How to manage multiple cards in batch?
A: Organize card information into lists, then use loops to create in batch:
```python
cards_data = [
    {"title": "Card 1", "content": "Content 1"},
    {"title": "Card 2", "content": "Content 2"}
]
for data in cards_data:
    email.add_card(data["title"], data["content"])
```

## 🔗 Related Widgets

- [StatusWidget](status-widget.md) - For displaying simple status information
- [AlertWidget](alert-widget.md) - Can add alert information in cards
- [TextWidget](text-widget.md) - For detailed text content in cards
- [SeparatorWidget](separator-widget.md) - For separating different card groups