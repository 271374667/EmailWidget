# 📧 Creating Your First Email

This tutorial will guide you through creating your first EmailWidget email report. We'll start with the simplest example and gradually add more features.

## 🎯 Chapter Goals

- Create a basic email object
- Add text, tables, charts, and other components
- Export HTML files
- Send emails to mailboxes

## 🚀 Step 1: The Simplest Email

Let's start with the simplest example:

```python
from email_widget import Email, TextWidget, TextType

email = Email("我的第一份报告")

# 添加欢迎文本
email.add_widget(
    TextWidget()
    .set_content("欢迎使用 EmailWidget! 🎉")
    .set_type(TextType.TITLE_LARGE)
)

# 导出HTML文件
file_path = email.export_html("first_email.html")
print(f"邮件已生成: {file_path}")
```

After running this code, you'll see a file named `first_email.html` in the current directory. Open it with a browser and you'll see a beautiful email page!

![image-20250704114446832](./first-email.assets/image-20250704114446832.png)

!!! success "🎉 Congratulations!"
    You've successfully created your first EmailWidget email!

## 📝 Step 2: Adding More Content

Now let's add more content to create a more complete report:

```python
from email_widget import Email, TextWidget, TableWidget, ProgressWidget
from email_widget.core.enums import TextType, ProgressTheme

# 创建邮件对象，并设置副标题和脚注
email = Email("📊 销售数据周报")
email.set_subtitle("2024年第3周销售情况汇总")
email.set_footer("本报告由销售团队自动生成")

# 1. 添加主标题
email.add_widget(
    TextWidget()
    .set_content("销售业绩概览")
    .set_type(TextType.TITLE_LARGE)
)

# 2. 添加进度指标
email.add_widget(
    ProgressWidget()
    .set_value(85)
    .set_label("本周目标完成率")
    .set_theme(ProgressTheme.SUCCESS)
)

# 3. 添加数据表格
table = TableWidget()
table.set_title("🏆 销售排行榜")
table.set_headers(["销售员", "销售额", "完成率", "状态"])
table.add_row(["张三", "¥125,000", "125%", "success"])
table.add_row(["李四", "¥98,000", "98%", "warning"])
table.add_row(["王五", "¥87,000", "87%", "info"])
email.add_widget(table)

# 4. 添加总结文本
email.add_widget(
    TextWidget()
    .set_content("本周销售业绩整体表现良好，超额完成既定目标。")
    .set_type(TextType.BODY)
)

# 导出HTML文件
file_path = email.export_html("sales_report.html")
print(f"销售报告已生成: {file_path}")
```

![image-20250704114504459](./first-email.assets/image-20250704114504459.png)

## Send to Mailbox

### Using Built-in `EmailSender` to Send Emails (Recommended)

The most convenient way is to directly use the `EmailSender` that comes with `EmailWidget`. Just select the appropriate `EmailSender` and call the `send` method with an `Email` object. Here's a simple example:

```python
from email_widget import Email, QQEmailSender

email = Email("欢迎使用EmailWidget")

email.add_card("Python版本", "您需要Python3.10或以上才能使用EmailWidget", metadata={"Python版本": "3.10+"})

email.add_quote("EmailWidget是一个用于构建和发送HTML邮件的Python库。", "EmailWidget")

# 一行代码成功发送邮件
QQEmailSender("你的QQ邮箱", "你的QQ邮箱授权码").send(email)
```

Here's the actual effect after sending the email. You can see that the email has been successfully sent and the styling is normal:

![image-20250706201345729](./first-email.assets/image-20250706201345729.png)

### Using smtplib Standard Library

Here we use the standard library smtplib to send emails. In actual development, you can also use other email sending libraries, such as redmail.

!!! warning "Note"

    yagmail has a built-in HTML processing step that removes EmailWidget's CSS styles, so it's currently incompatible. Please use email sending libraries other than yagmail, such as redmail.

```python
from email_widget import Email, TextWidget, TableWidget, ProgressWidget
from email_widget.core.enums import TextType, ProgressTheme
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 创建邮件对象，并设置副标题和脚注
email = Email("📊 销售数据周报")
email.set_subtitle("2024年第3周销售情况汇总")
email.set_footer("本报告由销售团队自动生成")

# 1. 添加主标题
email.add_widget(
    TextWidget().set_content("销售业绩概览").set_type(TextType.TITLE_LARGE)
)

# 2. 添加进度指标
email.add_widget(
    ProgressWidget()
    .set_value(85)
    .set_label("本周目标完成率")
    .set_theme(ProgressTheme.SUCCESS)
)

# 3. 添加数据表格
table = TableWidget()
table.set_title("🏆 销售排行榜")
table.set_headers(["销售员", "销售额", "完成率", "状态"])
table.add_row(["张三", "¥125,000", "125%", "success"])
table.add_row(["李四", "¥98,000", "98%", "warning"])
table.add_row(["王五", "¥87,000", "87%", "info"])
email.add_widget(table)

# 4. 添加总结文本
email.add_widget(
    TextWidget()
    .set_content("本周销售业绩整体表现良好，超额完成既定目标。")
    .set_type(TextType.BODY)
)

# 编写HTML类型的邮件正文
# 这里不导出为文件，而是使用 export_str 直接导出为字符串
msg = MIMEText(email.export_str(), "html", "utf-8")
msg["Subject"] = Header("邮件标题", "utf-8")
msg["From"] = "你的邮箱@qq.com"  # 添加发件人
msg["To"] = "你的邮箱@qq.com"  # 添加收件人

# 连接发送邮件(使用QQ邮箱为例)
smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
smtp.login("你的邮箱@qq.com", "jjhbkryjybwjbjbh")
smtp.sendmail("你的邮箱@qq.com", "你的邮箱@qq.com", msg.as_string())
smtp.quit()
```

After running, check your mailbox and you'll find the email has been successfully sent:

![image-20250704112531428](./first-email.assets/image-20250704112531428.png)

You can also see the beautiful report on mobile:

![image-20250704112733193](./first-email.assets/image-20250704112733193.png)

### Using redmail to Send Emails

Using redmail to send emails is relatively simpler, but requires installing additional dependencies:

```bash
pip install redmail
```

```python
from redmail import EmailSender
import os
from smtplib import SMTP_SSL
from email_widget import Email, TextWidget, TableWidget, ProgressWidget
from email_widget.core.enums import TextType, ProgressTheme

# 创建邮件对象，并设置副标题和脚注
email = Email("📊 销售数据周报")
email.set_subtitle("2024年第3周销售情况汇总")
email.set_footer("本报告由销售团队自动生成")

# 1. 添加主标题
email.add_widget(
    TextWidget().set_content("销售业绩概览").set_type(TextType.TITLE_LARGE)
)

# 2. 添加进度指标
email.add_widget(
    ProgressWidget()
    .set_value(85)
    .set_label("本周目标完成率")
    .set_theme(ProgressTheme.SUCCESS)
)

# 3. 添加数据表格
table = TableWidget()
table.set_title("🏆 销售排行榜")
table.set_headers(["销售员", "销售额", "完成率", "状态"])
table.add_row(["张三", "¥125,000", "125%", "success"])
table.add_row(["李四", "¥98,000", "98%", "warning"])
table.add_row(["王五", "¥87,000", "87%", "info"])
email.add_widget(table)

# 4. 添加总结文本
email.add_widget(
    TextWidget()
    .set_content("本周销售业绩整体表现良好，超额完成既定目标。")
    .set_type(TextType.BODY)
)

# 配置QQ邮箱发送器
email_sender = EmailSender(
    host="smtp.qq.com",
    port=465,
    username="你的邮箱@qq.com",  # 替换为你的QQ邮箱
    password="授权码",  # SMTP授权码
    use_starttls=False,
    cls_smtp=SMTP_SSL,
)

# 发送邮件
email_sender.send(
    subject="HTML测试邮件",
    sender="你的邮箱@qq.com",  # 替换为你的QQ邮箱
    receivers=["你的邮箱@qq.com"],  # 替换为接收邮件的邮箱
    html=email.export_str(),
)

print("邮件发送成功！")
```

## 🚀 Next Steps

Now that you've mastered the basic usage, you can continue learning:

- [Basic Concepts](concepts.md) - Deep dive into EmailWidget's design philosophy
- [User Guide](../user-guide/index.md) - Learn detailed usage of all components
- [Example Code](../examples/index.md) - See more real-world application scenarios

---

!!! question "Having Problems?"
    
    If you encounter any issues while creating your first email, you can:
    
    - Check [FAQ](faq.md)
    - Ask questions in [GitHub Issues](https://github.com/271374667/EmailWidget/issues)
    - Refer to [API Documentation](../api/index.md) for detailed usage