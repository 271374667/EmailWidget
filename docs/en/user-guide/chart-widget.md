# ChartWidget

ChartWidget is specifically designed for displaying various charts and data visualization content in emails. It not only supports displaying charts in image formats but also provides rich configuration options to enhance chart presentation.

## 🎯 Widget Preview

--8<-- "assets/chart_widget_component_preview.html"

## ✨ Core Features

- **📊 Multiple Chart Types**: Supports line charts, bar charts, pie charts, and various other chart types
- **🖼️ Image Display**: Supports network images, local files, and Base64 encoded images
- **📝 Detailed Annotations**: Supports titles, descriptions, and data summaries
- **📱 Responsive**: Automatically adapts to different device displays
- **📧 Email Compatible**: Implemented using email client-compatible HTML and CSS

## 🚀 Quick Start

### Basic Usage

```python
from email_widget import Email
from email_widget.widgets import ChartWidget

# 创建基本图表
email = Email("数据报告")

chart = ChartWidget()
chart.set_image_url("https://example.com/sales_chart.png")
chart.set_title("月度销售趋势")
chart.set_description("显示最近6个月的销售数据变化")

email.add_widget(chart)
```

### Advanced Usage

```python
# 带数据摘要的详细图表
performance_chart = ChartWidget()
performance_chart.set_image_url("performance_chart.png")
performance_chart.set_title("系统性能监控")
performance_chart.set_description("展示系统关键性能指标的实时状态")
performance_chart.set_data_summary("平均响应时间: 245ms | 峰值QPS: 12,500 | 错误率: 0.02%")
performance_chart.set_alt_text("系统性能监控图表")
performance_chart.set_max_width("800px")

email.add_widget(performance_chart)
```

📚 **Complete API Documentation**: [ChartWidget API](../api/chart-widget.md)

## 📊 Chart Type Examples

### Trend Line Chart

```python
trend_chart = ChartWidget()
trend_chart.set_image_url("trend_line.png")
trend_chart.set_title("用户增长趋势")
trend_chart.set_description("显示过去12个月的用户注册和活跃用户数量变化")
trend_chart.set_data_summary("新增用户: +15% | 活跃用户: +8% | 留存率: 76%")
```

### Bar Chart

```python
bar_chart = ChartWidget()
bar_chart.set_image_url("sales_by_region.png")
bar_chart.set_title("各地区销售对比")
bar_chart.set_description("展示不同地区的销售业绩和市场占比")
bar_chart.set_data_summary("华东: 35% | 华南: 28% | 华北: 22% | 其他: 15%")
```

### Pie Chart

```python
pie_chart = ChartWidget()
pie_chart.set_image_url("market_share.png")
pie_chart.set_title("市场份额分布")
pie_chart.set_description("各产品线在总营收中的占比情况")
pie_chart.set_data_summary("产品A: 45% | 产品B: 30% | 产品C: 15% | 其他: 10%")
```

## 🔗 Integration with Data Analysis Libraries

### Matplotlib Integration

```python
import matplotlib.pyplot as plt
import numpy as np
from email_widget import Email
from email_widget.widgets import ChartWidget

# 生成数据并创建图表
months = ['1月', '2月', '3月', '4月', '5月', '6月']
sales = [120, 135, 148, 162, 178, 195]

plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker='o', linewidth=2, markersize=8)
plt.title('月度销售趋势', fontsize=16, fontweight='bold')
plt.xlabel('月份')
plt.ylabel('销售额(万元)')
plt.grid(True, alpha=0.3)
plt.tight_layout()

# 保存图表
chart_path = 'monthly_sales.png'
plt.savefig(chart_path, dpi=300, bbox_inches='tight')
plt.close()

# 在邮件中展示
email = Email("销售数据报告")
chart_widget = ChartWidget()
chart_widget.set_image_url(chart_path)
chart_widget.set_title("月度销售趋势分析")
chart_widget.set_description("展示2024年上半年销售业绩的持续增长态势")
chart_widget.set_data_summary(f"总销售额: {sum(sales)}万元 | 平均增长率: {((sales[-1]/sales[0])-1)*100:.1f}%")

email.add_widget(chart_widget)
```

## 📱 Best Practices

### 1. Choosing Appropriate Chart Types

```python
from email_widget import Email
from email_widget.widgets import ChartWidget

email = Email("数据可视化最佳实践")

# 趋势数据 -> 线图
trend_chart = ChartWidget()
trend_chart.set_image_url("time_series.png")
trend_chart.set_title("时间序列趋势")
trend_chart.set_description("适合展示随时间变化的数据")

# 分类对比 -> 柱状图  
comparison_chart = ChartWidget()
comparison_chart.set_image_url("category_comparison.png")
comparison_chart.set_title("分类数据对比")
comparison_chart.set_description("适合展示不同类别之间的比较")

# 占比关系 -> 饼图
proportion_chart = ChartWidget()
proportion_chart.set_image_url("proportion_chart.png")
proportion_chart.set_title("比例分布")
proportion_chart.set_description("适合展示部分与整体的关系")

email.add_widgets([trend_chart, comparison_chart, proportion_chart])
```

--8<-- "assets/temp/chart_choosing_chart_types.html"

### 2. Business Data Dashboard

```python
from email_widget import Email
from email_widget.widgets import ChartWidget, TextWidget
from email_widget.core.enums import TextType

# 创建仪表板邮件
dashboard = Email("业务数据仪表板")

# 添加标题
title = TextWidget()
title.set_content("业务数据仪表板")
title.set_type(TextType.TITLE_LARGE)
title.set_align("center")
dashboard.add_widget(title)

# 创建多个图表
charts_data = [
    {
        'file': 'revenue_trend.png',
        'title': '营收趋势',
        'desc': '月度营收增长情况',
        'summary': '同比增长: +23%'
    },
    {
        'file': 'user_analytics.png', 
        'title': '用户分析',
        'desc': '用户活跃度和留存分析',
        'summary': '月活用户: 2.4M'
    },
    {
        'file': 'product_performance.png',
        'title': '产品表现', 
        'desc': '各产品线业绩对比',
        'summary': '核心产品占比: 68%'
    }
]

for chart_info in charts_data:
    chart = ChartWidget()
    chart.set_image_url(chart_info['file'])
    chart.set_title(chart_info['title'])
    chart.set_description(chart_info['desc'])
    chart.set_data_summary(chart_info['summary'])
    dashboard.add_widget(chart)
```

--8<-- "assets/temp/chart_business_dashboard.html"

### 3. Complete Business Report

```python
from email_widget import Email
from email_widget.widgets import ChartWidget, TextWidget
from email_widget.core.enums import TextType

# 创建业务报告
report = Email("Q4业务分析报告")

# 报告标题
report_title = TextWidget()
report_title.set_content("第四季度业务分析报告")
report_title.set_type(TextType.TITLE_LARGE)
report_title.set_align("center")
report_title.set_color("#0078d4")
report.add_widget(report_title)

# 营收分析图表
revenue_chart = ChartWidget()
revenue_chart.set_image_url("q4_revenue_analysis.png")
revenue_chart.set_title("营收分析")
revenue_chart.set_description("第四季度各月营收情况及与去年同期对比")
revenue_chart.set_data_summary("Q4总营收: ¥18.5M | 同比增长: +15.2% | 环比增长: +8.7%")

# 用户增长图表  
growth_chart = ChartWidget()
growth_chart.set_image_url("user_growth_funnel.png")
growth_chart.set_title("用户增长漏斗")
growth_chart.set_description("从访问到转化的用户流失情况分析")
growth_chart.set_data_summary("访问用户: 2.4M | 注册转化: 12% | 付费转化: 3.2%")

# 产品表现图表
product_chart = ChartWidget()
product_chart.set_image_url("product_performance_matrix.png") 
product_chart.set_title("产品表现矩阵")
product_chart.set_description("各产品线的市场表现和增长潜力分析")
product_chart.set_data_summary("明星产品: 3个 | 问题产品: 1个 | 现金牛产品: 2个")

# 添加到报告
report.add_widgets([revenue_chart, growth_chart, product_chart])
```

--8<-- "assets/temp/chart_business_report.html"

## ⚡ Shortcut Methods

The Email class provides the `add_chart` shortcut method:

```python
# 基础快捷方法
email.add_chart(
    image_url="sales_chart.png",
    title="销售图表"
)

# 带详细信息的快捷方法
email.add_chart(
    image_url="performance_chart.png",
    title="性能监控",
    description="系统关键指标实时监控",
    data_summary="响应时间: 245ms | QPS: 12.5K",
    max_width="800px"
)
```

## 🎯 Style and Size Control

### Image Size Optimization

```python
# 设置最大宽度避免图片过大
large_chart = ChartWidget()
large_chart.set_image_url("wide_chart.png")
large_chart.set_max_width("800px")

# 移动端自适应
responsive_chart = ChartWidget()
responsive_chart.set_image_url("responsive_chart.png")
responsive_chart.set_max_width("100%")  # 自动适配容器宽度
```

### Provide Clear Titles and Descriptions

```python
chart = ChartWidget()
chart.set_title("Q4营收分析")  # 简洁明确的标题
chart.set_description("展示第四季度月度营收变化及同比增长情况")  # 详细说明
chart.set_data_summary("总营收: ¥2.4M | 增长率: +15%")  # 关键数据
chart.set_alt_text("Q4营收分析柱状图")  # 无障碍访问
```

## 🐛 Common Issues

### Q: What to do when images don't display?
A: Check the following:
- Confirm image URL is correct
- Verify image file exists
- Check network connection and access permissions

### Q: How to choose appropriate image formats?
A: Recommend using PNG format for best compatibility:
```python
chart.set_image_url("chart.png")  # ✅ 推荐
# chart.set_image_url("chart.webp")  # ❌ 兼容性较差
```

### Q: Chart displays abnormally on mobile?
A: Set appropriate maximum width:
```python
chart.set_max_width("100%")  # 自动适配
chart.set_max_width("600px")  # 限制最大宽度
```

### Q: How to add data summaries?
A: Use the `set_data_summary()` method:
```python
chart.set_data_summary("关键指标: 转化率 12% | ROI 3.2x | 客单价 ¥890")
```

## 🚨 Important Notes

1. **Image Format**: Recommend PNG format for best compatibility
2. **File Size**: Control image file size to avoid oversized emails
3. **Network Access**: Ensure network image URLs are accessible when sending emails
4. **Alternative Text**: Set meaningful alt_text for all charts
5. **Mobile Adaptation**: Use percentage widths to ensure proper mobile display

## 🔗 Related Widgets

- [ImageWidget](image-widget.md) - Basic image display widget
- [MetricWidget](metric-widget.md) - Data metrics display widget
- [CardWidget](card-widget.md) - Card widget that can contain charts
- [TextWidget](text-widget.md) - Chart titles and descriptions