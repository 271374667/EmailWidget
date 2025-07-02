# 组件概览

EmailWidget 提供了丰富的组件库，涵盖了邮件中常见的各种内容类型。本页面将为您介绍所有可用的组件及其用途。

## 🏗️ 组件分类

### 📝 内容展示组件

#### TextWidget - 文本组件
用于显示各种文本内容，支持多种样式和格式。

```python
from email_widget.widgets import TextWidget
from email_widget.core.enums import TextType, TextAlign

text = TextWidget()
text.set_content("这是一段重要文本")
text.set_text_type(TextType.SECTION_H2)
text.set_align(TextAlign.CENTER)
text.set_color("#0078d4")
```

<div style="background: #f8f9fa; border: 1px solid #e9ecef; border-radius: 4px; padding: 16px; margin: 16px 0;">
    <h2 style="color: #0078d4; text-align: center; margin: 0; font-size: 18px;">这是一段重要文本</h2>
</div>

**适用场景**: 标题、段落、说明文字、通知内容

---

#### ImageWidget - 图片组件
展示图片内容，支持标题、描述和多种布局选项。

```python
from email_widget.widgets import ImageWidget

image = ImageWidget()
image.set_image_url("https://example.com/chart.png")
image.set_title("数据趋势图")
image.set_description("显示最近30天的用户增长趋势")
image.set_max_width("600px")
```

<div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0; text-align: center;">
    <h3 style="color: #323130; margin-bottom: 12px;">数据趋势图</h3>
    <div style="background: #f3f2f1; padding: 40px; border-radius: 4px; color: #605e5c;">
        [图片占位符]
    </div>
    <p style="color: #605e5c; margin-top: 12px; font-size: 14px;">显示最近30天的用户增长趋势</p>
</div>

**适用场景**: 图表展示、产品图片、截图说明

---

### 📊 数据展示组件

#### TableWidget - 表格组件
展示结构化数据，支持表头、索引列、条纹样式等。

```python
from email_widget.widgets import TableWidget, TableCell
from email_widget.core.enums import StatusType

table = TableWidget()
table.set_headers(["项目", "状态", "完成率"])
table.add_row([
    "用户注册功能",
    TableCell("正常", StatusType.SUCCESS),
    "95%"
])
table.set_striped(True)
table.set_show_index(True)
```

<div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0;">
    <table style="width: 100%; border-collapse: collapse;">
        <thead>
            <tr style="background: #f8f9fa;">
                <th style="padding: 12px; text-align: left; border-bottom: 2px solid #e9ecef; font-weight: 600;">索引</th>
                <th style="padding: 12px; text-align: left; border-bottom: 2px solid #e9ecef; font-weight: 600;">项目</th>
                <th style="padding: 12px; text-align: left; border-bottom: 2px solid #e9ecef; font-weight: 600;">状态</th>
                <th style="padding: 12px; text-align: left; border-bottom: 2px solid #e9ecef; font-weight: 600;">完成率</th>
            </tr>
        </thead>
        <tbody>
            <tr style="background: #ffffff;">
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">1</td>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">用户注册功能</td>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef; color: #107c10; font-weight: 600;">正常</td>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">95%</td>
            </tr>
        </tbody>
    </table>
</div>

**适用场景**: 数据报告、状态统计、对比分析

---

#### ChartWidget - 图表组件
专门用于展示图表，支持多种图表类型和数据摘要。

```python
from email_widget.widgets import ChartWidget

chart = ChartWidget()
chart.set_image_url("path/to/sales_chart.png")
chart.set_title("月度销售统计")
chart.set_description("显示各产品线的销售表现")
chart.set_data_summary("总销售额: ¥1,250,000")
```

<div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0; text-align: center;">
    <h3 style="color: #323130; margin-bottom: 12px;">月度销售统计</h3>
    <div style="background: #f8f9fa; padding: 60px; border-radius: 4px; border: 1px dashed #dee2e6; color: #6c757d;">
        [图表占位符]
    </div>
    <p style="color: #605e5c; margin: 12px 0; font-size: 14px;">显示各产品线的销售表现</p>
    <div style="font-size: 13px; color: #8e8e93; margin-top: 12px; padding-top: 12px; border-top: 1px solid #f3f2f1;">
        数据摘要: 总销售额: ¥1,250,000
    </div>
</div>

**适用场景**: 数据可视化、趋势分析、业务报告

---

### 📈 状态监控组件

#### ProgressWidget - 线性进度条
显示任务或进程的完成进度。

```python
from email_widget.widgets import ProgressWidget
from email_widget.core.enums import ProgressTheme

progress = ProgressWidget()
progress.set_value(75)
progress.set_label("项目完成进度")
progress.set_theme(ProgressTheme.SUCCESS)
progress.set_show_percentage(True)
```

<div style="margin: 16px 0;">
    <div style="font-size: 14px; font-weight: 600; color: #323130; margin-bottom: 8px;">项目完成进度</div>
    <div style="width: 100%; height: 20px; background: #e1dfdd; border-radius: 10px; overflow: hidden; position: relative;">
        <div style="width: 75%; height: 100%; background: #107c10; border-radius: 10px;"></div>
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 12px; font-weight: 600; color: #ffffff;">75.0%</div>
    </div>
</div>

**适用场景**: 任务进度、系统负载、完成度统计

---

#### CircularProgressWidget - 圆形进度条
以圆形方式显示进度，适合展示百分比数据。

```python
from email_widget.widgets import CircularProgressWidget

circular = CircularProgressWidget()
circular.set_value(88)
circular.set_label("系统性能")
circular.set_size("120px")
```

<div style="text-align: center; margin: 16px 0;">
    <div style="width: 120px; height: 120px; border-radius: 50%; background: conic-gradient(#0078d4 0deg, #0078d4 316.8deg, #e1dfdd 316.8deg); margin: 0 auto; display: flex; align-items: center; justify-content: center;">
        <div style="width: 80px; height: 80px; background: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; color: #323130;">88%</div>
    </div>
    <div style="margin-top: 8px; font-size: 14px; color: #323130;">系统性能</div>
</div>

**适用场景**: KPI展示、性能监控、达成率统计

---

#### StatusWidget - 状态信息
展示多个状态项的信息，支持水平和垂直布局。

```python
from email_widget.widgets import StatusWidget
from email_widget.core.enums import StatusType, LayoutType

status = StatusWidget()
status.set_title("系统状态")
status.add_status_item("CPU使用率", "45%", StatusType.SUCCESS)
status.add_status_item("内存使用率", "78%", StatusType.WARNING)
status.add_status_item("磁盘空间", "92%", StatusType.ERROR)
status.set_layout(LayoutType.VERTICAL)
```

<div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0;">
    <h3 style="font-size: 16px; font-weight: 600; color: #323130; margin-bottom: 12px;">系统状态</h3>
    <div style="margin: 8px 0; padding: 8px 0; border-bottom: 1px solid #f3f2f1;">
        <div style="font-weight: 500; color: #605e5c; font-size: 14px;">CPU使用率</div>
        <div style="color: #107c10; font-size: 14px; font-weight: 600;">45%</div>
    </div>
    <div style="margin: 8px 0; padding: 8px 0; border-bottom: 1px solid #f3f2f1;">
        <div style="font-weight: 500; color: #605e5c; font-size: 14px;">内存使用率</div>
        <div style="color: #ff8c00; font-size: 14px; font-weight: 600;">78%</div>
    </div>
    <div style="margin: 8px 0; padding: 8px 0; border-bottom: 1px solid #f3f2f1;">
        <div style="font-weight: 500; color: #605e5c; font-size: 14px;">磁盘空间</div>
        <div style="color: #d13438; font-size: 14px; font-weight: 600;">92%</div>
    </div>
</div>

**适用场景**: 系统监控、健康检查、状态汇总

---

### 🎨 交互反馈组件

#### AlertWidget - 警告框
GitHub风格的警告框，支持多种类型的提醒信息。

```python
from email_widget.widgets import AlertWidget
from email_widget.core.enums import AlertType

alert = AlertWidget()
alert.set_content("这是一个重要的系统通知，请及时处理相关事项。")
alert.set_alert_type(AlertType.WARNING)
alert.set_show_icon(True)
```

<div style="background: #fff8e1; border: 1px solid #ffecb3; border-left: 4px solid #ffecb3; border-radius: 6px; padding: 16px; margin: 16px 0; color: #bf8f00;">
    <div style="display: flex; align-items: center; margin-bottom: 8px; font-weight: 600; font-size: 16px;">
        <span style="margin-right: 8px; font-size: 18px;">⚠️</span>
        <span>WARNING</span>
    </div>
    <div style="line-height: 1.5; font-size: 14px;">这是一个重要的系统通知，请及时处理相关事项。</div>
</div>

**适用场景**: 重要通知、错误提醒、操作建议

---

#### CardWidget - 卡片组件
卡片式容器，适合展示结构化信息。

```python
from email_widget.widgets import CardWidget

card = CardWidget()
card.set_title("用户反馈")
card.set_content("用户对新功能的满意度达到了92%，特别是在界面设计和操作便捷性方面获得了很高的评价。")
card.add_metadata("反馈时间", "2024-01-15")
card.add_metadata("样本数量", "1,248")
```

<div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
    <h3 style="font-size: 18px; font-weight: 600; color: #323130; margin-bottom: 8px;">
        ℹ️ 用户反馈
    </h3>
    <div style="color: #323130; line-height: 1.5; font-size: 14px;">
        用户对新功能的满意度达到了92%，特别是在界面设计和操作便捷性方面获得了很高的评价。
    </div>
    <div style="margin-top: 12px; padding-top: 12px; border-top: 1px solid #e1dfdd;">
        <div style="margin: 4px 0; font-size: 13px;">
            <strong>反馈时间:</strong> 2024-01-15
        </div>
        <div style="margin: 4px 0; font-size: 13px;">
            <strong>样本数量:</strong> 1,248
        </div>
    </div>
</div>

**适用场景**: 信息卡片、产品介绍、数据摘要

---

#### QuoteWidget - 引用组件
显示引用内容，支持引用来源标注。

```python
from email_widget.widgets import QuoteWidget

quote = QuoteWidget()
quote.set_content("创新是企业发展的动力，我们必须始终保持对技术的敏锐度和对用户需求的深度理解。")
quote.set_author("张总")
quote.set_source("月度全员大会")
```

<div style="border-left: 4px solid #0078d4; background: #f8f9fa; padding: 16px; margin: 16px 0; font-style: italic;">
    <div style="color: #323130; line-height: 1.6; font-size: 16px; margin-bottom: 12px;">
        "创新是企业发展的动力，我们必须始终保持对技术的敏锐度和对用户需求的深度理解。"
    </div>
    <div style="color: #605e5c; font-size: 14px; text-align: right;">
        — 张总，月度全员大会
    </div>
</div>

**适用场景**: 名言引用、用户评价、重点摘录

---

### 🏗️ 布局组件

#### ColumnWidget - 多列布局
将内容组织成多列显示，提高空间利用率。

```python
from email_widget.widgets import ColumnWidget, TextWidget

column = ColumnWidget()
column.set_columns(2)
column.add_widgets([
    TextWidget().set_content("左列内容"),
    TextWidget().set_content("右列内容")
])
```

<div style="margin: 16px 0;">
    <table style="width: 100%; border-collapse: collapse;">
        <tr>
            <td style="width: 50%; padding: 0 10px; vertical-align: top;">
                <div style="background: #f8f9fa; padding: 16px; border-radius: 4px; text-align: center;">
                    左列内容
                </div>
            </td>
            <td style="width: 50%; padding: 0 10px; vertical-align: top;">
                <div style="background: #f8f9fa; padding: 16px; border-radius: 4px; text-align: center;">
                    右列内容
                </div>
            </td>
        </tr>
    </table>
</div>

**适用场景**: 对比展示、并列信息、空间优化

---

#### LogWidget - 日志组件
展示日志信息，支持多种日志级别和时间戳。

```python
from email_widget.widgets import LogWidget
from email_widget.core.enums import LogLevel

log = LogWidget()
log.set_title("系统日志")
log.add_log_entry("系统启动完成", LogLevel.INFO)
log.add_log_entry("数据库连接异常", LogLevel.ERROR)
log.set_max_entries(50)
```

<div style="background: #1e1e1e; color: #d4d4d4; font-family: 'Courier New', monospace; border-radius: 4px; padding: 16px; margin: 16px 0;">
    <h3 style="color: #d4d4d4; margin-bottom: 12px; font-size: 16px;">系统日志</h3>
    <div style="font-size: 13px; line-height: 1.4;">
        <div style="margin: 4px 0;">
            <span style="color: #4fc3f7;">[INFO]</span> 
            <span style="color: #757575;">2024-01-15 10:30:25</span> 
            <span>系统启动完成</span>
        </div>
        <div style="margin: 4px 0;">
            <span style="color: #f44336;">[ERROR]</span> 
            <span style="color: #757575;">2024-01-15 10:32:10</span> 
            <span>数据库连接异常</span>
        </div>
    </div>
</div>

**适用场景**: 系统日志、操作记录、调试信息

---

## 🔧 组件选择指南

### 根据内容类型选择

| 内容类型 | 推荐组件 | 说明 |
|---------|---------|------|
| 标题文本 | TextWidget | 使用不同的TextType设置层级 |
| 数据表格 | TableWidget | 结构化数据的最佳选择 |
| 图表图片 | ChartWidget | 专门优化了图表展示 |
| 普通图片 | ImageWidget | 支持标题描述的图片展示 |
| 进度信息 | ProgressWidget / CircularProgressWidget | 根据显示风格选择 |
| 状态列表 | StatusWidget | 多个状态项的集中展示 |
| 重要通知 | AlertWidget | 吸引注意力的提醒信息 |
| 信息卡片 | CardWidget | 结构化的信息容器 |
| 引用内容 | QuoteWidget | 突出显示引用文字 |
| 多列布局 | ColumnWidget | 优化空间利用率 |
| 日志记录 | LogWidget | 专门的日志展示格式 |

### 根据使用场景选择

#### 📊 数据报告
- 主标题: `TextWidget` (TextType.SECTION_H2)
- 数据表格: `TableWidget` 
- 图表: `ChartWidget`
- 数据摘要: `StatusWidget`

#### 🚨 系统监控
- 系统状态: `StatusWidget`
- 性能指标: `ProgressWidget` / `CircularProgressWidget`
- 警告信息: `AlertWidget`
- 日志信息: `LogWidget`

#### 📰 业务通知
- 标题: `TextWidget`
- 重要提醒: `AlertWidget`
- 详细信息: `CardWidget`
- 相关数据: `TableWidget`

## 🎨 样式统一性

所有组件都遵循统一的设计规范：

- **字体**: Segoe UI, Tahoma, Arial, sans-serif
- **主色调**: #323130 (深灰), #605e5c (中灰), #0078d4 (蓝色)
- **边框**: #e1dfdd
- **背景**: #ffffff (白色), #f8f9fa (浅灰)
- **圆角**: 4px
- **间距**: 16px (标准), 8px (紧密), 4px (最小)

---

**下一步**: 选择您感兴趣的组件，查看详细的使用指南。推荐从 [文本组件](text-widget.md) 开始学习。 