# 📚 基本概念

在深入使用EmailWidget之前，理解其核心概念将帮助你更好地构建邮件报告。本章将介绍EmailWidget的设计理念和关键概念。

## 🏗️ 核心架构

EmailWidget采用面向对象的设计，主要包含以下核心概念：

<div class="grid cards" markdown>

- :material-email: **Email类**
  
  ---
  
  邮件的主容器，管理所有Widget并负责最终渲染
  
  **作用**: 邮件生命周期管理、HTML导出

- :material-widgets: **Widget组件**
  
  ---
  
  可重用的UI组件，如文本、表格、图表等
  
  **特点**: 独立渲染、链式调用、类型安全

- :material-cog: **配置系统**
  
  ---
  
  全局和局部的样式、行为配置管理
  
  **功能**: 主题定制、字体设置、布局控制

- :material-check-circle: **验证器**
  
  ---
  
  确保数据类型和值的正确性
  
  **保障**: 类型安全、数据完整性、错误预防

</div>

## 📧 Email类详解

### 基本概念

`Email`类是EmailWidget的核心，它充当所有Widget的容器和管理器：

```python
from email_widget import Email

# 创建邮件对象
email = Email(title="报告标题")

# 设置元信息
email.set_subtitle("副标题")
email.set_footer("脚注信息")

# 管理Widget
email.add_widget(widget)
email.remove_widget("widget_id")
email.clear_widgets()

# 导出结果
html_content = email.export_str()
file_path = email.export_html("report.html")
```

### 生命周期

Email对象的典型生命周期：

1. **创建** - 初始化邮件对象
2. **配置** - 设置标题、副标题、脚注等
3. **添加内容** - 添加各种Widget组件
4. **渲染** - 生成HTML内容
5. **导出** - 保存为文件或获取字符串

### 特性功能

=== "便捷方法"
    
    ```python
    # 直接添加常用内容
    email.add_text("标题", text_type="title_large")
    email.add_table_from_data(data, headers)
    email.add_progress(75, "完成度")
    email.add_chart_from_plt(title="图表")
    ```

=== "Widget管理"
    
    ```python
    # 获取Widget
    widget = email.get_widget("my_widget_id")
    
    # 移除Widget
    email.remove_widget("widget_id")
    
    # 清空所有Widget
    email.clear_widgets()
    
    # 获取Widget数量
    count = email.get_widget_count()
    ```

=== "链式调用"
    
    ```python
    # 流畅的API设计
    email = (Email("标题")
             .set_subtitle("副标题")
             .set_footer("脚注")
             .add_widget(widget1)
             .add_widget(widget2))
    ```

## 🧩 Widget组件系统

### 设计理念

所有Widget组件都继承自`BaseWidget`，确保API的一致性：

```python
from email_widget.core.base import BaseWidget

class MyCustomWidget(BaseWidget):
    def __init__(self):
        super().__init__()
        self.widget_type = "custom"
    
    def render(self) -> str:
        # 渲染逻辑
        return self._render_template("custom.html", context)
```

### 公共特性

所有Widget都具有以下共同特性：

=== "标识管理"
    
    ```python
    # 设置唯一ID
    widget.set_widget_id("my_unique_id")
    
    # 获取ID
    widget_id = widget.widget_id
    
    # 获取类型
    widget_type = widget.widget_type
    ```

=== "样式控制"
    
    ```python
    # 设置CSS类
    widget.set_css_class("custom-style")
    
    # 添加自定义样式
    widget.set_style("background-color: #f0f0f0;")
    
    # 设置容器属性
    widget.set_container_class("container-fluid")
    ```

=== "模板渲染"
    
    ```python
    # 获取渲染上下文
    context = widget.get_template_context()
    
    # 渲染为HTML
    html = widget.render()
    
    # 验证Widget状态
    is_valid = widget.validate()
    ```

### Widget分类

EmailWidget提供12种专业组件，按功能分类：

#### 📝 内容组件
- **TextWidget** - 文本内容，8种样式
- **ImageWidget** - 图片展示，多源支持
- **QuoteWidget** - 引用样式，作者信息

#### 📊 数据组件  
- **TableWidget** - 数据表格，DataFrame集成
- **ChartWidget** - 图表展示，matplotlib支持
- **LogWidget** - 日志显示，级别分类

#### 📈 指标组件
- **ProgressWidget** - 线性进度条，5种主题
- **CircularProgressWidget** - 圆形进度，多种尺寸
- **StatusWidget** - 状态管理，动态更新

#### 🎨 界面组件
- **AlertWidget** - 警告提醒，5种类型
- **CardWidget** - 信息卡片，图标支持
- **ColumnWidget** - 布局容器，响应式设计

## ⚙️ 配置系统

### 配置层级

EmailWidget采用分层配置系统：

```python
from email_widget.core.config import EmailConfig

# 1. 全局默认配置
EmailConfig.set_global_default("theme_color", "#007bff")

# 2. 邮件级配置
email_config = EmailConfig()
email_config.set_theme_color("#ff6b6b")
email.config = email_config

# 3. Widget级配置
widget.set_style("color: red;")
```

优先级：Widget级 > 邮件级 > 全局级

### 常用配置

=== "主题配置"
    
    ```python
    config = EmailConfig()
    
    # 主题色
    config.set_theme_color("#FF6B6B")
    
    # 字体设置
    config.set_font_family("Microsoft YaHei")
    config.set_font_size("14px")
    
    # 布局设置
    config.set_max_width("1200px")
    config.set_padding("20px")
    ```

=== "行为配置"
    
    ```python
    # 渲染选项
    config.enable_responsive_design(True)
    config.enable_dark_mode(False)
    config.set_image_quality(0.8)
    
    # 缓存设置
    config.enable_template_cache(True)
    config.set_cache_ttl(3600)
    ```

=== "导出配置"
    
    ```python
    # HTML导出
    config.set_html_encoding("utf-8")
    config.enable_minify_html(True)
    
    # 文件命名
    config.set_default_filename_pattern("{title}_{date}.html")
    config.set_output_directory("./reports/")
    ```

## 🔍 验证器系统

### 数据验证

EmailWidget内置强大的验证器系统，确保数据安全：

```python
from email_widget.core.validators import (
    RangeValidator, ColorValidator, UrlValidator
)

# 范围验证
range_validator = RangeValidator(0, 100)
is_valid = range_validator.validate(85)  # True

# 颜色验证
color_validator = ColorValidator()
is_valid = color_validator.validate("#FF6B6B")  # True

# URL验证
url_validator = UrlValidator()
is_valid = url_validator.validate("https://example.com")  # True
```

### 组合验证

可以组合多个验证器：

```python
from email_widget.core.validators import CompositeValidator

# 创建组合验证器
validator = CompositeValidator([
    RangeValidator(0, 100),
    TypeValidator(int)
], require_all=True)

# 验证数据
try:
    validator.validate(85)
    print("验证通过")
except ValidationError as e:
    print(f"验证失败: {e}")
```

### 自定义验证器

可以创建自定义验证器：

```python
from email_widget.core.validators import BaseValidator

class EmailValidator(BaseValidator):
    def validate(self, value: str) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, value) is not None
    
    def get_error_message(self, value) -> str:
        return f"'{value}' 不是有效的邮箱地址"
```

## 🎨 模板系统

### Jinja2集成

EmailWidget使用Jinja2作为模板引擎：

```python
from email_widget.core.template_engine import TemplateEngine

# 获取模板引擎
engine = TemplateEngine()

# 渲染模板
template = engine.get_template("widget_template.html")
html = template.render(context={"title": "标题", "content": "内容"})
```

### 模板结构

典型的Widget模板结构：

```html
<!-- widget_template.html -->
<div class="widget {{ widget_type }}" id="{{ widget_id }}">
    <div class="widget-header">
        <h3>{{ title }}</h3>
    </div>
    <div class="widget-content">
        {{ content|safe }}
    </div>
</div>
```

### 自定义模板

可以为自定义Widget创建模板：

```python
class CustomWidget(BaseWidget):
    def __init__(self):
        super().__init__()
        self.template_name = "custom_widget.html"
    
    def get_template_context(self) -> dict:
        return {
            "title": self.title,
            "custom_data": self.custom_data,
            **super().get_template_context()
        }
```

## 🔄 渲染流程

### 渲染过程

EmailWidget的渲染流程：

```mermaid
graph TD
    A[Email.export_html()] --> B[收集所有Widget]
    B --> C[验证Widget数据]
    C --> D[渲染各个Widget]
    D --> E[生成CSS样式]
    E --> F[合并HTML模板]
    F --> G[输出最终HTML]
```

### 性能优化

EmailWidget在渲染过程中进行了多项优化：

- **模板缓存** - 避免重复解析模板
- **懒加载** - 按需加载资源
- **HTML压缩** - 减小文件大小
- **图片优化** - 自动压缩和编码

## 🧩 扩展性设计

### 插件化架构

EmailWidget支持插件化扩展：

```python
# 注册自定义Widget
from email_widget.core.registry import WidgetRegistry

WidgetRegistry.register("custom", CustomWidget)

# 使用自定义Widget
email.add_widget(CustomWidget())
```

### 事件系统

支持事件监听和处理：

```python
# 监听渲染事件
@email.on("before_render")
def before_render_handler(email_instance):
    print("开始渲染邮件")

@email.on("after_render")  
def after_render_handler(email_instance, html_content):
    print("邮件渲染完成")
```

## 🎯 最佳实践

### 代码组织

建议的代码组织方式：

```python
# 1. 导入
from email_widget import Email, TextWidget, TableWidget
from email_widget.enums import TextType

# 2. 配置
def create_email_config():
    config = EmailConfig()
    config.set_theme_color("#007bff")
    return config

# 3. 数据准备
def prepare_data():
    return {"sales": [100, 200, 300]}

# 4. 邮件构建
def build_email(data):
    email = Email("销售报告")
    email.config = create_email_config()
    
    # 添加内容
    email.add_widget(
        TextWidget()
        .set_content("销售数据分析")
        .set_type(TextType.TITLE_LARGE)
    )
    
    return email

# 5. 主函数
def main():
    data = prepare_data()
    email = build_email(data)
    email.export_html("report.html")
```

### 性能建议

- **批量操作** - 一次性添加多个Widget
- **合理缓存** - 复用配置和模板
- **图片优化** - 控制图片大小和质量
- **按需加载** - 只导入需要的组件

## 🚀 下一步

现在你已经理解了EmailWidget的核心概念，可以：

- 查看 [用户指南](../user-guide/index.md) 学习各组件详细用法
- 浏览 [API参考](../api/index.md) 了解完整API
- 研究 [示例代码](../examples/index.md) 学习实际应用
- 阅读 [开发指南](../development/index.md) 参与项目开发

---

!!! tip "💡 重要提示"
    
    理解这些概念将帮助你更好地使用EmailWidget。如果某些概念暂时不太理解，可以先跳过，在实际使用中会逐渐清晰。 