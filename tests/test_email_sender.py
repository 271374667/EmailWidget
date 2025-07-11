"""EmailSender组件的完整测试套件。

测试覆盖：
- 邮件发送器抽象接口
- 具体邮箱服务商实现
- SMTP连接管理
- 邮件发送功能
- 错误处理
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from unittest.mock import Mock, patch

import pytest

from email_widget.email_sender import (
    EmailSender,
    NetEaseEmailSender,
    QQEmailSender,
    create_email_sender,
)


# 创建Mock Email类用于测试
class MockEmail:
    def __init__(self, title="Test Email"):
        self.title = title

    def export_str(self):
        return f"<html><body><h1>{self.title}</h1></body></html>"


class TestEmailSenderBase:
    """EmailSender抽象基类测试"""

    def test_abstract_base_class(self):
        """测试抽象基类不能直接实例化"""
        with pytest.raises(TypeError):
            EmailSender("test@example.com", "password")

    def test_subclass_must_implement_methods(self):
        """测试子类必须实现抽象方法"""

        class IncompleteEmailSender(EmailSender):
            pass

        with pytest.raises(TypeError):
            IncompleteEmailSender("test@example.com", "password")

    def test_valid_subclass_implementation(self):
        """测试有效子类实现"""

        class ValidEmailSender(EmailSender):
            def _get_default_smtp_server(self):
                return "smtp.example.com"

            def _get_default_smtp_port(self):
                return 587

        sender = ValidEmailSender("test@example.com", "password")
        assert sender.username == "test@example.com"
        assert sender.password == "password"
        assert sender.smtp_server == "smtp.example.com"
        assert sender.smtp_port == 587


class TestQQEmailSender:
    """QQ邮箱发送器测试"""

    def test_init(self):
        """测试QQ发送器初始化"""
        sender = QQEmailSender("test@qq.com", "password123")
        assert sender.username == "test@qq.com"
        assert sender.password == "password123"

    def test_smtp_configuration(self):
        """测试SMTP配置"""
        sender = QQEmailSender("test@qq.com", "password123")
        assert sender._get_default_smtp_server() == "smtp.qq.com"
        assert sender._get_default_smtp_port() == 587

    @patch("smtplib.SMTP")
    def test_send_email_success(self, mock_smtp):
        """测试成功发送邮件"""
        mock_server = Mock()
        mock_smtp.return_value = mock_server

        sender = QQEmailSender("test@qq.com", "password123")
        email = MockEmail("QQ测试邮件")

        # 发送邮件
        sender.send(email, to=["recipient@example.com"])

        # 验证SMTP调用
        mock_smtp.assert_called_once_with("smtp.qq.com", 587)
        mock_server.starttls.assert_called_once()
        mock_server.login.assert_called_once_with("test@qq.com", "password123")
        mock_server.send_message.assert_called_once()

    @patch("smtplib.SMTP")
    def test_send_email_smtp_exception(self, mock_smtp):
        """测试SMTP异常处理"""
        mock_smtp.side_effect = smtplib.SMTPConnectError(421, "连接失败")

        sender = QQEmailSender("test@qq.com", "password123")
        email = MockEmail("异常测试")

        with pytest.raises(smtplib.SMTPException):
            sender.send(email, to=["recipient@example.com"])

    @patch("smtplib.SMTP")
    def test_send_email_auth_exception(self, mock_smtp):
        """测试认证异常处理"""
        mock_server = Mock()
        mock_smtp.return_value = mock_server
        mock_server.login.side_effect = smtplib.SMTPAuthenticationError(535, "认证失败")

        sender = QQEmailSender("test@qq.com", "wrong_password")
        email = MockEmail("认证测试")

        with pytest.raises(smtplib.SMTPException):
            sender.send(email, to=["recipient@example.com"])

    @patch("smtplib.SMTP")
    def test_send_email_with_multiple_recipients(self, mock_smtp):
        """测试多收件人邮件发送"""
        mock_server = Mock()
        mock_smtp.return_value = mock_server

        sender = QQEmailSender("test@qq.com", "password123")
        email = MockEmail("多收件人测试")
        recipients = ["user1@example.com", "user2@example.com", "user3@example.com"]

        sender.send(email, to=recipients)

        mock_server.send_message.assert_called_once()

    @patch("smtplib.SMTP")
    def test_send_email_empty_subject_and_body(self, mock_smtp):
        """测试空主题和内容"""
        mock_server = Mock()
        mock_smtp.return_value = mock_server

        sender = QQEmailSender("test@qq.com", "password123")
        email = MockEmail("")  # 空标题

        sender.send(email, to=["recipient@example.com"])

        mock_server.send_message.assert_called_once()


class TestNetEaseEmailSender:
    """网易邮箱发送器测试"""

    def test_init(self):
        """测试网易发送器初始化"""
        sender = NetEaseEmailSender("test@163.com", "password")
        assert sender.username == "test@163.com"
        assert sender.password == "password"

    def test_smtp_configuration(self):
        """测试SMTP配置"""
        sender = NetEaseEmailSender("test@163.com", "password")
        assert sender._get_default_smtp_server() == "smtp.163.com"
        assert sender._get_default_smtp_port() == 465

    @patch("smtplib.SMTP_SSL")
    def test_send_email_success(self, mock_smtp_ssl):
        """测试成功发送邮件"""
        mock_server = Mock()
        mock_smtp_ssl.return_value = mock_server

        sender = NetEaseEmailSender("test@163.com", "password")
        email = MockEmail("网易测试邮件")

        sender.send(email, to=["recipient@example.com"])

        # NetEaseEmailSender使用SSL，不使用TLS
        mock_smtp_ssl.assert_called_once_with("smtp.163.com", 465)
        mock_server.login.assert_called_once_with("test@163.com", "password")

    def test_126_email_domain(self):
        """测试126邮箱域名"""
        sender = NetEaseEmailSender("test@126.com", "password")
        assert sender.username == "test@126.com"
        assert sender._get_default_smtp_server() == "smtp.126.com"


class TestCreateEmailSender:
    """工厂函数测试"""

    def test_create_qq_sender(self):
        """测试创建QQ邮箱发送器"""
        sender = create_email_sender("qq", "test@qq.com", "password")
        assert isinstance(sender, QQEmailSender)
        assert sender.username == "test@qq.com"
        assert sender.password == "password"

    def test_create_netease_sender(self):
        """测试创建网易邮箱发送器"""
        sender = create_email_sender("netease", "test@163.com", "password")
        assert isinstance(sender, NetEaseEmailSender)
        assert sender.username == "test@163.com"
        assert sender.password == "password"

    def test_create_163_sender(self):
        """测试创建163邮箱发送器"""
        sender = create_email_sender("163", "test@163.com", "password")
        assert isinstance(sender, NetEaseEmailSender)
        assert sender.username == "test@163.com"
        assert sender.password == "password"

    def test_create_126_sender(self):
        """测试创建126邮箱发送器"""
        sender = create_email_sender("126", "test@126.com", "password")
        assert isinstance(sender, NetEaseEmailSender)
        assert sender.username == "test@126.com"
        assert sender.password == "password"

    def test_create_sender_case_insensitive(self):
        """测试工厂函数大小写不敏感"""
        sender = create_email_sender("QQ", "test@qq.com", "password")
        assert isinstance(sender, QQEmailSender)

        sender = create_email_sender("NetEase", "test@163.com", "password")
        assert isinstance(sender, NetEaseEmailSender)

    def test_create_sender_unsupported_provider(self):
        """测试不支持的邮箱服务商"""
        with pytest.raises(ValueError) as exc_info:
            create_email_sender("gmail", "test@gmail.com", "password")
        assert "不支持的邮箱服务商" in str(exc_info.value)

        with pytest.raises(ValueError) as exc_info:
            create_email_sender("outlook", "test@outlook.com", "password")
        assert "不支持的邮箱服务商" in str(exc_info.value)

    def test_create_sender_with_kwargs(self):
        """测试工厂函数传递额外参数"""
        sender = create_email_sender(
            "qq",
            "test@qq.com",
            "password",
            use_tls=False,
            smtp_server="custom.smtp.com",
        )
        assert isinstance(sender, QQEmailSender)
        assert sender.use_tls == False
        assert sender.smtp_server == "custom.smtp.com"


class TestEmailMessageCreation:
    """邮件消息创建测试"""

    def test_create_message_single_recipient(self):
        """测试创建单收件人邮件"""
        sender = QQEmailSender("sender@qq.com", "password")
        email = MockEmail("单收件人测试")

        msg = sender._create_message(email, to=["recipient@example.com"])

        assert isinstance(msg, MIMEMultipart)
        assert msg["From"] == "sender@qq.com"
        assert msg["To"] == "recipient@example.com"

    def test_create_message_multiple_recipients(self):
        """测试创建多收件人邮件"""
        sender = QQEmailSender("sender@qq.com", "password")
        email = MockEmail("多收件人测试")
        recipients = ["user1@example.com", "user2@example.com", "user3@example.com"]

        msg = sender._create_message(email, to=recipients)

        assert msg["To"] == ", ".join(recipients)

    def test_message_encoding_utf8(self):
        """测试消息UTF-8编码"""
        sender = QQEmailSender("sender@qq.com", "password")
        email = MockEmail("中文主题测试")

        msg = sender._create_message(email, to=["recipient@example.com"])

        # 验证主题包含中文字符
        assert "中文主题测试" in str(msg["Subject"])

    def test_message_with_special_characters(self):
        """测试包含特殊字符的邮件"""
        sender = QQEmailSender("sender@qq.com", "password")
        email = MockEmail("Special chars: <>&\"'")

        msg = sender._create_message(email, to=["recipient@example.com"])

        # 应该能正常创建消息
        assert msg is not None


class TestEmailSenderErrorHandling:
    """邮件发送器错误处理测试"""

    @patch("smtplib.SMTP")
    def test_connection_timeout(self, mock_smtp):
        """测试连接超时"""
        mock_smtp.side_effect = smtplib.SMTPConnectError(421, "连接超时")

        sender = QQEmailSender("test@qq.com", "password")
        email = MockEmail("超时测试")

        with pytest.raises(smtplib.SMTPException):
            sender.send(email, to=["recipient@example.com"])

    @patch("smtplib.SMTP")
    def test_server_not_ready(self, mock_smtp):
        """测试服务器未就绪"""
        mock_server = Mock()
        mock_smtp.return_value = mock_server
        mock_server.starttls.side_effect = smtplib.SMTPServerDisconnected("服务器断开")

        sender = QQEmailSender("test@qq.com", "password")
        email = MockEmail("服务器测试")

        with pytest.raises(Exception):
            sender.send(email, to=["recipient@example.com"])

    @patch("smtplib.SMTP")
    def test_message_too_large(self, mock_smtp):
        """测试消息过大"""
        mock_server = Mock()
        mock_smtp.return_value = mock_server
        mock_server.send_message.side_effect = smtplib.SMTPDataError(552, "消息过大")

        sender = QQEmailSender("test@qq.com", "password")
        email = MockEmail("大消息测试")

        with pytest.raises(smtplib.SMTPException):
            sender.send(email, to=["recipient@example.com"])

    @patch("smtplib.SMTP")
    def test_general_exception(self, mock_smtp):
        """测试一般异常"""
        mock_server = Mock()
        mock_smtp.return_value = mock_server
        mock_server.login.side_effect = Exception("未知错误")

        sender = QQEmailSender("test@qq.com", "password")
        email = MockEmail("异常测试")

        with pytest.raises(Exception):
            sender.send(email, to=["recipient@example.com"])

    @patch("smtplib.SMTP")
    def test_quit_exception_ignored(self, mock_smtp):
        """测试quit异常被忽略"""
        mock_server = Mock()
        mock_smtp.return_value = mock_server
        mock_server.quit.side_effect = Exception("quit失败")

        sender = QQEmailSender("test@qq.com", "password")
        email = MockEmail("quit测试")

        # 应该不抛出异常，quit错误被忽略
        sender.send(email, to=["recipient@example.com"])


class TestEmailSenderIntegration:
    """邮件发送器集成测试"""

    def test_all_senders_have_correct_interface(self):
        """测试所有发送器有正确接口"""
        senders = [
            QQEmailSender("test@qq.com", "password"),
            NetEaseEmailSender("test@163.com", "password"),
        ]

        for sender in senders:
            # 验证所有发送器都有必要的方法
            assert hasattr(sender, "_get_default_smtp_server")
            assert hasattr(sender, "_get_default_smtp_port")
            assert hasattr(sender, "send")
            assert hasattr(sender, "_create_message")
            assert hasattr(sender, "_send_message")

    @patch("smtplib.SMTP")
    @patch("smtplib.SMTP_SSL")
    def test_different_senders_same_workflow(self, mock_smtp_ssl, mock_smtp):
        """测试不同发送器相同工作流"""
        mock_server = Mock()
        mock_smtp.return_value = mock_server
        mock_smtp_ssl.return_value = mock_server

        senders_configs = [
            (QQEmailSender, "test@qq.com"),
            (NetEaseEmailSender, "test@163.com"),
        ]

        for sender_class, email_addr in senders_configs:
            sender = sender_class(email_addr, "password")
            email = MockEmail(f"{sender_class.__name__}测试")

            # 所有发送器都应该能正常发送
            sender.send(email, to=["recipient@example.com"])

    def test_sender_configuration_validation(self):
        """测试发送器配置验证"""
        # 测试空用户名或密码
        with pytest.raises(ValueError):
            QQEmailSender("", "password")

        with pytest.raises(ValueError):
            QQEmailSender("test@qq.com", "")

        with pytest.raises(ValueError):
            NetEaseEmailSender(None, "password")


class TestEmailSenderEdgeCases:
    """邮件发送器边界情况测试"""

    def test_empty_email_password(self):
        """测试空邮箱和密码"""
        with pytest.raises(ValueError):
            QQEmailSender("", "")

    def test_none_email_password(self):
        """测试None邮箱和密码"""
        with pytest.raises(ValueError):
            QQEmailSender(None, None)

    @patch("smtplib.SMTP")
    def test_none_recipient(self, mock_smtp):
        """测试None收件人"""
        mock_server = Mock()
        mock_smtp.return_value = mock_server

        sender = QQEmailSender("test@qq.com", "password")
        email = MockEmail("None收件人测试")

        # 传递None作为收件人，应该使用发送者作为收件人
        sender.send(email, to=None)

        mock_server.send_message.assert_called_once()

    @patch("smtplib.SMTP")
    def test_empty_recipient_list(self, mock_smtp):
        """测试空收件人列表"""
        mock_server = Mock()
        mock_smtp.return_value = mock_server

        sender = QQEmailSender("test@qq.com", "password")
        email = MockEmail("空收件人测试")

        # 传递空列表，应该使用发送者作为收件人
        sender.send(email, to=[])

        mock_server.send_message.assert_called_once()

    def test_very_long_subject(self):
        """测试很长的主题"""
        sender = QQEmailSender("test@qq.com", "password")
        long_subject = "很长的主题" * 100  # 创建很长的主题
        email = MockEmail(long_subject)

        msg = sender._create_message(email, to=["recipient@example.com"])

        # 应该能正常创建消息
        assert msg is not None

    def test_html_body_with_complex_structure(self):
        """测试复杂HTML结构"""
        sender = QQEmailSender("test@qq.com", "password")

        # 创建一个包含复杂HTML的邮件对象
        class ComplexEmail:
            def __init__(self):
                self.title = "复杂HTML测试"

            def export_str(self):
                return """
                <html>
                <head><style>body{color:red;}</style></head>
                <body>
                    <div class="container">
                        <table border="1">
                            <tr><td>Cell 1</td><td>Cell 2</td></tr>
                        </table>
                        <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8/5+hHgAHggJ/PchI7wAAAABJRU5ErkJggg==" />
                    </div>
                </body>
                </html>
                """

        email = ComplexEmail()
        msg = sender._create_message(email, to=["recipient@example.com"])

        # 应该能正常创建消息
        assert msg is not None
