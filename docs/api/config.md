# 配置管理

::: email_widget.core.config.EmailConfig

EmailConfig 类负责管理 EmailWidget 库的所有配置选项，包括邮件样式、字体、颜色、Widget 配置等。

## 类签名

```python
class EmailConfig:
    def __init__(self)
```

## 配置分类

### 📧 邮件基础配置
- 字符编码设置
- 语言区域设置
- 默认标题配置

### 🎨 样式配置
- 颜色主题设置
- 字体族配置
- 间距和尺寸设置

### 📐 布局配置
- 最大宽度设置
- 容器内边距配置
- 响应式断点设置

### 🧩 Widget 配置
- 各种 Widget 的默认配置
- 组件特定的样式设置

---

## 邮件基础配置

### `get_email_charset()` {: #get_email_charset}

```python
def get_email_charset(self) -> str
```

获取邮件字符集配置。

**Returns:**
- `str`: 字符集名称，默认为 "UTF-8"

### `get_email_lang()` {: #get_email_lang}

```python
def get_email_lang(self) -> str
```

获取邮件语言配置。

**Returns:**
- `str`: 语言代码，默认为 "zh-CN"

### `get_email_title()` {: #get_email_title}

```python
def get_email_title(self) -> str
```

获取邮件默认标题。

**Returns:**
- `str`: 默认标题，通常为 "邮件报告"

**示例:**
```python
from email_widget.core.config import EmailConfig

config = EmailConfig()
print(f"字符集: {config.get_email_charset()}")  # UTF-8
print(f"语言: {config.get_email_lang()}")        # zh-CN
print(f"默认标题: {config.get_email_title()}")   # 邮件报告
```

---

## 样式配置

### `get_primary_color()` {: #get_primary_color}

```python
def get_primary_color(self) -> str
```

获取主色调配置。

**Returns:**
- `str`: 主色调的十六进制颜色值，默认为 "#0078d4"

### `get_font_family()` {: #get_font_family}

```python
def get_font_family(self) -> str
```

获取默认字体族配置。

**Returns:**
- `str`: CSS 字体族字符串，默认为 "'Segoe UI', Tahoma, Arial, sans-serif"

### `get_max_width()` {: #get_max_width}

```python
def get_max_width(self) -> str
```

获取邮件最大宽度配置。

**Returns:**
- `str`: 最大宽度的 CSS 值，默认为 "1200px"

**示例:**
```python
config = EmailConfig()
print(f"主色调: {config.get_primary_color()}")    # #0078d4
print(f"字体族: {config.get_font_family()}")      # 'Segoe UI', Tahoma, Arial, sans-serif
print(f"最大宽度: {config.get_max_width()}")      # 1200px
```

---

## 布局配置

### `get_output_dir()` {: #get_output_dir}

```python
def get_output_dir(self) -> str
```

获取输出目录配置。

**Returns:**
- `str`: 输出目录路径字符串

**示例:**
```python
config = EmailConfig()
output_dir = config.get_output_dir()
print(f"输出目录: {output_dir}")
```

---

## Widget 配置

### `get_widget_config()` {: #get_widget_config}

```python
def get_widget_config(self, widget_type: str, key: str, default: Any = None) -> Any
```

获取指定 Widget 类型的配置项。

**Parameters:**
- `widget_type` (`str`): Widget 类型名称（如 "text", "chart", "table"）
- `key` (`str`): 配置键名
- `default` (`Any`): 默认值

**Returns:**
- `Any`: 配置值

**支持的 Widget 类型:**

#### Text Widget 配置
```python
# 文本相关配置
config.get_widget_config("text", "default_font_size", "14px")
config.get_widget_config("text", "default_color", "#323130")
config.get_widget_config("text", "line_height", "1.5")
```

#### Components 配置
```python
# 组件相关配置
config.get_widget_config("components", "table_striped", True)
config.get_widget_config("components", "log_max_height", "300px")
config.get_widget_config("components", "column_default_gap", "16px")
```

**示例:**
```python
config = EmailConfig()

# 获取文本默认配置
font_size = config.get_widget_config("text", "default_font_size", "14px")
text_color = config.get_widget_config("text", "default_color", "#333")

# 获取组件配置
striped = config.get_widget_config("components", "table_striped", False)
log_height = config.get_widget_config("components", "log_max_height", "200px")

print(f"默认字体大小: {font_size}")
print(f"默认文本颜色: {text_color}")
print(f"表格条纹: {striped}")
print(f"日志最大高度: {log_height}")
```

---

## 高级配置方法

### `get_text_config()` {: #get_text_config}

```python
def get_text_config(self, key: str, default: Any = None) -> Any
```

获取文本相关的配置项。

**Parameters:**
- `key` (`str`): 配置键名
- `default` (`Any`): 默认值

**Returns:**
- `Any`: 配置值

**可用配置键:**
- `"default_font_size"` - 默认字体大小
- `"default_color"` - 默认文本颜色
- `"line_height"` - 行高
- `"title_font_weight"` - 标题字重
- `"margin"` - 外边距

**示例:**
```python
config = EmailConfig()

# 文本样式配置
font_size = config.get_text_config("default_font_size", "14px")
line_height = config.get_text_config("line_height", "1.5")
title_weight = config.get_text_config("title_font_weight", "600")
```

---

## 配置常量

EmailConfig 使用预定义的常量来提供配置值：

### 基础常量

```python
# 输出配置
OUTPUT_DIR = Path("./output")

# 颜色配置
PRIMARY_COLOR = "#0078d4"           # 主色调
SECONDARY_COLOR = "#605e5c"         # 辅助色
SUCCESS_COLOR = "#107c10"           # 成功色
WARNING_COLOR = "#ff8c00"           # 警告色
ERROR_COLOR = "#d13438"             # 错误色

# 字体配置
FONT_FAMILY = "'Segoe UI', Tahoma, Arial, sans-serif"

# 尺寸配置
MAX_WIDTH = "1200px"
DEFAULT_MARGIN = "16px 0"
DEFAULT_PADDING = "16px"

# 邮件配置
DEFAULT_TITLE = "邮件报告"
CHARSET = "UTF-8"
LANG = "zh-CN"
```

### Widget 特定常量

```python
# 文本配置
TEXT_DEFAULT_FONT_SIZE = "14px"
TEXT_DEFAULT_COLOR = "#323130"
TEXT_LINE_HEIGHT = "1.5"

# 表格配置
TABLE_STRIPED = True
TABLE_BORDER_COLOR = "#e1dfdd"

# 日志配置
LOG_MAX_HEIGHT = "300px"

# 列布局配置
COLUMN_DEFAULT_GAP = "16px"
```

---

## 使用模式

### 1. 获取默认配置

```python
from email_widget import Email

# Email 对象自动使用默认配置
email = Email("我的报告")
config = email.config

# 查看当前配置
print(f"主色调: {config.get_primary_color()}")
print(f"字体: {config.get_font_family()}")
print(f"最大宽度: {config.get_max_width()}")
```

### 2. 查询 Widget 配置

```python
def setup_text_widget_with_config():
    config = EmailConfig()
    
    # 获取文本默认配置
    font_size = config.get_text_config("default_font_size")
    text_color = config.get_text_config("default_color")
    line_height = config.get_text_config("line_height")
    
    # 应用到 Widget
    from email_widget.widgets import TextWidget
    text = TextWidget()
    text.set_font_size(font_size)
    text.set_color(text_color)
    # line_height 通常在模板中自动应用
    
    return text
```

### 3. 条件配置选择

```python
def get_theme_colors(theme="default"):
    config = EmailConfig()
    
    if theme == "business":
        return {
            "primary": "#0078d4",
            "secondary": "#605e5c",
            "background": "#ffffff"
        }
    elif theme == "dark":
        return {
            "primary": "#60cdff",
            "secondary": "#cccccc", 
            "background": "#1f1f1f"
        }
    else:
        return {
            "primary": config.get_primary_color(),
            "secondary": "#605e5c",
            "background": "#ffffff"
        }
```

### 4. 配置验证

```python
def validate_config():
    config = EmailConfig()
    
    # 检查基本配置
    assert config.get_email_charset() == "UTF-8"
    assert config.get_email_lang() in ["zh-CN", "en-US", "zh-TW"]
    
    # 检查颜色配置
    primary_color = config.get_primary_color()
    assert primary_color.startswith("#")
    assert len(primary_color) == 7
    
    # 检查尺寸配置
    max_width = config.get_max_width()
    assert max_width.endswith("px") or max_width.endswith("%")
    
    print("配置验证通过")
```

---

## 自定义配置扩展

虽然 EmailConfig 使用预定义常量，但您可以通过继承来扩展配置功能：

### 1. 扩展配置类

```python
from email_widget.core.config import EmailConfig

class CustomEmailConfig(EmailConfig):
    """自定义邮件配置"""
    
    def __init__(self):
        super().__init__()
        self._custom_settings = {
            "brand_color": "#6c5ce7",
            "brand_font": "'Inter', 'Helvetica Neue', Arial, sans-serif",
            "custom_margin": "20px 0",
            "custom_border_radius": "8px"
        }
    
    def get_brand_color(self) -> str:
        return self._custom_settings["brand_color"]
    
    def get_brand_font(self) -> str:
        return self._custom_settings["brand_font"]
    
    def get_custom_margin(self) -> str:
        return self._custom_settings["custom_margin"]
    
    def get_border_radius(self) -> str:
        return self._custom_settings["custom_border_radius"]

# 使用自定义配置
custom_config = CustomEmailConfig()
print(f"品牌色: {custom_config.get_brand_color()}")
print(f"品牌字体: {custom_config.get_brand_font()}")
```

### 2. 配置工厂

```python
class ConfigFactory:
    """配置工厂类"""
    
    @staticmethod
    def create_business_config():
        """创建商务主题配置"""
        config = EmailConfig()
        # 这里可以包装或修改配置
        return config
    
    @staticmethod
    def create_minimal_config():
        """创建简约主题配置"""
        config = EmailConfig()
        # 这里可以包装或修改配置
        return config
    
    @staticmethod
    def create_dashboard_config():
        """创建仪表板主题配置"""
        config = EmailConfig()
        # 这里可以包装或修改配置
        return config

# 使用配置工厂
business_config = ConfigFactory.create_business_config()
minimal_config = ConfigFactory.create_minimal_config()
dashboard_config = ConfigFactory.create_dashboard_config()
```

---

## 完整示例

### 配置驱动的邮件创建

```python
from email_widget import Email
from email_widget.widgets import *
from email_widget.core.config import EmailConfig
from email_widget.core.enums import *

def create_configured_email():
    """创建使用配置的邮件"""
    
    # 获取配置
    config = EmailConfig()
    
    # 创建邮件
    email = Email("配置演示报告")
    email.config = config
    
    # 使用配置创建标题
    title_color = config.get_primary_color()
    font_family = config.get_font_family()
    
    title = TextWidget()
    title.set_content("配置驱动的邮件报告")
    title.set_type(TextType.TITLE_LARGE)
    title.set_color(title_color)
    # 字体族通常在全局样式中应用
    
    email.add_widget(title)
    
    # 使用配置创建文本
    default_font_size = config.get_text_config("default_font_size", "14px")
    default_color = config.get_text_config("default_color", "#323130")
    
    content = TextWidget()
    content.set_content("这个邮件使用了配置管理系统来统一样式设置。")
    content.set_font_size(default_font_size)
    content.set_color(default_color)
    
    email.add_widget(content)
    
    # 使用配置创建表格
    table_striped = config.get_widget_config("components", "table_striped", True)
    
    table = TableWidget()
    table.set_headers(["配置项", "值", "说明"])
    table.add_row(["主色调", config.get_primary_color(), "品牌主色"])
    table.add_row(["字体族", config.get_font_family(), "默认字体"])
    table.add_row(["最大宽度", config.get_max_width(), "邮件宽度限制"])
    table.set_striped(table_striped)
    
    email.add_widget(table)
    
    # 配置信息卡片
    config_card = CardWidget()
    config_card.set_title("配置概览")
    config_card.set_content(f"""
    字符集: {config.get_email_charset()}
    语言: {config.get_email_lang()}
    输出目录: {config.get_output_dir()}
    """)
    config_card.set_icon("⚙️")
    
    email.add_widget(config_card)
    
    return email

# 生成报告
email = create_configured_email()
email.export_html("configured_email.html")
```

### 多主题配置示例

```python
def create_multi_theme_demo():
    """演示不同配置主题的效果"""
    
    themes = {
        "default": EmailConfig(),
        "business": EmailConfig(),  # 在实际应用中可能是不同的配置
        "minimal": EmailConfig()    # 在实际应用中可能是不同的配置
    }
    
    for theme_name, config in themes.items():
        email = Email(f"{theme_name.title()} 主题演示")
        email.config = config
        
        # 添加主题信息
        email.add_title(f"{theme_name.title()} 主题", TextType.TITLE_LARGE)
        
        # 显示主题配置
        theme_info = f"""
        主色调: {config.get_primary_color()}
        字体族: {config.get_font_family()}
        最大宽度: {config.get_max_width()}
        """
        
        email.add_text(theme_info)
        
        # 导出对应主题的文件
        email.export_html(f"{theme_name}_theme_demo.html")
        
        print(f"✅ {theme_name.title()} 主题演示已生成")

# 生成多主题演示
create_multi_theme_demo()
```

---

## 最佳实践

### 1. 配置查询模式

```python
# ✅ 推荐：使用配置查询统一样式
def create_styled_widget():
    config = EmailConfig()
    
    widget = TextWidget()
    widget.set_color(config.get_primary_color())
    widget.set_font_size(config.get_text_config("default_font_size"))
    
    return widget

# ❌ 避免：硬编码样式值
def create_hardcoded_widget():
    widget = TextWidget()
    widget.set_color("#0078d4")  # 硬编码颜色
    widget.set_font_size("14px")  # 硬编码大小
    
    return widget
```

### 2. 配置缓存

```python
class ConfigCache:
    """配置缓存类"""
    _config = None
    
    @classmethod
    def get_config(cls):
        if cls._config is None:
            cls._config = EmailConfig()
        return cls._config

# 使用缓存避免重复创建配置对象
config = ConfigCache.get_config()
```

### 3. 配置验证

```python
def validate_and_get_config():
    """验证并获取配置"""
    try:
        config = EmailConfig()
        
        # 验证关键配置
        assert config.get_primary_color().startswith("#")
        assert len(config.get_font_family()) > 0
        assert config.get_max_width().endswith(("px", "%", "em"))
        
        return config
    except Exception as e:
        print(f"配置验证失败: {e}")
        return None
```

### 4. 环境相关配置

```python
import os

def get_environment_config():
    """根据环境获取不同配置"""
    env = os.getenv("EMAILWIDGET_ENV", "production")
    
    config = EmailConfig()
    
    if env == "development":
        # 开发环境可能需要不同的输出目录
        pass
    elif env == "testing":
        # 测试环境的特殊配置
        pass
    
    return config
``` 