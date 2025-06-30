# EmailWidget - 强大的邮件组件库

<div align="center">

![EmailWidget Logo](https://via.placeholder.com/400x200/FF69B4/FFFFFF?text=EmailWidget)

**一个现代化、易用的Python邮件组件库**

[![PyPI version](https://badge.fury.io/py/EmailWidget.svg)](https://badge.fury.io/py/EmailWidget)
[![Python versions](https://img.shields.io/pypi/pyversions/EmailWidget.svg)](https://pypi.org/project/EmailWidget/)
[![License](https://img.shields.io/github/license/271374667/SpiderDaily.svg)](https://github.com/271374667/SpiderDaily/blob/master/LICENSE)
[![Downloads](https://pepy.tech/badge/EmailWidget)](https://pepy.tech/project/EmailWidget)

</div>

## ✨ 特性亮点

!!! tip "为什么选择 EmailWidget？"
    
    EmailWidget 是专为Python开发者设计的邮件组件库，让你轻松创建美观、专业的HTML邮件报告。

### 🎨 美观的设计

- **现代化UI设计** - 基于Microsoft Fluent Design风格
- **响应式布局** - 完美适配桌面和移动设备
- **丰富的组件** - 文本、表格、图表、卡片等多种组件
- **主题定制** - 支持自定义颜色、字体和样式

### 🚀 简单易用

```python
from email_widget import Email, TextWidget, TableWidget

# 创建邮件
email = Email("每日数据报告")

# 添加标题
email.add_widget(
    TextWidget()
    .set_content("销售数据分析")
    .set_type(TextType.TITLE_LARGE)
)

# 添加表格
table = TableWidget().set_title("销售明细")
table.set_headers(["产品", "销量", "收入"])
table.add_row(["产品A", "100", "¥10,000"])
table.add_row(["产品B", "80", "¥8,000"])
email.add_widget(table)

# 导出HTML
email.export("report.html")
```

### 📊 强大的功能

=== "文本组件"
    
    - 多种预设样式（标题、正文、说明文字）
    - 自动章节编号
    - 丰富的格式选项
    - 多行文本支持

=== "表格组件"
    
    - 支持DataFrame直接导入
    - 状态单元格（成功、警告、错误）
    - 斑马纹和边框样式
    - 自定义列宽和样式

=== "图表组件"
    
    - 原生支持matplotlib/seaborn
    - 自动base64编码嵌入
    - 中文字体自动配置
    - 图表标题和描述

=== "其他组件"
    
    - 进度条和圆形进度条
    - 状态卡片和警告框
    - 日志输出框
    - 引用样式和列布局

## 🎯 使用场景

<div class="grid cards" markdown>

- :material-chart-line: **数据报告**
  
  ---
  
  为数据分析师和业务人员创建专业的数据报告邮件

- :material-monitor-dashboard: **系统监控**
  
  ---
  
  服务器状态、性能指标等系统监控报告

- :material-spider: **爬虫报告**
  
  ---
  
  爬虫任务执行情况、数据采集统计报告

- :material-email-newsletter: **定期通讯**
  
  ---
  
  团队周报、项目进展、业务总结等定期邮件

</div>

## 🏃‍♂️ 快速开始

### 安装

```bash
pip install EmailWidget
```

### 基本使用

```python
from email_widget import Email
from email_widget.widgets import TextWidget, ChartWidget
import matplotlib.pyplot as plt

# 创建邮件
email = Email("我的第一份报告")

# 添加欢迎文本
email.add_widget(
    TextWidget()
    .set_content("欢迎使用 EmailWidget！")
    .set_type(TextType.TITLE_LARGE)
)

# 创建图表
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
ax.set_title("示例图表")

# 添加图表组件
email.add_widget(
    ChartWidget()
    .set_chart(plt)
    .set_title("数据趋势")
    .set_description("这是一个示例图表")
)

# 导出HTML文件
file_path = email.export()
print(f"邮件已生成: {file_path}")
```

## 📖 文档导航

<div class="grid cards" markdown>

- :material-rocket-launch: **[快速开始](getting-started/installation.md)**
  
  ---
  
  安装库并创建你的第一个邮件报告

- :material-book-open: **[用户指南](user-guide/core-classes.md)**
  
  ---
  
  详细了解各个组件的使用方法

- :material-api: **[API参考](api/core.md)**
  
  ---
  
  完整的API文档和参数说明

- :material-code-braces: **[示例代码](examples/basic.md)**
  
  ---
  
  实际使用示例和最佳实践

</div>

## 🤝 社区与支持

- **GitHub**: [271374667/SpiderDaily](https://github.com/271374667/SpiderDaily)
- **问题反馈**: [GitHub Issues](https://github.com/271374667/SpiderDaily/issues)
- **讨论交流**: [GitHub Discussions](https://github.com/271374667/SpiderDaily/discussions)

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](https://github.com/271374667/SpiderDaily/blob/master/LICENSE) 了解详情。

---

<div align="center">
    <p>⭐ 如果这个项目对你有帮助，请给我们一个星标！</p>
    <p>Made with ❤️ by <a href="https://github.com/271374667">Python调包侠</a></p>
</div> 