# API 参考

欢迎来到 EmailWidget 的 API 参考文档！这里提供了所有 Widget 组件的详细 API 说明，包括方法签名、参数说明、返回值、异常处理和使用示例。

## 📚 文档组织

EmailWidget 的 API 按功能模块进行组织，便于您快速找到所需的接口：

### 🏗️ 核心架构

- **[核心模块](core.md)** - 基础组件和模板引擎
- **[Email主类](email.md)** - 邮件容器和管理功能
- **[邮件发送器](email-sender.md)** - 邮件发送功能和服务商支持

### 🧩 组件系统

- **[文本组件](text-widget.md)**
- **[表格组件](table-widget.md)**
- **[图片组件](image-widget.md)**
- **[警告组件](alert-widget.md)**
- **[进度组件](progress-widget.md)**
- **[圆形进度组件](circular-progress-widget.md)**
- **[卡片组件](card-widget.md)**
- **[图表组件](chart-widget.md)**
- **[日志组件](log-widget.md)**
- **[引用组件](quote-widget.md)**
- **[布局组件](column-widget.md)**

## 🚀 快速导航

### 按使用频率

**高频使用** (日常开发必备)
- [`Email`](email.md) - 邮件主类
- [`TextWidget`](text-widget.md) - 文本组件
- [`TableWidget`](table-widget.md) - 表格组件
- [`ChartWidget`](chart-widget.md) - 图表组件
- [`AlertWidget`](alert-widget.md) - 警告框组件

**中频使用** (常见场景)
- [`ProgressWidget`](progress-widget.md) - 进度条组件
- [`StatusWidget`](status-widget.md) - 状态组件
- [`CardWidget`](card-widget.md) - 卡片组件

### 按功能分类

| 功能分类 | 主要组件 | 适用场景 |
|---------|---------|----------|
| **文本展示** | `TextWidget`, `QuoteWidget` | 标题、正文、引用 |
| **数据展示** | `TableWidget`, `ChartWidget` | 数据报告、统计图表 |
| **状态监控** | `StatusWidget`, `ProgressWidget`, `CircularProgressWidget` | 系统监控、任务进度 |
| **布局控制** | `ColumnWidget`, `CardWidget` | 页面布局、信息卡片 |
| **交互反馈** | `AlertWidget`, `LogWidget` | 通知、日志记录 |

## 📖 使用说明

### API 文档约定

#### 🔗 链式调用
EmailWidget 广泛使用链式调用模式，大多数设置方法都返回 `self`：

```python
widget = TextWidget()\
    .set_content("Hello World")\
    .set_color("#0078d4")\
    .set_font_size("18px")
```

#### 🏷️ 类型提示
所有 API 都提供完整的类型提示：

```python
def set_content(self, content: str) -> 'TextWidget':
    """设置文本内容
    
    Args:
        content: 文本内容字符串
        
    Returns:
        返回self以支持链式调用
    """
```

#### ⚠️ 异常处理
API 使用明确的异常类型：

```python
from email_widget.core.validators import ValidationError

try:
    widget.set_color("invalid-color")
except ValidationError as e:
    print(f"颜色格式错误: {e}")
```

### 常用模式

#### 📝 创建基本邮件

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

#### 📊 数据可视化

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

#### 🎨 自定义样式

```python
from email_widget.core.config import EmailConfig

# 配置主题
config = EmailConfig()
config.set_primary_color("#6c5ce7")
config.set_font_family("'Helvetica Neue', Arial, sans-serif")

# 应用到邮件
email.config = config
```

## 🔍 搜索技巧

### 按需求查找

- **寻找特定方法**: 使用 `Ctrl+F` 搜索方法名
- **了解参数类型**: 查看类型提示和参数说明
- **查看使用示例**: 每个方法都提供实际使用示例
- **理解返回值**: 注意返回类型和链式调用支持

### 常见搜索词

| 搜索需求 | 搜索关键词 |
|---------|-----------|
| 设置颜色 | `color`, `set_color` |
| 调整大小 | `size`, `width`, `height` |
| 文本样式 | `font`, `text`, `align` |
| 数据绑定 | `data`, `dataframe`, `set_data` |
| 事件处理 | `callback`, `event`, `handler` |
| 验证规则 | `validator`, `validate` |

## 📋 版本兼容性

当前文档对应 EmailWidget v1.0.0，API 稳定性说明：

- 🟢 **稳定 API**: 主要的 Widget 类和方法
- 🟡 **实验性 API**: 高级功能和自定义扩展
- 🔴 **内部 API**: 以 `_` 开头的方法，不保证兼容性

## 📞 获取帮助

如果在使用 API 过程中遇到问题：

1. 📖 查阅对应的 [用户指南](../user-guide/index.md)
2. 💡 参考 [示例代码](../examples/index.md)
3. 🐛 提交 [GitHub Issue](https://github.com/271374667/EmailWidget/issues)
4. 💬 加入讨论 [GitHub Discussions](https://github.com/271374667/EmailWidget/discussions)

---

现在开始探索 EmailWidget 的强大 API 吧！建议从 [Email主类](email.md) 开始。

## 注意事项

1. **邮件兼容性** - 所有组件都针对邮件客户端进行了优化
2. **响应式设计** - 支持不同屏幕尺寸的自适应显示
3. **链式调用** - 所有设置方法都返回 self，支持链式调用
4. **参数验证** - 提供输入参数的验证和错误处理
5. **中文支持** - 完整支持中文字符显示
6. **依赖管理** - 部分功能需要额外的依赖库（如 matplotlib、pandas）

## 获取帮助

如果在使用 API 时遇到问题：

1. 查看对应组件的详细 API 文档
2. 参考用户指南中的使用示例
3. 查看 GitHub 仓库的示例代码
4. 提交 Issue 获取技术支持

## 版本信息

当前 API 文档对应 EmailWidget v1.0.0 版本。API 可能在新版本中发生变化，请注意版本兼容性。