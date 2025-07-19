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

# Create basic chart
email = Email("Data Report")

chart = ChartWidget()
chart.set_image_url("https://example.com/sales_chart.png")
chart.set_title("Monthly Sales Trends")
chart.set_description("Shows sales data changes over the last 6 months")

email.add_widget(chart)
```

### Advanced Usage

```python
# Detailed chart with data summary
performance_chart = ChartWidget()
performance_chart.set_image_url("performance_chart.png")
performance_chart.set_title("System Performance Monitoring")
performance_chart.set_description("Displays real-time status of system key performance indicators")
performance_chart.set_data_summary("Average Response Time: 245ms | Peak QPS: 12,500 | Error Rate: 0.02%")
performance_chart.set_alt_text("System performance monitoring chart")
performance_chart.set_max_width("800px")

email.add_widget(performance_chart)
```

📚 **Complete API Documentation**: [ChartWidget API](../api/chart-widget.md)

## 📊 Chart Type Examples

### Trend Line Chart

```python
trend_chart = ChartWidget()
trend_chart.set_image_url("trend_line.png")
trend_chart.set_title("User Growth Trend")
trend_chart.set_description("Shows user registration and active user count changes over the past 12 months")
trend_chart.set_data_summary("New Users: +15% | Active Users: +8% | Retention Rate: 76%")
```

### Bar Chart

```python
bar_chart = ChartWidget()
bar_chart.set_image_url("sales_by_region.png")
bar_chart.set_title("Regional Sales Comparison")
bar_chart.set_description("Shows sales performance and market share by region")
bar_chart.set_data_summary("East China: 35% | South China: 28% | North China: 22% | Others: 15%")
```

### Pie Chart

```python
pie_chart = ChartWidget()
pie_chart.set_image_url("market_share.png")
pie_chart.set_title("Market Share Distribution")
pie_chart.set_description("Shows each product line's share of total revenue")
pie_chart.set_data_summary("Product A: 45% | Product B: 30% | Product C: 15% | Others: 10%")
```

## 🔗 Integration with Data Analysis Libraries

### Matplotlib Integration

```python
import matplotlib.pyplot as plt
import numpy as np
from email_widget import Email
from email_widget.widgets import ChartWidget

# Generate data and create chart
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [120, 135, 148, 162, 178, 195]

plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker='o', linewidth=2, markersize=8)
plt.title('Monthly Sales Trends', fontsize=16, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Sales (10K)')
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save chart
chart_path = 'monthly_sales.png'
plt.savefig(chart_path, dpi=300, bbox_inches='tight')
plt.close()

# Display in email
email = Email("Sales Data Report")
chart_widget = ChartWidget()
chart_widget.set_image_url(chart_path)
chart_widget.set_title("Monthly Sales Trend Analysis")
chart_widget.set_description("Shows continuous growth in sales performance for the first half of 2024")
chart_widget.set_data_summary(f"Total Sales: {sum(sales)}0K | Average Growth Rate: {((sales[-1]/sales[0])-1)*100:.1f}%")

email.add_widget(chart_widget)
```

## 📱 Best Practices

### 1. Choosing Appropriate Chart Types

```python
from email_widget import Email
from email_widget.widgets import ChartWidget

email = Email("Data Visualization Best Practices")

# Trend data -> Line chart
trend_chart = ChartWidget()
trend_chart.set_image_url("time_series.png")
trend_chart.set_title("Time Series Trends")
trend_chart.set_description("Suitable for displaying data changes over time")

# Category comparison -> Bar chart  
comparison_chart = ChartWidget()
comparison_chart.set_image_url("category_comparison.png")
comparison_chart.set_title("Category Data Comparison")
comparison_chart.set_description("Suitable for displaying comparisons between different categories")

# Proportion relationship -> Pie chart
proportion_chart = ChartWidget()
proportion_chart.set_image_url("proportion_chart.png")
proportion_chart.set_title("Proportion Distribution")
proportion_chart.set_description("Suitable for displaying part-to-whole relationships")

email.add_widgets([trend_chart, comparison_chart, proportion_chart])
```

--8<-- "assets/temp/chart_choosing_chart_types.html"

### 2. Business Data Dashboard

```python
from email_widget import Email
from email_widget.widgets import ChartWidget, TextWidget
from email_widget.core.enums import TextType

# Create dashboard email
dashboard = Email("Business Data Dashboard")

# Add title
title = TextWidget()
title.set_content("Business Data Dashboard")
title.set_type(TextType.TITLE_LARGE)
title.set_align("center")
dashboard.add_widget(title)

# Create multiple charts
charts_data = [
    {
        'file': 'revenue_trend.png',
        'title': 'Revenue Trends',
        'desc': 'Monthly revenue growth situation',
        'summary': 'YoY Growth: +23%'
    },
    {
        'file': 'user_analytics.png', 
        'title': 'User Analytics',
        'desc': 'User activity and retention analysis',
        'summary': 'Monthly Active Users: 2.4M'
    },
    {
        'file': 'product_performance.png',
        'title': 'Product Performance', 
        'desc': 'Performance comparison of product lines',
        'summary': 'Core Product Share: 68%'
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

# Create business report
report = Email("Q4 Business Analysis Report")

# Report title
report_title = TextWidget()
report_title.set_content("Fourth Quarter Business Analysis Report")
report_title.set_type(TextType.TITLE_LARGE)
report_title.set_align("center")
report_title.set_color("#0078d4")
report.add_widget(report_title)

# Revenue analysis chart
revenue_chart = ChartWidget()
revenue_chart.set_image_url("q4_revenue_analysis.png")
revenue_chart.set_title("Revenue Analysis")
revenue_chart.set_description("Q4 monthly revenue and year-over-year comparison")
revenue_chart.set_data_summary("Q4 Total Revenue: ¥18.5M | YoY Growth: +15.2% | QoQ Growth: +8.7%")

# User growth chart  
growth_chart = ChartWidget()
growth_chart.set_image_url("user_growth_funnel.png")
growth_chart.set_title("User Growth Funnel")
growth_chart.set_description("User churn analysis from visits to conversion")
growth_chart.set_data_summary("Visitors: 2.4M | Registration Rate: 12% | Payment Rate: 3.2%")

# Product performance chart
product_chart = ChartWidget()
product_chart.set_image_url("product_performance_matrix.png") 
product_chart.set_title("Product Performance Matrix")
product_chart.set_description("Market performance and growth potential analysis of product lines")
product_chart.set_data_summary("Star Products: 3 | Problem Products: 1 | Cash Cow Products: 2")

# Add to report
report.add_widgets([revenue_chart, growth_chart, product_chart])
```

--8<-- "assets/temp/chart_business_report.html"

## ⚡ Shortcut Methods

The Email class provides the `add_chart` shortcut method:

```python
# Basic shortcut method
email.add_chart(
    image_url="sales_chart.png",
    title="Sales Chart"
)

# Shortcut method with detailed information
email.add_chart(
    image_url="performance_chart.png",
    title="Performance Monitor",
    description="Real-time monitoring of system key metrics",
    data_summary="Response Time: 245ms | QPS: 12.5K",
    max_width="800px"
)
```

## 🎯 Style and Size Control

### Image Size Optimization

```python
# Set maximum width to avoid oversized images
large_chart = ChartWidget()
large_chart.set_image_url("wide_chart.png")
large_chart.set_max_width("800px")

# Mobile responsive
responsive_chart = ChartWidget()
responsive_chart.set_image_url("responsive_chart.png")
responsive_chart.set_max_width("100%")  # Auto-adapt to container width
```

### Provide Clear Titles and Descriptions

```python
chart = ChartWidget()
chart.set_title("Q4 Revenue Analysis")  # Clear and concise title
chart.set_description("Shows Q4 monthly revenue changes and year-over-year growth")  # Detailed explanation
chart.set_data_summary("Total Revenue: ¥2.4M | Growth Rate: +15%")  # Key data
chart.set_alt_text("Q4 revenue analysis bar chart")  # Accessibility
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
chart.set_image_url("chart.png")  # ✅ Recommended
# chart.set_image_url("chart.webp")  # ❌ Poor compatibility
```

### Q: Chart displays abnormally on mobile?
A: Set appropriate maximum width:
```python
chart.set_max_width("100%")  # Auto-adapt
chart.set_max_width("600px")  # Limit maximum width
```

### Q: How to add data summaries?
A: Use the `set_data_summary()` method:
```python
chart.set_data_summary("Key Metrics: Conversion Rate 12% | ROI 3.2x | Average Order Value ¥890")
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