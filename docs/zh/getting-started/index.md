# 🚀 快速开始

欢迎使用 EmailWidget！这个部分将帮助你在几分钟内上手使用EmailWidget创建你的第一个专业邮件报告。

## ⚡ 30秒体验

如果你想立即体验EmailWidget的强大功能，这里有一个最简单的例子：

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

运行这个代码，你将得到一个美观的HTML邮件文件！

--8<-- "assets/getting_started/index/demo1.html"

## 📖 相关资源

除了快速开始，你可能还对这些内容感兴趣：

### 📚 深入学习
- [用户指南](../user-guide/index.md) - 详细的组件使用教程
- [API参考](../api/index.md) - 完整的API文档
- [示例代码](../examples/index.md) - 实际应用场景

### 🤝 获取帮助
- [GitHub Issues](https://github.com/271374667/SpiderDaily/issues) - 问题反馈
- [GitHub Discussions](https://github.com/271374667/EmailWidget/discussions) - 社区讨论
- [Bilibili视频](https://space.bilibili.com/282527875) - 视频教程

### 🔧 开发相关
- [开发指南](../development/index.md) - 参与项目开发
- [贡献代码](../development/contributing.md) - 贡献代码指南