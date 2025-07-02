# 状态组件 (Status Widgets)

状态组件用于展示系统状态、健康检查结果、监控指标等关键信息。EmailWidget 提供了 StatusWidget 组件来集中显示多个状态项。

## 🚀 快速开始

```python
from email_widget.widgets import StatusWidget
from email_widget.core.enums import StatusType, LayoutType

# 基本状态组件
status = StatusWidget()
status.set_title("系统状态")
status.add_status_item("服务器", "运行正常", StatusType.SUCCESS)
status.add_status_item("数据库", "连接异常", StatusType.ERROR)
status.add_status_item("缓存", "负载较高", StatusType.WARNING)
```

<div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0;">
    <h3 style="font-size: 16px; font-weight: 600; color: #323130; margin-bottom: 12px;">系统状态</h3>
    <div style="margin: 8px 0; padding: 8px 0; border-bottom: 1px solid #f3f2f1;">
        <div style="font-weight: 500; color: #605e5c; font-size: 14px;">服务器</div>
        <div style="color: #107c10; font-size: 14px; font-weight: 600;">运行正常</div>
    </div>
    <div style="margin: 8px 0; padding: 8px 0; border-bottom: 1px solid #f3f2f1;">
        <div style="font-weight: 500; color: #605e5c; font-size: 14px;">数据库</div>
        <div style="color: #d13438; font-size: 14px; font-weight: 600;">连接异常</div>
    </div>
    <div style="margin: 8px 0; padding: 8px 0; border-bottom: 1px solid #f3f2f1;">
        <div style="font-weight: 500; color: #605e5c; font-size: 14px;">缓存</div>
        <div style="color: #ff8c00; font-size: 14px; font-weight: 600;">负载较高</div>
    </div>
</div>

## 📊 基本用法

### 添加状态项

```python
# 创建状态组件
status = StatusWidget()
status.set_title("服务健康检查")

# 添加不同状态的项目
status.add_status_item("Web服务", "正常运行", StatusType.SUCCESS)
status.add_status_item("API网关", "响应缓慢", StatusType.WARNING)  
status.add_status_item("支付服务", "服务中断", StatusType.ERROR)
status.add_status_item("监控系统", "数据收集中", StatusType.INFO)

# 批量添加状态项
status_items = [
    ("用户服务", "负载正常", StatusType.SUCCESS),
    ("订单服务", "队列堆积", StatusType.WARNING),
    ("通知服务", "发送失败", StatusType.ERROR)
]

for label, value, status_type in status_items:
    status.add_status_item(label, value, status_type)
```

### 布局模式

StatusWidget 支持垂直和水平两种布局：

```python
# 垂直布局（默认）
vertical_status = StatusWidget()
vertical_status.set_layout(LayoutType.VERTICAL)
vertical_status.set_title("服务状态 - 垂直布局")
vertical_status.add_status_item("CPU使用率", "45%", StatusType.SUCCESS)
vertical_status.add_status_item("内存使用率", "78%", StatusType.WARNING)

# 水平布局
horizontal_status = StatusWidget()
horizontal_status.set_layout(LayoutType.HORIZONTAL)
horizontal_status.set_title("关键指标 - 水平布局")
horizontal_status.add_status_item("在线用户", "12,450", StatusType.INFO)
horizontal_status.add_status_item("今日订单", "1,287", StatusType.SUCCESS)
```

<div style="margin: 16px 0;">
    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin-bottom: 16px;">
        <h3 style="font-size: 16px; font-weight: 600; color: #323130; margin-bottom: 12px;">服务状态 - 垂直布局</h3>
        <div style="margin: 8px 0; padding: 8px 0; border-bottom: 1px solid #f3f2f1;">
            <div style="font-weight: 500; color: #605e5c; font-size: 14px;">CPU使用率</div>
            <div style="color: #107c10; font-size: 14px; font-weight: 600;">45%</div>
        </div>
        <div style="margin: 8px 0; padding: 8px 0; border-bottom: 1px solid #f3f2f1;">
            <div style="font-weight: 500; color: #605e5c; font-size: 14px;">内存使用率</div>
            <div style="color: #ff8c00; font-size: 14px; font-weight: 600;">78%</div>
        </div>
    </div>
    
    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px;">
        <h3 style="font-size: 16px; font-weight: 600; color: #323130; margin-bottom: 12px;">关键指标 - 水平布局</h3>
        <div style="display: flex; justify-content: space-between; align-items: center; margin: 8px 0; padding: 8px 0; border-bottom: 1px solid #f3f2f1;">
            <span style="font-weight: 500; color: #605e5c; font-size: 14px;">在线用户</span>
            <span style="color: #0078d4; font-size: 14px; font-weight: 600;">12,450</span>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin: 8px 0; padding: 8px 0; border-bottom: 1px solid #f3f2f1;">
            <span style="font-weight: 500; color: #605e5c; font-size: 14px;">今日订单</span>
            <span style="color: #107c10; font-size: 14px; font-weight: 600;">1,287</span>
        </div>
    </div>
</div>

## 🎨 状态类型

StatusWidget 支持四种状态类型，每种类型都有对应的颜色主题：

### 状态类型说明

```python
from email_widget.core.enums import StatusType

# SUCCESS - 绿色，表示正常、成功
status.add_status_item("备份任务", "已完成", StatusType.SUCCESS)

# WARNING - 橙色，表示警告、需注意  
status.add_status_item("磁盘空间", "85% 已使用", StatusType.WARNING)

# ERROR - 红色，表示错误、故障
status.add_status_item("网络连接", "连接失败", StatusType.ERROR)

# INFO - 蓝色，表示信息、中性状态
status.add_status_item("系统版本", "v2.1.0", StatusType.INFO)
```

<div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0;">
    <h3 style="font-size: 16px; font-weight: 600; color: #323130; margin-bottom: 12px;">状态类型示例</h3>
    <div style="margin: 8px 0; padding: 8px 0; border-bottom: 1px solid #f3f2f1;">
        <div style="font-weight: 500; color: #605e5c; font-size: 14px;">备份任务</div>
        <div style="color: #107c10; font-size: 14px; font-weight: 600;">✅ 已完成</div>
    </div>
    <div style="margin: 8px 0; padding: 8px 0; border-bottom: 1px solid #f3f2f1;">
        <div style="font-weight: 500; color: #605e5c; font-size: 14px;">磁盘空间</div>
        <div style="color: #ff8c00; font-size: 14px; font-weight: 600;">⚠️ 85% 已使用</div>
    </div>
    <div style="margin: 8px 0; padding: 8px 0; border-bottom: 1px solid #f3f2f1;">
        <div style="font-weight: 500; color: #605e5c; font-size: 14px;">网络连接</div>
        <div style="color: #d13438; font-size: 14px; font-weight: 600;">❌ 连接失败</div>
    </div>
    <div style="margin: 8px 0; padding: 8px 0; border-bottom: 1px solid #f3f2f1;">
        <div style="font-weight: 500; color: #605e5c; font-size: 14px;">系统版本</div>
        <div style="color: #0078d4; font-size: 14px; font-weight: 600;">ℹ️ v2.1.0</div>
    </div>
</div>

### 状态颜色参考

| 状态类型 | 颜色代码 | 适用场景 | 示例 |
|---------|---------|----------|------|
| `SUCCESS` | #107c10 (绿色) | 正常运行、任务完成、健康状态 | 服务正常、备份成功 |
| `WARNING` | #ff8c00 (橙色) | 需要注意、性能警告、即将到期 | 内存不足、证书即将过期 |
| `ERROR` | #d13438 (红色) | 错误状态、服务中断、故障 | 连接失败、服务异常 |
| `INFO` | #0078d4 (蓝色) | 一般信息、版本号、统计数据 | 版本信息、用户数量 |

## 📋 实际应用示例

### 系统监控面板

```python
from email_widget import Email
from email_widget.widgets import StatusWidget, TextWidget
from email_widget.core.enums import StatusType, LayoutType, TextType

# 创建监控报告
monitoring = Email("系统监控报告")

# 添加标题
monitoring.add_widget(
    TextWidget()
    .set_content("服务器集群监控报告")
    .set_text_type(TextType.SECTION_H2)
    .set_align(TextAlign.CENTER)
)

# 核心服务状态
core_services = StatusWidget()
core_services.set_title("🔧 核心服务状态")
core_services.add_status_item("Web服务器", "运行正常 (99.9% 正常运行时间)", StatusType.SUCCESS)
core_services.add_status_item("数据库集群", "主库正常，从库延迟", StatusType.WARNING)
core_services.add_status_item("Redis缓存", "内存使用率 89%", StatusType.WARNING)
core_services.add_status_item("消息队列", "队列积压严重", StatusType.ERROR)
core_services.add_status_item("文件存储", "存储空间充足", StatusType.SUCCESS)

# 性能指标
performance_metrics = StatusWidget()
performance_metrics.set_title("📊 性能指标")
performance_metrics.set_layout(LayoutType.HORIZONTAL)
performance_metrics.add_status_item("平均响应时间", "245ms", StatusType.SUCCESS)
performance_metrics.add_status_item("并发用户数", "8,450", StatusType.INFO)
performance_metrics.add_status_item("错误率", "0.02%", StatusType.SUCCESS)
performance_metrics.add_status_item("吞吐量", "1,250 req/s", StatusType.INFO)

# 资源使用情况
resource_usage = StatusWidget()
resource_usage.set_title("💻 资源使用情况")
resource_usage.add_status_item("CPU 使用率", "平均 45%，峰值 78%", StatusType.SUCCESS)
resource_usage.add_status_item("内存使用率", "67% (32GB/48GB)", StatusType.WARNING)
resource_usage.add_status_item("磁盘 I/O", "读: 125MB/s，写: 89MB/s", StatusType.SUCCESS)
resource_usage.add_status_item("网络带宽", "入: 450Mbps，出: 1.2Gbps", StatusType.INFO)

# 安全状态
security_status = StatusWidget()
security_status.set_title("🔒 安全状态")
security_status.add_status_item("防火墙", "规则已更新，运行正常", StatusType.SUCCESS)
security_status.add_status_item("SSL证书", "将在30天后过期", StatusType.WARNING)
security_status.add_status_item("入侵检测", "发现2次可疑尝试", StatusType.WARNING)
security_status.add_status_item("访问控制", "权限配置正常", StatusType.SUCCESS)

monitoring.add_widgets([
    core_services, performance_metrics, 
    resource_usage, security_status
])
```

### 业务KPI仪表板

```python
# 业务KPI监控
kpi_dashboard = Email("业务KPI仪表板")

# 销售指标
sales_metrics = StatusWidget()
sales_metrics.set_title("💰 销售指标")
sales_metrics.set_layout(LayoutType.HORIZONTAL)
sales_metrics.add_status_item("今日销售额", "¥245,670", StatusType.SUCCESS)
sales_metrics.add_status_item("月度目标完成", "78%", StatusType.WARNING)
sales_metrics.add_status_item("客单价", "¥189", StatusType.INFO)
sales_metrics.add_status_item("转化率", "3.2%", StatusType.SUCCESS)

# 用户指标
user_metrics = StatusWidget()
user_metrics.set_title("👥 用户指标")
user_metrics.add_status_item("在线用户数", "12,450 人", StatusType.INFO)
user_metrics.add_status_item("新注册用户", "今日 +890", StatusType.SUCCESS)
user_metrics.add_status_item("用户留存率", "7天: 68%，30天: 42%", StatusType.WARNING)
user_metrics.add_status_item("客户满意度", "4.6/5.0", StatusType.SUCCESS)

# 运营指标
operation_metrics = StatusWidget()
operation_metrics.set_title("📈 运营指标")
operation_metrics.add_status_item("页面浏览量", "今日 856K PV", StatusType.INFO)
operation_metrics.add_status_item("跳出率", "42%", StatusType.SUCCESS)
operation_metrics.add_status_item("平均停留时间", "4分32秒", StatusType.SUCCESS)
operation_metrics.add_status_item("移动端占比", "73%", StatusType.INFO)

kpi_dashboard.add_widgets([sales_metrics, user_metrics, operation_metrics])
```

### 项目状态跟踪

```python
# 项目状态跟踪
project_status = Email("项目状态跟踪")

# 开发进度
dev_progress = StatusWidget()
dev_progress.set_title("🚀 开发进度")
dev_progress.add_status_item("需求分析", "已完成", StatusType.SUCCESS)
dev_progress.add_status_item("架构设计", "评审中", StatusType.WARNING)
dev_progress.add_status_item("前端开发", "70% 完成", StatusType.INFO)
dev_progress.add_status_item("后端开发", "45% 完成", StatusType.INFO)
dev_progress.add_status_item("数据库设计", "待开始", StatusType.ERROR)

# 团队状态
team_status = StatusWidget()
team_status.set_title("👨‍💻 团队状态")
team_status.set_layout(LayoutType.HORIZONTAL)
team_status.add_status_item("前端团队", "2人，进度正常", StatusType.SUCCESS)
team_status.add_status_item("后端团队", "3人，有1人请假", StatusType.WARNING)
team_status.add_status_item("测试团队", "1人，资源不足", StatusType.ERROR)
team_status.add_status_item("设计团队", "1人，任务饱和", StatusType.INFO)

# 质量指标
quality_metrics = StatusWidget()
quality_metrics.set_title("📋 质量指标")
quality_metrics.add_status_item("代码覆盖率", "82%", StatusType.SUCCESS)
quality_metrics.add_status_item("已知Bug数量", "15个严重，23个一般", StatusType.WARNING)
quality_metrics.add_status_item("技术债务", "中等水平", StatusType.WARNING)
quality_metrics.add_status_item("文档完整度", "65%", StatusType.ERROR)

project_status.add_widgets([dev_progress, team_status, quality_metrics])
```

## ⚙️ API 参考

### StatusWidget 核心方法

| 方法 | 参数 | 说明 | 示例 |
|------|------|------|------|
| `set_title()` | `title: str` | 设置组件标题 | `.set_title("系统状态")` |
| `add_status_item()` | `label: str, value: str, status: StatusType` | 添加状态项 | `.add_status_item("CPU", "45%", StatusType.SUCCESS)` |
| `set_layout()` | `layout: LayoutType` | 设置布局方式 | `.set_layout(LayoutType.HORIZONTAL)` |
| `clear_items()` | 无 | 清空所有状态项 | `.clear_items()` |

### StatusItem 数据结构

```python
# StatusItem 内部数据结构
class StatusItem:
    label: str          # 状态项标签
    value: str          # 状态项值
    status: StatusType  # 状态类型
```

### 布局类型

```python
from email_widget.core.enums import LayoutType

LayoutType.VERTICAL     # 垂直布局（默认）
LayoutType.HORIZONTAL   # 水平布局
```

## 🎯 最佳实践

### 1. 合理分组状态信息
```python
# 推荐：按功能模块分组
database_status = StatusWidget().set_title("数据库状态")
cache_status = StatusWidget().set_title("缓存服务")
api_status = StatusWidget().set_title("API服务")
```

### 2. 选择合适的布局方式
```python
# 垂直布局 - 适合详细信息
detailed_status = StatusWidget()
detailed_status.set_layout(LayoutType.VERTICAL)
detailed_status.add_status_item("服务器", "运行正常，负载45%", StatusType.SUCCESS)

# 水平布局 - 适合简洁指标
metrics = StatusWidget()
metrics.set_layout(LayoutType.HORIZONTAL)
metrics.add_status_item("在线", "1,250", StatusType.INFO)
```

### 3. 提供有意义的状态描述
```python
# 推荐：包含具体数值和描述
status.add_status_item("内存使用", "6.4GB/16GB (40%)", StatusType.SUCCESS)

# 避免：过于简单的描述
status.add_status_item("内存", "正常", StatusType.SUCCESS)
```

### 4. 合理使用状态类型
```python
# 推荐：根据实际情况选择状态类型
if cpu_usage > 80:
    status_type = StatusType.ERROR
elif cpu_usage > 60:
    status_type = StatusType.WARNING
else:
    status_type = StatusType.SUCCESS
```

### 5. 保持状态项数量适中
```python
# 推荐：每个StatusWidget包含3-8个状态项
status = StatusWidget()
# 添加5-6个核心状态项
# 避免添加过多项目影响可读性
```

## 🚨 注意事项

1. **状态一致性**: 确保相同类型的状态使用相同的StatusType
2. **信息完整性**: 状态描述应该包含足够的信息便于理解
3. **更新频率**: 考虑状态信息的时效性，及时更新
4. **布局选择**: 根据内容长度选择合适的布局方式
5. **颜色语义**: 遵循常见的颜色语义约定（红色=错误，绿色=正常等）

## 🔧 故障排除

### 状态显示异常
- 检查StatusType是否正确设置
- 验证状态值是否包含特殊字符
- 确认布局类型设置是否合适

### 布局问题
- 水平布局时注意文本长度
- 垂直布局时考虑总体高度
- 移动设备上的显示效果

---

**下一步**: 了解 [布局组件](layout-widgets.md) 学习如何组织页面布局。 