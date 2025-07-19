# 实际应用示例

本页面展示 EmailWidget 在真实项目中的完整应用案例，包括电商分析、DevOps监控、数据科学等领域的综合应用。

## 电商数据分析仪表板

### 完整的电商运营报告

```python
import pandas as pd
from datetime import datetime, timedelta
from email_widget import Email
from email_widget.core.enums import TextType, ProgressTheme, AlertType

def create_ecommerce_dashboard():
    """创建电商数据分析仪表板"""
    
    # 模拟电商数据
    ecommerce_data = {
        'overview': {
            'revenue': 12500000,
            'orders': 8547,
            'users': 125000,
            'conversion_rate': 3.2,
            'avg_order_value': 1462
        },
        'products': [
            {'name': '智能手机', 'sales': 3200000, 'units': 1200, 'margin': 22.5},
            {'name': '笔记本电脑', 'sales': 4800000, 'units': 800, 'margin': 18.3},
            {'name': '平板电脑', 'sales': 2100000, 'units': 1050, 'margin': 25.1},
            {'name': '智能手表', 'sales': 1800000, 'units': 1800, 'margin': 35.2},
            {'name': '耳机', 'sales': 600000, 'units': 2000, 'margin': 45.8}
        ],
        'channels': {
            '官网直销': {'revenue': 6250000, 'orders': 3500, 'rate': 50.0},
            '天猫旗舰店': {'revenue': 3750000, 'orders': 2800, 'rate': 30.0},
            '京东店铺': {'revenue': 1875000, 'orders': 1547, 'rate': 15.0},
            '线下门店': {'revenue': 625000, 'orders': 700, 'rate': 5.0}
        }
    }
    
    email = Email("电商运营数据仪表板")
    
    # 报告标题和时间
    email.add_title("🛒 电商运营数据仪表板", TextType.TITLE_LARGE)
    email.add_text(f"报告周期: {(datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')} 至 {datetime.now().strftime('%Y-%m-%d')}")
    
    # 核心指标概览
    email.add_title("📊 核心指标概览", TextType.SECTION_H2)
    
    overview = ecommerce_data['overview']
    metrics = [
        ("总销售额", f"¥{overview['revenue']:,}", "💰"),
        ("订单数量", f"{overview['orders']:,}", "📦"),
        ("活跃用户", f"{overview['users']:,}", "👥"),
        ("转化率", f"{overview['conversion_rate']:.1f}%", "📈"),
        ("客单价", f"¥{overview['avg_order_value']:,}", "💳")
    ]
    
    for title, value, icon in metrics:
        email.add_card(title=title, content=value, icon=icon)
    
    # 产品销售排行
    email.add_title("🏆 产品销售排行", TextType.SECTION_H2)
    
    product_table_data = [["产品名称", "销售额", "销量", "毛利率", "市场表现"]]
    
    for product in ecommerce_data['products']:
        performance = "🔥 热销" if product['sales'] > 3000000 else \
                     "📈 良好" if product['sales'] > 1500000 else "📊 一般"
        
        product_table_data.append([
            product['name'],
            f"¥{product['sales']:,}",
            f"{product['units']:,}台",
            f"{product['margin']:.1f}%",
            performance
        ])
    
    email.add_table_from_data(
        data=product_table_data[1:],
        headers=product_table_data[0],
        title="产品销售明细"
    )
    
    # 销售渠道分析
    email.add_title("🌐 销售渠道分析", TextType.SECTION_H2)
    
    for channel, data in ecommerce_data['channels'].items():
        # 渠道占比进度条
        theme = ProgressTheme.SUCCESS if data['rate'] >= 30 else \
               ProgressTheme.INFO if data['rate'] >= 15 else \
               ProgressTheme.WARNING if data['rate'] >= 10 else ProgressTheme.ERROR
        
        email.add_text(f"🔹 {channel}")
        email.add_progress(
            value=data['rate'],
            label=f"¥{data['revenue']:,} ({data['orders']:,}单)",
            theme=theme
        )
    
    # 运营建议
    email.add_title("💡 运营策略建议", TextType.SECTION_H2)
    
    # 基于数据分析生成建议
    top_product = max(ecommerce_data['products'], key=lambda x: x['sales'])
    high_margin_products = [p for p in ecommerce_data['products'] if p['margin'] > 30]
    
    suggestions = f"""
**基于数据分析的运营建议：**

🎯 **产品策略**
• 重点推广 {top_product['name']}，销售额领先
• 提升高毛利产品推广：{', '.join(p['name'] for p in high_margin_products)}
• 优化低转化产品的营销策略

📈 **渠道优化**
• 加强官网直销渠道建设，占比已达50%
• 增加京东店铺投入，提升市场份额
• 考虑开拓新的销售渠道

💰 **收益提升**
• 当前客单价¥{overview['avg_order_value']:,}",
• 转化率{overview['conversion_rate']:.1f}%有提升空间，优化用户体验
"""
    
    email.add_text(suggestions.strip())
    
    # 风险提醒
    if overview['conversion_rate'] < 3.0:
        email.add_alert(
            "转化率低于3%，建议优化商品页面和购买流程",
            AlertType.WARNING,
            "⚠️ 转化率告警"
        )
    
    return email

# 生成电商仪表板
ecommerce_email = create_ecommerce_dashboard()
ecommerce_email.export_html("ecommerce_dashboard.html")
print("✅ 电商数据仪表板已生成：ecommerce_dashboard.html")
```

--8<-- "examples/assets/real_world_html/ecommerce_dashboard.html"

**电商仪表板特点：**
- 核心业务指标一目了然
- 产品和渠道多维分析
- 数据驱动的策略建议
- 智能风险提醒

---

## DevOps运维监控中心

### 全方位系统监控报告

```python
def create_devops_monitoring():
    """创建DevOps监控中心报告"""
    
    # 模拟监控数据
    monitoring_data = {
        'infrastructure': {
            'servers': [
                {'name': 'Web-01', 'cpu': 45, 'memory': 68, 'disk': 72, 'status': 'healthy'},
                {'name': 'Web-02', 'cpu': 52, 'memory': 71, 'disk': 69, 'status': 'healthy'},
                {'name': 'DB-01', 'cpu': 78, 'memory': 85, 'disk': 91, 'status': 'warning'},
                {'name': 'Cache-01', 'cpu': 35, 'memory': 42, 'disk': 55, 'status': 'healthy'}
            ],
            'services': [
                {'name': 'API Gateway', 'uptime': 99.95, 'response_time': 120, 'requests': 1250000},
                {'name': 'User Service', 'uptime': 99.87, 'response_time': 85, 'requests': 856000},
                {'name': 'Order Service', 'uptime': 98.92, 'response_time': 155, 'requests': 445000},
                {'name': 'Payment Service', 'uptime': 99.99, 'response_time': 95, 'requests': 198000}
            ]
        },
        'deployment': {
            'recent_deploys': [
                {'service': 'User Service', 'version': 'v2.3.1', 'status': 'success', 'time': '2小时前'},
                {'service': 'API Gateway', 'version': 'v1.8.2', 'status': 'success', 'time': '1天前'},
                {'service': 'Order Service', 'version': 'v3.1.0', 'status': 'failed', 'time': '3天前'}
            ]
        }
    }
    
    email = Email("DevOps运维监控中心")
    
    email.add_title("🔧 DevOps运维监控中心", TextType.TITLE_LARGE)
    email.add_text(f"监控时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 基础设施状态
    email.add_title("🖥️ 基础设施状态", TextType.SECTION_H2)
    
    # 服务器状态概览
    servers = monitoring_data['infrastructure']['servers']
    healthy_servers = sum(1 for s in servers if s['status'] == 'healthy')
    warning_servers = sum(1 for s in servers if s['status'] == 'warning')
    
    infra_overview = [
        ("服务器总数", f"{len(servers)}", "🖥️"),
        ("健康状态", f"{healthy_servers}", "✅"),
        ("警告状态", f"{warning_servers}", "⚠️"),
        ("集群可用性", "99.2%", "🎯")
    ]
    
    for title, value, icon in infra_overview:
        email.add_card(title=title, content=value, icon=icon)
    
    # 服务器详细状态
    server_table_data = [["服务器", "CPU使用率", "内存使用率", "磁盘使用率", "状态"]]
    
    for server in servers:
        status_emoji = "🟢" if server['status'] == 'healthy' else \
                      "🟡" if server['status'] == 'warning' else "🔴"
        
        server_table_data.append([
            server['name'],
            f"{server['cpu']}%",
            f"{server['memory']}%",
            f"{server['disk']}%",
            f"{status_emoji} {server['status']}"
        ])
    
    email.add_table_from_data(
        data=server_table_data[1:],
        headers=server_table_data[0],
        title="服务器资源使用详情"
    )
    
    # 应用服务监控
    email.add_title("🚀 应用服务监控", TextType.SECTION_H2)
    
    services = monitoring_data['infrastructure']['services']
    
    for service in services:
        # 服务可用性
        uptime_theme = ProgressTheme.SUCCESS if service['uptime'] >= 99.5 else \
                      ProgressTheme.WARNING if service['uptime'] >= 99.0 else ProgressTheme.ERROR
        
        email.add_text(f"🔹 {service['name']}")
        email.add_progress(
            value=service['uptime'],
            label=f"可用性: {service['uptime']:.2f}% | 响应时间: {service['response_time']}ms",
            theme=uptime_theme
        )
    
    # 部署历史
    email.add_title("📦 最近部署记录", TextType.SECTION_H2)
    
    deploy_table_data = [["服务名称", "版本", "部署状态", "部署时间"]]
    
    for deploy in monitoring_data['deployment']['recent_deploys']:
        status_display = "✅ 成功" if deploy['status'] == 'success' else \
                        "❌ 失败" if deploy['status'] == 'failed' else "🔄 进行中"
        
        deploy_table_data.append([
            deploy['service'],
            deploy['version'],
            status_display,
            deploy['time']
        ])
    
    email.add_table_from_data(
        data=deploy_table_data[1:],
        headers=deploy_table_data[0],
        title="部署记录"
    )
    
    # 告警和建议
    email.add_title("🚨 运维告警", TextType.SECTION_H2)
    
    # 检查需要关注的问题
    alerts = []
    
    for server in servers:
        if server['status'] == 'warning':
            if server['memory'] > 80:
                alerts.append(f"{server['name']} 内存使用率过高({server['memory']}%)")
            if server['disk'] > 90:
                alerts.append(f"{server['name']} 磁盘空间不足({server['disk']}%)")
    
    failed_deploys = [d for d in monitoring_data['deployment']['recent_deploys'] if d['status'] == 'failed']
    if failed_deploys:
        for deploy in failed_deploys:
            alerts.append(f"{deploy['service']} 部署失败，版本 {deploy['version']}")
    
    if alerts:
        for alert in alerts:
            email.add_alert(alert, AlertType.WARNING, "⚠️ 系统告警")
    else:
        email.add_alert("系统运行状态良好，无异常告警", AlertType.TIP, "✅ 系统正常")
    
    return email

# 生成DevOps监控报告
devops_email = create_devops_monitoring()
devops_email.export_html("devops_monitoring.html")
print("✅ DevOps监控报告已生成：devops_monitoring.html")
```

--8<-- "examples/assets/real_world_html/devops_monitoring.html"

**DevOps监控特点：**
- 全栈基础设施监控
- 应用服务健康检查
- 部署流水线跟踪
- 智能告警系统

---

## 数据科学实验报告

### 机器学习模型评估报告

```python
import numpy as np
import matplotlib.pyplot as plt

def create_ml_experiment_report():
    """创建机器学习实验报告"""
    
    # 模拟实验数据
    experiment_data = {
        'model_comparison': [
            {'name': 'Random Forest', 'accuracy': 0.892, 'precision': 0.885, 'recall': 0.898, 'f1': 0.891},
            {'name': 'XGBoost', 'accuracy': 0.907, 'precision': 0.902, 'recall': 0.911, 'f1': 0.906},
            {'name': 'SVM', 'accuracy': 0.875, 'precision': 0.871, 'recall': 0.879, 'f1': 0.875},
            {'name': 'Neural Network', 'accuracy': 0.923, 'precision': 0.919, 'recall': 0.927, 'f1': 0.923}
        ],
        'feature_importance': [
            {'feature': '用户年龄', 'importance': 0.23},
            {'feature': '购买历史', 'importance': 0.19},
            {'feature': '浏览时长', 'importance': 0.15},
            {'feature': '设备类型', 'importance': 0.12},
            {'feature': '地理位置', 'importance': 0.10}
        ],
        'training_metrics': {
            'dataset_size': 125000,
            'training_time': 45.2,
            'validation_split': 0.2,
            'cross_validation_folds': 5
        }
    }
    
    email = Email("机器学习实验报告")
    
    email.add_title("🧠 机器学习实验报告", TextType.TITLE_LARGE)
    email.add_text("实验目标: 用户购买意向预测模型")
    email.add_text(f"实验时间: {datetime.now().strftime('%Y-%m-%d')}")
    
    # 实验概览
    email.add_title("📊 实验概览", TextType.SECTION_H2)
    
    metrics = experiment_data['training_metrics']
    exp_overview = [
        ("数据集大小", f"{metrics['dataset_size']:,条", "📊"),
        ("训练时间", f"{metrics['training_time']:.1f}分钟", "⏱️"),
        ("验证集比例", f"{metrics['validation_split']*100:.0f}%", "✂️"),
        ("交叉验证", f"{metrics['cross_validation_folds']}折", "🔄")
    ]
    
    for title, value, icon in exp_overview:
        email.add_card(title=title, content=value, icon=icon)
    
    # 模型性能对比
    email.add_title("🏆 模型性能对比", TextType.SECTION_H2)
    
    model_table_data = [["模型", "准确率", "精确率", "召回率", "F1分数", "综合评价"]]
    
    for model in experiment_data['model_comparison']:
        # 计算综合评价
        avg_score = (model['accuracy'] + model['precision'] + model['recall'] + model['f1']) / 4
        rating = "🌟🌟🌟🌟🌟" if avg_score >= 0.92 else \
                "🌟🌟🌟🌟" if avg_score >= 0.90 else \
                "🌟🌟🌟" if avg_score >= 0.88 else "🌟🌟"
        
        model_table_data.append([
            model['name'],
            f"{model['accuracy']:.3f}",
            f"{model['precision']:.3f}",
            f"{model['recall']:.3f}",
            f"{model['f1']:.3f}",
            rating
        ])
    
    email.add_table_from_data(
        data=model_table_data[1:],
        headers=model_table_data[0],
        title="模型性能指标对比"
    )
    
    # 特征重要性分析
    email.add_title("🔍 特征重要性分析", TextType.SECTION_H2)
    
    # 创建特征重要性图表
    features = [f['feature'] for f in experiment_data['feature_importance']]
    importance = [f['importance'] for f in experiment_data['feature_importance']]
    
    plt.figure(figsize=(10, 6))
    bars = plt.barh(features, importance, color=['#3498db', '#2ecc71', '#f39c12', '#e74c3c', '#9b59b6'])
    plt.title('特征重要性排序', fontsize=14)
    plt.xlabel('重要性分数')
    
    # 添加数值标签
    for bar, imp in zip(bars, importance):
        plt.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2, 
                f'{imp:.2f}', ha='left', va='center')
    
    plt.tight_layout()
    feature_chart_path = "feature_importance.png"
    plt.savefig(feature_chart_path, dpi=150, bbox_inches='tight')
    plt.close()
    
    # 添加图表到邮件
    email.add_chart(
        chart_path=feature_chart_path,
        title="特征重要性分布",
        description="显示各特征对模型预测结果的影响程度"
    )
    
    # 实验结论
    email.add_title("📝 实验结论", TextType.SECTION_H2)
    
    best_model = max(experiment_data['model_comparison'], key=lambda x: x['f1'])
    top_feature = experiment_data['feature_importance'][0]
    
    conclusions = f"""
**实验结论与建议：**

🏆 **最优模型**
• {best_model['name']} 表现最佳，F1分数达到 {best_model['f1']:.3f}
• 建议作为生产环境的主要模型

🔍 **关键发现**
• {top_feature['feature']} 是最重要的预测特征 (重要性: {top_feature['importance']:.2f})
• 模型整体性能稳定，各指标均衡
• 交叉验证结果一致，模型泛化能力强

🚀 **后续工作**
• 进行超参数优化，进一步提升性能
• 收集更多样本数据，特别是边缘案例
• 开发模型解释性工具，提高业务可理解性
• 建立A/B测试框架，验证线上效果
"""
    
    email.add_text(conclusions.strip())
    
    # 模型部署建议
    if best_model['accuracy'] > 0.9:
        email.add_alert(
            f"{best_model['name']} 模型性能优秀，建议部署到生产环境",
            AlertType.TIP,
            "✅ 部署建议"
        )
    else:
        email.add_alert(
            "模型性能有待提升，建议进一步优化后再部署",
            AlertType.WARNING,
            "⚠️ 性能提醒"
        )
    
    return email

# 生成机器学习实验报告
ml_email = create_ml_experiment_report()
ml_email.export_html("ml_experiment_report.html")
print("✅ 机器学习实验报告已生成：ml_experiment_report.html")
```

--8<-- "examples/assets/real_world_html/ml_experiment_report.html"

**数据科学报告特点：**
- 全面的模型评估指标
- 可视化特征重要性
- 科学的实验记录
- 可操作的结论建议

---

## 项目管理看板

### 敏捷开发进度跟踪

```python
def create_project_management_dashboard():
    """创建项目管理看板"""
    
    # 项目数据
    project_data = {
        'project_info': {
            'name': 'EmailWidget v2.0',
            'start_date': '2024-01-01',
            'target_date': '2024-03-31',
            'team_size': 8,
            'current_sprint': 'Sprint 6'
        },
        'sprint_progress': {
            'total_story_points': 120,
            'completed_points': 95,
            'in_progress_points': 15,
            'remaining_points': 10
        },
        'tasks': [
            {'title': '用户认证系统', 'status': 'completed', 'assignee': '张三', 'points': 13},
            {'title': '数据可视化组件', 'status': 'in_progress', 'assignee': '李四', 'points': 8},
            {'title': '移动端适配', 'status': 'in_progress', 'assignee': '王五', 'points': 5},
            {'title': '性能优化', 'status': 'todo', 'assignee': '赵六', 'points': 8},
            {'title': '文档更新', 'status': 'todo', 'assignee': '孙七', 'points': 2}
        ],
        'quality_metrics': {
            'code_coverage': 87.5,
            'bugs_open': 12,
            'bugs_resolved': 45,
            'tech_debt_hours': 24
        }
    }
    
    email = Email("项目管理看板")
    
    email.add_title("📋 项目管理看板", TextType.TITLE_LARGE)
    
    # 项目概览
    project_info = project_data['project_info']
    email.add_text(f"项目名称: {project_info['name']}")
    email.add_text(f"当前迭代: {project_info['current_sprint']}")
    
    project_overview = [
        ("团队规模", f"{project_info['team_size']}人", "👥"),
        ("开始时间", project_info['start_date'], "📅"),
        ("目标时间", project_info['target_date'], "🎯"),
        ("当前迭代", project_info['current_sprint'], "🔄")
    ]
    
    for title, value, icon in project_overview:
        email.add_card(title=title, content=value, icon=icon)
    
    # Sprint进度
    email.add_title("🚀 Sprint 进度", TextType.SECTION_H2)
    
    sprint = project_data['sprint_progress']
    completed_rate = (sprint['completed_points'] / sprint['total_story_points']) * 100
    
    email.add_progress(
        value=completed_rate,
        label=f"已完成: {sprint['completed_points']}/{sprint['total_story_points']} 故事点 ({completed_rate:.1f}%)",
        theme=ProgressTheme.SUCCESS if completed_rate > 80 else ProgressTheme.INFO
    )
    
    # 任务状态分布
    email.add_title("📊 任务状态分布", TextType.SECTION_H2)
    
    tasks = project_data['tasks']
    status_counts = {
        'completed': len([t for t in tasks if t['status'] == 'completed']),
        'in_progress': len([t for t in tasks if t['status'] == 'in_progress']),
        'todo': len([t for t in tasks if t['status'] == 'todo'])
    }
    
    total_tasks = len(tasks)
    
    for status, count in status_counts.items():
        status_name = {'completed': '已完成', 'in_progress': '进行中', 'todo': '待开始'}[status]
        status_theme = {'completed': ProgressTheme.SUCCESS, 'in_progress': ProgressTheme.INFO, 'todo': ProgressTheme.WARNING}[status]
        percentage = (count / total_tasks) * 100
        
        email.add_text(f"🔹 {status_name}")
        email.add_progress(percentage, f"{count} 个任务 ({percentage:.1f}%)", theme=status_theme)
    
    # 任务详情
    email.add_title("📋 任务详情", TextType.SECTION_H2)
    
    task_table_data = [["任务名称", "状态", "负责人", "故事点", "进度"]]
    
    for task in tasks:
        status_emoji = {"completed": "✅", "in_progress": "🔄", "todo": "⏳"}[task['status']]
        status_text = {"completed": "已完成", "in_progress": "进行中", "todo": "待开始"}[task['status']]
        
        task_table_data.append([
            task['title'],
            f"{status_emoji} {status_text}",
            task['assignee'],
            str(task['points']),
            "100%" if task['status'] == 'completed' else "50%" if task['status'] == 'in_progress' else "0%"
        ])
    
    email.add_table_from_data(
        data=task_table_data[1:],
        headers=task_table_data[0],
        title="任务分配和进度"
    )
    
    # 质量指标
    email.add_title("🔍 质量指标", TextType.SECTION_H2)
    
    quality = project_data['quality_metrics']
    
    quality_overview = [
        ("代码覆盖率", f"{quality['code_coverage']:.1f}%", "📊"),
        ("待修复Bug", f"{quality['bugs_open']}", "🐛"),
        ("已修复Bug", f"{quality['bugs_resolved']}", "✅"),
        ("技术债务", f"{quality['tech_debt_hours']}小时", "⚠️")
    ]
    
    for title, value, icon in quality_overview:
        email.add_card(title=title, content=value, icon=icon)
    
    # 项目风险和建议
    email.add_title("💡 项目状态评估", TextType.SECTION_H2)
    
    # 基于数据生成评估
    risks = []
    if completed_rate < 70:
        risks.append("Sprint进度滞后，可能影响交付时间")
    if quality['code_coverage'] < 80:
        risks.append("代码覆盖率偏低，需要加强测试")
    if quality['bugs_open'] > 15:
        risks.append("待修复Bug较多，影响产品质量")
    
    if risks:
        for risk in risks:
            email.add_alert(risk, AlertType.WARNING, "⚠️ 项目风险")
    else:
        email.add_alert("项目进展顺利，各项指标正常", AlertType.TIP, "✅ 项目状态良好")
    
    return email

# 生成项目管理看板
pm_email = create_project_management_dashboard()
pm_email.export_html("project_management_dashboard.html")
print("✅ 项目管理看板已生成：project_management_dashboard.html")
```

--8<-- "examples/assets/real_world_html/project_management_dashboard.html"

**项目管理特点：**
- 敏捷开发进度跟踪
- 团队任务分配管理
- 质量指标监控
- 风险识别和预警

---

## 学习总结

通过这些实际应用示例，您已经看到了：

### 🌟 应用领域
- **电商运营** - 数据驱动的商业决策
- **DevOps运维** - 全栈系统监控
- **数据科学** - 机器学习实验管理
- **项目管理** - 敏捷开发跟踪

### 🎯 核心价值
- 将复杂数据转化为直观报告
- 支持多领域的专业应用
- 提供决策支持和洞察
- 自动化报告生成流程

### 💡 设计理念
- 数据驱动的可视化
- 业务导向的信息展示
- 智能化的分析和建议
- 响应式的交互体验

### 🚀 扩展方向
- 集成更多数据源
- 开发行业专用模板
- 增强实时监控能力
- 构建报告分发系统

这些实际应用案例展示了 EmailWidget 在真实业务场景中的强大能力。您可以根据自己的业务需求，参考这些示例创建专业的数据报告系统！ 