# Data Report Examples

This page demonstrates how to use EmailWidget to create professional data analysis reports, focusing on integration with pandas and matplotlib.

## Sales Data Report

### Sales Analysis Based on DataFrame

```python
import pandas as pd
from email_widget import Email, TableWidget, ChartWidget, TextWidget
from email_widget.core.enums import TextType, TextAlign
import matplotlib.pyplot as plt

# Create sales data
sales_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Revenue': [150000, 180000, 220000, 195000, 250000, 280000],
    'Orders': [450, 520, 680, 590, 720, 850],
    'AOV': [333, 346, 324, 331, 347, 329]
}

df = pd.DataFrame(sales_data)

# Create email report
email = Email("2024 H1 Sales Data Report")

# Report title
email.add_title("📊 2024 H1 Sales Data Analysis", TextType.TITLE_LARGE)
email.add_text(f"Report Generated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}", 
               align=TextAlign.RIGHT, color="#666666")

# Key metrics summary
email.add_title("📈 Key Metrics", TextType.SECTION_H2)

# Calculate overall metrics
total_sales = df['Revenue'].sum()
total_orders = df['Orders'].sum()
avg_order_value = df['AOV'].mean()
growth_rate = ((df['Revenue'].iloc[-1] - df['Revenue'].iloc[0]) / df['Revenue'].iloc[0]) * 100

# Display key metrics using cards
metrics = [
    ("Total Revenue", f"${total_sales:,}", "💰"),
    ("Total Orders", f"{total_orders:,}", "📋"),
    ("Average AOV", f"${avg_order_value:.0f}", "👤"),
    ("Growth Rate", f"{growth_rate:.1f}%", "📈")
]

for title, value, icon in metrics:
    email.add_card(title=title, content=value, icon=icon)

# Detailed data table
email.add_title("📋 Detailed Data", TextType.SECTION_H2)

# Create table directly from DataFrame
table = TableWidget()
table.set_headers(df.columns.tolist())

# Add data rows with formatting
for _, row in df.iterrows():
    formatted_row = [
        row['Month'],
        f"${row['Revenue']:,}",  # Format currency
        f"{row['Orders']:,}",    # Format quantity
        f"${row['AOV']:.0f}"     # Format AOV
    ]
    table.add_row(formatted_row)

table.set_striped(True)
email.add_widget(table)

# Trend analysis
email.add_title("📉 Trend Analysis", TextType.SECTION_H2)

# Create trend chart
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Revenue'], marker='o', linewidth=2, label='Revenue')
plt.title('Revenue Trend', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart
chart_path = "sales_trend.png"
plt.savefig(chart_path, dpi=150, bbox_inches='tight')
plt.close()

# Add chart to email
chart = ChartWidget()
chart.set_chart_path(chart_path) \
     .set_title("Monthly Revenue Trend") \
     .set_description("Shows monthly revenue changes in H1")
email.add_widget(chart)

# Analysis summary
email.add_title("💡 Analysis Summary", TextType.SECTION_H2)
summary_text = f"""
Based on H1 data analysis:

✅ **Positive Indicators**
• Revenue steadily increased with total growth rate of {growth_rate:.1f}%
• June achieved highest monthly revenue of ${df['Revenue'].max():,}
• Orders continuously growing, indicating expanding customer base

⚠️ **Areas to Monitor**
• April showed slight decline, needs cause analysis
• AOV fluctuates significantly, recommend optimizing product mix

🎯 **H2 Recommendations**
• Maintain growth momentum, target annual revenue of ${total_sales * 2:,}
• Strengthen marketing activities during April period
• Stabilize AOV, enhance product value
"""

email.add_text(summary_text.strip())

email.export_html("sales_report.html")
print("✅ Sales data report generated: sales_report.html")
```

--8<-- "examples/assets/data_reports_html/sales_report.html"

**Key Features:**
- Automatic calculation of key business metrics
- Direct DataFrame to table conversion
- Integrated matplotlib trend chart generation
- Data formatting and visualization

---

## Financial Report

### Income Statement Display

```python
import pandas as pd
from email_widget import Email, TableWidget, ProgressWidget, AlertWidget
from email_widget.core.enums import TextType, ProgressTheme, AlertType

# Financial data
financial_data = {
    'Account': ['Operating Revenue', 'Operating Cost', 'Gross Profit', 'Sales Expense', 'Admin Expense', 'Finance Expense', 'Operating Profit', 'Net Profit'],
    'Current Amount': [2800000, 1680000, 1120000, 280000, 350000, 45000, 445000, 356000],
    'Prior Amount': [2400000, 1440000, 960000, 240000, 320000, 40000, 360000, 288000],
    'Budget Amount': [3000000, 1800000, 1200000, 300000, 360000, 50000, 490000, 392000]
}

df_financial = pd.DataFrame(financial_data)

# Calculate YoY and budget completion
df_financial['YoY Growth'] = ((df_financial['Current Amount'] - df_financial['Prior Amount']) / df_financial['Prior Amount'] * 100).round(1)
df_financial['Budget Completion'] = (df_financial['Current Amount'] / df_financial['Budget Amount'] * 100).round(1)

# Create financial report
email = Email("2024 Q2 Financial Report")

email.add_title("💼 2024 Q2 Financial Report", TextType.TITLE_LARGE)

# Core financial metrics
email.add_title("🎯 Core Metrics", TextType.SECTION_H2)

# Key metric cards
key_metrics = [
    ("Operating Revenue", df_financial.loc[0, 'Current Amount'], "💰"),
    ("Net Profit", df_financial.loc[7, 'Current Amount'], "📈"),
    ("Gross Margin", f"{(df_financial.loc[2, 'Current Amount'] / df_financial.loc[0, 'Current Amount'] * 100):.1f}%", "📊"),
    ("Net Margin", f"{(df_financial.loc[7, 'Current Amount'] / df_financial.loc[0, 'Current Amount'] * 100):.1f}%", "🎯")
]

for title, value, icon in key_metrics:
    if isinstance(value, (int, float)):
        value = f"${value:,}"
    email.add_card(title=title, content=value, icon=icon)

# Financial detail table
email.add_title("📊 Financial Details", TextType.SECTION_H2)

table = TableWidget()
table.set_headers(['Account', 'Current Amount', 'Prior Amount', 'YoY Growth', 'Budget Completion'])

for _, row in df_financial.iterrows():
    formatted_row = [
        row['Account'],
        f"${row['Current Amount']:,}",
        f"${row['Prior Amount']:,}",
        f"{row['YoY Growth']:+.1f}%",
        f"{row['Budget Completion']:.1f}%"
    ]
    table.add_row(formatted_row)

table.set_striped(True)
email.add_widget(table)

# Budget execution analysis
email.add_title("🎯 Budget Execution Analysis", TextType.SECTION_H2)

# Display budget completion progress for key items
key_items = ['Operating Revenue', 'Operating Profit', 'Net Profit']
for item in key_items:
    row = df_financial[df_financial['Account'] == item].iloc[0]
    completion_rate = row['Budget Completion']
    
    # Select theme color based on completion rate
    if completion_rate >= 100:
        theme = ProgressTheme.SUCCESS
    elif completion_rate >= 80:
        theme = ProgressTheme.INFO
    elif completion_rate >= 60:
        theme = ProgressTheme.WARNING
    else:
        theme = ProgressTheme.ERROR
    
    email.add_text(f"📋 {item}")
    email.add_progress(
        value=min(completion_rate, 100),  # Limit display to 100%
        label=f"Budget Completion: {completion_rate:.1f}%",
        theme=theme
    )

# Risk alerts
email.add_title("⚠️ Risk Alerts", TextType.SECTION_H2)

# Analyze budget completion and generate alerts
risk_items = df_financial[df_financial['Budget Completion'] < 90]
if not risk_items.empty:
    for _, item in risk_items.iterrows():
        alert_type = AlertType.WARNING if item['Budget Completion'] >= 80 else AlertType.CAUTION
        email.add_alert(
            f"{item['Account']} budget completion only {item['Budget Completion']:.1f}%, needs attention",
            alert_type,
            "Budget Execution Alert"
        )

# Financial analysis
email.add_title("📈 Financial Analysis", TextType.SECTION_H2)

revenue_growth = df_financial.loc[0, 'YoY Growth']
profit_growth = df_financial.loc[7, 'YoY Growth']

analysis = f"""
**Operating Performance Analysis:**

📊 **Revenue Analysis**
• Operating revenue grew {revenue_growth:.1f}% YoY, performance is {'excellent' if revenue_growth > 15 else 'good' if revenue_growth > 5 else 'average'}
• Revenue budget completion: {df_financial.loc[0, 'Budget Completion']:.1f}%

💰 **Profitability**
• Net profit grew {profit_growth:.1f}% YoY, profitability {'significantly improved' if profit_growth > 20 else 'steadily improved' if profit_growth > 0 else 'declined'}
• Net margin: {(df_financial.loc[7, 'Current Amount'] / df_financial.loc[0, 'Current Amount'] * 100):.1f}%, maintaining healthy levels

🎯 **Budget Execution**
• Operating revenue budget completion: {df_financial.loc[0, 'Budget Completion']:.1f}%
• Net profit budget completion: {df_financial.loc[7, 'Budget Completion']:.1f}%
"""

email.add_text(analysis.strip())

email.export_html("financial_report.html")
print("✅ Financial report generated: financial_report.html")
```

--8<-- "examples/assets/data_reports_html/financial_report.html"

**Professional Features:**
- Complete financial statement structure
- Automatic calculation of YoY growth and budget completion
- Risk alerts and intelligent reminders
- Professional financial analysis terminology

---

## Product Analysis Report

### Multi-dimensional Product Data Analysis

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from email_widget import Email, ChartWidget, TableWidget
from email_widget.core.enums import TextType

# Set font (adjust based on system)
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# Product sales data
products_data = {
    'Product Name': ['Smartphone A', 'Smartphone B', 'Tablet C', 'Laptop D', 'Headphones E', 'Charger F'],
    'Sales Quantity': [1200, 800, 600, 450, 2000, 1500],
    'Unit Price': [2999, 3999, 1999, 5999, 299, 99],
    'Cost': [2100, 2800, 1400, 4200, 180, 60],
    'Inventory': [300, 150, 200, 100, 500, 800],
    'Rating': [4.5, 4.7, 4.2, 4.8, 4.3, 4.0]
}

df_products = pd.DataFrame(products_data)

# Calculate derived metrics
df_products['Revenue'] = df_products['Sales Quantity'] * df_products['Unit Price']
df_products['Gross Profit'] = (df_products['Unit Price'] - df_products['Cost']) * df_products['Sales Quantity']
df_products['Gross Margin'] = ((df_products['Unit Price'] - df_products['Cost']) / df_products['Unit Price'] * 100).round(1)
df_products['Inventory Turnover'] = (df_products['Sales Quantity'] / (df_products['Inventory'] + df_products['Sales Quantity']) * 100).round(1)

# Create product analysis report
email = Email("Product Sales Analysis Report")

email.add_title("📱 Product Sales Analysis Report", TextType.TITLE_LARGE)

# Product portfolio overview
email.add_title("🎯 Product Portfolio Overview", TextType.SECTION_H2)

# Calculate overall metrics
total_revenue = df_products['Revenue'].sum()
total_profit = df_products['Gross Profit'].sum()
avg_rating = df_products['Rating'].mean()
best_seller = df_products.loc[df_products['Sales Quantity'].idxmax(), 'Product Name']

overview_metrics = [
    ("Total Revenue", f"${total_revenue:,}", "💰"),
    ("Total Gross Profit", f"${total_profit:,}", "📈"),
    ("Average Rating", f"{avg_rating:.1f}★", "⭐"),
    ("Best Seller", best_seller, "🏆")
]

for title, value, icon in overview_metrics:
    email.add_card(title=title, content=value, icon=icon)

# Product detail table
email.add_title("📊 Product Sales Details", TextType.SECTION_H2)

table = TableWidget()
table.set_headers(['Product', 'Quantity', 'Unit Price', 'Revenue', 'Gross Margin', 'Rating'])

for _, row in df_products.iterrows():
    formatted_row = [
        row['Product Name'],
        f"{row['Sales Quantity']:,}",
        f"${row['Unit Price']:,}",
        f"${row['Revenue']:,}",
        f"{row['Gross Margin']:.1f}%",
        f"{row['Rating']:.1f}★"
    ]
    table.add_row(formatted_row)

table.set_striped(True)
email.add_widget(table)

# Revenue distribution chart
email.add_title("📈 Revenue Distribution", TextType.SECTION_H2)

plt.figure(figsize=(10, 6))
colors = plt.cm.Set3(range(len(df_products)))
plt.pie(df_products['Revenue'], labels=df_products['Product Name'], 
        autopct='%1.1f%%', startangle=90, colors=colors)
plt.title('Product Revenue Distribution', fontsize=14)
plt.axis('equal')

pie_chart_path = "sales_distribution.png"
plt.savefig(pie_chart_path, dpi=150, bbox_inches='tight')
plt.close()

chart1 = ChartWidget()
chart1.set_chart_path(pie_chart_path) \
      .set_title("Product Revenue Distribution") \
      .set_description("Shows each product's contribution to total revenue")
email.add_widget(chart1)

# Gross margin vs sales volume analysis
email.add_title("🔍 Gross Margin vs Sales Analysis", TextType.SECTION_H2)

plt.figure(figsize=(10, 6))
scatter = plt.scatter(df_products['Sales Quantity'], df_products['Gross Margin'], 
                     s=df_products['Rating']*50, alpha=0.7, c=colors)

# Add product labels
for i, txt in enumerate(df_products['Product Name']):
    plt.annotate(txt, (df_products['Sales Quantity'].iloc[i], df_products['Gross Margin'].iloc[i]),
                xytext=(5, 5), textcoords='offset points', fontsize=8)

plt.xlabel('Sales Quantity')
plt.ylabel('Gross Margin (%)')
plt.title('Product Gross Margin vs Sales (Bubble size represents rating)', fontsize=14)
plt.grid(True, alpha=0.3)

scatter_chart_path = "profit_sales_analysis.png"
plt.savefig(scatter_chart_path, dpi=150, bbox_inches='tight')
plt.close()

chart2 = ChartWidget()
chart2.set_chart_path(scatter_chart_path) \
      .set_title("Gross Margin vs Sales Relationship") \
      .set_description("Analyze relationship between profitability and market performance")
email.add_widget(chart2)

# Product strategy recommendations
email.add_title("💡 Product Strategy Recommendations", TextType.SECTION_H2)

# Analyze product performance
high_margin_products = df_products[df_products['Gross Margin'] > df_products['Gross Margin'].mean()]
high_volume_products = df_products[df_products['Sales Quantity'] > df_products['Sales Quantity'].mean()]
low_stock_products = df_products[df_products['Inventory Turnover'] > 80]

strategy_text = f"""
**Data-driven Product Strategy Recommendations:**

🌟 **Premium Products** (High Gross Margin)
{', '.join(high_margin_products['Product Name'].tolist())}
• Recommend increasing marketing investment to expand market share

📈 **Best Sellers** (High Volume)
{', '.join(high_volume_products['Product Name'].tolist())}
• Maintain adequate inventory, optimize supply chain

⚡ **Fast Movers** (Inventory Turnover >80%)
{', '.join(low_stock_products['Product Name'].tolist()) if not low_stock_products.empty else 'None'}
• Timely restocking to avoid stockouts affecting sales

🎯 **Overall Strategy**
• Focus on marketing high-margin products
• Optimize user experience for low-rated products
• Balance product portfolio, reduce single product dependency
"""

email.add_text(strategy_text.strip())

email.export_html("product_analysis.html")
print("✅ Product analysis report generated: product_analysis.html")
```

--8<-- "examples/assets/data_reports_html/product_analysis.html"

**Analysis Highlights:**
- Multi-dimensional product data analysis
- Visual charts showing product relationships
- Data-driven strategy recommendations
- Comprehensive consideration of volume, profit, rating factors

---

## Customer Analysis Report

### RFM Customer Value Analysis

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from email_widget import Email, TableWidget, ProgressWidget
from email_widget.core.enums import TextType, ProgressTheme

# Generate customer data
np.random.seed(42)
customer_data = {
    'Customer ID': [f'C{str(i).zfill(4)}' for i in range(1, 101)],
    'Days Since Purchase': np.random.randint(1, 365, 100),
    'Purchase Frequency': np.random.randint(1, 20, 100),
    'Purchase Amount': np.random.randint(100, 10000, 100)
}

df_customers = pd.DataFrame(customer_data)

# RFM analysis function
def rfm_analysis(df):
    """RFM customer value analysis"""
    # Calculate RFM quartiles
    r_quartiles = pd.qcut(df['Days Since Purchase'], 4, labels=[4, 3, 2, 1])  # Recent purchases, fewer days = higher score
    f_quartiles = pd.qcut(df['Purchase Frequency'].rank(method='first'), 4, labels=[1, 2, 3, 4])
    m_quartiles = pd.qcut(df['Purchase Amount'], 4, labels=[1, 2, 3, 4])
    
    df['R Score'] = r_quartiles
    df['F Score'] = f_quartiles  
    df['M Score'] = m_quartiles
    
    # Calculate RFM composite score
    df['RFM Score'] = df['R Score'].astype(str) + df['F Score'].astype(str) + df['M Score'].astype(str)
    
    # Customer segmentation
    def customer_segment(rfm_score):
        score = int(rfm_score)
        if score >= 444:
            return 'High Value'
        elif score >= 344:
            return 'High Potential'
        elif score >= 244:
            return 'High Retention'
        elif score >= 144:
            return 'High Risk'
        elif score >= 134:
            return 'Medium Value'
        elif score >= 124:
            return 'Medium Potential'
        elif score >= 114:
            return 'Medium Retention'
        else:
            return 'Medium Risk'
    
    df['Customer Segment'] = df['RFM Score'].apply(customer_segment)
    return df

# Execute RFM analysis
df_rfm = rfm_analysis(df_customers.copy())

# Create customer analysis report
email = Email("RFM Customer Value Analysis Report")

email.add_title("👥 RFM Customer Value Analysis Report", TextType.TITLE_LARGE)

# Customer overview
email.add_title("📊 Customer Overview", TextType.SECTION_H2)

total_customers = len(df_rfm)
avg_frequency = df_rfm['Purchase Frequency'].mean()
avg_monetary = df_rfm['Purchase Amount'].mean()
avg_recency = df_rfm['Days Since Purchase'].mean()

overview_stats = [
    ("Total Customers", f"{total_customers:,}", "👥"),
    ("Avg Purchase Frequency", f"{avg_frequency:.1f} times", "🔄"),
    ("Avg Purchase Amount", f"${avg_monetary:,.0f}", "💰"),
    ("Avg Days Since Purchase", f"{avg_recency:.0f} days", "📅")
]

for title, value, icon in overview_stats:
    email.add_card(title=title, content=value, icon=icon)

# Customer segment statistics
email.add_title("🎯 Customer Segment Distribution", TextType.SECTION_H2)

segment_stats = df_rfm['Customer Segment'].value_counts().sort_index()

table = TableWidget()
table.set_headers(['Customer Level', 'Count', 'Percentage', 'Avg Amount'])

for segment, count in segment_stats.items():
    segment_customers = df_rfm[df_rfm['Customer Segment'] == segment]
    avg_amount = segment_customers['Purchase Amount'].mean()
    percentage = (count / total_customers * 100)
    
    table.add_row([
        segment,
        f"{count:,}",
        f"{percentage:.1f}%",
        f"${avg_amount:,.0f}"
    ])

table.set_striped(True)
email.add_widget(table)

# Customer segment percentage progress bars
email.add_title("📈 Customer Segment Percentages", TextType.SECTION_H2)

# Define themes for customer segments
segment_themes = {
    'High Value': ProgressTheme.SUCCESS,
    'High Potential': ProgressTheme.INFO,
    'High Retention': ProgressTheme.WARNING,
    'High Risk': ProgressTheme.ERROR,
    'Medium Value': ProgressTheme.SUCCESS,
    'Medium Potential': ProgressTheme.INFO,
    'Medium Retention': ProgressTheme.WARNING,
    'Medium Risk': ProgressTheme.ERROR
}

for segment, count in segment_stats.items():
    percentage = (count / total_customers * 100)
    theme = segment_themes.get(segment, ProgressTheme.INFO)
    
    email.add_text(f"🔹 {segment}")
    email.add_progress(
        value=percentage,
        label=f"{count} customers ({percentage:.1f}%)",
        theme=theme
    )

# High-value customer details
email.add_title("⭐ High-Value Customer Analysis", TextType.SECTION_H2)

high_value_customers = df_rfm[df_rfm['Customer Segment'].str.contains('High Value|High Potential')]

if not high_value_customers.empty:
    hv_table = TableWidget()
    hv_table.set_headers(['Customer ID', 'R Score', 'F Score', 'M Score', 'Segment', 'Amount'])
    
    # Show top 10 high-value customers
    for _, customer in high_value_customers.head(10).iterrows():
        hv_table.add_row([
            customer['Customer ID'],
            str(customer['R Score']),
            str(customer['F Score']),
            str(customer['M Score']),
            customer['Customer Segment'],
            f"${customer['Purchase Amount']:,}"
        ])
    
    hv_table.set_striped(True)
    email.add_widget(hv_table)

# Marketing strategy recommendations
email.add_title("💡 Marketing Strategy Recommendations", TextType.SECTION_H2)

# Statistics for customer categories
important_customers_pct = (segment_stats.filter(regex='High').sum() / total_customers * 100)
high_frequency_pct = (len(df_rfm[df_rfm['Purchase Frequency'] > avg_frequency]) / total_customers * 100)

strategy_recommendations = f"""
**RFM Analysis-Based Marketing Strategy Recommendations:**

🎯 **High-Value Customer Retention** ({important_customers_pct:.1f}% of customers)
• High Value: Provide VIP service, personalized recommendations
• High Potential: Increase touchpoint frequency, boost purchase frequency
• High Retention: Regular care, prevent churn
• High Risk: Urgent retention strategy, special offers

📈 **Medium-Value Customer Enhancement**
• Medium Value: Cross-selling, increase average order value
• Medium Potential: Build loyalty, increase purchase frequency
• Medium Retention: Maintain status quo, moderate marketing
• Medium Risk: Churn alert, retention measures

📊 **Key Focus Metrics**
• High-frequency customer percentage: {high_frequency_pct:.1f}%
• Average customer lifecycle: {avg_recency:.0f} days
• Customer value improvement potential: Focus on customers with low F and M scores

💰 **ROI Optimization**
• Allocate 80% of marketing resources to high-value customers
• Use 20% of resources for medium-value customer enhancement
• Regularly review RFM model, optimize segmentation criteria
"""

email.add_text(strategy_recommendations.strip())

email.export_html("rfm_customer_analysis.html")
print("✅ RFM customer analysis report generated: rfm_customer_analysis.html")
```

--8<-- "examples/assets/data_reports_html/rfm_customer_analysis.html"

**Analysis Value:**
- Scientific RFM customer value analysis model
- Automated customer segmentation and strategy recommendations
- Visual display of customer distribution
- Data support for precision marketing

---

## Chart Integration

### Example Chart Integration

This section can include an example of chart integration with code and explanations.

---

## Learning Summary

Through these data report examples, you have mastered:

### 🎯 Core Skills
- **pandas Integration** - Seamless DataFrame to table conversion
- **matplotlib Integration** - Automatic chart generation and embedding
- **Data Calculation** - Automated business metric calculations
- **Formatted Display** - Professional data formatting

### 📊 Report Types
- **Sales Analysis** - Trend analysis and growth calculations
- **Financial Reports** - Income statements and budget analysis
- **Product Analysis** - Multi-dimensional product evaluation
- **Customer Analysis** - RFM value model application

### 💡 Best Practices
- Data-driven insight generation
- Combination of visualization and text explanation
- Automated metric calculation and anomaly alerts
- Data-based strategy recommendations

### 🚀 Advanced Directions
- Learn [System Monitoring](system-monitoring.md) for real-time data display
- Explore [Advanced Examples](real-world.md) for custom extensions
- Reference [Real Applications](real-world.md) to build complete analysis systems

Continue exploring more advanced features to create professional data analysis reports!