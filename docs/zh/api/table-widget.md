# 表格组件 API

!!! info "API 参考"
    完整的 API 文档请参考 [英文版本](../../en/api/table-widget.md)，此处提供中文说明。

`TableWidget` 是用于在邮件中显示表格数据的组件，支持灵活的数据展示和样式定制。

## 核心功能

- **数据源支持**：支持 pandas DataFrame、列表、字典等多种数据格式
- **表头管理**：灵活设置表头和列名
- **单元格样式**：支持单元格颜色、对齐方式、状态标识等
- **响应式表格**：自动适配不同屏幕尺寸
- **索引显示**：可选择显示或隐藏行索引

## 主要方法

### TableWidget 方法
- `set_title(title)`: 设置表格标题
- `set_headers(headers)`: 设置表头
- `add_row(row_data)`: 添加数据行
- `set_dataframe(df)`: 从 pandas DataFrame 设置数据
- `clear_rows()`: 清空所有数据行
- `set_show_index(show)`: 设置是否显示索引

### TableCell 类
- `value`: 单元格的值
- `color`: 单元格背景色  
- `text_color`: 文字颜色
- `alignment`: 对齐方式
- `status`: 状态标识（success, warning, error 等）