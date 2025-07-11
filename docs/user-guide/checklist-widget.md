# ChecklistWidget 清单组件

ChecklistWidget 是一个用于在邮件中创建任务清单、待办事项或检查列表的组件。它支持多种状态显示、进度统计和灵活的样式配置，帮助用户清晰地展示项目进度和任务完成情况。

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

# 创建邮件
email = Email("项目进度报告")

# 创建基础清单
checklist = ChecklistWidget()
checklist.set_title("开发任务")
checklist.add_item("完成需求分析", True)
checklist.add_item("设计数据库", True)
checklist.add_item("编写代码", False)
checklist.add_item("测试功能", False)

email.add_widget(checklist)

# 使用快捷方法
email.add_checklist("发布清单", [
    ("代码审查", True),
    ("文档更新", False),
    ("部署准备", False)
])

# 导出HTML
email.export_html("checklist_demo.html")
```

### 带进度统计的清单

```python
# 创建带进度统计的清单
checklist = (ChecklistWidget()
    .set_title("项目里程碑")
    .add_item("项目启动", True, "success", "项目已正式启动")
    .add_item("需求确认", True, "success", "所有需求已确认")
    .add_item("设计评审", False, "warning", "设计方案待审核")
    .add_item("开发实施", False, "pending", "等待开发团队")
    .show_progress_stats(True))

email.add_widget(checklist)
```

## 📖 API 参考

### 基本方法

#### `add_item(text, completed=False, status_type=None, description="", status_text="") -> ChecklistWidget`
添加清单项目。

**参数:**
- `text (str)`: 项目文本内容
- `completed (Union[bool, None])`: 完成状态。True=已完成，False=未完成，None=跳过
- `status_type (Union[str, StatusType, None])`: 状态类型
- `description (str)`: 项目描述信息
- `status_text (str)`: 自定义状态文本

**示例:**
```python
checklist.add_item("完成设计", True, "success", "UI设计已完成")
checklist.add_item("代码审查", False, "warning", "等待审查")
checklist.add_item("性能测试", None, "info", "暂时跳过")
```

#### `set_title(title) -> ChecklistWidget`
设置清单标题。

**参数:**
- `title (str)`: 清单标题

**示例:**
```python
checklist.set_title("项目检查清单")
```

#### `show_progress_stats(show=True) -> ChecklistWidget`
设置是否显示进度统计。

**参数:**
- `show (bool)`: 是否显示进度条和统计信息

**示例:**
```python
checklist.show_progress_stats(True)  # 显示进度条
checklist.show_progress_stats(False) # 隐藏进度条
```

#### `set_compact_mode(compact=True) -> ChecklistWidget`
设置紧凑模式。

**参数:**
- `compact (bool)`: 是否使用紧凑模式

**示例:**
```python
checklist.set_compact_mode(True)  # 紧凑模式
```

### 管理方法

#### `clear_items() -> ChecklistWidget`
清空所有清单项目。

**示例:**
```python
checklist.clear_items()
```

#### `remove_item(index) -> ChecklistWidget`
根据索引移除清单项目。

**参数:**
- `index (int)`: 要移除的项目索引

**示例:**
```python
checklist.remove_item(0)  # 移除第一个项目
```

#### `update_item_status(index, completed, status_type=None) -> ChecklistWidget`
更新指定项目的完成状态。

**参数:**
- `index (int)`: 项目索引
- `completed (Union[bool, None])`: 新的完成状态
- `status_type (Union[str, StatusType, None])`: 可选的状态类型

**示例:**
```python
checklist.update_item_status(0, True, "success")  # 标记第一个项目为完成
```

### 只读属性

- `items`: 获取所有清单项目列表
- `title`: 获取清单标题
- `item_count`: 获取项目总数
- `completed_count`: 获取已完成项目数量
- `pending_count`: 获取待完成项目数量
- `skipped_count`: 获取跳过项目数量
- `completion_percentage`: 获取完成百分比

```python
print(f"总项目数: {checklist.item_count}")
print(f"已完成: {checklist.completed_count}")
print(f"完成率: {checklist.completion_percentage}%")
```

## 🎨 样式指南

### 状态类型和主题颜色

#### 成功状态 (success)
```python
checklist.add_item("数据备份", True, "success")
```
- 颜色: 绿色 (#107c10)
- 图标: ✓
- 适用于: 已完成的重要任务

#### 警告状态 (warning)
```python
checklist.add_item("性能优化", False, "warning")
```
- 颜色: 橙色 (#ff8c00)
- 图标: !
- 适用于: 需要注意的项目

#### 错误状态 (error)
```python
checklist.add_item("安全检查", False, "error")
```
- 颜色: 红色 (#d13438)
- 图标: ✗
- 适用于: 失败或阻塞的任务

#### 信息状态 (info)
```python
checklist.add_item("文档更新", None, "info")
```
- 颜色: 蓝色 (#0078d4)
- 图标: i
- 适用于: 信息性或参考性项目

#### 主要状态 (primary)
```python
checklist.add_item("核心功能", False, "primary")
```
- 颜色: 蓝色 (#0078d4)
- 图标: ●
- 适用于: 正在进行的重要任务

### 进度条颜色映射

- **90%+ 完成**: 绿色 (#107c10) - 接近完成
- **70-89% 完成**: 蓝色 (#0078d4) - 进展良好
- **50-69% 完成**: 橙色 (#ff8c00) - 需要加速
- **<50% 完成**: 灰色 (#8e8e93) - 刚刚开始

## 📱 最佳实践

### 1. 项目管理清单

```python
email = Email("项目管理报告")

# 主要里程碑
email.add_checklist("项目里程碑", [
    ("项目启动", True),
    ("需求分析", True),
    ("概要设计", True),
    ("详细设计", False),
    ("开发实施", False),
    ("测试验收", False),
    ("上线部署", False)
], show_progress=True)

# 当前冲刺任务
checklist = ChecklistWidget()
checklist.set_title("当前冲刺")
checklist.add_item("用户登录功能", True, "success", "已通过代码审查")
checklist.add_item("数据导出功能", False, "warning", "API设计待确认")
checklist.add_item("邮件通知功能", False, "primary", "开发中")
checklist.add_item("性能监控", None, "info", "下个冲刺处理")
checklist.show_progress_stats(True)
checklist.set_compact_mode(True)

email.add_widget(checklist)
```

### 2. 系统运维检查清单

```python
email = Email("系统运维日报")

# 日常检查清单
email.add_checklist("系统健康检查", [
    ("服务器状态", True),
    ("数据库连接", True),
    ("磁盘空间", False),  # 需要关注
    ("内存使用", True),
    ("网络连通", True)
], show_progress=True)

# 安全检查
security_checklist = ChecklistWidget()
security_checklist.set_title("安全检查")
security_checklist.add_item("SSL证书", True, "success", "有效期至2024年12月")
security_checklist.add_item("防火墙规则", True, "success", "已更新")
security_checklist.add_item("漏洞扫描", False, "warning", "发现3个中级漏洞")
security_checklist.add_item("访问日志", False, "error", "发现异常访问")
security_checklist.show_progress_stats(True)

email.add_widget(security_checklist)
```

### 3. 发布准备清单

```python
email = Email("产品发布准备")

# 发布前检查
release_checklist = ChecklistWidget()
release_checklist.set_title("发布检查清单")
release_checklist.add_item("代码冻结", True, "success", "v2.1.0已冻结")
release_checklist.add_item("测试完成", True, "success", "所有测试用例通过")
release_checklist.add_item("文档更新", False, "warning", "API文档待完善")
release_checklist.add_item("数据库迁移", False, "primary", "脚本已准备")
release_checklist.add_item("监控配置", False, "info", "新增监控指标")
release_checklist.add_item("回滚预案", False, "error", "回滚脚本未测试")
release_checklist.show_progress_stats(True)

email.add_widget(release_checklist)

# 发布步骤
email.add_checklist("发布步骤", [
    ("停止旧服务", False),
    ("备份数据", False),
    ("部署新版本", False),
    ("数据库升级", False),
    ("启动新服务", False),
    ("健康检查", False),
    ("通知用户", False)
])
```

### 4. 学习计划清单

```python
email = Email("学习进度报告")

# 本周学习计划
study_checklist = ChecklistWidget()
study_checklist.set_title("本周学习计划")
study_checklist.add_item("Python基础", True, "success", "完成第1-3章")
study_checklist.add_item("数据结构", True, "success", "完成数组和链表")
study_checklist.add_item("算法练习", False, "warning", "完成5/10题")
study_checklist.add_item("项目实战", False, "primary", "搭建项目框架")
study_checklist.add_item("技术博客", False, "info", "准备写作素材")
study_checklist.show_progress_stats(True)
study_checklist.set_compact_mode(True)

email.add_widget(study_checklist)
```

## ⚡ 快捷方法

Email 类提供了 `add_checklist` 快捷方法：

```python
# 等价于创建 ChecklistWidget 然后添加
email.add_checklist()

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

### Q: 如何处理长文本描述？
A: 使用description参数添加详细说明：
```python
checklist.add_item(
    "数据库优化",
    False,
    "warning",
    "需要优化用户查询性能，预计影响响应时间30%，建议在低峰期执行",
    "高优先级"
)
```

### Q: 跳过状态和未完成状态有什么区别？
A: 
- 未完成 (False): 计入总进度，需要完成的任务
- 跳过 (None): 不计入进度统计，被跳过的任务

### Q: 如何批量更新任务状态？
A: 可以使用循环和 `update_item_status` 方法：
```python
# 批量标记前3个任务为完成
for i in range(3):
    checklist.update_item_status(i, True, "success")
```

### Q: 进度条为什么不显示？
A: 确保调用了 `show_progress_stats(True)` 方法：
```python
checklist.show_progress_stats(True)  # 显示进度条
```

## 🔗 相关组件

- [ProgressWidget](progress-widget.md) - 单项进度显示
- [StatusWidget](status-widget.md) - 状态信息展示
- [CardWidget](card-widget.md) - 可以包含清单的卡片
- [AlertWidget](alert-widget.md) - 可与清单配合使用的提醒
- [TextWidget](text-widget.md) - 清单标题和说明文字