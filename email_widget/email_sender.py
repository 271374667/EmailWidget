"""邮件发送模块

这个模块提供了邮件发送的抽象接口和各种邮箱服务商的具体实现。
支持QQ邮箱、网易邮箱、Outlook邮箱和Gmail邮箱。

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
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from typing import Optional, List, Dict, TYPE_CHECKING
from contextlib import suppress

if TYPE_CHECKING:
    from email_widget.email import Email  # 避免循环导入问题


class EmailSender(ABC):
    """邮件发送器抽象基类。
    
    定义了发送邮件的标准接口，所有具体的邮箱服务商实现都需要继承此类。
    
    Attributes:
        username: 邮箱用户名
        password: 邮箱密码或授权码
        use_tls: 是否使用TLS加密连接
        smtp_server: SMTP服务器地址
        smtp_port: SMTP服务器端口
        
    Examples:
        >>> # 不能直接实例化抽象基类
        >>> # sender = EmailSender()  # 会抛出TypeError
        >>> 
        >>> # 需要使用具体的实现类
        >>> sender = QQEmailSender("user@qq.com", "password")
    """

    def __init__(
        self, 
        username: str, 
        password: str, 
        use_tls: bool = True, 
        smtp_server: Optional[str] = None,
        smtp_port: Optional[int] = None,
        *args, 
        **kwargs
    ) -> None:
        """初始化邮件发送器。

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
        """获取默认的SMTP服务器地址。
        
        Returns:
            SMTP服务器地址
        """
        pass

    @abstractmethod
    def _get_default_smtp_port(self) -> int:
        """获取默认的SMTP服务器端口。
        
        Returns:
            SMTP服务器端口号
        """
        pass

    def _create_message(
        self, 
        email: "Email", 
        sender: Optional[str] = None, 
        to: Optional[List[str]] = None
    ) -> MIMEMultipart:
        """创建邮件消息对象。
        
        Args:
            email: 邮件对象
            sender: 发送者邮箱地址，如果为None则使用username
            to: 接收者邮箱地址列表，如果为None则使用sender作为接收者
            
        Returns:
            配置好的邮件消息对象
        """
        msg = MIMEMultipart('alternative')
        
        # 设置发送者 - 对于大多数邮箱服务商，From必须与登录用户名一致
        # 忽略sender参数，始终使用登录的username作为发送者
        msg['From'] = self.username
        
        # 设置接收者
        recipients = to or [sender or self.username]
        msg['To'] = ', '.join(recipients)
        
        # 设置主题
        msg['Subject'] = Header(email.title, 'utf-8')
        
        # 设置邮件内容
        html_content = email.export_str()
        html_part = MIMEText(html_content, 'html', 'utf-8')
        msg.attach(html_part)
        
        return msg

    def _send_message(self, msg: MIMEMultipart, to: List[str]) -> None:
        """发送邮件消息。
        
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
            raise smtplib.SMTPException(f"SMTP认证失败: {str(e)}。请检查用户名、密码或授权码是否正确。")
        except smtplib.SMTPConnectError as e:
            raise smtplib.SMTPException(f"SMTP连接失败: {str(e)}。请检查服务器地址和端口设置。")
        except smtplib.SMTPRecipientsRefused as e:
            raise smtplib.SMTPException(f"收件人被拒绝: {str(e)}。请检查收件人邮箱地址是否正确。")
        except smtplib.SMTPSenderRefused as e:
            raise smtplib.SMTPException(f"发件人被拒绝: {str(e)}。请检查发件人邮箱地址是否正确。")
        except smtplib.SMTPDataError as e:
            raise smtplib.SMTPException(f"SMTP数据错误: {str(e)}。邮件内容可能有问题。")
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
        self, 
        email: "Email", 
        sender: Optional[str] = None, 
        to: Optional[List[str]] = None
    ) -> None:
        """发送邮件。

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
    """QQ邮箱发送器。
    
    支持QQ邮箱和企业QQ邮箱的邮件发送功能。
    
    Note:
        QQ邮箱需要开启SMTP服务并使用授权码而非登录密码。
        
    Examples:
        >>> # 使用QQ邮箱发送
        >>> sender = QQEmailSender("your_qq@qq.com", "your_auth_code")
        >>> email = Email("QQ邮件测试")
        >>> sender.send(email, to=["recipient@example.com"])
    """

    def __init__(
        self, 
        username: str, 
        password: str, 
        use_tls: bool = True, 
        *args, 
        **kwargs
    ) -> None:
        """初始化QQ邮箱发送器。

        Args:
            username: QQ邮箱地址
            password: QQ邮箱授权码（非登录密码）
            use_tls: 是否使用TLS加密，默认为True
            *args: 其他位置参数
            **kwargs: 其他关键字参数
        """
        super().__init__(username, password, use_tls, *args, **kwargs)

    def _get_default_smtp_server(self) -> str:
        """获取QQ邮箱的默认SMTP服务器地址。
        
        Returns:
            QQ邮箱SMTP服务器地址
        """
        return "smtp.qq.com"

    def _get_default_smtp_port(self) -> int:
        """获取QQ邮箱的默认SMTP端口。
        
        Returns:
            QQ邮箱SMTP端口号
        """
        return 587 if self.use_tls else 465


class NetEaseEmailSender(EmailSender):
    """网易邮箱发送器。
    
    支持163邮箱、126邮箱等网易邮箱服务的邮件发送功能。
    
    Note:
        网易邮箱需要开启SMTP服务并使用授权码。
        网易邮箱只支持SSL连接（端口465），不支持TLS（端口587）。
        
    Examples:
        >>> # 使用163邮箱发送
        >>> sender = NetEaseEmailSender("your_email@163.com", "your_auth_code")
        >>> email = Email("网易邮件测试")
        >>> sender.send(email, to=["recipient@example.com"])
    """

    def __init__(
        self, 
        username: str, 
        password: str, 
        use_tls: bool = False,  # 网易邮箱默认使用SSL，不是TLS
        *args, 
        **kwargs
    ) -> None:
        """初始化网易邮箱发送器。

        Args:
            username: 网易邮箱地址
            password: 网易邮箱授权码
            use_tls: 是否使用TLS加密，默认为False（网易邮箱使用SSL）
            *args: 其他位置参数
            **kwargs: 其他关键字参数
            
        Note:
            网易邮箱只支持SSL连接（端口465），建议保持use_tls=False。
        """
        super().__init__(username, password, use_tls, *args, **kwargs)

    def _get_default_smtp_server(self) -> str:
        """获取网易邮箱的默认SMTP服务器地址。
        
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
        """获取网易邮箱的默认SMTP端口。
        
        Returns:
            网易邮箱SMTP端口号
            
        Note:
            网易邮箱只支持SSL连接（端口465）。
        """
        return 465  # 网易邮箱只支持SSL端口465


class OutlookEmailSender(EmailSender):
    """Outlook邮箱发送器。
    
    支持Outlook.com、Hotmail.com等微软邮箱服务的邮件发送功能。
    
    Note:
        Outlook邮箱建议使用应用密码而非登录密码。
        Outlook邮箱只支持TLS连接（端口587），不支持SSL连接。
        需要在Outlook.com设置中启用POP和IMAP访问。
        
    Examples:
        >>> # 使用Outlook邮箱发送
        >>> sender = OutlookEmailSender("your_email@outlook.com", "your_app_password")
        >>> email = Email("Outlook邮件测试")
        >>> sender.send(email, to=["recipient@example.com"])
    """

    def __init__(
        self, 
        username: str, 
        password: str, 
        use_tls: bool = True, 
        *args, 
        **kwargs
    ) -> None:
        """初始化Outlook邮箱发送器。

        Args:
            username: Outlook邮箱地址
            password: Outlook邮箱应用密码
            use_tls: 是否使用TLS加密，默认为True（Outlook只支持TLS）
            *args: 其他位置参数
            **kwargs: 其他关键字参数
            
        Note:
            Outlook邮箱只支持TLS连接，不支持SSL连接。
        """
        # 强制使用TLS，因为Outlook不支持SSL
        super().__init__(username, password, True, *args, **kwargs)

    def _get_default_smtp_server(self) -> str:
        """获取Outlook邮箱的默认SMTP服务器地址。
        
        Returns:
            Outlook邮箱SMTP服务器地址
        """
        return "smtp-mail.outlook.com"

    def _get_default_smtp_port(self) -> int:
        """获取Outlook邮箱的默认SMTP端口。
        
        Returns:
            Outlook邮箱SMTP端口号
            
        Note:
            Outlook只支持TLS连接，端口587。
        """
        return 587  # Outlook只支持TLS，端口587


class GmailSender(EmailSender):
    """Gmail邮箱发送器。
    
    支持Gmail邮箱的邮件发送功能。
    
    Note:
        Gmail需要开启两步验证并使用应用专用密码。
        Gmail支持TLS（端口587）和SSL（端口465）两种连接方式。
        建议使用TLS连接以获得更好的兼容性。
        
    Examples:
        >>> # 使用Gmail发送
        >>> sender = GmailSender("your_email@gmail.com", "your_app_password")
        >>> email = Email("Gmail邮件测试")
        >>> sender.send(email, to=["recipient@example.com"])
    """

    def __init__(
        self, 
        username: str, 
        password: str, 
        use_tls: bool = True, 
        *args, 
        **kwargs
    ) -> None:
        """初始化Gmail发送器。

        Args:
            username: Gmail邮箱地址
            password: Gmail应用专用密码
            use_tls: 是否使用TLS加密，默认为True（推荐TLS连接）
            *args: 其他位置参数
            **kwargs: 其他关键字参数
            
        Note:
            Gmail支持TLS（端口587）和SSL（端口465），推荐使用TLS。
        """
        super().__init__(username, password, use_tls, *args, **kwargs)

    def _get_default_smtp_server(self) -> str:
        """获取Gmail的默认SMTP服务器地址。
        
        Returns:
            Gmail SMTP服务器地址
        """
        return "smtp.gmail.com"

    def _get_default_smtp_port(self) -> int:
        """获取Gmail的默认SMTP端口。
        
        Returns:
            Gmail SMTP端口号
            
        Note:
            TLS使用端口587，SSL使用端口465。
        """
        return 587 if self.use_tls else 465


# 邮箱服务商映射字典，方便用户选择
EMAIL_PROVIDERS: Dict[str, type] = {
    "qq": QQEmailSender,
    "netease": NetEaseEmailSender,
    "163": NetEaseEmailSender,
    "126": NetEaseEmailSender,
    "outlook": OutlookEmailSender,
    "hotmail": OutlookEmailSender,
    "gmail": GmailSender,
}


def create_email_sender(
    provider: str, 
    username: str, 
    password: str, 
    **kwargs
) -> EmailSender:
    """工厂函数，根据服务商名称创建对应的邮件发送器。
    
    Args:
        provider: 邮箱服务商名称，支持的值包括：
            - "qq": QQ邮箱
            - "netease", "163", "126": 网易邮箱
            - "outlook", "hotmail": Outlook邮箱
            - "gmail": Gmail邮箱
        username: 邮箱用户名
        password: 邮箱密码或授权码
        **kwargs: 其他参数传递给具体的发送器类
        
    Returns:
        对应的邮件发送器实例
        
    Raises:
        ValueError: 当provider不支持时抛出
        
    Examples:
        >>> # 创建QQ邮箱发送器
        >>> sender = create_email_sender("qq", "user@qq.com", "auth_code")
        >>> 
        >>> # 创建Gmail发送器
        >>> sender = create_email_sender("gmail", "user@gmail.com", "app_password")
    """
    provider_lower = provider.lower()
    if provider_lower not in EMAIL_PROVIDERS:
        supported = ", ".join(EMAIL_PROVIDERS.keys())
        raise ValueError(f"不支持的邮箱服务商: {provider}. 支持的服务商: {supported}")
    
    sender_class = EMAIL_PROVIDERS[provider_lower]
    return sender_class(username, password, **kwargs)