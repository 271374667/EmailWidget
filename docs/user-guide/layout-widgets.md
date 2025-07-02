# 布局组件 (Layout Widgets)

布局组件用于组织和排列页面内容，优化空间利用率。EmailWidget 提供了 ColumnWidget 来实现多列布局，让您能够创建更加紧凑和美观的邮件内容。

## 🚀 快速开始

```python
from email_widget.widgets import ColumnWidget, TextWidget

# 创建两列布局
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
                <div style="background: #f8f9fa; padding: 16px; border-radius: 4px; text-align: center; border: 1px solid #e9ecef;">
                    左列内容
                </div>
            </td>
            <td style="width: 50%; padding: 0 10px; vertical-align: top;">
                <div style="background: #f8f9fa; padding: 16px; border-radius: 4px; text-align: center; border: 1px solid #e9ecef;">
                    右列内容
                </div>
            </td>
        </tr>
    </table>
</div>

## 📊 ColumnWidget 详解

### 基本概念

ColumnWidget 使用表格布局来实现多列显示，确保在各种邮件客户端中的兼容性。它支持1-4列的布局，并提供了自动模式来智能分配列数。

### 列数配置

```python
# 自动模式（默认）- 根据内容数量自动分配列数
auto_column = ColumnWidget()
auto_column.add_widgets([
    TextWidget().set_content("内容1"),
    TextWidget().set_content("内容2"),
    TextWidget().set_content("内容3")
])

# 固定列数
two_column = ColumnWidget().set_columns(2)
three_column = ColumnWidget().set_columns(3)
four_column = ColumnWidget().set_columns(4)
```

### 间隔设置

```python
# 设置列间距
column = ColumnWidget()
column.set_columns(3)
column.set_gap("20px")  # 默认间距
column.set_gap("30px")  # 增加间距
column.set_gap("10px")  # 减少间距
```

## 🎨 布局模式展示

### 两列布局

```python
two_col = ColumnWidget()
two_col.set_columns(2)
two_col.set_gap("24px")
two_col.add_widgets([
    TextWidget().set_content("数据统计").set_text_type(TextType.SECTION_H3),
    TextWidget().set_content("增长分析").set_text_type(TextType.SECTION_H3)
])
```

<div style="margin: 16px 0;">
    <table style="width: 100%; border-collapse: collapse;">
        <tr>
            <td style="width: 50%; padding: 0 12px; vertical-align: top;">
                <div style="background: #ffffff; border: 1px solid #e1dfdd; padding: 16px; border-radius: 4px;">
                    <h3 style="margin: 0; font-size: 18px; color: #323130; font-weight: 600;">数据统计</h3>
                </div>
            </td>
            <td style="width: 50%; padding: 0 12px; vertical-align: top;">
                <div style="background: #ffffff; border: 1px solid #e1dfdd; padding: 16px; border-radius: 4px;">
                    <h3 style="margin: 0; font-size: 18px; color: #323130; font-weight: 600;">增长分析</h3>
                </div>
            </td>
        </tr>
    </table>
</div>

### 三列布局

```python
three_col = ColumnWidget()
three_col.set_columns(3)
three_col.add_widgets([
    TextWidget().set_content("第一季度").set_align(TextAlign.CENTER),
    TextWidget().set_content("第二季度").set_align(TextAlign.CENTER),
    TextWidget().set_content("第三季度").set_align(TextAlign.CENTER)
])
```

<div style="margin: 16px 0;">
    <table style="width: 100%; border-collapse: collapse;">
        <tr>
            <td style="width: 33.33%; padding: 0 8px; vertical-align: top;">
                <div style="background: #f0f9ff; border: 1px solid #0ea5e9; padding: 12px; border-radius: 4px; text-align: center;">
                    第一季度
                </div>
            </td>
            <td style="width: 33.33%; padding: 0 8px; vertical-align: top;">
                <div style="background: #f0fdf4; border: 1px solid #22c55e; padding: 12px; border-radius: 4px; text-align: center;">
                    第二季度
                </div>
            </td>
            <td style="width: 33.33%; padding: 0 8px; vertical-align: top;">
                <div style="background: #fef3c7; border: 1px solid #f59e0b; padding: 12px; border-radius: 4px; text-align: center;">
                    第三季度
                </div>
            </td>
        </tr>
    </table>
</div>

### 四列布局

```python
four_col = ColumnWidget()
four_col.set_columns(4)
four_col.add_widgets([
    TextWidget().set_content("北区").set_align(TextAlign.CENTER),
    TextWidget().set_content("南区").set_align(TextAlign.CENTER),
    TextWidget().set_content("东区").set_align(TextAlign.CENTER),
    TextWidget().set_content("西区").set_align(TextAlign.CENTER)
])
```

<div style="margin: 16px 0;">
    <table style="width: 100%; border-collapse: collapse;">
        <tr>
            <td style="width: 25%; padding: 0 6px; vertical-align: top;">
                <div style="background: #fef2f2; border: 1px solid #f87171; padding: 10px; border-radius: 4px; text-align: center; font-size: 13px;">北区</div>
            </td>
            <td style="width: 25%; padding: 0 6px; vertical-align: top;">
                <div style="background: #f0fdf4; border: 1px solid #4ade80; padding: 10px; border-radius: 4px; text-align: center; font-size: 13px;">南区</div>
            </td>
            <td style="width: 25%; padding: 0 6px; vertical-align: top;">
                <div style="background: #eff6ff; border: 1px solid #60a5fa; padding: 10px; border-radius: 4px; text-align: center; font-size: 13px;">东区</div>
            </td>
            <td style="width: 25%; padding: 0 6px; vertical-align: top;">
                <div style="background: #fef3c7; border: 1px solid #fbbf24; padding: 10px; border-radius: 4px; text-align: center; font-size: 13px;">西区</div>
            </td>
        </tr>
    </table>
</div>

## 🔧 高级用法

### 混合组件布局

ColumnWidget 可以包含不同类型的组件：

```python
from email_widget.widgets import (
    ColumnWidget, TextWidget, ProgressWidget, StatusWidget
)

# 创建混合布局
mixed_layout = ColumnWidget()
mixed_layout.set_columns(2)

# 左列：进度信息
left_progress = ProgressWidget()
left_progress.set_value(85)
left_progress.set_label("项目进度")
left_progress.set_theme(ProgressTheme.SUCCESS)

# 右列：状态信息
right_status = StatusWidget()
right_status.set_title("系统状态")
right_status.add_status_item("服务器", "正常", StatusType.SUCCESS)
right_status.add_status_item("数据库", "警告", StatusType.WARNING)

mixed_layout.add_widgets([left_progress, right_status])
```

### 不等列宽内容

```python
# 当内容长度不一致时的处理
uneven_layout = ColumnWidget()
uneven_layout.set_columns(2)

short_content = TextWidget().set_content("简短内容")
long_content = TextWidget().set_content("""
这是一段比较长的内容，
包含多行文字和详细的说明信息。
可以看到即使内容长度不同，
布局依然保持整齐。
""")

uneven_layout.add_widgets([short_content, long_content])
```

### 嵌套布局

```python
# 创建嵌套的列布局
main_layout = ColumnWidget()
main_layout.set_columns(2)

# 左侧：单个组件
left_content = TextWidget().set_content("主要内容区域")

# 右侧：嵌套的子布局
right_nested = ColumnWidget()
right_nested.set_columns(2)
right_nested.add_widgets([
    TextWidget().set_content("子内容1"),
    TextWidget().set_content("子内容2")
])

main_layout.add_widgets([left_content, right_nested])
```

## 📋 实际应用示例

### 数据仪表板布局

```python
from email_widget import Email
from email_widget.widgets import (
    ColumnWidget, TextWidget, ProgressWidget, 
    StatusWidget, ChartWidget
)

# 创建仪表板邮件
dashboard = Email("业务仪表板")

# 标题
dashboard.add_widget(
    TextWidget()
    .set_content("业务数据仪表板")
    .set_text_type(TextType.SECTION_H2)
    .set_align(TextAlign.CENTER)
)

# 第一行：关键指标（4列）
key_metrics = ColumnWidget()
key_metrics.set_columns(4)

metrics_data = [
    ("总用户数", "12,450", "#0078d4"),
    ("活跃用户", "8,920", "#107c10"),
    ("今日订单", "1,287", "#ff8c00"),
    ("营收", "¥85,670", "#d13438")
]

for label, value, color in metrics_data:
    metric_text = TextWidget()
    metric_text.set_content(f"{label}\n{value}")
    metric_text.set_align(TextAlign.CENTER)
    metric_text.set_color(color)
    metric_text.set_font_weight("bold")
    key_metrics.add_widget(metric_text)

# 第二行：进度和状态（2列）
progress_status = ColumnWidget()
progress_status.set_columns(2)

# 左列：项目进度
project_progress = ProgressWidget()
project_progress.set_value(75)
project_progress.set_label("月度目标完成进度")
project_progress.set_theme(ProgressTheme.PRIMARY)

# 右列：系统状态
system_status = StatusWidget()
system_status.set_title("系统运行状态")
system_status.add_status_item("Web服务", "正常", StatusType.SUCCESS)
system_status.add_status_item("数据库", "正常", StatusType.SUCCESS)
system_status.add_status_item("缓存", "警告", StatusType.WARNING)

progress_status.add_widgets([project_progress, system_status])

# 第三行：图表展示（2列）
charts_layout = ColumnWidget()
charts_layout.set_columns(2)

revenue_chart = ChartWidget()
revenue_chart.set_image_url("revenue_trend.png")
revenue_chart.set_title("营收趋势")

user_chart = ChartWidget()
user_chart.set_image_url("user_growth.png")
user_chart.set_title("用户增长")

charts_layout.add_widgets([revenue_chart, user_chart])

# 添加到仪表板
dashboard.add_widgets([key_metrics, progress_status, charts_layout])
```

### 产品对比布局

```python
# 产品对比页面
comparison = Email("产品对比")

# 产品对比表格（3列）
product_comparison = ColumnWidget()
product_comparison.set_columns(3)

products = [
    {
        "name": "基础版",
        "price": "¥99/月",
        "features": ["10GB存储", "基础支持", "标准功能"],
        "color": "#8e8e93"
    },
    {
        "name": "专业版",
        "price": "¥299/月", 
        "features": ["100GB存储", "优先支持", "高级功能", "API访问"],
        "color": "#0078d4"
    },
    {
        "name": "企业版",
        "price": "¥899/月",
        "features": ["无限存储", "24/7专属支持", "全部功能", "定制开发"],
        "color": "#107c10"
    }
]

for product in products:
    # 创建产品信息组件
    product_info = TextWidget()
    content = f"""
    {product['name']}
    {product['price']}
    
    功能特性：
    """ + "\n".join([f"• {feature}" for feature in product['features']])
    
    product_info.set_content(content)
    product_info.set_align(TextAlign.CENTER)
    product_info.set_color(product['color'])
    
    product_comparison.add_widget(product_info)

comparison.add_widget(product_comparison)
```

### 团队介绍布局

```python
# 团队介绍页面
team_intro = Email("团队介绍")

# 团队成员展示（2列）
team_layout = ColumnWidget()
team_layout.set_columns(2)

team_members = [
    {"name": "张三", "role": "技术总监", "desc": "10年技术经验，专注架构设计"},
    {"name": "李四", "role": "产品经理", "desc": "5年产品经验，用户体验专家"},
    {"name": "王五", "role": "设计师", "desc": "资深UI/UX设计师，获多项设计奖"},
    {"name": "赵六", "role": "运营总监", "desc": "8年运营经验，增长黑客"}
]

for member in team_members:
    member_card = TextWidget()
    member_card.set_content(f"""
    {member['name']}
    {member['role']}
    
    {member['desc']}
    """)
    member_card.set_align(TextAlign.CENTER)
    team_layout.add_widget(member_card)

team_intro.add_widget(team_layout)
```

## ⚙️ API 参考

### ColumnWidget 核心方法

| 方法 | 参数 | 说明 | 默认值 |
|------|------|------|--------|
| `set_columns()` | `columns: int` | 设置列数(1-4)，-1为自动 | `-1` |
| `set_gap()` | `gap: str` | 设置列间距 | `"20px"` |
| `add_widget()` | `widget: BaseWidget` | 添加单个组件 | - |
| `add_widgets()` | `widgets: List[BaseWidget]` | 批量添加组件 | - |
| `clear_widgets()` | 无 | 清空所有组件 | - |

### 自动列数规则

当设置为自动模式（`columns=-1`）时，ColumnWidget 会根据组件数量自动分配：

| 组件数量 | 自动列数 | 说明 |
|---------|---------|------|
| 1 | 1 | 单列显示 |
| 2 | 2 | 两列并排 |
| 3 | 3 | 三列平分 |
| 4 | 2 | 2x2网格 |
| 5-6 | 3 | 三列布局 |
| 7-8 | 4 | 四列布局 |
| 9+ | 4 | 四列，多行显示 |

## 🎯 最佳实践

### 1. 选择合适的列数
```python
# 推荐：根据内容类型选择列数
metrics = ColumnWidget().set_columns(4)      # 数值指标适合4列
comparison = ColumnWidget().set_columns(3)   # 产品对比适合3列
detail = ColumnWidget().set_columns(2)       # 详细内容适合2列
```

### 2. 保持内容平衡
```python
# 推荐：内容长度相近的组件放在同一行
balanced_layout = ColumnWidget()
balanced_layout.set_columns(2)
balanced_layout.add_widgets([
    TextWidget().set_content("简短标题A"),
    TextWidget().set_content("简短标题B")
])
```

### 3. 合理设置间距
```python
# 推荐：根据内容密度调整间距
dense_layout = ColumnWidget().set_gap("12px")    # 紧密布局
normal_layout = ColumnWidget().set_gap("20px")   # 标准间距  
spacious_layout = ColumnWidget().set_gap("32px") # 宽松布局
```

### 4. 考虑移动设备兼容性
```python
# 推荐：避免过多列数，考虑移动设备显示
mobile_friendly = ColumnWidget().set_columns(2)  # 移动设备友好
desktop_only = ColumnWidget().set_columns(4)     # 仅适合桌面
```

## 🚨 注意事项

1. **列数限制**: 最多支持4列，超过4列可能在移动设备上显示异常
2. **内容平衡**: 尽量保持各列内容长度相近，避免布局不均
3. **邮件兼容性**: 使用表格布局确保在老旧邮件客户端中正常显示
4. **响应式考虑**: 在移动设备上可能会强制单列显示
5. **嵌套深度**: 避免过深的嵌套布局，影响性能和可读性

## 🔧 故障排除

### 布局异常
- 检查组件数量与列数设置是否匹配
- 验证gap设置是否为有效的CSS尺寸值
- 确认嵌套层级不要过深

### 内容溢出
- 调整列间距或减少列数
- 检查组件内容是否过长
- 考虑使用自动模式而非固定列数

---

**下一步**: 了解 [其他组件](other-widgets.md) 学习警告框、卡片、引用等特殊功能组件。 