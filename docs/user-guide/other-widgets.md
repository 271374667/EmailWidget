# 其他组件 (Other Widgets)

除了数据展示和布局组件外，EmailWidget 还提供了一系列特殊功能的组件，用于增强邮件的表现力和用户体验。

## 🚨 警告框组件 (AlertWidget)

AlertWidget 提供 GitHub 风格的警告框，用于显示重要提醒、通知和说明信息。

### 🚀 快速开始

```python
from email_widget.widgets import AlertWidget
from email_widget.core.enums import AlertType

# 基本警告框
alert = AlertWidget()
alert.set_content("这是一个重要的系统通知")
alert.set_alert_type(AlertType.WARNING)
```

<div style="background: #fff8e1; border: 1px solid #ffecb3; border-left: 4px solid #ffecb3; border-radius: 6px; padding: 16px; margin: 16px 0; color: #bf8f00;">
    <div style="display: flex; align-items: center; margin-bottom: 8px; font-weight: 600; font-size: 16px;">
        <span style="margin-right: 8px; font-size: 18px;">⚠️</span>
        <span>WARNING</span>
    </div>
    <div style="line-height: 1.5; font-size: 14px;">这是一个重要的系统通知</div>
</div>

### 📝 警告类型

AlertWidget 支持五种不同类型的警告框：

```python
# NOTE - 一般信息
note_alert = AlertWidget()
note_alert.set_content("这是一条普通的信息提示")
note_alert.set_alert_type(AlertType.NOTE)

# TIP - 提示建议
tip_alert = AlertWidget()
tip_alert.set_content("💡 小贴士：记得定期备份您的数据")
tip_alert.set_alert_type(AlertType.TIP)

# IMPORTANT - 重要信息
important_alert = AlertWidget()
important_alert.set_content("❗ 重要：系统将在今晚进行维护")
important_alert.set_alert_type(AlertType.IMPORTANT)

# WARNING - 警告信息
warning_alert = AlertWidget()
warning_alert.set_content("⚠️ 警告：磁盘空间即将不足")
warning_alert.set_alert_type(AlertType.WARNING)

# CAUTION - 注意事项
caution_alert = AlertWidget()
caution_alert.set_content("🚫 注意：此操作不可逆转")
caution_alert.set_alert_type(AlertType.CAUTION)
```

<div style="margin: 16px 0;">
    <div style="background: #e3f2fd; border: 1px solid #90caf9; border-left: 4px solid #90caf9; border-radius: 6px; padding: 16px; margin: 8px 0; color: #1565c0;">
        <div style="font-weight: 600; margin-bottom: 8px;">📝 NOTE</div>
        <div>这是一条普通的信息提示</div>
    </div>
    <div style="background: #f3e5f5; border: 1px solid #ce93d8; border-left: 4px solid #ce93d8; border-radius: 6px; padding: 16px; margin: 8px 0; color: #7b1fa2;">
        <div style="font-weight: 600; margin-bottom: 8px;">💡 TIP</div>
        <div>小贴士：记得定期备份您的数据</div>
    </div>
    <div style="background: #e8f5e8; border: 1px solid #a5d6a7; border-left: 4px solid #a5d6a7; border-radius: 6px; padding: 16px; margin: 8px 0; color: #2e7d32;">
        <div style="font-weight: 600; margin-bottom: 8px;">❗ IMPORTANT</div>
        <div>重要：系统将在今晚进行维护</div>
    </div>
    <div style="background: #fff8e1; border: 1px solid #ffecb3; border-left: 4px solid #ffecb3; border-radius: 6px; padding: 16px; margin: 8px 0; color: #bf8f00;">
        <div style="font-weight: 600; margin-bottom: 8px;">⚠️ WARNING</div>
        <div>警告：磁盘空间即将不足</div>
    </div>
    <div style="background: #ffebee; border: 1px solid #ef9a9a; border-left: 4px solid #ef9a9a; border-radius: 6px; padding: 16px; margin: 8px 0; color: #c62828;">
        <div style="font-weight: 600; margin-bottom: 8px;">🚫 CAUTION</div>
        <div>注意：此操作不可逆转</div>
    </div>
</div>

### 🎨 自定义选项

```python
# 自定义标题和图标
custom_alert = AlertWidget()
custom_alert.set_content("自定义警告框内容")
custom_alert.set_alert_type(AlertType.INFO)
custom_alert.set_title("自定义标题")
custom_alert.set_icon("🔔")
custom_alert.set_show_icon(True)

# 不显示图标
no_icon_alert = AlertWidget()
no_icon_alert.set_content("这个警告框没有图标")
no_icon_alert.set_show_icon(False)
```

## 🃏 卡片组件 (CardWidget)

CardWidget 提供现代化的卡片容器，适合展示结构化信息。

### 🚀 基本用法

```python
from email_widget.widgets import CardWidget

# 基本卡片
card = CardWidget()
card.set_title("用户反馈")
card.set_content("用户对新功能的满意度达到了92%，特别是在界面设计方面获得了很高的评价。")
```

<div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
    <h3 style="font-size: 18px; font-weight: 600; color: #323130; margin-bottom: 8px;">用户反馈</h3>
    <div style="color: #323130; line-height: 1.5; font-size: 14px;">用户对新功能的满意度达到了92%，特别是在界面设计方面获得了很高的评价。</div>
</div>

### 🎯 高级功能

```python
# 带图标和元数据的卡片
advanced_card = CardWidget()
advanced_card.set_title("项目进展")
advanced_card.set_icon("📊")
advanced_card.set_content("本月项目进展顺利，各项指标均达到预期目标。团队协作效率有显著提升。")

# 添加元数据
advanced_card.add_metadata("项目经理", "张三")
advanced_card.add_metadata("完成时间", "2024-01-15")
advanced_card.add_metadata("参与人数", "12人")
advanced_card.add_metadata("预算使用", "75%")

# 设置样式
advanced_card.set_elevated(True)  # 启用阴影效果
advanced_card.set_padding("20px")
```

<div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 20px; margin: 16px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
    <h3 style="font-size: 18px; font-weight: 600; color: #323130; margin-bottom: 8px;">
        📊 项目进展
    </h3>
    <div style="color: #323130; line-height: 1.5; font-size: 14px;">本月项目进展顺利，各项指标均达到预期目标。团队协作效率有显著提升。</div>
    <div style="margin-top: 12px; padding-top: 12px; border-top: 1px solid #e1dfdd;">
        <div style="margin: 4px 0; font-size: 13px;"><strong>项目经理:</strong> 张三</div>
        <div style="margin: 4px 0; font-size: 13px;"><strong>完成时间:</strong> 2024-01-15</div>
        <div style="margin: 4px 0; font-size: 13px;"><strong>参与人数:</strong> 12人</div>
        <div style="margin: 4px 0; font-size: 13px;"><strong>预算使用:</strong> 75%</div>
    </div>
</div>

## 💬 引用组件 (QuoteWidget)

QuoteWidget 用于显示引用内容，支持引用来源标注。

### 🚀 基本用法

```python
from email_widget.widgets import QuoteWidget

# 基本引用
quote = QuoteWidget()
quote.set_content("创新是企业发展的动力，我们必须始终保持对技术的敏锐度。")
quote.set_author("张总")
quote.set_source("月度全员大会")
```

<div style="border-left: 4px solid #0078d4; background: #f8f9fa; padding: 16px; margin: 16px 0; font-style: italic;">
    <div style="color: #323130; line-height: 1.6; font-size: 16px; margin-bottom: 12px;">
        "创新是企业发展的动力，我们必须始终保持对技术的敏锐度。"
    </div>
    <div style="color: #605e5c; font-size: 14px; text-align: right;">
        — 张总，月度全员大会
    </div>
</div>

### 🎨 样式变化

```python
# 不同样式的引用
simple_quote = QuoteWidget()
simple_quote.set_content("简单就是美。")
simple_quote.set_author("乔布斯")

# 仅内容的引用
content_only = QuoteWidget()
content_only.set_content("这是一段重要的引用内容，没有特定的作者信息。")

# 长篇引用
long_quote = QuoteWidget()
long_quote.set_content("""
在数字化转型的浪潮中，我们不仅要关注技术的创新，
更要关注如何将技术与业务深度融合，
为客户创造真正的价值。
这需要我们具备前瞻性的思维和敏捷的执行力。
""")
long_quote.set_author("李总")
long_quote.set_source("数字化转型研讨会")
```

## 📋 日志组件 (LogWidget)

LogWidget 专门用于展示日志信息，支持多种日志级别和时间戳。

### 🚀 基本用法

```python
from email_widget.widgets import LogWidget
from email_widget.core.enums import LogLevel

# 创建日志组件
log = LogWidget()
log.set_title("系统日志")

# 添加不同级别的日志
log.add_log_entry("系统启动完成", LogLevel.INFO)
log.add_log_entry("数据库连接成功", LogLevel.INFO)
log.add_log_entry("内存使用率较高", LogLevel.WARNING)
log.add_log_entry("磁盘空间不足", LogLevel.ERROR)
log.add_log_entry("开始执行数据备份", LogLevel.DEBUG)

# 设置显示选项
log.set_show_timestamp(True)
log.set_max_entries(20)
```

<div style="background: #1e1e1e; color: #d4d4d4; font-family: 'Courier New', monospace; border-radius: 4px; padding: 16px; margin: 16px 0;">
    <h3 style="color: #d4d4d4; margin-bottom: 12px; font-size: 16px;">系统日志</h3>
    <div style="font-size: 13px; line-height: 1.4;">
        <div style="margin: 4px 0;">
            <span style="color: #4fc3f7;">[INFO]</span> 
            <span style="color: #757575;">2024-01-15 10:30:25</span> 
            <span>系统启动完成</span>
        </div>
        <div style="margin: 4px 0;">
            <span style="color: #4fc3f7;">[INFO]</span> 
            <span style="color: #757575;">2024-01-15 10:30:28</span> 
            <span>数据库连接成功</span>
        </div>
        <div style="margin: 4px 0;">
            <span style="color: #ffb74d;">[WARNING]</span> 
            <span style="color: #757575;">2024-01-15 10:31:15</span> 
            <span>内存使用率较高</span>
        </div>
        <div style="margin: 4px 0;">
            <span style="color: #f44336;">[ERROR]</span> 
            <span style="color: #757575;">2024-01-15 10:32:10</span> 
            <span>磁盘空间不足</span>
        </div>
        <div style="margin: 4px 0;">
            <span style="color: #9e9e9e;">[DEBUG]</span> 
            <span style="color: #757575;">2024-01-15 10:32:45</span> 
            <span>开始执行数据备份</span>
        </div>
    </div>
</div>

### 🎨 日志级别

LogWidget 支持标准的日志级别：

| 级别 | 颜色 | 用途 |
|------|------|------|
| `DEBUG` | 灰色 | 调试信息 |
| `INFO` | 蓝色 | 一般信息 |
| `WARNING` | 橙色 | 警告信息 |
| `ERROR` | 红色 | 错误信息 |
| `CRITICAL` | 深红色 | 严重错误 |

## 📋 综合应用示例

### 系统状态报告

```python
from email_widget import Email
from email_widget.widgets import (
    AlertWidget, CardWidget, QuoteWidget, LogWidget,
    TextWidget, StatusWidget
)

# 创建系统状态报告
system_report = Email("系统状态报告")

# 1. 标题
system_report.add_widget(
    TextWidget()
    .set_content("系统健康检查报告")
    .set_text_type(TextType.SECTION_H2)
    .set_align(TextAlign.CENTER)
)

# 2. 重要警告
critical_alert = AlertWidget()
critical_alert.set_content("检测到3个需要立即处理的问题，请查看详细日志并采取相应措施。")
critical_alert.set_alert_type(AlertType.CAUTION)

# 3. 系统概览卡片
overview_card = CardWidget()
overview_card.set_title("系统概览")
overview_card.set_icon("🖥️")
overview_card.set_content("系统整体运行稳定，部分服务需要关注。建议在非高峰期进行维护。")
overview_card.add_metadata("检查时间", "2024-01-15 10:30:00")
overview_card.add_metadata("检查项目", "15项")
overview_card.add_metadata("通过项目", "12项")
overview_card.add_metadata("警告项目", "3项")

# 4. 管理员建议引用
admin_quote = QuoteWidget()
admin_quote.set_content("""
基于当前的系统状态，建议在本周末进行一次全面的系统维护，
包括清理临时文件、优化数据库索引和更新安全补丁。
这将有助于提升系统整体性能和稳定性。
""")
admin_quote.set_author("系统管理员")
admin_quote.set_source("维护建议")

# 5. 最新日志
recent_logs = LogWidget()
recent_logs.set_title("最新系统日志")
recent_logs.add_log_entry("定时备份任务完成", LogLevel.INFO)
recent_logs.add_log_entry("CPU使用率达到85%", LogLevel.WARNING)
recent_logs.add_log_entry("用户登录认证失败", LogLevel.ERROR)
recent_logs.add_log_entry("缓存清理完成", LogLevel.INFO)
recent_logs.set_max_entries(10)

# 6. 操作建议提示
action_tip = AlertWidget()
action_tip.set_content("💡 建议立即检查CPU使用率异常的原因，可能需要重启相关服务。")
action_tip.set_alert_type(AlertType.TIP)

# 添加所有组件
system_report.add_widgets([
    critical_alert, overview_card, admin_quote, 
    recent_logs, action_tip
])
```

### 项目进展汇报

```python
# 项目进展汇报邮件
project_update = Email("项目进展汇报")

# 项目信息卡片
project_card = CardWidget()
project_card.set_title("项目：客户管理系统升级")
project_card.set_icon("🚀")
project_card.set_content("""
本周项目进展良好，前端开发基本完成，后端API开发进度达到80%。
测试团队已经开始功能测试，发现并修复了5个bug。
预计下周可以进入系统集成测试阶段。
""")
project_card.add_metadata("项目经理", "张三")
project_card.add_metadata("开始时间", "2024-01-01")
project_card.add_metadata("预计完成", "2024-02-15") 
project_card.add_metadata("当前进度", "75%")

# 重要里程碑提醒
milestone_alert = AlertWidget()
milestone_alert.set_content("🎯 重要提醒：下周一(1月22日)将进行项目中期评审，请各团队准备相关材料。")
milestone_alert.set_alert_type(AlertType.IMPORTANT)

# 团队反馈引用
team_quote = QuoteWidget()
team_quote.set_content("""
团队协作非常顺畅，新的敏捷开发流程大大提升了我们的工作效率。
大家对新技术栈的掌握程度也在快速提升，
相信能够按时高质量地完成项目目标。
""")
team_quote.set_author("开发团队负责人 李四")

# 开发日志
dev_logs = LogWidget()
dev_logs.set_title("开发日志")
dev_logs.add_log_entry("完成用户管理模块前端开发", LogLevel.INFO)
dev_logs.add_log_entry("API响应时间优化完成", LogLevel.INFO)
dev_logs.add_log_entry("发现数据同步问题", LogLevel.WARNING)
dev_logs.add_log_entry("修复登录状态异常bug", LogLevel.INFO)
dev_logs.add_log_entry("完成单元测试覆盖率提升", LogLevel.INFO)

project_update.add_widgets([
    project_card, milestone_alert, team_quote, dev_logs
])
```

## ⚙️ API 参考

### AlertWidget API

| 方法 | 参数 | 说明 |
|------|------|------|
| `set_content()` | `content: str` | 设置警告内容 |
| `set_alert_type()` | `type: AlertType` | 设置警告类型 |
| `set_title()` | `title: str` | 自定义标题 |
| `set_icon()` | `icon: str` | 自定义图标 |
| `set_show_icon()` | `show: bool` | 是否显示图标 |

### CardWidget API

| 方法 | 参数 | 说明 |
|------|------|------|
| `set_title()` | `title: str` | 设置卡片标题 |
| `set_content()` | `content: str` | 设置卡片内容 |
| `set_icon()` | `icon: str` | 设置标题图标 |
| `add_metadata()` | `key: str, value: str` | 添加元数据 |
| `set_elevated()` | `elevated: bool` | 设置阴影效果 |
| `set_padding()` | `padding: str` | 设置内边距 |

### QuoteWidget API

| 方法 | 参数 | 说明 |
|------|------|------|
| `set_content()` | `content: str` | 设置引用内容 |
| `set_author()` | `author: str` | 设置作者 |
| `set_source()` | `source: str` | 设置来源 |

### LogWidget API

| 方法 | 参数 | 说明 |
|------|------|------|
| `set_title()` | `title: str` | 设置日志标题 |
| `add_log_entry()` | `message: str, level: LogLevel` | 添加日志条目 |
| `set_show_timestamp()` | `show: bool` | 显示时间戳 |
| `set_max_entries()` | `max_count: int` | 最大条目数 |
| `clear_logs()` | 无 | 清空日志 |

## 🎯 最佳实践

### 1. 合理使用警告类型
```python
# 根据重要程度选择合适的警告类型
AlertWidget().set_alert_type(AlertType.NOTE)       # 一般信息
AlertWidget().set_alert_type(AlertType.WARNING)    # 需要注意
AlertWidget().set_alert_type(AlertType.CAUTION)    # 需要谨慎
```

### 2. 卡片内容结构化
```python
# 推荐：结构化组织卡片内容
card = CardWidget()
card.set_title("清晰的标题")
card.set_content("简洁明了的正文内容")
card.add_metadata("关键信息", "具体数值")
```

### 3. 引用内容要有价值
```python
# 推荐：引用有意义的内容
quote = QuoteWidget()
quote.set_content("具有启发性或权威性的内容")
quote.set_author("可信的来源")
```

### 4. 日志信息要有层次
```python
# 推荐：合理使用日志级别
log.add_log_entry("正常操作信息", LogLevel.INFO)
log.add_log_entry("需要关注的情况", LogLevel.WARNING)
log.add_log_entry("严重问题", LogLevel.ERROR)
```

## 🚨 注意事项

1. **内容长度**: 避免在组件中放置过长的内容
2. **颜色一致性**: 保持整个邮件中颜色使用的一致性
3. **信息层次**: 合理使用不同组件来体现信息的重要程度
4. **移动适配**: 考虑组件在移动设备上的显示效果
5. **可读性**: 确保文本内容具有良好的可读性

---

**下一步**: 了解 [配置系统](configuration.md) 学习如何全局配置EmailWidget。 