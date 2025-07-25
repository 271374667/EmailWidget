# 用户指南

欢迎使用 EmailWidget 用户指南！这个全面的指南将帮助您掌握 EmailWidget 的所有功能，从基础概念到高级用法。

## 📚 学习路径

### 🚀 快速开始
如果您是新用户，建议按以下顺序阅读：

1. **[核心类](core-classes.md)** - 了解 EmailWidget 的基础架构
2. **[组件概览](widget-overview.md)** - 了解所有可用的组件类型
3. **[文本组件](text-widget.md)** - 从最基础的文本组件开始

## 🏗️ 系统架构

EmailWidget 采用组件化架构，让您可以灵活地构建各种类型的邮件内容：

```python
from email_widget import Email
from email_widget.widgets import TextWidget, TableWidget, ChartWidget, ButtonWidget

# 创建邮件容器
email = Email("数据报告")

# 添加组件
email.add_widget(TextWidget().set_content("本周数据概览"))
email.add_widget(TableWidget().set_headers(["项目", "数值"]))
email.add_widget(ChartWidget().set_image_url("chart.png"))
email.add_button("查看完整报告", "https://dashboard.example.com")

# 生成HTML
html = email.render_html()
```

## 📊 组件类型一览

| 组件类型     | 用途      | 示例场景       |
|----------|---------|------------|
| **文本组件** | 显示文本内容  | 标题、说明、备注   |
| **表格组件** | 展示结构化数据 | 数据报告、统计表格  |
| **图表组件** | 可视化数据   | 趋势图、柱状图、饼图 |
| **进度组件** | 显示进度状态  | 任务完成度、系统负载 |
| **状态组件** | 展示状态信息  | 系统监控、健康检查  |
| **布局组件** | 组织页面布局  | 多列布局、分组显示  |
| **按钮组件** | 用户交互操作  | 链接跳转、行动按钮  |
| **其他组件** | 特殊功能    | 引用、警告、卡片   |

## 🎨 设计理念

EmailWidget 遵循以下设计原则：

### 📱 邮件兼容性优先
- 使用表格布局确保在各种邮件客户端中正确显示
- 避免现代CSS特性，确保广泛兼容性
- 内联样式保证渲染一致性

### 🔧 简单易用
- 链式API设计，代码简洁直观
- 合理的默认配置，开箱即用
- 丰富的配置选项，满足定制需求

### 🛡️ 安全可靠
- 输入验证确保数据安全
- 错误处理保证系统稳定
- 日志记录便于问题排查

## 🔧 核心特性

### ✨ 模板引擎
- 基于 Jinja2 的强大模板系统
- 支持条件渲染和循环
- 模板缓存提升性能

### 🖼️ 图片处理
- 智能图片缓存机制
- 多种图片格式支持
- 自动优化图片大小

### 📝 日志系统
- 分级日志记录
- 环境变量控制
- 便于调试和监控

### ⚡ 性能优化
- LRU缓存策略
- 模板预编译
- 内存使用优化

## 🎯 最佳实践

### 📝 内容组织
1. **逻辑分层**: 按重要性组织内容
2. **适度分段**: 避免单一组件内容过多
3. **清晰标题**: 使用层次化的标题结构

### 🎨 视觉设计
1. **保持一致**: 统一的字体和颜色方案
2. **合理留白**: 适当的间距提升阅读体验
3. **突出重点**: 使用颜色和字重强调关键信息

### 🔧 代码质量
1. **参数验证**: 使用内置验证器确保数据有效性
2. **错误处理**: 妥善处理异常情况
3. **性能考虑**: 避免在循环中创建大量对象

## 🆘 获取帮助

如果您在使用过程中遇到问题：

1. 📖 查看 [常见问题](../getting-started/faq.md)
2. 🔍 搜索 [API 参考](../api/index.md) 获取详细信息
3. 💡 参考 [示例代码](../examples/index.md) 寻找灵感
4. 🐛 在 [GitHub](https://github.com/271374667/EmailWidget) 提交问题

---

现在开始您的 EmailWidget 学习之旅吧！建议从 [核心类](core-classes.md) 开始。 