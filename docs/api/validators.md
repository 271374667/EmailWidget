# 验证器系统

::: email_widget.core.validators

EmailWidget 提供了完整的数据验证系统，确保输入数据的正确性和安全性。所有验证器都基于面向对象的设计模式。

## 验证器基类

### BaseValidator

::: email_widget.core.validators.BaseValidator

所有验证器的抽象基类，定义了验证器的基本接口。

```python
class BaseValidator(ABC):
    def __init__(self, error_message: Optional[str] = None)
```

#### 构造方法

**Parameters:**
- `error_message` (`Optional[str]`): 自定义错误消息，如果不提供则使用默认消息

#### 抽象方法

##### `validate()` {: #base_validate}

```python
@abstractmethod
def validate(self, value: Any) -> bool
```

验证值是否有效。

**Parameters:**
- `value` (`Any`): 要验证的值

**Returns:**
- `bool`: 验证是否通过

#### 实例方法

##### `get_error_message()` {: #base_get_error_message}

```python
def get_error_message(self, value: Any = None) -> str
```

获取错误消息。

**Parameters:**
- `value` (`Any`): 验证失败的值（可选）

**Returns:**
- `str`: 错误消息

**示例:**
```python
from email_widget.core.validators import BaseValidator

class CustomValidator(BaseValidator):
    def validate(self, value):
        return isinstance(value, str) and len(value) > 0
    
    def _get_default_error_message(self):
        return "值必须是非空字符串"

validator = CustomValidator()
result = validator.validate("")
if not result:
    print(validator.get_error_message(""))  # 输出错误消息
```

---

## 通用验证器

### TypeValidator

::: email_widget.core.validators.TypeValidator

类型验证器，验证值是否为指定类型。

```python
class TypeValidator(BaseValidator):
    def __init__(self, expected_type: Union[type, tuple], error_message: Optional[str] = None)
```

**Parameters:**
- `expected_type` (`Union[type, tuple]`): 期望的类型或类型元组
- `error_message` (`Optional[str]`): 自定义错误消息

**示例:**
```python
from email_widget.core.validators import TypeValidator

# 单一类型验证
string_validator = TypeValidator(str)
print(string_validator.validate("hello"))    # True
print(string_validator.validate(123))        # False

# 多类型验证
number_validator = TypeValidator((int, float))
print(number_validator.validate(42))         # True
print(number_validator.validate(3.14))       # True
print(number_validator.validate("123"))      # False
```

### RangeValidator

::: email_widget.core.validators.RangeValidator

数值范围验证器，验证数值是否在指定范围内。

```python
class RangeValidator(BaseValidator):
    def __init__(self, min_value: Union[int, float], max_value: Union[int, float], 
                 error_message: Optional[str] = None)
```

**Parameters:**
- `min_value` (`Union[int, float]`): 最小值
- `max_value` (`Union[int, float]`): 最大值
- `error_message` (`Optional[str]`): 自定义错误消息

**示例:**
```python
from email_widget.core.validators import RangeValidator

# 进度值验证 (0-100)
progress_validator = RangeValidator(0, 100)
print(progress_validator.validate(50))       # True
print(progress_validator.validate(150))      # False

# 年龄验证 (0-120)
age_validator = RangeValidator(0, 120, "年龄必须在0-120之间")
print(age_validator.validate(25))            # True
print(age_validator.validate(-5))            # False
```

### ChoicesValidator

::: email_widget.core.validators.ChoicesValidator

选项验证器，验证值是否在允许的选项列表中。

```python
class ChoicesValidator(BaseValidator):
    def __init__(self, choices: List[Any], error_message: Optional[str] = None)
```

**Parameters:**
- `choices` (`List[Any]`): 允许的选项列表
- `error_message` (`Optional[str]`): 自定义错误消息

**示例:**
```python
from email_widget.core.validators import ChoicesValidator

# 状态选择验证
status_choices = ["active", "inactive", "pending"]
status_validator = ChoicesValidator(status_choices)
print(status_validator.validate("active"))   # True
print(status_validator.validate("deleted"))  # False

# 颜色主题验证
theme_validator = ChoicesValidator(["light", "dark", "auto"])
print(theme_validator.validate("light"))     # True
print(theme_validator.validate("custom"))    # False
```

---

## 字符串验证器

### NonEmptyStringValidator

::: email_widget.core.validators.NonEmptyStringValidator

非空字符串验证器，验证字符串是否非空。

```python
class NonEmptyStringValidator(BaseValidator):
    def __init__(self, error_message: Optional[str] = None)
```

**示例:**
```python
from email_widget.core.validators import NonEmptyStringValidator

validator = NonEmptyStringValidator()
print(validator.validate("hello"))           # True
print(validator.validate(""))                # False
print(validator.validate("   "))             # False (空白字符)
print(validator.validate(None))              # False
```

### LengthValidator

::: email_widget.core.validators.LengthValidator

长度验证器，验证字符串长度是否在指定范围内。

```python
class LengthValidator(BaseValidator):
    def __init__(self, min_length: int, max_length: int, error_message: Optional[str] = None)
```

**Parameters:**
- `min_length` (`int`): 最小长度
- `max_length` (`int`): 最大长度
- `error_message` (`Optional[str]`): 自定义错误消息

**示例:**
```python
from email_widget.core.validators import LengthValidator

# 用户名长度验证 (3-20字符)
username_validator = LengthValidator(3, 20)
print(username_validator.validate("john"))      # True
print(username_validator.validate("jo"))        # False (太短)
print(username_validator.validate("a" * 25))    # False (太长)

# 标题长度验证
title_validator = LengthValidator(1, 100, "标题长度必须在1-100字符之间")
print(title_validator.validate("报告标题"))      # True
```

---

## 格式验证器

### ColorValidator

::: email_widget.core.validators.ColorValidator

颜色格式验证器，支持多种CSS颜色格式。

```python
class ColorValidator(BaseValidator):
    def __init__(self, error_message: Optional[str] = None)
```

**支持格式:**
- 十六进制: `#rgb`, `#rrggbb`
- RGB: `rgb(r, g, b)`
- RGBA: `rgba(r, g, b, a)`
- HSL: `hsl(h, s%, l%)`
- HSLA: `hsla(h, s%, l%, a)`
- 命名颜色: `red`, `blue`, `green` 等

**示例:**
```python
from email_widget.core.validators import ColorValidator

color_validator = ColorValidator()

# 十六进制颜色
print(color_validator.validate("#ff0000"))        # True
print(color_validator.validate("#f00"))           # True
print(color_validator.validate("#xyz"))           # False

# RGB 颜色
print(color_validator.validate("rgb(255, 0, 0)")) # True
print(color_validator.validate("rgb(300, 0, 0)")) # False (超出范围)

# 命名颜色
print(color_validator.validate("red"))            # True
print(color_validator.validate("blue"))           # True
print(color_validator.validate("unknown"))        # False
```

### SizeValidator

::: email_widget.core.validators.SizeValidator

尺寸格式验证器，验证CSS尺寸值格式。

```python
class SizeValidator(BaseValidator):
    def __init__(self, error_message: Optional[str] = None)
```

**支持单位:**
- `px` - 像素
- `%` - 百分比
- `em` - 相对字体大小
- `rem` - 根元素字体大小
- `pt` - 点
- `vw` - 视口宽度
- `vh` - 视口高度

**示例:**
```python
from email_widget.core.validators import SizeValidator

size_validator = SizeValidator()

# 像素值
print(size_validator.validate("100px"))          # True
print(size_validator.validate("50px"))           # True

# 百分比
print(size_validator.validate("50%"))            # True
print(size_validator.validate("100%"))           # True

# 其他单位
print(size_validator.validate("1.5em"))          # True
print(size_validator.validate("2rem"))           # True
print(size_validator.validate("12pt"))           # True

# 无效格式
print(size_validator.validate("100"))            # False (缺少单位)
print(size_validator.validate("abc"))            # False
```

### UrlValidator

::: email_widget.core.validators.UrlValidator

URL 格式验证器，验证 URL 格式是否正确。

```python
class UrlValidator(BaseValidator):
    def __init__(self, error_message: Optional[str] = None)
```

**支持协议:**
- `http://`
- `https://`
- `ftp://`
- `data:` (base64 数据URL)

**示例:**
```python
from email_widget.core.validators import UrlValidator

url_validator = UrlValidator()

# HTTP/HTTPS URL
print(url_validator.validate("https://example.com"))         # True
print(url_validator.validate("http://www.google.com"))       # True
print(url_validator.validate("https://cdn.example.com/image.png")) # True

# FTP URL
print(url_validator.validate("ftp://files.example.com"))     # True

# Data URL
print(url_validator.validate("data:image/png;base64,iVBOR...")) # True

# 无效 URL
print(url_validator.validate("not-a-url"))                   # False
print(url_validator.validate("example.com"))                 # False (缺少协议)
```

### EmailValidator

::: email_widget.core.validators.EmailValidator

邮箱地址验证器，验证电子邮箱格式。

```python
class EmailValidator(BaseValidator):
    def __init__(self, error_message: Optional[str] = None)
```

**示例:**
```python
from email_widget.core.validators import EmailValidator

email_validator = EmailValidator()

# 有效邮箱
print(email_validator.validate("user@example.com"))          # True
print(email_validator.validate("test.email@domain.org"))     # True
print(email_validator.validate("user+tag@example.co.uk"))    # True

# 无效邮箱
print(email_validator.validate("invalid-email"))             # False
print(email_validator.validate("@example.com"))              # False
print(email_validator.validate("user@"))                     # False
```

---

## 专用验证器

### ProgressValidator

::: email_widget.core.validators.ProgressValidator

进度值验证器，专门用于验证进度条数值。

```python
class ProgressValidator(BaseValidator):
    def __init__(self, error_message: Optional[str] = None)
```

**验证规则:**
- 必须是数值类型 (int 或 float)
- 值必须 >= 0
- 支持超过 100 的值（用于自定义最大值的场景）

**示例:**
```python
from email_widget.core.validators import ProgressValidator

progress_validator = ProgressValidator()

# 有效进度值
print(progress_validator.validate(0))            # True (0%)
print(progress_validator.validate(50))           # True (50%)
print(progress_validator.validate(100))          # True (100%)
print(progress_validator.validate(150))          # True (自定义最大值场景)
print(progress_validator.validate(75.5))         # True (小数值)

# 无效进度值
print(progress_validator.validate(-10))          # False (负值)
print(progress_validator.validate("50"))         # False (字符串)
print(progress_validator.validate(None))         # False (None值)
```

---

## 复合验证器

### CompositeValidator

::: email_widget.core.validators.CompositeValidator

复合验证器，可以组合多个验证器进行联合验证。

```python
class CompositeValidator(BaseValidator):
    def __init__(self, validators: List[BaseValidator], 
                 require_all: bool = True, error_message: Optional[str] = None)
```

**Parameters:**
- `validators` (`List[BaseValidator]`): 验证器列表
- `require_all` (`bool`): 是否要求所有验证器都通过，默认 True
- `error_message` (`Optional[str]`): 自定义错误消息

**验证模式:**
- `require_all=True`: 所有验证器都必须通过（AND 逻辑）
- `require_all=False`: 至少一个验证器通过即可（OR 逻辑）

**示例:**
```python
from email_widget.core.validators import (
    CompositeValidator, TypeValidator, LengthValidator, NonEmptyStringValidator
)

# 复合字符串验证：非空 + 类型 + 长度
string_validators = [
    NonEmptyStringValidator(),
    TypeValidator(str),
    LengthValidator(3, 50)
]

composite_validator = CompositeValidator(string_validators, require_all=True)

# 测试验证
print(composite_validator.validate("hello"))     # True (满足所有条件)
print(composite_validator.validate("hi"))        # False (长度不够)
print(composite_validator.validate(""))          # False (空字符串)
print(composite_validator.validate(123))         # False (类型错误)

# OR 逻辑验证：满足任一条件即可
or_validator = CompositeValidator([
    TypeValidator(str),
    TypeValidator(int)
], require_all=False)

print(or_validator.validate("text"))             # True (字符串)
print(or_validator.validate(42))                 # True (整数)
print(or_validator.validate(3.14))               # False (浮点数)
```

---

## 预定义验证器实例

EmailWidget 提供了常用验证器的预定义实例，可以直接使用：

```python
from email_widget.core.validators import (
    color_validator, size_validator, progress_validator,
    url_validator, email_validator, non_empty_string_validator,
    string_validator, int_validator, float_validator, 
    number_validator, bool_validator, list_validator, dict_validator
)

# 直接使用预定义实例
print(color_validator.validate("#ff0000"))           # True
print(size_validator.validate("100px"))              # True
print(progress_validator.validate(75))               # True
print(url_validator.validate("https://example.com")) # True
print(email_validator.validate("user@example.com"))  # True

# 类型验证器
print(string_validator.validate("hello"))            # True
print(int_validator.validate(42))                    # True
print(float_validator.validate(3.14))                # True
print(number_validator.validate(42))                 # True (int 或 float)
print(bool_validator.validate(True))                 # True
print(list_validator.validate([1, 2, 3]))            # True
print(dict_validator.validate({"key": "value"}))     # True
```

---

## 在 Widget 中使用验证器

### Widget 内部验证

```python
from email_widget.core.base import BaseWidget
from email_widget.core.validators import ColorValidator, SizeValidator

class CustomWidget(BaseWidget):
    def __init__(self):
        super().__init__()
        self._color = "#000000"
        self._size = "100px"
        
        # 初始化验证器
        self._color_validator = ColorValidator()
        self._size_validator = SizeValidator()
    
    def set_color(self, color: str):
        if not self._color_validator.validate(color):
            raise ValueError(self._color_validator.get_error_message(color))
        self._color = color
        return self
    
    def set_size(self, size: str):
        if not self._size_validator.validate(size):
            raise ValueError(self._size_validator.get_error_message(size))
        self._size = size
        return self
```

### 批量验证

```python
def validate_widget_data(data: dict) -> bool:
    """批量验证 Widget 数据"""
    
    validators = {
        "title": non_empty_string_validator,
        "color": color_validator,
        "size": size_validator,
        "progress": progress_validator,
        "url": url_validator
    }
    
    for key, value in data.items():
        if key in validators:
            validator = validators[key]
            if not validator.validate(value):
                print(f"验证失败 - {key}: {validator.get_error_message(value)}")
                return False
    
    return True

# 使用示例
widget_data = {
    "title": "标题",
    "color": "#ff0000",
    "size": "200px",
    "progress": 75,
    "url": "https://example.com/image.png"
}

if validate_widget_data(widget_data):
    print("所有数据验证通过")
else:
    print("数据验证失败")
```

---

## 自定义验证器

### 创建简单验证器

```python
from email_widget.core.validators import BaseValidator

class PositiveNumberValidator(BaseValidator):
    """正数验证器"""
    
    def _get_default_error_message(self):
        return "值必须是正数"
    
    def validate(self, value):
        return isinstance(value, (int, float)) and value > 0

# 使用自定义验证器
validator = PositiveNumberValidator()
print(validator.validate(10))      # True
print(validator.validate(-5))      # False
print(validator.validate(0))       # False
```

### 创建复杂验证器

```python
class IPAddressValidator(BaseValidator):
    """IP地址验证器"""
    
    def _get_default_error_message(self):
        return "无效的IP地址格式"
    
    def validate(self, value):
        if not isinstance(value, str):
            return False
        
        parts = value.split('.')
        if len(parts) != 4:
            return False
        
        try:
            for part in parts:
                num = int(part)
                if not (0 <= num <= 255):
                    return False
            return True
        except ValueError:
            return False

# 使用示例
ip_validator = IPAddressValidator()
print(ip_validator.validate("192.168.1.1"))    # True
print(ip_validator.validate("192.168.1.256"))  # False
print(ip_validator.validate("not.an.ip"))      # False
```

### 参数化验证器

```python
class RegexValidator(BaseValidator):
    """正则表达式验证器"""
    
    def __init__(self, pattern: str, error_message: Optional[str] = None):
        self.pattern = re.compile(pattern)
        super().__init__(error_message)
    
    def _get_default_error_message(self):
        return f"值不匹配正则表达式: {self.pattern.pattern}"
    
    def validate(self, value):
        if not isinstance(value, str):
            return False
        return bool(self.pattern.match(value))

# 使用示例
phone_validator = RegexValidator(r'^\d{3}-\d{3}-\d{4}$', "电话号码格式错误")
print(phone_validator.validate("123-456-7890"))  # True
print(phone_validator.validate("1234567890"))    # False

hex_color_validator = RegexValidator(r'^#[0-9a-fA-F]{6}$', "必须是6位十六进制颜色")
print(hex_color_validator.validate("#ff0000"))   # True
print(hex_color_validator.validate("#f00"))      # False
```

---

## 完整示例

### 表单数据验证

```python
from email_widget.core.validators import *

class FormValidator:
    """表单数据验证器"""
    
    def __init__(self):
        self.validators = {
            'name': CompositeValidator([
                NonEmptyStringValidator(),
                LengthValidator(2, 50)
            ]),
            'email': EmailValidator(),
            'age': RangeValidator(0, 120),
            'website': UrlValidator(),
            'theme_color': ColorValidator(),
            'avatar_size': SizeValidator(),
            'progress': ProgressValidator(),
            'status': ChoicesValidator(['active', 'inactive', 'pending'])
        }
    
    def validate_form(self, form_data: dict):
        """验证整个表单"""
        errors = {}
        
        for field, value in form_data.items():
            if field in self.validators:
                validator = self.validators[field]
                if not validator.validate(value):
                    errors[field] = validator.get_error_message(value)
        
        return len(errors) == 0, errors
    
    def validate_field(self, field: str, value):
        """验证单个字段"""
        if field not in self.validators:
            return True, None
        
        validator = self.validators[field]
        is_valid = validator.validate(value)
        error = None if is_valid else validator.get_error_message(value)
        
        return is_valid, error

# 使用示例
form_validator = FormValidator()

# 测试数据
test_data = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'age': 30,
    'website': 'https://johndoe.com',
    'theme_color': '#3498db',
    'avatar_size': '64px',
    'progress': 75,
    'status': 'active'
}

is_valid, errors = form_validator.validate_form(test_data)

if is_valid:
    print("✅ 表单验证通过")
else:
    print("❌ 表单验证失败:")
    for field, error in errors.items():
        print(f"  {field}: {error}")

# 单字段验证
field_valid, field_error = form_validator.validate_field('email', 'invalid-email')
if not field_valid:
    print(f"邮箱验证失败: {field_error}")
```

### Widget 配置验证

```python
def create_validated_widget():
    """创建经过验证的 Widget"""
    
    # 模拟 Widget 配置
    config = {
        'title': 'Dashboard Widget',
        'background_color': '#ffffff',
        'border_color': '#e1e8ed',
        'width': '300px',
        'height': '200px',
        'progress_value': 85,
        'link_url': 'https://dashboard.example.com',
        'admin_email': 'admin@example.com'
    }
    
    # 验证配置
    validation_rules = {
        'title': non_empty_string_validator,
        'background_color': color_validator,
        'border_color': color_validator,
        'width': size_validator,
        'height': size_validator,
        'progress_value': progress_validator,
        'link_url': url_validator,
        'admin_email': email_validator
    }
    
    # 执行验证
    for key, value in config.items():
        if key in validation_rules:
            validator = validation_rules[key]
            if not validator.validate(value):
                raise ValueError(f"配置项 '{key}' 验证失败: {validator.get_error_message(value)}")
    
    print("✅ Widget 配置验证通过")
    return config

# 使用
try:
    validated_config = create_validated_widget()
    print("Widget 配置:", validated_config)
except ValueError as e:
    print(f"配置错误: {e}")
```

---

## 最佳实践

### 1. 验证器选择

```python
# ✅ 推荐：根据数据类型选择合适的验证器
color_validator = ColorValidator()           # 颜色值
size_validator = SizeValidator()             # CSS尺寸
progress_validator = ProgressValidator()     # 进度值
email_validator = EmailValidator()           # 邮箱地址

# ❌ 避免：使用过于宽泛的验证器
generic_validator = TypeValidator(str)       # 太宽泛，不能验证格式
```

### 2. 错误处理

```python
# ✅ 推荐：提供友好的错误消息
validator = LengthValidator(3, 20, "用户名长度必须在3-20字符之间")

# ✅ 推荐：捕获并处理验证异常
try:
    widget.set_color(user_input)
except ValueError as e:
    logger.warning(f"颜色设置失败: {e}")
    # 使用默认颜色
    widget.set_color("#000000")
```

### 3. 性能优化

```python
# ✅ 推荐：复用验证器实例
class WidgetFactory:
    def __init__(self):
        self.color_validator = ColorValidator()
        self.size_validator = SizeValidator()
    
    def create_widget(self, config):
        # 使用共享的验证器实例
        if not self.color_validator.validate(config['color']):
            raise ValueError("无效颜色")
        # ...

# ❌ 避免：重复创建验证器
def create_widget(config):
    color_validator = ColorValidator()  # 每次都创建新实例
    # ...
```

### 4. 组合验证

```python
# ✅ 推荐：使用 CompositeValidator 组合多个验证条件
username_validator = CompositeValidator([
    NonEmptyStringValidator(),
    LengthValidator(3, 20),
    RegexValidator(r'^[a-zA-Z0-9_]+$', "用户名只能包含字母、数字和下划线")
])

# ✅ 推荐：创建语义化的验证器
def create_password_validator():
    return CompositeValidator([
        LengthValidator(8, 128, "密码长度必须在8-128字符之间"),
        RegexValidator(r'[A-Z]', "密码必须包含大写字母"),
        RegexValidator(r'[a-z]', "密码必须包含小写字母"),
        RegexValidator(r'\d', "密码必须包含数字")
    ])
``` 