# Email 主类

::: email_widget.email.Email

Email 是 EmailWidget 库的核心类，负责管理和渲染邮件内容。它作为 Widget 容器，协调各个组件的渲染和输出。

## 类签名

```python
class Email:
    def __init__(self, title: str = "邮件报告")
```

## 属性

| 属性名 | 类型 | 说明 |
|--------|------|------|
| `title` | `str` | 邮件标题 |
| `subtitle` | `Optional[str]` | 邮件副标题 |
| `footer_text` | `Optional[str]` | 邮件页脚文本 |
| `widgets` | `List[BaseWidget]` | 包含的 Widget 列表 |
| `config` | `EmailConfig` | 邮件配置对象 |

## 构造方法

### `__init__()`

```python
def __init__(self, title: str = "邮件报告")
```

初始化 Email 对象。

**Parameters:**
- `title` (`str`): 邮件标题，默认为"邮件报告"

**示例:**
```python
from email_widget import Email

# 使用默认标题
email1 = Email()

# 自定义标题
email2 = Email("月度数据报告")
```

---

## Widget 管理

### `add_widget()` {: #add_widget}

```python
def add_widget(self, widget: BaseWidget) -> "Email"
```

添加单个 Widget 到邮件中。

**Parameters:**
- `widget` (`BaseWidget`): 要添加的 Widget 对象

**Returns:**
- `Email`: 返回 self 以支持链式调用

**示例:**
```python
from email_widget.widgets import TextWidget

email = Email()
text_widget = TextWidget().set_content("Hello World")
email.add_widget(text_widget)
```

### `add_widgets()` {: #add_widgets}

```python
def add_widgets(self, widgets: List[BaseWidget]) -> "Email"
```

批量添加多个 Widget 到邮件中。

**Parameters:**
- `widgets` (`List[BaseWidget]`): Widget 对象列表

**Returns:**
- `Email`: 返回 self 以支持链式调用

**示例:**
```python
from email_widget.widgets import TextWidget, TableWidget, ChartWidget

widgets = [
    TextWidget().set_content("标题"),
    TableWidget().set_headers(["列1", "列2"]),
    ChartWidget().set_image_url("chart.png")
]

email = Email()
email.add_widgets(widgets)
```

### `clear_widgets()` {: #clear_widgets}

```python
def clear_widgets(self) -> "Email"
```

清空所有 Widget。

**Returns:**
- `Email`: 返回 self 以支持链式调用

**示例:**
```python
email = Email()
# ... 添加一些 Widget
email.clear_widgets()  # 清空所有 Widget
```

### `remove_widget()` {: #remove_widget}

```python
def remove_widget(self, widget_id: str) -> "Email"
```

根据 ID 移除指定的 Widget。

**Parameters:**
- `widget_id` (`str`): 要移除的 Widget 的 ID

**Returns:**
- `Email`: 返回 self 以支持链式调用

**示例:**
```python
email = Email()
widget = TextWidget().set_widget_id("my_text")
email.add_widget(widget)
email.remove_widget("my_text")  # 移除指定 Widget
```

### `get_widget()` {: #get_widget}

```python
def get_widget(self, widget_id: str) -> Optional[BaseWidget]
```

根据 ID 获取指定的 Widget。

**Parameters:**
- `widget_id` (`str`): Widget 的 ID

**Returns:**
- `Optional[BaseWidget]`: 找到的 Widget 对象，如果不存在则返回 None

**示例:**
```python
email = Email()
widget = TextWidget().set_widget_id("my_text")
email.add_widget(widget)

found_widget = email.get_widget("my_text")
if found_widget:
    print(f"找到 Widget: {found_widget.widget_id}")
```

---

## 邮件属性设置

### `set_title()` {: #set_title}

```python
def set_title(self, title: str) -> "Email"
```

设置邮件标题。

**Parameters:**
- `title` (`str`): 邮件标题

**Returns:**
- `Email`: 返回 self 以支持链式调用

### `set_subtitle()` {: #set_subtitle}

```python
def set_subtitle(self, subtitle: Optional[str]) -> "Email"
```

设置邮件副标题。

**Parameters:**
- `subtitle` (`Optional[str]`): 邮件副标题，传入 None 可清除副标题

**Returns:**
- `Email`: 返回 self 以支持链式调用

**示例:**
```python
email = Email("主标题")
email.set_subtitle("详细说明副标题")
```

### `set_footer()` {: #set_footer}

```python
def set_footer(self, footer_text: Optional[str]) -> "Email"
```

设置邮件页脚文本。

**Parameters:**
- `footer_text` (`Optional[str]`): 页脚文本，传入 None 可清除页脚

**Returns:**
- `Email`: 返回 self 以支持链式调用

**示例:**
```python
email = Email()
email.set_footer("本报告由数据团队自动生成 - 2024年")
```

---

## 便捷构造方法

EmailWidget 提供了一系列便捷方法，让您快速添加常用的 Widget 而无需手动创建。

### `add_title()` {: #add_title}

```python
def add_title(self, text: str, text_type: "TextType" = None) -> "Email"
```

快速添加标题 Widget。

**Parameters:**
- `text` (`str`): 标题文本
- `text_type` (`TextType`): 文本类型，默认为 `TextType.TITLE_LARGE`

**Returns:**
- `Email`: 返回 self 以支持链式调用

**示例:**
```python
from email_widget.core.enums import TextType

email = Email()
email.add_title("每日数据报告")  # 使用默认的大标题样式
email.add_title("章节标题", TextType.SECTION_H2)  # 使用二级标题样式
```

### `add_text()` {: #add_text}

```python
def add_text(self, content: str, **kwargs) -> "Email"
```

快速添加文本 Widget。

**Parameters:**
- `content` (`str`): 文本内容
- `**kwargs`: 其他文本属性，如 `color`, `font_size`, `align` 等

**Returns:**
- `Email`: 返回 self 以支持链式调用

**示例:**
```python
email = Email()
email.add_text("这是一段普通文本")
email.add_text("重要提示", color="#ff0000", font_size="18px")
```

### `add_table_from_data()` {: #add_table_from_data}

```python
def add_table_from_data(
    self,
    data: List[List[str]],
    headers: Optional[List[str]] = None,
    title: Optional[str] = None,
    **kwargs,
) -> "Email"
```

从二维数组数据快速创建表格 Widget。

**Parameters:**
- `data` (`List[List[str]]`): 二维数组数据
- `headers` (`Optional[List[str]]`): 表头列表
- `title` (`Optional[str]]`): 表格标题
- `**kwargs`: 其他表格属性

**Returns:**
- `Email`: 返回 self 以支持链式调用

**示例:**
```python
data = [
    ["张三", "销售部", "15000"],
    ["李四", "技术部", "18000"],
    ["王五", "市场部", "12000"]
]
headers = ["姓名", "部门", "薪资"]

email = Email()
email.add_table_from_data(data, headers, title="员工信息统计")
```

### `add_table_from_df()` {: #add_table_from_df}

```python
def add_table_from_df(
    self, df: "pd.DataFrame", title: Optional[str] = None, **kwargs
) -> "Email"
```

从 pandas DataFrame 快速创建表格 Widget。

**Parameters:**
- `df` (`pd.DataFrame`): pandas DataFrame 对象
- `title` (`Optional[str]`): 表格标题
- `**kwargs`: 其他表格属性

**Returns:**
- `Email`: 返回 self 以支持链式调用

**示例:**
```python
import pandas as pd

df = pd.DataFrame({
    '产品': ['iPhone', 'iPad', 'MacBook'],
    '销量': [1200, 800, 600],
    '收入': [120000, 64000, 120000]
})

email = Email()
email.add_table_from_df(df, title="产品销售统计")
```

### `add_alert()` {: #add_alert}

```python
def add_alert(
    self, content: str, alert_type: "AlertType" = None, title: Optional[str] = None
) -> "Email"
```

快速添加警告框 Widget。

**Parameters:**
- `content` (`str`): 警告内容
- `alert_type` (`AlertType`): 警告类型，默认为 `AlertType.NOTE`
- `title` (`Optional[str]`): 自定义标题

**Returns:**
- `Email`: 返回 self 以支持链式调用

**示例:**
```python
from email_widget.core.enums import AlertType

email = Email()
email.add_alert("任务执行成功！", AlertType.TIP)
email.add_alert("注意检查数据", AlertType.WARNING, "重要提醒")
```

### `add_progress()` {: #add_progress}

```python
def add_progress(
    self,
    value: float,
    label: Optional[str] = None,
    max_value: float = 100.0,
    theme: "ProgressTheme" = None,
) -> "Email"
```

快速添加进度条 Widget。

**Parameters:**
- `value` (`float`): 当前进度值
- `label` (`Optional[str]`): 进度条标签
- `max_value` (`float`): 最大值，默认 100.0
- `theme` (`ProgressTheme`): 进度条主题，默认为 `ProgressTheme.PRIMARY`

**Returns:**
- `Email`: 返回 self 以支持链式调用

**示例:**
```python
from email_widget.core.enums import ProgressTheme

email = Email()
email.add_progress(75, "任务完成度", theme=ProgressTheme.SUCCESS)
```

### `add_card()` {: #add_card}

```python
def add_card(
    self,
    title: str,
    content: str,
    icon: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> "Email"
```

快速添加卡片 Widget。

**Parameters:**
- `title` (`str`): 卡片标题
- `content` (`str`): 卡片内容
- `icon` (`Optional[str]`): 图标
- `metadata` (`Optional[Dict[str, str]]`): 元数据

**Returns:**
- `Email`: 返回 self 以支持链式调用

**示例:**
```python
email = Email()
email.add_card(
    title="系统状态",
    content="所有服务运行正常",
    icon="✅",
    metadata={"更新时间": "2024-01-15", "负责人": "张三"}
)
```

### `add_chart_from_plt()` {: #add_chart_from_plt}

```python
def add_chart_from_plt(
    self,
    title: Optional[str] = None,
    description: Optional[str] = None,
    data_summary: Optional[str] = None,
) -> "Email"
```

从 matplotlib 图表快速创建图表 Widget。

!!! note "前置条件"
    使用此方法前需要先创建 matplotlib 图表并调用 `plt.show()` 或类似方法。

**Parameters:**
- `title` (`Optional[str]`): 图表标题
- `description` (`Optional[str]`): 图表描述
- `data_summary` (`Optional[str]`): 数据摘要

**Returns:**
- `Email`: 返回 self 以支持链式调用

**示例:**
```python
import matplotlib.pyplot as plt

# 创建图表
fig, ax = plt.subplots()
ax.bar(['A', 'B', 'C'], [1, 2, 3])
plt.title("销量对比")

# 添加到邮件
email = Email()
email.add_chart_from_plt(
    title="月度销量分析",
    description="显示各产品线销量对比",
    data_summary="总销量: 6 件"
)
```

### `add_status_items()` {: #add_status_items}

```python
def add_status_items(
    self,
    items: List[Dict[str, str]],
    title: Optional[str] = None,
    layout: "LayoutType" = None,
) -> "Email"
```

快速添加状态信息 Widget。

**Parameters:**
- `items` (`List[Dict[str, str]]`): 状态项列表
- `title` (`Optional[str]`): 状态组标题
- `layout` (`LayoutType`): 布局类型，默认为 `LayoutType.VERTICAL`

**Returns:**
- `Email`: 返回 self 以支持链式调用

**示例:**
```python
from email_widget.core.enums import LayoutType

status_items = [
    {"name": "CPU使用率", "value": "45%", "type": "success"},
    {"name": "内存使用率", "value": "78%", "type": "warning"},
    {"name": "磁盘使用率", "value": "92%", "type": "error"}
]

email = Email()
email.add_status_items(
    items=status_items,
    title="系统状态监控",
    layout=LayoutType.HORIZONTAL
)
```

---

## 输出方法

### `export_html()` {: #export_html}

```python
def export_html(
    self, filename: Optional[str] = None, output_dir: Optional[str] = None
) -> Path
```

导出邮件为 HTML 文件。

**Parameters:**
- `filename` (`Optional[str]`): 输出文件名，默认为 `{title}_report.html`
- `output_dir` (`Optional[str]`): 输出目录，默认为当前目录

**Returns:**
- `Path`: 生成的 HTML 文件路径

**示例:**
```python
email = Email("数据报告")
# ... 添加 Widget

# 使用默认文件名
file_path = email.export_html()
print(f"文件已保存到: {file_path}")

# 指定文件名和目录
file_path = email.export_html("my_report.html", "./reports/")
```

### `export_str()` {: #export_str}

```python
def export_str(self) -> str
```

导出邮件为 HTML 字符串。

**Returns:**
- `str`: 完整的 HTML 邮件字符串

**示例:**
```python
email = Email("数据报告")
# ... 添加 Widget

html_content = email.export_str()
print(html_content)

# 可以进一步处理 HTML 内容
with open("custom_report.html", "w", encoding="utf-8") as f:
    f.write(html_content)
```

---

## 工具方法

### `get_widget_count()` {: #get_widget_count}

```python
def get_widget_count(self) -> int
```

获取邮件中的 Widget 数量。

**Returns:**
- `int`: Widget 数量

### `__len__()` {: #__len__}

```python
def __len__(self) -> int
```

获取邮件中的 Widget 数量（`len()` 函数支持）。

**Returns:**
- `int`: Widget 数量

**示例:**
```python
email = Email()
email.add_text("文本1")
email.add_text("文本2")

print(email.get_widget_count())  # 输出: 2
print(len(email))                # 输出: 2
```

### `__str__()` {: #__str__}

```python
def __str__(self) -> str
```

返回邮件的字符串表示。

**Returns:**
- `str`: 邮件信息字符串

**示例:**
```python
email = Email("月度报告")
print(str(email))  # 输出邮件基本信息
```

---

## 完整示例

### 创建复杂邮件报告

```python
from email_widget import Email, TextWidget, TableWidget, ChartWidget, AlertWidget
from email_widget.core.enums import TextType, AlertType, ProgressTheme
import pandas as pd
import matplotlib.pyplot as plt

# 创建邮件
email = Email("📊 月度业务数据报告")
email.set_subtitle("2024年1月业务数据汇总分析")
email.set_footer("本报告由数据团队自动生成 | 更新时间: 2024-01-15")

# 1. 添加概述
email.add_title("执行摘要", TextType.SECTION_H2)
email.add_text(
    "本月业务表现优异，各项指标均达到预期目标。重点关注用户增长和收入提升。",
    color="#323130",
    font_size="16px"
)

# 2. 添加关键指标
email.add_title("关键业绩指标", TextType.SECTION_H2)

# 进度指标
email.add_progress(92, "营收目标完成率", theme=ProgressTheme.SUCCESS)
email.add_progress(78, "用户增长目标", theme=ProgressTheme.WARNING)
email.add_progress(85, "客户满意度", theme=ProgressTheme.INFO)

# 3. 添加数据表格
email.add_title("详细数据分析", TextType.SECTION_H2)

# 从 DataFrame 创建表格
df = pd.DataFrame({
    '产品线': ['iPhone', 'iPad', 'MacBook', 'Apple Watch'],
    '销量': [1200, 800, 600, 900],
    '收入(万元)': [120, 64, 120, 45],
    '同比增长': ['+15%', '+8%', '+22%', '+35%']
})

email.add_table_from_df(df, title="产品销售统计")

# 4. 添加图表
# 假设已经创建了 matplotlib 图表
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 销量图表
ax1.bar(df['产品线'], df['销量'])
ax1.set_title('产品销量对比')
ax1.set_ylabel('销量')

# 收入图表
ax2.pie(df['收入(万元)'], labels=df['产品线'], autopct='%1.1f%%')
ax2.set_title('收入占比')

email.add_chart_from_plt(
    title="📈 销售数据可视化",
    description="显示各产品线的销量对比和收入占比情况",
    data_summary="总销量: 3,500 件 | 总收入: 349 万元"
)

# 5. 添加卡片信息
email.add_card(
    title="🎯 下月目标",
    content="继续保持增长态势，重点提升MacBook和Apple Watch的销量表现。",
    metadata={
        "目标设定时间": "2024-01-15",
        "负责团队": "销售部门",
        "预期收入增长": "15%"
    }
)

# 6. 添加重要提醒
email.add_alert(
    content="由于春节假期影响，2月份数据可能出现波动，请提前做好应对准备。",
    alert_type=AlertType.IMPORTANT,
    title="重要提醒"
)

# 7. 添加系统状态
status_items = [
    {"name": "数据处理系统", "value": "正常", "type": "success"},
    {"name": "报表生成服务", "value": "正常", "type": "success"},
    {"name": "备份系统", "value": "维护中", "type": "warning"}
]

email.add_status_items(
    items=status_items,
    title="🔧 系统状态"
)

# 导出邮件
output_path = email.export_html("monthly_business_report.html", "./reports/")
print(f"📧 月度报告已生成: {output_path}")

# 也可以获取 HTML 字符串进行其他处理
html_content = email.export_str()
print(f"📄 HTML 内容长度: {len(html_content)} 字符")
print(f"📊 包含 Widget 数量: {len(email)}")
```

### 链式调用示例

```python
# 使用链式调用创建邮件
email = (Email("快速报告")
    .set_subtitle("演示链式调用")
    .set_footer("演示报告")
    .add_title("标题")
    .add_text("这是正文内容")
    .add_progress(85, "完成度")
    .add_alert("重要提醒", AlertType.TIP)
)

# 批量添加 Widget
widgets = [
    TextWidget().set_content("Widget 1"),
    TextWidget().set_content("Widget 2"),
    TextWidget().set_content("Widget 3")
]

email.add_widgets(widgets)

# 输出
file_path = email.export_html()
```

---

## 最佳实践

### 1. 邮件结构组织

```python
def create_structured_report():
    email = Email("结构化报告")
    
    # 头部信息
    email.set_subtitle("详细的业务分析报告")
    email.set_footer("数据团队 | 自动生成")
    
    # 按逻辑分组添加内容
    add_executive_summary(email)    # 执行摘要
    add_key_metrics(email)          # 关键指标
    add_detailed_analysis(email)    # 详细分析
    add_recommendations(email)      # 建议和行动项
    
    return email

def add_executive_summary(email):
    email.add_title("执行摘要", TextType.SECTION_H2)
    email.add_text("...")
    
def add_key_metrics(email):
    email.add_title("关键指标", TextType.SECTION_H2)
    # 添加各种指标 Widget
```

### 2. 错误处理

```python
def safe_email_creation():
    try:
        email = Email("安全报告")
        
        # 安全地添加内容
        try:
            email.add_table_from_df(df)
        except Exception as e:
            email.add_alert(f"数据表格加载失败: {e}", AlertType.WARNING)
        
        try:
            email.add_chart_from_plt()
        except Exception as e:
            email.add_alert(f"图表生成失败: {e}", AlertType.WARNING)
            
        return email.export_html()
        
    except Exception as e:
        print(f"邮件创建失败: {e}")
        return None
```

### 3. 性能优化

```python
def optimized_email_creation():
    email = Email("优化报告")
    
    # 批量添加而不是逐个添加
    widgets = []
    for data in large_dataset:
        widget = create_widget_from_data(data)
        widgets.append(widget)
    
    email.add_widgets(widgets)  # 一次性添加所有 Widget
    
    return email
``` 