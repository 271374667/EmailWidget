# TableWidget

TableWidget is a professional component for displaying structured data, supporting multiple features like headers, status cells, striped styles, and index columns. It's a core component in data reports.

## 🎯 Widget Preview

--8<-- "assets/table_widget_component_preview.html"

## 🚀 Quick Start

```python
from email_widget.widgets import TableWidget

# 创建基本表格
table = TableWidget()
table.set_headers(["姓名", "年龄", "部门"])
table.add_row(["张三", "28", "技术部"])
table.add_row(["李四", "32", "销售部"])
```

<div class="email-preview-wrapper">
<div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0;">
    <table style="width: 100%; border-collapse: collapse;">
        <thead>
            <tr style="background: #f8f9fa;">
                <th style="padding: 12px; text-align: left; border-bottom: 2px solid #e9ecef; font-weight: 600;">Name</th>
                <th style="padding: 12px; text-align: left; border-bottom: 2px solid #e9ecef; font-weight: 600;">Age</th>
                <th style="padding: 12px; text-align: left; border-bottom: 2px solid #e9ecef; font-weight: 600;">Department</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">John</td>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">28</td>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">Tech</td>
            </tr>
            <tr>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">Jane</td>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">32</td>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">Sales</td>
            </tr>
        </tbody>
    </table>
</div>
</div>

## 📊 Basic Usage

### Setting Headers and Data

```python
# 设置表头
table = TableWidget()
table.set_headers(["项目", "状态", "进度", "负责人"])

# 添加数据行
table.add_row(["用户系统", "开发中", "75%", "张工"])
table.add_row(["支付模块", "测试中", "90%", "李工"])
table.add_row(["数据统计", "已完成", "100%", "王工"])

# 批量添加行
rows_data = [
    ["项目A", "进行中", "60%", "员工A"],
    ["项目B", "已完成", "100%", "员工B"],
    ["项目C", "计划中", "0%", "员工C"]
]
table.add_rows(rows_data)
```

### Setting Table Title

```python
table = TableWidget()
table.set_title("项目进度统计表")
table.set_headers(["项目名称", "完成状态"])
table.add_row(["项目Alpha", "75%"])
```

<div class="email-preview-wrapper">
<div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0;">
    <h3 style="margin: 0 0 16px 0; font-size: 18px; font-weight: 600; color: #323130;">Project Progress Statistics</h3>
    <table style="width: 100%; border-collapse: collapse;">
        <thead>
            <tr style="background: #f8f9fa;">
                <th style="padding: 12px; text-align: left; border-bottom: 2px solid #e9ecef; font-weight: 600;">Project Name</th>
                <th style="padding: 12px; text-align: left; border-bottom: 2px solid #e9ecef; font-weight: 600;">Completion Status</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">Project Alpha</td>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">75%</td>
            </tr>
        </tbody>
    </table>
</div>
</div>

## 🎨 Style Configuration

### Striped Style

```python
# 启用条纹样式
table = TableWidget()
table.set_striped(True)
table.set_headers(["序号", "产品", "销量"])
table.add_rows([
    ["1", "产品A", "1,200"],
    ["2", "产品B", "980"],
    ["3", "产品C", "1,500"],
    ["4", "产品D", "750"]
])
```

<div class="email-preview-wrapper">
<div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0;">
    <table style="width: 100%; border-collapse: collapse;">
        <thead>
            <tr style="background: #f8f9fa;">
                <th style="padding: 12px; text-align: left; border-bottom: 2px solid #e9ecef; font-weight: 600;">No.</th>
                <th style="padding: 12px; text-align: left; border-bottom: 2px solid #e9ecef; font-weight: 600;">Product</th>
                <th style="padding: 12px; text-align: left; border-bottom: 2px solid #e9ecef; font-weight: 600;">Sales</th>
            </tr>
        </thead>
        <tbody>
            <tr style="background: #ffffff;">
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">1</td>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">Product A</td>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">1,200</td>
            </tr>
            <tr style="background: #f8f9fa;">
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">2</td>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">Product B</td>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">980</td>
            </tr>
            <tr style="background: #ffffff;">
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">3</td>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">Product C</td>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">1,500</td>
            </tr>
            <tr style="background: #f8f9fa;">
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">4</td>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">Product D</td>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">750</td>
            </tr>
        </tbody>
    </table>
</div>
</div>

### Borders and Index Column

```python
# 显示边框和索引列
table = TableWidget()
table.set_show_border(True)
table.set_show_index(True)
table.set_headers(["任务", "状态"])
table.add_rows([
    ["数据备份", "完成"],
    ["系统更新", "进行中"],
    ["安全检查", "待开始"]
])
```

<div class="email-preview-wrapper">
<div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0;">
    <table style="width: 100%; border-collapse: collapse; border: 1px solid #e1dfdd;">
        <thead>
            <tr style="background: #f8f9fa;">
                <th style="padding: 12px; text-align: left; border: 1px solid #e1dfdd; font-weight: 600;">Index</th>
                <th style="padding: 12px; text-align: left; border: 1px solid #e1dfdd; font-weight: 600;">Task</th>
                <th style="padding: 12px; text-align: left; border: 1px solid #e1dfdd; font-weight: 600;">Status</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="padding: 12px; border: 1px solid #e1dfdd; background: #f8f9fa; font-weight: 600;">1</td>
                <td style="padding: 12px; border: 1px solid #e1dfdd;">Data Backup</td>
                <td style="padding: 12px; border: 1px solid #e1dfdd;">Complete</td>
            </tr>
            <tr>
                <td style="padding: 12px; border: 1px solid #e1dfdd; background: #f8f9fa; font-weight: 600;">2</td>
                <td style="padding: 12px; border: 1px solid #e1dfdd;">System Update</td>
                <td style="padding: 12px; border: 1px solid #e1dfdd;">In Progress</td>
            </tr>
            <tr>
                <td style="padding: 12px; border: 1px solid #e1dfdd; background: #f8f9fa; font-weight: 600;">3</td>
                <td style="padding: 12px; border: 1px solid #e1dfdd;">Security Check</td>
                <td style="padding: 12px; border: 1px solid #e1dfdd;">Pending</td>
            </tr>
        </tbody>
    </table>
</div>
</div>

## 🎯 Status Cells

TableWidget supports special status cells that can display colored status information:

```python
from email_widget.widgets import TableWidget, TableCell
from email_widget.core.enums import StatusType

table = TableWidget()
table.set_headers(["服务", "状态", "响应时间"])
table.add_row([
    "Web服务",
    TableCell("正常", StatusType.SUCCESS),
    "145ms"
])
table.add_row([
    "数据库",
    TableCell("警告", StatusType.WARNING),
    "892ms"
])
table.add_row([
    "缓存服务",
    TableCell("故障", StatusType.ERROR),
    "超时"
])
```

<div class="email-preview-wrapper">
<div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0;">
    <table style="width: 100%; border-collapse: collapse;">
        <thead>
            <tr style="background: #f8f9fa;">
                <th style="padding: 12px; text-align: left; border-bottom: 2px solid #e9ecef; font-weight: 600;">Service</th>
                <th style="padding: 12px; text-align: left; border-bottom: 2px solid #e9ecef; font-weight: 600;">Status</th>
                <th style="padding: 12px; text-align: left; border-bottom: 2px solid #e9ecef; font-weight: 600;">Response Time</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">Web Service</td>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef; color: #107c10; font-weight: 600;">Normal</td>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">145ms</td>
            </tr>
            <tr>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">Database</td>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef; color: #ff8c00; font-weight: 600;">Warning</td>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">892ms</td>
            </tr>
            <tr>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">Cache Service</td>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef; color: #d13438; font-weight: 600;">Error</td>
                <td style="padding: 12px; border-bottom: 1px solid #e9ecef;">Timeout</td>
            </tr>
        </tbody>
    </table>
</div>
</div>

### Status Type Description

| Status Type | Color | Use Cases |
|-------------|-------|----------|
| `StatusType.SUCCESS` | Green (#107c10) | Success, Normal, Pass |
| `StatusType.WARNING` | Orange (#ff8c00) | Warning, Attention, Pending |
| `StatusType.ERROR` | Red (#d13438) | Error, Failure, Exception |
| `StatusType.INFO` | Blue (#0078d4) | Information, Tips, Neutral |

## 📋 Complete Examples

### System Monitoring Table

```python
from email_widget import Email
from email_widget.widgets import TableWidget, TableCell
from email_widget.core.enums import StatusType

# 创建邮件
email = Email("系统监控报告")

# 创建监控表格
monitor_table = TableWidget()
monitor_table.set_title("系统服务状态")
monitor_table.set_headers(["服务名称", "状态", "CPU使用率", "内存使用率", "最后检查时间"])
monitor_table.set_striped(True)
monitor_table.set_show_index(True)

# 添加监控数据
monitor_table.add_rows([
    ["Web服务器", TableCell("运行", StatusType.SUCCESS), "23%", "45%", "2024-01-15 10:30"],
    ["数据库", TableCell("警告", StatusType.WARNING), "78%", "67%", "2024-01-15 10:29"],
    ["Redis缓存", TableCell("正常", StatusType.SUCCESS), "12%", "34%", "2024-01-15 10:30"],
    ["消息队列", TableCell("故障", StatusType.ERROR), "0%", "0%", "2024-01-15 09:45"],
    ["文件服务", TableCell("正常", StatusType.SUCCESS), "15%", "28%", "2024-01-15 10:30"]
])

email.add_widget(monitor_table)
```

### Sales Data Table

```python
# 创建销售数据表格
sales_table = TableWidget()
sales_table.set_title("月度销售数据")
sales_table.set_headers(["产品名称", "销售数量", "销售额", "增长率", "状态"])
sales_table.set_show_border(True)

# 添加销售数据
sales_table.add_rows([
    ["智能手机", "1,250", "¥2,500,000", "+15%", TableCell("超额", StatusType.SUCCESS)],
    ["平板电脑", "680", "¥1,360,000", "+8%", TableCell("达标", StatusType.SUCCESS)],
    ["笔记本电脑", "420", "¥2,100,000", "-5%", TableCell("待改进", StatusType.WARNING)],
    ["智能手表", "890", "¥1,780,000", "+25%", TableCell("优秀", StatusType.SUCCESS)]
])

email.add_widget(sales_table)
```

📚 **Complete API Documentation**: [TableWidget API](../api/table-widget.md)

## 🎯 Best Practices

### 1. Proper Use of Status Cells
```python
# 推荐：为状态相关的列使用状态单元格
table.add_row([
    "任务名称",
    TableCell("已完成", StatusType.SUCCESS),  # 状态列
    "2024-01-15"  # 普通文本列
])
```

### 2. Maintain Data Consistency
```python
# 推荐：确保每行数据列数与表头一致
headers = ["姓名", "年龄", "部门"]
table.set_headers(headers)
table.add_row(["张三", "28", "技术部"])  # 3列数据匹配3个表头
```

### 3. Use Appropriate Styling for Better Readability
```python
# 推荐：大数据表格使用条纹样式
large_table = TableWidget()
large_table.set_striped(True)
large_table.set_show_index(True)  # 便于引用特定行
```

### 4. Control Table Width to Avoid Layout Issues
```python
# 推荐：为包含大量列的表格设置最大宽度
wide_table = TableWidget()
wide_table.set_max_width("800px")
```

## 🚨 Important Notes

1. **Column Consistency**: Ensure each row has the same number of columns as headers
2. **Content Length**: Avoid overly long cell content that affects layout
3. **Status Usage**: Use status cells appropriately, don't overuse colors
4. **Performance**: Consider pagination or table splitting for large datasets

---

**Next Step**: Learn about [Chart Widget](chart-widget.md) to display visualized data.