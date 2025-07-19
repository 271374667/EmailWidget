# System Monitoring Examples

This page demonstrates how to use EmailWidget to create system monitoring reports, implementing service health checks, resource monitoring, and alert notifications.

## Server Resource Monitoring

### System Resource Usage Report

```python
import psutil
from datetime import datetime
from email_widget import Email, ProgressWidget, StatusWidget, AlertWidget
from email_widget.core.enums import TextType, ProgressTheme, StatusType, AlertType

# Get system resource usage
def get_system_info():
    """Get basic system information"""
    return {
        'cpu_percent': psutil.cpu_percent(interval=1),
        'memory': psutil.virtual_memory(),
        'disk': psutil.disk_usage('/'),
        'network': psutil.net_io_counters(),
        'boot_time': datetime.fromtimestamp(psutil.boot_time())
    }

# Create system monitoring report
email = Email("Server Resource Monitoring Report")

email.add_title("🖥️ Server Resource Monitoring Report", TextType.TITLE_LARGE)
email.add_text(f"Monitoring Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 
               color="#666666")

# Get system information
sys_info = get_system_info()

# System overview
email.add_title("📊 System Overview", TextType.SECTION_H2)

uptime = datetime.now() - sys_info['boot_time']
overview_info = [
    ("Server Status", "🟢 Running Normal", "💻"),
    ("Uptime", f"{uptime.days} days {uptime.seconds//3600} hours", "⏰"),
    ("CPU Cores", f"{psutil.cpu_count()} cores", "⚙️"),
    ("Total Memory", f"{sys_info['memory'].total / (1024**3):.1f} GB", "💾")
]

for title, value, icon in overview_info:
    email.add_card(title=title, content=value, icon=icon)

# Resource usage details
email.add_title("📈 Resource Usage Details", TextType.SECTION_H2)

# CPU usage
cpu_usage = sys_info['cpu_percent']
cpu_theme = ProgressTheme.SUCCESS if cpu_usage < 50 else \
            ProgressTheme.WARNING if cpu_usage < 80 else ProgressTheme.ERROR

email.add_text("🔹 CPU Usage")
email.add_progress(cpu_usage, f"CPU: {cpu_usage:.1f}%", theme=cpu_theme)

# Memory usage
memory = sys_info['memory']
memory_usage = memory.percent
memory_theme = ProgressTheme.SUCCESS if memory_usage < 60 else \
               ProgressTheme.WARNING if memory_usage < 85 else ProgressTheme.ERROR

email.add_text("🔹 Memory Usage")
email.add_progress(memory_usage, f"Memory: {memory_usage:.1f}%", theme=memory_theme)

# Disk usage
disk = sys_info['disk']
disk_usage = (disk.used / disk.total) * 100
disk_theme = ProgressTheme.SUCCESS if disk_usage < 70 else \
             ProgressTheme.WARNING if disk_usage < 90 else ProgressTheme.ERROR

email.add_text("🔹 Disk Usage")
email.add_progress(disk_usage, f"Disk: {disk_usage:.1f}%", theme=disk_theme)

# Alert checking
email.add_title("⚠️ System Alerts", TextType.SECTION_H2)

# Check if any metrics need alerts
alerts = []
if cpu_usage > 80:
    alerts.append(("High CPU Usage", f"Current CPU usage {cpu_usage:.1f}%, recommend checking high CPU processes", AlertType.CAUTION))
if memory_usage > 85:
    alerts.append(("Low Memory", f"Memory usage {memory_usage:.1f}%, may affect system performance", AlertType.WARNING))
if disk_usage > 90:
    alerts.append(("Low Disk Space", f"Disk usage {disk_usage:.1f}%, recommend cleaning unnecessary files", AlertType.CAUTION))

if alerts:
    for title, content, alert_type in alerts:
        email.add_alert(content, alert_type, title)
else:
    email.add_alert("System running normally, all metrics within normal range", AlertType.TIP, "✅ System Status Good")

email.export_html("system_monitor.html")
print("✅ System monitoring report generated: system_monitor.html")
```

--8<-- "examples/assets/system_monitoring_html/system_monitor.html"

**Monitoring Features:**
- Real-time system resource usage acquisition
- Intelligent alert threshold settings
- Intuitive progress bar displays
- Automated status assessment

---

## Application Service Monitoring

### Multi-Service Health Check

```python
import requests
from datetime import datetime
from email_widget import Email, StatusWidget, TableWidget, AlertWidget
from email_widget.core.enums import TextType, StatusType, AlertType

# Define services to monitor
services = [
    {"name": "Web Service", "url": "http://localhost:8080/health", "timeout": 5},
    {"name": "API Service", "url": "http://localhost:3000/api/health", "timeout": 5},
    {"name": "Database", "url": "http://localhost:5432/health", "timeout": 3},
    {"name": "Redis Cache", "url": "http://localhost:6379/ping", "timeout": 3},
    {"name": "Message Queue", "url": "http://localhost:5672/health", "timeout": 5}
]

def check_service_health(service):
    """Check individual service health status"""
    try:
        start_time = datetime.now()
        response = requests.get(service["url"], timeout=service["timeout"])
        response_time = (datetime.now() - start_time).total_seconds() * 1000
        
        if response.status_code == 200:
            return {
                "status": "Normal",
                "response_time": response_time,
                "status_type": StatusType.SUCCESS,
                "error": None
            }
        else:
            return {
                "status": "Error",
                "response_time": response_time,
                "status_type": StatusType.ERROR,
                "error": f"HTTP {response.status_code}"
            }
    except requests.exceptions.Timeout:
        return {
            "status": "Timeout",
            "response_time": service["timeout"] * 1000,
            "status_type": StatusType.WARNING,
            "error": "Request timeout"
        }
    except Exception as e:
        return {
            "status": "Unreachable",
            "response_time": 0,
            "status_type": StatusType.ERROR,
            "error": str(e)
        }

# Create service monitoring report
email = Email("Application Service Monitoring Report")

email.add_title("🛠️ Application Service Monitoring Report", TextType.TITLE_LARGE)
email.add_text(f"Check Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Execute health checks
service_results = []
for service in services:
    result = check_service_health(service)
    service_results.append({
        "name": service["name"],
        "url": service["url"],
        **result
    })

# Service status overview
email.add_title("📊 Service Status Overview", TextType.SECTION_H2)

normal_count = sum(1 for r in service_results if r["status"] == "Normal")
total_count = len(service_results)
health_rate = (normal_count / total_count) * 100

overview_metrics = [
    ("Total Services", f"{total_count}", "🛠️"),
    ("Normal Services", f"{normal_count}", "✅"),
    ("Error Services", f"{total_count - normal_count}", "❌"),
    ("Health Rate", f"{health_rate:.1f}%", "💚")
]

for title, value, icon in overview_metrics:
    email.add_card(title=title, content=value, icon=icon)

# Service status details
email.add_title("🔍 Service Status Details", TextType.SECTION_H2)

for result in service_results:
    status_widget = StatusWidget()
    status_widget.set_title(result["name"]) \
                 .set_status(result["status"]) \
                 .set_status_type(result["status_type"]) \
                 .set_description(f"Response Time: {result['response_time']:.0f}ms")
    email.add_widget(status_widget)

# Detailed service table
email.add_title("📋 Detailed Monitoring Data", TextType.SECTION_H2)

table = TableWidget()
table.set_headers(["Service Name", "Status", "Response Time", "Error Message"])

for result in service_results:
    status_emoji = "🟢" if result["status"] == "Normal" else \
                  "🟡" if result["status"] == "Timeout" else "🔴"
    
    table.add_row([
        result["name"],
        f"{status_emoji} {result['status']}",
        f"{result['response_time']:.0f}ms",
        result["error"] or "None"
    ])

table.set_striped(True)
email.add_widget(table)

# Exception alerts
email.add_title("🚨 Exception Alerts", TextType.SECTION_H2)

error_services = [r for r in service_results if r["status"] != "Normal"]
if error_services:
    for service in error_services:
        alert_type = AlertType.WARNING if service["status"] == "Timeout" else AlertType.CAUTION
        email.add_alert(
            f"{service['name']} status abnormal: {service['error']}",
            alert_type,
            f"⚠️ {service['name']} Exception"
        )
else:
    email.add_alert("All services running normally", AlertType.TIP, "✅ System Status Good")

email.export_html("service_monitor.html")
print("✅ Service monitoring report generated: service_monitor.html")
```

--8<-- "examples/assets/system_monitoring_html/service_monitor.html"

**Monitoring Highlights:**
- Multi-service concurrent checking
- Response time statistics
- Automatic exception alerts
- Health rate calculation

---

## Log Analysis Monitoring

### System Log Statistical Analysis

```python
import re
from datetime import datetime, timedelta
from collections import Counter
from email_widget import Email, TableWidget, ProgressWidget
from email_widget.core.enums import TextType, ProgressTheme

# Simulate log data (in real applications, read from log files)
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
    """Analyze log data"""
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
    
    # Statistical analysis
    level_counts = Counter(log['level'] for log in parsed_logs)
    error_messages = [log['message'] for log in parsed_logs if log['level'] == 'ERROR']
    
    return {
        'total_logs': len(parsed_logs),
        'level_counts': level_counts,
        'error_messages': error_messages,
        'parsed_logs': parsed_logs
    }

# Create log analysis report
email = Email("System Log Analysis Report")

email.add_title("📝 System Log Analysis Report", TextType.TITLE_LARGE)
email.add_text(f"Analysis Time Range: Last 1 hour")

# Analyze logs
log_analysis = analyze_logs(sample_logs)

# Log statistics overview
email.add_title("📊 Log Statistics Overview", TextType.SECTION_H2)

total_logs = log_analysis['total_logs']
error_count = log_analysis['level_counts'].get('ERROR', 0)
warn_count = log_analysis['level_counts'].get('WARN', 0)
info_count = log_analysis['level_counts'].get('INFO', 0)

log_stats = [
    ("Total Logs", f"{total_logs:,}", "📄"),
    ("Error Logs", f"{error_count}", "🔴"),
    ("Warning Logs", f"{warn_count}", "🟡"),
    ("Info Logs", f"{info_count}", "🟢")
]

for title, value, icon in log_stats:
    email.add_card(title=title, content=value, icon=icon)

# Log level distribution
email.add_title("📈 Log Level Distribution", TextType.SECTION_H2)

for level, count in log_analysis['level_counts'].items():
    percentage = (count / total_logs) * 100
    
    # Set theme color based on log level
    if level == 'ERROR':
        theme = ProgressTheme.ERROR
    elif level == 'WARN':
        theme = ProgressTheme.WARNING
    elif level == 'INFO':
        theme = ProgressTheme.SUCCESS
    else:
        theme = ProgressTheme.INFO
    
    email.add_text(f"🔹 {level} Level")
    email.add_progress(percentage, f"{count} entries ({percentage:.1f}%)", theme=theme)

# Error log details
if error_count > 0:
    email.add_title("🚨 Error Log Details", TextType.SECTION_H2)
    
    error_table = TableWidget()
    error_table.set_headers(["No.", "Error Message"])
    
    for i, error_msg in enumerate(log_analysis['error_messages'], 1):
        error_table.add_row([str(i), error_msg])
    
    error_table.set_striped(True)
    email.add_widget(error_table)

# System health assessment
email.add_title("💡 System Health Assessment", TextType.SECTION_H2)

error_rate = (error_count / total_logs) * 100 if total_logs > 0 else 0
warn_rate = (warn_count / total_logs) * 100 if total_logs > 0 else 0

health_assessment = f"""
**System Health Assessment Based on Log Analysis:**

📊 **Key Metrics**
• Error Rate: {error_rate:.1f}% ({error_count}/{total_logs})
• Warning Rate: {warn_rate:.1f}% ({warn_count}/{total_logs})
• System Status: {'🔴 Needs Attention' if error_rate > 10 else '🟡 Needs Improvement' if error_rate > 5 else '🟢 Running Well'}

💡 **Recommended Actions**
"""

if error_rate > 10:
    health_assessment += """
• Immediately check error logs and fix critical issues
• Increase monitoring frequency, track system status in real-time
• Consider system maintenance and optimization
"""
elif error_rate > 5:
    health_assessment += """
• Regularly check error logs, prevent issues from expanding
• Optimize system configuration, reduce error occurrence
• Establish more comprehensive monitoring mechanisms
"""
else:
    health_assessment += """
• Maintain current operations level
• Continue regular monitoring and analysis
• Optimize system performance and stability
"""

email.add_text(health_assessment.strip())

email.export_html("log_analysis.html")
print("✅ Log analysis report generated: log_analysis.html")
```

--8<-- "examples/assets/system_monitoring_html/log_analysis.html"

**Analysis Value:**
- Automated log parsing and statistics
- Error rate and warning rate calculation
- Intelligent health assessment
- Problem identification and recommendations

---

## Database Monitoring

### Database Performance Monitoring

```python
# Simulate database monitoring data
database_metrics = {
    'connections': {'active': 45, 'max': 100, 'idle': 15},
    'queries': {'slow_queries': 12, 'total_queries': 8547, 'avg_response_time': 0.8},
    'storage': {'size': 2.4, 'growth_rate': 0.15, 'fragmentation': 8.2},
    'performance': {'cpu_usage': 35.2, 'memory_usage': 72.1, 'io_wait': 5.8}
}

from email_widget import Email, ProgressWidget, TableWidget, StatusWidget
from email_widget.core.enums import TextType, ProgressTheme, StatusType

# Create database monitoring report
email = Email("Database Performance Monitoring Report")

email.add_title("🗄️ Database Performance Monitoring Report", TextType.TITLE_LARGE)

# Database status overview
email.add_title("📊 Database Status Overview", TextType.SECTION_H2)

# Connection pool status
connections = database_metrics['connections']
conn_usage = (connections['active'] / connections['max']) * 100

db_overview = [
    ("Database Status", "🟢 Running Normal", "💾"),
    ("Active Connections", f"{connections['active']}/{connections['max']}", "🔗"),
    ("Connection Usage", f"{conn_usage:.1f}%", "📊"),
    ("Database Size", f"{database_metrics['storage']['size']:.1f} GB", "💿")
]

for title, value, icon in db_overview:
    email.add_card(title=title, content=value, icon=icon)

# Performance metrics monitoring
email.add_title("⚡ Performance Metrics", TextType.SECTION_H2)

performance = database_metrics['performance']

# CPU usage
cpu_theme = ProgressTheme.SUCCESS if performance['cpu_usage'] < 50 else \
           ProgressTheme.WARNING if performance['cpu_usage'] < 80 else ProgressTheme.ERROR

email.add_text("🔹 Database CPU Usage")
email.add_progress(performance['cpu_usage'], f"CPU: {performance['cpu_usage']:.1f}%", theme=cpu_theme)

# Memory usage
memory_theme = ProgressTheme.SUCCESS if performance['memory_usage'] < 70 else \
              ProgressTheme.WARNING if performance['memory_usage'] < 90 else ProgressTheme.ERROR

email.add_text("🔹 Database Memory Usage")
email.add_progress(performance['memory_usage'], f"Memory: {performance['memory_usage']:.1f}%", theme=memory_theme)

# Connection pool usage
conn_theme = ProgressTheme.SUCCESS if conn_usage < 60 else \
            ProgressTheme.WARNING if conn_usage < 85 else ProgressTheme.ERROR

email.add_text("🔹 Connection Pool Usage")
email.add_progress(conn_usage, f"Connection Pool: {conn_usage:.1f}%", theme=conn_theme)

# Query performance analysis
email.add_title("🔍 Query Performance Analysis", TextType.SECTION_H2)

queries = database_metrics['queries']
slow_query_rate = (queries['slow_queries'] / queries['total_queries']) * 100

query_table = TableWidget()
query_table.set_headers(["Metric", "Value", "Status"])

query_metrics = [
    ("Total Queries", f"{queries['total_queries']:,}", "Normal"),
    ("Slow Queries", f"{queries['slow_queries']}", "Needs Attention" if queries['slow_queries'] > 10 else "Normal"),
    ("Slow Query Rate", f"{slow_query_rate:.2f}%", "Warning" if slow_query_rate > 1 else "Normal"),
    ("Avg Response Time", f"{queries['avg_response_time']:.1f}ms", "Excellent" if queries['avg_response_time'] < 1 else "Normal")
]

for metric, value, status in query_metrics:
    status_emoji = "🟢" if status == "Normal" or status == "Excellent" else \
                  "🟡" if status == "Needs Attention" else "🔴"
    query_table.add_row([metric, value, f"{status_emoji} {status}"])

query_table.set_striped(True)
email.add_widget(query_table)

email.export_html("database_monitor.html")
print("✅ Database monitoring report generated: database_monitor.html")
```

--8<-- "examples/assets/system_monitoring_html/database_monitor.html"

**Monitoring Focus:**
- Connection pool usage
- Query performance analysis
- Resource usage monitoring
- Storage growth trends

---

## Comprehensive Monitoring Dashboard

### Complete System Monitoring Overview

```python
from email_widget import Email, ColumnWidget, StatusWidget
from email_widget.core.enums import TextType, StatusType

# Create comprehensive monitoring dashboard
email = Email("System Comprehensive Monitoring Dashboard")

email.add_title("🎛️ System Comprehensive Monitoring Dashboard", TextType.TITLE_LARGE)
email.add_text(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Use column layout to display multiple monitoring modules
column_layout = ColumnWidget()

# Left column: System status
left_column = ColumnWidget()
left_column.add_widget(StatusWidget()
                      .set_title("Web Service")
                      .set_status("Normal")
                      .set_status_type(StatusType.SUCCESS)
                      .set_description("Response Time: 120ms"))

left_column.add_widget(StatusWidget()
                      .set_title("Database")
                      .set_status("Normal")
                      .set_status_type(StatusType.SUCCESS)
                      .set_description("Connections: 45/100"))

# Right column: Resource monitoring
right_column = ColumnWidget()
right_column.add_widget(StatusWidget()
                       .set_title("CPU Usage")
                       .set_status("45%")
                       .set_status_type(StatusType.SUCCESS)
                       .set_description("Moderate Load"))

right_column.add_widget(StatusWidget()
                       .set_title("Memory Usage")
                       .set_status("72%")
                       .set_status_type(StatusType.WARNING)
                       .set_description("Usage High"))

# Combine column layout
column_layout.add_column(left_column)
column_layout.add_column(right_column)
email.add_widget(column_layout)

# Current alert summary
email.add_title("🚨 Current Alerts", TextType.SECTION_H2)
email.add_alert("Memory usage reached 72%, recommend monitoring", AlertType.WARNING, "Memory Alert")

email.export_html("monitoring_dashboard.html")
print("✅ Comprehensive monitoring dashboard generated: monitoring_dashboard.html")
```

--8<-- "examples/assets/system_monitoring_html/monitoring_dashboard.html"

**Dashboard Features:**
- Modular design
- Real-time status display
- Multi-dimensional monitoring
- Responsive layout

---

## Learning Summary

Through system monitoring examples, you have mastered:

### 🎯 Monitoring Skills
- **Resource Monitoring** - CPU, memory, disk usage
- **Service Monitoring** - Health checks and status management
- **Log Analysis** - Automated log parsing and statistics
- **Performance Monitoring** - Database and application performance

### 🛠️ Technical Points
- Real-time data acquisition and display
- Intelligent alert threshold settings
- Multi-service status aggregation
- Visual monitoring dashboards

### 💡 Best Practices
- Layered monitoring architecture
- Automated anomaly detection
- Intuitive status display
- Timely alert notifications

### 🚀 Application Scenarios
- DevOps operations monitoring
- Server resource management
- Application performance monitoring
- System health checks

Continue learning [Spider Reports](spider-reports.md) and [Real Applications](real-world.md) to explore more professional applications!