# 🚀 Getting Started

Welcome to EmailWidget! This section will help you get started with EmailWidget and create your first professional email report in just a few minutes.

## ⚡ 30-Second Experience

If you want to experience the powerful features of EmailWidget right away, here's the simplest example:

```python
from email_widget import Email, TextWidget
from email_widget.core.enums import TextType

# 创建邮件
email = Email("我的第一份报告")

# 添加标题
email.add_widget(
    TextWidget()
    .set_content("欢迎使用 EmailWidget! 🎉")
    .set_type(TextType.TITLE_LARGE)
)

# 导出HTML文件
file_path = email.export_html("my_first_report.html")
print(f"报告已生成: {file_path}")
```

Run this code and you'll get a beautiful HTML email file!

--8<-- "assets/getting_started/index/demo1.html"

## 📖 Related Resources

In addition to getting started, you might also be interested in these resources:

### 📚 Deep Learning
- [User Guide](../user-guide/index.md) - Detailed component usage tutorials
- [API Reference](../api/index.md) - Complete API documentation
- [Example Code](../examples/index.md) - Real-world application scenarios

### 🤝 Get Help
- [GitHub Issues](https://github.com/271374667/SpiderDaily/issues) - Bug reports and feature requests
- [GitHub Discussions](https://github.com/271374667/EmailWidget/discussions) - Community discussions
- [Bilibili Videos](https://space.bilibili.com/282527875) - Video tutorials

### 🔧 Development Related
- [Development Guide](../development/index.md) - Contributing to the project
- [Contributing Code](../development/contributing.md) - Code contribution guidelines