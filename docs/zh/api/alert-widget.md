# 警告组件 API

!!! info "API 参考"
    完整的 API 文档请参考 [英文版本](../../en/api/alert-widget.md)，此处提供中文说明。

`AlertWidget` 是用于在邮件中显示重要提醒和通知信息的组件，支持多种警告类型和样式。

## 核心功能

- **多种警告类型**：支持信息、成功、警告、错误等不同类型的提醒
- **自定义内容**：可设置标题、内容文本和图标
- **视觉效果**：提供醒目的颜色和样式区分不同警告级别
- **响应式设计**：自动适配邮件客户端显示

## 主要方法

- `set_alert_type(alert_type)`: 设置警告类型（info, success, warning, error）
- `set_title(title)`: 设置警告标题
- `set_content(content)`: 设置警告内容
- `set_icon(icon)`: 设置自定义图标
