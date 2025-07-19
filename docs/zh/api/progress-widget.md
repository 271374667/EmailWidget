# 进度组件 API

!!! info "API 参考"
    完整的 API 文档请参考 [英文版本](../../en/api/progress-widget.md)，此处提供中文说明。

`ProgressWidget` 是用于显示进度信息的组件，支持线性进度条和百分比显示。

## 核心功能

- **进度显示**：支持数值和百分比显示
- **主题样式**：提供多种预设主题颜色
- **标签支持**：可添加进度标签说明
- **自定义范围**：支持自定义最大值

## 主要方法

- `set_value(value)`: 设置当前进度值
- `set_max_value(max_value)`: 设置最大值
- `set_label(label)`: 设置进度标签
- `set_theme(theme)`: 设置主题样式
