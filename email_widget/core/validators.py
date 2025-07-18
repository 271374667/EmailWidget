"""EmailWidget object-oriented validator system

This module provides a class-based validator system using generic base classes and concrete subclass implementations.
"""

import re
from abc import ABC, abstractmethod
from typing import Any


class BaseValidator(ABC):
    """Validator base class.

    All validators should inherit from this base class and implement the validate method.

    Attributes:
        error_message: Error message when validation fails
    """

    def __init__(self, error_message: str | None = None):
        """Initialize validator.

        Args:
            error_message: Custom error message
        """
        self.error_message = error_message or self._get_default_error_message()

    @abstractmethod
    def validate(self, value: Any) -> bool:
        """Validate whether value is valid.

        Args:
            value: Value to validate

        Returns:
            Whether validation passes
        """
        pass

    def _get_default_error_message(self) -> str:
        """Get default error message.

        Returns:
            Default error message
        """
        return f"{self.__class__.__name__} validation failed"

    def get_error_message(self, value: Any = None) -> str:
        """Get error message.

        Args:
            value: Value that failed validation

        Returns:
            Error message
        """
        if value is not None:
            return f"{self.error_message}: {value}"
        return self.error_message


class ColorValidator(BaseValidator):
    """CSS color value validator."""

    def _get_default_error_message(self) -> str:
        return "Invalid CSS color value"

    def validate(self, value: Any) -> bool:
        """Validate CSS color value.

        Args:
            value: Color value to validate

        Returns:
            Whether it's a valid color
        """
        if not isinstance(value, str):
            return False

        value = value.strip().lower()

        # Hexadecimal color
        if value.startswith("#") and len(value) in [4, 7]:
            hex_part = value[1:]
            return all(c in "0123456789abcdef" for c in hex_part)

        # RGB/RGBA color
        if value.startswith(("rgb(", "rgba(")):
            return True

        # Predefined color names
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
    """CSS size value validator."""

    def _get_default_error_message(self) -> str:
        return "Invalid CSS size value"

    def validate(self, value: Any) -> bool:
        """Validate CSS size value.

        Args:
            value: Size value to validate

        Returns:
            Whether it's a valid size
        """
        if not isinstance(value, str):
            return False

        value = value.strip().lower()

        # Number + unit
        size_units = ["px", "em", "rem", "%", "pt", "pc", "in", "cm", "mm"]

        for unit in size_units:
            if value.endswith(unit):
                number_part = value[: -len(unit)]
                try:
                    float(number_part)
                    return True
                except ValueError:
                    continue

        # Pure number (default px)
        try:
            float(value)
            return True
        except ValueError:
            return False


class RangeValidator(BaseValidator):
    """Numeric range validator."""

    def __init__(
        self,
        min_value: int | float,
        max_value: int | float,
        error_message: str | None = None,
    ):
        """Initialize range validator.

        Args:
            min_value: Minimum value
            max_value: Maximum value
            error_message: Custom error message
        """
        self.min_value = min_value
        self.max_value = max_value
        super().__init__(error_message)

    def _get_default_error_message(self) -> str:
        return f"Value must be between {self.min_value} and {self.max_value}"

    def validate(self, value: Any) -> bool:
        """Validate whether numeric value is within specified range.

        Args:
            value: Numeric value to validate

        Returns:
            Whether it's within range
        """
        if not isinstance(value, (int, float)):
            return False

        return self.min_value <= value <= self.max_value


class ProgressValidator(RangeValidator):
    """Progress value validator (0-100)."""

    def __init__(self, error_message: str | None = None):
        super().__init__(0, 100, error_message)

    def _get_default_error_message(self) -> str:
        return "Progress value must be between 0 and 100"


class UrlValidator(BaseValidator):
    """URL format validator."""

    def _get_default_error_message(self) -> str:
        return "Invalid URL format"

    def validate(self, value: Any) -> bool:
        """Validate URL format.

        Args:
            value: URL to validate

        Returns:
            Whether it's a valid URL
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
    """Email address validator."""

    def _get_default_error_message(self) -> str:
        return "Invalid email address format"

    def validate(self, value: Any) -> bool:
        """Validate email address format.

        Args:
            value: Email address to validate

        Returns:
            Whether it's a valid email
        """
        if not isinstance(value, str):
            return False

        email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

        return bool(email_pattern.match(value))


class NonEmptyStringValidator(BaseValidator):
    """Non-empty string validator."""

    def _get_default_error_message(self) -> str:
        return "String cannot be empty"

    def validate(self, value: Any) -> bool:
        """Validate whether string is non-empty.

        Args:
            value: String to validate

        Returns:
            Whether it's a non-empty string
        """
        return isinstance(value, str) and len(value.strip()) > 0


class LengthValidator(BaseValidator):
    """String length validator."""

    def __init__(
        self,
        min_length: int = 0,
        max_length: int | None = None,
        error_message: str | None = None,
    ):
        """Initialize length validator.

        Args:
            min_length: Minimum length
            max_length: Maximum length, None means no limit
            error_message: Custom error message
        """
        self.min_length = min_length
        self.max_length = max_length
        super().__init__(error_message)

    def _get_default_error_message(self) -> str:
        if self.max_length is not None:
            return f"Length must be between {self.min_length} and {self.max_length}"
        else:
            return f"Length must be at least {self.min_length}"

    def validate(self, value: Any) -> bool:
        """Validate string length.

        Args:
            value: String to validate

        Returns:
            Whether length meets requirements
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
    """Type validator."""

    def __init__(self, expected_type: type | tuple, error_message: str | None = None):
        """Initialize type validator.

        Args:
            expected_type: Expected type or type tuple
            error_message: Custom error message
        """
        self.expected_type = expected_type
        super().__init__(error_message)

    def _get_default_error_message(self) -> str:
        if isinstance(self.expected_type, tuple):
            type_names = [t.__name__ for t in self.expected_type]
            return f"Type must be one of {' or '.join(type_names)}"
        else:
            return f"Type must be {self.expected_type.__name__}"

    def validate(self, value: Any) -> bool:
        """Validate value type.

        Args:
            value: Value to validate

        Returns:
            Whether type matches
        """
        return isinstance(value, self.expected_type)


class ChoicesValidator(BaseValidator):
    """Choices validator."""

    def __init__(self, choices: list[Any], error_message: str | None = None):
        """Initialize choices validator.

        Args:
            choices: List of allowed choices
            error_message: Custom error message
        """
        self.choices = choices
        super().__init__(error_message)

    def _get_default_error_message(self) -> str:
        return f"Value must be one of the following choices: {self.choices}"

    def validate(self, value: Any) -> bool:
        """Validate whether value is in allowed choices.

        Args:
            value: Value to validate

        Returns:
            Whether it's in allowed choices
        """
        return value in self.choices


class CompositeValidator(BaseValidator):
    """Composite validator, can combine multiple validators."""

    def __init__(
        self,
        validators: list[BaseValidator],
        require_all: bool = True,
        error_message: str | None = None,
    ):
        """Initialize composite validator.

        Args:
            validators: List of validators
            require_all: Whether all validators must pass, False means only one needs to pass
            error_message: Custom error message
        """
        self.validators = validators
        self.require_all = require_all
        super().__init__(error_message)

    def _get_default_error_message(self) -> str:
        if self.require_all:
            return "Must pass all validation conditions"
        else:
            return "Must pass at least one validation condition"

    def validate(self, value: Any) -> bool:
        """Validate whether value passes composite conditions.

        Args:
            value: Value to validate

        Returns:
            Whether validation passes
        """
        results = [validator.validate(value) for validator in self.validators]

        if self.require_all:
            return all(results)
        else:
            return any(results)

    def get_failed_validators(self, value: Any) -> list[BaseValidator]:
        """Get list of validators that failed validation.

        Args:
            value: Value being validated

        Returns:
            List of failed validators
        """
        failed = []
        for validator in self.validators:
            if not validator.validate(value):
                failed.append(validator)
        return failed


# Predefined common validator instances
color_validator = ColorValidator()
size_validator = SizeValidator()
progress_validator = ProgressValidator()
url_validator = UrlValidator()
email_validator = EmailValidator()
non_empty_string_validator = NonEmptyStringValidator()

# Common type validators
string_validator = TypeValidator(str)
int_validator = TypeValidator(int)
float_validator = TypeValidator(float)
number_validator = TypeValidator((int, float))
bool_validator = TypeValidator(bool)
list_validator = TypeValidator(list)
dict_validator = TypeValidator(dict)
