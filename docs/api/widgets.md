# Widget 组件

Widget 组件是 EmailWidget 的核心功能模块，提供了丰富的UI组件来构建邮件内容。所有 Widget 都继承自 `BaseWidget` 基类。

## 组件分类

### 📝 内容展示组件
- [TextWidget](#textwidget) - 文本组件
- [ImageWidget](#imagewidget) - 图片组件
- [QuoteWidget](#quotewidget) - 引用组件

### 📊 数据展示组件
- [TableWidget](#tablewidget) - 表格组件
- [ChartWidget](#chartwidget) - 图表组件

### 📈 状态监控组件
- [ProgressWidget](#progresswidget) - 线性进度条
- [CircularProgressWidget](#circularprogresswidget) - 圆形进度条
- [StatusWidget](#statuswidget) - 状态信息

### 🎨 布局组件
- [ColumnWidget](#columnwidget) - 多列布局
- [CardWidget](#cardwidget) - 卡片容器

### 🔔 交互反馈组件
- [AlertWidget](#alertwidget) - 警告框
- [LogWidget](#logwidget) - 日志记录

---

## TextWidget

::: email_widget.widgets.text_widget.TextWidget

文本组件，用于显示各种文本内容，支持多种样式和格式。

### 构造方法

```python
def __init__(self, widget_id: Optional[str] = None)
```

### 主要方法

#### `set_content()` {: #text_set_content}

```python
def set_content(self, content: str) -> 'TextWidget'
```

设置文本内容。

**Parameters:**
- `content` (`str`): 文本内容

**Returns:**
- `TextWidget`: 支持链式调用

#### `set_type()` {: #text_set_type}

```python
def set_type(self, text_type: TextType) -> 'TextWidget'
```

设置文本类型。

**Parameters:**
- `text_type` (`TextType`): 文本类型枚举

**可用类型:**
- `TextType.TITLE_LARGE` - 大标题
- `TextType.TITLE_SMALL` - 小标题  
- `TextType.BODY` - 正文（默认）
- `TextType.CAPTION` - 说明文字
- `TextType.SECTION_H2` - 二级标题
- `TextType.SECTION_H3` - 三级标题
- `TextType.SECTION_H4` - 四级标题
- `TextType.SECTION_H5` - 五级标题

#### `set_color()` {: #text_set_color}

```python
def set_color(self, color: str) -> 'TextWidget'
```

设置文本颜色。

**Parameters:**
- `color` (`str`): CSS 颜色值（如 "#ff0000", "red", "rgb(255,0,0)"）

#### `set_font_size()` {: #text_set_font_size}

```python
def set_font_size(self, size: str) -> 'TextWidget'
```

设置字体大小。

**Parameters:**
- `size` (`str`): CSS 字体大小（如 "16px", "1.2em", "large"）

#### `set_align()` {: #text_set_align}

```python
def set_align(self, align: TextAlign) -> 'TextWidget'
```

设置文本对齐方式。

**Parameters:**
- `align` (`TextAlign`): 对齐方式枚举
  - `TextAlign.LEFT` - 左对齐
  - `TextAlign.CENTER` - 居中
  - `TextAlign.RIGHT` - 右对齐
  - `TextAlign.JUSTIFY` - 两端对齐

### 使用示例

```python
from email_widget.widgets import TextWidget
from email_widget.core.enums import TextType, TextAlign

# 基本用法
text = TextWidget()
text.set_content("Hello World")

# 链式调用
title = (TextWidget()
    .set_content("重要标题")
    .set_type(TextType.TITLE_LARGE)
    .set_color("#0078d4")
    .set_align(TextAlign.CENTER)
)

# 段落文本
paragraph = (TextWidget()
    .set_content("这是一段正文内容，说明了项目的基本情况和重要信息。")
    .set_type(TextType.BODY)
    .set_font_size("16px")
)
```

---

## TableWidget

::: email_widget.widgets.table_widget.TableWidget

表格组件，用于展示结构化数据，支持表头、条纹样式、状态单元格等功能。

### 构造方法

```python
def __init__(self, widget_id: Optional[str] = None)
```

### 主要方法

#### `set_headers()` {: #table_set_headers}

```python
def set_headers(self, headers: List[str]) -> 'TableWidget'
```

设置表格表头。

**Parameters:**
- `headers` (`List[str]`): 表头列表

#### `add_row()` {: #table_add_row}

```python
def add_row(self, row: List[Union[str, TableCell]]) -> 'TableWidget'
```

添加表格行。

**Parameters:**
- `row` (`List[Union[str, TableCell]]`): 行数据，可以是字符串或 TableCell 对象

#### `set_dataframe()` {: #table_set_dataframe}

```python
def set_dataframe(self, df: "pd.DataFrame") -> 'TableWidget'
```

从 pandas DataFrame 设置表格数据。

**Parameters:**
- `df` (`pd.DataFrame`): pandas DataFrame 对象

#### `set_striped()` {: #table_set_striped}

```python
def set_striped(self, striped: bool) -> 'TableWidget'
```

设置是否使用条纹样式。

**Parameters:**
- `striped` (`bool`): 是否启用条纹样式

#### `set_show_index()` {: #table_set_show_index}

```python
def set_show_index(self, show_index: bool) -> 'TableWidget'
```

设置是否显示索引列。

**Parameters:**
- `show_index` (`bool`): 是否显示索引列

### TableCell 辅助类

```python
class TableCell:
    def __init__(self, content: str, status: Optional[StatusType] = None)
```

表格单元格，支持状态样式。

**Parameters:**
- `content` (`str`): 单元格内容
- `status` (`Optional[StatusType]`): 状态类型

### 使用示例

```python
from email_widget.widgets import TableWidget, TableCell
from email_widget.core.enums import StatusType
import pandas as pd

# 基本表格
table = TableWidget()
table.set_headers(["姓名", "部门", "状态"])
table.add_row(["张三", "技术部", "在职"])
table.add_row(["李四", "销售部", "在职"])

# 带状态的表格
table_with_status = TableWidget()
table_with_status.set_headers(["服务", "状态", "响应时间"])
table_with_status.add_row([
    "Web服务",
    TableCell("正常", StatusType.SUCCESS),
    "120ms"
])
table_with_status.add_row([
    "数据库",
    TableCell("警告", StatusType.WARNING), 
    "250ms"
])

# 从 DataFrame 创建
df = pd.DataFrame({
    '产品': ['iPhone', 'iPad', 'MacBook'],
    '销量': [1200, 800, 600],
    '收入': [120000, 64000, 120000]
})

df_table = (TableWidget()
    .set_dataframe(df)
    .set_title("产品销售统计")
    .set_striped(True)
    .set_show_index(True)
)
```

---

## ChartWidget

::: email_widget.widgets.chart_widget.ChartWidget

图表组件，专门用于展示图表，支持多种图表类型和数据摘要。

### 主要方法

#### `set_image_url()` {: #chart_set_image_url}

```python
def set_image_url(self, image_url: str) -> 'ChartWidget'
```

设置图表图片URL。

#### `set_title()` {: #chart_set_title}

```python
def set_title(self, title: str) -> 'ChartWidget'
```

设置图表标题。

#### `set_description()` {: #chart_set_description}

```python
def set_description(self, description: str) -> 'ChartWidget'
```

设置图表描述。

#### `set_data_summary()` {: #chart_set_data_summary}

```python
def set_data_summary(self, summary: str) -> 'ChartWidget'
```

设置数据摘要信息。

#### `set_chart()` {: #chart_set_chart}

```python
def set_chart(self, plt_instance) -> 'ChartWidget'
```

从 matplotlib 实例设置图表。

### 使用示例

```python
from email_widget.widgets import ChartWidget
import matplotlib.pyplot as plt

# 从图片URL创建
chart1 = (ChartWidget()
    .set_image_url("https://example.com/chart.png")
    .set_title("销售趋势图")
    .set_description("显示最近6个月的销售趋势")
    .set_data_summary("总销售额: ¥1,250,000")
)

# 从 matplotlib 创建
fig, ax = plt.subplots()
ax.bar(['Q1', 'Q2', 'Q3', 'Q4'], [100, 120, 140, 160])
ax.set_title('季度营收')

chart2 = (ChartWidget()
    .set_chart(plt)
    .set_title("季度营收分析")
    .set_description("2024年各季度营收对比")
)
```

---

## ProgressWidget

::: email_widget.widgets.progress_widget.ProgressWidget

线性进度条组件，显示任务或进程的完成进度。

### 主要方法

#### `set_value()` {: #progress_set_value}

```python
def set_value(self, value: float) -> 'ProgressWidget'
```

设置当前进度值。

#### `set_max_value()` {: #progress_set_max_value}

```python
def set_max_value(self, max_val: float) -> 'ProgressWidget'
```

设置最大值。

#### `set_label()` {: #progress_set_label}

```python
def set_label(self, label: str) -> 'ProgressWidget'
```

设置进度条标签。

#### `set_theme()` {: #progress_set_theme}

```python
def set_theme(self, theme: ProgressTheme) -> 'ProgressWidget'
```

设置进度条主题。

**可用主题:**
- `ProgressTheme.PRIMARY` - 主色调（默认）
- `ProgressTheme.SUCCESS` - 成功绿色
- `ProgressTheme.WARNING` - 警告橙色
- `ProgressTheme.ERROR` - 错误红色
- `ProgressTheme.INFO` - 信息蓝色

#### `set_show_percentage()` {: #progress_set_show_percentage}

```python
def set_show_percentage(self, show: bool) -> 'ProgressWidget'
```

设置是否显示百分比。

### 使用示例

```python
from email_widget.widgets import ProgressWidget
from email_widget.core.enums import ProgressTheme

# 基本进度条
progress = (ProgressWidget()
    .set_value(75)
    .set_label("任务完成度")
    .set_theme(ProgressTheme.SUCCESS)
)

# 自定义最大值
custom_progress = (ProgressWidget()
    .set_value(450)
    .set_max_value(500)
    .set_label("数据处理进度")
    .set_show_percentage(True)
)
```

---

## CircularProgressWidget

::: email_widget.widgets.circular_progress_widget.CircularProgressWidget

圆形进度条组件，以圆形方式显示进度，适合展示百分比数据。

### 主要方法

#### `set_value()` {: #circular_set_value}

```python
def set_value(self, value: float) -> 'CircularProgressWidget'
```

设置当前进度值。

#### `set_size()` {: #circular_set_size}

```python
def set_size(self, size: str) -> 'CircularProgressWidget'
```

设置圆形进度条尺寸。

#### `set_label()` {: #circular_set_label}

```python
def set_label(self, label: str) -> 'CircularProgressWidget'
```

设置标签文本。

### 使用示例

```python
from email_widget.widgets import CircularProgressWidget

circular = (CircularProgressWidget()
    .set_value(88)
    .set_label("系统性能")
    .set_size("120px")
)
```

---

## AlertWidget

::: email_widget.widgets.alert_widget.AlertWidget

警告框组件，GitHub 风格的提示框，支持多种警告类型。

### 主要方法

#### `set_content()` {: #alert_set_content}

```python
def set_content(self, content: str) -> 'AlertWidget'
```

设置警告内容。

#### `set_alert_type()` {: #alert_set_alert_type}

```python
def set_alert_type(self, alert_type: AlertType) -> 'AlertWidget'
```

设置警告类型。

**可用类型:**
- `AlertType.NOTE` - 一般提示（默认）
- `AlertType.TIP` - 小贴士
- `AlertType.IMPORTANT` - 重要信息
- `AlertType.WARNING` - 警告
- `AlertType.CAUTION` - 注意事项

#### `set_title()` {: #alert_set_title}

```python
def set_title(self, title: str) -> 'AlertWidget'
```

设置自定义标题。

### 使用示例

```python
from email_widget.widgets import AlertWidget
from email_widget.core.enums import AlertType

# 基本警告
alert = (AlertWidget()
    .set_content("请注意检查数据完整性。")
    .set_alert_type(AlertType.WARNING)
)

# 自定义标题
important_alert = (AlertWidget()
    .set_content("系统将在今晚进行维护升级。")
    .set_alert_type(AlertType.IMPORTANT)
    .set_title("系统维护通知")
)
```

---

## StatusWidget

::: email_widget.widgets.status_widget.StatusWidget

状态信息组件，展示多个状态项的信息，支持水平和垂直布局。

### 主要方法

#### `set_title()` {: #status_set_title}

```python
def set_title(self, title: str) -> 'StatusWidget'
```

设置状态组标题。

#### `add_status_item()` {: #status_add_status_item}

```python
def add_status_item(self, name: str, value: str, status_type: StatusType) -> 'StatusWidget'
```

添加状态项。

**Parameters:**
- `name` (`str`): 状态项名称
- `value` (`str`): 状态值
- `status_type` (`StatusType`): 状态类型

#### `set_layout()` {: #status_set_layout}

```python
def set_layout(self, layout: LayoutType) -> 'StatusWidget'
```

设置布局类型。

**可用布局:**
- `LayoutType.VERTICAL` - 垂直布局（默认）
- `LayoutType.HORIZONTAL` - 水平布局

### StatusItem 辅助类

```python
class StatusItem:
    def __init__(self, name: str, value: str, status_type: StatusType)
```

### 使用示例

```python
from email_widget.widgets import StatusWidget
from email_widget.core.enums import StatusType, LayoutType

status = (StatusWidget()
    .set_title("系统监控")
    .add_status_item("CPU使用率", "45%", StatusType.SUCCESS)
    .add_status_item("内存使用率", "78%", StatusType.WARNING)
    .add_status_item("磁盘使用率", "92%", StatusType.ERROR)
    .set_layout(LayoutType.HORIZONTAL)
)
```

---

## CardWidget

::: email_widget.widgets.card_widget.CardWidget

卡片组件，提供卡片式的信息容器，支持标题、内容、图标和元数据。

### 主要方法

#### `set_title()` {: #card_set_title}

```python
def set_title(self, title: str) -> 'CardWidget'
```

设置卡片标题。

#### `set_content()` {: #card_set_content}

```python
def set_content(self, content: str) -> 'CardWidget'
```

设置卡片内容。

#### `set_icon()` {: #card_set_icon}

```python
def set_icon(self, icon: str) -> 'CardWidget'
```

设置卡片图标。

#### `set_metadata()` {: #card_set_metadata}

```python
def set_metadata(self, metadata: Dict[str, str]) -> 'CardWidget'
```

设置元数据。

### 使用示例

```python
from email_widget.widgets import CardWidget

card = (CardWidget()
    .set_title("项目状态")
    .set_content("所有功能模块开发完成，正在进行最终测试。")
    .set_icon("🚀")
    .set_metadata({
        "负责人": "张三",
        "预计完成": "2024-02-15",
        "进度": "95%"
    })
)
```

---

## ColumnWidget

::: email_widget.widgets.column_widget.ColumnWidget

多列布局组件，用于创建响应式的多列布局。

### 主要方法

#### `set_columns()` {: #column_set_columns}

```python
def set_columns(self, columns: int) -> 'ColumnWidget'
```

设置列数。

#### `add_widget()` {: #column_add_widget}

```python
def add_widget(self, widget: BaseWidget) -> 'ColumnWidget'
```

添加子 Widget。

#### `add_widgets()` {: #column_add_widgets}

```python
def add_widgets(self, widgets: List[BaseWidget]) -> 'ColumnWidget'
```

批量添加子 Widget。

### 使用示例

```python
from email_widget.widgets import ColumnWidget, CardWidget

# 创建3列布局
layout = ColumnWidget().set_columns(3)

# 添加卡片到每列
cards = [
    CardWidget().set_title("卡片1").set_content("内容1"),
    CardWidget().set_title("卡片2").set_content("内容2"),
    CardWidget().set_title("卡片3").set_content("内容3")
]

layout.add_widgets(cards)
```

---

## QuoteWidget

::: email_widget.widgets.quote_widget.QuoteWidget

引用组件，用于显示引用内容和作者信息。

### 主要方法

#### `set_content()` {: #quote_set_content}

```python
def set_content(self, content: str) -> 'QuoteWidget'
```

设置引用内容。

#### `set_author()` {: #quote_set_author}

```python
def set_author(self, author: str) -> 'QuoteWidget'
```

设置作者信息。

### 使用示例

```python
from email_widget.widgets import QuoteWidget

quote = (QuoteWidget()
    .set_content("代码质量不仅仅是没有bug，更重要的是代码的可读性和可维护性。")
    .set_author("Martin Fowler")
)
```

---

## LogWidget

::: email_widget.widgets.log_widget.LogWidget

日志组件，用于显示日志条目，支持不同的日志级别和语法高亮。

### 主要方法

#### `add_log_entry()` {: #log_add_entry}

```python
def add_log_entry(self, timestamp: str, level: LogLevel, message: str) -> 'LogWidget'
```

添加日志条目。

#### `set_max_height()` {: #log_set_max_height}

```python
def set_max_height(self, height: str) -> 'LogWidget'
```

设置最大高度。

### LogEntry 辅助类

```python
class LogEntry:
    def __init__(self, timestamp: str, level: LogLevel, message: str)
```

### 使用示例

```python
from email_widget.widgets import LogWidget
from email_widget.core.enums import LogLevel

log = (LogWidget()
    .add_log_entry("2024-01-15 10:30:00", LogLevel.INFO, "系统启动成功")
    .add_log_entry("2024-01-15 10:31:15", LogLevel.WARNING, "内存使用率较高")
    .add_log_entry("2024-01-15 10:32:00", LogLevel.ERROR, "数据库连接失败")
    .set_max_height("300px")
)
```

---

## ImageWidget

::: email_widget.widgets.image_widget.ImageWidget

图片组件，用于展示图片内容，支持标题、描述和多种布局选项。

### 主要方法

#### `set_image_url()` {: #image_set_image_url}

```python
def set_image_url(self, image_url: str) -> 'ImageWidget'
```

设置图片URL。

#### `set_title()` {: #image_set_title}

```python
def set_title(self, title: str) -> 'ImageWidget'
```

设置图片标题。

#### `set_description()` {: #image_set_description}

```python
def set_description(self, description: str) -> 'ImageWidget'
```

设置图片描述。

#### `set_max_width()` {: #image_set_max_width}

```python
def set_max_width(self, width: str) -> 'ImageWidget'
```

设置最大宽度。

### 使用示例

```python
from email_widget.widgets import ImageWidget

image = (ImageWidget()
    .set_image_url("https://example.com/screenshot.png")
    .set_title("系统界面截图")
    .set_description("新版本的用户界面展示")
    .set_max_width("600px")
)
```

---

## 通用方法

所有 Widget 都继承自 `BaseWidget`，因此都具有以下通用方法：

### `set_widget_id()` {: #widget_set_widget_id}

```python
def set_widget_id(self, widget_id: str) -> 'BaseWidget'
```

设置 Widget 的唯一ID。

### `render_html()` {: #widget_render_html}

```python
def render_html(self) -> str
```

将 Widget 渲染为 HTML 字符串。

---

## 完整使用示例

### 创建仪表板样式的邮件

```python
from email_widget import Email
from email_widget.widgets import *
from email_widget.core.enums import *

# 创建邮件
email = Email("📊 系统监控仪表板")
email.set_subtitle("实时系统状态和性能指标")

# 1. 关键指标卡片布局
metrics_layout = ColumnWidget().set_columns(4)
metrics_layout.add_widgets([
    CardWidget()
        .set_title("CPU使用率")
        .set_content("45%")
        .set_icon("⚡")
        .set_metadata({"状态": "正常"}),
    
    CardWidget()
        .set_title("内存使用")
        .set_content("8.2GB / 16GB")
        .set_icon("🧠")
        .set_metadata({"使用率": "51%"}),
    
    CardWidget()
        .set_title("磁盘空间")
        .set_content("782GB / 1TB")
        .set_icon("💾")
        .set_metadata({"使用率": "78%"}),
    
    CardWidget()
        .set_title("网络流量")
        .set_content("125 Mbps")
        .set_icon("🌐")
        .set_metadata({"峰值": "250 Mbps"})
])

email.add_widget(metrics_layout)

# 2. 进度指标
email.add_title("系统负载", TextType.SECTION_H2)

progress_layout = ColumnWidget().set_columns(2)
progress_layout.add_widgets([
    ProgressWidget()
        .set_value(45)
        .set_label("CPU负载")
        .set_theme(ProgressTheme.SUCCESS),
    
    CircularProgressWidget()
        .set_value(78)
        .set_label("磁盘使用率")
        .set_size("100px")
])

email.add_widget(progress_layout)

# 3. 服务状态
email.add_title("服务状态", TextType.SECTION_H2)

status = StatusWidget().set_title("关键服务")
status.add_status_item("Web服务", "运行中", StatusType.SUCCESS)
status.add_status_item("数据库", "运行中", StatusType.SUCCESS)
status.add_status_item("缓存服务", "重启中", StatusType.WARNING)
status.add_status_item("备份服务", "离线", StatusType.ERROR)

email.add_widget(status)

# 4. 最近日志
email.add_title("系统日志", TextType.SECTION_H2)

log = LogWidget()
log.add_log_entry("2024-01-15 14:30:00", LogLevel.INFO, "系统自检完成")
log.add_log_entry("2024-01-15 14:28:15", LogLevel.WARNING, "磁盘空间不足警告")
log.add_log_entry("2024-01-15 14:25:00", LogLevel.ERROR, "备份服务连接失败")
log.set_max_height("200px")

email.add_widget(log)

# 5. 重要提醒
alert = AlertWidget()
alert.set_content("系统将在今晚23:00进行例行维护，预计停机2小时。")
alert.set_alert_type(AlertType.IMPORTANT)
alert.set_title("维护通知")

email.add_widget(alert)

# 导出
email.export_html("system_dashboard.html")
```

### 数据分析报告示例

```python
# 创建数据分析邮件
email = Email("📈 销售数据分析报告")

# 引用
quote = QuoteWidget()
quote.set_content("数据是新时代的石油，分析是提炼的技术。")
quote.set_author("Clive Humby")
email.add_widget(quote)

# 图表展示
chart = ChartWidget()
chart.set_image_url("sales_chart.png")
chart.set_title("月度销售趋势")
chart.set_description("显示过去12个月的销售表现")
chart.set_data_summary("总销售额: ¥12,450,000 | 平均增长率: 15%")
email.add_widget(chart)

# 数据表格
import pandas as pd
df = pd.DataFrame({
    '区域': ['华北', '华东', '华南', '西部'],
    '销售额(万)': [2500, 3200, 2800, 1900],
    '增长率': ['12%', '18%', '15%', '8%'],
    '排名': [3, 1, 2, 4]
})

table = TableWidget()
table.set_dataframe(df)
table.set_title("区域销售业绩")
table.set_striped(True)
email.add_widget(table)

# 导出
email.export_html("sales_analysis.html")
```

---

## 最佳实践

### 1. Widget 选择指南

| 需求场景 | 推荐 Widget | 备注 |
|---------|-------------|------|
| 显示标题 | TextWidget | 使用不同的 TextType |
| 展示数据表 | TableWidget | 支持 DataFrame 直接导入 |
| 显示图表 | ChartWidget | 支持 matplotlib 集成 |
| 状态监控 | StatusWidget + ProgressWidget | 组合使用效果更佳 |
| 重要提醒 | AlertWidget | 根据重要程度选择 AlertType |
| 多列布局 | ColumnWidget | 响应式设计 |
| 日志展示 | LogWidget | 自动语法高亮 |

### 2. 性能优化

```python
# ✅ 推荐：批量添加
widgets = []
for data in dataset:
    widget = create_widget(data)
    widgets.append(widget)
email.add_widgets(widgets)

# ❌ 避免：逐个添加
for data in dataset:
    widget = create_widget(data)
    email.add_widget(widget)
```

### 3. 布局设计

```python
# 响应式布局设计
def create_responsive_layout():
    # 主要指标 - 4列布局
    metrics = ColumnWidget().set_columns(4)
    metrics.add_widgets([...])
    
    # 详细数据 - 2列布局
    details = ColumnWidget().set_columns(2)
    details.add_widgets([...])
    
    return [metrics, details]
```

### 4. 错误处理

```python
def safe_widget_creation():
    try:
        # 创建 Widget
        widget = TableWidget().set_dataframe(df)
    except Exception as e:
        # 降级处理
        widget = AlertWidget()
        widget.set_content(f"数据加载失败: {e}")
        widget.set_alert_type(AlertType.ERROR)
    
    return widget
``` 