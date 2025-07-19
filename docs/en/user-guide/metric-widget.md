# MetricWidget

MetricWidget is a component for displaying key data metrics in emails. It can show KPIs, data trends, business metrics and other information, supporting trend analysis, number formatting, and multiple layout configurations, making it ideal for data reports and dashboard emails.

## 🎯 Widget Preview

--8<-- "assets/metric_widget_component_preview.html"

## ✨ Core Features

- **📊 Data Display**: Supports complete metric display including values, units, and trend changes
- **📈 Trend Analysis**: Automatically identifies trend direction, provides visual trend indicators
- **🎨 Status Themes**: Theme color configuration based on StatusType, such as success, warning, error, etc.
- **📏 Layout Options**: Supports horizontal and vertical layouts to adapt to different display needs
- **🔢 Number Formatting**: Automatically formats large numbers, using K, M suffixes to simplify display
- **📧 Email Compatible**: Implemented using email client-compatible HTML and CSS

## 🚀 Quick Start

### Basic Usage

```python
from email_widget import Email
from email_widget.widgets import MetricWidget

# 创建基础指标组件
metric = MetricWidget()
metric.set_title("核心指标")
metric.add_metric("活跃用户", 12345, "人")
metric.add_metric("月收入", "¥1,250,000")
metric.add_metric("转化率", "3.2", "%")

email = Email("业务数据报告")
email.add_widget(metric)
```

### Advanced Usage

```python
# 创建带趋势的详细指标
metric = MetricWidget()
metric.set_title("业务关键指标")
metric.add_metric("新用户注册", 1567, "人", "+15.6%", "success", "较上月增长显著")
metric.add_metric("用户活跃度", "78.9", "%", "+2.3%", "success", "用户参与度提升")
metric.add_metric("平均响应时间", "156", "ms", "+12ms", "warning", "需要优化性能")
metric.add_metric("错误率", "0.23", "%", "-0.1%", "success", "系统稳定性改善")
metric.set_layout("horizontal")
metric.show_trends(True)

email.add_widget(metric)
```

📚 **Complete API Documentation**: [MetricWidget API](../api/metric-widget.md)

## 🎨 Style Guide

### Trend Status Types and Colors

- **success**: Green (#107c10) - Positive growth, target achieved, good performance
- **warning**: Orange (#ff8c00) - Needs attention, slight deterioration, approaching threshold
- **error**: Red (#d13438) - Negative change, exceeding threshold, serious problems
- **info**: Blue (#0078d4) - Neutral information, regular data, reference metrics
- **primary**: Blue (#0078d4) - Important metrics, key data, main KPIs

### Number Formatting Rules

- **1,000,000+**: Display as "1M", "1.2M"
- **1,000+**: Display as "1K", "5.3K"
- **Less than 1,000**: Display original number "123", "89.5"

## 📱 Best Practices

### 1. Business Dashboard

```python
from email_widget import Email
from email_widget.widgets.metric_widget import MetricWidget

# 创建业务数据仪表板邮件
email = Email("业务数据仪表板")

# 核心业务指标
metric1 = MetricWidget()
metric1.set_title("核心KPI")
metric1.add_metric("月活用户", 125436, "人", "+15.6%", "success", "用户增长强劲")
metric1.add_metric("月收入", 2850000, "元", "+18.2%", "success", "收入创历史新高")
metric1.add_metric("转化率", "4.23", "%", "+0.8%", "success", "转化效果提升")
metric1.add_metric("客单价", "168.5", "元", "-2.3%", "warning", "需要关注定价策略")
metric1.set_layout("horizontal")
metric1.show_trends(True)

email.add_widget(metric1)

# 导出HTML文件
email.export_html("business_dashboard.html")
```

--8<-- "assets/metric_business_dashboard.html"

### 2. System Performance Monitoring

```python
from email_widget import Email
from email_widget.widgets.metric_widget import MetricWidget

# 创建系统性能报告邮件
email = Email("系统性能报告")

# 系统资源使用
metric = MetricWidget()
metric.set_title("系统资源")
metric.add_metric("CPU使用率", "45.2", "%", "+2.1%", "warning", "负载略有上升")
metric.add_metric("内存使用率", "78.5", "%", "-1.3%", "success", "内存使用正常")
metric.add_metric("磁盘I/O", "234", "MB/s", "+45MB/s", "info", "读写频率增加")
metric.add_metric("网络带宽", "1.2", "GB/s", "+0.3GB/s", "info", "流量增长稳定")
metric.set_layout("horizontal")

email.add_widget(metric)
```

--8<-- "assets/metric_system_performance.html"

## ⚡ Shortcut Methods

The Email class provides the `add_metric` shortcut method:

```python
# 带参数的快捷方法
email.add_metric(
    title="核心指标",
    metrics=[
        ("指标1", 1234, "单位", "+10%", "success", "描述"),
        ("指标2", "5.6", "%", "-2%", "warning"),
        ("指标3", "¥1,250,000", "", "+15%", "success")
    ],
    layout="horizontal",
    show_trends=True
)
```

## 🐛 Common Issues

### Q: Recommendations for choosing horizontal vs vertical layout?
A: 
- **Horizontal Layout**: Suitable for 3-5 core metrics, displayed in one row
- **Vertical Layout**: Suitable for detailed metric lists, each metric takes one row

### Q: How to customize number format?
A: Pass pre-formatted string as value:
```python
metric.add_metric("自定义", "1,234.56", "万元")      # 自定义格式
metric.add_metric("百分比", "99.95", "%")            # 保留小数
```

### Q: Why don't trends show?
A: Make sure you called the `show_trends(True)` method.

## 🔗 Related Widgets

- [ProgressWidget](progress-widget.md) - Progress bar display
- [CircularProgressWidget](circular-progress-widget.md) - Circular progress metrics
- [StatusWidget](status-widget.md) - Status information display
- [CardWidget](card-widget.md) - Card that can contain metrics
- [TableWidget](table-widget.md) - Tabular data display