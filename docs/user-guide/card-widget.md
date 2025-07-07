# CardWidget 卡片组件

<div style="background: #f0f8ff; border: 1px solid #4a90e2; border-radius: 8px; padding: 20px; margin: 20px 0;">
  <h3 style="color: #2c5282; margin-top: 0;">🎴 卡片展示组件</h3>
  <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 12px 0; font-family: 'Segoe UI', Tahoma, Arial, sans-serif; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
    <h3 style="font-size: 18px; font-weight: 600; color: #323130; margin-bottom: 8px;">
      📊 数据统计报告
    </h3>
    <div style="color: #323130; line-height: 1.5; font-size: 14px;">本月系统运行状况良好，各项指标均在正常范围内。用户活跃度较上月提升15%，系统响应时间保持在100ms以内。</div>
    <div style="margin-top: 12px; padding-top: 12px; border-top: 1px solid #e1dfdd;">
      <div style="margin: 4px 0; font-size: 13px;"><strong>报告时间:</strong> 2024-01-15</div>
      <div style="margin: 4px 0; font-size: 13px;"><strong>报告类型:</strong> 月度总结</div>
      <div style="margin: 4px 0; font-size: 13px;"><strong>状态:</strong> 正常</div>
    </div>
  </div>
  <div style="display: flex; gap: 10px; margin-top: 15px;">
    <span style="background: #e8f4fd; color: #0078d4; padding: 4px 8px; border-radius: 4px; font-size: 12px;">内容展示</span>
    <span style="background: #e8f4fd; color: #0078d4; padding: 4px 8px; border-radius: 4px; font-size: 12px;">元数据</span>
    <span style="background: #e8f4fd; color: #0078d4; padding: 4px 8px; border-radius: 4px; font-size: 12px;">状态指示</span>
  </div>
</div>

CardWidget是一个通用的卡片容器组件，用于展示结构化的内容信息。它支持标题、内容、图标和元数据的组合展示，是构建信息面板、产品展示和内容摘要的理想选择。

## 🎯 主要功能

### 内容展示
- **标题支持**：可选的卡片标题
- **内容区域**：主要内容展示区域
- **图标装饰**：支持多种图标类型
- **状态指示**：支持不同状态的视觉反馈

### 元数据管理
- **键值对**：支持添加元数据信息
- **动态管理**：支持动态添加、更新和清除元数据
- **灵活展示**：元数据区域自动布局

### 样式定制
- **阴影效果**：可选的卡片阴影
- **边框圆角**：可自定义圆角大小
- **内边距**：可调整内容间距

## 📋 核心方法

### 基础使用

```python
from email_widget.widgets import CardWidget
from email_widget.core.enums import StatusType, IconType

# 创建卡片组件
card = CardWidget()

# 设置基本信息
card.set_title("产品介绍")
card.set_content("这是一个功能强大的邮件组件库，提供了丰富的UI组件。")
card.set_icon(IconType.INFO)
```

### 内容管理方法

```python
# 设置标题
card.set_title("卡片标题")

# 设置内容
card.set_content("卡片的主要内容信息")

# 设置图标
card.set_icon(IconType.SUCCESS)  # 使用预定义图标
card.set_icon("🎉")              # 使用自定义图标

# 设置状态
card.set_status(StatusType.SUCCESS)
```

### 元数据管理

```python
# 添加单个元数据
card.add_metadata("作者", "张三")
card.add_metadata("创建时间", "2024-01-15")

# 批量设置元数据
metadata = {
    "版本": "v1.0.0",
    "大小": "2.5MB",
    "更新时间": "2024-01-15"
}
card.set_metadata(metadata)

# 清空元数据
card.clear_metadata()
```

## 💡 实用示例

### 产品展示卡片

```python
from email_widget.widgets import CardWidget
from email_widget.core.enums import StatusType, IconType

# 创建产品展示卡片
product_card = CardWidget()
product_card.set_title("EmailWidget Pro")
product_card.set_content("专业的Python邮件组件库，提供丰富的UI组件和强大的邮件渲染能力。支持多种组件类型，完美适配各种邮件客户端。")
product_card.set_icon(IconType.SUCCESS)
product_card.set_status(StatusType.SUCCESS)

# 添加产品信息
product_card.add_metadata("版本", "v2.1.0")
product_card.add_metadata("许可证", "MIT")
product_card.add_metadata("支持Python", "3.8+")
product_card.add_metadata("最后更新", "2024-01-15")

# 渲染卡片
html = product_card.render_html()
```

### 用户信息卡片

```python
# 创建用户信息卡片
user_card = CardWidget()
user_card.set_title("用户档案")
user_card.set_content("高级开发工程师，专注于Python后端开发和数据分析。拥有5年以上的项目经验，熟悉多种开发框架和工具。")
user_card.set_icon("👤")

# 添加用户信息
user_card.add_metadata("姓名", "李四")
user_card.add_metadata("职位", "高级工程师")
user_card.add_metadata("部门", "技术部")
user_card.add_metadata("入职时间", "2019-03-15")
user_card.add_metadata("邮箱", "lisi@example.com")
```

### 项目状态卡片

```python
# 创建项目状态卡片
project_card = CardWidget()
project_card.set_title("项目进展")
project_card.set_content("EmailWidget项目开发进展顺利，目前已完成核心功能开发，正在进行测试和文档编写阶段。")
project_card.set_icon(IconType.INFO)
project_card.set_status(StatusType.SUCCESS)

# 添加项目信息
project_card.add_metadata("项目名称", "EmailWidget")
project_card.add_metadata("项目状态", "开发中")
project_card.add_metadata("完成度", "85%")
project_card.add_metadata("预计完成", "2024-02-01")
project_card.add_metadata("负责人", "王五")
```

### 通知消息卡片

```python
# 创建通知消息卡片
notification_card = CardWidget()
notification_card.set_title("系统通知")
notification_card.set_content("系统将在今晚22:00-24:00进行维护升级，届时可能会影响部分功能的正常使用，请提前做好相关准备。")
notification_card.set_icon("⚠️")
notification_card.set_status(StatusType.WARNING)

# 添加通知信息
notification_card.add_metadata("通知类型", "系统维护")
notification_card.add_metadata("影响范围", "全系统")
notification_card.add_metadata("维护时间", "22:00-24:00")
notification_card.add_metadata("发布时间", "2024-01-15 10:30")
```

### 数据报告卡片

```python
# 创建数据报告卡片
report_card = CardWidget()
report_card.set_title("月度数据报告")
report_card.set_content("本月网站访问量达到新高，用户活跃度显著提升。移动端访问占比持续增长，用户体验优化效果明显。")
report_card.set_icon("📊")
report_card.set_status(StatusType.INFO)

# 添加报告数据
report_card.add_metadata("报告周期", "2024年1月")
report_card.add_metadata("总访问量", "1,234,567")
report_card.add_metadata("活跃用户", "45,678")
report_card.add_metadata("移动端占比", "68%")
report_card.add_metadata("生成时间", "2024-01-15 09:00")
```

## 🎨 图标类型详解

### 预定义图标

| 图标类型 | 显示效果 | 适用场景 |
|---------|----------|----------|
| `IconType.INFO` | ℹ️ | 信息提示、说明 |
| `IconType.SUCCESS` | ✅ | 成功状态、完成 |
| `IconType.WARNING` | ⚠️ | 警告信息、注意 |
| `IconType.ERROR` | ❌ | 错误状态、失败 |
| `IconType.QUESTION` | ❓ | 帮助信息、疑问 |

### 自定义图标

```python
# 使用Emoji图标
card.set_icon("🎉")  # 庆祝
card.set_icon("📈")  # 数据增长
card.set_icon("🔧")  # 工具/设置
card.set_icon("👤")  # 用户
card.set_icon("📊")  # 报告/统计

# 使用Unicode符号
card.set_icon("★")   # 星号
card.set_icon("●")   # 圆点
card.set_icon("▲")   # 三角形
```

## 📊 状态类型说明

### 状态视觉效果

| 状态类型 | 视觉效果 | 适用场景 |
|---------|----------|----------|
| `SUCCESS` | 成功色调 | 完成状态、正常运行 |
| `WARNING` | 警告色调 | 需要注意、待处理 |
| `ERROR` | 错误色调 | 异常状态、错误信息 |
| `INFO` | 信息色调 | 一般信息、说明 |
| `PRIMARY` | 主色调 | 重要信息、突出显示 |

## 🎨 最佳实践

### 1. 内容结构化

```python
# 保持内容结构清晰
card = CardWidget()
card.set_title("明确的标题")  # 简洁明了的标题
card.set_content("详细的内容描述...")  # 重要信息在前
card.set_icon(IconType.INFO)  # 合适的图标

# 元数据按重要性排序
card.add_metadata("关键信息", "重要数据")
card.add_metadata("补充信息", "额外数据")
```

### 2. 状态和图标搭配

```python
# 状态和图标保持一致
success_card = CardWidget()
success_card.set_status(StatusType.SUCCESS)
success_card.set_icon(IconType.SUCCESS)

warning_card = CardWidget()
warning_card.set_status(StatusType.WARNING)
warning_card.set_icon(IconType.WARNING)
```

### 3. 元数据管理

```python
# 批量设置元数据
metadata = {
    "创建时间": "2024-01-15",
    "更新时间": "2024-01-15",
    "作者": "张三",
    "版本": "v1.0.0"
}
card.set_metadata(metadata)

# 动态更新元数据
def update_card_metadata(card, new_data):
    for key, value in new_data.items():
        card.add_metadata(key, value)
```

### 4. 组合使用

```python
# 多卡片组合展示
from email_widget.widgets import ColumnWidget

# 创建卡片组合
column = ColumnWidget().set_columns(2)

# 创建多个相关卡片
cards = []
for i in range(4):
    card = CardWidget()
    card.set_title(f"卡片 {i+1}")
    card.set_content(f"这是第{i+1}个卡片的内容")
    card.set_icon(IconType.INFO)
    cards.append(card)

# 组合显示
column.add_widgets(cards)
```

### 5. 响应式设计

```python
# 根据内容长度调整卡片
def create_adaptive_card(title, content, metadata=None):
    card = CardWidget()
    card.set_title(title)
    card.set_content(content)
    
    # 根据内容长度选择图标
    if len(content) > 100:
        card.set_icon("📄")  # 长文档
    else:
        card.set_icon(IconType.INFO)  # 简短信息
    
    if metadata:
        card.set_metadata(metadata)
    
    return card
```

## 🔧 常见问题

### Q: 如何控制卡片的宽度？
A: 卡片宽度由容器控制，可以通过外层布局组件（如ColumnWidget）来管理。

### Q: 元数据区域可以自定义样式吗？
A: 元数据区域使用统一的样式，如需自定义可以通过CSS覆盖。

### Q: 卡片内容支持HTML吗？
A: 支持基本的HTML标签，但建议使用纯文本以确保邮件客户端兼容性。

### Q: 如何实现卡片的点击效果？
A: 在邮件环境中，可以通过包装链接标签来实现点击跳转。

CardWidget为您提供了灵活而美观的内容展示方案，无论是产品介绍、用户信息还是数据报告，都能完美呈现！ 