# 配置系统

EmailWidget 提供了灵活的配置系统，允许您自定义邮件的各种设置，包括字符编码、语言、样式主题等。

## 🚀 快速开始

```python
from email_widget import Email
from email_widget.core.config import EmailConfig

# 使用默认配置
email = Email("我的邮件")

# 获取当前配置
config = email.config
print(f"字符集: {config.get_email_charset()}")
print(f"语言: {config.get_email_lang()}")
```

## ⚙️ 配置选项

### 📧 邮件基础配置

```python
# 字符编码设置
config = EmailConfig()
config.set_email_charset("UTF-8")        # 默认UTF-8
config.set_email_charset("GB2312")       # 中文编码

# 语言设置
config.set_email_lang("zh-CN")           # 简体中文
config.set_email_lang("en-US")           # 英文
config.set_email_lang("zh-TW")           # 繁体中文

# 获取配置值
charset = config.get_email_charset()
language = config.get_email_lang()
```

### 🎨 样式配置

```python
# 默认字体设置
config.set_default_font_family("'Microsoft YaHei', Arial, sans-serif")

# 默认颜色设置
config.set_primary_color("#0078d4")      # 主色调
config.set_secondary_color("#605e5c")    # 辅助色
config.set_success_color("#107c10")      # 成功色
config.set_warning_color("#ff8c00")      # 警告色
config.set_error_color("#d13438")        # 错误色

# 默认间距设置
config.set_default_margin("16px 0")      # 默认外边距
config.set_default_padding("16px")       # 默认内边距
```

### 📐 布局配置

```python
# 最大宽度设置
config.set_max_width("1200px")           # 邮件最大宽度
config.set_container_padding("20px")     # 容器内边距

# 响应式断点
config.set_mobile_breakpoint("600px")    # 移动设备断点
```

## 🎯 配置应用方式

### 方式一：直接设置Email配置

```python
from email_widget import Email

# 创建邮件并设置配置
email = Email("配置示例")

# 修改配置
email.config.set_email_charset("UTF-8")
email.config.set_email_lang("zh-CN")
email.config.set_primary_color("#ff6b6b")
```

### 方式二：使用预配置对象

```python
from email_widget import Email
from email_widget.core.config import EmailConfig

# 创建配置对象
config = EmailConfig()
config.set_email_charset("UTF-8")
config.set_email_lang("zh-CN")
config.set_primary_color("#4ecdc4")
config.set_default_font_family("'PingFang SC', 'Helvetica Neue', Arial")

# 应用配置
email = Email("自定义配置邮件")
email.config = config
```

### 方式三：全局配置

```python
from email_widget.core.config import EmailConfig

# 设置全局默认配置
EmailConfig.set_global_defaults({
    "charset": "UTF-8",
    "lang": "zh-CN",
    "primary_color": "#6c5ce7",
    "font_family": "'Source Han Sans CN', Arial, sans-serif"
})

# 后续创建的邮件将使用全局配置
email1 = Email("邮件1")  # 使用全局配置
email2 = Email("邮件2")  # 使用全局配置
```

## 🎨 主题配置

### 预定义主题

EmailWidget 提供了几种预定义主题：

```python
from email_widget.core.config import EmailConfig, Theme

# 商务主题
business_config = EmailConfig.from_theme(Theme.BUSINESS)
business_config.apply({
    "primary_color": "#0078d4",
    "secondary_color": "#605e5c",
    "font_family": "'Segoe UI', Tahoma, Arial, sans-serif"
})

# 现代主题
modern_config = EmailConfig.from_theme(Theme.MODERN)
modern_config.apply({
    "primary_color": "#6c5ce7",
    "secondary_color": "#74b9ff",
    "font_family": "'Inter', 'Helvetica Neue', Arial, sans-serif"
})

# 简约主题
minimal_config = EmailConfig.from_theme(Theme.MINIMAL)
minimal_config.apply({
    "primary_color": "#2d3748",
    "secondary_color": "#718096",
    "font_family": "'SF Pro Text', -apple-system, Arial, sans-serif"
})
```

### 自定义主题

```python
# 创建自定义主题
custom_theme = {
    "charset": "UTF-8",
    "lang": "zh-CN",
    "primary_color": "#e74c3c",
    "secondary_color": "#34495e",
    "success_color": "#27ae60",
    "warning_color": "#f39c12",
    "error_color": "#e74c3c",
    "font_family": "'Roboto', 'Noto Sans SC', Arial, sans-serif",
    "max_width": "800px",
    "default_margin": "20px 0",
    "default_padding": "20px"
}

# 应用自定义主题
config = EmailConfig()
config.apply(custom_theme)

email = Email("自定义主题邮件")
email.config = config
```

## 📱 响应式配置

### 移动端优化

```python
# 移动端配置
mobile_config = EmailConfig()
mobile_config.set_mobile_breakpoint("768px")
mobile_config.set_mobile_font_size("16px")     # 移动端字体大小
mobile_config.set_mobile_padding("12px")       # 移动端内边距
mobile_config.set_mobile_max_width("100%")     # 移动端最大宽度

# 响应式图片配置
mobile_config.set_image_max_width("100%")
mobile_config.set_image_height("auto")
```

### 暗色主题支持

```python
# 暗色主题配置
dark_config = EmailConfig()
dark_config.set_background_color("#1a1a1a")
dark_config.set_text_color("#ffffff")
dark_config.set_border_color("#404040")
dark_config.set_card_background("#2d2d2d")

# 条件应用暗色主题
def apply_dark_theme_if_needed(config, user_preference):
    if user_preference == "dark":
        config.apply({
            "background_color": "#1a1a1a",
            "text_color": "#ffffff",
            "border_color": "#404040"
        })
    return config
```

## 🌍 国际化配置

### 多语言支持

```python
# 中文配置
zh_config = EmailConfig()
zh_config.set_email_lang("zh-CN")
zh_config.set_date_format("%Y年%m月%d日")
zh_config.set_time_format("%H:%M:%S")
zh_config.set_default_footer("此邮件由EmailWidget自动生成")

# 英文配置
en_config = EmailConfig()
en_config.set_email_lang("en-US")
en_config.set_date_format("%Y-%m-%d")
en_config.set_time_format("%H:%M:%S")
en_config.set_default_footer("This email was generated by EmailWidget")

# 日文配置
ja_config = EmailConfig()
ja_config.set_email_lang("ja-JP")
ja_config.set_date_format("%Y年%m月%d日")
ja_config.set_font_family("'Hiragino Sans', 'Yu Gothic', Arial, sans-serif")
```

### 地区化设置

```python
# 根据地区设置配置
def get_locale_config(locale):
    config = EmailConfig()
    
    if locale.startswith("zh"):
        config.set_email_lang("zh-CN")
        config.set_font_family("'PingFang SC', 'Microsoft YaHei', Arial")
        config.set_date_format("%Y年%m月%d日")
    elif locale.startswith("en"):
        config.set_email_lang("en-US")
        config.set_font_family("'Segoe UI', 'Helvetica Neue', Arial")
        config.set_date_format("%m/%d/%Y")
    elif locale.startswith("ja"):
        config.set_email_lang("ja-JP")
        config.set_font_family("'Hiragino Sans', 'Yu Gothic', Arial")
        config.set_date_format("%Y年%m月%d日")
    
    return config

# 使用
user_locale = "zh-CN"
config = get_locale_config(user_locale)
```

## 🔧 高级配置

### 性能优化配置

```python
# 性能相关配置
performance_config = EmailConfig()

# 模板缓存设置
performance_config.set_template_cache_size(100)    # 缓存大小
performance_config.set_template_cache_ttl(3600)    # 缓存时间(秒)

# 图片处理配置
performance_config.set_image_cache_enabled(True)
performance_config.set_image_max_size("2MB")
performance_config.set_image_quality(85)

# 渲染优化
performance_config.set_async_rendering(True)       # 异步渲染
performance_config.set_parallel_widgets(True)      # 并行处理组件
```

### 安全配置

```python
# 安全相关配置
security_config = EmailConfig()

# XSS防护
security_config.set_escape_html(True)              # HTML转义
security_config.set_allowed_tags(["b", "i", "u"])  # 允许的HTML标签

# 内容验证
security_config.set_validate_urls(True)            # URL验证
security_config.set_max_content_length(10000)      # 最大内容长度

# 图片安全
security_config.set_validate_images(True)          # 图片验证
security_config.set_allowed_image_types(["png", "jpg", "gif"])
```

## 📋 完整配置示例

### 企业级邮件配置

```python
from email_widget import Email
from email_widget.core.config import EmailConfig

# 创建企业级配置
enterprise_config = EmailConfig()

# 基础设置
enterprise_config.set_email_charset("UTF-8")
enterprise_config.set_email_lang("zh-CN")

# 视觉设计
enterprise_config.apply({
    "primary_color": "#0078d4",           # 微软蓝
    "secondary_color": "#605e5c",         # 中性灰
    "success_color": "#107c10",           # 绿色
    "warning_color": "#ff8c00",           # 橙色
    "error_color": "#d13438",             # 红色
    "font_family": "'Segoe UI', 'Microsoft YaHei', Arial, sans-serif",
    "max_width": "1000px",
    "default_margin": "16px 0",
    "default_padding": "16px"
})

# 移动端优化
enterprise_config.set_mobile_breakpoint("768px")
enterprise_config.set_mobile_padding("12px")

# 性能优化
enterprise_config.set_template_cache_size(200)
enterprise_config.set_image_cache_enabled(True)

# 安全设置
enterprise_config.set_escape_html(True)
enterprise_config.set_validate_urls(True)

# 应用配置
email = Email("企业级邮件报告")
email.config = enterprise_config
```

### 个人博客风格配置

```python
# 个人博客风格配置
blog_config = EmailConfig()

blog_config.apply({
    "charset": "UTF-8",
    "lang": "zh-CN",
    "primary_color": "#ff6b6b",
    "secondary_color": "#4ecdc4",
    "success_color": "#51cf66",
    "warning_color": "#ffd43b",
    "error_color": "#ff6b6b",
    "font_family": "'Inter', 'SF Pro Text', 'Helvetica Neue', Arial",
    "max_width": "700px",
    "default_margin": "24px 0",
    "default_padding": "20px",
    "border_radius": "8px",
    "box_shadow": "0 4px 12px rgba(0,0,0,0.1)"
})

email = Email("个人博客订阅")
email.config = blog_config
```

## ⚙️ API 参考

### EmailConfig 核心方法

#### 基础配置
| 方法 | 参数 | 说明 | 默认值 |
|------|------|------|--------|
| `set_email_charset()` | `charset: str` | 设置字符编码 | `"UTF-8"` |
| `set_email_lang()` | `lang: str` | 设置语言 | `"zh-CN"` |
| `get_email_charset()` | 无 | 获取字符编码 | - |
| `get_email_lang()` | 无 | 获取语言设置 | - |

#### 样式配置
| 方法 | 参数 | 说明 | 默认值 |
|------|------|------|--------|
| `set_primary_color()` | `color: str` | 设置主色调 | `"#0078d4"` |
| `set_secondary_color()` | `color: str` | 设置辅助色 | `"#605e5c"` |
| `set_default_font_family()` | `family: str` | 设置默认字体 | `"'Segoe UI', Arial"` |
| `set_max_width()` | `width: str` | 设置最大宽度 | `"100%"` |

#### 高级方法
| 方法 | 参数 | 说明 |
|------|------|------|
| `apply()` | `config_dict: dict` | 批量应用配置 |
| `merge()` | `other_config: EmailConfig` | 合并其他配置 |
| `reset()` | 无 | 重置为默认配置 |
| `to_dict()` | 无 | 导出为字典 |
| `from_dict()` | `config_dict: dict` | 从字典创建配置 |

## 🎯 最佳实践

### 1. 配置管理策略
```python
# 推荐：使用配置文件管理
import json

def load_email_config(config_file):
    with open(config_file, 'r', encoding='utf-8') as f:
        config_data = json.load(f)
    
    config = EmailConfig()
    config.apply(config_data)
    return config

# 配置文件 email_config.json
{
    "charset": "UTF-8",
    "lang": "zh-CN",
    "primary_color": "#0078d4",
    "font_family": "'Segoe UI', Arial, sans-serif"
}
```

### 2. 环境配置区分
```python
# 推荐：根据环境使用不同配置
def get_config_for_environment(env):
    if env == "production":
        return EmailConfig.from_theme(Theme.BUSINESS)
    elif env == "staging":
        return EmailConfig.from_theme(Theme.MODERN)
    else:  # development
        config = EmailConfig()
        config.set_primary_color("#ff6b6b")  # 开发环境使用醒目颜色
        return config
```

### 3. 用户偏好配置
```python
# 推荐：支持用户个人偏好
def apply_user_preferences(config, user_prefs):
    if user_prefs.get("dark_mode"):
        config.apply({
            "background_color": "#1a1a1a",
            "text_color": "#ffffff"
        })
    
    if user_prefs.get("large_font"):
        config.set_default_font_size("18px")
    
    return config
```

### 4. 配置验证
```python
# 推荐：验证配置有效性
def validate_config(config):
    errors = []
    
    # 验证颜色格式
    colors = [config.get_primary_color(), config.get_secondary_color()]
    for color in colors:
        if not color.startswith('#') or len(color) != 7:
            errors.append(f"无效的颜色格式: {color}")
    
    # 验证字符集
    charset = config.get_email_charset()
    if charset not in ["UTF-8", "GB2312", "GBK"]:
        errors.append(f"不支持的字符集: {charset}")
    
    return errors
```

## 🚨 注意事项

1. **字符编码**: 确保选择正确的字符编码，UTF-8是最安全的选择
2. **颜色对比度**: 确保文字与背景有足够的对比度
3. **字体回退**: 设置合适的字体回退序列
4. **性能影响**: 过多的配置可能影响渲染性能
5. **兼容性**: 考虑不同邮件客户端的兼容性

## 🔧 故障排除

### 配置不生效
- 检查配置是否正确应用到Email对象
- 验证配置参数格式是否正确
- 确认配置优先级顺序

### 样式异常
- 检查CSS属性值是否有效
- 验证颜色代码格式
- 确认字体名称拼写正确

---

**下一步**: 了解 [最佳实践](best-practices.md) 学习EmailWidget的进阶使用技巧。 