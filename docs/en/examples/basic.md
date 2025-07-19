# Basic Examples

This page provides core functionality examples of EmailWidget, covering the most common use cases and best practices.

## 📚 Example Overview

| Example | Function | Components Involved | Difficulty |
|---------|----------|-------------------|------------|
| [Quick Start](#quick-start) | Create your first email report | TextWidget, AlertWidget | ⭐ |
| [Text Styles](#text-styles) | Various text types and colors | TextWidget, SeparatorWidget | ⭐ |
| [Data Display](#data-display) | Tables and progress bars | TableWidget, ProgressWidget | ⭐⭐ |
| [Comprehensive Application](#comprehensive) | Complete monitoring report | Multiple components | ⭐⭐⭐ |

---

## Quick Start {#quick-start}

### Create Your First Email Report

This is the simplest example, showing how to create a basic email with title, text, and alerts:

```python
from email_widget import Email
from email_widget.core.enums import TextType, AlertType

# 创建邮件对象
email = Email("我的第一个报告")

# 添加主标题
email.add_text("欢迎使用 EmailWidget", TextType.TITLE_LARGE)

# 添加说明文本
email.add_text("这是一个简单的邮件报告示例，展示基本功能。", TextType.BODY)

# 添加重要提示
email.add_alert("EmailWidget 让创建美观的HTML邮件变得简单快捷！", AlertType.TIP)

# 导出为HTML文件
email.export_html("my_first_report.html")
print("✅ 邮件报告已生成：my_first_report.html")
```

--8<-- "examples/assets/basic_html/example_1_quick_start_fixed.html"

**Key Points:**
- Use `Email()` to create email container
- `add_text()` shortcut method to add text
- `add_alert()` shortcut method to add alert messages
- `export_html()` to export as HTML file

---

## Text Style Display {#text-styles}

### Various Text Types and Color Styles

Demonstrates all text types and color settings supported by EmailWidget:

```python
from email_widget import Email
from email_widget.widgets.text_widget import TextWidget
from email_widget.core.enums import TextType

email = Email("文本样式展示")

# 展示不同的文本类型
email.add_text("文本类型展示", TextType.TITLE_LARGE)

email.add_text("这是大标题", TextType.TITLE_LARGE)
email.add_text("这是小标题", TextType.TITLE_SMALL)
email.add_text("这是二级章节标题", TextType.SECTION_H2)
email.add_text("这是三级章节标题", TextType.SECTION_H3)
email.add_text("这是正文内容，用于段落描述和详细说明。", TextType.BODY)
email.add_text("这是说明文字，通常用于补充信息。", TextType.CAPTION)

# 分隔线
email.add_separator()

# 带颜色的文本
email.add_text("颜色样式展示", TextType.TITLE_SMALL)

blue_text = (TextWidget()
            .set_content("这是蓝色的重要文本")
            .set_type(TextType.BODY)
            .set_color("#0078d4"))
email.add_widget(blue_text)

green_text = (TextWidget()
             .set_content("这是绿色的成功文本")
             .set_type(TextType.BODY)
             .set_color("#107c10"))
email.add_widget(green_text)

red_text = (TextWidget()
           .set_content("这是红色的警告文本")
           .set_type(TextType.BODY)
           .set_color("#d13438"))
email.add_widget(red_text)

email.export_html("text_styles.html")
```

--8<-- "examples/assets/basic_html/example_2_text_styles_fixed.html"

**Key Points:**
- Supports multiple predefined text types (titles, sections, body, caption)
- Section headers automatically add numbering
- Supports custom color settings
- Separators used to distinguish different content areas

---

## Data Display {#data-display}

### Table and Progress Bar Combination

Shows how to use tables and progress bars to display project data:

```python
from email_widget import Email
from email_widget.widgets.table_widget import TableWidget
from email_widget.core.enums import TextType, ProgressTheme

email = Email("数据展示示例")

# 标题
email.add_text("项目进度报告", TextType.TITLE_LARGE)

# 项目概况
email.add_text("项目概况", TextType.SECTION_H2)
email.add_text("以下是本月各项目的进展情况：", TextType.BODY)

# 创建数据表格
table = TableWidget()
table.set_headers(["项目名称", "负责人", "进度", "状态"])

# 添加数据行
table_data = [
    ["网站重构", "张三", "85%", "进行中"],
    ["移动应用", "李四", "60%", "进行中"],
    ["数据分析", "王五", "100%", "已完成"],
    ["系统优化", "赵六", "30%", "刚开始"]
]

for row in table_data:
    table.add_row(row)

email.add_widget(table)

# 分隔线
email.add_separator()

# 整体进度
email.add_text("整体进度", TextType.SECTION_H2)

# 进度条展示
email.add_progress(68.7, label="项目总体完成度", theme=ProgressTheme.PRIMARY)
email.add_progress(85, label="网站重构", theme=ProgressTheme.SUCCESS)
email.add_progress(60, label="移动应用", theme=ProgressTheme.PRIMARY)
email.add_progress(30, label="系统优化", theme=ProgressTheme.PRIMARY)

# 结论
email.add_text("总结", TextType.SECTION_H2)
email.add_text("本月整体进度良好，网站重构项目即将完成，需要重点关注系统优化项目的进展。", TextType.BODY)

email.export_html("data_display.html")
```

--8<-- "examples/assets/basic_html/example_3_data_display_fixed.html"

**Key Points:**
- `TableWidget` for structured data display
- `add_progress()` shortcut method to create progress bars
- Different progress bar themes represent different statuses
- Combining multiple components enhances information expression

---

## Comprehensive Application {#comprehensive}

### Complete System Monitoring Report

This example shows how to combine multiple components to create a complete system monitoring report:

```python
from email_widget import Email
from email_widget.widgets.table_widget import TableWidget
from email_widget.core.enums import TextType, AlertType, ProgressTheme

email = Email("系统监控周报")

# 报告标题
email.add_text("系统监控周报", TextType.TITLE_LARGE)
email.add_text("监控时间：2024年7月8日 - 2024年7月14日", TextType.CAPTION)

# 系统状态概览
email.add_text("系统状态概览", TextType.SECTION_H2)

# 正常服务
email.add_alert("Web服务运行正常，响应时间稳定", AlertType.TIP)
email.add_alert("数据库连接良好，查询性能优秀", AlertType.TIP)

# 警告信息
email.add_alert("缓存服务偶有延迟，建议关注", AlertType.WARNING)

# 分隔线
email.add_separator()

# 性能指标
email.add_text("关键性能指标", TextType.SECTION_H2)

# 性能表格
perf_table = TableWidget()
perf_table.set_headers(["指标", "当前值", "目标值", "状态"])

perf_data = [
    ["CPU使用率", "65%", "< 80%", "正常"],
    ["内存使用率", "72%", "< 85%", "正常"],
    ["磁盘使用率", "45%", "< 90%", "正常"],
    ["响应时间", "120ms", "< 200ms", "优秀"]
]

for row in perf_data:
    perf_table.add_row(row)

email.add_widget(perf_table)

# 性能进度条
email.add_text("资源使用情况", TextType.SECTION_H3)
email.add_progress(65, label="CPU使用率", theme=ProgressTheme.SUCCESS)
email.add_progress(72, label="内存使用率", theme=ProgressTheme.SUCCESS)
email.add_progress(45, label="磁盘使用率", theme=ProgressTheme.SUCCESS)

# 分隔线
email.add_separator()

# 总结和建议
email.add_text("总结与建议", TextType.SECTION_H2)
email.add_text("本周系统运行稳定，各项指标均在正常范围内。建议：", TextType.BODY)

# 建议列表
email.add_text("1. 继续监控缓存服务性能", TextType.BODY)
email.add_text("2. 优化数据库查询，进一步提升响应速度", TextType.BODY)
email.add_text("3. 定期清理日志文件，保持磁盘空间充足", TextType.BODY)

# 重要提醒
email.add_alert("下周计划进行系统维护，请提前做好准备！", AlertType.IMPORTANT)

email.export_html("system_monitoring.html")
```

--8<-- "examples/assets/basic_html/example_4_comprehensive_fixed.html"

**Key Points:**
- Structured report layout from overview to detailed data
- Different types of alert messages convey different levels of importance
- Tables and progress bars combined to display quantitative data
- Proper use of separators to organize content hierarchy

---

## 🚀 Quick Run

### Environment Setup

```bash
# Install EmailWidget
pip install EmailWidget

# Or install from source
git clone https://github.com/271374667/EmailWidget.git
cd EmailWidget
pip install -e .
```

### Batch Run Examples

Save any of the above example code as a `.py` file, then run:

```bash
python your_example.py
```

Generated HTML files can be:
- Opened directly in browsers for preview
- Sent as email content
- Integrated into email sending systems

### Email Sending Integration

```python
from email_widget import Email, QQEmailSender

# 创建邮件内容
email = Email("监控报告")
email.add_text("系统运行正常", TextType.TITLE_LARGE)

# 获取HTML内容
html_content = email.export_str()

# 发送邮件（需要配置SMTP）
sender = QQEmailSender(
    email_address="your_email@qq.com",
    password="your_password"  # 使用应用密码
)

sender.send_email(
    to_emails=["recipient@example.com"],
    subject="系统监控报告",
    html_body=html_content
)
```

## 💡 Learning Suggestions

### Progressive Learning Path

1. **Beginner Stage** - Start with quick start example, master basic concepts
2. **Style Stage** - Learn text styles, understand component property settings
3. **Data Stage** - Master tables and progress bars, handle structured data
4. **Comprehensive Stage** - Combine multiple components, create complete applications

### Practice Recommendations

- 📝 **Hands-on Practice** - Copy code to run locally
- 🔄 **Modify Parameters** - Try changing colors, text, data
- 🎨 **Custom Styles** - Experiment with different component combinations
- 📧 **Real Applications** - Apply examples to actual projects

### Advanced Directions

After completing basic examples, you can explore:
- [Data Reports](data-reports.md) - In-depth data visualization
- [System Monitoring](system-monitoring.md) - Professional monitoring reports
- [Real-world Applications](real-world.md) - Complex business scenarios

---

**Next Step:** Try running these examples, then explore more features based on your needs!