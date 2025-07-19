# Email 主类

!!! info "API 参考"
    完整的 API 文档请参考 [英文版本](../../en/api/email.md)，此处提供中文说明。

`Email` 类是 EmailWidget 库的核心类，负责管理和渲染邮件内容。它是一个强大的容器，可以添加、管理和编排各种"组件"（widgets），最终将它们渲染成美观、专业的 HTML 邮件。

## 核心功能

- **组件管理**：轻松添加、删除、查找和遍历各种内容组件（文本、表格、图表等）
- **邮件属性配置**：自定义邮件标题、副标题和页脚
- **便捷方法**：提供一系列 `add_*` 方法快速创建和添加常用组件，简化代码
- **内容导出**：支持导出邮件为独立的 HTML 文件或获取 HTML 字符串内容
- **样式配置**：通过 `EmailConfig` 对象自定义邮件主题颜色、字体和布局宽度

## 主要属性

- `title` (str): 邮件的主标题
- `subtitle` (Optional[str]): 邮件的副标题，显示在主标题下方
- `footer_text` (Optional[str]): 邮件的页脚文本
- `widgets` (List[BaseWidget]): 存储所有已添加组件的列表
- `config` (EmailConfig): 邮件配置对象，用于控制样式和行为

## 使用示例

```python
from email_widget import Email

# 创建邮件实例
email = Email(title="月度报告", subtitle="2024年1月数据统计")

# 添加文本组件
email.add_text("本月业务表现良好，各项指标稳步增长。")

# 添加表格组件
email.add_table(data, title="销售数据")

# 导出为 HTML 文件
email.export("monthly_report.html")
```

## 主要方法

### 初始化方法
- `__init__(title, subtitle=None, footer_text=None, config=None)`: 创建 Email 实例

### 组件管理方法
- `add_widget(widget)`: 添加组件到邮件
- `add_text(text, **kwargs)`: 快速添加文本组件
- `add_table(data, **kwargs)`: 快速添加表格组件
- `add_metric(value, **kwargs)`: 快速添加指标组件
- `add_chart(data, **kwargs)`: 快速添加图表组件
- `add_image(src, **kwargs)`: 快速添加图片组件

### 导出方法
- `export(file_path)`: 导出邮件为 HTML 文件
- `get_html()`: 获取邮件的 HTML 字符串内容
- `render()`: 渲染邮件内容为 HTML
