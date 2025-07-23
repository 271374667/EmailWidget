# 邮件发送器

## 常见邮箱SMTP配置与授权码获取

以下为主流邮箱（QQ、163、Outlook、Gmail）SMTP服务器参数及授权码获取方法，便于快速配置。

| 邮箱类型   | SMTP服务器         | 端口 | 加密方式 | 用户名           | 密码类型   |
|------------|--------------------|------|----------|------------------|------------|
| QQ邮箱     | smtp.qq.com        | 465  | SSL      | 完整邮箱地址     | 授权码     |
| 163邮箱    | smtp.163.com       | 465  | SSL      | 完整邮箱地址     | 授权码     |
| Gmail      | smtp.gmail.com     | 587  | TLS      | 完整邮箱地址     | 应用专用密码 |

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

### Gmail
1. 登录Google账户，访问[Google账户设置](https://myaccount.google.com)。
2. 导航到"安全性" > "两步验证"，如未启用请先启用两步验证。
3. 前往"安全性" > "应用专用密码"，生成新的应用专用密码：
   - 选择"邮件"作为应用类型
   - 选择设备或输入自定义名称
   - 复制生成的16位密码（不含空格）
4. 邮件客户端配置时，用户名为完整Gmail地址，密码为生成的应用专用密码。
- 官方文档：[Google账户帮助 - 应用专用密码](https://support.google.com/accounts/answer/185833)
- Gmail SMTP设置：[Gmail IMAP和SMTP设置](https://support.google.com/mail/answer/7126229)

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

!!! info "API 参考"
    完整的 API 文档请参考 [英文版本](../../en/api/email-sender.md)，此处提供中文说明。

`EmailSender` 模块提供了一套完整且易于使用的邮件发送解决方案，它内置了对多种主流邮箱服务商的支持。

## 发送器基类

`EmailSender` 是所有具体发送器的抽象基类，定义了邮件发送的标准接口。

### 主要方法

- `send(email, to_addrs, subject=None, **kwargs)`: 发送邮件的主要方法
  - `email`: Email 对象实例
  - `to_addrs`: 收件人地址（字符串或列表）
  - `subject`: 邮件主题（可选）
  - `**kwargs`: 其他邮件选项

### 配置属性

- `smtp_server`: SMTP 服务器地址
- `smtp_port`: SMTP 服务器端口
- `username`: 发件人邮箱地址
- `password`: 邮箱密码或授权码
- `use_tls`: 是否使用 TLS 加密

## 工厂函数

`create_email_sender(email_type, username, password, **kwargs)` 是创建发送器实例的推荐方式。

### 参数说明

- `email_type`: 邮箱类型，支持 'qq', 'netease', '163', '126', 'gmail' 等
- `username`: 发件人邮箱地址
- `password`: 邮箱密码或授权码
- `**kwargs`: 其他配置选项

### 使用示例

```python
from email_widget.email_sender import create_email_sender

# 创建 QQ 邮箱发送器
sender = create_email_sender('qq', 'your_email@qq.com', 'your_auth_code')

# 创建 Gmail 发送器
gmail_sender = create_email_sender('gmail', 'your_email@gmail.com', 'your_app_password')

# 发送邮件
sender.send(email, to=['recipient@example.com'])
```

## 具体实现

### QQEmailSender

专门针对 QQ 邮箱的发送器实现，预配置了 QQ 邮箱的 SMTP 参数。

- **SMTP 服务器**: smtp.qq.com
- **端口**: 465 (SSL)
- **认证**: 需要使用授权码而非登录密码

### NetEaseEmailSender

专门针对网易邮箱（163、126等）的发送器实现。

- **SMTP 服务器**: smtp.163.com 或 smtp.126.com
- **端口**: 465 (SSL)
- **认证**: 需要使用授权码而非登录密码

### GmailEmailSender

专门针对 Gmail 的发送器实现，预配置了 Gmail 的 SMTP 参数。

- **SMTP 服务器**: smtp.gmail.com
- **端口**: 587 (TLS，默认) 或 465 (SSL)
- **认证**: 需要使用应用专用密码而非普通登录密码
- **重要提醒**: 必须先启用两步验证，然后生成应用专用密码

### 使用示例

```python
from email_widget.email_sender import GmailEmailSender
from email_widget import Email

# 创建 Gmail 发送器
sender = GmailEmailSender("your_email@gmail.com", "your_app_password")

# 创建邮件
email = Email("测试邮件")
email.add_text("这是通过Gmail发送的测试邮件")

# 发送邮件
sender.send(email, to=["recipient@example.com"])
```