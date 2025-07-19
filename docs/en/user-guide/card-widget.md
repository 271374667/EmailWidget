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

# 创建邮件
email = Email("卡片组件示例")

# 创建基础卡片
card = CardWidget()
card.set_title("产品介绍")
card.set_content("这是一个功能强大的邮件组件库，提供了丰富的UI组件。")
card.set_icon(IconType.INFO)

email.add_widget(card)

# 使用快捷方法
email.add_card("快捷卡片", "使用快捷方法创建的卡片组件")

# 导出HTML
email.export_html("card_demo.html")
```

### Advanced Usage

```python
# 创建带元数据的详细卡片
product_card = CardWidget()
product_card.set_title("EmailWidget Pro")
product_card.set_content("专业的Python邮件组件库，提供丰富的UI组件和强大的邮件渲染能力。")
product_card.set_icon(IconType.SUCCESS)
product_card.set_status(StatusType.SUCCESS)

# 添加元数据信息
product_card.add_metadata("版本", "v2.1.0")
product_card.add_metadata("许可证", "MIT")
product_card.add_metadata("支持Python", "3.8+")
product_card.add_metadata("最后更新", "2024-01-15")

email.add_widget(product_card)

# 批量设置元数据
metadata = {
    "作者": "Python开发团队",
    "大小": "2.5MB",
    "下载量": "10K+"
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

# 创建产品展示邮件
email = Email("产品展示")

# 主要产品卡片
product_card = CardWidget()
product_card.set_title("EmailWidget Pro")
product_card.set_content("专业的Python邮件组件库，提供丰富的UI组件和强大的邮件渲染能力。支持多种组件类型，完美适配各种邮件客户端。")
product_card.set_icon("🎯")
product_card.set_status(StatusType.SUCCESS)

# 添加产品信息
product_card.add_metadata("版本", "v2.1.0")
product_card.add_metadata("许可证", "MIT")
product_card.add_metadata("支持Python", "3.8+")
product_card.add_metadata("最后更新", "2024-01-15")

email.add_widget(product_card)

# 功能特性卡片
feature_card = CardWidget()
feature_card.set_title("核心功能")
feature_card.set_content("提供15+个精美组件，支持表格、图表、进度条、时间线等多种展示方式，满足各种邮件场景需求。")
feature_card.set_icon("⚡")

email.add_widget(feature_card)

# 导出HTML文件
email.export_html("product_showcase.html")
```

--8<-- "assets/temp/card_product_showcase.html"

### 2. User Information Panel

```python
# 创建用户信息面板邮件
email = Email("用户信息面板")

# 用户基本信息卡片
user_card = CardWidget()
user_card.set_title("用户档案")
user_card.set_content("高级开发工程师，专注于Python后端开发和数据分析。拥有5年以上的项目经验，熟悉多种开发框架和工具。")
user_card.set_icon("👤")
user_card.set_status(StatusType.SUCCESS)

# 添加用户详细信息
user_card.add_metadata("姓名", "李开发")
user_card.add_metadata("职位", "高级工程师")
user_card.add_metadata("部门", "技术部")
user_card.add_metadata("入职时间", "2019-03-15")
user_card.add_metadata("邮箱", "li.dev@example.com")

email.add_widget(user_card)

# 技能展示卡片
skill_card = CardWidget()
skill_card.set_title("技能专长")
skill_card.set_content("精通Python、Django、FastAPI等后端技术栈，具备丰富的数据库设计和API开发经验。")
skill_card.set_icon("🛠️")

skill_card.add_metadata("主要技能", "Python, Django, FastAPI")
skill_card.add_metadata("数据库", "MySQL, PostgreSQL, Redis")
skill_card.add_metadata("项目经验", "5年+")

email.add_widget(skill_card)

email.export_html("user_profile.html")
```

--8<-- "assets/temp/card_user_profile.html"

### 3. Project Status Dashboard

```python
# 创建项目状态仪表板邮件
email = Email("项目状态仪表板")

# 项目进展卡片
project_card = CardWidget()
project_card.set_title("项目进展")
project_card.set_content("EmailWidget项目开发进展顺利，目前已完成核心功能开发，正在进行测试和文档编写阶段。预计本月底发布正式版本。")
project_card.set_icon("📊")
project_card.set_status(StatusType.SUCCESS)

project_card.add_metadata("项目名称", "EmailWidget")
project_card.add_metadata("当前版本", "v2.1.0-beta")
project_card.add_metadata("完成进度", "85%")
project_card.add_metadata("预计发布", "2024-01-30")

email.add_widget(project_card)

# 团队状态卡片
team_card = CardWidget()
team_card.set_title("团队状态")
team_card.set_content("开发团队运转正常，所有成员积极参与项目开发。当前正在进行最后的测试和优化工作。")
team_card.set_icon("👥")

team_card.add_metadata("团队规模", "6人")
team_card.add_metadata("开发人员", "4人")
team_card.add_metadata("测试人员", "2人")

email.add_widget(team_card)

email.export_html("project_dashboard.html")
```

--8<-- "assets/temp/card_project_dashboard.html"

## ⚡ Shortcut Methods

The Email class provides the `add_card` shortcut method:

```python
# 基础快捷方法
email.add_card("卡片标题", "卡片内容")

# 带图标的快捷方法
email.add_card("产品介绍", "这是一个优秀的产品", icon="🎯")

# 带元数据的快捷方法
email.add_card(
    title="用户信息",
    content="用户详细信息展示",
    metadata={
        "姓名": "张三",
        "部门": "技术部",
        "职位": "工程师"
    }
)

# 带状态的快捷方法
email.add_card(
    title="系统状态",
    content="系统运行正常",
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
    {"title": "卡片1", "content": "内容1"},
    {"title": "卡片2", "content": "内容2"}
]
for data in cards_data:
    email.add_card(data["title"], data["content"])
```

## 🔗 Related Widgets

- [StatusWidget](status-widget.md) - For displaying simple status information
- [AlertWidget](alert-widget.md) - Can add alert information in cards
- [TextWidget](text-widget.md) - For detailed text content in cards
- [SeparatorWidget](separator-widget.md) - For separating different card groups