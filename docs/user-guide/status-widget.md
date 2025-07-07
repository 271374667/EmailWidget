# StatusWidget 状态组件

<div style="background: #f0f8ff; border: 1px solid #4a90e2; border-radius: 8px; padding: 20px; margin: 20px 0;">
  <h3 style="color: #2c5282; margin-top: 0;">📊 状态展示组件</h3>
  <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 12px 0; font-family: 'Segoe UI', Tahoma, Arial, sans-serif;">
    <h4 style="font-size: 16px; font-weight: 600; color: #323130; margin-bottom: 12px;">系统状态</h4>
    <div style="display: flex; justify-content: space-between; align-items: center; margin: 8px 0; padding: 8px 0; border-bottom: 1px solid #f3f2f1;">
      <span style="font-weight: 500; color: #605e5c; font-size: 14px;">CPU使用率</span>
      <span style="color: #107c10; font-size: 14px; font-weight: 600;">68%</span>
    </div>
    <div style="display: flex; justify-content: space-between; align-items: center; margin: 8px 0; padding: 8px 0; border-bottom: 1px solid #f3f2f1;">
      <span style="font-weight: 500; color: #605e5c; font-size: 14px;">内存使用</span>
      <span style="color: #ff8c00; font-size: 14px; font-weight: 600;">4.2GB / 8GB</span>
    </div>
    <div style="display: flex; justify-content: space-between; align-items: center; margin: 8px 0; padding: 8px 0; border-bottom: 1px solid #f3f2f1;">
      <span style="font-weight: 500; color: #605e5c; font-size: 14px;">磁盘空间</span>
      <span style="color: #107c10; font-size: 14px; font-weight: 600;">256GB / 512GB</span>
    </div>
    <div style="display: flex; justify-content: space-between; align-items: center; margin: 8px 0; padding: 8px 0;">
      <span style="font-weight: 500; color: #605e5c; font-size: 14px;">网络状态</span>
      <span style="color: #d13438; font-size: 14px; font-weight: 600;">断开连接</span>
    </div>
  </div>
  <div style="display: flex; gap: 10px; margin-top: 15px;">
    <span style="background: #e8f4fd; color: #0078d4; padding: 4px 8px; border-radius: 4px; font-size: 12px;">状态展示</span>
    <span style="background: #e8f4fd; color: #0078d4; padding: 4px 8px; border-radius: 4px; font-size: 12px;">实时更新</span>
    <span style="background: #e8f4fd; color: #0078d4; padding: 4px 8px; border-radius: 4px; font-size: 12px;">状态分类</span>
  </div>
</div>

StatusWidget是一个专门用于显示系统状态、配置信息或键值对数据的组件。它支持多种状态类型的颜色标识，提供灵活的布局选项，是监控面板和状态报告的理想选择。

## 🎯 主要功能

### 状态项管理
- **动态添加**：支持动态添加状态项
- **状态更新**：实时更新状态值和类型
- **状态移除**：支持移除指定状态项
- **状态分类**：支持SUCCESS、WARNING、ERROR、INFO等状态类型

### 布局控制
- **垂直布局**：标签和值垂直排列（默认）
- **水平布局**：标签和值水平对齐
- **自定义样式**：支持自定义颜色和字体

### 数据展示
- **键值对显示**：清晰的标签-值对展示
- **状态着色**：根据状态类型自动着色
- **标题支持**：可选的组件标题

## 📋 核心方法

### 基础使用

```python
from email_widget.widgets import StatusWidget
from email_widget.core.enums import StatusType, LayoutType

# 创建状态组件
status = StatusWidget()

# 添加状态项
status.add_status_item("服务状态", "运行中", StatusType.SUCCESS)
status.add_status_item("CPU使用率", "68%", StatusType.WARNING)
status.add_status_item("内存使用", "4.2GB / 8GB", StatusType.INFO)
```

### 状态管理方法

```python
# 添加状态项
status.add_status_item(label, value, status_type)

# 更新状态项
status.update_item("服务状态", "已停止", StatusType.ERROR)

# 移除状态项
status.remove_item("CPU使用率")

# 清空所有状态项
status.clear_items()

# 获取状态项数量
count = status.get_item_count()
```

### 布局和样式

```python
# 设置标题
status.set_title("系统状态监控")

# 设置布局（水平/垂直）
status.set_layout(LayoutType.HORIZONTAL)  # 水平布局
status.set_layout(LayoutType.VERTICAL)    # 垂直布局（默认）
```

## 💡 实用示例

### 系统监控面板

```python
from email_widget.widgets import StatusWidget
from email_widget.core.enums import StatusType, LayoutType

# 创建系统监控状态
monitor = StatusWidget()
monitor.set_title("系统监控面板")
monitor.set_layout(LayoutType.HORIZONTAL)

# 添加系统状态
monitor.add_status_item("CPU使用率", "68%", StatusType.WARNING)
monitor.add_status_item("内存使用", "4.2GB / 8GB", StatusType.INFO)
monitor.add_status_item("磁盘空间", "256GB / 512GB", StatusType.SUCCESS)
monitor.add_status_item("网络状态", "断开连接", StatusType.ERROR)

# 渲染组件
html = monitor.render_html()
```

### 服务状态报告

```python
# 创建服务状态报告
service_status = StatusWidget()
service_status.set_title("服务状态报告")

# 添加服务状态
service_status.add_status_item("Web服务", "运行中", StatusType.SUCCESS)
service_status.add_status_item("数据库", "连接正常", StatusType.SUCCESS)
service_status.add_status_item("缓存服务", "部分故障", StatusType.WARNING)
service_status.add_status_item("文件服务", "离线", StatusType.ERROR)

# 更新状态
service_status.update_item("缓存服务", "已恢复", StatusType.SUCCESS)
```

### 配置信息展示

```python
# 创建配置信息展示
config_info = StatusWidget()
config_info.set_title("应用配置")
config_info.set_layout(LayoutType.VERTICAL)

# 添加配置项
config_info.add_status_item("应用版本", "v2.1.0", StatusType.INFO)
config_info.add_status_item("环境", "生产环境", StatusType.PRIMARY)
config_info.add_status_item("数据库版本", "MySQL 8.0", StatusType.INFO)
config_info.add_status_item("最后更新", "2024-01-15", StatusType.INFO)
```

### 动态状态更新

```python
# 创建动态状态监控
dynamic_status = StatusWidget()
dynamic_status.set_title("实时状态")

# 初始状态
dynamic_status.add_status_item("连接状态", "连接中...", StatusType.INFO)
dynamic_status.add_status_item("数据同步", "等待中", StatusType.WARNING)

# 模拟状态更新
def update_status():
    # 更新连接状态
    dynamic_status.update_item("连接状态", "已连接", StatusType.SUCCESS)
    
    # 更新同步状态
    dynamic_status.update_item("数据同步", "同步完成", StatusType.SUCCESS)
    
    # 添加新状态
    dynamic_status.add_status_item("最后同步", "刚刚", StatusType.INFO)
```

## 📊 状态类型详解

### 状态类型说明

| 状态类型 | 颜色 | 适用场景 |
|---------|------|----------|
| `SUCCESS` | 绿色 | 成功状态、正常运行 |
| `WARNING` | 橙色 | 警告状态、需要关注 |
| `ERROR` | 红色 | 错误状态、需要处理 |
| `INFO` | 蓝色 | 信息状态、一般信息 |
| `PRIMARY` | 蓝色 | 主要信息、重要配置 |

### 状态使用建议

```python
# 服务状态
StatusType.SUCCESS   # 服务正常运行
StatusType.WARNING   # 服务有警告但仍可用
StatusType.ERROR     # 服务故障或不可用

# 资源使用
StatusType.SUCCESS   # 资源使用正常（< 70%）
StatusType.WARNING   # 资源使用较高（70-90%）
StatusType.ERROR     # 资源使用过高（> 90%）

# 配置信息
StatusType.INFO      # 一般配置信息
StatusType.PRIMARY   # 重要配置信息
```

## 📐 布局选择指南

### 水平布局（HORIZONTAL）
- **适用场景**：状态项较多，需要紧凑显示
- **特点**：标签和值在同一行，左右对齐
- **推荐用途**：监控面板、状态表格

### 垂直布局（VERTICAL）
- **适用场景**：状态项较少，需要清晰展示
- **特点**：标签和值分行显示
- **推荐用途**：配置信息、详细状态

## 🎨 最佳实践

### 1. 状态分类管理

```python
# 按类别组织状态
system_status = StatusWidget()
system_status.set_title("系统状态")

# 核心服务状态
system_status.add_status_item("Web服务", "运行中", StatusType.SUCCESS)
system_status.add_status_item("API服务", "运行中", StatusType.SUCCESS)

# 资源状态
system_status.add_status_item("CPU", "68%", StatusType.WARNING)
system_status.add_status_item("内存", "4.2GB", StatusType.INFO)
```

### 2. 状态更新策略

```python
# 批量更新状态
def update_system_status(status_widget, metrics):
    for metric_name, value, status_type in metrics:
        status_widget.update_item(metric_name, value, status_type)
```

### 3. 状态阈值管理

```python
# 根据阈值设置状态类型
def get_cpu_status(usage):
    if usage < 70:
        return StatusType.SUCCESS
    elif usage < 90:
        return StatusType.WARNING
    else:
        return StatusType.ERROR

cpu_usage = 68
status.add_status_item("CPU使用率", f"{cpu_usage}%", get_cpu_status(cpu_usage))
```

### 4. 组合使用

```python
# 多个状态组件组合
from email_widget.widgets import ColumnWidget

# 创建多列状态展示
column = ColumnWidget().set_columns(2)

# 系统状态
system_status = StatusWidget()
system_status.set_title("系统状态")
system_status.add_status_item("服务", "运行中", StatusType.SUCCESS)

# 性能状态
performance_status = StatusWidget()
performance_status.set_title("性能指标")
performance_status.add_status_item("响应时间", "120ms", StatusType.INFO)

# 组合显示
column.add_widgets([system_status, performance_status])
```

## 🔧 常见问题

### Q: 如何实现状态的自动更新？
A: 通过定期调用 `update_item()` 方法来更新状态值和类型。

### Q: 状态项过多时如何优化显示？
A: 使用水平布局（`LayoutType.HORIZONTAL`）或考虑分组显示。

### Q: 如何自定义状态颜色？
A: 目前支持预定义的状态类型，如需自定义颜色可以通过CSS样式覆盖。

### Q: 状态项的显示顺序如何控制？
A: 状态项按添加顺序显示，可以通过 `clear_items()` 后重新添加来调整顺序。

StatusWidget为您提供了灵活而强大的状态展示功能，无论是系统监控、服务状态还是配置信息展示，都能轻松胜任！ 