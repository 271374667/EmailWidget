<div align="center">

<h1>EmailWidget - 强大的邮件组件库</h1>

**🚀 一个现代化、易用的 Python 邮件组件库，让你轻松创建美观的 HTML 邮件报告**

[![PyPI version](https://badge.fury.io/py/EmailWidget.svg)](https://badge.fury.io/py/EmailWidget)
[![Python versions](https://img.shields.io/badge/python-3.10%2B-blue)](https://pypi.org/project/EmailWidget/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Codecov](https://codecov.io/gh/271374667/EmailWidget/branch/master/graph/badge.svg)](https://codecov.io/gh/271374667/EmailWidget)

[📖 文档](https://271374667.github.io/EmailWidget) • [🚀 快速开始](#-快速开始) • [💡 示例](#-组件展示)

</div>

---
## ✨ 特性

- **小巧轻量**: 快速安装，无复杂依赖(小于 1MB)
- **易于使用**: 清晰简单的 API，几行代码就能创建漂亮的邮件模板然后快速发送
- **完整文档**: 项目拥有完整的文档和类型注解，在 IDE 中能获得全面的提示
- **丰富组件**: 目前包含 17 个漂亮的展示组件，所有组件均符合 Fluent 风格，可在下方查看
- **全面测试**: 核心的功能经过完整的测试，确保项目可用
- **完全免费**: 项目使用 MIT 开源协议，您可以随意在任何商业项目中使用


## ✨ 为什么选择 EmailWidget？

> **想发警告或者日志到邮箱，但是不会美化，样式太丑？使用 EmailWidget 来打通发送邮件的最后一步！**

5行代码节省您 30 分钟处理各种邮箱CSS兼容问题，支持PC端，移动端，让曾经痛苦的发送预警邮件变得简单，您可以像搭积木一样完成一个您独一无二的邮件模板，
一行代码就能轻松发送，无重量级依赖，完全开源免费，可商用，安装完小于 2MB，EmailWidget欢迎您随时加入进您的项目

下面的邮箱样式，只需要 **3 行代码** 就能创建，生成出来的内容就能直接当做邮件发送，接受者也能看到美观的邮件

```python
from email_widget import Email

email = Email("欢迎使用EmailWidget")

email.add_card("Python版本", "您需要Python3.10或以上才能使用EmailWidget", metadata={"Python版本": "3.10+"})

email.add_quote("EmailWidget是一个用于构建和发送HTML邮件的Python库。", "EmailWidget")

email.export_html('welcome_email.html')
```

![image-20250706200253564](https://271374667.github.io/picx-images-hosting/EmailWidget/image-20250706200253564.3k8ahgbqia.webp)

### 🎨 丰富的组件 - 17 个直观组件

```python
# 一行代码，多种组件
email.add_widget(TextWidget().set_content("标题").set_type(TextType.TITLE_LARGE))
email.add_widget(TableWidget().set_dataframe(df)) # 支持 pandas 的 Dataframe
email.add_widget(ChartWidget().set_chart(plt)) # 支持 matplotlib/seaborn 的图表
email.add_widget(ProgressWidget().set_value(85).set_theme(ProgressTheme.SUCCESS))

# 直接使用快捷方法添加组件
email.add_progress(value=95, max_value=100)
```

| 🎯 **组件类型**                  | 📝 **功能特色**                  | 🔧 **使用场景**  |
|------------------------------|------------------------------|--------------|
| 📝 **TextWidget**            | 8 种文本样式、自动编号、章节管理            | 标题、正文、说明文字   |
| 📊 **TableWidget**           | DataFrame 集成、状态单元格、彩色标记      | 数据表格、统计报表    |
| 📈 **ChartWidget**           | matplotlib/seaborn 原生支持、自动编码 | 数据可视化、趋势图    |
| 📊 **ProgressWidget**        | 5 种主题、增减操作、百分比显示             | 任务进度、完成率     |
| ⭕ **CircularProgressWidget** | 圆形进度条、多种尺寸、动态更新              | KPI 指标、完成度   |
| 🎴 **CardWidget**            | 信息卡片、图标支持、元数据管理              | 摘要信息、状态展示    |
| ⚠️ **AlertWidget**           | 5 种警告类型、自定义图标、消息提醒           | 通知、警告、提示     |
| 🖼️ **ImageWidget**          | 多源支持、尺寸控制、描述文字               | 图片展示、Logo 显示 |
| 💬 **QuoteWidget**           | 引用样式、作者信息、来源标注               | 引言、评论、摘录     |
| 📊 **StatusWidget**          | 状态项管理、布局控制、动态更新              | 系统状态、服务监控    |
| 📑 **ColumnWidget**          | 自动/手动列、响应式布局、Widget 管理       | 多列布局、内容分组    |
| 📋 **LogWidget**             | 日志级别、语法高亮、过滤功能               | 系统日志、运行记录    |
| 🔘 **ButtonWidget**           | 链接按钮、自定义样式、多种风格            | 操作按钮、跳转链接    |
| 📏 **SeparatorWidget**        | 分隔线、多种样式、可定制颜色             | 内容分割、区域分隔    |
| ✅ **ChecklistWidget**        | 任务清单、状态追踪、进度统计             | 待办事项、检查列表    |
| ⏰ **TimelineWidget**         | 时间线展示、事件管理、状态标记            | 进度跟踪、历史记录    |
| 📊 **MetricWidget**           | 数据指标、趋势分析、多种布局             | KPI 展示、数据监控   |


## 🏃‍♂️ 快速开始

### 📦 安装

#### 基础安装（推荐）
```bash
pip install EmailWidget
```

> 💡 **安装说明**：仅需 jinja2 依赖，轻量快速。如果需要 TableWidget 的 DataFrame 功能，或者 ChartWidget 的 Matplotlib 请自行安装 pandas 或者 matplotlib/seaborn。

### 🎯 30 秒创建第一个报告

```python
from email_widget import Email, TextWidget, ProgressWidget
from email_widget.core.enums import TextType, ProgressTheme

# 1️⃣ 创建邮件对象
email = Email("📊 销售数据日报")

# 2️⃣ 添加标题和页面脚注
email.set_subtitle("2024年第一季度业绩汇总")
email.set_footer("本报告由数据分析团队自动生成")

# 3️⃣ 添加一个大标题
email.add_widget(
    TextWidget().set_content("📈 销售业绩总览").set_type(TextType.TITLE_LARGE)
)

# 4️⃣ 添加进度指标
email.add_widget(
    ProgressWidget()
    .set_value(92)
    .set_label("季度目标完成率")
    .set_theme(ProgressTheme.SUCCESS)
)

# 5️⃣ 添加数据表格(使用便捷方法,直接调用email而不是创建控件然后add_widget)
data = [
    ["iPhone 15", "1,250", "¥1,875,000", "125%"],
    ["MacBook Pro", "580", "¥1,740,000", "116%"],
    ["iPad Air", "920", "¥552,000", "108%"],
]
email.add_table_from_data(
    data=data, headers=["产品", "销量", "收入", "达成率"], title="🏆 产品销售明细"
)

# 6️⃣ 导出HTML文件
file_path = email.export_html("daily_report.html")
# 如果需要直接诶发送邮件也提供导出为 str 的接口(图片会被自动转为base64嵌入html)
# html_str: str = email.export_str()
print(f"🎉 报告已生成: {file_path}")
```

<details>
<summary>🎨 点击查看生成效果</summary>

[![image-20250702215545140](./README.assets/image-20250702215545140.png)](https://271374667.github.io/picx-images-hosting/image-20250702215545140.6wr07lwngk.webp)

</details>

### 快速发送

EmailWidget 内置一个基础的邮件发送功能，可以通过 `EmailSender` 类快速发送邮件，目前支持 **QQ邮箱**, **网易邮箱**

在开始使用之前需要先前往各自的邮箱获取具体的账号以及秘钥，下面是一个简单的发送邮件的例子，通过导入 QQEmailSender 然后直接进行配置账号和秘钥即可

```python
from email_widget import Email, QQEmailSender

email = Email("测试邮件")
email.add_card("测试卡片", "这是一个测试卡片的内容。")
email.add_quote("这里是一个引用文本。", "PythonImporter")
email.add_status_items(
    [{"label": "状态1", "value": "完成"}, {"label": "状态2", "value": "进行中"}],
    title="测试状态",
)
email.add_table_from_data(
    [["列1", "列2"], ["数据1", "数据2"]],
    title="测试表格",
)
QQEmailSender(username="你的邮箱@qq.com", password="秘钥").send(email)
print("邮件发送成功！")
```


## 🔧 组件展示

下面为目前所有可用控件的展示(部分功能可能未能及时更新，如果出现错误或者不一致的情况请以文档为准)

<details>
<summary>🎨 点击查看组件效果预览</summary>

![image-20250702215350732](https://271374667.github.io/picx-images-hosting/EmailWidget/PixPin_2025-07-12_10-02-42.7snhz8im11.webp)

</details>

## 邮箱内实际显示效果

### 电脑网页版

<details>
<summary>🎨 点击查看电脑端报告</summary>

![电脑版](https://271374667.github.io/picx-images-hosting/image-20250704112531428.9o02gn5kp8.webp)

</details>

### 移动端

<details>
<summary>🎨 点击查看手机端报告</summary>

![移动端](https://271374667.github.io/picx-images-hosting/image-20250704112733193.4qrlmsrswe.webp)

</details>

## 🎨 高级特性

### 🎯 **链式调用支持**

```python
# 流畅的API设计
email = (Email("项目进展报告")
         .set_subtitle("第一季度总结")
         .set_footer("Generated by EmailWidget")
         .add_widget(TextWidget().set_content("概览").set_type(TextType.TITLE_LARGE))
         .add_widget(ProgressWidget().set_value(78).set_label("整体进度")))
```

## 📚 学习资源

| 📖 **资源类型**   | 🔗 **链接**                                                                     | 📝 **内容**  |
|---------------|-------------------------------------------------------------------------------|------------|
| 🚀 **快速开始**   | [安装指南](https://271374667.github.io/EmailWidget/getting-started/installation/) | 环境配置、第一个邮件 |
| 📘 **用户手册**   | [组件详解](https://271374667.github.io/EmailWidget/user-guide/core-classes/)      | 17 个组件完整教程 |
| 🔧 **API 文档** | [API 参考](https://271374667.github.io/EmailWidget/api/core/)                   | 完整类和方法文档   |
| 💡 **实战示例**   | [应用案例](https://271374667.github.io/EmailWidget/examples/basic/)               | 真实场景代码     |
| 🛠️ **开发指南**  | [贡献代码](https://271374667.github.io/EmailWidget/development/contributing/)     | 参与项目开发     |

## 🤝 社区与贡献

### 🌟 **参与开源**

```bash
# 克隆项目
git clone https://github.com/271374667/EmailWidget.git

# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest tests/

# 提交代码
git add .
git commit -m "feat: 添加新功能"
```

### 📞 **联系我们**

- **🐛 问题反馈**: [GitHub Issues](https://github.com/271374667/EmailWidget/issues)
- **💬 讨论交流**: [GitHub Discussions](https://github.com/271374667/EmailWidget/discussions)
- **📧 邮件联系**: 271374667@qq.com
- **📺 视频教程**: [Bilibili 频道](https://space.bilibili.com/282527875)

## 📄 许可证

本项目采用 [MIT License](https://opensource.org/licenses/MIT) 开源协议。

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给我们一个 Star！ ⭐**

Made with ❤️ by [Python 调包侠](https://github.com/271374667) | [观看教程](https://space.bilibili.com/282527875) | [查看文档](https://271374667.github.io/EmailWidget/)

</div>
