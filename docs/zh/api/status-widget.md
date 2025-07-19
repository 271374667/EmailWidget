# 状态组件 API

!!! info "API 参考"
    完整的 API 文档请参考 [英文版本](../../en/api/status-widget.md)，此处提供中文说明。

`StatusWidget` 是用于显示系统状态和监控信息的组件，支持多项状态的列表展示。

## 核心功能

- **状态列表**：支持显示多个状态项
- **状态类型**：支持成功、警告、错误等状态
- **实时更新**：便于动态更新状态信息
- **分组显示**：可按类别组织状态项

## 主要方法

- `add_status_item(item)`: 添加状态项
- `clear_status_items()`: 清空所有状态项
- `set_title(title)`: 设置状态组标题
- `update_status(label, status)`: 更新指定状态
