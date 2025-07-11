# TimelineWidget 时间线组件

TimelineWidget 是一个用于在邮件中展示时间序列事件的组件。它能够按时间顺序显示项目进展、系统日志、历史记录等信息，支持状态标记、时间戳显示和灵活的样式配置。

## ✨ 核心特性

- **⏰ 时间排序**: 自动按时间顺序排列事件，支持正序和倒序
- **🎨 状态主题**: 基于StatusType的主题颜色配置，如成功、警告、错误等
- **📅 时间解析**: 智能解析多种时间格式，包括日期和时间戳
- **⚙️ 灵活配置**: 支持显示/隐藏时间戳、倒序排列等选项
- **📧 邮件兼容**: 使用邮件客户端兼容的HTML和CSS实现

## 🚀 快速开始

### 基础用法

```python
from email_widget import Email
from email_widget.widgets import TimelineWidget

# 创建邮件
email = Email("项目进展报告")

# 创建基础时间线
timeline = TimelineWidget()
timeline.set_title("项目历程")
timeline.add_event("项目启动", "2024-01-01", "项目正式开始")
timeline.add_event("需求确认", "2024-01-15", "完成需求分析")
timeline.add_event("设计评审", "2024-02-01", "UI设计通过评审")
timeline.add_event("开发完成", "2024-02-28", "核心功能开发完成")

email.add_widget(timeline)

# 使用快捷方法
email.add_timeline("系统日志", [
    ("服务启动", "2024-01-01 09:00:00", "系统成功启动"),
    ("用户登录", "2024-01-01 09:15:30", "管理员登录"),
    ("数据备份", "2024-01-01 10:00:00", "自动备份完成")
])

# 导出HTML
email.export_html("timeline_demo.html")
```

### 带状态和时间戳的时间线

```python
# 创建带状态的详细时间线
timeline = (TimelineWidget()
    .set_title("系统监控日志")
    .add_event("系统启动", "2024-01-01 09:00:00", "服务器启动成功", "success")
    .add_event("用户登录", "2024-01-01 09:15:30", "管理员用户登录", "info")
    .add_event("发现警告", "2024-01-01 10:30:00", "CPU使用率过高", "warning")
    .add_event("问题解决", "2024-01-01 11:00:00", "系统性能恢复正常", "success")
    .add_event("服务异常", "2024-01-01 12:00:00", "数据库连接失败", "error")
    .show_timestamps(True)
    .set_reverse_order(True))

email.add_widget(timeline)
```

## 📖 API 参考

### 基本方法

#### `add_event(title, time=None, description="", status_type=None) -> TimelineWidget`
添加时间线事件。

**参数:**
- `title (str)`: 事件标题
- `time (Union[str, datetime, None])`: 事件时间，支持多种格式
- `description (str)`: 事件描述信息
- `status_type (Union[str, StatusType, None])`: 状态类型

**示例:**
```python
timeline.add_event("部署完成", "2024-01-01 15:30", "生产环境部署成功", "success")
timeline.add_event("发现问题", datetime.now(), "发现性能问题", "error")
timeline.add_event("会议记录", "2024-01-02", "每周例会", "info")
```

#### `set_title(title) -> TimelineWidget`
设置时间线标题。

**参数:**
- `title (str)`: 时间线标题

**示例:**
```python
timeline.set_title("项目开发时间线")
```

#### `show_timestamps(show=True) -> TimelineWidget`
设置是否显示时间戳。

**参数:**
- `show (bool)`: 是否显示时间戳

**示例:**
```python
timeline.show_timestamps(True)   # 显示时间戳
timeline.show_timestamps(False)  # 隐藏时间戳
```

#### `set_reverse_order(reverse=True) -> TimelineWidget`
设置时间线排序方式。

**参数:**
- `reverse (bool)`: 是否倒序排列（最新事件在前）

**示例:**
```python
timeline.set_reverse_order(True)   # 倒序排列
timeline.set_reverse_order(False)  # 正序排列
```

### 管理方法

#### `clear_events() -> TimelineWidget`
清空所有时间线事件。

**示例:**
```python
timeline.clear_events()
```

#### `remove_event(index) -> TimelineWidget`
根据索引移除时间线事件。

**参数:**
- `index (int)`: 要移除的事件索引

**示例:**
```python
timeline.remove_event(0)  # 移除第一个事件
```

### 只读属性

- `events`: 获取所有时间线事件列表
- `title`: 获取时间线标题
- `event_count`: 获取事件总数

```python
print(f"总事件数: {timeline.event_count}")
print(f"时间线标题: {timeline.title}")
for event in timeline.events:
    print(f"事件: {event['title']}")
```

## 🎨 样式指南

### 状态类型和主题颜色

#### 成功状态 (success)
```python
timeline.add_event("任务完成", "2024-01-01", "功能开发完成", "success")
```
- 颜色: 绿色 (#107c10)
- 适用于: 成功完成的任务、里程碑达成

#### 警告状态 (warning)
```python
timeline.add_event("性能警告", "2024-01-01", "CPU使用率超过80%", "warning")
```
- 颜色: 橙色 (#ff8c00)
- 适用于: 需要注意的事件、性能警告

#### 错误状态 (error)
```python
timeline.add_event("系统故障", "2024-01-01", "数据库连接失败", "error")
```
- 颜色: 红色 (#d13438)
- 适用于: 错误、故障、失败事件

#### 信息状态 (info)
```python
timeline.add_event("版本发布", "2024-01-01", "v1.2.0版本发布", "info")
```
- 颜色: 蓝色 (#0078d4)
- 适用于: 信息性事件、通知、发布

#### 主要状态 (primary)
```python
timeline.add_event("重要会议", "2024-01-01", "产品规划会议", "primary")
```
- 颜色: 蓝色 (#0078d4)
- 适用于: 重要事件、关键节点

#### 中性状态 (neutral)
```python
timeline.add_event("日常维护", "2024-01-01", "例行维护", "neutral")
```
- 颜色: 灰色 (#8e8e93)
- 适用于: 常规事件、维护记录

## 📱 最佳实践

### 1. 项目进展时间线

```python
email = Email("项目进展报告")

# 项目关键里程碑
email.add_timeline("项目里程碑", [
    ("项目启动", "2024-01-01", "项目正式启动", "success"),
    ("需求确认", "2024-01-15", "需求文档确认完成", "success"),
    ("设计评审", "2024-02-01", "技术架构设计通过", "success"),
    ("开发阶段", "2024-02-15", "进入开发阶段", "info"),
    ("测试阶段", "2024-03-15", "功能测试开始", "warning"),
    ("上线部署", "2024-04-01", "预计上线时间", "primary")
], show_time=True)

# 当前进展详情
current_timeline = TimelineWidget()
current_timeline.set_title("本周进展")
current_timeline.add_event("功能开发", "2024-02-20 09:00", "完成用户登录模块", "success")
current_timeline.add_event("代码审查", "2024-02-21 14:30", "登录模块代码审查通过", "success")
current_timeline.add_event("BUG修复", "2024-02-22 10:15", "修复密码验证问题", "warning")
current_timeline.add_event("集成测试", "2024-02-23 16:00", "集成测试进行中", "info")
current_timeline.show_timestamps(True)
current_timeline.set_reverse_order(True)

email.add_widget(current_timeline)
```

### 2. 系统运维日志

```python
email = Email("系统运维日报")

# 系统事件时间线
system_timeline = TimelineWidget()
system_timeline.set_title("系统事件日志")
system_timeline.add_event("系统启动", "2024-01-01 08:00:00", "服务器重启完成", "success")
system_timeline.add_event("定时备份", "2024-01-01 12:00:00", "数据库自动备份", "info")
system_timeline.add_event("内存警告", "2024-01-01 14:30:00", "内存使用率达到85%", "warning")
system_timeline.add_event("服务异常", "2024-01-01 15:45:00", "Redis连接超时", "error")
system_timeline.add_event("问题修复", "2024-01-01 16:15:00", "Redis服务重启，连接恢复", "success")
system_timeline.add_event("性能优化", "2024-01-01 18:00:00", "优化数据库查询", "info")
system_timeline.show_timestamps(True)
system_timeline.set_reverse_order(True)

email.add_widget(system_timeline)

# 部署历史
email.add_timeline("部署记录", [
    ("v1.2.0部署", "2024-01-01 20:00", "生产环境部署完成", "success"),
    ("热修复", "2024-01-02 09:30", "修复登录问题", "warning"),
    ("回滚操作", "2024-01-02 10:00", "回滚到v1.1.9", "error"),
    ("重新部署", "2024-01-02 14:00", "修复后重新部署v1.2.1", "success")
], show_time=True, reverse_order=True)
```

### 3. 学习进度跟踪

```python
email = Email("学习进度报告")

# 学习里程碑
study_timeline = TimelineWidget()
study_timeline.set_title("Python学习历程")
study_timeline.add_event("开始学习", "2024-01-01", "开始Python基础课程", "info")
study_timeline.add_event("基础完成", "2024-01-15", "完成Python基础语法学习", "success")
study_timeline.add_event("进阶学习", "2024-02-01", "开始面向对象编程", "info")
study_timeline.add_event("项目实践", "2024-02-15", "完成第一个项目：计算器", "success")
study_timeline.add_event("遇到困难", "2024-02-20", "数据结构理解有困难", "warning")
study_timeline.add_event("突破瓶颈", "2024-02-25", "理解了链表和树结构", "success")
study_timeline.add_event("高级特性", "2024-03-01", "学习装饰器和生成器", "primary")
study_timeline.show_timestamps(False)

email.add_widget(study_timeline)
```

### 4. 产品发布历史

```python
email = Email("产品版本历史")

# 版本发布时间线
release_timeline = TimelineWidget()
release_timeline.set_title("版本发布历史")
release_timeline.add_event("v1.0.0发布", "2024-01-01", "首个正式版本发布", "success")
release_timeline.add_event("v1.0.1热修复", "2024-01-03", "修复安全漏洞", "warning")
release_timeline.add_event("v1.1.0功能更新", "2024-01-15", "新增用户管理功能", "info")
release_timeline.add_event("v1.1.1BUG修复", "2024-01-18", "修复数据导出问题", "warning")
release_timeline.add_event("v1.2.0重大更新", "2024-02-01", "全新UI设计，性能优化", "primary")
release_timeline.add_event("v1.2.1稳定版", "2024-02-05", "修复已知问题，稳定发布", "success")
release_timeline.show_timestamps(True)
release_timeline.set_reverse_order(True)

email.add_widget(release_timeline)
```

## ⚡ 快捷方法

Email 类提供了 `add_timeline` 快捷方法：

```python
# 等价于创建 TimelineWidget 然后添加
email.add_timeline()

# 带参数的快捷方法
email.add_timeline(
    title="项目时间线",
    events=[
        ("事件1", "2024-01-01", "描述1"),
        ("事件2", "2024-01-02", "描述2", "success"),
        ("事件3", "2024-01-03", "描述3", "warning")
    ],
    show_time=True,
    reverse_order=True
)
```

## 🐛 常见问题

### Q: 时间格式有什么要求？
A: 支持多种时间格式，自动解析：
```python
timeline.add_event("事件1", "2024-01-01")                    # 日期
timeline.add_event("事件2", "2024-01-01 15:30")              # 日期时间
timeline.add_event("事件3", "2024-01-01 15:30:45")           # 精确时间
timeline.add_event("事件4", datetime.now())                  # datetime对象
```

### Q: 如何处理相同时间的事件？
A: 相同时间的事件按添加顺序排列：
```python
timeline.add_event("事件A", "2024-01-01 15:30", "", "info")
timeline.add_event("事件B", "2024-01-01 15:30", "", "warning")
# 事件B会排在事件A后面
```

### Q: 时间线为什么不按时间排序？
A: 确保时间格式正确，组件会自动排序：
```python
# 正确格式
timeline.add_event("早期事件", "2024-01-01")
timeline.add_event("晚期事件", "2024-01-02")
# 会自动按时间排序显示
```

### Q: 如何创建没有时间的时间线？
A: 可以不传时间参数，按添加顺序显示：
```python
timeline.add_event("步骤1", description="第一步操作")
timeline.add_event("步骤2", description="第二步操作")
timeline.add_event("步骤3", description="第三步操作")
```

### Q: 倒序和正序有什么区别？
A: 
- 正序 (False): 最早事件在上，最新事件在下
- 倒序 (True): 最新事件在上，最早事件在下

### Q: 如何批量添加事件？
A: 可以使用循环添加：
```python
events_data = [
    ("启动", "2024-01-01", "开始", "info"),
    ("进行", "2024-01-02", "处理中", "warning"),
    ("完成", "2024-01-03", "结束", "success")
]

for title, time, desc, status in events_data:
    timeline.add_event(title, time, desc, status)
```

## 🔗 相关组件

- [ChecklistWidget](checklist-widget.md) - 任务进度展示
- [ProgressWidget](progress-widget.md) - 进度条显示
- [StatusWidget](status-widget.md) - 状态信息展示
- [LogWidget](log-widget.md) - 日志信息展示
- [CardWidget](card-widget.md) - 可以包含时间线的卡片