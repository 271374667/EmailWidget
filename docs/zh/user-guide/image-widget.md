# ImageWidget 图片组件

ImageWidget 是一个专门用于在邮件中显示图片的组件，支持多种图片来源并自动转换为邮件兼容格式。它能够处理本地文件、网络图片和Base64数据，是展示报表图表、产品图片和视觉内容的重要组件。

## 🎯 组件预览

--8<-- "assets/image_widget_component_preview.html"

## ✨ 核心特性

- **📁 多种来源**: 支持本地文件、网络URL、Base64数据等多种图片来源
- **🔄 自动转换**: 自动转换为邮件兼容的base64嵌入格式
- **🎨 样式控制**: 支持尺寸、边框圆角、最大宽度等样式设置
- **📝 标题描述**: 支持图片标题和详细描述展示
- **♿ 无障碍访问**: 支持替代文本，确保无障碍访问
- **📧 邮件兼容**: 使用邮件客户端兼容的HTML和CSS实现

## 🚀 快速开始

### 基础用法

```python
from email_widget import Email
from email_widget.widgets import ImageWidget

# 创建基础图片组件
image = ImageWidget()
image.set_image_url("./charts/sales.png")
image.set_title("销售数据图表")
image.set_description("2024年各季度销售数据对比分析")

email = Email("数据报告")
email.add_widget(image)
```

### 进阶用法

```python
# 带样式和缓存控制的图片
image = (ImageWidget()
         .set_image_url("https://example.com/chart.png", cache=True)
         .set_title("在线图表")
         .set_size(width="600px")
         .set_border_radius("8px")
         .set_max_width("100%")
         .set_alt_text("销售趋势图表"))

email.add_widget(image)

# 本地文件图片
local_image = (ImageWidget()
               .set_image_url("./reports/monthly_report.jpg")
               .set_title("月度报告")
               .set_size(width="400px", height="300px"))
```

📚 **完整API文档**: [ImageWidget API](../api/image-widget.md)

## 🎨 样式指南

### 图片尺寸建议

- **小图标**: 50px - 100px，适合状态图标
- **常规图片**: 300px - 600px，适合内容展示
- **大横幅**: 800px+，适合主要展示内容
- **响应式**: 使用`max_width="100%"`确保邮件兼容性

### 文件格式支持

- **PNG**: 最佳质量，支持透明背景
- **JPEG**: 适合照片，文件较小
- **GIF**: 支持动画效果
- **WebP**: 现代格式，体积小但兼容性较差

## 📱 最佳实践

### 1. 报表图表展示

```python
from email_widget import Email
from email_widget.widgets import ImageWidget

email = Email("业务数据报告")

# 主要数据图表
main_chart = (ImageWidget()
              .set_image_url("./charts/sales_trend.png")
              .set_title("销售趋势分析")
              .set_description("过去12个月的销售数据变化趋势")
              .set_size(width="700px")
              .set_border_radius("6px"))

email.add_widget(main_chart)

# 补充图表
support_chart = (ImageWidget()
                 .set_image_url("./charts/region_comparison.png")
                 .set_title("地区对比")
                 .set_description("各地区销售表现对比")
                 .set_size(width="500px"))

email.add_widget(support_chart)
```

### 2. 产品展示

```python
from email_widget import Email
from email_widget.widgets import ImageWidget

email = Email("新品发布")

# 产品主图
product_image = (ImageWidget()
                 .set_image_url("./products/new_product.jpg")
                 .set_title("新品展示")
                 .set_description("我们最新推出的革命性产品")
                 .set_size(width="400px", height="300px")
                 .set_border_radius("10px")
                 .set_alt_text("新产品外观图片"))

email.add_widget(product_image)
```

## ⚡ 快捷方法

Email 类提供了 `add_image` 快捷方法：

```python
# 基础快捷方法
email.add_image(
    image_url="./charts/data.png",
    title="数据图表",
    description="关键业务指标展示"
)

# 带样式的快捷方法
email.add_image(
    image_url="./assets/logo.png",
    title="公司Logo",
    width="200px",
    border_radius="8px",
    alt_text="公司标志"
)
```

## 🐛 常见问题

### Q: 图片在邮件中不显示怎么办？
A: 检查以下几点：
- 确保图片文件路径正确
- 网络图片URL可访问
- 图片格式为常见格式（PNG、JPEG等）

### Q: 如何控制图片大小？
A: 使用`set_size()`和`set_max_width()`：
```python
image.set_size(width="600px").set_max_width("100%")
```

### Q: 支持动态图片吗？
A: 支持，使用`cache=False`禁用缓存：
```python
image.set_image_url("./dynamic/chart.png", cache=False)
```

### Q: 如何确保无障碍访问？
A: 始终设置有意义的替代文本：
```python
image.set_alt_text("2024年销售数据柱状图")
```

## 🔗 相关组件

- [ChartWidget](chart-widget.md) - 专门用于显示图表的组件
- [CardWidget](card-widget.md) - 可以包含图片的卡片组件
- [ColumnWidget](column-widget.md) - 用于布局多个图片组件
- [TextWidget](text-widget.md) - 可与图片配合使用的文本组件