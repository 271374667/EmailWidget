# 基础示例

本页面提供 EmailWidget 的核心功能示例，涵盖最常用的使用场景和最佳实践。

## 📚 示例概览

| 示例 | 功能 | 涉及组件 | 难度 |
|------|------|----------|------|
| [快速入门](#quick-start) | 创建第一个邮件报告 | TextWidget, AlertWidget | ⭐ |
| [文本样式](#text-styles) | 各种文本类型和颜色 | TextWidget, SeparatorWidget | ⭐ |
| [数据展示](#data-display) | 表格和进度条 | TableWidget, ProgressWidget | ⭐⭐ |
| [综合应用](#comprehensive) | 完整的监控报告 | 多组件综合 | ⭐⭐⭐ |

---

## 快速入门 {#quick-start}

### 创建第一个邮件报告

这是最简单的示例，展示如何创建一个包含标题、文本和提示的基础邮件：

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

**核心要点：**
- 使用 `Email()` 创建邮件容器
- `add_text()` 快捷方法添加文本
- `add_alert()` 快捷方法添加提示信息
- `export_html()` 导出为HTML文件

---

## 文本样式展示 {#text-styles}

### 各种文本类型和颜色样式

展示 EmailWidget 支持的所有文本类型和颜色设置：

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

**核心要点：**
- 支持多种预定义文本类型（标题、章节、正文、说明）
- 章节标题会自动添加编号
- 支持自定义颜色设置
- 分隔符用于区分不同内容区域

---

## 数据展示 {#data-display}

### 表格和进度条组合

展示如何使用表格和进度条展示项目数据：

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

**核心要点：**
- `TableWidget` 用于结构化数据展示
- `add_progress()` 快捷方法创建进度条
- 不同主题的进度条表示不同状态
- 组合使用多个组件增强信息表达

---

## 综合应用 {#comprehensive}

### 完整的系统监控报告

这个示例展示了如何组合使用多个组件创建一个完整的系统监控报告：

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

**核心要点：**
- 结构化的报告布局，从概览到详细数据
- 不同类型的提醒信息传达不同程度的重要性
- 表格和进度条结合展示量化数据
- 合理使用分隔符组织内容层次

---

## 🚀 快速运行

### 运行环境准备

```bash
# 安装 EmailWidget
pip install EmailWidget

# 或从源码安装
git clone https://github.com/271374667/EmailWidget.git
cd EmailWidget
pip install -e .
```

### 批量运行示例

将以上任意示例代码保存为 `.py` 文件，然后运行：

```bash
python your_example.py
```

生成的HTML文件可以：
- 在浏览器中直接打开预览
- 作为邮件正文发送
- 集成到邮件发送系统中

### 邮件发送集成

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

## 💡 学习建议

### 循序渐进学习路径

1. **入门阶段** - 从快速入门示例开始，掌握基本概念
2. **样式阶段** - 学习文本样式，了解组件属性设置
3. **数据阶段** - 掌握表格和进度条，处理结构化数据
4. **综合阶段** - 组合多个组件，创建完整应用

### 实践建议

- 📝 **动手实践** - 复制代码到本地运行
- 🔄 **修改参数** - 尝试修改颜色、文字、数据
- 🎨 **自定义样式** - 实验不同的组件组合
- 📧 **实际应用** - 将示例应用到实际项目中

### 进阶方向

完成基础示例后，可以探索：
- [数据报告](data-reports.md) - 深入的数据可视化
- [系统监控](system-monitoring.md) - 专业的监控报告
- [实际应用](real-world.md) - 复杂的业务场景

---

**下一步：** 尝试运行这些示例，然后根据您的需求探索更多功能！