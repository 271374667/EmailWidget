# CardWidget 卡片组件

CardWidget 是一个通用的卡片容器组件，用于展示结构化的内容信息。它支持标题、内容、图标和元数据的组合展示，是构建信息面板、产品展示和内容摘要的理想选择。

## 🎯 组件预览

--8<-- "assets/card_widget_component_preview.html"

## ✨ 核心特性

- **📋 内容展示**: 支持标题、内容、图标的组合展示
- **🏷️ 元数据管理**: 支持键值对形式的元数据信息展示
- **🎨 样式定制**: 可选的卡片阴影、边框圆角、内边距调整
- **📱 状态指示**: 支持不同状态的视觉反馈和状态显示
- **📧 邮件兼容**: 使用邮件客户端兼容的HTML和CSS实现

## 🚀 快速开始

### 基础用法

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

### 进阶用法

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

📚 **完整API文档**: [CardWidget API](../api/card-widget.md)

## 🎨 样式指南

### 状态类型和颜色

- **SUCCESS**: 绿色 (#107c10) - 成功状态、正常运行、完成状态
- **WARNING**: 橙色 (#ff8c00) - 警告状态、需要注意、待处理
- **ERROR**: 红色 (#d13438) - 错误状态、失败状态、异常情况
- **INFO**: 蓝色 (#0078d4) - 信息状态、常规信息、提示信息
- **PRIMARY**: 蓝色 (#0078d4) - 主要内容、重要信息、核心功能

### 图标使用建议

- **IconType.INFO**: 📄 用于信息展示、文档说明
- **IconType.SUCCESS**: ✅ 用于成功状态、完成任务
- **IconType.WARNING**: ⚠️ 用于警告信息、注意事项
- **IconType.ERROR**: ❌ 用于错误信息、失败状态
- **自定义图标**: 🎯 📊 🚀 等，根据内容选择合适的图标

## 📱 最佳实践

### 1. 产品展示卡片

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

### 2. 用户信息面板

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

### 3. 项目状态仪表板

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

## ⚡ 快捷方法

Email 类提供了 `add_card` 快捷方法：

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

## 🐛 常见问题

### Q: 卡片内容过长时如何处理？
A: CardWidget 会自动处理长内容的换行和布局。建议将过长的内容拆分为多个卡片或使用元数据来组织信息。

### Q: 如何自定义卡片的样式？
A: 可以通过设置不同的StatusType来改变卡片的主题色。如需更多自定义，可以通过CSS覆盖的方式实现。

### Q: 元数据信息显示不全怎么办？
A: 检查元数据的键值是否过长，建议使用简短的键名和适当的值长度。如果信息较多，可以分成多个卡片展示。

### Q: 卡片在某些邮件客户端中显示异常？
A: CardWidget 采用了邮件客户端兼容的布局方式。如遇问题，可以尝试简化卡片内容或使用其他组件替代。

### Q: 如何批量管理多个卡片？
A: 可以将卡片信息组织成列表，然后使用循环批量创建：
```python
cards_data = [
    {"title": "卡片1", "content": "内容1"},
    {"title": "卡片2", "content": "内容2"}
]
for data in cards_data:
    email.add_card(data["title"], data["content"])
```

## 🔗 相关组件

- [StatusWidget](status-widget.md) - 用于显示简单的状态信息
- [AlertWidget](alert-widget.md) - 可以在卡片中添加警告信息
- [TextWidget](text-widget.md) - 用于卡片中的详细文本内容
- [SeparatorWidget](separator-widget.md) - 用于分隔不同的卡片组