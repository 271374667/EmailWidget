# 图表组件 (ChartWidget)

ChartWidget 专门用于在邮件中展示各种图表和数据可视化内容。它不仅支持显示图片格式的图表，还提供了丰富的配置选项来增强图表的展示效果。

## 🚀 快速开始

```python
from email_widget.widgets import ChartWidget

# 基本图表展示
chart = ChartWidget()
chart.set_image_url("https://example.com/sales_chart.png")
chart.set_title("月度销售趋势")
chart.set_description("显示最近6个月的销售数据变化")
```

<div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0; text-align: center;">
    <h3 style="color: #323130; margin-bottom: 12px; font-size: 18px; font-weight: 600;">月度销售趋势</h3>
    <div style="background: #f8f9fa; padding: 80px 20px; border-radius: 4px; border: 2px dashed #dee2e6; color: #6c757d; font-size: 16px;">
        [图表占位符 - 月度销售趋势图]
    </div>
    <p style="color: #605e5c; margin: 12px 0; font-size: 14px; line-height: 1.5;">显示最近6个月的销售数据变化</p>
</div>

## 📊 基本用法

### 设置图片来源

ChartWidget 支持多种图片来源：

```python
# 网络图片
chart = ChartWidget()
chart.set_image_url("https://example.com/chart.png")

# 本地文件路径
chart = ChartWidget()
chart.set_image_url("/path/to/local/chart.png")

# Base64 编码图片
chart = ChartWidget()
chart.set_image_url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...")
```

### 添加标题和描述

```python
chart = ChartWidget()
chart.set_image_url("revenue_chart.png")
chart.set_title("年度营收分析")
chart.set_description("展示各季度营收增长情况及同比变化")
chart.set_alt_text("年度营收分析图表")
```

### 数据摘要

为图表添加数据摘要信息：

```python
chart = ChartWidget()
chart.set_image_url("performance_chart.png")
chart.set_title("系统性能监控")
chart.set_data_summary("平均响应时间: 245ms | 峰值QPS: 12,500 | 错误率: 0.02%")
```

<div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0; text-align: center;">
    <h3 style="color: #323130; margin-bottom: 12px; font-size: 18px; font-weight: 600;">系统性能监控</h3>
    <div style="background: #f8f9fa; padding: 60px 20px; border-radius: 4px; border: 2px dashed #dee2e6; color: #6c757d;">
        [性能图表占位符]
    </div>
    <div style="font-size: 13px; color: #8e8e93; margin-top: 12px; padding-top: 12px; border-top: 1px solid #f3f2f1;">
        数据摘要: 平均响应时间: 245ms | 峰值QPS: 12,500 | 错误率: 0.02%
    </div>
</div>

## 🎨 样式配置

### 图片尺寸控制

```python
# 设置最大宽度
chart = ChartWidget()
chart.set_image_url("wide_chart.png")
chart.set_max_width("800px")

# 在移动设备上自动适配
chart = ChartWidget()
chart.set_image_url("responsive_chart.png")
chart.set_max_width("100%")  # 默认值，自动适配容器宽度
```

### 容器样式

```python
# 自定义容器样式
chart = ChartWidget()
chart.set_image_url("custom_chart.png")
chart.set_title("自定义样式图表")
# 注意：容器样式由组件内部管理，确保邮件兼容性
```

## 📈 图表类型示例

### 趋势线图表

```python
trend_chart = ChartWidget()
trend_chart.set_image_url("trend_line.png")
trend_chart.set_title("用户增长趋势")
trend_chart.set_description("显示过去12个月的用户注册和活跃用户数量变化")
trend_chart.set_data_summary("新增用户: +15% | 活跃用户: +8% | 留存率: 76%")
```

### 柱状图表

```python
bar_chart = ChartWidget()
bar_chart.set_image_url("sales_by_region.png")
bar_chart.set_title("各地区销售对比")
bar_chart.set_description("展示不同地区的销售业绩和市场占比")
bar_chart.set_data_summary("华东: 35% | 华南: 28% | 华北: 22% | 其他: 15%")
```

### 饼图

```python
pie_chart = ChartWidget()
pie_chart.set_image_url("market_share.png")
pie_chart.set_title("市场份额分布")
pie_chart.set_description("各产品线在总营收中的占比情况")
pie_chart.set_data_summary("产品A: 45% | 产品B: 30% | 产品C: 15% | 其他: 10%")
```

<div style="display: flex; gap: 16px; margin: 16px 0; flex-wrap: wrap;">
    <div style="flex: 1; min-width: 250px; background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; text-align: center;">
        <h4 style="color: #323130; margin-bottom: 8px; font-size: 16px;">用户增长趋势</h4>
        <div style="background: #f0f9ff; padding: 40px 10px; border-radius: 4px; color: #0369a1; margin: 8px 0;">📈 趋势图</div>
        <div style="font-size: 12px; color: #8e8e93;">新增用户: +15%</div>
    </div>
    <div style="flex: 1; min-width: 250px; background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; text-align: center;">
        <h4 style="color: #323130; margin-bottom: 8px; font-size: 16px;">各地区销售对比</h4>
        <div style="background: #f0fdf4; padding: 40px 10px; border-radius: 4px; color: #166534; margin: 8px 0;">📊 柱状图</div>
        <div style="font-size: 12px; color: #8e8e93;">华东: 35%</div>
    </div>
    <div style="flex: 1; min-width: 250px; background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; text-align: center;">
        <h4 style="color: #323130; margin-bottom: 8px; font-size: 16px;">市场份额分布</h4>
        <div style="background: #fef3c7; padding: 40px 10px; border-radius: 4px; color: #92400e; margin: 8px 0;">🥧 饼图</div>
        <div style="font-size: 12px; color: #8e8e93;">产品A: 45%</div>
    </div>
</div>

## 🔗 与Matplotlib集成

ChartWidget 可以很好地与Python的数据可视化库配合使用：

### 生成图表并展示

```python
import matplotlib.pyplot as plt
import numpy as np
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
chart_widget = ChartWidget()
chart_widget.set_image_url(chart_path)
chart_widget.set_title("月度销售趋势分析")
chart_widget.set_description("展示2024年上半年销售业绩的持续增长态势")
chart_widget.set_data_summary(f"总销售额: {sum(sales)}万元 | 平均增长率: {((sales[-1]/sales[0])-1)*100:.1f}%")
```

### 数据仪表板

```python
import matplotlib.pyplot as plt
import seaborn as sns
from email_widget import Email
from email_widget.widgets import ChartWidget, TextWidget

# 创建仪表板邮件
dashboard = Email("数据仪表板")

# 添加标题
dashboard.add_widget(
    TextWidget()
    .set_content("业务数据仪表板")
    .set_text_type(TextType.SECTION_H2)
    .set_align(TextAlign.CENTER)
)

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

## 📋 完整示例

### 业务报告图表

```python
from email_widget import Email
from email_widget.widgets import ChartWidget, TextWidget
from email_widget.core.enums import TextType

# 创建业务报告
report = Email("Q4业务分析报告")

# 报告标题
report.add_widget(
    TextWidget()
    .set_content("第四季度业务分析报告")
    .set_text_type(TextType.SECTION_H2)
    .set_align(TextAlign.CENTER)
    .set_color("#0078d4")
)

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

# 生成报告
html = report.render_html()
```

## ⚙️ API 参考

### 核心方法

| 方法                   | 参数             | 说明       | 示例                              |
|----------------------|----------------|----------|---------------------------------|
| `set_image_url()`    | `url: str`     | 设置图片URL  | `.set_image_url("chart.png")`   |
| `set_title()`        | `title: str`   | 设置图表标题   | `.set_title("销售趋势")`            |
| `set_description()`  | `desc: str`    | 设置图表描述   | `.set_description("月度销售数据")`    |
| `set_alt_text()`     | `alt: str`     | 设置图片替代文本 | `.set_alt_text("销售图表")`         |
| `set_data_summary()` | `summary: str` | 设置数据摘要   | `.set_data_summary("总计: 100万")` |
| `set_max_width()`    | `width: str`   | 设置最大宽度   | `.set_max_width("600px")`       |

### 高级配置

| 方法                     | 参数           | 说明       | 默认值    |
|------------------------|--------------|----------|--------|
| `set_show_caption()`   | `show: bool` | 是否显示标题描述 | `True` |
| `clear_title()`        | 无            | 清除标题     | -      |
| `clear_description()`  | 无            | 清除描述     | -      |
| `clear_data_summary()` | 无            | 清除数据摘要   | -      |

## 🎯 最佳实践

### 1. 选择合适的图表类型
```python
# 趋势数据 -> 线图
trend_chart = ChartWidget().set_title("时间序列趋势")

# 分类对比 -> 柱状图  
comparison_chart = ChartWidget().set_title("分类数据对比")

# 占比关系 -> 饼图
proportion_chart = ChartWidget().set_title("比例分布")
```

### 2. 提供清晰的标题和描述
```python
chart = ChartWidget()
chart.set_title("Q4营收分析")  # 简洁明确的标题
chart.set_description("展示第四季度月度营收变化及同比增长情况")  # 详细说明
chart.set_data_summary("总营收: ¥2.4M | 增长率: +15%")  # 关键数据
```

### 3. 确保图片质量和尺寸
```python
# 推荐：设置合适的图片尺寸
chart = ChartWidget()
chart.set_max_width("800px")  # 避免图片过大
chart.set_image_url("high_quality_chart.png")  # 使用高质量图片
```

### 4. 添加有意义的数据摘要
```python
# 推荐：提供关键指标摘要
chart = ChartWidget()
chart.set_data_summary("关键指标: 转化率 12% | ROI 3.2x | 客单价 ¥890")
```

## 🚨 注意事项

1. **图片格式**: 推荐使用PNG格式以获得最佳兼容性
2. **文件大小**: 控制图片文件大小，避免邮件过大
3. **网络访问**: 确保网络图片URL在邮件发送时可访问
4. **替代文本**: 为所有图表设置有意义的alt_text
5. **移动适配**: 使用百分比宽度确保移动设备显示正常

## 🔧 故障排除

### 图片无法显示
- 检查图片URL是否正确
- 确认图片文件是否存在
- 验证网络连接和权限

### 布局异常
- 检查max_width设置
- 确认图片尺寸比例
- 验证容器样式

---

**下一步**: 了解 [进度组件](progress-widget.md) 学习如何展示进度和状态信息。 