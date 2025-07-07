"""Validators测试用例"""

import pytest

from email_widget.core.validators import (
    BaseValidator,
    ChoicesValidator,
    ColorValidator,
    CompositeValidator,
    EmailValidator,
    LengthValidator,
    NonEmptyStringValidator,
    ProgressValidator,
    RangeValidator,
    SizeValidator,
    TypeValidator,
    UrlValidator,
)


class MockValidator(BaseValidator):
    """模拟验证器用于测试基类"""

    def __init__(self, should_pass=True, error_message=None):
        self.should_pass = should_pass
        super().__init__(error_message)

    def validate(self, value):
        return self.should_pass


class TestBaseValidator:
    """BaseValidator测试类"""

    def test_init_default_error_message(self):
        """测试默认错误消息"""
        validator = MockValidator()
        assert "MockValidator 验证失败" in validator.error_message

    def test_init_custom_error_message(self):
        """测试自定义错误消息"""
        custom_message = "自定义错误消息"
        validator = MockValidator(error_message=custom_message)
        assert validator.error_message == custom_message

    def test_get_error_message_with_value(self):
        """测试带值的错误消息"""
        validator = MockValidator(error_message="测试错误")
        message = validator.get_error_message("test_value")
        assert message == "测试错误: test_value"

    def test_get_error_message_without_value(self):
        """测试不带值的错误消息"""
        validator = MockValidator(error_message="测试错误")
        message = validator.get_error_message()
        assert message == "测试错误"


class TestColorValidator:
    """ColorValidator测试类"""

    def setup_method(self):
        """每个测试方法执行前的设置"""
        self.validator = ColorValidator()

    @pytest.mark.parametrize(
        "color,expected",
        [
            ("#ff0000", True),
            ("#FF0000", True),
            ("#f00", True),
            ("#F00", True),
            ("red", True),
            ("blue", True),
            ("green", True),
            ("yellow", True),
            ("white", True),
            ("black", True),
            ("rgb(255,0,0)", True),
            ("rgba(255,0,0,0.5)", True),
            ("RGB(255,0,0)", True),
            ("RGBA(255,0,0,0.5)", True),
            ("invalid_color", False),
            ("#gggggg", False),
            ("#ff", False),
            ("", False),
            (123, False),
            (None, False),
        ],
    )
    def test_validate_colors(self, color, expected):
        """测试颜色验证"""
        assert self.validator.validate(color) == expected

    def test_default_error_message(self):
        """测试默认错误消息"""
        assert self.validator.error_message == "无效的CSS颜色值"


class TestSizeValidator:
    """SizeValidator测试类"""

    def setup_method(self):
        """每个测试方法执行前的设置"""
        self.validator = SizeValidator()

    @pytest.mark.parametrize(
        "size,expected",
        [
            ("10px", True),
            ("1.5em", True),
            ("100%", True),
            ("2rem", True),
            ("12pt", True),
            ("1cm", True),
            ("10mm", True),
            ("15", True),  # 纯数字
            ("0", True),
            ("-5px", True),  # 负值也被认为有效
            ("invalid_size", False),
            ("px", False),
            ("", False),
            (123, False),
            (None, False),
        ],
    )
    def test_validate_sizes(self, size, expected):
        """测试尺寸验证"""
        assert self.validator.validate(size) == expected

    def test_default_error_message(self):
        """测试默认错误消息"""
        assert self.validator.error_message == "无效的CSS尺寸值"


class TestRangeValidator:
    """RangeValidator测试类"""

    def setup_method(self):
        """每个测试方法执行前的设置"""
        self.validator = RangeValidator(0, 100)

    @pytest.mark.parametrize(
        "value,expected",
        [
            (0, True),
            (50, True),
            (100, True),
            (-1, False),
            (101, False),
            (50.5, True),
            ("50", False),  # 字符串不通过
            (None, False),
        ],
    )
    def test_validate_range(self, value, expected):
        """测试范围验证"""
        assert self.validator.validate(value) == expected

    def test_custom_range(self):
        """测试自定义范围"""
        validator = RangeValidator(-10, 10)
        assert validator.validate(-10) is True
        assert validator.validate(0) is True
        assert validator.validate(10) is True
        assert validator.validate(-11) is False
        assert validator.validate(11) is False

    def test_default_error_message(self):
        """测试默认错误消息"""
        assert "值必须在 0 到 100 之间" in self.validator.error_message


class TestProgressValidator:
    """ProgressValidator测试类"""

    def setup_method(self):
        """每个测试方法执行前的设置"""
        self.validator = ProgressValidator()

    @pytest.mark.parametrize(
        "value,expected",
        [
            (0, True),
            (50, True),
            (100, True),
            (-1, False),
            (101, False),
            (50.5, True),
        ],
    )
    def test_validate_progress(self, value, expected):
        """测试进度值验证"""
        assert self.validator.validate(value) == expected

    def test_default_error_message(self):
        """测试默认错误消息"""
        assert "进度值必须在 0 到 100 之间" in self.validator.error_message


class TestUrlValidator:
    """UrlValidator测试类"""

    def setup_method(self):
        """每个测试方法执行前的设置"""
        self.validator = UrlValidator()

    @pytest.mark.parametrize(
        "url,expected",
        [
            ("http://example.com", True),
            ("https://example.com", True),
            ("http://localhost", True),
            ("https://subdomain.example.com", True),
            ("http://192.168.1.1", True),
            ("https://example.com:8080", True),
            ("http://example.com/path", True),
            ("https://example.com/path?query=value", True),
            ("ftp://example.com", False),  # 不支持ftp
            ("example.com", False),  # 缺少协议
            ("http://", False),  # 不完整的URL
            ("invalid_url", False),
            ("", False),
            (123, False),
            (None, False),
        ],
    )
    def test_validate_urls(self, url, expected):
        """测试URL验证"""
        assert self.validator.validate(url) == expected

    def test_default_error_message(self):
        """测试默认错误消息"""
        assert self.validator.error_message == "无效的URL格式"


class TestEmailValidator:
    """EmailValidator测试类"""

    def setup_method(self):
        """每个测试方法执行前的设置"""
        self.validator = EmailValidator()

    @pytest.mark.parametrize(
        "email,expected",
        [
            ("test@example.com", True),
            ("user.name@domain.co.uk", True),
            ("user+tag@example.org", True),
            ("123@example.com", True),
            ("user@localhost", False),  # 不支持localhost
            ("user@", False),
            ("@example.com", False),
            ("user.example.com", False),  # 缺少@
            ("user@example", False),  # 缺少域名后缀
            ("", False),
            (123, False),
            (None, False),
        ],
    )
    def test_validate_emails(self, email, expected):
        """测试邮箱验证"""
        assert self.validator.validate(email) == expected

    def test_default_error_message(self):
        """测试默认错误消息"""
        assert self.validator.error_message == "无效的邮箱地址格式"


class TestNonEmptyStringValidator:
    """NonEmptyStringValidator测试类"""

    def setup_method(self):
        """每个测试方法执行前的设置"""
        self.validator = NonEmptyStringValidator()

    @pytest.mark.parametrize(
        "value,expected",
        [
            ("hello", True),
            ("  hello  ", True),  # 两端有空格但内容非空
            ("", False),
            ("   ", False),  # 只有空格
            ("\n\t", False),  # 只有空白字符
            (123, False),  # 非字符串
            (None, False),
            ([], False),
        ],
    )
    def test_validate_non_empty_strings(self, value, expected):
        """测试非空字符串验证"""
        assert self.validator.validate(value) == expected

    def test_default_error_message(self):
        """测试默认错误消息"""
        assert self.validator.error_message == "字符串不能为空"


class TestLengthValidator:
    """LengthValidator测试类"""

    def test_min_length_only(self):
        """测试只设置最小长度"""
        validator = LengthValidator(min_length=3)
        assert validator.validate("abc") is True
        assert validator.validate("abcd") is True
        assert validator.validate("ab") is False
        assert validator.validate([1, 2, 3]) is True  # 测试列表
        assert validator.validate(123) is False  # 没有长度属性

    def test_min_max_length(self):
        """测试设置最小和最大长度"""
        validator = LengthValidator(min_length=3, max_length=5)
        assert validator.validate("abc") is True
        assert validator.validate("abcd") is True
        assert validator.validate("abcde") is True
        assert validator.validate("ab") is False
        assert validator.validate("abcdef") is False

    def test_zero_min_length(self):
        """测试最小长度为0"""
        validator = LengthValidator(min_length=0, max_length=3)
        assert validator.validate("") is True
        assert validator.validate("abc") is True
        assert validator.validate("abcd") is False

    def test_error_messages(self):
        """测试错误消息"""
        validator1 = LengthValidator(min_length=3)
        assert "长度必须至少 3" in validator1.error_message

        validator2 = LengthValidator(min_length=3, max_length=10)
        assert "长度必须在 3 到 10 之间" in validator2.error_message


class TestTypeValidator:
    """TypeValidator测试类"""

    def test_single_type(self):
        """测试单一类型验证"""
        validator = TypeValidator(str)
        assert validator.validate("hello") is True
        assert validator.validate(123) is False
        assert validator.validate([]) is False

    def test_multiple_types(self):
        """测试多类型验证"""
        validator = TypeValidator((str, int))
        assert validator.validate("hello") is True
        assert validator.validate(123) is True
        assert validator.validate(12.5) is False
        assert validator.validate([]) is False

    def test_error_message_single_type(self):
        """测试单类型错误消息"""
        validator = TypeValidator(str)
        assert "类型必须是 str" in validator.error_message

    def test_error_message_multiple_types(self):
        """测试多类型错误消息"""
        validator = TypeValidator((str, int))
        assert "类型必须是 str 或 int 之一" in validator.error_message


class TestChoicesValidator:
    """ChoicesValidator测试类"""

    def setup_method(self):
        """每个测试方法执行前的设置"""
        self.validator = ChoicesValidator(["red", "green", "blue"])

    @pytest.mark.parametrize(
        "value,expected",
        [
            ("red", True),
            ("green", True),
            ("blue", True),
            ("yellow", False),
            ("", False),
            (123, False),
        ],
    )
    def test_validate_choices(self, value, expected):
        """测试选项验证"""
        assert self.validator.validate(value) == expected

    def test_mixed_type_choices(self):
        """测试混合类型选项"""
        validator = ChoicesValidator([1, "two", 3.0])
        assert validator.validate(1) is True
        assert validator.validate("two") is True
        assert validator.validate(3.0) is True
        assert validator.validate(2) is False
        assert validator.validate("three") is False

    def test_error_message(self):
        """测试错误消息"""
        assert (
            "值必须是以下选项之一: ['red', 'green', 'blue']"
            in self.validator.error_message
        )


class TestCompositeValidator:
    """CompositeValidator测试类"""

    def test_require_all_true(self):
        """测试要求所有验证器都通过"""
        validator1 = MockValidator(should_pass=True)
        validator2 = MockValidator(should_pass=True)
        composite = CompositeValidator([validator1, validator2], require_all=True)

        assert composite.validate("test") is True

    def test_require_all_false_one_fails(self):
        """测试要求所有验证器都通过，但有一个失败"""
        validator1 = MockValidator(should_pass=True)
        validator2 = MockValidator(should_pass=False)
        composite = CompositeValidator([validator1, validator2], require_all=True)

        assert composite.validate("test") is False

    def test_require_any_true(self):
        """测试只要有一个验证器通过"""
        validator1 = MockValidator(should_pass=True)
        validator2 = MockValidator(should_pass=False)
        composite = CompositeValidator([validator1, validator2], require_all=False)

        assert composite.validate("test") is True

    def test_require_any_false_all_fail(self):
        """测试只要有一个验证器通过，但全部失败"""
        validator1 = MockValidator(should_pass=False)
        validator2 = MockValidator(should_pass=False)
        composite = CompositeValidator([validator1, validator2], require_all=False)

        assert composite.validate("test") is False

    def test_get_failed_validators(self):
        """测试获取失败的验证器"""
        validator1 = MockValidator(should_pass=True)
        validator2 = MockValidator(should_pass=False)
        validator3 = MockValidator(should_pass=False)
        composite = CompositeValidator([validator1, validator2, validator3])

        failed = composite.get_failed_validators("test")
        assert len(failed) == 2
        assert validator2 in failed
        assert validator3 in failed
        assert validator1 not in failed

    def test_error_messages(self):
        """测试错误消息"""
        validator1 = MockValidator(should_pass=True)
        validator2 = MockValidator(should_pass=True)

        composite_all = CompositeValidator([validator1, validator2], require_all=True)
        assert "必须通过所有验证条件" in composite_all.error_message

        composite_any = CompositeValidator([validator1, validator2], require_all=False)
        assert "必须通过至少一个验证条件" in composite_any.error_message


class TestPredefinedValidators:
    """测试预定义的验证器实例"""

    def test_predefined_validators_exist(self):
        """测试预定义验证器实例存在"""
        from email_widget.core.validators import (
            bool_validator,
            color_validator,
            dict_validator,
            email_validator,
            float_validator,
            int_validator,
            list_validator,
            non_empty_string_validator,
            number_validator,
            progress_validator,
            size_validator,
            string_validator,
            url_validator,
        )

        # 测试预定义实例不为None
        assert color_validator is not None
        assert size_validator is not None
        assert progress_validator is not None
        assert url_validator is not None
        assert email_validator is not None
        assert non_empty_string_validator is not None
        assert string_validator is not None
        assert int_validator is not None
        assert float_validator is not None
        assert number_validator is not None
        assert bool_validator is not None
        assert list_validator is not None
        assert dict_validator is not None

    def test_predefined_validators_functionality(self):
        """测试预定义验证器的功能"""
        from email_widget.core.validators import (
            color_validator,
            number_validator,
            string_validator,
        )

        # 测试颜色验证器
        assert color_validator.validate("#ff0000") is True
        assert color_validator.validate("invalid") is False

        # 测试字符串验证器
        assert string_validator.validate("hello") is True
        assert string_validator.validate(123) is False

        # 测试数字验证器
        assert number_validator.validate(123) is True
        assert number_validator.validate(12.5) is True
        assert number_validator.validate("123") is False
