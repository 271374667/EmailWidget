# MetricWidget 指标组件

MetricWidget 是一个用于在邮件中展示关键数据指标的组件。它能够显示KPI、数据趋势、业务指标等信息，支持趋势分析、数字格式化和多种布局配置，是数据报告和仪表板邮件的理想选择。

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

# 创建邮件
email = Email("业务数据报告")

# 创建基础指标组件
metric = MetricWidget()
metric.set_title("核心指标")
metric.add_metric("活跃用户", 12345, "人")
metric.add_metric("月收入", "¥1,250,000")
metric.add_metric("转化率", "3.2", "%")

email.add_widget(metric)

# 使用快捷方法
email.add_metric("系统性能", [
    ("CPU使用率", "45.2", "%", "+2.1%", "warning"),
    ("内存使用", "78.5", "%", "-1.3%", "success"),
    ("磁盘空间", "23.8", "GB", "+5.2GB", "info")
])

# 导出HTML
email.export_html("metric_demo.html")
```

### 带趋势分析的指标

```python
# 创建带趋势的详细指标
metric = (MetricWidget()
    .set_title("业务关键指标")
    .add_metric("新用户注册", 1567, "人", "+15.6%", "success", "较上月增长显著")
    .add_metric("用户活跃度", "78.9", "%", "+2.3%", "success", "用户参与度提升")
    .add_metric("平均响应时间", "156", "ms", "+12ms", "warning", "需要优化性能")
    .add_metric("错误率", "0.23", "%", "-0.1%", "success", "系统稳定性改善")
    .add_metric("服务可用性", "99.95", "%", "-0.02%", "warning", "略有下降")
    .set_layout("horizontal")
    .show_trends(True))

email.add_widget(metric)
```

## 📖 API 参考

### 基本方法

#### `add_metric(label, value, unit="", trend="", trend_type=None, description="") -> MetricWidget`
添加指标数据。

**参数:**
- `label (str)`: 指标名称标签
- `value (Union[str, int, float])`: 指标数值
- `unit (str)`: 数值单位，可选
- `trend (str)`: 趋势变化，如"+12.3%"、"-5.6%"
- `trend_type (Union[str, StatusType, None])`: 趋势状态类型
- `description (str)`: 指标描述信息，可选

**示例:**
```python
metric.add_metric("用户数", 12345, "人", "+15.6%", "success", "月度增长良好")
metric.add_metric("收入", 1250000, "元", "+12.3%", "success")
metric.add_metric("转化率", "3.2", "%", "-0.8%", "warning")
```

#### `set_title(title) -> MetricWidget`
设置指标组标题。

**参数:**
- `title (str)`: 指标组标题

**示例:**
```python
metric.set_title("核心业务指标")
```

#### `set_layout(layout) -> MetricWidget`
设置指标布局方式。

**参数:**
- `layout (str)`: 布局方式，"horizontal"（水平）或"vertical"（垂直）

**示例:**
```python
metric.set_layout("horizontal")  # 水平排列
metric.set_layout("vertical")    # 垂直排列
```

#### `show_trends(show=True) -> MetricWidget`
设置是否显示趋势信息。

**参数:**
- `show (bool)`: 是否显示趋势和变化率

**示例:**
```python
metric.show_trends(True)   # 显示趋势
metric.show_trends(False)  # 隐藏趋势
```

### 管理方法

#### `clear_metrics() -> MetricWidget`
清空所有指标数据。

**示例:**
```python
metric.clear_metrics()
```

#### `remove_metric(index) -> MetricWidget`
根据索引移除指标。

**参数:**
- `index (int)`: 要移除的指标索引

**示例:**
```python
metric.remove_metric(0)  # 移除第一个指标
```

### 只读属性

- `metrics`: 获取所有指标数据列表
- `title`: 获取指标组标题
- `metric_count`: 获取指标总数
- `layout`: 获取当前布局方式

```python
print(f"指标总数: {metric.metric_count}")
print(f"布局方式: {metric.layout}")
for m in metric.metrics:
    print(f"指标: {m['label']} = {m['value']}{m['unit']}")
```

## 🎨 样式指南

### 趋势状态类型和颜色

#### 成功状态 (success)
```python
metric.add_metric("用户增长", "1234", "人", "+15.6%", "success")
```
- 颜色: 绿色 (#107c10)
- 图标: ↗
- 适用于: 正向增长、达成目标、良好表现

#### 警告状态 (warning)
```python
metric.add_metric("响应时间", "156", "ms", "+12ms", "warning")
```
- 颜色: 橙色 (#ff8c00)
- 图标: →
- 适用于: 需要关注、轻微恶化、接近阈值

#### 错误状态 (error)
```python
metric.add_metric("错误率", "1.2", "%", "+0.5%", "error")
```
- 颜色: 红色 (#d13438)
- 图标: ↘
- 适用于: 负向变化、超出阈值、严重问题

#### 信息状态 (info)
```python
metric.add_metric("在线用户", "567", "人", "+23", "info")
```
- 颜色: 蓝色 (#0078d4)
- 图标: →
- 适用于: 中性信息、常规数据、参考指标

#### 主要状态 (primary)
```python
metric.add_metric("核心指标", "89.5", "%", "+2.1%", "primary")
```
- 颜色: 蓝色 (#0078d4)
- 图标: ●
- 适用于: 重要指标、关键数据、主要KPI

#### 中性状态 (neutral)
```python
metric.add_metric("稳定指标", "100", "%", "0%", "neutral")
```
- 颜色: 灰色 (#8e8e93)
- 图标: —
- 适用于: 无变化、平稳数据、基准值

### 自动趋势检测

当不指定趋势类型时，组件会自动判断：

```python
metric.add_metric("增长指标", "100", "%", "+5%")   # 自动识别为success
metric.add_metric("下降指标", "95", "%", "-3%")    # 自动识别为error
metric.add_metric("平稳指标", "100", "%", "0%")    # 自动识别为neutral
```

### 数字格式化规则

- **1,000,000+**: 显示为 "1M"、"1.2M"
- **1,000+**: 显示为 "1K"、"5.3K"
- **小于1,000**: 显示原数字 "123"、"89.5"

```python
metric.add_metric("大数字", 1234567)    # 显示为 "1M"
metric.add_metric("中等数字", 5432)     # 显示为 "5K"
metric.add_metric("小数字", 123)       # 显示为 "123"
```

## 📱 最佳实践

### 1. 业务仪表板

```python
email = Email("业务数据仪表板")

# 核心业务指标
email.add_metric("核心KPI", [
    ("月活用户", 125436, "人", "+15.6%", "success", "用户增长强劲"),
    ("月收入", 2850000, "元", "+18.2%", "success", "收入创历史新高"),
    ("转化率", "4.23", "%", "+0.8%", "success", "转化效果提升"),
    ("客单价", "168.5", "元", "-2.3%", "warning", "需要关注定价策略")
], layout="horizontal", show_trends=True)

# 运营指标
operations_metric = MetricWidget()
operations_metric.set_title("运营效率")
operations_metric.add_metric("页面访问量", 567890, "次", "+22.1%", "success")
operations_metric.add_metric("跳出率", "24.5", "%", "-3.2%", "success")
operations_metric.add_metric("平均停留", "3.8", "分钟", "+0.6分钟", "info")
operations_metric.add_metric("注册转化", "12.3", "%", "+1.8%", "success")
operations_metric.set_layout("vertical")
operations_metric.show_trends(True)

email.add_widget(operations_metric)
```

### 2. 系统性能监控

```python
email = Email("系统性能报告")

# 系统资源使用
email.add_metric("系统资源", [
    ("CPU使用率", "45.2", "%", "+2.1%", "warning", "负载略有上升"),
    ("内存使用率", "78.5", "%", "-1.3%", "success", "内存使用正常"),
    ("磁盘I/O", "234", "MB/s", "+45MB/s", "info", "读写频率增加"),
    ("网络带宽", "1.2", "GB/s", "+0.3GB/s", "info", "流量增长稳定")
], layout="horizontal")

# 应用性能指标
app_metric = MetricWidget()
app_metric.set_title("应用性能")
app_metric.add_metric("平均响应时间", "156", "ms", "+12ms", "warning", "响应时间略有增加")
app_metric.add_metric("QPS", "2456", "请求/秒", "+234", "success", "处理能力提升")
app_metric.add_metric("错误率", "0.23", "%", "-0.1%", "success", "系统稳定性改善")
app_metric.add_metric("可用性", "99.95", "%", "-0.02%", "warning", "可用性略有下降")
app_metric.set_layout("vertical")

email.add_widget(app_metric)
```

### 3. 财务数据报告

```python
email = Email("财务数据月报")

# 财务核心指标
finance_metric = MetricWidget()
finance_metric.set_title("财务概览")
finance_metric.add_metric("总收入", 5680000, "元", "+12.5%", "success", "收入持续增长")
finance_metric.add_metric("总支出", 3420000, "元", "+8.3%", "warning", "支出增长需控制")
finance_metric.add_metric("净利润", 2260000, "元", "+18.7%", "success", "利润率显著提升")
finance_metric.add_metric("毛利率", "68.5", "%", "+2.3%", "success", "盈利能力增强")
finance_metric.set_layout("horizontal")
finance_metric.show_trends(True)

email.add_widget(finance_metric)

# 细分指标
email.add_metric("成本分析", [
    ("人力成本", 1250000, "元", "+5.2%", "info"),
    ("技术成本", 680000, "元", "+12.8%", "warning"),
    ("运营成本", 890000, "元", "+3.1%", "info"),
    ("营销成本", 600000, "元", "+25.6%", "error")
], layout="vertical", show_trends=True)
```

### 4. 学习和项目进度

```python
email = Email("学习进度统计")

# 学习数据
study_metric = MetricWidget()
study_metric.set_title("学习统计")
study_metric.add_metric("学习天数", 45, "天", "+5天", "success", "坚持学习")
study_metric.add_metric("完成课程", 12, "门", "+2门", "success", "学习进度良好")
study_metric.add_metric("学习时长", "156", "小时", "+18小时", "success", "投入时间充足")
study_metric.add_metric("实践项目", 3, "个", "+1个", "success", "理论结合实践")
study_metric.set_layout("horizontal")

email.add_widget(study_metric)

# 技能掌握度
email.add_metric("技能评估", [
    ("Python基础", "95", "%", "+10%", "success"),
    ("Web开发", "78", "%", "+15%", "success"),
    ("数据库", "65", "%", "+8%", "warning"),
    ("算法", "52", "%", "+12%", "warning")
], layout="vertical", show_trends=True)
```

## ⚡ 快捷方法

Email 类提供了 `add_metric` 快捷方法：

```python
# 等价于创建 MetricWidget 然后添加
email.add_metric()

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

### Q: 如何设置指标的优先级显示？
A: 通过调整添加顺序和使用不同的趋势状态：
```python
metric.add_metric("重要指标", "100", "%", "+5%", "primary")   # 重要
metric.add_metric("警告指标", "80", "%", "-2%", "warning")   # 需要关注
metric.add_metric("正常指标", "95", "%", "+1%", "success")   # 良好
```

### Q: 如何处理负数和特殊数值？
A: 直接传入数值，组件会正确处理：
```python
metric.add_metric("亏损", -125000, "元", "-15%", "error")
metric.add_metric("零值", 0, "次", "0%", "neutral")
metric.add_metric("小数", 3.14159, "", "+0.1", "info")
```

### Q: 水平布局和垂直布局的选择建议？
A: 
- **水平布局**: 适合3-5个核心指标，在一行内展示
- **垂直布局**: 适合详细指标列表，每个指标占一行

### Q: 如何自定义数字格式？
A: 传入已格式化的字符串作为value：
```python
metric.add_metric("自定义", "1,234.56", "万元")      # 自定义格式
metric.add_metric("百分比", "99.95", "%")            # 保留小数
metric.add_metric("货币", "¥1,250,000.00", "")      # 货币格式
```

### Q: 趋势不显示怎么办？
A: 确保调用了 `show_trends(True)` 方法：
```python
metric.show_trends(True)  # 显示趋势
```

### Q: 如何批量添加指标？
A: 可以使用循环或快捷方法：
```python
# 使用循环
metrics_data = [
    ("用户数", 1234, "人", "+10%", "success"),
    ("收入", 5678, "元", "+15%", "success"),
    ("转化", "3.2", "%", "-0.5%", "warning")
]

for label, value, unit, trend, trend_type in metrics_data:
    metric.add_metric(label, value, unit, trend, trend_type)

# 使用快捷方法
email.add_metric("批量指标", metrics_data)
```

## 🔗 相关组件

- [ProgressWidget](progress-widget.md) - 进度条展示
- [CircularProgressWidget](circular-progress-widget.md) - 圆形进度指标
- [StatusWidget](status-widget.md) - 状态信息展示
- [CardWidget](card-widget.md) - 可以包含指标的卡片
- [TableWidget](table-widget.md) - 表格形式的数据展示