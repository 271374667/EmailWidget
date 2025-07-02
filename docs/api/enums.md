# 枚举类型

::: email_widget.core.enums

EmailWidget 使用枚举类型来定义各种常量和选项，确保类型安全和代码可读性。所有枚举都继承自 Python 的 `Enum` 基类。

## 文本相关枚举

### TextType

::: email_widget.core.enums.TextType

文本类型枚举，定义了不同的文本样式和语义级别。

```python
class TextType(Enum):
    TITLE_LARGE = "title_large"      # 大标题
    TITLE_SMALL = "title_small"      # 小标题
    BODY = "body"                    # 正文(默认)
    CAPTION = "caption"              # 正文补充
    SECTION_H2 = "section_h2"        # 二级章节标题
    SECTION_H3 = "section_h3"        # 三级章节标题
    SECTION_H4 = "section_h4"        # 四级章节标题
    SECTION_H5 = "section_h5"        # 五级章节标题
```

#### 值说明

| 枚举值 | 描述 | 典型字体大小 | 使用场景 |
|--------|------|-------------|----------|
| `TITLE_LARGE` | 大标题 | 24px | 邮件主标题、报告标题 |
| `TITLE_SMALL` | 小标题 | 20px | 章节标题、模块标题 |
| `BODY` | 正文 | 14px | 普通文本内容 |
| `CAPTION` | 说明文字 | 12px | 图片说明、补充信息 |
| `SECTION_H2` | 二级标题 | 18px | 主要章节 |
| `SECTION_H3` | 三级标题 | 16px | 次要章节 |
| `SECTION_H4` | 四级标题 | 15px | 小节标题 |
| `SECTION_H5` | 五级标题 | 14px | 详细分类 |

#### 使用示例

```python
from email_widget.widgets import TextWidget
from email_widget.core.enums import TextType

# 创建不同类型的文本
title = TextWidget().set_content("数据报告").set_type(TextType.TITLE_LARGE)
section = TextWidget().set_content("销售分析").set_type(TextType.SECTION_H2)
body = TextWidget().set_content("本月销售表现优异").set_type(TextType.BODY)
caption = TextWidget().set_content("数据截止到2024年1月").set_type(TextType.CAPTION)
```

---

### TextAlign

::: email_widget.core.enums.TextAlign

文本对齐方式枚举。

```python
class TextAlign(Enum):
    LEFT = "left"        # 左对齐
    CENTER = "center"    # 居中对齐
    RIGHT = "right"      # 右对齐
    JUSTIFY = "justify"  # 两端对齐
```

#### 使用示例

```python
from email_widget.widgets import TextWidget
from email_widget.core.enums import TextAlign

# 不同对齐方式
left_text = TextWidget().set_content("左对齐文本").set_align(TextAlign.LEFT)
center_text = TextWidget().set_content("居中文本").set_align(TextAlign.CENTER)
right_text = TextWidget().set_content("右对齐文本").set_align(TextAlign.RIGHT)
justify_text = TextWidget().set_content("两端对齐的长文本内容").set_align(TextAlign.JUSTIFY)
```

---

## 状态相关枚举

### StatusType

::: email_widget.core.enums.StatusType

状态类型枚举，定义了不同的状态级别和对应的颜色主题。

```python
class StatusType(Enum):
    SUCCESS = "success"    # 成功状态
    WARNING = "warning"    # 警告状态  
    ERROR = "error"        # 错误状态
    INFO = "info"          # 信息状态
    PRIMARY = "primary"    # 主要状态
```

#### 颜色主题

| 状态类型 | 颜色 | 十六进制值 | 使用场景 |
|---------|------|-----------|----------|
| `SUCCESS` | 绿色 | `#107c10` | 成功、正常、通过 |
| `WARNING` | 橙色 | `#ff8c00` | 警告、注意、待处理 |
| `ERROR` | 红色 | `#d13438` | 错误、失败、危险 |
| `INFO` | 蓝色 | `#0078d4` | 信息、提示、中性 |
| `PRIMARY` | 主色调 | `#0078d4` | 主要、默认、强调 |

#### 使用示例

```python
from email_widget.widgets import StatusWidget, TableWidget, TableCell
from email_widget.core.enums import StatusType

# 状态组件
status = StatusWidget()
status.add_status_item("Web服务", "运行中", StatusType.SUCCESS)
status.add_status_item("数据库", "连接缓慢", StatusType.WARNING)
status.add_status_item("缓存服务", "连接失败", StatusType.ERROR)

# 表格中的状态单元格
table = TableWidget()
table.add_row([
    "系统检查",
    TableCell("通过", StatusType.SUCCESS),
    "2024-01-15"
])
```

---

### AlertType

::: email_widget.core.enums.AlertType

警告类型枚举，基于 GitHub 风格的警告框类型。

```python
class AlertType(Enum):
    NOTE = "note"              # 一般提示
    TIP = "tip"                # 小贴士
    IMPORTANT = "important"     # 重要信息
    WARNING = "warning"         # 警告
    CAUTION = "caution"         # 注意事项
```

#### 样式特征

| 警告类型 | 图标 | 边框颜色 | 背景色 | 使用场景 |
|---------|------|---------|--------|----------|
| `NOTE` | ℹ️ | 蓝色 | 浅蓝 | 一般说明、备注 |
| `TIP` | 💡 | 绿色 | 浅绿 | 建议、技巧 |
| `IMPORTANT` | ❗ | 紫色 | 浅紫 | 重要通知、关键信息 |
| `WARNING` | ⚠️ | 橙色 | 浅橙 | 警告、风险提示 |
| `CAUTION` | 🚨 | 红色 | 浅红 | 严重警告、危险操作 |

#### 使用示例

```python
from email_widget.widgets import AlertWidget
from email_widget.core.enums import AlertType

# 不同类型的警告框
note = AlertWidget().set_content("这是一般提示信息").set_alert_type(AlertType.NOTE)
tip = AlertWidget().set_content("小贴士：定期备份数据").set_alert_type(AlertType.TIP)
important = AlertWidget().set_content("重要：请及时更新密码").set_alert_type(AlertType.IMPORTANT)
warning = AlertWidget().set_content("警告：磁盘空间不足").set_alert_type(AlertType.WARNING)
caution = AlertWidget().set_content("危险：此操作不可撤销").set_alert_type(AlertType.CAUTION)
```

---

## 进度相关枚举

### ProgressTheme

::: email_widget.core.enums.ProgressTheme

进度条主题枚举，定义了不同的进度条颜色主题。

```python
class ProgressTheme(Enum):
    PRIMARY = "primary"    # 主色调
    SUCCESS = "success"    # 成功绿色
    WARNING = "warning"    # 警告橙色
    ERROR = "error"        # 错误红色
    INFO = "info"          # 信息蓝色
```

#### 主题颜色

| 主题 | 颜色 | 适用场景 |
|------|------|----------|
| `PRIMARY` | 主色调蓝 | 一般进度、默认状态 |
| `SUCCESS` | 绿色 | 成功进度、健康状态 |
| `WARNING` | 橙色 | 警告进度、注意状态 |
| `ERROR` | 红色 | 错误进度、危险状态 |
| `INFO` | 蓝色 | 信息进度、中性状态 |

#### 使用示例

```python
from email_widget.widgets import ProgressWidget, CircularProgressWidget
from email_widget.core.enums import ProgressTheme

# 线性进度条
progress = ProgressWidget()
progress.set_value(85).set_theme(ProgressTheme.SUCCESS)

# 圆形进度条  
circular = CircularProgressWidget()
circular.set_value(65).set_theme(ProgressTheme.WARNING)

# 不同主题的进度条
themes_demo = [
    ProgressWidget().set_value(20).set_theme(ProgressTheme.ERROR).set_label("错误率"),
    ProgressWidget().set_value(75).set_theme(ProgressTheme.WARNING).set_label("警告级别"),
    ProgressWidget().set_value(90).set_theme(ProgressTheme.SUCCESS).set_label("成功率"),
    ProgressWidget().set_value(60).set_theme(ProgressTheme.INFO).set_label("信息完整度")
]
```

---

## 布局相关枚举

### LayoutType

::: email_widget.core.enums.LayoutType

布局类型枚举，定义了组件的排列方式。

```python
class LayoutType(Enum):
    HORIZONTAL = "horizontal"  # 水平布局
    VERTICAL = "vertical"      # 垂直布局
```

#### 使用示例

```python
from email_widget.widgets import StatusWidget, ColumnWidget
from email_widget.core.enums import LayoutType

# 状态组件的布局
status_horizontal = StatusWidget().set_layout(LayoutType.HORIZONTAL)
status_vertical = StatusWidget().set_layout(LayoutType.VERTICAL)

# 多列布局（隐式使用水平布局）
columns = ColumnWidget().set_columns(3)  # 3列水平布局
```

---

## 日志相关枚举

### LogLevel

::: email_widget.core.enums.LogLevel

日志级别枚举，定义了不同的日志严重性级别。

```python
class LogLevel(Enum):
    DEBUG = "DEBUG"        # 调试信息
    INFO = "INFO"          # 一般信息
    WARNING = "WARNING"    # 警告信息
    ERROR = "ERROR"        # 错误信息
    CRITICAL = "CRITICAL"  # 严重错误
```

#### 级别说明

| 级别 | 颜色 | 使用场景 | 示例 |
|------|------|----------|------|
| `DEBUG` | 灰色 | 调试信息、详细跟踪 | 函数调用、变量值 |
| `INFO` | 蓝色 | 一般信息、正常操作 | 任务开始、状态更新 |
| `WARNING` | 橙色 | 警告、潜在问题 | 配置问题、性能警告 |
| `ERROR` | 红色 | 错误、操作失败 | 连接失败、数据错误 |
| `CRITICAL` | 深红 | 严重错误、系统故障 | 系统崩溃、数据丢失 |

#### 使用示例

```python
from email_widget.widgets import LogWidget
from email_widget.core.enums import LogLevel

log = LogWidget()
log.add_log_entry("2024-01-15 10:00:00", LogLevel.INFO, "系统启动")
log.add_log_entry("2024-01-15 10:01:00", LogLevel.DEBUG, "加载配置文件")
log.add_log_entry("2024-01-15 10:02:00", LogLevel.WARNING, "内存使用率高")
log.add_log_entry("2024-01-15 10:03:00", LogLevel.ERROR, "数据库连接失败")
log.add_log_entry("2024-01-15 10:04:00", LogLevel.CRITICAL, "系统内存耗尽")
```

---

## 图标相关枚举

### IconType

::: email_widget.core.enums.IconType

图标类型枚举，提供了爬虫和数据处理领域的常用图标。

```python
class IconType(Enum):
    # 数据相关
    DATA = "📊"         # 数据
    DATABASE = "🗄️"     # 数据库
    CHART = "📈"        # 图表
    TABLE = "📋"        # 表格
    REPORT = "📄"       # 报告
    
    # 爬虫相关
    SPIDER = "🕷️"       # 爬虫
    WEB = "🌐"          # 网页
    LINK = "🔗"         # 链接
    SEARCH = "🔍"       # 搜索
    DOWNLOAD = "⬇️"     # 下载
    
    # 系统相关
    SERVER = "🖥️"       # 服务器
    NETWORK = "🌐"      # 网络
    STORAGE = "💾"      # 存储
    MEMORY = "🧠"       # 内存
    CPU = "⚡"          # CPU
    
    # 状态相关
    SUCCESS = "✅"      # 成功
    ERROR = "❌"        # 错误
    WARNING = "⚠️"      # 警告
    INFO = "ℹ️"         # 信息
    PROCESSING = "⚙️"   # 处理中
    
    # 默认图标
    DEFAULT = "📋"      # 默认
```

#### 分类说明

**数据相关图标**
适用于数据展示、报告生成等场景：

```python
from email_widget.widgets import CardWidget
from email_widget.core.enums import IconType

data_card = CardWidget()
data_card.set_icon(IconType.DATA.value)
data_card.set_title("数据概览")

chart_card = CardWidget()
chart_card.set_icon(IconType.CHART.value)
chart_card.set_title("图表分析")
```

**爬虫相关图标**
适用于网络爬虫、数据采集等场景：

```python
spider_card = CardWidget()
spider_card.set_icon(IconType.SPIDER.value)
spider_card.set_title("爬虫任务")

download_card = CardWidget()
download_card.set_icon(IconType.DOWNLOAD.value)
download_card.set_title("下载进度")
```

**系统相关图标**
适用于系统监控、资源管理等场景：

```python
server_card = CardWidget()
server_card.set_icon(IconType.SERVER.value)
server_card.set_title("服务器状态")

memory_card = CardWidget()
memory_card.set_icon(IconType.MEMORY.value)
memory_card.set_title("内存使用")
```

**状态相关图标**
适用于状态提示、结果展示等场景：

```python
success_card = CardWidget()
success_card.set_icon(IconType.SUCCESS.value)
success_card.set_title("操作成功")

warning_alert = AlertWidget()
warning_alert.set_icon(IconType.WARNING.value)
warning_alert.set_content("注意事项")
```

---

## 枚举使用最佳实践

### 1. 类型安全

```python
# ✅ 推荐：使用枚举确保类型安全
from email_widget.core.enums import TextType, AlertType

widget.set_type(TextType.TITLE_LARGE)
alert.set_alert_type(AlertType.WARNING)

# ❌ 避免：使用字符串值
widget.set_type("title_large")  # 容易拼写错误
alert.set_alert_type("warning")  # 没有IDE提示
```

### 2. 语义化选择

```python
# 根据内容语义选择合适的枚举值
title = TextWidget().set_type(TextType.TITLE_LARGE)      # 主标题
section = TextWidget().set_type(TextType.SECTION_H2)     # 章节标题
body = TextWidget().set_type(TextType.BODY)              # 正文
note = TextWidget().set_type(TextType.CAPTION)           # 说明文字
```

### 3. 主题一致性

```python
# 保持同一报告中主题颜色的一致性
def create_themed_widgets(theme_color="success"):
    if theme_color == "success":
        progress_theme = ProgressTheme.SUCCESS
        status_type = StatusType.SUCCESS
        alert_type = AlertType.TIP
    elif theme_color == "warning":
        progress_theme = ProgressTheme.WARNING
        status_type = StatusType.WARNING
        alert_type = AlertType.WARNING
    
    return {
        "progress": ProgressWidget().set_theme(progress_theme),
        "status": StatusWidget().add_status_item("状态", "值", status_type),
        "alert": AlertWidget().set_alert_type(alert_type)
    }
```

### 4. 条件选择

```python
def get_status_by_value(value: float) -> StatusType:
    """根据数值选择合适的状态类型"""
    if value >= 90:
        return StatusType.SUCCESS
    elif value >= 70:
        return StatusType.WARNING
    elif value >= 50:
        return StatusType.INFO
    else:
        return StatusType.ERROR

def get_progress_theme(percentage: float) -> ProgressTheme:
    """根据百分比选择进度条主题"""
    if percentage >= 80:
        return ProgressTheme.SUCCESS
    elif percentage >= 60:
        return ProgressTheme.INFO
    elif percentage >= 40:
        return ProgressTheme.WARNING
    else:
        return ProgressTheme.ERROR
```

---

## 完整示例

### 状态监控仪表板

```python
from email_widget import Email
from email_widget.widgets import *
from email_widget.core.enums import *

def create_monitoring_dashboard():
    email = Email("🖥️ 系统监控仪表板")
    
    # 1. 系统指标卡片
    metrics = ColumnWidget().set_columns(4)
    
    # CPU指标
    cpu_status = StatusType.SUCCESS if 45 < 70 else StatusType.WARNING
    cpu_card = CardWidget()
    cpu_card.set_title("CPU使用率")
    cpu_card.set_content("45%")
    cpu_card.set_icon(IconType.CPU.value)
    
    # 内存指标
    memory_status = StatusType.WARNING if 78 > 70 else StatusType.SUCCESS
    memory_card = CardWidget()
    memory_card.set_title("内存使用")
    memory_card.set_content("78%")
    memory_card.set_icon(IconType.MEMORY.value)
    
    # 存储指标
    storage_status = StatusType.ERROR if 92 > 85 else StatusType.SUCCESS
    storage_card = CardWidget()
    storage_card.set_title("存储空间")
    storage_card.set_content("92%")
    storage_card.set_icon(IconType.STORAGE.value)
    
    # 网络指标
    network_card = CardWidget()
    network_card.set_title("网络状态")
    network_card.set_content("正常")
    network_card.set_icon(IconType.NETWORK.value)
    
    metrics.add_widgets([cpu_card, memory_card, storage_card, network_card])
    email.add_widget(metrics)
    
    # 2. 进度指标
    email.add_title("资源使用情况", TextType.SECTION_H2)
    
    progress_layout = ColumnWidget().set_columns(2)
    
    # CPU进度条
    cpu_progress = ProgressWidget()
    cpu_progress.set_value(45)
    cpu_progress.set_label("CPU负载")
    cpu_progress.set_theme(ProgressTheme.SUCCESS)
    
    # 内存圆形进度
    memory_circular = CircularProgressWidget()
    memory_circular.set_value(78)
    memory_circular.set_label("内存使用率")
    
    progress_layout.add_widgets([cpu_progress, memory_circular])
    email.add_widget(progress_layout)
    
    # 3. 服务状态
    email.add_title("服务状态", TextType.SECTION_H2)
    
    services = StatusWidget()
    services.set_title("关键服务监控")
    services.add_status_item("Web服务", "运行中", StatusType.SUCCESS)
    services.add_status_item("数据库", "运行中", StatusType.SUCCESS)
    services.add_status_item("缓存服务", "重启中", StatusType.WARNING)
    services.add_status_item("监控服务", "离线", StatusType.ERROR)
    services.set_layout(LayoutType.VERTICAL)
    
    email.add_widget(services)
    
    # 4. 告警信息
    if storage_status == StatusType.ERROR:
        storage_alert = AlertWidget()
        storage_alert.set_content("存储空间使用率超过90%，请及时清理磁盘空间。")
        storage_alert.set_alert_type(AlertType.CAUTION)
        storage_alert.set_title("存储告警")
        email.add_widget(storage_alert)
    
    # 5. 系统日志
    email.add_title("最近日志", TextType.SECTION_H2)
    
    log = LogWidget()
    log.add_log_entry("2024-01-15 14:30:00", LogLevel.INFO, "系统自检完成")
    log.add_log_entry("2024-01-15 14:28:15", LogLevel.WARNING, "内存使用率超过75%")
    log.add_log_entry("2024-01-15 14:25:00", LogLevel.ERROR, "存储空间不足")
    log.add_log_entry("2024-01-15 14:20:00", LogLevel.CRITICAL, "监控服务连接丢失")
    log.set_max_height("200px")
    
    email.add_widget(log)
    
    return email

# 生成报告
dashboard = create_monitoring_dashboard()
dashboard.export_html("monitoring_dashboard.html")
```

这个示例展示了如何综合使用各种枚举类型来创建一个完整的系统监控仪表板，包括：

- 使用 `IconType` 为卡片添加语义化图标
- 根据数值条件选择合适的 `StatusType`
- 使用不同的 `ProgressTheme` 表示不同的状态
- 通过 `LogLevel` 区分日志的重要性
- 使用 `AlertType` 提供不同级别的告警
- 通过 `TextType` 创建层次化的标题结构 