# 数据报告示例

本页面展示如何使用 EmailWidget 创建专业的数据分析报告，重点介绍与 pandas 和 matplotlib 的集成使用。

## 销售数据报告

### 基于 DataFrame 的销售分析

```python
import pandas as pd
from email_widget import Email, TableWidget, ChartWidget, TextWidget
from email_widget.core.enums import TextType, TextAlign
import matplotlib.pyplot as plt

# 创建销售数据
sales_data = {
    '月份': ['1月', '2月', '3月', '4月', '5月', '6月'],
    '销售额': [150000, 180000, 220000, 195000, 250000, 280000],
    '订单数': [450, 520, 680, 590, 720, 850],
    '客单价': [333, 346, 324, 331, 347, 329]
}

df = pd.DataFrame(sales_data)

# 创建邮件报告
email = Email("2024年上半年销售数据报告")

# 报告标题
email.add_title("📊 2024年上半年销售数据分析", TextType.TITLE_LARGE)
email.add_text(f"报告生成时间: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}", 
               align=TextAlign.RIGHT, color="#666666")

# 关键指标汇总
email.add_title("📈 关键指标", TextType.SECTION_H2)

# 计算总体指标
total_sales = df['销售额'].sum()
total_orders = df['订单数'].sum()
avg_order_value = df['客单价'].mean()
growth_rate = ((df['销售额'].iloc[-1] - df['销售额'].iloc[0]) / df['销售额'].iloc[0]) * 100

# 使用卡片展示关键指标
metrics = [
    ("总销售额", f"¥{total_sales:,}", "💰"),
    ("总订单数", f"{total_orders:,}", "📋"),
    ("平均客单价", f"¥{avg_order_value:.0f}", "👤"),
    ("增长率", f"{growth_rate:.1f}%", "📈")
]

for title, value, icon in metrics:
    email.add_card(title=title, content=value, icon=icon)

# 详细数据表格
email.add_title("📋 详细数据", TextType.SECTION_H2)

# 直接从 DataFrame 创建表格
table = TableWidget()
table.set_headers(df.columns.tolist())

# 添加数据行并格式化
for _, row in df.iterrows():
    formatted_row = [
        row['月份'],
        f"¥{row['销售额']:,}",  # 格式化金额
        f"{row['订单数']:,}",    # 格式化数量
        f"¥{row['客单价']:.0f}" # 格式化客单价
    ]
    table.add_row(formatted_row)

table.set_striped(True)
email.add_widget(table)

# 趋势分析
email.add_title("📉 趋势分析", TextType.SECTION_H2)

# 创建趋势图表
plt.figure(figsize=(10, 6))
plt.plot(df['月份'], df['销售额'], marker='o', linewidth=2, label='销售额')
plt.title('销售额趋势', fontsize=14)
plt.xlabel('月份')
plt.ylabel('销售额 (元)')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()

# 保存图表
chart_path = "sales_trend.png"
plt.savefig(chart_path, dpi=150, bbox_inches='tight')
plt.close()

# 添加图表到邮件
chart = ChartWidget()
chart.set_chart_path(chart_path) \
     .set_title("销售额月度趋势") \
     .set_description("显示上半年销售额的月度变化情况")
email.add_widget(chart)

# 分析总结
email.add_title("💡 分析总结", TextType.SECTION_H2)
summary_text = f"""
根据上半年数据分析：

✅ **积极指标**
• 销售额稳步增长，总增长率达到 {growth_rate:.1f}%
• 6月份创造了单月最高销售额 ¥{df['销售额'].max():,}
• 订单数持续增长，显示客户基础扩大

⚠️ **需要关注**
• 4月份出现小幅回落，需分析原因
• 客单价波动较大，建议优化产品结构

🎯 **下半年建议**
• 保持增长势头，目标年销售额 ¥{total_sales * 2:,}
• 加强4月份同期市场活动
• 稳定客单价，提升产品价值
"""

email.add_text(summary_text.strip())

email.export_html("sales_report.html")
print("✅ 销售数据报告已生成：sales_report.html")
```

**功能特点：**
- 自动计算关键业务指标
- DataFrame 数据直接转换为表格
- 集成 matplotlib 生成趋势图
- 数据格式化和美化展示

---

## 财务报表

### 损益表展示

```python
import pandas as pd
from email_widget import Email, TableWidget, ProgressWidget, AlertWidget
from email_widget.core.enums import TextType, ProgressTheme, AlertType

# 财务数据
financial_data = {
    '科目': ['营业收入', '营业成本', '毛利润', '销售费用', '管理费用', '财务费用', '营业利润', '净利润'],
    '本期金额': [2800000, 1680000, 1120000, 280000, 350000, 45000, 445000, 356000],
    '上期金额': [2400000, 1440000, 960000, 240000, 320000, 40000, 360000, 288000],
    '预算金额': [3000000, 1800000, 1200000, 300000, 360000, 50000, 490000, 392000]
}

df_financial = pd.DataFrame(financial_data)

# 计算同比和预算完成率
df_financial['同比增长'] = ((df_financial['本期金额'] - df_financial['上期金额']) / df_financial['上期金额'] * 100).round(1)
df_financial['预算完成率'] = (df_financial['本期金额'] / df_financial['预算金额'] * 100).round(1)

# 创建财务报告
email = Email("2024年Q2财务报告")

email.add_title("💼 2024年第二季度财务报告", TextType.TITLE_LARGE)

# 核心财务指标
email.add_title("🎯 核心指标", TextType.SECTION_H2)

# 关键指标卡片
key_metrics = [
    ("营业收入", df_financial.loc[0, '本期金额'], "💰"),
    ("净利润", df_financial.loc[7, '本期金额'], "📈"),
    ("毛利率", f"{(df_financial.loc[2, '本期金额'] / df_financial.loc[0, '本期金额'] * 100):.1f}%", "📊"),
    ("净利率", f"{(df_financial.loc[7, '本期金额'] / df_financial.loc[0, '本期金额'] * 100):.1f}%", "🎯")
]

for title, value, icon in key_metrics:
    if isinstance(value, (int, float)):
        value = f"¥{value:,}"
    email.add_card(title=title, content=value, icon=icon)

# 财务数据详表
email.add_title("📊 财务明细", TextType.SECTION_H2)

table = TableWidget()
table.set_headers(['科目', '本期金额', '上期金额', '同比增长', '预算完成率'])

for _, row in df_financial.iterrows():
    formatted_row = [
        row['科目'],
        f"¥{row['本期金额']:,}",
        f"¥{row['上期金额']:,}",
        f"{row['同比增长']:+.1f}%",
        f"{row['预算完成率']:.1f}%"
    ]
    table.add_row(formatted_row)

table.set_striped(True)
email.add_widget(table)

# 预算执行情况
email.add_title("🎯 预算执行分析", TextType.SECTION_H2)

# 为主要科目显示预算完成进度
key_items = ['营业收入', '营业利润', '净利润']
for item in key_items:
    row = df_financial[df_financial['科目'] == item].iloc[0]
    completion_rate = row['预算完成率']
    
    # 根据完成率选择主题色
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
        value=min(completion_rate, 100),  # 限制在100%内显示
        label=f"预算完成率: {completion_rate:.1f}%",
        theme=theme
    )

# 风险提示
email.add_title("⚠️ 风险提示", TextType.SECTION_H2)

# 分析预算完成情况，生成提醒
risk_items = df_financial[df_financial['预算完成率'] < 90]
if not risk_items.empty:
    for _, item in risk_items.iterrows():
        alert_type = AlertType.WARNING if item['预算完成率'] >= 80 else AlertType.CAUTION
        email.add_alert(
            f"{item['科目']}预算完成率仅为{item['预算完成率']:.1f}%，需要重点关注",
            alert_type,
            "预算执行预警"
        )

# 财务分析
email.add_title("📈 财务分析", TextType.SECTION_H2)

revenue_growth = df_financial.loc[0, '同比增长']
profit_growth = df_financial.loc[7, '同比增长']

analysis = f"""
**经营业绩分析：**

📊 **收入分析**
• 营业收入同比增长 {revenue_growth:.1f}%，表现{('优秀' if revenue_growth > 15 else '良好' if revenue_growth > 5 else '一般')}
• 收入预算完成率 {df_financial.loc[0, '预算完成率']:.1f}%

💰 **盈利能力**
• 净利润同比增长 {profit_growth:.1f}%，盈利能力{'显著提升' if profit_growth > 20 else '稳步提升' if profit_growth > 0 else '有所下降'}
• 净利率 {(df_financial.loc[7, '本期金额'] / df_financial.loc[0, '本期金额'] * 100):.1f}%，保持健康水平

🎯 **预算执行**
• 营业收入预算完成率 {df_financial.loc[0, '预算完成率']:.1f}%
• 净利润预算完成率 {df_financial.loc[7, '预算完成率']:.1f}%
"""

email.add_text(analysis.strip())

email.export_html("financial_report.html")
print("✅ 财务报告已生成：financial_report.html")
```

**专业特色：**
- 完整的财务报表结构
- 自动计算同比增长和预算完成率
- 风险预警和智能提醒
- 专业的财务分析用语

---

## 产品分析报表

### 多维度产品数据分析

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from email_widget import Email, ChartWidget, TableWidget
from email_widget.core.enums import TextType

# 设置中文字体（根据系统调整）
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 产品销售数据
products_data = {
    '产品名称': ['智能手机A', '智能手机B', '平板电脑C', '笔记本D', '耳机E', '充电器F'],
    '销售数量': [1200, 800, 600, 450, 2000, 1500],
    '单价': [2999, 3999, 1999, 5999, 299, 99],
    '成本': [2100, 2800, 1400, 4200, 180, 60],
    '库存': [300, 150, 200, 100, 500, 800],
    '评分': [4.5, 4.7, 4.2, 4.8, 4.3, 4.0]
}

df_products = pd.DataFrame(products_data)

# 计算衍生指标
df_products['销售额'] = df_products['销售数量'] * df_products['单价']
df_products['毛利润'] = (df_products['单价'] - df_products['成本']) * df_products['销售数量']
df_products['毛利率'] = ((df_products['单价'] - df_products['成本']) / df_products['单价'] * 100).round(1)
df_products['库存周转'] = (df_products['销售数量'] / (df_products['库存'] + df_products['销售数量']) * 100).round(1)

# 创建产品分析报告
email = Email("产品销售分析报告")

email.add_title("📱 产品销售分析报告", TextType.TITLE_LARGE)

# 产品组合概览
email.add_title("🎯 产品组合概览", TextType.SECTION_H2)

# 计算总体指标
total_revenue = df_products['销售额'].sum()
total_profit = df_products['毛利润'].sum()
avg_rating = df_products['评分'].mean()
best_seller = df_products.loc[df_products['销售数量'].idxmax(), '产品名称']

overview_metrics = [
    ("总销售额", f"¥{total_revenue:,}", "💰"),
    ("总毛利润", f"¥{total_profit:,}", "📈"),
    ("平均评分", f"{avg_rating:.1f}★", "⭐"),
    ("最佳销量", best_seller, "🏆")
]

for title, value, icon in overview_metrics:
    email.add_card(title=title, content=value, icon=icon)

# 产品明细表
email.add_title("📊 产品销售明细", TextType.SECTION_H2)

table = TableWidget()
table.set_headers(['产品', '数量', '单价', '销售额', '毛利率', '评分'])

for _, row in df_products.iterrows():
    formatted_row = [
        row['产品名称'],
        f"{row['销售数量']:,}",
        f"¥{row['单价']:,}",
        f"¥{row['销售额']:,}",
        f"{row['毛利率']:.1f}%",
        f"{row['评分']:.1f}★"
    ]
    table.add_row(formatted_row)

table.set_striped(True)
email.add_widget(table)

# 销售额分布图
email.add_title("📈 销售额分布", TextType.SECTION_H2)

plt.figure(figsize=(10, 6))
colors = plt.cm.Set3(range(len(df_products)))
plt.pie(df_products['销售额'], labels=df_products['产品名称'], 
        autopct='%1.1f%%', startangle=90, colors=colors)
plt.title('各产品销售额占比', fontsize=14)
plt.axis('equal')

pie_chart_path = "sales_distribution.png"
plt.savefig(pie_chart_path, dpi=150, bbox_inches='tight')
plt.close()

chart1 = ChartWidget()
chart1.set_chart_path(pie_chart_path) \
      .set_title("产品销售额分布") \
      .set_description("展示各产品对总销售额的贡献比例")
email.add_widget(chart1)

# 毛利率与销量关系分析
email.add_title("🔍 毛利率与销量分析", TextType.SECTION_H2)

plt.figure(figsize=(10, 6))
scatter = plt.scatter(df_products['销售数量'], df_products['毛利率'], 
                     s=df_products['评分']*50, alpha=0.7, c=colors)

# 添加产品标签
for i, txt in enumerate(df_products['产品名称']):
    plt.annotate(txt, (df_products['销售数量'].iloc[i], df_products['毛利率'].iloc[i]),
                xytext=(5, 5), textcoords='offset points', fontsize=8)

plt.xlabel('销售数量')
plt.ylabel('毛利率 (%)')
plt.title('产品毛利率与销量关系（气泡大小代表评分）', fontsize=14)
plt.grid(True, alpha=0.3)

scatter_chart_path = "profit_sales_analysis.png"
plt.savefig(scatter_chart_path, dpi=150, bbox_inches='tight')
plt.close()

chart2 = ChartWidget()
chart2.set_chart_path(scatter_chart_path) \
      .set_title("毛利率与销量关系") \
      .set_description("分析各产品的盈利能力与市场表现的关系")
email.add_widget(chart2)

# 产品策略建议
email.add_title("💡 产品策略建议", TextType.SECTION_H2)

# 分析各产品表现
high_margin_products = df_products[df_products['毛利率'] > df_products['毛利率'].mean()]
high_volume_products = df_products[df_products['销售数量'] > df_products['销售数量'].mean()]
low_stock_products = df_products[df_products['库存周转'] > 80]

strategy_text = f"""
**基于数据分析的产品策略建议：**

🌟 **优势产品** (高毛利率)
{', '.join(high_margin_products['产品名称'].tolist())}
• 建议加大营销投入，扩大市场份额

📈 **热销产品** (高销量)
{', '.join(high_volume_products['产品名称'].tolist())}
• 保持库存充足，优化供应链

⚡ **快周转产品** (库存周转率>80%)
{', '.join(low_stock_products['产品名称'].tolist()) if not low_stock_products.empty else '暂无'}
• 及时补货，避免缺货影响销售

🎯 **综合策略**
• 重点关注高毛利率产品的市场推广
• 优化低评分产品的用户体验
• 平衡产品组合，降低单一产品依赖
"""

email.add_text(strategy_text.strip())

email.export_html("product_analysis.html")
print("✅ 产品分析报告已生成：product_analysis.html")
```

**分析亮点：**
- 多维度产品数据分析
- 可视化图表展示产品关系
- 基于数据的策略建议
- 综合考虑销量、利润、评分等因素

---

## 客户分析报告

### RFM客户价值分析

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from email_widget import Email, TableWidget, ProgressWidget
from email_widget.core.enums import TextType, ProgressTheme

# 生成客户数据
np.random.seed(42)
customer_data = {
    '客户ID': [f'C{str(i).zfill(4)}' for i in range(1, 101)],
    '最近购买天数': np.random.randint(1, 365, 100),
    '购买频次': np.random.randint(1, 20, 100),
    '购买金额': np.random.randint(100, 10000, 100)
}

df_customers = pd.DataFrame(customer_data)

# RFM分析函数
def rfm_analysis(df):
    """RFM客户价值分析"""
    # 计算RFM分位数
    r_quartiles = pd.qcut(df['最近购买天数'], 4, labels=[4, 3, 2, 1])  # 最近购买，天数越少分值越高
    f_quartiles = pd.qcut(df['购买频次'].rank(method='first'), 4, labels=[1, 2, 3, 4])
    m_quartiles = pd.qcut(df['购买金额'], 4, labels=[1, 2, 3, 4])
    
    df['R分值'] = r_quartiles
    df['F分值'] = f_quartiles  
    df['M分值'] = m_quartiles
    
    # 计算RFM综合分值
    df['RFM综合分值'] = df['R分值'].astype(str) + df['F分值'].astype(str) + df['M分值'].astype(str)
    
    # 客户分级
    def customer_segment(rfm_score):
        score = int(rfm_score)
        if score >= 444:
            return '重要价值客户'
        elif score >= 344:
            return '重要发展客户'
        elif score >= 244:
            return '重要保持客户'
        elif score >= 144:
            return '重要挽留客户'
        elif score >= 134:
            return '一般价值客户'
        elif score >= 124:
            return '一般发展客户'
        elif score >= 114:
            return '一般保持客户'
        else:
            return '一般挽留客户'
    
    df['客户分级'] = df['RFM综合分值'].apply(customer_segment)
    return df

# 执行RFM分析
df_rfm = rfm_analysis(df_customers.copy())

# 创建客户分析报告
email = Email("RFM客户价值分析报告")

email.add_title("👥 RFM客户价值分析报告", TextType.TITLE_LARGE)

# 客户总体概况
email.add_title("📊 客户总体概况", TextType.SECTION_H2)

total_customers = len(df_rfm)
avg_frequency = df_rfm['购买频次'].mean()
avg_monetary = df_rfm['购买金额'].mean()
avg_recency = df_rfm['最近购买天数'].mean()

overview_stats = [
    ("客户总数", f"{total_customers:,}", "👥"),
    ("平均购买频次", f"{avg_frequency:.1f}次", "🔄"),
    ("平均购买金额", f"¥{avg_monetary:,.0f}", "💰"),
    ("平均间隔天数", f"{avg_recency:.0f}天", "📅")
]

for title, value, icon in overview_stats:
    email.add_card(title=title, content=value, icon=icon)

# 客户分级统计
email.add_title("🎯 客户分级分布", TextType.SECTION_H2)

segment_stats = df_rfm['客户分级'].value_counts().sort_index()

table = TableWidget()
table.set_headers(['客户级别', '客户数量', '占比', '平均金额'])

for segment, count in segment_stats.items():
    segment_customers = df_rfm[df_rfm['客户分级'] == segment]
    avg_amount = segment_customers['购买金额'].mean()
    percentage = (count / total_customers * 100)
    
    table.add_row([
        segment,
        f"{count:,}",
        f"{percentage:.1f}%",
        f"¥{avg_amount:,.0f}"
    ])

table.set_striped(True)
email.add_widget(table)

# 各级别客户占比进度条
email.add_title("📈 客户分级占比", TextType.SECTION_H2)

# 定义客户级别对应的主题色
segment_themes = {
    '重要价值客户': ProgressTheme.SUCCESS,
    '重要发展客户': ProgressTheme.INFO,
    '重要保持客户': ProgressTheme.WARNING,
    '重要挽留客户': ProgressTheme.ERROR,
    '一般价值客户': ProgressTheme.SUCCESS,
    '一般发展客户': ProgressTheme.INFO,
    '一般保持客户': ProgressTheme.WARNING,
    '一般挽留客户': ProgressTheme.ERROR
}

for segment, count in segment_stats.items():
    percentage = (count / total_customers * 100)
    theme = segment_themes.get(segment, ProgressTheme.INFO)
    
    email.add_text(f"🔹 {segment}")
    email.add_progress(
        value=percentage,
        label=f"{count}人 ({percentage:.1f}%)",
        theme=theme
    )

# 高价值客户详情
email.add_title("⭐ 高价值客户分析", TextType.SECTION_H2)

high_value_customers = df_rfm[df_rfm['客户分级'].str.contains('重要价值|重要发展')]

if not high_value_customers.empty:
    hv_table = TableWidget()
    hv_table.set_headers(['客户ID', 'R分值', 'F分值', 'M分值', '客户级别', '购买金额'])
    
    # 显示前10个高价值客户
    for _, customer in high_value_customers.head(10).iterrows():
        hv_table.add_row([
            customer['客户ID'],
            str(customer['R分值']),
            str(customer['F分值']),
            str(customer['M分值']),
            customer['客户分级'],
            f"¥{customer['购买金额']:,}"
        ])
    
    hv_table.set_striped(True)
    email.add_widget(hv_table)

# 营销策略建议
email.add_title("💡 营销策略建议", TextType.SECTION_H2)

# 统计各类客户比例
important_customers_pct = (segment_stats.filter(regex='重要').sum() / total_customers * 100)
high_frequency_pct = (len(df_rfm[df_rfm['购买频次'] > avg_frequency]) / total_customers * 100)

strategy_recommendations = f"""
**基于RFM分析的营销策略建议：**

🎯 **重要客户维护** ({important_customers_pct:.1f}%的客户)
• 重要价值客户：提供VIP服务，个性化推荐
• 重要发展客户：增加触达频率，提升购买频次
• 重要保持客户：定期关怀，防止流失
• 重要挽留客户：紧急挽回策略，特别优惠

📈 **一般客户提升**
• 一般价值客户：交叉销售，提升客单价
• 一般发展客户：培养忠诚度，增加购买频次
• 一般保持客户：保持现状，适度营销
• 一般挽留客户：流失预警，挽回措施

🔍 **重点关注指标**
• 高频购买客户占比：{high_frequency_pct:.1f}%
• 平均客户生命周期：{avg_recency:.0f}天
• 客户价值提升潜力：关注F分值和M分值较低的客户

💰 **投入产出优化**
• 80%的营销资源投入到重要客户
• 20%的资源用于一般客户的价值提升
• 定期复评RFM模型，优化客户分级标准
"""

email.add_text(strategy_recommendations.strip())

email.export_html("rfm_customer_analysis.html")
print("✅ RFM客户分析报告已生成：rfm_customer_analysis.html")
```

**分析价值：**
- 科学的RFM客户价值分析模型
- 自动化客户分级和策略建议
- 可视化展示客户分布情况
- 为精准营销提供数据支持

---

## 学习总结

通过这些数据报告示例，您已经掌握了：

### 🎯 核心技能
- **pandas集成** - DataFrame无缝转换为表格
- **matplotlib集成** - 自动生成和嵌入图表
- **数据计算** - 业务指标的自动计算
- **格式化展示** - 专业的数据格式化

### 📊 报告类型
- **销售分析** - 趋势分析和增长计算
- **财务报表** - 损益表和预算分析
- **产品分析** - 多维度产品评估
- **客户分析** - RFM价值模型应用

### 💡 最佳实践
- 数据驱动的洞察生成
- 可视化与文字说明结合
- 自动化指标计算和异常提醒
- 基于数据的策略建议

### 🚀 进阶方向
- 学习 [系统监控](system-monitoring.md) 的实时数据展示
- 探索 [高级示例](advanced.md) 的自定义扩展
- 参考 [实际应用](real-world.md) 构建完整分析系统

继续探索更多高级功能，打造专业的数据分析报告！ 