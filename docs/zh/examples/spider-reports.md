# 爬虫报告示例

本页面展示如何使用 EmailWidget 为爬虫和数据采集项目创建专业的监控报告。

## 爬虫任务监控

### 数据采集进度跟踪

```python
from datetime import datetime, timedelta
import random
from email_widget import Email, ProgressWidget, TableWidget, StatusWidget
from email_widget.core.enums import TextType, ProgressTheme, StatusType

# 模拟爬虫任务数据
spider_tasks = [
    {
        'name': '电商产品信息采集',
        'target_count': 10000,
        'completed_count': 8500,
        'success_rate': 95.2,
        'avg_speed': 120,  # 条/分钟
        'status': '运行中',
        'start_time': datetime.now() - timedelta(hours=2)
    },
    {
        'name': '新闻资讯爬取',
        'target_count': 5000,
        'completed_count': 5000,
        'success_rate': 98.8,
        'avg_speed': 200,
        'status': '已完成',
        'start_time': datetime.now() - timedelta(hours=1, minutes=30)
    },
    {
        'name': '用户评论数据',
        'target_count': 20000,
        'completed_count': 12000,
        'success_rate': 92.1,
        'avg_speed': 80,
        'status': '运行中',
        'start_time': datetime.now() - timedelta(hours=3)
    }
]

# 创建爬虫监控报告
email = Email("爬虫任务监控报告")

email.add_title("🕷️ 爬虫任务监控报告", TextType.TITLE_LARGE)
email.add_text(f"报告时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# 任务概览统计
email.add_title("📊 任务概览", TextType.SECTION_H2)

total_tasks = len(spider_tasks)
running_tasks = sum(1 for task in spider_tasks if task['status'] == '运行中')
completed_tasks = sum(1 for task in spider_tasks if task['status'] == '已完成')
total_collected = sum(task['completed_count'] for task in spider_tasks)

overview_stats = [
    ("任务总数", f"{total_tasks}", "🎯"),
    ("运行中", f"{running_tasks}", "🔄"),
    ("已完成", f"{completed_tasks}", "✅"),
    ("总采集量", f"{total_collected:,}", "📦")
]

for title, value, icon in overview_stats:
    email.add_card(title=title, content=value, icon=icon)

# 各任务详细进度
email.add_title("📈 任务进度详情", TextType.SECTION_H2)

for task in spider_tasks:
    # 计算进度百分比
    progress_percent = (task['completed_count'] / task['target_count']) * 100
    
    # 根据状态设置主题色
    if task['status'] == '已完成':
        theme = ProgressTheme.SUCCESS
        status_type = StatusType.SUCCESS
    elif task['success_rate'] > 95:
        theme = ProgressTheme.INFO
        status_type = StatusType.SUCCESS
    elif task['success_rate'] > 90:
        theme = ProgressTheme.WARNING
        status_type = StatusType.WARNING
    else:
        theme = ProgressTheme.ERROR
        status_type = StatusType.ERROR
    
    # 任务状态卡片
    status_widget = StatusWidget()
    status_widget.set_title(task['name']) \
                 .set_status(task['status']) \
                 .set_status_type(status_type) \
                 .set_description(f"成功率: {task['success_rate']:.1f}% | 速度: {task['avg_speed']}条/分钟")
    email.add_widget(status_widget)
    
    # 进度条
    email.add_progress(
        value=progress_percent,
        label=f"{task['completed_count']:,}/{task['target_count']:,} ({progress_percent:.1f}%)",
        theme=theme
    )

# 详细数据表格
email.add_title("📋 任务详细数据", TextType.SECTION_H2)

table = TableWidget()
table.set_headers(["任务名称", "目标数量", "已完成", "完成率", "成功率", "平均速度", "运行时长"])

for task in spider_tasks:
    runtime = datetime.now() - task['start_time']
    runtime_str = f"{runtime.seconds // 3600}h {(runtime.seconds % 3600) // 60}m"
    
    progress_percent = (task['completed_count'] / task['target_count']) * 100
    
    table.add_row([
        task['name'],
        f"{task['target_count']:,}",
        f"{task['completed_count']:,}",
        f"{progress_percent:.1f}%",
        f"{task['success_rate']:.1f}%",
        f"{task['avg_speed']}条/分钟",
        runtime_str
    ])

table.set_striped(True)
email.add_widget(table)

# 性能分析
email.add_title("⚡ 性能分析", TextType.SECTION_H2)

avg_success_rate = sum(task['success_rate'] for task in spider_tasks) / len(spider_tasks)
fastest_task = max(spider_tasks, key=lambda x: x['avg_speed'])
slowest_task = min(spider_tasks, key=lambda x: x['avg_speed'])

performance_text = f"""
**爬虫性能分析：**

📊 **整体表现**
• 平均成功率: {avg_success_rate:.1f}%
• 最快任务: {fastest_task['name']} ({fastest_task['avg_speed']}条/分钟)
• 最慢任务: {slowest_task['name']} ({slowest_task['avg_speed']}条/分钟)

💡 **优化建议**
• 成功率低于90%的任务需要检查反爬策略
• 考虑调整并发数以提高采集速度
• 监控目标网站的响应时间变化
"""

email.add_text(performance_text.strip())

email.export_html("spider_monitor.html")
print("✅ 爬虫监控报告已生成：spider_monitor.html")
```

--8<-- "examples/assets/spider_reports_html/spider_monitor.html"

**监控特点：**
- 实时任务进度跟踪
- 成功率和速度监控
- 多任务状态聚合
- 性能分析和优化建议

---

## 数据质量报告

### 采集数据质量检查

```python
import pandas as pd
from email_widget import Email, TableWidget, AlertWidget, ProgressWidget
from email_widget.core.enums import TextType, AlertType, ProgressTheme

# 模拟采集的数据质量统计
data_quality_stats = {
    'total_records': 50000,
    'valid_records': 47500,
    'duplicate_records': 1200,
    'incomplete_records': 800,
    'invalid_format': 500,
    'fields_quality': {
        '标题': {'completeness': 98.5, 'validity': 99.2},
        '价格': {'completeness': 95.2, 'validity': 92.8},
        '图片URL': {'completeness': 89.3, 'validity': 88.1},
        '商品描述': {'completeness': 78.6, 'validity': 95.4},
        '评分': {'completeness': 92.1, 'validity': 98.7}
    }
}

# 创建数据质量报告
email = Email("数据质量检查报告")

email.add_title("🔍 数据质量检查报告", TextType.TITLE_LARGE)
email.add_text(f"数据检查时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# 数据质量概览
email.add_title("📊 数据质量概览", TextType.SECTION_H2)

total = data_quality_stats['total_records']
valid = data_quality_stats['valid_records']
duplicate = data_quality_stats['duplicate_records']
incomplete = data_quality_stats['incomplete_records']
invalid = data_quality_stats['invalid_format']

quality_rate = (valid / total) * 100
duplicate_rate = (duplicate / total) * 100

quality_overview = [
    ("总记录数", f"{total:,}", "📦"),
    ("有效记录", f"{valid:,}", "✅"),
    ("数据质量率", f"{quality_rate:.1f}%", "🎯"),
    ("重复率", f"{duplicate_rate:.1f}%", "🔄")
]

for title, value, icon in quality_overview:
    email.add_card(title=title, content=value, icon=icon)

# 数据质量详细分析
email.add_title("📈 质量指标分析", TextType.SECTION_H2)

# 整体质量评分
overall_quality = (valid / total) * 100
quality_theme = ProgressTheme.SUCCESS if overall_quality > 95 else \
               ProgressTheme.WARNING if overall_quality > 90 else ProgressTheme.ERROR

email.add_text("🔹 整体数据质量")
email.add_progress(overall_quality, f"质量率: {overall_quality:.1f}%", theme=quality_theme)

# 重复数据率
dup_theme = ProgressTheme.SUCCESS if duplicate_rate < 2 else \
           ProgressTheme.WARNING if duplicate_rate < 5 else ProgressTheme.ERROR

email.add_text("🔹 重复数据比例")
email.add_progress(duplicate_rate, f"重复率: {duplicate_rate:.1f}%", theme=dup_theme)

# 字段质量详情
email.add_title("🔍 字段质量详情", TextType.SECTION_H2)

field_table = TableWidget()
field_table.set_headers(["字段名称", "完整性", "有效性", "质量评级"])

for field_name, quality in data_quality_stats['fields_quality'].items():
    completeness = quality['completeness']
    validity = quality['validity']
    avg_quality = (completeness + validity) / 2
    
    # 质量评级
    if avg_quality >= 95:
        grade = "🟢 优秀"
    elif avg_quality >= 90:
        grade = "🟡 良好"
    elif avg_quality >= 80:
        grade = "🟠 一般"
    else:
        grade = "🔴 较差"
    
    field_table.add_row([
        field_name,
        f"{completeness:.1f}%",
        f"{validity:.1f}%",
        grade
    ])

field_table.set_striped(True)
email.add_widget(field_table)

# 数据问题统计
email.add_title("⚠️ 数据问题统计", TextType.SECTION_H2)

problem_table = TableWidget()
problem_table.set_headers(["问题类型", "记录数", "占比", "影响等级"])

problems = [
    ("重复记录", duplicate, (duplicate/total)*100, "中等"),
    ("不完整记录", incomplete, (incomplete/total)*100, "高"),
    ("格式错误", invalid, (invalid/total)*100, "高"),
]

for problem_type, count, percentage, impact in problems:
    impact_emoji = "🟢" if impact == "低" else "🟡" if impact == "中等" else "🔴"
    problem_table.add_row([
        problem_type,
        f"{count:,}",
        f"{percentage:.1f}%",
        f"{impact_emoji} {impact}"
    ])

problem_table.set_striped(True)
email.add_widget(problem_table)

# 质量改进建议
email.add_title("💡 质量改进建议", TextType.SECTION_H2)

# 根据数据质量情况生成建议
if overall_quality < 90:
    email.add_alert(
        "数据质量低于90%，建议立即优化爬虫逻辑和数据清洗流程",
        AlertType.CAUTION,
        "🚨 质量告警"
    )

if duplicate_rate > 5:
    email.add_alert(
        f"重复数据率达到{duplicate_rate:.1f}%，建议增强去重机制",
        AlertType.WARNING,
        "⚠️ 重复数据告警"
    )

# 改进建议
improvement_suggestions = f"""
**数据质量改进建议：**

🔧 **技术改进**
• 加强数据验证规则，提高字段有效性
• 优化去重算法，降低重复数据率
• 完善异常处理，减少不完整记录

📊 **质量监控**
• 设置质量阈值告警 (建议: 质量率>95%, 重复率<2%)
• 实时监控关键字段的完整性
• 定期进行数据质量评估

⚡ **流程优化**
• 在数据入库前进行质量检查
• 建立数据质量评分体系
• 自动化数据清洗和修复流程
"""

email.add_text(improvement_suggestions.strip())

email.export_html("data_quality_report.html")
print("✅ 数据质量报告已生成：data_quality_report.html")
```

--8<-- "examples/assets/spider_reports_html/data_quality_report.html"

**质量检查特色：**
- 多维度质量评估
- 字段级别质量分析
- 自动化问题识别
- 改进建议生成

---

## 异常监控报告

### 爬虫异常和错误分析

```python
from collections import Counter
from email_widget import Email, ChartWidget, TableWidget, AlertWidget
from email_widget.core.enums import TextType, AlertType
import matplotlib.pyplot as plt

# 模拟爬虫异常数据
spider_errors = [
    {'timestamp': '2024-01-20 10:15', 'error_type': 'HTTP_TIMEOUT', 'url': 'example1.com', 'message': '请求超时'},
    {'timestamp': '2024-01-20 10:16', 'error_type': 'PARSING_ERROR', 'url': 'example2.com', 'message': '解析失败'},
    {'timestamp': '2024-01-20 10:17', 'error_type': 'HTTP_404', 'url': 'example3.com', 'message': '页面不存在'},
    {'timestamp': '2024-01-20 10:18', 'error_type': 'RATE_LIMITED', 'url': 'example4.com', 'message': '请求被限制'},
    {'timestamp': '2024-01-20 10:19', 'error_type': 'HTTP_TIMEOUT', 'url': 'example5.com', 'message': '连接超时'},
    {'timestamp': '2024-01-20 10:20', 'error_type': 'CAPTCHA_DETECTED', 'url': 'example6.com', 'message': '检测到验证码'},
    {'timestamp': '2024-01-20 10:21', 'error_type': 'PARSING_ERROR', 'url': 'example7.com', 'message': '数据结构变化'},
    {'timestamp': '2024-01-20 10:22', 'error_type': 'HTTP_403', 'url': 'example8.com', 'message': '访问被禁止'},
]

# 创建异常监控报告
email = Email("爬虫异常监控报告")

email.add_title("🚨 爬虫异常监控报告", TextType.TITLE_LARGE)
email.add_text(f"异常统计时间: 最近1小时")

# 异常统计概览
error_counts = Counter(error['error_type'] for error in spider_errors)
total_errors = len(spider_errors)

email.add_title("📊 异常统计概览", TextType.SECTION_H2)

error_overview = [
    ("异常总数", f"{total_errors}", "🚨"),
    ("异常类型", f"{len(error_counts)}", "🔍"),
    ("最多异常", f"{error_counts.most_common(1)[0][0]}", "⚠️"),
    ("时间范围", "最近1小时", "⏰")
]

for title, value, icon in error_overview:
    email.add_card(title=title, content=value, icon=icon)

# 异常类型分布
email.add_title("📈 异常类型分布", TextType.SECTION_H2)

# 创建异常分布图表
plt.figure(figsize=(10, 6))
error_types = list(error_counts.keys())
error_values = list(error_counts.values())

bars = plt.bar(error_types, error_values, color=['#e74c3c', '#f39c12', '#3498db', '#9b59b6', '#1abc9c', '#95a5a6'])
plt.title('异常类型分布', fontsize=14)
plt.xlabel('异常类型')
plt.ylabel('发生次数')
plt.xticks(rotation=45)

# 添加数值标签
for bar, value in zip(bars, error_values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
             str(value), ha='center', va='bottom')

plt.tight_layout()
error_chart_path = "spider_errors_distribution.png"
plt.savefig(error_chart_path, dpi=150, bbox_inches='tight')
plt.close()

chart = ChartWidget()
chart.set_chart_path(error_chart_path) \
     .set_title("异常类型分布图") \
     .set_description("显示各类异常的发生频率")
email.add_widget(chart)

# 异常详情表格
email.add_title("📋 异常详情列表", TextType.SECTION_H2)

error_table = TableWidget()
error_table.set_headers(["时间", "异常类型", "目标URL", "错误信息"])

for error in spider_errors[-10:]:  # 显示最近10条异常
    error_table.add_row([
        error['timestamp'],
        error['error_type'],
        error['url'][:30] + "..." if len(error['url']) > 30 else error['url'],
        error['message']
    ])

error_table.set_striped(True)
email.add_widget(error_table)

# 异常分析和建议
email.add_title("💡 异常分析与建议", TextType.SECTION_H2)

# 基于异常类型生成告警和建议
critical_errors = ['RATE_LIMITED', 'CAPTCHA_DETECTED', 'HTTP_403']
timeout_errors = ['HTTP_TIMEOUT']
parsing_errors = ['PARSING_ERROR']

for error_type, count in error_counts.items():
    if error_type in critical_errors:
        email.add_alert(
            f"{error_type} 发生 {count} 次，可能触发反爬虫机制",
            AlertType.CAUTION,
            f"🚨 {error_type} 告警"
        )
    elif error_type in timeout_errors and count > 3:
        email.add_alert(
            f"超时错误频发 ({count} 次)，建议检查网络连接和超时设置",
            AlertType.WARNING,
            "⚠️ 超时告警"
        )

analysis_text = f"""
**异常分析结果：**

🔍 **主要问题**
• {error_counts.most_common(1)[0][0]} 是最频繁的异常类型 ({error_counts.most_common(1)[0][1]} 次)
• 总异常率需要关注，建议优化爬虫策略

🛠️ **解决建议**
"""

# 针对不同异常类型给出建议
if 'HTTP_TIMEOUT' in error_counts:
    analysis_text += f"\n• 超时异常 ({error_counts['HTTP_TIMEOUT']} 次): 增加超时时间，优化网络连接"

if 'RATE_LIMITED' in error_counts:
    analysis_text += f"\n• 限流异常 ({error_counts['RATE_LIMITED']} 次): 降低请求频率，增加代理池"

if 'CAPTCHA_DETECTED' in error_counts:
    analysis_text += f"\n• 验证码异常 ({error_counts['CAPTCHA_DETECTED']} 次): 集成验证码识别服务"

if 'PARSING_ERROR' in error_counts:
    analysis_text += f"\n• 解析异常 ({error_counts['PARSING_ERROR']} 次): 更新解析规则，增强容错性"

analysis_text += f"""

⚡ **优化措施**
• 实施智能重试机制
• 增加异常处理逻辑
• 监控目标网站变化
• 定期更新爬虫策略
"""

email.add_text(analysis_text.strip())

email.export_html("spider_error_analysis.html")
print("✅ 爬虫异常分析报告已生成：spider_error_analysis.html")
```

--8<-- "examples/assets/spider_reports_html/spider_error_analysis.html"

**异常监控亮点：**
- 异常类型统计分析
- 可视化异常分布
- 智能告警机制
- 针对性解决建议

---

## 采集效率优化

### 爬虫性能分析报告

```python
from email_widget import Email, ProgressWidget, TableWidget
from email_widget.core.enums import TextType, ProgressTheme

# 爬虫性能数据
performance_data = {
    'spider_configs': [
        {'name': '单线程模式', 'threads': 1, 'success_rate': 98.5, 'speed': 50, 'cpu_usage': 15, 'memory_mb': 128},
        {'name': '多线程模式', 'threads': 5, 'success_rate': 95.2, 'speed': 200, 'cpu_usage': 45, 'memory_mb': 512},
        {'name': '异步模式', 'threads': 10, 'success_rate': 92.8, 'speed': 450, 'cpu_usage': 35, 'memory_mb': 256},
        {'name': '分布式模式', 'threads': 20, 'success_rate': 89.1, 'speed': 800, 'cpu_usage': 25, 'memory_mb': 1024}
    ]
}

# 创建性能分析报告
email = Email("爬虫性能优化分析")

email.add_title("⚡ 爬虫性能优化分析", TextType.TITLE_LARGE)

# 性能对比概览
email.add_title("📊 性能配置对比", TextType.SECTION_H2)

perf_table = TableWidget()
perf_table.set_headers(["配置模式", "线程数", "成功率", "采集速度", "CPU使用", "内存使用"])

for config in performance_data['spider_configs']:
    perf_table.add_row([
        config['name'],
        str(config['threads']),
        f"{config['success_rate']:.1f}%",
        f"{config['speed']} 条/分钟",
        f"{config['cpu_usage']}%",
        f"{config['memory_mb']} MB"
    ])

perf_table.set_striped(True)
email.add_widget(perf_table)

# 各配置详细分析
email.add_title("🔍 配置详细分析", TextType.SECTION_H2)

for config in performance_data['spider_configs']:
    email.add_text(f"📋 {config['name']}")
    
    # 成功率进度条
    success_theme = ProgressTheme.SUCCESS if config['success_rate'] > 95 else \
                   ProgressTheme.WARNING if config['success_rate'] > 90 else ProgressTheme.ERROR
    
    # 效率评分 (综合考虑速度和成功率)
    efficiency_score = (config['speed'] / 10) * (config['success_rate'] / 100)
    efficiency_percent = min(efficiency_score, 100)
    
    email.add_progress(config['success_rate'], f"成功率: {config['success_rate']:.1f}%", theme=success_theme)
    email.add_progress(efficiency_percent, f"效率评分: {efficiency_score:.1f}", theme=ProgressTheme.INFO)

# 优化建议
email.add_title("💡 性能优化建议", TextType.SECTION_H2)

# 找出最佳配置
best_config = max(performance_data['spider_configs'], 
                 key=lambda x: (x['speed'] / 10) * (x['success_rate'] / 100))

optimization_text = f"""
**性能优化分析结果：**

🏆 **推荐配置**
• 最佳综合性能: {best_config['name']}
• 采集速度: {best_config['speed']} 条/分钟
• 成功率: {best_config['success_rate']:.1f}%
• 资源消耗: CPU {best_config['cpu_usage']}%, 内存 {best_config['memory_mb']}MB

⚖️ **配置权衡**
• 单线程模式: 高成功率，低资源消耗，适合小规模采集
• 多线程模式: 平衡性能，适合中等规模项目
• 异步模式: 高效率低资源，适合大规模快速采集
• 分布式模式: 超高速度，适合超大规模项目

🎯 **优化建议**
• 根据目标网站特性选择合适的并发模式
• 监控成功率变化，及时调整并发数
• 在速度和稳定性之间找到最佳平衡点
• 考虑网站反爬策略，避免过度激进的配置
"""

email.add_text(optimization_text.strip())

email.export_html("spider_performance_analysis.html")
print("✅ 爬虫性能分析报告已生成：spider_performance_analysis.html")
```

--8<-- "examples/assets/spider_reports_html/spider_performance_analysis.html"

**性能分析特色：**
- 多维度性能对比
- 综合效率评分
- 资源消耗分析
- 配置优化建议

---

## 数据采集总结

### 完整的爬虫项目报告

```python
from email_widget import Email, ColumnWidget, StatusWidget, CardWidget
from email_widget.core.enums import TextType, StatusType

# 创建综合爬虫项目报告
email = Email("爬虫项目综合报告")

email.add_title("🕷️ 爬虫项目综合报告", TextType.TITLE_LARGE)
email.add_text(f"项目周期: 2024年1月15日 - 2024年1月21日")

# 项目整体概况
email.add_title("📊 项目整体概况", TextType.SECTION_H2)

project_summary = [
    ("目标网站", "15个", "🌐"),
    ("总采集量", "125,000条", "📦"),
    ("平均成功率", "94.3%", "✅"),
    ("数据质量率", "92.8%", "🎯")
]

for title, value, icon in project_summary:
    email.add_card(title=title, content=value, icon=icon)

# 关键成果展示
email.add_title("🏆 关键成果", TextType.SECTION_H2)

achievements = f"""
**项目主要成果：**

✅ **采集成果**
• 成功完成15个目标网站的数据采集
• 累计获取有效数据125,000条
• 数据覆盖率达到预期目标的105%

🎯 **质量保证**
• 数据质量率92.8%，超过预期90%
• 重复数据率控制在2.1%以内
• 关键字段完整性达到95%以上

⚡ **技术突破**
• 成功应对5种不同的反爬机制
• 开发了智能重试和降级策略
• 实现了分布式采集架构

📈 **效率提升**
• 相比传统方式，效率提升300%
• 异常处理机制减少人工干预80%
• 自动化程度达到95%
"""

email.add_text(achievements.strip())

# 经验总结
email.add_title("💡 经验总结", TextType.SECTION_H2)

lessons_learned = f"""
**项目经验与教训：**

🎓 **成功经验**
• 充分的前期调研和技术选型
• 完善的监控和告警机制
• 灵活的策略调整和优化

🚧 **遇到的挑战**
• 目标网站频繁更新反爬策略
• 数据结构变化需要及时适配
• 高并发下的资源管理优化

🔄 **持续改进**
• 建立网站变化监控机制
• 完善自动化测试流程
• 优化数据质量检查规则
"""

email.add_text(lessons_learned.strip())

email.export_html("spider_project_summary.html")
print("✅ 爬虫项目综合报告已生成：spider_project_summary.html")
```

--8<-- "examples/assets/spider_reports_html/spider_project_summary.html"

**综合报告价值：**
- 项目全貌展示
- 成果量化统计
- 经验总结归纳
- 决策支持信息

---

## 学习总结

通过爬虫报告示例，您已经掌握了：

### 🎯 专业技能
- **任务监控** - 实时进度跟踪和状态管理
- **质量检查** - 多维度数据质量评估
- **异常分析** - 智能异常识别和处理建议
- **性能优化** - 配置对比和效率分析

### 📊 报告类型
- 爬虫任务进度报告
- 数据质量检查报告
- 异常监控分析报告
- 性能优化分析报告

### 💡 最佳实践
- 实时监控和告警机制
- 数据驱动的优化决策
- 自动化异常检测和处理
- 可视化展示复杂数据关系

### 🚀 应用价值
- 提高爬虫项目管理效率
- 确保数据采集质量
- 及时发现和解决问题
- 为技术优化提供依据

继续学习 [实际应用](real-world.md)，探索更多专业应用场景！ 