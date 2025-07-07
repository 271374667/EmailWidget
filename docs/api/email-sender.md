# 邮件发送器

`EmailSender` 模块提供了一套完整且易于使用的邮件发送解决方案，它内置了对多种主流邮箱服务商的支持。

## 发送器基类

所有具体的发送器都继承自 `EmailSender` 抽象基类。

::: email_widget.email_sender.EmailSender
    options:
        show_root_heading: true
        show_source: false
        heading_level: 3

## 工厂函数

为了方便使用，我们推荐使用 `create_email_sender` 工厂函数来创建发送器实例。

::: email_widget.email_sender.create_email_sender
    options:
        show_root_heading: true
        show_source: false
        heading_level: 3

## 具体实现

以下是针对不同邮箱服务商的具体实现类。通常你只需要通过工厂函数来使用它们。

### QQEmailSender

::: email_widget.email_sender.QQEmailSender
    options:
        show_root_heading: false
        heading_level: 4

### NetEaseEmailSender

::: email_widget.email_sender.NetEaseEmailSender
    options:
        show_root_heading: false
        heading_level: 4

### OutlookEmailSender

::: email_widget.email_sender.OutlookEmailSender
    options:
        show_root_heading: false
        heading_level: 4

### GmailSender

::: email_widget.email_sender.GmailSender
    options:
        show_root_heading: false
        heading_level: 4