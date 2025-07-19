# MetricWidget 指标组件

MetricWidget 是一个用于在邮件中展示关键数据指标的组件。它能够显示KPI、数据趋势、业务指标等信息，支持趋势分析、数字格式化和多种布局配置，是数据报告和仪表板邮件的理想选择。

## 🎯 组件预览

--8<-- "assets/metric_widget_component_preview.html"

## ✨ 核心特性

- **📊 数据展示**: 支持数值、单位、趋势变化的完整指标展示
- **📈 趋势分析**: 自动识别趋势方向，提供视觉化的趋势指示
- **🎨 状态主题**: 基于StatusType的主题颜色配置，如成功、警告、错误等
- **📐 布局选择**: 支持水平和垂直布局，适应不同显示需求
- **🔢 数字格式化**: 自动格式化大数字，使用K、M等后缀简化显示
- **📧 邮件兼容**: 使用邮件客户端兼容的HTML和CSS实现

## 🚀 快速开始

### 基础用法

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

### 进阶用法

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

📚 **完整API文档**: [MetricWidget API](../api/metric-widget.md)

## 🎨 样式指南

### 趋势状态类型和颜色

- **success**: 绿色 (#107c10) - 正向增长、达成目标、良好表现
- **warning**: 橙色 (#ff8c00) - 需要关注、轻微恶化、接近阈值
- **error**: 红色 (#d13438) - 负向变化、超出阈值、严重问题
- **info**: 蓝色 (#0078d4) - 中性信息、常规数据、参考指标
- **primary**: 蓝色 (#0078d4) - 重要指标、关键数据、主要KPI

### 数字格式化规则

- **1,000,000+**: 显示为 "1M"、"1.2M"
- **1,000+**: 显示为 "1K"、"5.3K"
- **小于1,000**: 显示原数字 "123"、"89.5"

## 📱 最佳实践

### 1. 业务仪表板

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

### 2. 系统性能监控

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

## ⚡ 快捷方法

Email 类提供了 `add_metric` 快捷方法：

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

## 🐛 常见问题

### Q: 水平布局和垂直布局的选择建议？
A: 
- **水平布局**: 适合3-5个核心指标，在一行内展示
- **垂直布局**: 适合详细指标列表，每个指标占一行

### Q: 如何自定义数字格式？
A: 传入已格式化的字符串作为value：
```python
metric.add_metric("自定义", "1,234.56", "万元")      # 自定义格式
metric.add_metric("百分比", "99.95", "%")            # 保留小数
```

### Q: 趋势不显示怎么办？
A: 确保调用了 `show_trends(True)` 方法。

## 🔗 相关组件

- [ProgressWidget](progress-widget.md) - 进度条展示
- [CircularProgressWidget](circular-progress-widget.md) - 圆形进度指标
- [StatusWidget](status-widget.md) - 状态信息展示
- [CardWidget](card-widget.md) - 可以包含指标的卡片
- [TableWidget](table-widget.md) - 表格形式的数据展示