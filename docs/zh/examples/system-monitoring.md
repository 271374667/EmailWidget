# 系统监控示例

本页面展示如何使用 EmailWidget 创建系统监控报告，实现服务状态检查、资源监控和告警通知。

## 服务器资源监控

### 系统资源使用情况报告

```python
import psutil
from datetime import datetime
from email_widget import Email, ProgressWidget, StatusWidget, AlertWidget
from email_widget.core.enums import TextType, ProgressTheme, StatusType, AlertType

# 获取系统资源使用情况
def get_system_info():
    """获取系统基本信息"""
    return {
        'cpu_percent': psutil.cpu_percent(interval=1),
        'memory': psutil.virtual_memory(),
        'disk': psutil.disk_usage('/'),
        'network': psutil.net_io_counters(),
        'boot_time': datetime.fromtimestamp(psutil.boot_time())
    }

# 创建系统监控报告
email = Email("服务器资源监控报告")

email.add_title("🖥️ 服务器资源监控报告", TextType.TITLE_LARGE)
email.add_text(f"监控时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 
               color="#666666")

# 获取系统信息
sys_info = get_system_info()

# 系统概况
email.add_title("📊 系统概况", TextType.SECTION_H2)

uptime = datetime.now() - sys_info['boot_time']
overview_info = [
    ("服务器状态", "🟢 正常运行", "💻"),
    ("运行时间", f"{uptime.days}天 {uptime.seconds//3600}小时", "⏰"),
    ("CPU核心数", f"{psutil.cpu_count()}核", "⚙️"),
    ("内存总量", f"{sys_info['memory'].total / (1024**3):.1f} GB", "💾")
]

for title, value, icon in overview_info:
    email.add_card(title=title, content=value, icon=icon)

# 资源使用详情
email.add_title("📈 资源使用详情", TextType.SECTION_H2)

# CPU使用率
cpu_usage = sys_info['cpu_percent']
cpu_theme = ProgressTheme.SUCCESS if cpu_usage < 50 else \
            ProgressTheme.WARNING if cpu_usage < 80 else ProgressTheme.ERROR

email.add_text("🔹 CPU使用率")
email.add_progress(cpu_usage, f"CPU: {cpu_usage:.1f}%", theme=cpu_theme)

# 内存使用率
memory = sys_info['memory']
memory_usage = memory.percent
memory_theme = ProgressTheme.SUCCESS if memory_usage < 60 else \
               ProgressTheme.WARNING if memory_usage < 85 else ProgressTheme.ERROR

email.add_text("🔹 内存使用率")
email.add_progress(memory_usage, f"内存: {memory_usage:.1f}%", theme=memory_theme)

# 磁盘使用率
disk = sys_info['disk']
disk_usage = (disk.used / disk.total) * 100
disk_theme = ProgressTheme.SUCCESS if disk_usage < 70 else \
             ProgressTheme.WARNING if disk_usage < 90 else ProgressTheme.ERROR

email.add_text("🔹 磁盘使用率")
email.add_progress(disk_usage, f"磁盘: {disk_usage:.1f}%", theme=disk_theme)

# 告警检查
email.add_title("⚠️ 系统告警", TextType.SECTION_H2)

# 检查各项指标是否需要告警
alerts = []
if cpu_usage > 80:
    alerts.append(("CPU使用率过高", f"当前CPU使用率{cpu_usage:.1f}%，建议检查高CPU进程", AlertType.CAUTION))
if memory_usage > 85:
    alerts.append(("内存不足", f"内存使用率{memory_usage:.1f}%，可能影响系统性能", AlertType.WARNING))
if disk_usage > 90:
    alerts.append(("磁盘空间不足", f"磁盘使用率{disk_usage:.1f}%，建议清理无用文件", AlertType.CAUTION))

if alerts:
    for title, content, alert_type in alerts:
        email.add_alert(content, alert_type, title)
else:
    email.add_alert("系统运行正常，所有指标均在正常范围内", AlertType.TIP, "✅ 系统状态良好")

email.export_html("system_monitor.html")
print("✅ 系统监控报告已生成：system_monitor.html")
```

--8<-- "examples/assets/system_monitoring_html/system_monitor.html"

**监控特点：**
- 实时获取系统资源使用情况
- 智能告警阈值设置
- 直观的进度条显示
- 自动化状态评估

---

## 应用服务监控

### 多服务健康检查

```python
import requests
from datetime import datetime
from email_widget import Email, StatusWidget, TableWidget, AlertWidget
from email_widget.core.enums import TextType, StatusType, AlertType

# 定义要监控的服务
services = [
    {"name": "Web服务", "url": "http://localhost:8080/health", "timeout": 5},
    {"name": "API服务", "url": "http://localhost:3000/api/health", "timeout": 5},
    {"name": "数据库", "url": "http://localhost:5432/health", "timeout": 3},
    {"name": "Redis缓存", "url": "http://localhost:6379/ping", "timeout": 3},
    {"name": "消息队列", "url": "http://localhost:5672/health", "timeout": 5}
]

def check_service_health(service):
    """检查单个服务健康状态"""
    try:
        start_time = datetime.now()
        response = requests.get(service["url"], timeout=service["timeout"])
        response_time = (datetime.now() - start_time).total_seconds() * 1000
        
        if response.status_code == 200:
            return {
                "status": "正常",
                "response_time": response_time,
                "status_type": StatusType.SUCCESS,
                "error": None
            }
        else:
            return {
                "status": "异常",
                "response_time": response_time,
                "status_type": StatusType.ERROR,
                "error": f"HTTP {response.status_code}"
            }
    except requests.exceptions.Timeout:
        return {
            "status": "超时",
            "response_time": service["timeout"] * 1000,
            "status_type": StatusType.WARNING,
            "error": "请求超时"
        }
    except Exception as e:
        return {
            "status": "不可达",
            "response_time": 0,
            "status_type": StatusType.ERROR,
            "error": str(e)
        }

# 创建服务监控报告
email = Email("应用服务监控报告")

email.add_title("🛠️ 应用服务监控报告", TextType.TITLE_LARGE)
email.add_text(f"检查时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# 执行健康检查
service_results = []
for service in services:
    result = check_service_health(service)
    service_results.append({
        "name": service["name"],
        "url": service["url"],
        **result
    })

# 服务状态概览
email.add_title("📊 服务状态概览", TextType.SECTION_H2)

normal_count = sum(1 for r in service_results if r["status"] == "正常")
total_count = len(service_results)
health_rate = (normal_count / total_count) * 100

overview_metrics = [
    ("服务总数", f"{total_count}", "🛠️"),
    ("正常服务", f"{normal_count}", "✅"),
    ("异常服务", f"{total_count - normal_count}", "❌"),
    ("健康率", f"{health_rate:.1f}%", "💚")
]

for title, value, icon in overview_metrics:
    email.add_card(title=title, content=value, icon=icon)

# 服务状态详情
email.add_title("🔍 服务状态详情", TextType.SECTION_H2)

for result in service_results:
    status_widget = StatusWidget()
    status_widget.set_title(result["name"]) \
                 .set_status(result["status"]) \
                 .set_status_type(result["status_type"]) \
                 .set_description(f"响应时间: {result['response_time']:.0f}ms")
    email.add_widget(status_widget)

# 详细服务表格
email.add_title("📋 详细监控数据", TextType.SECTION_H2)

table = TableWidget()
table.set_headers(["服务名称", "状态", "响应时间", "错误信息"])

for result in service_results:
    status_emoji = "🟢" if result["status"] == "正常" else \
                  "🟡" if result["status"] == "超时" else "🔴"
    
    table.add_row([
        result["name"],
        f"{status_emoji} {result['status']}",
        f"{result['response_time']:.0f}ms",
        result["error"] or "无"
    ])

table.set_striped(True)
email.add_widget(table)

# 异常告警
email.add_title("🚨 异常告警", TextType.SECTION_H2)

error_services = [r for r in service_results if r["status"] != "正常"]
if error_services:
    for service in error_services:
        alert_type = AlertType.WARNING if service["status"] == "超时" else AlertType.CAUTION
        email.add_alert(
            f"{service['name']} 状态异常: {service['error']}",
            alert_type,
            f"⚠️ {service['name']} 异常"
        )
else:
    email.add_alert("所有服务运行正常", AlertType.TIP, "✅ 系统状态良好")

email.export_html("service_monitor.html")
print("✅ 服务监控报告已生成：service_monitor.html")
```

--8<-- "examples/assets/system_monitoring_html/service_monitor.html"

**监控亮点：**
- 多服务并发检查
- 响应时间统计
- 异常自动告警
- 健康率计算

---

## 日志分析监控

### 系统日志统计分析

```python
import re
from datetime import datetime, timedelta
from collections import Counter
from email_widget import Email, TableWidget, ProgressWidget
from email_widget.core.enums import TextType, ProgressTheme

# 模拟日志数据（实际应用中从日志文件读取）
sample_logs = [
    "2024-01-20 10:15:23 INFO User login successful: user123",
    "2024-01-20 10:16:45 ERROR Database connection failed: timeout",
    "2024-01-20 10:17:12 WARN High memory usage detected: 85%",
    "2024-01-20 10:18:30 INFO User logout: user123",
    "2024-01-20 10:19:55 ERROR API request failed: 500 Internal Server Error",
    "2024-01-20 10:20:18 INFO New user registration: user456",
    "2024-01-20 10:21:44 WARN Slow query detected: 3.2s",
    "2024-01-20 10:22:17 ERROR File not found: config.xml",
    "2024-01-20 10:23:35 INFO Backup completed successfully",
    "2024-01-20 10:24:52 ERROR Network timeout: redis connection",
]

def analyze_logs(logs):
    """分析日志数据"""
    log_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)'
    
    parsed_logs = []
    for log in logs:
        match = re.match(log_pattern, log)
        if match:
            timestamp, level, message = match.groups()
            parsed_logs.append({
                'timestamp': datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S'),
                'level': level,
                'message': message
            })
    
    # 统计分析
    level_counts = Counter(log['level'] for log in parsed_logs)
    error_messages = [log['message'] for log in parsed_logs if log['level'] == 'ERROR']
    
    return {
        'total_logs': len(parsed_logs),
        'level_counts': level_counts,
        'error_messages': error_messages,
        'parsed_logs': parsed_logs
    }

# 创建日志分析报告
email = Email("系统日志分析报告")

email.add_title("📝 系统日志分析报告", TextType.TITLE_LARGE)
email.add_text(f"分析时间范围: 最近1小时")

# 分析日志
log_analysis = analyze_logs(sample_logs)

# 日志统计概览
email.add_title("📊 日志统计概览", TextType.SECTION_H2)

total_logs = log_analysis['total_logs']
error_count = log_analysis['level_counts'].get('ERROR', 0)
warn_count = log_analysis['level_counts'].get('WARN', 0)
info_count = log_analysis['level_counts'].get('INFO', 0)

log_stats = [
    ("日志总数", f"{total_logs:,}", "📄"),
    ("错误日志", f"{error_count}", "🔴"),
    ("警告日志", f"{warn_count}", "🟡"),
    ("信息日志", f"{info_count}", "🟢")
]

for title, value, icon in log_stats:
    email.add_card(title=title, content=value, icon=icon)

# 日志级别分布
email.add_title("📈 日志级别分布", TextType.SECTION_H2)

for level, count in log_analysis['level_counts'].items():
    percentage = (count / total_logs) * 100
    
    # 根据日志级别设置主题色
    if level == 'ERROR':
        theme = ProgressTheme.ERROR
    elif level == 'WARN':
        theme = ProgressTheme.WARNING
    elif level == 'INFO':
        theme = ProgressTheme.SUCCESS
    else:
        theme = ProgressTheme.INFO
    
    email.add_text(f"🔹 {level} 级别")
    email.add_progress(percentage, f"{count} 条 ({percentage:.1f}%)", theme=theme)

# 错误日志详情
if error_count > 0:
    email.add_title("🚨 错误日志详情", TextType.SECTION_H2)
    
    error_table = TableWidget()
    error_table.set_headers(["序号", "错误信息"])
    
    for i, error_msg in enumerate(log_analysis['error_messages'], 1):
        error_table.add_row([str(i), error_msg])
    
    error_table.set_striped(True)
    email.add_widget(error_table)

# 系统健康评估
email.add_title("💡 系统健康评估", TextType.SECTION_H2)

error_rate = (error_count / total_logs) * 100 if total_logs > 0 else 0
warn_rate = (warn_count / total_logs) * 100 if total_logs > 0 else 0

health_assessment = f"""
**基于日志分析的系统健康评估：**

📊 **关键指标**
• 错误率: {error_rate:.1f}% ({error_count}/{total_logs})
• 警告率: {warn_rate:.1f}% ({warn_count}/{total_logs})
• 系统状态: {'🔴 需要关注' if error_rate > 10 else '🟡 有待改善' if error_rate > 5 else '🟢 运行良好'}

💡 **建议措施**
"""

if error_rate > 10:
    health_assessment += """
• 立即检查错误日志，修复关键问题
• 增加监控频率，实时跟踪系统状态
• 考虑系统维护和优化
"""
elif error_rate > 5:
    health_assessment += """
• 定期检查错误日志，预防问题扩大
• 优化系统配置，减少错误发生
• 建立更完善的监控机制
"""
else:
    health_assessment += """
• 保持当前运维水平
• 继续定期监控和分析
• 优化系统性能和稳定性
"""

email.add_text(health_assessment.strip())

email.export_html("log_analysis.html")
print("✅ 日志分析报告已生成：log_analysis.html")
```

--8<-- "examples/assets/system_monitoring_html/log_analysis.html"

**分析价值：**
- 自动化日志解析和统计
- 错误率和警告率计算
- 智能健康评估
- 问题定位和建议

---

## 数据库监控

### 数据库性能监控

```python
# 模拟数据库监控数据
database_metrics = {
    'connections': {'active': 45, 'max': 100, 'idle': 15},
    'queries': {'slow_queries': 12, 'total_queries': 8547, 'avg_response_time': 0.8},
    'storage': {'size': 2.4, 'growth_rate': 0.15, 'fragmentation': 8.2},
    'performance': {'cpu_usage': 35.2, 'memory_usage': 72.1, 'io_wait': 5.8}
}

from email_widget import Email, ProgressWidget, TableWidget, StatusWidget
from email_widget.core.enums import TextType, ProgressTheme, StatusType

# 创建数据库监控报告
email = Email("数据库性能监控报告")

email.add_title("🗄️ 数据库性能监控报告", TextType.TITLE_LARGE)

# 数据库状态概览
email.add_title("📊 数据库状态概览", TextType.SECTION_H2)

# 连接池状态
connections = database_metrics['connections']
conn_usage = (connections['active'] / connections['max']) * 100

db_overview = [
    ("数据库状态", "🟢 正常运行", "💾"),
    ("活跃连接", f"{connections['active']}/{connections['max']}", "🔗"),
    ("连接使用率", f"{conn_usage:.1f}%", "📊"),
    ("数据库大小", f"{database_metrics['storage']['size']:.1f} GB", "💿")
]

for title, value, icon in db_overview:
    email.add_card(title=title, content=value, icon=icon)

# 性能指标监控
email.add_title("⚡ 性能指标", TextType.SECTION_H2)

performance = database_metrics['performance']

# CPU使用率
cpu_theme = ProgressTheme.SUCCESS if performance['cpu_usage'] < 50 else \
           ProgressTheme.WARNING if performance['cpu_usage'] < 80 else ProgressTheme.ERROR

email.add_text("🔹 数据库CPU使用率")
email.add_progress(performance['cpu_usage'], f"CPU: {performance['cpu_usage']:.1f}%", theme=cpu_theme)

# 内存使用率
memory_theme = ProgressTheme.SUCCESS if performance['memory_usage'] < 70 else \
              ProgressTheme.WARNING if performance['memory_usage'] < 90 else ProgressTheme.ERROR

email.add_text("🔹 数据库内存使用率")
email.add_progress(performance['memory_usage'], f"内存: {performance['memory_usage']:.1f}%", theme=memory_theme)

# 连接池使用率
conn_theme = ProgressTheme.SUCCESS if conn_usage < 60 else \
            ProgressTheme.WARNING if conn_usage < 85 else ProgressTheme.ERROR

email.add_text("🔹 连接池使用率")
email.add_progress(conn_usage, f"连接池: {conn_usage:.1f}%", theme=conn_theme)

# 查询性能分析
email.add_title("🔍 查询性能分析", TextType.SECTION_H2)

queries = database_metrics['queries']
slow_query_rate = (queries['slow_queries'] / queries['total_queries']) * 100

query_table = TableWidget()
query_table.set_headers(["指标", "数值", "状态"])

query_metrics = [
    ("总查询数", f"{queries['total_queries']:,}", "正常"),
    ("慢查询数", f"{queries['slow_queries']}", "需关注" if queries['slow_queries'] > 10 else "正常"),
    ("慢查询率", f"{slow_query_rate:.2f}%", "警告" if slow_query_rate > 1 else "正常"),
    ("平均响应时间", f"{queries['avg_response_time']:.1f}ms", "优秀" if queries['avg_response_time'] < 1 else "正常")
]

for metric, value, status in query_metrics:
    status_emoji = "🟢" if status == "正常" or status == "优秀" else \
                  "🟡" if status == "需关注" else "🔴"
    query_table.add_row([metric, value, f"{status_emoji} {status}"])

query_table.set_striped(True)
email.add_widget(query_table)

email.export_html("database_monitor.html")
print("✅ 数据库监控报告已生成：database_monitor.html")
```

--8<-- "examples/assets/system_monitoring_html/database_monitor.html"

**监控重点：**
- 连接池使用情况
- 查询性能分析
- 资源使用监控
- 存储增长趋势

---

## 综合监控仪表板

### 完整的系统监控概览

```python
from email_widget import Email, ColumnWidget, StatusWidget
from email_widget.core.enums import TextType, StatusType

# 创建综合监控仪表板
email = Email("系统综合监控仪表板")

email.add_title("🎛️ 系统综合监控仪表板", TextType.TITLE_LARGE)
email.add_text(f"最后更新: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# 使用列布局展示多个监控模块
column_layout = ColumnWidget()

# 左列：系统状态
left_column = ColumnWidget()
left_column.add_widget(StatusWidget()
                      .set_title("Web服务")
                      .set_status("正常")
                      .set_status_type(StatusType.SUCCESS)
                      .set_description("响应时间: 120ms"))

left_column.add_widget(StatusWidget()
                      .set_title("数据库")
                      .set_status("正常")
                      .set_status_type(StatusType.SUCCESS)
                      .set_description("连接数: 45/100"))

# 右列：资源监控
right_column = ColumnWidget()
right_column.add_widget(StatusWidget()
                       .set_title("CPU使用率")
                       .set_status("45%")
                       .set_status_type(StatusType.SUCCESS)
                       .set_description("负载适中"))

right_column.add_widget(StatusWidget()
                       .set_title("内存使用")
                       .set_status("72%")
                       .set_status_type(StatusType.WARNING)
                       .set_description("使用率偏高"))

# 组合列布局
column_layout.add_column(left_column)
column_layout.add_column(right_column)
email.add_widget(column_layout)

# 当前告警汇总
email.add_title("🚨 当前告警", TextType.SECTION_H2)
email.add_alert("内存使用率达到72%，建议监控", AlertType.WARNING, "内存告警")

email.export_html("monitoring_dashboard.html")
print("✅ 综合监控仪表板已生成：monitoring_dashboard.html")
```

--8<-- "examples/assets/system_monitoring_html/monitoring_dashboard.html"

**仪表板特色：**
- 模块化设计
- 实时状态展示
- 多维度监控
- 响应式布局

---

## 学习总结

通过系统监控示例，您已经掌握了：

### 🎯 监控技能
- **资源监控** - CPU、内存、磁盘使用率
- **服务监控** - 健康检查和状态管理
- **日志分析** - 自动化日志解析和统计
- **性能监控** - 数据库和应用性能

### 🛠️ 技术要点
- 实时数据获取和展示
- 智能告警阈值设置
- 多服务状态聚合
- 可视化监控仪表板

### 💡 最佳实践
- 分层监控架构
- 自动化异常检测
- 直观的状态展示
- 及时的告警通知

### 🚀 应用场景
- DevOps运维监控
- 服务器资源管理
- 应用性能监控
- 系统健康检查

继续学习 [爬虫报告](spider-reports.md) 和 [实际应用](real-world.md)，探索更多专业应用！
