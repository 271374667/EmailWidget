# AlertWidget 警告组件

AlertWidget 是一个GitHub风格的警告框组件，用于显示各种类型的提示信息。它支持多种警告级别，每种类型都有对应的颜色主题和图标，能够有效地吸引用户注意力并传达重要信息。

## 组件预览

<div class="component-preview">
    <div style="margin: 16px 0;">
        <!-- NOTE 类型 -->
        <div style="background: #dbeafe; border: 1px solid #3b82f6; border-left: 4px solid #3b82f6; border-radius: 4px; padding: 16px; margin: 12px 0; color: #1e40af;">
            <div style="display: flex; align-items: center; margin-bottom: 8px; font-weight: 600; font-size: 16px;">
                <span style="margin-right: 8px;">ℹ️</span>
                <span>注意</span>
            </div>
            <div style="line-height: 1.5; font-size: 14px;">这是一条一般提示信息，用于说明或备注</div>
        </div>
        
        <!-- TIP 类型 -->
        <div style="background: #dcfce7; border: 1px solid #22c55e; border-left: 4px solid #22c55e; border-radius: 4px; padding: 16px; margin: 12px 0; color: #15803d;">
            <div style="display: flex; align-items: center; margin-bottom: 8px; font-weight: 600; font-size: 16px;">
                <span style="margin-right: 8px;">💡</span>
                <span>提示</span>
            </div>
            <div style="line-height: 1.5; font-size: 14px;">这是一条有用的小贴士，可以帮助提高效率</div>
        </div>
        
        <!-- WARNING 类型 -->
        <div style="background: #fed7aa; border: 1px solid #f97316; border-left: 4px solid #f97316; border-radius: 4px; padding: 16px; margin: 12px 0; color: #ea580c;">
            <div style="display: flex; align-items: center; margin-bottom: 8px; font-weight: 600; font-size: 16px;">
                <span style="margin-right: 8px;">⚠️</span>
                <span>警告</span>
            </div>
            <div style="line-height: 1.5; font-size: 14px;">这是一条警告信息，需要用户注意</div>
        </div>
    </div>
</div>

## 主要功能

### 🎨 多种警告类型
- **NOTE** (注意): 一般提示信息、说明、备注
- **TIP** (提示): 有用的建议、小贴士、技巧
- **IMPORTANT** (重要): 重要通知、关键信息
- **WARNING** (警告): 警告信息、风险提示
- **CAUTION** (危险): 严重警告、危险操作提示

### 🎯 GitHub风格设计
- 统一的视觉风格和颜色主题
- 每种类型都有专属的图标和颜色
- 清晰的边框和背景色区分

### ⚙️ 灵活配置
- 自定义标题和图标
- 可控制图标显示/隐藏
- 支持链式调用

## 核心方法

### `set_content(content: str)`
设置警告框的内容文本。

```python
from email_widget.widgets import AlertWidget

alert = AlertWidget().set_content("这是一条重要的系统通知")
```

### `set_alert_type(alert_type: AlertType)`
设置警告框的类型，不同类型有不同的颜色主题和默认图标。

```python
from email_widget.core.enums import AlertType

# 不同类型的警告框
note = AlertWidget().set_content("一般提示信息").set_alert_type(AlertType.NOTE)
tip = AlertWidget().set_content("有用的小贴士").set_alert_type(AlertType.TIP)
important = AlertWidget().set_content("重要信息").set_alert_type(AlertType.IMPORTANT)
warning = AlertWidget().set_content("警告信息").set_alert_type(AlertType.WARNING)
caution = AlertWidget().set_content("危险警告").set_alert_type(AlertType.CAUTION)
```

### `set_title(title: str)`
设置自定义标题，覆盖默认标题。

```python
alert = (AlertWidget()
    .set_content("系统将在今晚进行维护")
    .set_alert_type(AlertType.WARNING)
    .set_title("系统维护通知"))
```

### `set_full_alert(content: str, alert_type: AlertType, title: str = None)`
一次性设置完整的警告信息。

```python
alert = AlertWidget().set_full_alert(
    content="请及时备份重要数据",
    alert_type=AlertType.IMPORTANT,
    title="数据备份提醒"
)
```

### `show_icon(show: bool = True)`
控制是否显示图标。

```python
# 隐藏图标
alert = (AlertWidget()
    .set_content("纯文本警告信息")
    .set_alert_type(AlertType.NOTE)
    .show_icon(False))
```

### `set_icon(icon: str)`
设置自定义图标。

```python
alert = (AlertWidget()
    .set_content("自定义图标的警告")
    .set_alert_type(AlertType.TIP)
    .set_icon("🚀"))
```

## 实用示例

### 基础用法

```python
from email_widget.widgets import AlertWidget
from email_widget.core.enums import AlertType

# 创建不同类型的警告框
note = AlertWidget().set_content("请注意查收邮件中的附件").set_alert_type(AlertType.NOTE)

tip = AlertWidget().set_content("使用快捷键 Ctrl+S 可以快速保存").set_alert_type(AlertType.TIP)

warning = AlertWidget().set_content("磁盘空间不足，请及时清理").set_alert_type(AlertType.WARNING)

important = AlertWidget().set_content("系统将在今晚22:00进行升级维护").set_alert_type(AlertType.IMPORTANT)

caution = AlertWidget().set_content("此操作将删除所有数据且不可恢复").set_alert_type(AlertType.CAUTION)
```

### 自定义标题和图标

```python
# 自定义标题
custom_title = (AlertWidget()
    .set_content("新版本已发布，包含重要安全更新")
    .set_alert_type(AlertType.IMPORTANT)
    .set_title("版本更新"))

# 自定义图标
custom_icon = (AlertWidget()
    .set_content("恭喜！您的任务已完成")
    .set_alert_type(AlertType.TIP)
    .set_icon("🎉")
    .set_title("任务完成"))

# 无图标样式
no_icon = (AlertWidget()
    .set_content("这是一个简洁的提示信息")
    .set_alert_type(AlertType.NOTE)
    .show_icon(False))
```

### 系统监控场景

```python
# 服务状态通知
service_ok = (AlertWidget()
    .set_content("所有服务运行正常，系统状态良好")
    .set_alert_type(AlertType.TIP)
    .set_title("系统状态"))

service_warning = (AlertWidget()
    .set_content("数据库连接缓慢，响应时间超过阈值")
    .set_alert_type(AlertType.WARNING)
    .set_title("性能警告"))

service_error = (AlertWidget()
    .set_content("缓存服务连接失败，请立即检查服务状态")
    .set_alert_type(AlertType.CAUTION)
    .set_title("服务异常"))
```

### 业务流程提醒

```python
# 流程提醒
process_tip = (AlertWidget()
    .set_content("提交前请确认所有必填项已完成")
    .set_alert_type(AlertType.TIP)
    .set_title("提交提醒"))

deadline_warning = (AlertWidget()
    .set_content("距离项目截止日期还有3天，请加快进度")
    .set_alert_type(AlertType.WARNING)
    .set_title("截止日期提醒"))

approval_needed = (AlertWidget()
    .set_content("您的申请需要主管审批，预计1-2个工作日完成")
    .set_alert_type(AlertType.NOTE)
    .set_title("等待审批"))
```

## 警告类型详解

### AlertType 枚举值

| 类型 | 图标 | 颜色主题 | 使用场景 |
|------|------|---------|----------|
| `NOTE` | ℹ️ | 蓝色 | 一般说明、备注信息、操作指引 |
| `TIP` | 💡 | 绿色 | 建议、技巧、最佳实践 |
| `IMPORTANT` | ❗ | 黄色 | 重要通知、关键信息、必读内容 |
| `WARNING` | ⚠️ | 橙色 | 警告、风险提示、注意事项 |
| `CAUTION` | 🚨 | 红色 | 严重警告、危险操作、不可逆操作 |

### 颜色规范

| 类型 | 背景色 | 边框色 | 文字色 |
|------|--------|--------|--------|
| `NOTE` | `#dbeafe` | `#3b82f6` | `#1e40af` |
| `TIP` | `#dcfce7` | `#22c55e` | `#15803d` |
| `IMPORTANT` | `#fef3c7` | `#f59e0b` | `#d97706` |
| `WARNING` | `#fed7aa` | `#f97316` | `#ea580c` |
| `CAUTION` | `#fecaca` | `#ef4444` | `#dc2626` |

## 最佳实践

### 1. 选择合适的警告类型
```python
# ✅ 好的做法：根据信息重要性选择类型
info_alert = AlertWidget().set_content("操作已完成").set_alert_type(AlertType.TIP)
warning_alert = AlertWidget().set_content("磁盘空间不足").set_alert_type(AlertType.WARNING)
danger_alert = AlertWidget().set_content("即将删除所有数据").set_alert_type(AlertType.CAUTION)

# ❌ 避免：所有信息都使用同一种类型
```

### 2. 保持内容简洁明了
```python
# ✅ 好的做法：简洁明了的信息
alert = AlertWidget().set_content("密码将在7天后过期，请及时更新")

# ❌ 避免：过于冗长的内容
```

### 3. 合理使用自定义标题
```python
# ✅ 好的做法：标题概括主要信息
alert = (AlertWidget()
    .set_content("系统将在今晚22:00-02:00进行维护升级")
    .set_alert_type(AlertType.IMPORTANT)
    .set_title("维护通知"))

# ❌ 避免：标题与内容重复
```

### 4. 适当使用图标
```python
# ✅ 好的做法：特殊场景使用自定义图标
success_alert = (AlertWidget()
    .set_content("数据同步完成")
    .set_alert_type(AlertType.TIP)
    .set_icon("✅"))

# ✅ 好的做法：简洁场景隐藏图标
simple_alert = (AlertWidget()
    .set_content("操作说明")
    .set_alert_type(AlertType.NOTE)
    .show_icon(False))
```

## 常见问题

### Q: 如何在一个邮件中使用多个警告框？
A: 直接创建多个AlertWidget实例，按需要的顺序添加到邮件中。

### Q: 可以自定义警告框的颜色吗？
A: 当前版本不支持自定义颜色，建议使用预定义的5种类型。

### Q: 警告框支持HTML内容吗？
A: 不支持，内容会被转义为纯文本。

### Q: 如何让警告框更突出？
A: 选择合适的警告类型，CAUTION类型最为突出，适合重要警告。

## 适用场景

### 📊 数据报告
- 数据说明和备注
- 重要指标提醒
- 数据质量警告

### 🔧 系统监控
- 服务状态通知
- 性能警告
- 故障提醒

### 📋 业务流程
- 操作指引
- 流程提醒
- 审批状态

### 🚨 安全提醒
- 安全警告
- 权限提示
- 风险提醒

## 相关组件

- [TextWidget](text-widget.md) - 用于普通文本显示
- [CardWidget](card-widget.md) - 用于信息卡片容器
- [StatusWidget](status-widget.md) - 用于状态信息展示

## 下一步

了解了AlertWidget的基本用法后，建议继续学习：
- [CardWidget](card-widget.md) - 学习如何使用卡片容器
- [StatusWidget](status-widget.md) - 学习如何展示状态信息 