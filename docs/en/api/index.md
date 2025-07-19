# API Reference

Welcome to the EmailWidget API reference documentation! This provides detailed API specifications for all Widget components, including method signatures, parameter descriptions, return values, exception handling, and usage examples.

## 📚 Documentation Organization

EmailWidget's API is organized by functional modules to help you quickly find the interfaces you need:

### 🏗️ Core Architecture

- **[Core Module](core.md)** - Base components and template engine
- **[Email Main Class](email.md)** - Email container and management functionality
- **[Email Sender](email-sender.md)** - Email sending functionality and service provider support

### 🧩 Component System

- **[Text Widget](text-widget.md)**
- **[Table Widget](table-widget.md)**
- **[Image Widget](image-widget.md)**
- **[Alert Widget](alert-widget.md)**
- **[Progress Widget](progress-widget.md)**
- **[Circular Progress Widget](circular-progress-widget.md)**
- **[Card Widget](card-widget.md)**
- **[Chart Widget](chart-widget.md)**
- **[Log Widget](log-widget.md)**
- **[Quote Widget](quote-widget.md)**
- **[Column Widget](column-widget.md)**

## 🚀 Quick Navigation

### By Usage Frequency

**High Frequency** (Essential for daily development)
- [`Email`](email.md) - Email main class
- [`TextWidget`](text-widget.md) - Text component
- [`TableWidget`](table-widget.md) - Table component
- [`ChartWidget`](chart-widget.md) - Chart component
- [`AlertWidget`](alert-widget.md) - Alert box component

**Medium Frequency** (Common scenarios)
- [`ProgressWidget`](progress-widget.md) - Progress bar component
- [`StatusWidget`](status-widget.md) - Status component
- [`CardWidget`](card-widget.md) - Card component

### By Functional Category

| Function Category | Main Components | Use Cases |
|---------|---------|----------|
| **Text Display** | `TextWidget`, `QuoteWidget` | Titles, body text, quotes |
| **Data Display** | `TableWidget`, `ChartWidget` | Data reports, statistical charts |
| **Status Monitoring** | `StatusWidget`, `ProgressWidget`, `CircularProgressWidget` | System monitoring, task progress |
| **Layout Control** | `ColumnWidget`, `CardWidget` | Page layout, information cards |
| **Interactive Feedback** | `AlertWidget`, `LogWidget` | Notifications, log recording |

## 📖 Usage Instructions

### API Documentation Conventions

#### 🔗 Method Chaining
EmailWidget extensively uses method chaining patterns, where most setter methods return `self`:

```python
widget = TextWidget()\
    .set_content("Hello World")\
    .set_color("#0078d4")\
    .set_font_size("18px")
```

#### 🏷️ Type Hints
All APIs provide complete type hints:

```python
def set_content(self, content: str) -> 'TextWidget':
    """设置文本内容
    
    Args:
        content: 文本内容字符串
        
    Returns:
        返回self以支持链式调用
    """
```

#### ⚠️ Exception Handling
API uses explicit exception types:

```python
from email_widget.core.validators import ValidationError

try:
    widget.set_color("invalid-color")
except ValidationError as e:
    print(f"颜色格式错误: {e}")
```

### Common Patterns

#### 📝 Creating Basic Email

```python
from email_widget import Email, TextWidget, TableWidget
from email_widget.core.enums import TextType

# 创建邮件
email = Email("数据报告")

# 添加标题
email.add_widget(
    TextWidget()\
    .set_content("月度业绩汇总")\
    .set_type(TextType.TITLE_LARGE)
)

# 导出HTML
email.export_html("report.html")
```

#### 📊 Data Visualization

```python
from email_widget.widgets import ChartWidget, ProgressWidget
from email_widget.core.enums import ProgressTheme

# 添加图表
email.add_widget(
    ChartWidget()\
    .set_image_url("chart.png")\
    .set_title("销售趋势")
)

# 添加进度指标
email.add_widget(
    ProgressWidget()\
    .set_value(85)\
    .set_label("目标完成度")\
    .set_theme(ProgressTheme.SUCCESS)
)
```

#### 🎨 Custom Styling

```python
from email_widget.core.config import EmailConfig

# 配置主题
config = EmailConfig()
config.set_primary_color("#6c5ce7")
config.set_font_family("'Helvetica Neue', Arial, sans-serif")

# 应用到邮件
email.config = config
```

## 🔍 Search Tips

### Finding by Need

- **Looking for specific methods**: Use `Ctrl+F` to search method names
- **Understanding parameter types**: Check type hints and parameter descriptions
- **Viewing usage examples**: Each method provides practical usage examples
- **Understanding return values**: Note return types and method chaining support

### Common Search Terms

| Search Need | Search Keywords |
|---------|-----------|
| Set colors | `color`, `set_color` |
| Adjust size | `size`, `width`, `height` |
| Text styling | `font`, `text`, `align` |
| Data binding | `data`, `dataframe`, `set_data` |
| Event handling | `callback`, `event`, `handler` |
| Validation rules | `validator`, `validate` |

## 📋 Version Compatibility

Current documentation corresponds to EmailWidget v1.0.0, API stability description:

- 🟢 **Stable API**: Main Widget classes and methods
- 🟡 **Experimental API**: Advanced features and custom extensions
- 🔴 **Internal API**: Methods starting with `_`, compatibility not guaranteed

## 📞 Getting Help

If you encounter issues while using the API:

1. 📖 Consult the corresponding [User Guide](../user-guide/index.md)
2. 💡 Reference [Example Code](../examples/index.md)
3. 🐛 Submit [GitHub Issue](https://github.com/271374667/EmailWidget/issues)
4. 💬 Join discussions [GitHub Discussions](https://github.com/271374667/EmailWidget/discussions)

---

Now start exploring EmailWidget's powerful API! We recommend starting with the [Email Main Class](email.md).

## Important Notes

1. **Email Compatibility** - All components are optimized for email clients
2. **Responsive Design** - Supports adaptive display for different screen sizes
3. **Method Chaining** - All setter methods return self, supporting method chaining
4. **Parameter Validation** - Provides input parameter validation and error handling
5. **Chinese Support** - Complete support for Chinese character display
6. **Dependency Management** - Some features require additional dependency libraries (such as matplotlib, pandas)

## Getting Help

If you encounter problems while using the API:

1. Check the detailed API documentation for the corresponding component
2. Reference usage examples in the user guide
3. View example code in the GitHub repository
4. Submit an Issue for technical support

## Version Information

Current API documentation corresponds to EmailWidget v1.0.0. The API may change in new versions, please pay attention to version compatibility.