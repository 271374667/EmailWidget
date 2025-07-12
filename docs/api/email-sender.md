# 邮件发送器

## 常见邮箱SMTP配置与授权码获取

以下为主流邮箱（QQ、163、Outlook、Gmail）SMTP服务器参数及授权码获取方法，便于快速配置。

| 邮箱类型   | SMTP服务器         | 端口 | 加密方式 | 用户名           | 密码类型   |
|------------|--------------------|------|----------|------------------|------------|
| QQ邮箱     | smtp.qq.com        | 465  | SSL      | 完整邮箱地址     | 授权码     |
| 163邮箱    | smtp.163.com       | 465  | SSL      | 完整邮箱地址     | 授权码     |

---

### QQ邮箱
1. 登录QQ邮箱网页版，点击右上角"设置">"账户"。
2. 在"POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务"处，勾选"开启SMTP服务"，保存。
3. 按提示进行手机验证，获取授权码（此码即为SMTP登录密码）。
4. 邮件客户端配置时，用户名为完整邮箱，密码为授权码。
- 详细官方说明：[QQ邮箱帮助中心](https://service.mail.qq.com/)
- 微软官方Outlook对接QQ邮箱说明（含授权码获取步骤）：[查看](https://support.microsoft.com/en-us/office/add-a-qqmail-account-to-outlook-34ef1254-0d07-405a-856f-0409c7c905eb)

### 163邮箱
1. 登录163邮箱网页版，点击"设置">"POP3/SMTP/IMAP"。
2. 开启"SMTP服务"，如需验证请按提示操作。
3. 获取授权码（部分账号需手机验证），此码即为SMTP登录密码。
4. 邮件客户端配置时，用户名为完整邮箱，密码为授权码。
- 官方帮助中心：[网易邮箱帮助](https://help.mail.163.com/faqDetail.do?code=d7a5dc8471cd0c0e8b4b8f4f8e49998b374173cfe9171305fa1ce630d7f67ac2c9926ce59ec02fa9)
- 参考博客：[Mailbird 163邮箱配置](https://www.getmailbird.com/setup/access-163-com-via-imap-smtp)

---

### FAQ

**Q1：什么是授权码/应用专用密码？**
A：授权码/应用专用密码是邮箱服务商为提升安全性而生成的专用密码，用于第三方应用（如邮件客户端、自动化脚本）登录邮箱，不能用普通登录密码代替。

**Q2：为什么要用授权码/应用专用密码？**
A：开启两步验证后，普通密码无法直接用于SMTP等第三方服务，必须使用授权码/应用专用密码，保障账户安全。

**Q3：授权码/应用专用密码丢失怎么办？**
A：可随时在邮箱安全设置中重新生成新的授权码/应用专用密码，原有的可作废。

**Q4：配置失败常见原因有哪些？**
A：常见原因包括未开启SMTP服务、未使用授权码/专用密码、端口/加密方式配置错误、邮箱被限制登录等。

如遇特殊问题，建议优先查阅各邮箱官方帮助中心或联系邮箱服务商客服。

---

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