"""邮件发送模块

这个模块提供了邮件发送的抽象接口和各种邮箱服务商的具体实现.
支持QQ邮箱和网易邮箱.

Examples:
    >>> from email_widget import Email
    >>> from email_widget.email_sender import QQEmailSender
    >>>
    >>> # 创建邮件对象
    >>> email = Email("测试邮件")
    >>> email.add_text("这是一封测试邮件")
    >>>
    >>> # 创建发送器并发送邮件
    >>> sender = QQEmailSender("your_qq@qq.com", "your_password")
    >>> sender.send(email, to=["recipient@example.com"])
"""

import smtplib
from abc import ABC, abstractmethod
from contextlib import suppress
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from email_widget.email import Email  # 避免循环导入问题


class EmailSender(ABC):
    """邮件发送器抽象基类.

    定义了发送邮件的标准接口，所有具体的邮箱服务商实现都需要继承此类.
    这个基类处理了通用的邮件构建和发送逻辑，子类只需提供特定于服务商的
    SMTP服务器地址和端口号即可.

    Attributes:
        username (str): 邮箱用户名（通常是完整的邮箱地址）.
        password (str): 邮箱密码或授权码/应用密码.
        use_tls (bool): 是否使用TLS加密连接.
        smtp_server (str): SMTP服务器地址.
        smtp_port (int): SMTP服务器端口.

    Raises:
        ValueError: 如果用户名或密码为空.
    """

    def __init__(
        self,
        username: str,
        password: str,
        use_tls: bool = True,
        smtp_server: str | None = None,
        smtp_port: int | None = None,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """初始化邮件发送器.

        Args:
            username: 邮箱用户名/邮箱地址
            password: 邮箱密码或授权码
            use_tls: 是否使用TLS加密连接，默认为True
            smtp_server: SMTP服务器地址，如果不提供则使用默认值
            smtp_port: SMTP服务器端口，如果不提供则使用默认值
            *args: 其他位置参数
            **kwargs: 其他关键字参数

        Raises:
            ValueError: 当用户名或密码为空时抛出
        """
        if not username or not password:
            raise ValueError("用户名和密码不能为空")

        self.username = username
        self.password = password
        self.use_tls = use_tls
        self.smtp_server = smtp_server or self._get_default_smtp_server()
        self.smtp_port = smtp_port or self._get_default_smtp_port()

    @abstractmethod
    def _get_default_smtp_server(self) -> str:
        """获取默认的SMTP服务器地址.

        Returns:
            SMTP服务器地址
        """
        pass

    @abstractmethod
    def _get_default_smtp_port(self) -> int:
        """获取默认的SMTP服务器端口.

        Returns:
            SMTP服务器端口号
        """
        pass

    def _create_message(
        self, email: "Email", sender: str | None = None, to: list[str] | None = None
    ) -> MIMEMultipart:
        """创建邮件消息对象.

        Args:
            email: 邮件对象
            sender: 发送者邮箱地址，如果为None则使用username
            to: 接收者邮箱地址列表，如果为None则使用sender作为接收者

        Returns:
            配置好的邮件消息对象
        """
        msg = MIMEMultipart("alternative")

        # 设置发送者 - 对于大多数邮箱服务商，From必须与登录用户名一致
        # 忽略sender参数，始终使用登录的username作为发送者
        msg["From"] = self.username

        # 设置接收者
        recipients = to or [sender or self.username]
        msg["To"] = ", ".join(recipients)

        # 设置主题
        msg["Subject"] = Header(email.title, "utf-8")

        # 设置邮件内容
        html_content = email.export_str()
        html_part = MIMEText(html_content, "html", "utf-8")
        msg.attach(html_part)

        return msg

    def _send_message(self, msg: MIMEMultipart, to: list[str]) -> None:
        """发送邮件消息.

        Args:
            msg: 邮件消息对象
            to: 接收者邮箱地址列表

        Raises:
            smtplib.SMTPException: SMTP发送错误
            Exception: 其他发送错误
        """
        server = None
        try:
            # 创建SMTP连接
            if self.use_tls:
                # 使用TLS连接（STARTTLS）
                server = smtplib.SMTP(self.smtp_server, self.smtp_port)
                server.starttls()
            else:
                # 使用SSL连接
                server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)

            # 登录验证
            server.login(self.username, self.password)

            # 发送邮件 - 明确指定from_addr以确保兼容性
            server.send_message(msg, from_addr=self.username, to_addrs=to)

        except smtplib.SMTPAuthenticationError as e:
            raise smtplib.SMTPException(
                f"SMTP认证失败: {str(e)}.请检查用户名、密码或授权码是否正确."
            )
        except smtplib.SMTPConnectError as e:
            raise smtplib.SMTPException(
                f"SMTP连接失败: {str(e)}.请检查服务器地址和端口设置."
            )
        except smtplib.SMTPRecipientsRefused as e:
            raise smtplib.SMTPException(
                f"收件人被拒绝: {str(e)}.请检查收件人邮箱地址是否正确."
            )
        except smtplib.SMTPSenderRefused as e:
            raise smtplib.SMTPException(
                f"发件人被拒绝: {str(e)}.请检查发件人邮箱地址是否正确."
            )
        except smtplib.SMTPDataError as e:
            raise smtplib.SMTPException(f"SMTP数据错误: {str(e)}.邮件内容可能有问题.")
        except smtplib.SMTPException as e:
            raise smtplib.SMTPException(f"SMTP发送失败: {str(e)}")
        except Exception as e:
            raise Exception(f"邮件发送失败: {str(e)}")
        finally:
            # 确保连接被正确关闭
            if server:
                with suppress(Exception):
                    server.quit()

    def send(
        self, email: "Email", sender: str | None = None, to: list[str] | None = None
    ) -> None:
        """发送邮件.

        Args:
            email: 要发送的邮件对象
            sender: 发送者邮箱地址，如果为None则使用初始化时的username
            to: 接收者邮箱地址列表，如果为None则发送给sender

        Raises:
            ValueError: 当邮件对象为None时抛出
            smtplib.SMTPException: SMTP发送错误
            Exception: 其他发送错误

        Examples:
            >>> sender = QQEmailSender("user@qq.com", "password")
            >>> email = Email("测试邮件")
            >>>
            >>> # 发送给自己
            >>> sender.send(email)
            >>>
            >>> # 发送给指定收件人
            >>> sender.send(email, to=["recipient@example.com"])
            >>>
            >>> # 指定发送者和收件人
            >>> sender.send(email, sender="custom@qq.com", to=["recipient@example.com"])
        """
        if email is None:
            raise ValueError("邮件对象不能为None")

        # 准备接收者列表
        recipients = to or [sender or self.username]

        # 创建邮件消息
        msg = self._create_message(email, sender, recipients)

        # 发送邮件
        self._send_message(msg, recipients)


class QQEmailSender(EmailSender):
    """QQ邮箱发送器.

    专门用于通过 QQ 邮箱（包括企业邮箱）发送邮件.
    它预设了 QQ 邮箱的 SMTP 服务器地址和推荐的端口.

    重要提示:
        - **必须使用授权码**: 出于安全原因，QQ邮箱的SMTP服务要求使用"授权码"而非你的登录密码.你需要在QQ邮箱的"设置"->"账户"页面下生成此授权码.
        - **开启SMTP服务**: 请确保你已经在QQ邮箱设置中开启了IMAP/SMTP服务.

    Examples:
        ```python
        from email_widget import Email, QQEmailSender
        import os

        # 建议从环境变量读取敏感信息
        # export EMAIL_USER="your_account@qq.com"
        # export EMAIL_AUTH_CODE="your_generated_auth_code"

        qq_user = os.getenv("EMAIL_USER")
        auth_code = os.getenv("EMAIL_AUTH_CODE")

        # 创建邮件内容
        email = Email("来自QQ邮箱的报告")
        email.add_text("这是一封通过 EmailWidget 发送的测试邮件.")

        # 初始化QQ邮箱发送器
        sender = QQEmailSender(username=qq_user, password=auth_code)

        # 发送邮件给一个或多个收件人
        try:
            sender.send(email, to=["recipient1@example.com", "recipient2@example.com"])
            print("邮件发送成功！")
        except Exception as e:
            print(f"邮件发送失败: {e}")
        ```
    """

    def __init__(
        self, username: str, password: str, use_tls: bool = True, *args: Any, **kwargs: Any
    ) -> None:
        """初始化QQ邮箱发送器.

        Args:
            username: QQ邮箱地址
            password: QQ邮箱授权码（非登录密码）
            use_tls: 是否使用TLS加密，默认为True
            *args: 其他位置参数
            **kwargs: 其他关键字参数
        """
        super().__init__(username, password, use_tls, *args, **kwargs)

    def _get_default_smtp_server(self) -> str:
        """获取QQ邮箱的默认SMTP服务器地址.

        Returns:
            QQ邮箱SMTP服务器地址
        """
        return "smtp.qq.com"

    def _get_default_smtp_port(self) -> int:
        """获取QQ邮箱的默认SMTP端口.

        Returns:
            QQ邮箱SMTP端口号
        """
        return 587 if self.use_tls else 465


class NetEaseEmailSender(EmailSender):
    """网易邮箱发送器.

    支持网易旗下的 163、126 和 yeah.net 邮箱.
    它会自动根据你的邮箱地址后缀选择正确的SMTP服务器.

    重要提示:
        - **必须使用授权码**: 与QQ邮箱类似，网易邮箱也需要使用专用的"客户端授权密码"，而不是你的邮箱登录密码.
        - **开启SMTP服务**: 请在你的网易邮箱设置中开启POP3/SMTP/IMAP服务.
        - **SSL连接**: 网易邮箱的SMTP服务主要使用SSL加密（端口465），因此默认 `use_tls` 为 `False`.

    Examples:
        ```python
        from email_widget import Email, NetEaseEmailSender
        import os

        # 使用163邮箱
        user_163 = os.getenv("NETEASE_USER_163") # e.g., "my_account@163.com"
        auth_code_163 = os.getenv("NETEASE_AUTH_CODE_163")

        email = Email("来自163邮箱的问候")
        email.add_text("这是通过 NetEaseEmailSender 发送的邮件.")

        sender = NetEaseEmailSender(username=user_163, password=auth_code_163)

        try:
            sender.send(email, to=["friend@example.com"])
            print("163邮件发送成功！")
        except Exception as e:
            print(f"邮件发送失败: {e}")
        ```
    """

    def __init__(
        self,
        username: str,
        password: str,
        use_tls: bool = False,  # 网易邮箱默认使用SSL，不是TLS
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """初始化网易邮箱发送器.

        Args:
            username: 网易邮箱地址
            password: 网易邮箱授权码
            use_tls: 是否使用TLS加密，默认为False（网易邮箱使用SSL）
            *args: 其他位置参数
            **kwargs: 其他关键字参数

        Note:
            网易邮箱只支持SSL连接（端口465），建议保持use_tls=False.
        """
        super().__init__(username, password, use_tls, *args, **kwargs)

    def _get_default_smtp_server(self) -> str:
        """获取网易邮箱的默认SMTP服务器地址.

        Returns:
            网易邮箱SMTP服务器地址
        """
        # 根据邮箱域名返回对应的SMTP服务器
        if "@163.com" in self.username:
            return "smtp.163.com"
        elif "@126.com" in self.username:
            return "smtp.126.com"
        elif "@yeah.net" in self.username:
            return "smtp.yeah.net"
        else:
            return "smtp.163.com"  # 默认使用163的服务器

    def _get_default_smtp_port(self) -> int:
        """获取网易邮箱的默认SMTP端口.

        Returns:
            网易邮箱SMTP端口号

        Note:
            网易邮箱只支持SSL连接（端口465）.
        """
        return 465  # 网易邮箱只支持SSL端口465


# 邮箱服务商映射字典，方便用户选择
EMAIL_PROVIDERS: dict[str, type] = {
    "qq": QQEmailSender,
    "netease": NetEaseEmailSender,
    "163": NetEaseEmailSender,
    "126": NetEaseEmailSender,
}


def create_email_sender(
    provider: str, username: str, password: str, **kwargs: Any
) -> EmailSender:
    """工厂函数，根据服务商名称快速创建对应的邮件发送器实例.

    这是一个便捷的辅助函数，让你无需直接导入和实例化特定的发送器类.
    它通过一个字符串标识来选择正确的发送器，特别适合在配置文件中指定服务商的场景.

    Args:
        provider (str): 邮箱服务商的标识符.支持的值（不区分大小写）包括：
                      'qq', 'netease', '163', '126'.
        username (str): 邮箱账户，通常是完整的邮箱地址.
        password (str): 邮箱的授权码或应用密码.
        **kwargs: 其他关键字参数，将直接传递给所选发送器类的构造函数.

    Returns:
        EmailSender: 一个具体的邮件发送器实例 (例如 `QQEmailSender`).

    Raises:
        ValueError: 如果提供的 `provider` 名称不被支持.

    Examples:
        ```python
        from email_widget import Email, create_email_sender
        import os

        # 从配置或环境变量中读取服务商和凭证
        email_provider = os.getenv("EMAIL_PROVIDER", "qq") # e.g., 'qq' or 'netease'
        email_user = os.getenv("EMAIL_USER")
        email_password = os.getenv("EMAIL_PASSWORD")

        # 使用工厂函数创建发送器
        try:
            sender = create_email_sender(
                provider=email_provider,
                username=email_user,
                password=email_password
            )

            email = Email(f"来自 {email_provider.upper()} 的邮件")
            email.add_text("通过工厂函数创建的发送器.")
            sender.send(email, to=["test@example.com"])
            print("邮件发送成功！")

        except ValueError as e:
            print(f"配置错误: {e}")
        except Exception as e:
            print(f"发送失败: {e}")
        ```
    """
    provider_lower = provider.lower()
    if provider_lower not in EMAIL_PROVIDERS:
        supported = ", ".join(EMAIL_PROVIDERS.keys())
        raise ValueError(f"不支持的邮箱服务商: {provider}.支持的服务商: {supported}")

    sender_class = EMAIL_PROVIDERS[provider_lower]
    return sender_class(username, password, **kwargs)
