# 文本组件 API

!!! info "API 参考"
    完整的 API 文档请参考 [英文版本](../../en/api/text-widget.md)，此处提供中文说明。

`TextWidget` 是用于在邮件中显示文本内容的组件，支持多种文本样式和格式。

## 核心功能

- **多种文本类型**：支持标题、副标题、正文、强调文本等多种预设样式
- **灵活的内容设置**：可以设置纯文本或简单的 HTML 内容
- **响应式设计**：自动适配不同设备和邮件客户端
- **样式自定义**：支持自定义颜色、对齐方式等样式属性

## 主要方法

- `set_content(content)`: 设置文本内容
- `set_type(text_type)`: 设置文本类型（标题、正文等）
- `set_color(color)`: 设置文本颜色
- `set_alignment(alignment)`: 设置文本对齐方式

## 文本类型

- `TITLE_LARGE`: 大标题
- `TITLE_MEDIUM`: 中等标题  
- `TITLE_SMALL`: 小标题
- `SECTION_H2`: 二级标题
- `SECTION_H3`: 三级标题
- `BODY`: 正文文本
- `SUBTITLE`: 副标题
- `CAPTION`: 说明文字