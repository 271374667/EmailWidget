"""EmailWidget面向对象验证器系统

这个模块提供了基于类的验证器系统，使用通用基类和具体子类实现.
"""

import re
from abc import ABC, abstractmethod
from typing import Any


class BaseValidator(ABC):
    """验证器基类.

    所有验证器都应该继承这个基类并实现validate方法.

    Attributes:
        error_message: 验证失败时的错误消息
    """

    def __init__(self, error_message: str | None = None):
        """初始化验证器.

        Args:
            error_message: 自定义错误消息
        """
        self.error_message = error_message or self._get_default_error_message()

    @abstractmethod
    def validate(self, value: Any) -> bool:
        """验证值是否有效.

        Args:
            value: 要验证的值

        Returns:
            验证是否通过
        """
        pass

    def _get_default_error_message(self) -> str:
        """获取默认错误消息.

        Returns:
            默认错误消息
        """
        return f"{self.__class__.__name__} 验证失败"

    def get_error_message(self, value: Any = None) -> str:
        """获取错误消息.

        Args:
            value: 验证失败的值

        Returns:
            错误消息
        """
        if value is not None:
            return f"{self.error_message}: {value}"
        return self.error_message


class ColorValidator(BaseValidator):
    """CSS颜色值验证器."""

    def _get_default_error_message(self) -> str:
        return "无效的CSS颜色值"

    def validate(self, value: Any) -> bool:
        """验证CSS颜色值.

        Args:
            value: 要验证的颜色值

        Returns:
            是否为有效颜色
        """
        if not isinstance(value, str):
            return False

        value = value.strip().lower()

        # 十六进制颜色
        if value.startswith("#") and len(value) in [4, 7]:
            hex_part = value[1:]
            return all(c in "0123456789abcdef" for c in hex_part)

        # RGB/RGBA颜色
        if value.startswith(("rgb(", "rgba(")):
            return True

        # 预定义颜色名称
        css_colors = {
            "black",
            "white",
            "red",
            "green",
            "blue",
            "yellow",
            "cyan",
            "magenta",
            "silver",
            "gray",
            "maroon",
            "olive",
            "lime",
            "aqua",
            "teal",
            "navy",
            "fuchsia",
            "purple",
        }

        return value in css_colors


class SizeValidator(BaseValidator):
    """CSS尺寸值验证器."""

    def _get_default_error_message(self) -> str:
        return "无效的CSS尺寸值"

    def validate(self, value: Any) -> bool:
        """验证CSS尺寸值.

        Args:
            value: 要验证的尺寸值

        Returns:
            是否为有效尺寸
        """
        if not isinstance(value, str):
            return False

        value = value.strip().lower()

        # 数字 + 单位
        size_units = ["px", "em", "rem", "%", "pt", "pc", "in", "cm", "mm"]

        for unit in size_units:
            if value.endswith(unit):
                number_part = value[: -len(unit)]
                try:
                    float(number_part)
                    return True
                except ValueError:
                    continue

        # 纯数字（默认px）
        try:
            float(value)
            return True
        except ValueError:
            return False


class RangeValidator(BaseValidator):
    """数值范围验证器."""

    def __init__(
        self,
        min_value: int | float,
        max_value: int | float,
        error_message: str | None = None,
    ):
        """初始化范围验证器.

        Args:
            min_value: 最小值
            max_value: 最大值
            error_message: 自定义错误消息
        """
        self.min_value = min_value
        self.max_value = max_value
        super().__init__(error_message)

    def _get_default_error_message(self) -> str:
        return f"值必须在 {self.min_value} 到 {self.max_value} 之间"

    def validate(self, value: Any) -> bool:
        """验证数值是否在指定范围内.

        Args:
            value: 要验证的数值

        Returns:
            是否在范围内
        """
        if not isinstance(value, (int, float)):
            return False

        return self.min_value <= value <= self.max_value


class ProgressValidator(RangeValidator):
    """进度值验证器（0-100）."""

    def __init__(self, error_message: str | None = None):
        super().__init__(0, 100, error_message)

    def _get_default_error_message(self) -> str:
        return "进度值必须在 0 到 100 之间"


class UrlValidator(BaseValidator):
    """URL格式验证器."""

    def _get_default_error_message(self) -> str:
        return "无效的URL格式"

    def validate(self, value: Any) -> bool:
        """验证URL格式.

        Args:
            value: 要验证的URL

        Returns:
            是否为有效URL
        """
        if not isinstance(value, str):
            return False

        url_pattern = re.compile(
            r"^https?://"  # http:// or https://
            r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|"  # domain...
            r"localhost|"  # localhost...
            r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
            r"(?::\d+)?"  # optional port
            r"(?:/?|[/?]\S+)$",
            re.IGNORECASE,
        )

        return bool(url_pattern.match(value))


class EmailValidator(BaseValidator):
    """邮箱地址验证器."""

    def _get_default_error_message(self) -> str:
        return "无效的邮箱地址格式"

    def validate(self, value: Any) -> bool:
        """验证邮箱地址格式.

        Args:
            value: 要验证的邮箱地址

        Returns:
            是否为有效邮箱
        """
        if not isinstance(value, str):
            return False

        email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

        return bool(email_pattern.match(value))


class NonEmptyStringValidator(BaseValidator):
    """非空字符串验证器."""

    def _get_default_error_message(self) -> str:
        return "字符串不能为空"

    def validate(self, value: Any) -> bool:
        """验证字符串是否非空.

        Args:
            value: 要验证的字符串

        Returns:
            是否为非空字符串
        """
        return isinstance(value, str) and len(value.strip()) > 0


class LengthValidator(BaseValidator):
    """字符串长度验证器."""

    def __init__(
        self,
        min_length: int = 0,
        max_length: int | None = None,
        error_message: str | None = None,
    ):
        """初始化长度验证器.

        Args:
            min_length: 最小长度
            max_length: 最大长度，None表示无限制
            error_message: 自定义错误消息
        """
        self.min_length = min_length
        self.max_length = max_length
        super().__init__(error_message)

    def _get_default_error_message(self) -> str:
        if self.max_length is not None:
            return f"长度必须在 {self.min_length} 到 {self.max_length} 之间"
        else:
            return f"长度必须至少 {self.min_length}"

    def validate(self, value: Any) -> bool:
        """验证字符串长度.

        Args:
            value: 要验证的字符串

        Returns:
            长度是否符合要求
        """
        if not hasattr(value, "__len__"):
            return False

        length = len(value)

        if length < self.min_length:
            return False

        if self.max_length is not None and length > self.max_length:
            return False

        return True


class TypeValidator(BaseValidator):
    """类型验证器."""

    def __init__(self, expected_type: type | tuple, error_message: str | None = None):
        """初始化类型验证器.

        Args:
            expected_type: 期望的类型或类型元组
            error_message: 自定义错误消息
        """
        self.expected_type = expected_type
        super().__init__(error_message)

    def _get_default_error_message(self) -> str:
        if isinstance(self.expected_type, tuple):
            type_names = [t.__name__ for t in self.expected_type]
            return f"类型必须是 {' 或 '.join(type_names)} 之一"
        else:
            return f"类型必须是 {self.expected_type.__name__}"

    def validate(self, value: Any) -> bool:
        """验证值的类型.

        Args:
            value: 要验证的值

        Returns:
            类型是否匹配
        """
        return isinstance(value, self.expected_type)


class ChoicesValidator(BaseValidator):
    """选项验证器."""

    def __init__(self, choices: list[Any], error_message: str | None = None):
        """初始化选项验证器.

        Args:
            choices: 允许的选项列表
            error_message: 自定义错误消息
        """
        self.choices = choices
        super().__init__(error_message)

    def _get_default_error_message(self) -> str:
        return f"值必须是以下选项之一: {self.choices}"

    def validate(self, value: Any) -> bool:
        """验证值是否在允许的选项中.

        Args:
            value: 要验证的值

        Returns:
            是否在允许的选项中
        """
        return value in self.choices


class CompositeValidator(BaseValidator):
    """组合验证器，可以组合多个验证器."""

    def __init__(
        self,
        validators: list[BaseValidator],
        require_all: bool = True,
        error_message: str | None = None,
    ):
        """初始化组合验证器.

        Args:
            validators: 验证器列表
            require_all: 是否要求所有验证器都通过，False表示只要有一个通过即可
            error_message: 自定义错误消息
        """
        self.validators = validators
        self.require_all = require_all
        super().__init__(error_message)

    def _get_default_error_message(self) -> str:
        if self.require_all:
            return "必须通过所有验证条件"
        else:
            return "必须通过至少一个验证条件"

    def validate(self, value: Any) -> bool:
        """验证值是否通过组合条件.

        Args:
            value: 要验证的值

        Returns:
            是否通过验证
        """
        results = [validator.validate(value) for validator in self.validators]

        if self.require_all:
            return all(results)
        else:
            return any(results)

    def get_failed_validators(self, value: Any) -> list[BaseValidator]:
        """获取验证失败的验证器列表.

        Args:
            value: 验证的值

        Returns:
            失败的验证器列表
        """
        failed = []
        for validator in self.validators:
            if not validator.validate(value):
                failed.append(validator)
        return failed


# 预定义的常用验证器实例
color_validator = ColorValidator()
size_validator = SizeValidator()
progress_validator = ProgressValidator()
url_validator = UrlValidator()
email_validator = EmailValidator()
non_empty_string_validator = NonEmptyStringValidator()

# 常用的类型验证器
string_validator = TypeValidator(str)
int_validator = TypeValidator(int)
float_validator = TypeValidator(float)
number_validator = TypeValidator((int, float))
bool_validator = TypeValidator(bool)
list_validator = TypeValidator(list)
dict_validator = TypeValidator(dict)
