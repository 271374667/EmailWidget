# 图表组件 API

!!! info "API 参考"
    完整的 API 文档请参考 [英文版本](../../en/api/chart-widget.md)，此处提供中文说明。

`ChartWidget` 是用于在邮件中显示图表的组件，支持 matplotlib 生成的各种图表类型。

## 核心功能

- **matplotlib 集成**：直接使用 matplotlib 图表对象
- **图片格式**：自动转换为邮件兼容的图片格式
- **响应式显示**：自动调整图表尺寸适配邮件布局
- **标题和描述**：可添加图表标题和说明文字

## 主要方法

- `set_chart(plt_figure)`: 设置 matplotlib 图表对象
- `set_title(title)`: 设置图表标题
- `set_description(description)`: 设置图表描述
- `set_size(width, height)`: 设置图表显示尺寸
