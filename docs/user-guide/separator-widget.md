# SeparatorWidget 分隔符组件

SeparatorWidget 是一个用于在邮件中创建视觉分隔线的组件。它支持多种样式的分隔线，包括实线、虚线和点线，帮助组织邮件内容的层次结构，提升可读性。

## ✨ 核心特性

- **📏 多种样式**: 支持实线、虚线、点线三种分隔符样式
- **🎨 颜色主题**: 支持基于StatusType的主题颜色配置
- **🔧 灵活配置**: 可自定义颜色、粗细、宽度和边距
- **📧 邮件兼容**: 使用邮件客户端兼容的CSS实现

## 🚀 快速开始

### 基础用法

```python
from email_widget import Email
from email_widget.widgets import SeparatorWidget
from email_widget.core.enums import SeparatorType

# 创建邮件
email = Email("分隔符示例")

# 创建基础分隔符
separator = SeparatorWidget().set_type(SeparatorType.SOLID)
email.add_widget(separator)

# 使用快捷方法
email.add_separator()

# 导出HTML
email.export_html("separator_demo.html")
```

### 自定义样式

```python
# 创建带样式的虚线分隔符
dashed_separator = (SeparatorWidget()
    .set_type(SeparatorType.DASHED)
    .set_color("#0078d4")
    .set_thickness("2px")
    .set_width("80%")
    .set_margin("20px"))

email.add_widget(dashed_separator)

# 使用快捷方法创建点线分隔符
email.add_separator(
    separator_type=SeparatorType.DOTTED,
    color="#ff8c00",
    thickness="3px",
    width="50%"
)
```

## 📖 API 参考

### 基本方法

#### `set_type(separator_type: SeparatorType) -> SeparatorWidget`
设置分隔符类型。

**参数:**
- `separator_type (SeparatorType)`: 分隔符类型枚举值

**示例:**
```python
separator.set_type(SeparatorType.SOLID)    # 实线
separator.set_type(SeparatorType.DASHED)   # 虚线
separator.set_type(SeparatorType.DOTTED)   # 点线
```

#### `set_color(color: str) -> SeparatorWidget`
设置分隔符颜色。

**参数:**
- `color (str)`: CSS颜色值，支持十六进制、RGB、颜色名称等

**示例:**
```python
separator.set_color("#0078d4")             # 蓝色
separator.set_color("#ff8c00")             # 橙色
separator.set_color("red")                 # 红色
separator.set_color("rgb(255, 0, 0)")      # RGB红色
```

#### `set_thickness(thickness: str) -> SeparatorWidget`
设置分隔符粗细。

**参数:**
- `thickness (str)`: CSS长度值

**示例:**
```python
separator.set_thickness("1px")  # 细线
separator.set_thickness("2px")  # 中等
separator.set_thickness("3px")  # 粗线
```

#### `set_width(width: str) -> SeparatorWidget`
设置分隔符宽度。

**参数:**
- `width (str)`: CSS宽度值

**示例:**
```python
separator.set_width("100%")   # 全宽
separator.set_width("80%")    # 80%宽度
separator.set_width("300px")  # 固定宽度
```

#### `set_margin(margin: str) -> SeparatorWidget`
设置分隔符上下边距。

**参数:**
- `margin (str)`: CSS边距值

**示例:**
```python
separator.set_margin("16px")  # 默认边距
separator.set_margin("30px")  # 大边距
separator.set_margin("1em")   # em单位
```

### 主题方法

#### `set_theme_color(status_type: StatusType) -> SeparatorWidget`
根据状态类型设置主题颜色。

**参数:**
- `status_type (StatusType)`: 状态类型枚举值

**示例:**
```python
from email_widget.core.enums import StatusType

separator.set_theme_color(StatusType.SUCCESS)  # 绿色
separator.set_theme_color(StatusType.WARNING)  # 橙色
separator.set_theme_color(StatusType.ERROR)    # 红色
separator.set_theme_color(StatusType.INFO)     # 蓝色
```

### 便捷方法

#### `set_style(**kwargs) -> SeparatorWidget`
一次性设置多个样式属性。

**参数:**
- `separator_type (SeparatorType, optional)`: 分隔符类型
- `color (str, optional)`: 分隔符颜色
- `thickness (str, optional)`: 分隔符粗细
- `width (str, optional)`: 分隔符宽度
- `margin (str, optional)`: 上下边距

**示例:**
```python
separator.set_style(
    separator_type=SeparatorType.DASHED,
    color="#ff8c00",
    thickness="2px",
    width="80%",
    margin="20px"
)
```

#### `reset_to_default() -> SeparatorWidget`
重置所有样式为默认值。

**示例:**
```python
separator.reset_to_default()
```

### 只读属性

- `separator_type`: 获取分隔符类型
- `color`: 获取分隔符颜色
- `thickness`: 获取分隔符粗细
- `width`: 获取分隔符宽度
- `margin`: 获取分隔符边距

```python
print(f"分隔符类型: {separator.separator_type}")
print(f"分隔符颜色: {separator.color}")
```

## 🎨 样式指南

### 分隔符类型

#### 实线分隔符 (SOLID)
```python
separator = SeparatorWidget().set_type(SeparatorType.SOLID)
```
适用于：主要内容区域的分割、章节间的清晰分隔

#### 虚线分隔符 (DASHED)
```python
separator = SeparatorWidget().set_type(SeparatorType.DASHED)
```
适用于：次要内容的分割、相关内容的分组

#### 点线分隔符 (DOTTED)
```python
separator = SeparatorWidget().set_type(SeparatorType.DOTTED)
```
适用于：装饰性分割、轻量级的内容分隔

### 推荐配色

#### 主题色系
```python
# 主要分隔符 - 蓝色
separator.set_color("#0078d4")

# 成功分隔符 - 绿色
separator.set_color("#107c10")

# 警告分隔符 - 橙色
separator.set_color("#ff8c00")

# 错误分隔符 - 红色
separator.set_color("#d13438")
```

#### 中性色系
```python
# 默认灰色
separator.set_color("#e1dfdd")

# 深灰色
separator.set_color("#8e8e93")

# 浅灰色
separator.set_color("#f3f2f1")
```

### 尺寸建议

#### 粗细建议
```python
# 细分隔符 - 适用于密集内容
separator.set_thickness("1px")

# 标准分隔符 - 通用场景
separator.set_thickness("2px")

# 粗分隔符 - 重要分割
separator.set_thickness("3px")
```

#### 宽度建议
```python
# 全宽分隔符
separator.set_width("100%")

# 居中分隔符
separator.set_width("80%")

# 装饰性分隔符
separator.set_width("50%")
```

## 📱 最佳实践

### 1. 内容层次分割
```python
email = Email("层次化内容")

# 主要章节间用粗实线
email.add_text("第一章", TextType.TITLE_LARGE)
email.add_text("章节内容...")
email.add_separator(
    separator_type=SeparatorType.SOLID,
    thickness="2px",
    margin="30px"
)

# 子节间用细虚线
email.add_text("1.1 小节", TextType.SECTION_H2)
email.add_text("小节内容...")
email.add_separator(
    separator_type=SeparatorType.DASHED,
    thickness="1px",
    margin="20px"
)
```

### 2. 主题化分割
```python
# 成功状态后的分隔
email.add_alert("任务完成", AlertType.TIP)
email.add_separator(
    separator_type=SeparatorType.SOLID,
    color="#107c10",
    thickness="2px"
)

# 警告状态后的分隔
email.add_alert("注意事项", AlertType.WARNING)
email.add_separator(
    separator_type=SeparatorType.DASHED,
    color="#ff8c00",
    thickness="2px"
)
```

### 3. 响应式设计
```python
# 移动端友好的分隔符
separator = (SeparatorWidget()
    .set_type(SeparatorType.SOLID)
    .set_width("90%")       # 避免贴边
    .set_thickness("1px")   # 细线减少视觉负担
    .set_margin("16px"))    # 适中的间距
```

### 4. 装饰性分隔
```python
# 页眉下方的装饰线
email.add_text("邮件标题", TextType.TITLE_LARGE)
email.add_separator(
    separator_type=SeparatorType.DOTTED,
    color="#0078d4",
    width="60%",
    thickness="2px",
    margin="10px"
)
```

## 🔗 实际应用场景

### 报告分节
```python
email = Email("月度报告")

# 执行摘要
email.add_text("执行摘要", TextType.TITLE_LARGE)
email.add_text("本月业绩概况...")

# 主分隔线
email.add_separator(SeparatorType.SOLID, thickness="2px", margin="25px")

# 详细数据
email.add_text("详细数据分析", TextType.TITLE_LARGE)
email.add_table_from_data([...])

# 次分隔线
email.add_separator(SeparatorType.DASHED, margin="20px")

# 结论
email.add_text("总结", TextType.SECTION_H2)
email.add_text("本月表现...")
```

### 系统监控邮件
```python
email = Email("系统状态监控")

# 正常服务
email.add_status_items([{"label": "Web服务", "value": "正常"}])
email.add_separator(
    separator_type=SeparatorType.SOLID,
    color="#107c10",
    thickness="1px"
)

# 警告服务
email.add_status_items([{"label": "数据库", "value": "警告"}])
email.add_separator(
    separator_type=SeparatorType.DASHED,
    color="#ff8c00",
    thickness="2px"
)

# 错误服务
email.add_status_items([{"label": "缓存", "value": "故障"}])
email.add_separator(
    separator_type=SeparatorType.SOLID,
    color="#d13438",
    thickness="2px"
)
```

### 新闻简报
```python
email = Email("每日新闻简报")

for i, news in enumerate(news_list):
    email.add_card(news.title, news.summary)
    
    # 新闻间用装饰性分隔
    if i < len(news_list) - 1:
        email.add_separator(
            separator_type=SeparatorType.DOTTED,
            width="70%",
            color="#e1dfdd",
            margin="15px"
        )
```

## ⚡ 快捷方法

Email 类提供了 `add_separator` 快捷方法：

```python
# 等价于创建 SeparatorWidget 然后添加
email.add_separator()

# 带参数的快捷方法
email.add_separator(
    separator_type=SeparatorType.DASHED,
    color="#0078d4",
    thickness="2px",
    width="80%",
    margin="20px"
)
```

## 🐛 常见问题

### Q: 分隔符在某些邮件客户端中不显示？
A: 确保使用标准的 CSS 边框样式，避免使用复杂的 CSS 属性。SeparatorWidget 已经针对主流邮件客户端进行了优化。

### Q: 如何创建渐变色分隔符？
A: 由于邮件客户端的限制，建议使用纯色。如果需要视觉层次，可以使用不同的颜色深浅。

### Q: 分隔符太细或太粗？
A: 调整 `thickness` 属性，推荐使用 1px-3px 之间的值以确保良好的显示效果。

### Q: 如何让分隔符居中显示？
A: 分隔符默认居中显示，可以通过调整 `width` 属性来控制宽度，如 `set_width("80%")` 创建居中的80%宽度分隔符。

## 🔗 相关组件

- [TextWidget](text-widget.md) - 用于分隔符前后的标题文字
- [CardWidget](card-widget.md) - 可以在卡片间使用分隔符
- [ColumnWidget](column-widget.md) - 用于多列布局中的分隔
- [AlertWidget](alert-widget.md) - 可与分隔符组合使用的提示信息