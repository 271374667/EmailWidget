# ChecklistWidget 清单组件

ChecklistWidget 是一个用于在邮件中创建任务清单、待办事项或检查列表的组件。它支持多种状态显示、进度统计和灵活的样式配置，帮助用户清晰地展示项目进度和任务完成情况。

## 🎯 组件预览

--8<-- "assets/checklist_widget_component_preview.html"

## ✨ 核心特性

- **📝 多种状态**: 支持已完成、未完成、跳过等多种项目状态
- **🎨 状态主题**: 基于StatusType的主题颜色配置，如成功、警告、错误等
- **📊 进度统计**: 可选的进度条和完成百分比显示
- **🔧 灵活配置**: 支持紧凑模式、自定义描述、状态文本等
- **📧 邮件兼容**: 使用邮件客户端兼容的HTML和CSS实现

## 🚀 快速开始

### 基础用法

```python
from email_widget import Email
from email_widget.widgets import ChecklistWidget

# 创建基础清单
checklist = ChecklistWidget()
checklist.set_title("开发任务")
checklist.add_item("完成需求分析", True)
checklist.add_item("设计数据库", True)
checklist.add_item("编写代码", False)

email = Email("项目进度报告")
email.add_widget(checklist)
```

### 进阶用法

```python
# 带进度统计和状态的清单
checklist = ChecklistWidget()
checklist.set_title("项目里程碑")
checklist.add_item("项目启动", True, "success", "项目已正式启动")
checklist.add_item("需求确认", True, "success", "所有需求已确认")
checklist.add_item("设计评审", False, "warning", "设计方案待审核")
checklist.add_item("开发实施", False, "pending", "等待开发团队")
checklist.show_progress_stats(True)
checklist.set_compact_mode(True)

email.add_widget(checklist)
```

📚 **完整API文档**: [ChecklistWidget API](../api/checklist-widget.md)

## 🎨 样式指南

### 状态类型和主题颜色

- **success**: 绿色 (#107c10) - 已完成的重要任务
- **warning**: 橙色 (#ff8c00) - 需要注意的项目
- **error**: 红色 (#d13438) - 失败或阻塞的任务
- **info**: 蓝色 (#0078d4) - 信息性或参考性项目
- **primary**: 蓝色 (#0078d4) - 正在进行的重要任务

## 📱 最佳实践

### 1. 项目管理清单

```python
from email_widget import Email
from email_widget.widgets.checklist_widget import ChecklistWidget

# 创建项目管理报告邮件
email = Email("项目管理报告")

# 主要里程碑
checklist1 = ChecklistWidget()
checklist1.set_title("项目里程碑")
checklist1.add_item("项目启动", True, "success")
checklist1.add_item("需求分析", True, "success")
checklist1.add_item("概要设计", True, "success")
checklist1.add_item("详细设计", False, "warning")
checklist1.add_item("开发实施", False, "pending")
checklist1.show_progress_stats(True)

email.add_widget(checklist1)

# 导出HTML文件
email.export_html("project_management_report.html")
```

--8<-- "assets/checklist_project_management.html"

### 2. 系统运维检查清单

```python
from email_widget import Email
from email_widget.widgets.checklist_widget import ChecklistWidget

# 创建系统运维日报邮件
email = Email("系统运维日报")

# 日常检查清单
checklist = ChecklistWidget()
checklist.set_title("系统健康检查")
checklist.add_item("服务器状态", True, "success")
checklist.add_item("数据库连接", True, "success")
checklist.add_item("磁盘空间", False, "warning", "需要关注")
checklist.add_item("内存使用", True, "success")
checklist.add_item("网络连通", True, "success")
checklist.show_progress_stats(True)

email.add_widget(checklist)
```

--8<-- "assets/checklist_system_ops.html"

## ⚡ 快捷方法

Email 类提供了 `add_checklist` 快捷方法：

```python
# 带参数的快捷方法
email.add_checklist(
    title="任务清单",
    items=[
        ("任务1", True),
        ("任务2", False),
        ("任务3", False)
    ],
    show_progress=True,
    compact_mode=True
)
```

## 🐛 常见问题

### Q: 如何创建不同优先级的任务？
A: 使用不同的status_type来表示优先级：
```python
checklist.add_item("高优先级", False, "error")    # 红色-紧急
checklist.add_item("中优先级", False, "warning")  # 橙色-重要
checklist.add_item("低优先级", False, "info")     # 蓝色-普通
```

### Q: 跳过状态和未完成状态有什么区别？
A: 
- 未完成 (False): 计入总进度，需要完成的任务
- 跳过 (None): 不计入进度统计，被跳过的任务

### Q: 进度条为什么不显示？
A: 确保调用了 `show_progress_stats(True)` 方法。

## 🔗 相关组件

- [ProgressWidget](progress-widget.md) - 单项进度显示
- [StatusWidget](status-widget.md) - 状态信息展示
- [CardWidget](card-widget.md) - 可以包含清单的卡片
- [AlertWidget](alert-widget.md) - 可与清单配合使用的提醒