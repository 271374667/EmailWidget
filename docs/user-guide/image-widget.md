# 图片组件 (ImageWidget)

`ImageWidget` 是一个专门用于在邮件中显示图片的组件，支持多种图片来源并自动转换为邮件兼容格式。

## 🎯 组件预览

<div class="widget-preview">
<div class="preview-item">
<div class="preview-header">
<h4>📷 图片组件</h4>
<span class="preview-tag basic">基础组件</span>
</div>
<div class="preview-content">
<div style="border: 1px solid #e1e4e8; border-radius: 6px; padding: 20px; text-align: center; background: #f6f8fa;">
<div style="width: 200px; height: 150px; margin: 0 auto; background: linear-gradient(45deg, #667eea 0%, #764ba2 100%); border-radius: 4px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">
示例图片
</div>
<div style="margin-top: 10px; font-weight: bold; color: #24292e;">销售趋势图</div>
<div style="color: #586069; font-size: 14px;">展示了2024年各季度的销售数据对比</div>
</div>
</div>
</div>
</div>

## ✨ 主要功能

### 📁 多种图片来源支持
- **网络图片** - 支持HTTP/HTTPS URL
- **本地文件** - 支持本地图片文件路径
- **Base64数据** - 支持data URI格式

### 🔄 自动格式转换
- **邮件兼容** - 自动转换为base64嵌入格式
- **格式支持** - PNG、JPEG、GIF、BMP、WebP、SVG
- **缓存机制** - 避免重复下载和转换

### 🎨 丰富的展示选项
- **标题描述** - 支持图片标题和详细描述
- **替代文本** - 无障碍访问支持
- **尺寸控制** - 灵活的尺寸设置
- **样式定制** - 边框圆角、最大宽度等

## 🛠️ 核心方法详解

### 图片设置方法

#### `set_image_url(image_url, cache=True)`
设置图片来源，支持多种格式。

```python
from email_widget.widgets import ImageWidget
from pathlib import Path

# 使用网络图片
image = ImageWidget().set_image_url("https://example.com/chart.png")

# 使用本地文件
image = ImageWidget().set_image_url(Path("./images/logo.png"))

# 使用字符串路径
image = ImageWidget().set_image_url("./reports/data.jpg")
```

#### `set_title(title)` 和 `set_description(description)`
设置图片的标题和描述信息。

```python
image = (ImageWidget()
         .set_image_url("./charts/sales.png")
         .set_title("月度销售报告")
         .set_description("展示了各地区的销售表现和增长趋势"))
```

### 样式设置方法

#### `set_size(width, height)`
设置图片的显示尺寸。

```python
# 设置固定尺寸
image = ImageWidget().set_size(width="400px", height="300px")

# 只设置宽度，高度自适应
image = ImageWidget().set_size(width="100%")

# 设置响应式宽度
image = ImageWidget().set_size(width="600px").set_max_width("100%")
```

#### `set_border_radius(radius)` 和 `set_max_width(max_width)`
设置圆角和最大宽度。

```python
image = (ImageWidget()
         .set_border_radius("8px")    # 圆角
         .set_max_width("800px"))     # 最大宽度
```

### 显示控制方法

#### `set_alt_text(alt)` 和 `show_caption(show)`
设置替代文本和控制标题显示。

```python
image = (ImageWidget()
         .set_alt_text("公司Logo图片")  # 无障碍访问
         .show_caption(True))          # 显示标题和描述
```

## 💡 实用示例

### 基础图片展示

```python
from email_widget.widgets import ImageWidget

# 创建基础图片组件
image = (ImageWidget()
         .set_image_url("https://example.com/logo.png")
         .set_title("公司Logo")
         .set_alt_text("公司标志"))
```

### 本地图表展示

```python
# 展示本地生成的图表
chart_image = (ImageWidget()
               .set_image_url("./outputs/sales_chart.png")
               .set_title("2024年销售分析")
               .set_description("各产品线的销售数据对比和趋势分析")
               .set_size(width="600px")
               .set_border_radius("6px"))
```

### 响应式图片

```python
# 创建响应式图片
responsive_image = (ImageWidget()
                    .set_image_url("./images/banner.jpg")
                    .set_title("活动横幅")
                    .set_max_width("100%")
                    .set_size(width="100%"))  # 自适应宽度
```

### 产品展示图片

```python
# 产品图片展示
product_image = (ImageWidget()
                 .set_image_url("./products/product_001.jpg")
                 .set_title("新品发布")
                 .set_description("我们最新推出的旗舰产品，具有革命性的技术创新")
                 .set_size(width="400px", height="300px")
                 .set_border_radius("10px")
                 .set_alt_text("新品产品图片"))
```

### 报告图表集合

```python
# 创建多个图表
charts = []

# CPU使用率图表
cpu_chart = (ImageWidget()
             .set_image_url("./monitoring/cpu_usage.png")
             .set_title("CPU使用率")
             .set_description("过去24小时的CPU使用情况")
             .set_size(width="300px"))

# 内存使用图表
memory_chart = (ImageWidget()
                .set_image_url("./monitoring/memory_usage.png")
                .set_title("内存使用率")
                .set_description("内存使用趋势和峰值分析")
                .set_size(width="300px"))

charts.extend([cpu_chart, memory_chart])
```

## 🎨 样式定制

### 图片边框和圆角

```python
# 设置圆角和边框效果
styled_image = (ImageWidget()
                .set_image_url("./images/profile.jpg")
                .set_title("团队照片")
                .set_border_radius("15px")
                .set_size(width="250px", height="250px"))
```

### 最大宽度限制

```python
# 设置最大宽度，确保在不同设备上正确显示
constrained_image = (ImageWidget()
                     .set_image_url("./reports/wide_chart.png")
                     .set_title("宽屏数据图表")
                     .set_max_width("800px")
                     .set_size(width="100%"))
```

## 🔧 高级用法

### 条件图片显示

```python
def create_status_image(status):
    """根据状态创建不同的图片"""
    if status == "success":
        return (ImageWidget()
                .set_image_url("./icons/success.png")
                .set_title("操作成功")
                .set_alt_text("成功图标")
                .set_size(width="50px", height="50px"))
    elif status == "error":
        return (ImageWidget()
                .set_image_url("./icons/error.png")
                .set_title("操作失败")
                .set_alt_text("错误图标")
                .set_size(width="50px", height="50px"))
```

### 图片缓存控制

```python
# 禁用缓存，每次重新加载
fresh_image = (ImageWidget()
               .set_image_url("./dynamic/current_status.png", cache=False)
               .set_title("实时状态图"))

# 启用缓存（默认）
cached_image = (ImageWidget()
                .set_image_url("./static/logo.png", cache=True)
                .set_title("公司Logo"))
```

## 📝 最佳实践

### 1. 图片格式选择
```python
# 推荐使用PNG格式获得最佳质量
logo = ImageWidget().set_image_url("./assets/logo.png")

# 对于照片可以使用JPEG格式
photo = ImageWidget().set_image_url("./photos/team.jpg")
```

### 2. 响应式设计
```python
# 确保图片在不同设备上正确显示
responsive = (ImageWidget()
              .set_image_url("./images/banner.png")
              .set_max_width("100%")
              .set_size(width="800px"))  # 设置期望宽度但不超过容器
```

### 3. 无障碍访问
```python
# 始终设置有意义的替代文本
accessible = (ImageWidget()
              .set_image_url("./charts/sales.png")
              .set_title("销售数据图表")
              .set_alt_text("2024年各季度销售额对比柱状图"))
```

### 4. 性能优化
```python
# 对于静态图片启用缓存
static_image = (ImageWidget()
                .set_image_url("./assets/logo.png", cache=True)
                .set_title("Logo"))

# 对于动态图片可以禁用缓存
dynamic_image = (ImageWidget()
                 .set_image_url("./temp/current_chart.png", cache=False)
                 .set_title("实时数据"))
```

## ⚠️ 注意事项

1. **文件大小** - base64编码会增加约33%的文件大小，注意邮件大小限制
2. **路径验证** - 确保本地文件路径正确且文件存在
3. **网络访问** - 网络图片需要确保URL可访问
4. **格式支持** - 虽然支持多种格式，但PNG和JPEG兼容性最好
5. **尺寸设置** - 建议设置合适的尺寸避免图片过大影响邮件加载
6. **替代文本** - 为了无障碍访问，建议总是设置alt_text
7. **缓存策略** - 根据图片更新频率选择合适的缓存策略

## 🔗 相关组件

- **[ChartWidget](chart-widget.md)** - 专门用于显示图表的组件
- **[CardWidget](card-widget.md)** - 可以包含图片的卡片组件
- **[ColumnWidget](column-widget.md)** - 用于布局多个图片组件 