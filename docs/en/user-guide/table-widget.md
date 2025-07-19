# TableWidget

TableWidget is a professional component for displaying structured data, supporting multiple features like headers, status cells, striped styles, and index columns. It's a core component in data reports.

## 🎯 Widget Preview

--8<-- "assets/table_widget_component_preview.html"

## 🚀 Quick Start

```python
from email_widget.widgets import TableWidget

# Create basic table
table = TableWidget()
table.set_headers(["Name", "Age", "Department"])
table.add_row(["John", "28", "Tech"])
table.add_row(["Jane", "32", "Sales"])
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
# Set headers
table = TableWidget()
table.set_headers(["Project", "Status", "Progress", "Owner"])

# Add data rows
table.add_row(["User System", "In Development", "75%", "John"])
table.add_row(["Payment Module", "Testing", "90%", "Jane"])
table.add_row(["Data Analytics", "Completed", "100%", "Bob"])

# Batch add rows
rows_data = [
    ["Project A", "In Progress", "60%", "Employee A"],
    ["Project B", "Completed", "100%", "Employee B"],
    ["Project C", "Planning", "0%", "Employee C"]
]
table.add_rows(rows_data)
```

### Setting Table Title

```python
table = TableWidget()
table.set_title("Project Progress Statistics")
table.set_headers(["Project Name", "Completion Status"])
table.add_row(["Project Alpha", "75%"])
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
# Enable striped style
table = TableWidget()
table.set_striped(True)
table.set_headers(["No.", "Product", "Sales"])
table.add_rows([
    ["1", "Product A", "1,200"],
    ["2", "Product B", "980"],
    ["3", "Product C", "1,500"],
    ["4", "Product D", "750"]
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
# Show borders and index column
table = TableWidget()
table.set_show_border(True)
table.set_show_index(True)
table.set_headers(["Task", "Status"])
table.add_rows([
    ["Data Backup", "Complete"],
    ["System Update", "In Progress"],
    ["Security Check", "Pending"]
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
table.set_headers(["Service", "Status", "Response Time"])
table.add_row([
    "Web Service",
    TableCell("Normal", StatusType.SUCCESS),
    "145ms"
])
table.add_row([
    "Database",
    TableCell("Warning", StatusType.WARNING),
    "892ms"
])
table.add_row([
    "Cache Service",
    TableCell("Error", StatusType.ERROR),
    "Timeout"
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

# Create email
email = Email("System Monitoring Report")

# Create monitoring table
monitor_table = TableWidget()
monitor_table.set_title("System Service Status")
monitor_table.set_headers(["Service Name", "Status", "CPU Usage", "Memory Usage", "Last Check"])
monitor_table.set_striped(True)
monitor_table.set_show_index(True)

# Add monitoring data
monitor_table.add_rows([
    ["Web Server", TableCell("Running", StatusType.SUCCESS), "23%", "45%", "2024-01-15 10:30"],
    ["Database", TableCell("Warning", StatusType.WARNING), "78%", "67%", "2024-01-15 10:29"],
    ["Redis Cache", TableCell("Normal", StatusType.SUCCESS), "12%", "34%", "2024-01-15 10:30"],
    ["Message Queue", TableCell("Error", StatusType.ERROR), "0%", "0%", "2024-01-15 09:45"],
    ["File Service", TableCell("Normal", StatusType.SUCCESS), "15%", "28%", "2024-01-15 10:30"]
])

email.add_widget(monitor_table)
```

### Sales Data Table

```python
# Create sales data table
sales_table = TableWidget()
sales_table.set_title("Monthly Sales Data")
sales_table.set_headers(["Product Name", "Sales Quantity", "Sales Amount", "Growth Rate", "Status"])
sales_table.set_show_border(True)

# Add sales data
sales_table.add_rows([
    ["Smartphone", "1,250", "¥2,500,000", "+15%", TableCell("Exceeded", StatusType.SUCCESS)],
    ["Tablet", "680", "¥1,360,000", "+8%", TableCell("Met Target", StatusType.SUCCESS)],
    ["Laptop", "420", "¥2,100,000", "-5%", TableCell("Needs Improvement", StatusType.WARNING)],
    ["Smartwatch", "890", "¥1,780,000", "+25%", TableCell("Excellent", StatusType.SUCCESS)]
])

email.add_widget(sales_table)
```

📚 **Complete API Documentation**: [TableWidget API](../api/table-widget.md)

## 🎯 Best Practices

### 1. Proper Use of Status Cells
```python
# Recommended: Use status cells for status-related columns
table.add_row([
    "Task Name",
    TableCell("Completed", StatusType.SUCCESS),  # Status column
    "2024-01-15"  # Regular text column
])
```

### 2. Maintain Data Consistency
```python
# Recommended: Ensure each row has same number of columns as headers
headers = ["Name", "Age", "Department"]
table.set_headers(headers)
table.add_row(["John", "28", "Tech"])  # 3 columns matching 3 headers
```

### 3. Use Appropriate Styling for Better Readability
```python
# Recommended: Use striped style for large data tables
large_table = TableWidget()
large_table.set_striped(True)
large_table.set_show_index(True)  # Easy to reference specific rows
```

### 4. Control Table Width to Avoid Layout Issues
```python
# Recommended: Set max width for tables with many columns
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