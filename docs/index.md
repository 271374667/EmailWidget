# EmailWidget - 强大的邮件组件库

<div align="center">

![EmailWidget Logo](https://via.placeholder.com/400x200/FF69B4/FFFFFF?text=EmailWidget+v1.0.0)

**一个现代化、易用的Python邮件组件库**

[![PyPI version](https://badge.fury.io/py/EmailWidget.svg)](https://badge.fury.io/py/EmailWidget)
[![Python versions](https://img.shields.io/pypi/pyversions/EmailWidget.svg)](https://pypi.org/project/EmailWidget/)
[![License](https://img.shields.io/github/license/271374667/SpiderDaily.svg)](https://github.com/271374667/SpiderDaily/blob/master/LICENSE)
[![Codecov](https://codecov.io/gh/username/EmailWidget/branch/main/graph/badge.svg)](https://codecov.io/gh/username/EmailWidget)

</div>

---

## ✨ 项目概览

!!! tip "为什么选择 EmailWidget？"
    
    EmailWidget 是专为Python开发者设计的邮件组件库，让你轻松创建美观、专业的HTML邮件报告而不需要掌握任何额外的前端知识。

### "🎨 丰富组件"

12个专业组件，满足各种邮件报告需求：

- 📝 **TextWidget** - 8种文本样式，自动章节编号
- 📊 **TableWidget** - DataFrame集成，状态单元格  
- 📈 **ChartWidget** - matplotlib/seaborn原生支持
- 📊 **ProgressWidget** - 5种主题，动态进度显示
- ⭕ **CircularProgressWidget** - 圆形进度条，多种尺寸
- 🎴 **CardWidget** - 信息卡片，图标和元数据支持
- ⚠️ **AlertWidget** - 5种警告类型，自定义图标
- 🖼️ **ImageWidget** - 多源支持，尺寸控制
- 💬 **QuoteWidget** - 引用样式，作者信息
- 📊 **StatusWidget** - 状态管理，布局控制
- 📑 **ColumnWidget** - 响应式多列布局
- 📋 **LogWidget** - 日志级别，语法高亮

### "🚀 快速开始"

**30秒创建专业报告**：

```python
from email_widget import Email, TextWidget, ProgressWidget
from email_widget.core.enums import TextType, ProgressTheme

# 创建邮件
email = Email("📊 业务报告")

# 添加标题
email.add_widget(
    TextWidget()
    .set_content("季度业绩总结")
    .set_type(TextType.TITLE_LARGE)
)

# 添加进度指标
email.add_widget(
    ProgressWidget()
    .set_value(92)
    .set_label("目标完成率")
    .set_theme(ProgressTheme.SUCCESS)
)

# 导出HTML
email.export_html("report.html")
```

--8<-- "assets/index_html/demo1.html"


## 🏃‍♂️ 快速开始

### 📦 安装

```bash
pip install email-widget
# 或者安装完整版(包含pandas)
pip install email-widget[pandas]
```

### 🎯 第一个邮件报告

EmailWidget 兼容 pandas 的表格和 matplotlib/seaborn 的图表，并且会自动对其进行美化

```python
from email_widget import Email
from email_widget.widgets import TextWidget, TableWidget, ChartWidget, AlertWidget
from email_widget.core.enums import TextType, AlertType
import matplotlib.pyplot as plt
import pandas as pd

# 创建邮件对象
email = Email("📈 数据分析日报")
email.set_subtitle("2024年第一季度数据汇总")
email.set_footer("本报告由数据团队自动生成")

# 1. 添加标题
email.add_widget(
    TextWidget()
    .set_content("销售业绩概览")
    .set_type(TextType.TITLE_LARGE)
)

# 2. 添加数据表格
df = pd.DataFrame({
    '产品': ['iPhone', 'iPad', 'MacBook'],
    '销量': [1200, 800, 600],
    '收入': [120000, 64000, 120000]
})

table = TableWidget().set_title("产品销售统计")
table.set_dataframe(df)
email.add_widget(table)

# 3. 添加图表
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df['产品'], df['销量'])
ax.set_title('产品销量对比')
ax.set_ylabel('销量')

email.add_widget(
    ChartWidget()
    .set_chart(plt)
    .set_title("📊 销量趋势分析")
    .set_description("显示各产品线的销量对比情况")
)

# 4. 添加重要提醒
email.add_widget(
    AlertWidget()
    .set_content("下月将推出新产品，请提前做好市场准备。")
    .set_alert_type(AlertType.IMPORTANT)
    .set_title("重要通知")
)

# 5. 导出HTML文件
file_path = email.export_html("daily_report.html")
print(f"📧 报告已生成: {file_path}")
```

--8<-- "assets/index_html/demo2.html"

## 🎪 使用场景

<div style="margin: 40px 0; padding: 30px;">
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; margin-top: 30px;">

    <!-- 数据分析报告 -->
    <div style="background: white; border-radius: 15px; padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); transition: transform 0.3s ease, box-shadow 0.3s ease; position: relative; overflow: hidden; border: 1px solid #f0f0f0;">
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, #FF6B6B, #4ECDC4);"></div>
      <div style="display: flex; align-items: center; margin-bottom: 15px;">
        <div style="width: 50px; height: 50px; background: linear-gradient(135deg, #FF6B6B, #FF8E8E); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-right: 15px; box-shadow: 0 5px 15px rgba(255,107,107,0.3);">
          <span style="font-size: 24px;">📊</span>
        </div>
        <h3 style="margin: 0; color: #2C3E50; font-size: 1.4em; font-weight: 700;">数据分析报告</h3>
      </div>
      <p style="color: #666; line-height: 1.6; margin-bottom: 15px; font-size: 0.95em;">为数据分析师创建专业的数据可视化邮件报告</p>
      <div style="margin-bottom: 15px;">
        <span style="background: #E8F4FD; color: #2980B9; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; margin-right: 8px; display: inline-block; margin-bottom: 5px;">业务分析</span>
        <span style="background: #E8F4FD; color: #2980B9; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; margin-right: 8px; display: inline-block; margin-bottom: 5px;">KPI监控</span>
        <span style="background: #E8F4FD; color: #2980B9; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 5px;">趋势分析</span>
      </div>
      <div style="border-top: 1px solid #F0F0F0; padding-top: 15px;">
        <p style="margin: 0; color: #888; font-size: 0.9em;"><strong>核心组件:</strong> ChartWidget、TableWidget、ProgressWidget</p>
      </div>
    </div>
    
    <!-- 系统监控报告 -->
    <div style="background: white; border-radius: 15px; padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); transition: transform 0.3s ease, box-shadow 0.3s ease; position: relative; overflow: hidden; border: 1px solid #f0f0f0;">
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, #4ECDC4, #44A08D);"></div>
      <div style="display: flex; align-items: center; margin-bottom: 15px;">
        <div style="width: 50px; height: 50px; background: linear-gradient(135deg, #4ECDC4, #5FDDD5); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-right: 15px; box-shadow: 0 5px 15px rgba(78,205,196,0.3);">
          <span style="font-size: 24px;">🖥️</span>
        </div>
        <h3 style="margin: 0; color: #2C3E50; font-size: 1.4em; font-weight: 700;">系统监控报告</h3>
      </div>
      <p style="color: #666; line-height: 1.6; margin-bottom: 15px; font-size: 0.95em;">服务器状态、性能指标等系统运维监控邮件</p>
      <div style="margin-bottom: 15px;">
        <span style="background: #E8F8F5; color: #27AE60; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; margin-right: 8px; display: inline-block; margin-bottom: 5px;">系统运维</span>
        <span style="background: #E8F8F5; color: #27AE60; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; margin-right: 8px; display: inline-block; margin-bottom: 5px;">服务监控</span>
        <span style="background: #E8F8F5; color: #27AE60; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 5px;">告警通知</span>
      </div>
      <div style="border-top: 1px solid #F0F0F0; padding-top: 15px;">
        <p style="margin: 0; color: #888; font-size: 0.9em;"><strong>核心组件:</strong> StatusWidget、AlertWidget、LogWidget</p>
      </div>
    </div>
    
    <!-- 爬虫任务报告 -->
    <div style="background: white; border-radius: 15px; padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); transition: transform 0.3s ease, box-shadow 0.3s ease; position: relative; overflow: hidden; border: 1px solid #f0f0f0;">
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, #A8E6CF, #7FCDCD);"></div>
      <div style="display: flex; align-items: center; margin-bottom: 15px;">
        <div style="width: 50px; height: 50px; background: linear-gradient(135deg, #A8E6CF, #B8F2E6); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-right: 15px; box-shadow: 0 5px 15px rgba(168,230,207,0.3);">
          <span style="font-size: 24px;">🕷️</span>
        </div>
        <h3 style="margin: 0; color: #2C3E50; font-size: 1.4em; font-weight: 700;">爬虫任务报告</h3>
      </div>
      <p style="color: #666; line-height: 1.6; margin-bottom: 15px; font-size: 0.95em;">爬虫任务执行情况、数据采集统计邮件报告</p>
      <div style="margin-bottom: 15px;">
        <span style="background: #F0F9F0; color: #16A085; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; margin-right: 8px; display: inline-block; margin-bottom: 5px;">数据采集</span>
        <span style="background: #F0F9F0; color: #16A085; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; margin-right: 8px; display: inline-block; margin-bottom: 5px;">任务监控</span>
        <span style="background: #F0F9F0; color: #16A085; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 5px;">质量报告</span>
      </div>
      <div style="border-top: 1px solid #F0F0F0; padding-top: 15px;">
        <p style="margin: 0; color: #888; font-size: 0.9em;"><strong>核心组件:</strong> ProgressWidget、TableWidget、LogWidget</p>
      </div>
    </div>
    
    <!-- 定期业务通讯 -->
    <div style="background: white; border-radius: 15px; padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); transition: transform 0.3s ease, box-shadow 0.3s ease; position: relative; overflow: hidden; border: 1px solid #f0f0f0;">
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, #FFB6C1, #FFA07A);"></div>
      <div style="display: flex; align-items: center; margin-bottom: 15px;">
        <div style="width: 50px; height: 50px; background: linear-gradient(135deg, #FFB6C1, #FFC1CC); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-right: 15px; box-shadow: 0 5px 15px rgba(255,182,193,0.3);">
          <span style="font-size: 24px;">📧</span>
        </div>
        <h3 style="margin: 0; color: #2C3E50; font-size: 1.4em; font-weight: 700;">定期业务通讯</h3>
      </div>
      <p style="color: #666; line-height: 1.6; margin-bottom: 15px; font-size: 0.95em;">团队周报、项目进展、业务总结等定期邮件</p>
      <div style="margin-bottom: 15px;">
        <span style="background: #FFF0F5; color: #E74C3C; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; margin-right: 8px; display: inline-block; margin-bottom: 5px;">项目管理</span>
        <span style="background: #FFF0F5; color: #E74C3C; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; margin-right: 8px; display: inline-block; margin-bottom: 5px;">团队沟通</span>
        <span style="background: #FFF0F5; color: #E74C3C; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 5px;">业务汇报</span>
      </div>
      <div style="border-top: 1px solid #F0F0F0; padding-top: 15px;">
        <p style="margin: 0; color: #888; font-size: 0.9em;"><strong>核心组件:</strong> TextWidget、CardWidget、QuoteWidget</p>
      </div>
    </div>

  </div>
</div>

<style>
  /* 悬停效果 */
  div[style*="background: white"]:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.15) !important;
  }
  /* 响应式布局 */
  @media (max-width: 768px) {
    div[style*="display: grid"] {
      grid-template-columns: 1fr !important;
    }
  }
</style>

## 🎨 组件画廊

### 基础组件

=== "文本组件"
    
    ```python
    # 8种预设样式
    email.add_widget(
        TextWidget()
        .set_content("大标题")
        .set_type(TextType.TITLE_LARGE)
    )
    
    email.add_widget(
        TextWidget()
        .set_content("章节标题")
        .set_type(TextType.SECTION_H2)
    )
    
    email.add_widget(
        TextWidget()
        .set_content("正文内容，支持多行文本和自动格式化。")
        .set_type(TextType.BODY)
    )
    ```
    
    <center>![image-20250702112724320](./index.assets/image-20250702112724320.png)</center>

=== "表格组件"

    ```python
    # DataFrame直接导入
    table = TableWidget().set_title("销售数据")
    table.set_dataframe(df)
    
    # 手动添加行
    table = TableWidget()
    table.set_headers(["产品", "销量", "状态"])
    table.add_row(["iPhone", "1000", "success"])
    table.add_row(["iPad", "800", "warning"])
    
    email.add_widget(table)
    ```

    <center>![image-20250702113233960](./index.assets/image-20250702113233960.png)</center>

=== "图表组件"

    ```python
    # matplotlib图表
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
    ax.set_title("趋势图")
    
    email.add_widget(
        ChartWidget()
        .set_chart(plt)
        .set_title("数据趋势")
        .set_description("显示业务指标变化趋势")
    )
    ```
    
    <center>![image-20250702113423501](./index.assets/image-20250702113423501.png)</center>

### 高级组件

=== "进度组件"
    
    ```python
    # 线性进度条
    email.add_widget(
        ProgressWidget()
        .set_value(75)
        .set_label("项目进度")
        .set_theme(ProgressTheme.PRIMARY)
    )
    
    # 圆形进度条
    email.add_widget(
        CircularProgressWidget()
        .set_value(85)
        .set_label("完成率")
    )
    ```
    
    <center>![image-20250702113553794](./index.assets/image-20250702113553794.png)</center>

=== "状态组件"
    
    ```python
    # 状态卡片
    email.add_widget(
        CardWidget()
        .set_title("系统状态")
        .set_content("所有服务正常运行")
        .set_icon("✅")
    )
    
    # 状态列表
    status_items = [
        {"label": "数据库", "status": "success", "value": "连接稳定"},
        {"label": "API", "status": "warning", "value": "响应时间较长"}
    ]
    email.add_status_items(status_items)
    ```
    
    <center>![image-20250702113934973](./index.assets/image-20250702113934973.png)</center>

=== "通知组件"
    
    ```python
    # 警告框
    email.add_widget(
        AlertWidget()
        .set_content("系统维护通知")
        .set_alert_type(AlertType.WARNING)
        .set_title("重要提醒")
    )
    
    # 引用样式
    email.add_widget(
        QuoteWidget()
        .set_content("数据是新时代的石油")
        .set_author("Clive Humby")
        .set_source("数据科学家")
    )
    ```
    
    <center>![image-20250702114027153](./index.assets/image-20250702114027153.png)</center>


## 📖 文档导航

<div class="grid cards" markdown>
- :material-rocket-launch: **[快速开始](getting-started/installation.md)**
- :material-book-open: **[用户指南](user-guide/core-classes.md)**
- :material-api: **[API参考](api/core.md)**
- :material-code-braces: **[示例代码](examples/basic.md)**
- :material-tools: **[开发指南](development/contributing.md)**
</div>


## 🤝 社区与支持

### 获取帮助

- **📚 文档中心**: [完整文档](https://271374667.github.io/SpiderDaily/)
- **🐛 问题反馈**: [GitHub Issues](https://github.com/271374667/SpiderDaily/issues)
- **💬 讨论交流**: [GitHub Discussions](https://github.com/271374667/SpiderDaily/discussions)
- **📧 邮件支持**: 271374667@qq.com

### 参与贡献

```bash
# 1. 克隆项目
git clone https://github.com/271374667/SpiderDaily.git

# 2. 安装开发环境
pip install -e ".[dev]"

# 3. 运行测试
pytest tests/

# 4. 提交更改
git commit -m "feat: 添加新功能"
```

### 社交媒体

- **GitHub**: [271374667/SpiderDaily](https://github.com/271374667/SpiderDaily)
- **Bilibili**: [Python调包侠](https://space.bilibili.com/282527875)
- **Email**: 271374667@qq.com

## 📄 许可证

本项目采用 [MIT License](https://github.com/271374667/SpiderDaily/blob/master/LICENSE) 开源协议。

---

<div align="center">
    <p>⭐ **如果这个项目对你有帮助，请给我们一个星标！** ⭐</p>
    <p>Made with ❤️ by <a href="https://github.com/271374667">Python调包侠</a></p>
    <p><a href="https://space.bilibili.com/282527875">📺 观看视频教程</a> • <a href="https://271374667.github.io/SpiderDaily/">📖 查看完整文档</a></p>
</div> 