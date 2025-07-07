# QuoteWidget 引用组件

<div style="background: #f0f8ff; border: 1px solid #4a90e2; border-radius: 8px; padding: 20px; margin: 20px 0;">
  <h3 style="color: #2c5282; margin-top: 0;">💬 引用展示组件</h3>
  <blockquote style="border-left: 4px solid #0078d4; background: #faf9f8; padding: 16px 20px; margin: 12px 0; font-family: 'Segoe UI', Tahoma, Arial, sans-serif; border-radius: 0 4px 4px 0;">
    <p style="font-size: 16px; line-height: 1.6; color: #323130; margin: 0 0 12px 0; font-style: italic;">"代码如诗，简洁而优雅。好的代码不仅能够运行，更能够传达思想和美感。"</p>
    <cite style="font-size: 14px; color: #605e5c; text-align: right; margin: 0;">— 某位智者</cite>
  </blockquote>
  <div style="display: flex; gap: 10px; margin-top: 15px;">
    <span style="background: #e8f4fd; color: #0078d4; padding: 4px 8px; border-radius: 4px; font-size: 12px;">引用样式</span>
    <span style="background: #e8f4fd; color: #0078d4; padding: 4px 8px; border-radius: 4px; font-size: 12px;">作者标注</span>
    <span style="background: #e8f4fd; color: #0078d4; padding: 4px 8px; border-radius: 4px; font-size: 12px;">多种主题</span>
  </div>
</div>

QuoteWidget是一个专门用于展示引用内容的组件，支持多种引用样式和主题颜色。它能够优雅地展示名人名言、用户反馈、重要声明等内容，是内容展示的重要补充。

## 🎯 主要功能

### 引用内容
- **内容设置**：支持设置引用的主要内容
- **作者标注**：可选的引用作者信息
- **来源标注**：可选的引用来源信息
- **完整引用**：一次性设置所有引用信息

### 样式主题
- **多种主题**：支持INFO、SUCCESS、WARNING、ERROR等主题
- **颜色标识**：不同主题对应不同的边框颜色
- **统一样式**：保持与其他组件的视觉一致性

### 灵活配置
- **可选元素**：作者和来源信息都是可选的
- **动态更新**：支持动态更新引用内容和信息
- **清理功能**：支持清除作者和来源信息

## 📋 核心方法

### 基础使用

```python
from email_widget.widgets import QuoteWidget
from email_widget.core.enums import StatusType

# 创建引用组件
quote = QuoteWidget()

# 设置引用内容
quote.set_content("知识就是力量，学习永无止境。")
quote.set_author("培根")
quote.set_source("《随笔集》")
```

### 内容管理方法

```python
# 设置引用内容
quote.set_content("引用的主要内容")

# 设置作者
quote.set_author("作者姓名")

# 设置来源
quote.set_source("来源信息")

# 一次性设置完整引用
quote.set_full_quote(
    content="引用内容",
    author="作者",
    source="来源"
)

# 清除作者和来源信息
quote.clear_attribution()
```

### 样式设置

```python
# 设置引用主题
quote.set_quote_type(StatusType.INFO)     # 信息主题（蓝色）
quote.set_quote_type(StatusType.SUCCESS)  # 成功主题（绿色）
quote.set_quote_type(StatusType.WARNING)  # 警告主题（橙色）
quote.set_quote_type(StatusType.ERROR)    # 错误主题（红色）
```

## 💡 实用示例

### 名人名言展示

```python
from email_widget.widgets import QuoteWidget
from email_widget.core.enums import StatusType

# 创建名人名言
famous_quote = QuoteWidget()
famous_quote.set_content("生活不是等待暴风雨过去，而是要学会在雨中跳舞。")
famous_quote.set_author("维维安·格林")
famous_quote.set_quote_type(StatusType.INFO)

# 渲染引用
html = famous_quote.render_html()
```

### 用户反馈展示

```python
# 创建用户反馈引用
feedback_quote = QuoteWidget()
feedback_quote.set_content("这个邮件组件库真的很棒！界面美观，功能强大，大大提高了我们的开发效率。")
feedback_quote.set_author("张三")
feedback_quote.set_source("产品评价")
feedback_quote.set_quote_type(StatusType.SUCCESS)
```

### 重要声明展示

```python
# 创建重要声明
statement_quote = QuoteWidget()
statement_quote.set_content("请注意：系统将在今晚进行维护升级，期间可能会影响部分功能的正常使用。")
statement_quote.set_source("系统公告")
statement_quote.set_quote_type(StatusType.WARNING)
```

### 错误信息展示

```python
# 创建错误信息引用
error_quote = QuoteWidget()
error_quote.set_content("数据库连接失败，请检查网络连接或联系系统管理员。")
error_quote.set_source("系统错误")
error_quote.set_quote_type(StatusType.ERROR)
```

### 技术文档引用

```python
# 创建技术文档引用
tech_quote = QuoteWidget()
tech_quote.set_full_quote(
    content="代码应该是自文档化的，好的变量名和函数名比注释更重要。",
    author="Robert C. Martin",
    source="《代码整洁之道》"
)
tech_quote.set_quote_type(StatusType.INFO)
```

## 🎨 主题类型详解

### 主题颜色说明

| 主题类型 | 边框颜色 | 适用场景 |
|---------|----------|----------|
| `INFO` | 蓝色 | 一般信息、说明、引用 |
| `SUCCESS` | 绿色 | 正面评价、成功案例 |
| `WARNING` | 橙色 | 警告信息、注意事项 |
| `ERROR` | 红色 | 错误信息、问题说明 |
| `PRIMARY` | 蓝色 | 重要信息、主要内容 |

### 主题使用建议

```python
# 信息引用
StatusType.INFO      # 名人名言、技术引用
StatusType.PRIMARY   # 重要声明、核心理念

# 反馈引用
StatusType.SUCCESS   # 正面评价、成功案例
StatusType.WARNING   # 建议改进、注意事项
StatusType.ERROR     # 负面反馈、问题报告
```

## 🎨 最佳实践

### 1. 内容组织

```python
# 保持引用内容简洁明了
quote = QuoteWidget()
quote.set_content("简洁明了的引用内容")  # 避免过长的内容
quote.set_author("明确的作者")           # 提供可信的作者信息
quote.set_source("具体的来源")           # 标明具体来源
```

### 2. 主题选择

```python
# 根据内容性质选择合适的主题
positive_quote = QuoteWidget()
positive_quote.set_quote_type(StatusType.SUCCESS)  # 正面内容

warning_quote = QuoteWidget()
warning_quote.set_quote_type(StatusType.WARNING)   # 警告内容

info_quote = QuoteWidget()
info_quote.set_quote_type(StatusType.INFO)         # 一般信息
```

### 3. 引用信息管理

```python
# 动态更新引用信息
def update_quote_info(quote, new_content, author=None, source=None):
    quote.set_content(new_content)
    if author:
        quote.set_author(author)
    if source:
        quote.set_source(source)

# 清理不必要的信息
quote.clear_attribution()  # 清除作者和来源信息
```

### 4. 组合使用

```python
# 多个引用组合展示
from email_widget.widgets import ColumnWidget

# 创建引用组合
column = ColumnWidget().set_columns(1)

# 创建多个相关引用
quotes = []
quote_data = [
    ("第一个引用内容", "作者1", StatusType.INFO),
    ("第二个引用内容", "作者2", StatusType.SUCCESS),
    ("第三个引用内容", "作者3", StatusType.WARNING)
]

for content, author, theme in quote_data:
    quote = QuoteWidget()
    quote.set_content(content)
    quote.set_author(author)
    quote.set_quote_type(theme)
    quotes.append(quote)

# 组合显示
column.add_widgets(quotes)
```

### 5. 内容验证

```python
# 内容长度控制
def create_validated_quote(content, author=None, source=None):
    if len(content) > 200:
        content = content[:197] + "..."
    
    quote = QuoteWidget()
    quote.set_content(content)
    
    if author:
        quote.set_author(author)
    if source:
        quote.set_source(source)
    
    return quote
```

## 🔧 常见问题

### Q: 如何处理很长的引用内容？
A: 建议将长内容分段或截取重要部分，保持引用的简洁性。

### Q: 可以不设置作者和来源吗？
A: 可以，作者和来源都是可选的，可以只设置引用内容。

### Q: 如何选择合适的主题颜色？
A: 根据引用内容的性质选择：正面内容用SUCCESS，警告用WARNING，一般信息用INFO。

### Q: 引用组件支持HTML格式吗？
A: 支持基本的HTML标签，但建议使用纯文本以确保邮件客户端兼容性。

QuoteWidget为您提供了优雅的引用展示方案，让重要内容以更具吸引力的方式呈现！ 