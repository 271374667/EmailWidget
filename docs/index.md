# EmailWidget - 强大的邮件组件库

## ✨ 特性

- **小巧轻量**: 快速安装，无复杂依赖(小于 1MB)
- **易于使用**: 清晰简单的 API，几行代码就能创建漂亮的邮件模板然后快速发送
- **完整文档**: 项目拥有完整的文档和类型注解，在 IDE 中能获得全面的提示
- **丰富组件**: 目前包含 15+ 个漂亮的展示组件，所有组件均符合 Fluent 风格，可在下方查看
- **全面测试**: 核心的功能经过完整的测试，确保项目可用
- **完全免费**: 项目使用 MIT 开源协议，您可以随意在任何商业项目中使用

## ✨ 为什么选择 EmailWidget？

> **想发警告或者日志到邮箱，但是不会美化，样式太丑？使用 EmailWidget 来打通发送邮件的最后一步！**

想要一个漂亮的邮件模版，但是不会 HTML/CSS 或者干脆懒得写？网上的模版删删改改复用困难而且不支持移动端？那么欢迎来试试 EmailWidget，可复用，响应式，完整的类型提示，全面的文档，轻量级的邮箱组件库，祝您快速搭建自己的报告模版

EmailWidget 是专为 Python 开发者设计的邮件组件库，让你用几行代码就能创建出美观的 HTML 邮件报告而不需要了解 HTML 和邮箱的 CSS 的细节。项目经过 **1000+个测试用例** 验证，**核心代码 100% 测试覆盖**, 确保稳定可靠。

下面的邮箱样式，只需要 **3 行代码** 就能创建，生成出来的内容就能直接当做邮件发送，接受者也能看到美观的邮件

```python
from email_widget import Email

email = Email("欢迎使用EmailWidget")

email.add_card("Python版本", "您需要Python3.10或以上才能使用EmailWidget", metadata={"Python版本": "3.10+"})

email.add_quote("EmailWidget是一个用于构建和发送HTML邮件的Python库。", "EmailWidget")

email.export_html('welcome_email.html')
```

![image-20250706200253564](https://271374667.github.io/picx-images-hosting/EmailWidget/image-20250706200253564.3k8ahgbqia.webp)

## "🚀 快速开始"

### 📦 安装

```bash
pip install EmailWidget
```

### 30秒创建专业报告

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


## 🎪 使用场景

<div class="email-preview-wrapper">
<div style="margin: 40px 0; padding: 30px;">
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; margin-top: 30px;">

    <!-- Data Analysis Reports -->
    <div style="background: white; border-radius: 15px; padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); transition: transform 0.3s ease, box-shadow 0.3s ease; position: relative; overflow: hidden; border: 1px solid #f0f0f0;">
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, #FF6B6B, #4ECDC4);"></div>
      <div style="display: flex; align-items: center; margin-bottom: 15px;">
        <div style="width: 50px; height: 50px; background: linear-gradient(135deg, #FF6B6B, #FF8E8E); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-right: 15px; box-shadow: 0 5px 15px rgba(255,107,107,0.3);">
          <span style="font-size: 24px;">📊</span>
        </div>
        <h3 style="margin: 0; color: #2C3E50; font-size: 1.4em; font-weight: 700;">Data Analysis Reports</h3>
      </div>
      <p style="color: #666; line-height: 1.6; margin-bottom: 15px; font-size: 0.95em;">Create professional data visualization email reports for data analysts</p>
      <div style="margin-bottom: 15px;">
        <span style="background: #E8F4FD; color: #2980B9; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; margin-right: 8px; display: inline-block; margin-bottom: 5px;">Business Analysis</span>
        <span style="background: #E8F4FD; color: #2980B9; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; margin-right: 8px; display: inline-block; margin-bottom: 5px;">KPI Monitoring</span>
        <span style="background: #E8F4FD; color: #2980B9; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 5px;">Trend Analysis</span>
      </div>
      <div style="border-top: 1px solid #F0F0F0; padding-top: 15px;">
        <p style="margin: 0; color: #888; font-size: 0.9em;"><strong>Core Components:</strong> ChartWidget, TableWidget, ProgressWidget</p>
      </div>
    </div>
    
    <!-- System Monitoring Reports -->
    <div style="background: white; border-radius: 15px; padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); transition: transform 0.3s ease, box-shadow 0.3s ease; position: relative; overflow: hidden; border: 1px solid #f0f0f0;">
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, #4ECDC4, #44A08D);"></div>
      <div style="display: flex; align-items: center; margin-bottom: 15px;">
        <div style="width: 50px; height: 50px; background: linear-gradient(135deg, #4ECDC4, #5FDDD5); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-right: 15px; box-shadow: 0 5px 15px rgba(78,205,196,0.3);">
          <span style="font-size: 24px;">🖥️</span>
        </div>
        <h3 style="margin: 0; color: #2C3E50; font-size: 1.4em; font-weight: 700;">System Monitoring Reports</h3>
      </div>
      <p style="color: #666; line-height: 1.6; margin-bottom: 15px; font-size: 0.95em;">Server status, performance metrics and system operations monitoring emails</p>
      <div style="margin-bottom: 15px;">
        <span style="background: #E8F8F5; color: #27AE60; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; margin-right: 8px; display: inline-block; margin-bottom: 5px;">System Ops</span>
        <span style="background: #E8F8F5; color: #27AE60; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; margin-right: 8px; display: inline-block; margin-bottom: 5px;">Service Monitor</span>
        <span style="background: #E8F8F5; color: #27AE60; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 5px;">Alert System</span>
      </div>
      <div style="border-top: 1px solid #F0F0F0; padding-top: 15px;">
        <p style="margin: 0; color: #888; font-size: 0.9em;"><strong>Core Components:</strong> StatusWidget, AlertWidget, LogWidget</p>
      </div>
    </div>
    
    <!-- Web Scraping Reports -->
    <div style="background: white; border-radius: 15px; padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); transition: transform 0.3s ease, box-shadow 0.3s ease; position: relative; overflow: hidden; border: 1px solid #f0f0f0;">
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, #A8E6CF, #7FCDCD);"></div>
      <div style="display: flex; align-items: center; margin-bottom: 15px;">
        <div style="width: 50px; height: 50px; background: linear-gradient(135deg, #A8E6CF, #B8F2E6); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-right: 15px; box-shadow: 0 5px 15px rgba(168,230,207,0.3);">
          <span style="font-size: 24px;">🕷️</span>
        </div>
        <h3 style="margin: 0; color: #2C3E50; font-size: 1.4em; font-weight: 700;">Web Scraping Reports</h3>
      </div>
      <p style="color: #666; line-height: 1.6; margin-bottom: 15px; font-size: 0.95em;">Scraping task execution status and data collection statistics email reports</p>
      <div style="margin-bottom: 15px;">
        <span style="background: #F0F9F0; color: #16A085; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; margin-right: 8px; display: inline-block; margin-bottom: 5px;">Data Collection</span>
        <span style="background: #F0F9F0; color: #16A085; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; margin-right: 8px; display: inline-block; margin-bottom: 5px;">Task Monitoring</span>
        <span style="background: #F0F9F0; color: #16A085; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 5px;">Quality Reports</span>
      </div>
      <div style="border-top: 1px solid #F0F0F0; padding-top: 15px;">
        <p style="margin: 0; color: #888; font-size: 0.9em;"><strong>Core Components:</strong> ProgressWidget, TableWidget, LogWidget</p>
      </div>
    </div>
    
    <!-- Regular Business Communication -->
    <div style="background: white; border-radius: 15px; padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); transition: transform 0.3s ease, box-shadow 0.3s ease; position: relative; overflow: hidden; border: 1px solid #f0f0f0;">
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, #FFB6C1, #FFA07A);"></div>
      <div style="display: flex; align-items: center; margin-bottom: 15px;">
        <div style="width: 50px; height: 50px; background: linear-gradient(135deg, #FFB6C1, #FFC1CC); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-right: 15px; box-shadow: 0 5px 15px rgba(255,182,193,0.3);">
          <span style="font-size: 24px;">📧</span>
        </div>
        <h3 style="margin: 0; color: #2C3E50; font-size: 1.4em; font-weight: 700;">Regular Business Communication</h3>
      </div>
      <p style="color: #666; line-height: 1.6; margin-bottom: 15px; font-size: 0.95em;">Team weekly reports, project progress, business summaries and other regular emails</p>
      <div style="margin-bottom: 15px;">
        <span style="background: #FFF0F5; color: #E74C3C; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; margin-right: 8px; display: inline-block; margin-bottom: 5px;">Project Management</span>
        <span style="background: #FFF0F5; color: #E74C3C; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; margin-right: 8px; display: inline-block; margin-bottom: 5px;">Team Communication</span>
        <span style="background: #FFF0F5; color: #E74C3C; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 5px;">Business Reports</span>
      </div>
      <div style="border-top: 1px solid #F0F0F0; padding-top: 15px;">
        <p style="margin: 0; color: #888; font-size: 0.9em;"><strong>Core Components:</strong> TextWidget, CardWidget, QuoteWidget</p>
      </div>
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
- :octicons-device-camera-video-24: **[组件预览](user-guide/widget-overview.md)**
- :material-api: **[API参考](api/core.md)**
- :material-code-braces: **[示例代码](examples/basic.md)**
- :material-tools: **[开发指南](development/contributing.md)**
</div>


## 🤝 社区与支持

### 获取帮助

- **📚 文档中心**: [完整文档](https://271374667.github.io/EmailWidget/)
- **🐛 问题反馈**: [GitHub Issues](https://github.com/271374667/EmailWidget/issues)
- **💬 讨论交流**: [GitHub Discussions](https://github.com/271374667/EmailWidget/discussions)
- **📧 邮件支持**: 271374667@qq.com

### 参与贡献

推荐使用 uv 作为项目管理和开发的包管理工具

```bash
# 1. 克隆项目
git clone https://github.com/271374667/EmailWidget.git

# 2. 安装开发环境
uv sync

# 3. 运行测试
uv run pytest

# 4. 提交更改
git commit -m "Feature: 添加新功能"
```

### 社交媒体

- **GitHub**: [271374667/EmailWidget](https://github.com/271374667/EmailWidget)
- **Bilibili**: [Python调包侠](https://space.bilibili.com/282527875)
- **Email**: 271374667@qq.com

## 📄 许可证

本项目采用 [MIT License](https://github.com/271374667/EmailWidget/blob/master/LICENSE) 开源协议。

---

<div align="center">
    <p>⭐ **如果这个项目对你有帮助，请给我们一个星标！** ⭐</p>
    <p>Made with ❤️ by <a href="https://github.com/271374667">Python调包侠</a></p>
    <p><a href="https://space.bilibili.com/282527875">📺 观看视频教程</a> • <a href="https://271374667.github.io/EmailWidget/">📖 查看完整文档</a></p>
</div> 