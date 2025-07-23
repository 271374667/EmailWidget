"""Email sending module

This module provides abstract interfaces for email sending and specific implementations for various email service providers.
Supports QQ Mail, NetEase Mail, and Gmail.

Examples:
    >>> from email_widget import Email
    >>> from email_widget.email_sender import QQEmailSender
    >>>
    >>> # Create email object
    >>> email = Email("Test Email")
    >>> email.add_text("This is a test email")
    >>>
    >>> # Create sender and send email
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
    from email_widget.email import Email  # Avoid circular import issues


class EmailSender(ABC):
    """Email sender abstract base class.

    Defines the standard interface for sending emails, all specific email service provider implementations must inherit from this class.
    This base class handles common email construction and sending logic, subclasses only need to provide service-specific
    SMTP server addresses and port numbers.

    Attributes:
        username (str): Email username (usually the complete email address).
        password (str): Email password or authorization code/app password.
        use_tls (bool): Whether to use TLS encrypted connection.
        smtp_server (str): SMTP server address.
        smtp_port (int): SMTP server port.

    Raises:
        ValueError: If username or password is empty.
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
        """Initialize email sender.

        Args:
            username: Email username/email address
            password: Email password or authorization code
            use_tls: Whether to use TLS encrypted connection, defaults to True
            smtp_server: SMTP server address, if not provided, uses default value
            smtp_port: SMTP server port, if not provided, uses default value
            *args: Other positional arguments
            **kwargs: Other keyword arguments

        Raises:
            ValueError: Raised when username or password is empty
        """
        if not username or not password:
            raise ValueError("Username and password cannot be empty")

        self.username = username
        self.password = password
        self.use_tls = use_tls
        self.smtp_server = smtp_server or self._get_default_smtp_server()
        self.smtp_port = smtp_port or self._get_default_smtp_port()

    @abstractmethod
    def _get_default_smtp_server(self) -> str:
        """Get default SMTP server address.

        Returns:
            SMTP server address
        """
        pass

    @abstractmethod
    def _get_default_smtp_port(self) -> int:
        """Get default SMTP server port.

        Returns:
            SMTP server port number
        """
        pass

    def _create_message(
        self, email: "Email", sender: str | None = None, to: list[str] | None = None
    ) -> MIMEMultipart:
        """Create email message object.

        Args:
            email: Email object
            sender: Sender email address, uses username if None
            to: Recipient email address list, uses sender as recipient if None

        Returns:
            Configured email message object
        """
        msg = MIMEMultipart("alternative")

        # Set sender - For most email service providers, From must match the logged-in username
        # Ignore sender parameter, always use logged-in username as sender
        msg["From"] = self.username

        # Set recipients
        recipients = to or [sender or self.username]
        msg["To"] = ", ".join(recipients)

        # Set subject
        msg["Subject"] = Header(email.title, "utf-8")

        # Set email content
        html_content = email.export_str()
        html_part = MIMEText(html_content, "html", "utf-8")
        msg.attach(html_part)

        return msg

    def _send_message(self, msg: MIMEMultipart, to: list[str]) -> None:
        """Send email message.

        Args:
            msg: Email message object
            to: Recipient email address list

        Raises:
            smtplib.SMTPException: SMTP sending error
            Exception: Other sending errors
        """
        server = None
        try:
            # Create SMTP connection
            if self.use_tls:
                # Use TLS connection (STARTTLS)
                server = smtplib.SMTP(self.smtp_server, self.smtp_port)
                server.starttls()
            else:
                # Use SSL connection
                server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)

            # Login authentication
            server.login(self.username, self.password)

            # Send email - explicitly specify from_addr for compatibility
            server.send_message(msg, from_addr=self.username, to_addrs=to)

        except smtplib.SMTPAuthenticationError as e:
            raise smtplib.SMTPException(
                f"SMTP authentication failed: {str(e)}. Please check username, password or authorization code."
            )
        except smtplib.SMTPConnectError as e:
            raise smtplib.SMTPException(
                f"SMTP connection failed: {str(e)}. Please check server address and port settings."
            )
        except smtplib.SMTPRecipientsRefused as e:
            raise smtplib.SMTPException(
                f"Recipients refused: {str(e)}. Please check recipient email addresses."
            )
        except smtplib.SMTPSenderRefused as e:
            raise smtplib.SMTPException(
                f"Sender refused: {str(e)}. Please check sender email address."
            )
        except smtplib.SMTPDataError as e:
            raise smtplib.SMTPException(f"SMTP data error: {str(e)}. Email content may have issues.")
        except smtplib.SMTPException as e:
            raise smtplib.SMTPException(f"SMTP sending failed: {str(e)}")
        except Exception as e:
            raise Exception(f"Email sending failed: {str(e)}")
        finally:
            # Ensure connection is properly closed
            if server:
                with suppress(Exception):
                    server.quit()

    def send(
        self, email: "Email", sender: str | None = None, to: list[str] | None = None
    ) -> None:
        """Send email.

        Args:
            email: Email object to send
            sender: Sender email address, uses username if None
            to: Recipient email address list, sends to sender if None

        Raises:
            ValueError: Raised when email object is None
            smtplib.SMTPException: SMTP sending error
            Exception: Other sending errors

        Examples:
            >>> sender = QQEmailSender("user@qq.com", "password")
            >>> email = Email("Test Email")
            >>>
            >>> # Send to self
            >>> sender.send(email)
            >>>
            >>> # Send to specified recipients
            >>> sender.send(email, to=["recipient@example.com"])
            >>>
            >>> # Specify sender and recipients
            >>> sender.send(email, sender="custom@qq.com", to=["recipient@example.com"])
        """
        if email is None:
            raise ValueError("Email object cannot be None")

        # Prepare recipient list
        recipients = to or [sender or self.username]

        # Create email message
        msg = self._create_message(email, sender, recipients)

        # Send email
        self._send_message(msg, recipients)


class QQEmailSender(EmailSender):
    """QQ Email sender.

    Specifically designed for sending emails through QQ Email (including enterprise email).
    It presets the SMTP server address and recommended port for QQ Email.

    Important notes:
        - **Must use authorization code**: For security reasons, QQ Email's SMTP service requires using an "authorization code" instead of your login password. You need to generate this authorization code in QQ Email's "Settings" -> "Account" page.
        - **Enable SMTP service**: Please ensure you have enabled IMAP/SMTP service in QQ Email settings.

    Examples:
        ```python
        from email_widget import Email, QQEmailSender
        import os

        # Recommend reading sensitive information from environment variables
        # export EMAIL_USER="your_account@qq.com"
        # export EMAIL_AUTH_CODE="your_generated_auth_code"

        qq_user = os.getenv("EMAIL_USER")
        auth_code = os.getenv("EMAIL_AUTH_CODE")

        # Create email content
        email = Email("Report from QQ Email")
        email.add_text("This is a test email sent through EmailWidget.")

        # Initialize QQ Email sender
        sender = QQEmailSender(username=qq_user, password=auth_code)

        # Send email to one or more recipients
        try:
            sender.send(email, to=["recipient1@example.com", "recipient2@example.com"])
            print("Email sent successfully!")
        except Exception as e:
            print(f"Email sending failed: {e}")
        ```
    """

    def __init__(
        self, username: str, password: str, use_tls: bool = True, *args: Any, **kwargs: Any
    ) -> None:
        """Initialize QQ Email sender.

        Args:
            username: QQ Email address
            password: QQ Email authorization code (not login password)
            use_tls: Whether to use TLS encryption, defaults to True
            *args: Other positional arguments
            **kwargs: Other keyword arguments
        """
        super().__init__(username, password, use_tls, *args, **kwargs)

    def _get_default_smtp_server(self) -> str:
        """Get default SMTP server address for QQ Email.

        Returns:
            QQ Email SMTP server address
        """
        return "smtp.qq.com"

    def _get_default_smtp_port(self) -> int:
        """Get default SMTP port for QQ Email.

        Returns:
            QQ Email SMTP port number
        """
        return 587 if self.use_tls else 465


class NetEaseEmailSender(EmailSender):
    """NetEase Email sender.

    Supports NetEase's 163, 126, and yeah.net email services.
    It automatically selects the correct SMTP server based on your email address suffix.

    Important notes:
        - **Must use authorization code**: Similar to QQ Email, NetEase Email also requires using a dedicated "client authorization password" instead of your email login password.
        - **Enable SMTP service**: Please enable POP3/SMTP/IMAP service in your NetEase Email settings.
        - **SSL connection**: NetEase Email's SMTP service primarily uses SSL encryption (port 465), so the default `use_tls` is `False`.

    Examples:
        ```python
        from email_widget import Email, NetEaseEmailSender
        import os

        # Using 163 email
        user_163 = os.getenv("NETEASE_USER_163") # e.g., "my_account@163.com"
        auth_code_163 = os.getenv("NETEASE_AUTH_CODE_163")

        email = Email("Greetings from 163 Email")
        email.add_text("This is an email sent through NetEaseEmailSender.")

        sender = NetEaseEmailSender(username=user_163, password=auth_code_163)

        try:
            sender.send(email, to=["friend@example.com"])
            print("163 email sent successfully!")
        except Exception as e:
            print(f"Email sending failed: {e}")
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
        """Initialize NetEase Email sender.

        Args:
            username: NetEase Email address
            password: NetEase Email authorization code
            use_tls: Whether to use TLS encryption, defaults to False (NetEase Email uses SSL)
            *args: Other positional arguments
            **kwargs: Other keyword arguments

        Note:
            NetEase Email only supports SSL connection (port 465), recommend keeping use_tls=False.
        """
        super().__init__(username, password, use_tls, *args, **kwargs)

    def _get_default_smtp_server(self) -> str:
        """Get default SMTP server address for NetEase Email.

        Returns:
            NetEase Email SMTP server address
        """
        # Return corresponding SMTP server based on email domain
        if "@163.com" in self.username:
            return "smtp.163.com"
        elif "@126.com" in self.username:
            return "smtp.126.com"
        elif "@yeah.net" in self.username:
            return "smtp.yeah.net"
        else:
            return "smtp.163.com"  # Default to 163's server

    def _get_default_smtp_port(self) -> int:
        """Get default SMTP port for NetEase Email.

        Returns:
            NetEase Email SMTP port number

        Note:
            NetEase Email only supports SSL connection (port 465).
        """
        return 465  # NetEase Email only supports SSL port 465


class GmailEmailSender(EmailSender):
    """Gmail email sender.

    Specifically designed for sending emails through Gmail SMTP service.
    It presets the SMTP server address and recommended port for Gmail.

    Important notes:
        - **Must use App Password**: For security reasons, Gmail's SMTP service requires using an "App Password" instead of your regular Gmail password. You need to:
          1. Enable 2-Factor Authentication on your Google account
          2. Generate an App Password in Google Account settings (Security > App passwords)
        - **Less Secure App Access**: Alternatively, you can enable "Less secure app access" in Gmail settings, but App Password is the recommended approach.
        - **SMTP Service**: Gmail SMTP service is enabled by default for all accounts.

    Examples:
        ```python
        from email_widget import Email, GmailEmailSender
        import os

        # Recommend reading sensitive information from environment variables
        # export GMAIL_USER="your_account@gmail.com"
        # export GMAIL_APP_PASSWORD="your_generated_app_password"

        gmail_user = os.getenv("GMAIL_USER")
        app_password = os.getenv("GMAIL_APP_PASSWORD")

        # Create email content
        email = Email("Report from Gmail")
        email.add_text("This is a test email sent through EmailWidget via Gmail.")

        # Initialize Gmail sender
        sender = GmailEmailSender(username=gmail_user, password=app_password)

        # Send email to one or more recipients
        try:
            sender.send(email, to=["recipient1@example.com", "recipient2@example.com"])
            print("Email sent successfully!")
        except Exception as e:
            print(f"Email sending failed: {e}")
        ```

    Setup Instructions:
        1. **Enable 2-Factor Authentication**:
           - Go to Google Account settings (https://myaccount.google.com)
           - Navigate to Security > 2-Step Verification
           - Follow the setup process

        2. **Generate App Password**:
           - Go to Security > App passwords
           - Select "Mail" and your device
           - Copy the generated 16-character password (without spaces)

        3. **Use in EmailWidget**:
           - Use your full Gmail address as username
           - Use the generated App Password (not your regular password)
    """

    def __init__(
        self, username: str, password: str, use_tls: bool = True, *args: Any, **kwargs: Any
    ) -> None:
        """Initialize Gmail sender.

        Args:
            username: Gmail address (e.g., "user@gmail.com")
            password: Gmail App Password (16-character generated password)
            use_tls: Whether to use TLS encryption, defaults to True
            *args: Other positional arguments
            **kwargs: Other keyword arguments

        Note:
            Gmail supports both TLS (port 587) and SSL (port 465). TLS is recommended.
        """
        super().__init__(username, password, use_tls, *args, **kwargs)

    def _get_default_smtp_server(self) -> str:
        """Get default SMTP server address for Gmail.

        Returns:
            Gmail SMTP server address
        """
        return "smtp.gmail.com"

    def _get_default_smtp_port(self) -> int:
        """Get default SMTP port for Gmail.

        Returns:
            Gmail SMTP port number

        Note:
            Gmail supports both TLS (port 587) and SSL (port 465).
            TLS is the recommended approach.
        """
        return 587 if self.use_tls else 465


# Email provider mapping dictionary for user convenience
EMAIL_PROVIDERS: dict[str, type] = {
    "qq": QQEmailSender,
    "netease": NetEaseEmailSender,
    "163": NetEaseEmailSender,
    "126": NetEaseEmailSender,
    "gmail": GmailEmailSender,
}


def create_email_sender(
    provider: str, username: str, password: str, **kwargs: Any
) -> EmailSender:
    """Factory function to quickly create corresponding email sender instances based on provider name.

    This is a convenient helper function that allows you to avoid directly importing and instantiating specific sender classes.
    It selects the correct sender through a string identifier, particularly suitable for scenarios where the provider is specified in configuration files.

    Args:
        provider (str): Email provider identifier. Supported values (case-insensitive) include:
                      'qq', 'netease', '163', '126', 'gmail'.
        username (str): Email account, usually the complete email address.
        password (str): Email authorization code or app password.
        **kwargs: Other keyword arguments, will be passed directly to the selected sender class constructor.

    Returns:
        EmailSender: A concrete email sender instance (e.g. `QQEmailSender`).

    Raises:
        ValueError: If the provided `provider` name is not supported.

    Examples:
        ```python
        from email_widget import Email, create_email_sender
        import os

        # Read provider and credentials from config or environment variables
        email_provider = os.getenv("EMAIL_PROVIDER", "qq") # e.g., 'qq' or 'netease'
        email_user = os.getenv("EMAIL_USER")
        email_password = os.getenv("EMAIL_PASSWORD")

        # Create sender using factory function
        try:
            sender = create_email_sender(
                provider=email_provider,
                username=email_user,
                password=email_password
            )

            email = Email(f"Email from {email_provider.upper()}")
            email.add_text("Sender created through factory function.")
            sender.send(email, to=["test@example.com"])
            print("Email sent successfully!")

        except ValueError as e:
            print(f"Configuration error: {e}")
        except Exception as e:
            print(f"Sending failed: {e}")
        ```
    """
    provider_lower = provider.lower()
    if provider_lower not in EMAIL_PROVIDERS:
        supported = ", ".join(EMAIL_PROVIDERS.keys())
        raise ValueError(f"Unsupported email provider: {provider}. Supported providers: {supported}")

    sender_class = EMAIL_PROVIDERS[provider_lower]
    return sender_class(username, password, **kwargs)
