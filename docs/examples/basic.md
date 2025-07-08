# 基础示例

本页面提供 EmailWidget 的基础使用示例，适合初学者快速上手。

## 快速入门

### 创建第一个邮件报告

这是最简单的示例，展示如何创建一个包含标题和文本的基础邮件：

```python
from email_widget import Email, TextWidget
from email_widget.core.enums import TextType

# 创建邮件对象
email = Email("我的第一个报告")

# 添加主标题
title = TextWidget()
title.set_content("欢迎使用 EmailWidget") \
     .set_type(TextType.TITLE_LARGE) \
     .set_color("#0078d4")

# 添加说明文本
description = TextWidget()
description.set_content("这是一个简单的邮件报告示例，展示基本功能。") \
           .set_type(TextType.BODY)

# 将组件添加到邮件
email.add_widget(title)
email.add_widget(description)

# 导出为HTML文件
email.export_html("my_first_report.html")
print("✅ 邮件报告已生成：my_first_report.html")
```

email.export_html("my_first_report.html")
print("✅ 邮件报告已生成：my_first_report.html")
```

--8<-- "examples/assets/basic_html/basic_example_1.html"

**效果说明：**
- 生成一个包含蓝色大标题和普通正文的HTML邮件
- 使用链式调用方式设置组件属性
- 自动应用邮件客户端兼容的样式

---

## 文本样式展示

### 各种文本类型和样式

```python
from email_widget import Email, TextWidget
from email_widget.core.enums import TextType, TextAlign

# 创建样式展示邮件
email = Email("文本样式展示")

# 展示不同的文本类型
text_samples = [
    ("大标题样式", TextType.TITLE_LARGE, "#2c3e50"),
    ("小标题样式", TextType.TITLE_SMALL, "#34495e"),
    ("二级章节标题", TextType.SECTION_H2, "#3498db"),
    ("三级章节标题", TextType.SECTION_H3, "#9b59b6"),
    ("正文内容", TextType.BODY, "#2c3e50"),
    ("说明文字", TextType.CAPTION, "#7f8c8d"),
]

# 循环创建不同样式的文本
for content, text_type, color in text_samples:
    text = TextWidget()
    text.set_content(content) \
        .set_type(text_type) \
        .set_color(color)
    email.add_widget(text)

# 展示不同的对齐方式
alignments = [
    ("左对齐文本", TextAlign.LEFT),
    ("居中对齐文本", TextAlign.CENTER),
    ("右对齐文本", TextAlign.RIGHT),
]

for content, align in alignments:
    text = TextWidget()
    text.set_content(content) \
        .set_align(align) \
        .set_font_size("16px")
    email.add_widget(text)

email.export_html("text_styles.html")
print("✅ 文本样式展示已生成：text_styles.html")
```

--8<-- "examples/assets/basic_html/basic_example_2.html"

**学习要点：**
- 了解不同 `TextType` 的视觉效果
- 掌握颜色设置和对齐方式
- 学会使用方法链简化代码

---

## 表格展示

### 创建基础数据表格

```python
from email_widget import Email, TableWidget, TextWidget
from email_widget.core.enums import TextType

# 创建包含表格的邮件
email = Email("员工信息表")

# 添加表格标题
email.add_title("部门员工统计", TextType.SECTION_H2)

# 创建表格组件
table = TableWidget()

# 设置表头
table.set_headers(["姓名", "部门", "职位", "工龄"])

# 添加数据行
employees = [
    ["张三", "技术部", "高级工程师", "3年"],
    ["李四", "产品部", "产品经理", "2年"],
    ["王五", "设计部", "UI设计师", "1年"],
    ["赵六", "市场部", "市场专员", "4年"],
]

for employee in employees:
    table.add_row(employee)

# 启用条纹样式，提高可读性
table.set_striped(True)

# 添加到邮件
email.add_widget(table)

# 添加总结
summary = TextWidget()
summary.set_content("共有 4 名员工，平均工龄 2.5 年") \
       .set_type(TextType.CAPTION) \
       .set_color("#666666")
email.add_widget(summary)

email.export_html("employee_table.html")
print("✅ 员工信息表已生成：employee_table.html")
```

--8<-- "examples/assets/basic_html/basic_example_3.html"

**功能特点：**
- 简单的表格数据展示
- 条纹样式提高可读性
- 结合文本组件做总结说明

---

## 进度展示

### 使用进度条展示完成情况

```python
from email_widget import Email, ProgressWidget, TextWidget
from email_widget.core.enums import ProgressTheme, TextType

# 创建进度展示邮件
email = Email("项目进度报告")

# 添加标题
email.add_title("本周项目进度", TextType.TITLE_LARGE)

# 定义项目进度数据
projects = [
    ("网站重构", 85, ProgressTheme.SUCCESS, "即将完成"),
    ("移动端开发", 60, ProgressTheme.INFO, "正常推进"),
    ("数据迁移", 30, ProgressTheme.WARNING, "需要关注"),
    ("测试优化", 15, ProgressTheme.ERROR, "进度滞后"),
]

# 为每个项目创建进度条
for name, value, theme, status in projects:
    # 项目名称
    project_title = TextWidget()
    project_title.set_content(f"📋 {name}") \
                 .set_type(TextType.SECTION_H3)
    email.add_widget(project_title)
    
    # 进度条
    progress = ProgressWidget()
    progress.set_value(value) \
           .set_label(f"完成度: {value}%") \
           .set_theme(theme) \
           .set_show_percentage(True)
    email.add_widget(progress)
    
    # 状态说明
    status_text = TextWidget()
    status_text.set_content(f"状态: {status}") \
               .set_type(TextType.CAPTION) \
               .set_color("#666666")
    email.add_widget(status_text)

email.export_html("project_progress.html")
print("✅ 项目进度报告已生成：project_progress.html")
```

--8<-- "examples/assets/basic_html/basic_example_4.html"

**设计亮点：**
- 使用不同主题色区分进度状态
- 结合文本说明提供更多信息
- 清晰的视觉层次结构

---

## 警告提示

### 多级别提醒信息

```python
from email_widget import Email, AlertWidget, TextWidget
from email_widget.core.enums import AlertType, TextType

# 创建提醒信息邮件
email = Email("系统通知")

# 添加主标题
email.add_title("重要通知", TextType.TITLE_LARGE)

# 定义不同级别的提醒
alerts = [
    ("一般提示", AlertType.NOTE, "系统将在今晚进行例行维护。"),
    ("友情提醒", AlertType.TIP, "建议定期备份重要数据。"),
    ("重要信息", AlertType.IMPORTANT, "新版本功能已上线，请查看更新日志。"),
    ("注意事项", AlertType.WARNING, "检测到异常登录，请及时修改密码。"),
    ("紧急通知", AlertType.CAUTION, "发现安全漏洞，请立即更新系统。"),
]

# 创建不同类型的警告框
for title, alert_type, content in alerts:
    alert = AlertWidget()
    alert.set_content(content) \
         .set_alert_type(alert_type) \
         .set_title(title)
    email.add_widget(alert)

# 添加联系信息
contact = TextWidget()
contact.set_content("如有疑问，请联系技术支持：support@example.com") \
       .set_type(TextType.CAPTION) \
       .set_align(TextAlign.CENTER)
email.add_widget(contact)

email.export_html("system_alerts.html")
print("✅ 系统通知已生成：system_alerts.html")
```

--8<-- "examples/assets/basic_html/basic_example_5.html"

**使用场景：**
- 系统维护通知
- 安全提醒
- 功能更新说明
- 操作注意事项

---

## 图片展示

### 添加图片和图表

```python
from email_widget import Email, ImageWidget, TextWidget
from email_widget.core.enums import TextType

# 创建包含图片的邮件
email = Email("图片展示")

# 添加标题
email.add_title("产品展示", TextType.TITLE_LARGE)

# 添加产品图片
product_image = ImageWidget()
product_image.set_image_url("https://via.placeholder.com/600x300/3498db/ffffff?text=产品图片") \
            .set_title("新产品预览") \
            .set_description("这是我们即将发布的新产品界面截图") \
            .set_max_width("100%")

email.add_widget(product_image)

# 添加说明文字
description = TextWidget()
description.set_content("产品特色：简洁界面、高效性能、用户友好") \
           .set_type(TextType.BODY)
email.add_widget(description)

# 添加图表示例
chart_title = TextWidget()
chart_title.set_content("销售数据图表") \
           .set_type(TextType.SECTION_H2)
email.add_widget(chart_title)

chart_image = ImageWidget()
chart_image.set_image_url("https://via.placeholder.com/500x300/e74c3c/ffffff?text=图表示例") \
          .set_title("月度销售趋势") \
          .set_description("显示最近6个月的销售数据变化趋势") \
          .set_max_width("500px")

email.add_widget(chart_image)

email.export_html("image_showcase.html")
print("✅ 图片展示已生成：image_showcase.html")
```

--8<-- "examples/assets/basic_html/basic_example_6.html"

**注意事项：**
- 使用占位符图片便于测试
- 设置合适的图片尺寸
- 提供图片标题和描述信息

---

## 便捷方法使用

### 使用 Email 类的快速方法

```python
from email_widget import Email
from email_widget.core.enums import TextType, AlertType, ProgressTheme

# 创建邮件并使用便捷方法
email = Email("便捷方法演示")

# 使用便捷方法快速添加内容
email.add_title("快速报告", TextType.TITLE_LARGE) \
     .add_text("这个报告使用便捷方法快速创建") \
     .add_text("演示如何用更少的代码实现更多功能", color="#666666")

# 快速添加进度条
email.add_progress(75, "任务完成度", theme=ProgressTheme.SUCCESS)

# 快速添加提醒
email.add_alert("记得查看详细说明文档", AlertType.TIP, "友情提醒")

# 快速添加表格数据
data = [
    ["功能", "状态"],
    ["文本展示", "✅ 完成"],
    ["表格显示", "✅ 完成"],
    ["图片展示", "🔄 进行中"],
]
email.add_table_from_data(data[1:], headers=data[0], title="功能清单")

# 快速添加卡片
email.add_card(
    title="开发总结",
    content="EmailWidget 提供了丰富的便捷方法，大大简化了代码编写。",
    icon="🎉"
)

email.export_html("convenience_methods.html")
print("✅ 便捷方法演示已生成：convenience_methods.html")
```

--8<-- "examples/assets/basic_html/basic_example_7.html"

**便捷之处：**
- 支持方法链式调用
- 减少创建 Widget 对象的代码
- 提供常用场景的快速方法
- 保持代码简洁易读

---

## 完整示例：个人周报

### 综合使用多种组件

```python
from email_widget import Email, TextWidget, TableWidget, ProgressWidget, AlertWidget
from email_widget.core.enums import TextType, TextAlign, ProgressTheme, AlertType

# 创建个人周报
email = Email("个人工作周报")

# 报告标题和时间
email.add_title("📋 个人工作周报", TextType.TITLE_LARGE)
email.add_text("报告时间：2024年1月15日 - 2024年1月21日", 
               align=TextAlign.CENTER, color="#666666")

# 本周完成工作
email.add_title("✅ 本周完成工作", TextType.SECTION_H2)

completed_tasks = [
    ["任务", "耗时", "完成度"],
    ["需求文档编写", "8小时", "100%"],
    ["原型设计", "12小时", "100%"],
    ["代码开发", "20小时", "100%"],
]

table = TableWidget()
table.set_headers(completed_tasks[0])
for task in completed_tasks[1:]:
    table.add_row(task)
table.set_striped(True)
email.add_widget(table)

# 项目进度
email.add_title("📊 项目进度", TextType.SECTION_H2)

# 主要项目进度条
projects_progress = [
    ("前端开发", 80, ProgressTheme.INFO),
    ("后端开发", 65, ProgressTheme.WARNING),
    ("测试用例", 90, ProgressTheme.SUCCESS),
]

for name, progress, theme in projects_progress:
    email.add_text(f"🔹 {name}")
    email.add_progress(progress, f"{progress}% 完成", theme=theme)

# 下周计划
email.add_title("📅 下周计划", TextType.SECTION_H2)
next_week_plan = """
1. 完成后端API开发
2. 集成测试和调试
3. 性能优化
4. 文档更新
"""
email.add_text(next_week_plan.strip())

# 需要关注的问题
email.add_alert(
    "数据库性能需要优化，建议下周安排专门时间处理",
    AlertType.WARNING,
    "⚠️ 需要关注"
)

# 报告总结
email.add_title("📝 总结", TextType.SECTION_H2)
email.add_text(
    "本周工作进展顺利，主要任务按计划完成。下周将重点关注后端开发和性能优化。",
    color="#2c3e50"
)

email.export_html("weekly_report.html")
print("✅ 个人周报已生成：weekly_report.html")
```

--8<-- "examples/assets/basic_html/basic_example_8.html"

**综合特点：**
- 结构清晰的周报格式
- 多种组件协同工作
- 信息层次分明
- 专业的视觉效果

---

## 学习总结

通过这些基础示例，您已经学会了：

### 🎯 核心概念
- Email 对象作为容器管理所有组件
- Widget 组件的创建和配置
- 方法链式调用的使用方式

### 🛠️ 基本技能
- 文本样式和格式设置
- 表格数据的展示方法
- 进度信息的可视化
- 警告提醒的多级别使用

### 📈 进阶方向
- 学习 [数据报告](data-reports.md) 处理复杂数据
- 探索 [系统监控](system-monitoring.md) 的实时展示
- 研究 [高级示例](advanced.md) 的自定义功能

### 💡 最佳实践
- 保持代码简洁易读
- 合理使用组件组合
- 注意视觉层次和信息结构
- 充分利用便捷方法提高效率

继续学习更多高级功能，探索 EmailWidget 的强大能力！
