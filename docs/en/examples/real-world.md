# Real-world Application Examples

This page showcases complete application cases of EmailWidget in real projects, including comprehensive applications in e-commerce analysis, DevOps monitoring, data science, and other fields.

## E-commerce Data Analysis Dashboard

### Complete E-commerce Operations Report

```python
import pandas as pd
from datetime import datetime, timedelta
from email_widget import Email
from email_widget.core.enums import TextType, ProgressTheme, AlertType

def create_ecommerce_dashboard():
    """Create e-commerce data analysis dashboard"""
    
    # Simulate e-commerce data
    ecommerce_data = {
        'overview': {
            'revenue': 12500000,
            'orders': 8547,
            'users': 125000,
            'conversion_rate': 3.2,
            'avg_order_value': 1462
        },
        'products': [
            {'name': 'Smartphone', 'sales': 3200000, 'units': 1200, 'margin': 22.5},
            {'name': 'Laptop', 'sales': 4800000, 'units': 800, 'margin': 18.3},
            {'name': 'Tablet', 'sales': 2100000, 'units': 1050, 'margin': 25.1},
            {'name': 'Smart Watch', 'sales': 1800000, 'units': 1800, 'margin': 35.2},
            {'name': 'Headphones', 'sales': 600000, 'units': 2000, 'margin': 45.8}
        ],
        'channels': {
            'Official Website': {'revenue': 6250000, 'orders': 3500, 'rate': 50.0},
            'Tmall Store': {'revenue': 3750000, 'orders': 2800, 'rate': 30.0},
            'JD Store': {'revenue': 1875000, 'orders': 1547, 'rate': 15.0},
            'Offline Stores': {'revenue': 625000, 'orders': 700, 'rate': 5.0}
        }
    }
    
    email = Email("E-commerce Operations Data Dashboard")
    
    # Report title and time
    email.add_title("🛒 E-commerce Operations Data Dashboard", TextType.TITLE_LARGE)
    email.add_text(f"Report Period: {(datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')} to {datetime.now().strftime('%Y-%m-%d')}")
    
    # Core metrics overview
    email.add_title("📊 Core Metrics Overview", TextType.SECTION_H2)
    
    overview = ecommerce_data['overview']
    metrics = [
        ("Total Revenue", f"${overview['revenue']:,}", "💰"),
        ("Orders", f"{overview['orders']:,}", "📦"),
        ("Active Users", f"{overview['users']:,}", "👥"),
        ("Conversion Rate", f"{overview['conversion_rate']:.1f}%", "📈"),
        ("AOV", f"${overview['avg_order_value']:,}", "💳")
    ]
    
    for title, value, icon in metrics:
        email.add_card(title=title, content=value, icon=icon)
    
    # Product sales ranking
    email.add_title("🏆 Product Sales Ranking", TextType.SECTION_H2)
    
    product_table_data = [["Product Name", "Revenue", "Units Sold", "Margin", "Performance"]]
    
    for product in ecommerce_data['products']:
        performance = "🔥 Hot" if product['sales'] > 3000000 else \
                     "📈 Good" if product['sales'] > 1500000 else "📊 Average"
        
        product_table_data.append([
            product['name'],
            f"${product['sales']:,}",
            f"{product['units']:,} units",
            f"{product['margin']:.1f}%",
            performance
        ])
    
    email.add_table_from_data(
        data=product_table_data[1:],
        headers=product_table_data[0],
        title="Product Sales Details"
    )
    
    # Sales channel analysis
    email.add_title("🌐 Sales Channel Analysis", TextType.SECTION_H2)
    
    for channel, data in ecommerce_data['channels'].items():
        # Channel percentage progress bar
        theme = ProgressTheme.SUCCESS if data['rate'] >= 30 else \
               ProgressTheme.INFO if data['rate'] >= 15 else \
               ProgressTheme.WARNING if data['rate'] >= 10 else ProgressTheme.ERROR
        
        email.add_text(f"🔹 {channel}")
        email.add_progress(
            value=data['rate'],
            label=f"${data['revenue']:,} ({data['orders']:,} orders)",
            theme=theme
        )
    
    # Operations recommendations
    email.add_title("💡 Operations Strategy Recommendations", TextType.SECTION_H2)
    
    # Generate recommendations based on data analysis
    top_product = max(ecommerce_data['products'], key=lambda x: x['sales'])
    high_margin_products = [p for p in ecommerce_data['products'] if p['margin'] > 30]
    
    suggestions = f"""
**Operations Recommendations Based on Data Analysis:**

🎯 **Product Strategy**
• Focus on promoting {top_product['name']}, leading in sales revenue
• Enhance promotion of high-margin products: {', '.join(p['name'] for p in high_margin_products)}
• Optimize marketing strategies for low-conversion products

📈 **Channel Optimization**
• Strengthen official website direct sales channel, already reaching 50%
• Increase investment in JD store to boost market share
• Consider developing new sales channels

💰 **Revenue Enhancement**
• Current AOV is ${overview['avg_order_value']:,}
• Conversion rate of {overview['conversion_rate']:.1f}% has room for improvement, optimize user experience
"""
    
    email.add_text(suggestions.strip())
    
    # Risk alerts
    if overview['conversion_rate'] < 3.0:
        email.add_alert(
            "Conversion rate below 3%, recommend optimizing product pages and purchase flow",
            AlertType.WARNING,
            "⚠️ Conversion Rate Alert"
        )
    
    return email

# Generate e-commerce dashboard
ecommerce_email = create_ecommerce_dashboard()
ecommerce_email.export_html("ecommerce_dashboard.html")
print("✅ E-commerce data dashboard generated: ecommerce_dashboard.html")
```

--8<-- "examples/assets/real_world_html/ecommerce_dashboard.html"

**E-commerce Dashboard Features:**
- Core business metrics at a glance
- Multi-dimensional product and channel analysis
- Data-driven strategy recommendations
- Intelligent risk alerts

---

## DevOps Operations Monitoring Center

### Comprehensive System Monitoring Report

```python
def create_devops_monitoring():
    """Create DevOps monitoring center report"""
    
    # Simulate monitoring data
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
                {'service': 'User Service', 'version': 'v2.3.1', 'status': 'success', 'time': '2 hours ago'},
                {'service': 'API Gateway', 'version': 'v1.8.2', 'status': 'success', 'time': '1 day ago'},
                {'service': 'Order Service', 'version': 'v3.1.0', 'status': 'failed', 'time': '3 days ago'}
            ]
        }
    }
    
    email = Email("DevOps Operations Monitoring Center")
    
    email.add_title("🔧 DevOps Operations Monitoring Center", TextType.TITLE_LARGE)
    email.add_text(f"Monitoring Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Infrastructure status
    email.add_title("🖥️ Infrastructure Status", TextType.SECTION_H2)
    
    # Server status overview
    servers = monitoring_data['infrastructure']['servers']
    healthy_servers = sum(1 for s in servers if s['status'] == 'healthy')
    warning_servers = sum(1 for s in servers if s['status'] == 'warning')
    
    infra_overview = [
        ("Total Servers", f"{len(servers)}", "🖥️"),
        ("Healthy", f"{healthy_servers}", "✅"),
        ("Warning", f"{warning_servers}", "⚠️"),
        ("Cluster Availability", "99.2%", "🎯")
    ]
    
    for title, value, icon in infra_overview:
        email.add_card(title=title, content=value, icon=icon)
    
    # Detailed server status
    server_table_data = [["Server", "CPU Usage", "Memory Usage", "Disk Usage", "Status"]]
    
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
        title="Server Resource Usage Details"
    )
    
    # Application service monitoring
    email.add_title("🚀 Application Service Monitoring", TextType.SECTION_H2)
    
    services = monitoring_data['infrastructure']['services']
    
    for service in services:
        # Service availability
        uptime_theme = ProgressTheme.SUCCESS if service['uptime'] >= 99.5 else \
                      ProgressTheme.WARNING if service['uptime'] >= 99.0 else ProgressTheme.ERROR
        
        email.add_text(f"🔹 {service['name']}")
        email.add_progress(
            value=service['uptime'],
            label=f"Uptime: {service['uptime']:.2f}% | Response Time: {service['response_time']}ms",
            theme=uptime_theme
        )
    
    # Deployment history
    email.add_title("📦 Recent Deployment Records", TextType.SECTION_H2)
    
    deploy_table_data = [["Service Name", "Version", "Deploy Status", "Deploy Time"]]
    
    for deploy in monitoring_data['deployment']['recent_deploys']:
        status_display = "✅ Success" if deploy['status'] == 'success' else \
                        "❌ Failed" if deploy['status'] == 'failed' else "🔄 In Progress"
        
        deploy_table_data.append([
            deploy['service'],
            deploy['version'],
            status_display,
            deploy['time']
        ])
    
    email.add_table_from_data(
        data=deploy_table_data[1:],
        headers=deploy_table_data[0],
        title="Deployment Records"
    )
    
    # Alerts and recommendations
    email.add_title("🚨 Operations Alerts", TextType.SECTION_H2)
    
    # Check issues that need attention
    alerts = []
    
    for server in servers:
        if server['status'] == 'warning':
            if server['memory'] > 80:
                alerts.append(f"{server['name']} memory usage too high ({server['memory']}%)")
            if server['disk'] > 90:
                alerts.append(f"{server['name']} disk space insufficient ({server['disk']}%)")
    
    failed_deploys = [d for d in monitoring_data['deployment']['recent_deploys'] if d['status'] == 'failed']
    if failed_deploys:
        for deploy in failed_deploys:
            alerts.append(f"{deploy['service']} deployment failed, version {deploy['version']}")
    
    if alerts:
        for alert in alerts:
            email.add_alert(alert, AlertType.WARNING, "⚠️ System Alert")
    else:
        email.add_alert("System running in good condition, no abnormal alerts", AlertType.TIP, "✅ System Normal")
    
    return email

# Generate DevOps monitoring report
devops_email = create_devops_monitoring()
devops_email.export_html("devops_monitoring.html")
print("✅ DevOps monitoring report generated: devops_monitoring.html")
```

--8<-- "examples/assets/real_world_html/devops_monitoring.html"

**DevOps Monitoring Features:**
- Full-stack infrastructure monitoring
- Application service health checks
- Deployment pipeline tracking
- Intelligent alert system

---

## Data Science Experiment Report

### Machine Learning Model Evaluation Report

```python
import numpy as np
import matplotlib.pyplot as plt

def create_ml_experiment_report():
    """Create machine learning experiment report"""
    
    # Simulate experiment data
    experiment_data = {
        'model_comparison': [
            {'name': 'Random Forest', 'accuracy': 0.892, 'precision': 0.885, 'recall': 0.898, 'f1': 0.891},
            {'name': 'XGBoost', 'accuracy': 0.907, 'precision': 0.902, 'recall': 0.911, 'f1': 0.906},
            {'name': 'SVM', 'accuracy': 0.875, 'precision': 0.871, 'recall': 0.879, 'f1': 0.875},
            {'name': 'Neural Network', 'accuracy': 0.923, 'precision': 0.919, 'recall': 0.927, 'f1': 0.923}
        ],
        'feature_importance': [
            {'feature': 'User Age', 'importance': 0.23},
            {'feature': 'Purchase History', 'importance': 0.19},
            {'feature': 'Browse Duration', 'importance': 0.15},
            {'feature': 'Device Type', 'importance': 0.12},
            {'feature': 'Geographic Location', 'importance': 0.10}
        ],
        'training_metrics': {
            'dataset_size': 125000,
            'training_time': 45.2,
            'validation_split': 0.2,
            'cross_validation_folds': 5
        }
    }
    
    email = Email("Machine Learning Experiment Report")
    
    email.add_title("🧠 Machine Learning Experiment Report", TextType.TITLE_LARGE)
    email.add_text("Experiment Goal: User Purchase Intent Prediction Model")
    email.add_text(f"Experiment Date: {datetime.now().strftime('%Y-%m-%d')}")
    
    # Experiment overview
    email.add_title("📊 Experiment Overview", TextType.SECTION_H2)
    
    metrics = experiment_data['training_metrics']
    exp_overview = [
        ("Dataset Size", f"{metrics['dataset_size']:,} records", "📊"),
        ("Training Time", f"{metrics['training_time']:.1f} minutes", "⏱️"),
        ("Validation Split", f"{metrics['validation_split']*100:.0f}%", "✂️"),
        ("Cross Validation", f"{metrics['cross_validation_folds']} folds", "🔄")
    ]
    
    for title, value, icon in exp_overview:
        email.add_card(title=title, content=value, icon=icon)
    
    # Model performance comparison
    email.add_title("🏆 Model Performance Comparison", TextType.SECTION_H2)
    
    model_table_data = [["Model", "Accuracy", "Precision", "Recall", "F1 Score", "Overall Rating"]]
    
    for model in experiment_data['model_comparison']:
        # Calculate overall rating
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
        title="Model Performance Metrics Comparison"
    )
    
    # Feature importance analysis
    email.add_title("🔍 Feature Importance Analysis", TextType.SECTION_H2)
    
    # Create feature importance chart
    features = [f['feature'] for f in experiment_data['feature_importance']]
    importance = [f['importance'] for f in experiment_data['feature_importance']]
    
    plt.figure(figsize=(10, 6))
    bars = plt.barh(features, importance, color=['#3498db', '#2ecc71', '#f39c12', '#e74c3c', '#9b59b6'])
    plt.title('Feature Importance Ranking', fontsize=14)
    plt.xlabel('Importance Score')
    
    # Add value labels
    for bar, imp in zip(bars, importance):
        plt.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2, 
                f'{imp:.2f}', ha='left', va='center')
    
    plt.tight_layout()
    feature_chart_path = "feature_importance.png"
    plt.savefig(feature_chart_path, dpi=150, bbox_inches='tight')
    plt.close()
    
    # Add chart to email
    email.add_chart(
        chart_path=feature_chart_path,
        title="Feature Importance Distribution",
        description="Shows the impact of each feature on model prediction results"
    )
    
    # Experiment conclusions
    email.add_title("📝 Experiment Conclusions", TextType.SECTION_H2)
    
    best_model = max(experiment_data['model_comparison'], key=lambda x: x['f1'])
    top_feature = experiment_data['feature_importance'][0]
    
    conclusions = f"""
**Experiment Conclusions and Recommendations:**

🏆 **Best Model**
• {best_model['name']} performed best with F1 score of {best_model['f1']:.3f}
• Recommended as the primary model for production environment

🔍 **Key Findings**
• {top_feature['feature']} is the most important predictive feature (importance: {top_feature['importance']:.2f})
• Overall model performance is stable with balanced metrics
• Cross-validation results are consistent, model has strong generalization ability

🚀 **Future Work**
• Perform hyperparameter optimization to further improve performance
• Collect more diverse sample data, especially edge cases
• Develop model interpretability tools to improve business understanding
• Establish A/B testing framework to validate online effectiveness
"""
    
    email.add_text(conclusions.strip())
    
    # Model deployment recommendations
    if best_model['accuracy'] > 0.9:
        email.add_alert(
            f"{best_model['name']} model performance excellent, recommend deploying to production",
            AlertType.TIP,
            "✅ Deployment Recommendation"
        )
    else:
        email.add_alert(
            "Model performance needs improvement, recommend further optimization before deployment",
            AlertType.WARNING,
            "⚠️ Performance Reminder"
        )
    
    return email

# Generate machine learning experiment report
ml_email = create_ml_experiment_report()
ml_email.export_html("ml_experiment_report.html")
print("✅ Machine learning experiment report generated: ml_experiment_report.html")
```

--8<-- "examples/assets/real_world_html/ml_experiment_report.html"

**Data Science Report Features:**
- Comprehensive model evaluation metrics
- Visual feature importance
- Scientific experiment records
- Actionable conclusion recommendations

---

## Project Management Dashboard

### Agile Development Progress Tracking

```python
def create_project_management_dashboard():
    """Create project management dashboard"""
    
    # Project data
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
            {'title': 'User Authentication System', 'status': 'completed', 'assignee': 'John Smith', 'points': 13},
            {'title': 'Data Visualization Components', 'status': 'in_progress', 'assignee': 'Jane Doe', 'points': 8},
            {'title': 'Mobile Adaptation', 'status': 'in_progress', 'assignee': 'Bob Wilson', 'points': 5},
            {'title': 'Performance Optimization', 'status': 'todo', 'assignee': 'Alice Brown', 'points': 8},
            {'title': 'Documentation Update', 'status': 'todo', 'assignee': 'Charlie Davis', 'points': 2}
        ],
        'quality_metrics': {
            'code_coverage': 87.5,
            'bugs_open': 12,
            'bugs_resolved': 45,
            'tech_debt_hours': 24
        }
    }
    
    email = Email("Project Management Dashboard")
    
    email.add_title("📋 Project Management Dashboard", TextType.TITLE_LARGE)
    
    # Project overview
    project_info = project_data['project_info']
    email.add_text(f"Project Name: {project_info['name']}")
    email.add_text(f"Current Sprint: {project_info['current_sprint']}")
    
    project_overview = [
        ("Team Size", f"{project_info['team_size']} members", "👥"),
        ("Start Date", project_info['start_date'], "📅"),
        ("Target Date", project_info['target_date'], "🎯"),
        ("Current Sprint", project_info['current_sprint'], "🔄")
    ]
    
    for title, value, icon in project_overview:
        email.add_card(title=title, content=value, icon=icon)
    
    # Sprint progress
    email.add_title("🚀 Sprint Progress", TextType.SECTION_H2)
    
    sprint = project_data['sprint_progress']
    completed_rate = (sprint['completed_points'] / sprint['total_story_points']) * 100
    
    email.add_progress(
        value=completed_rate,
        label=f"Completed: {sprint['completed_points']}/{sprint['total_story_points']} story points ({completed_rate:.1f}%)",
        theme=ProgressTheme.SUCCESS if completed_rate > 80 else ProgressTheme.INFO
    )
    
    # Task status distribution
    email.add_title("📊 Task Status Distribution", TextType.SECTION_H2)
    
    tasks = project_data['tasks']
    status_counts = {
        'completed': len([t for t in tasks if t['status'] == 'completed']),
        'in_progress': len([t for t in tasks if t['status'] == 'in_progress']),
        'todo': len([t for t in tasks if t['status'] == 'todo'])
    }
    
    total_tasks = len(tasks)
    
    for status, count in status_counts.items():
        status_name = {'completed': 'Completed', 'in_progress': 'In Progress', 'todo': 'To Do'}[status]
        status_theme = {'completed': ProgressTheme.SUCCESS, 'in_progress': ProgressTheme.INFO, 'todo': ProgressTheme.WARNING}[status]
        percentage = (count / total_tasks) * 100
        
        email.add_text(f"🔹 {status_name}")
        email.add_progress(percentage, f"{count} tasks ({percentage:.1f}%)", theme=status_theme)
    
    # Task details
    email.add_title("📋 Task Details", TextType.SECTION_H2)
    
    task_table_data = [["Task Name", "Status", "Assignee", "Story Points", "Progress"]]
    
    for task in tasks:
        status_emoji = {"completed": "✅", "in_progress": "🔄", "todo": "⏳"}[task['status']]
        status_text = {"completed": "Completed", "in_progress": "In Progress", "todo": "To Do"}[task['status']]
        
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
        title="Task Assignment and Progress"
    )
    
    # Quality metrics
    email.add_title("🔍 Quality Metrics", TextType.SECTION_H2)
    
    quality = project_data['quality_metrics']
    
    quality_overview = [
        ("Code Coverage", f"{quality['code_coverage']:.1f}%", "📊"),
        ("Open Bugs", f"{quality['bugs_open']}", "🐛"),
        ("Resolved Bugs", f"{quality['bugs_resolved']}", "✅"),
        ("Tech Debt", f"{quality['tech_debt_hours']} hours", "⚠️")
    ]
    
    for title, value, icon in quality_overview:
        email.add_card(title=title, content=value, icon=icon)
    
    # Project risks and recommendations
    email.add_title("💡 Project Status Assessment", TextType.SECTION_H2)
    
    # Generate assessment based on data
    risks = []
    if completed_rate < 70:
        risks.append("Sprint progress behind schedule, may affect delivery timeline")
    if quality['code_coverage'] < 80:
        risks.append("Code coverage low, need to strengthen testing")
    if quality['bugs_open'] > 15:
        risks.append("Too many open bugs, affecting product quality")
    
    if risks:
        for risk in risks:
            email.add_alert(risk, AlertType.WARNING, "⚠️ Project Risk")
    else:
        email.add_alert("Project progressing smoothly, all metrics normal", AlertType.TIP, "✅ Project Status Good")
    
    return email

# Generate project management dashboard
pm_email = create_project_management_dashboard()
pm_email.export_html("project_management_dashboard.html")
print("✅ Project management dashboard generated: project_management_dashboard.html")
```

--8<-- "examples/assets/real_world_html/project_management_dashboard.html"

**Project Management Features:**
- Agile development progress tracking
- Team task assignment management
- Quality metrics monitoring
- Risk identification and alerts

---

## Learning Summary

Through these real-world application examples, you have seen:

### 🌟 Application Domains
- **E-commerce Operations** - Data-driven business decisions
- **DevOps Operations** - Full-stack system monitoring
- **Data Science** - Machine learning experiment management
- **Project Management** - Agile development tracking

### 🎯 Core Value
- Transform complex data into intuitive reports
- Support professional applications across multiple domains
- Provide decision support and insights
- Automate report generation processes

### 💡 Design Philosophy
- Data-driven visualization
- Business-oriented information display
- Intelligent analysis and recommendations
- Responsive interactive experience

### 🚀 Extension Directions
- Integrate more data sources
- Develop industry-specific templates
- Enhance real-time monitoring capabilities
- Build report distribution systems

These real-world application cases demonstrate the powerful capabilities of EmailWidget in real business scenarios. You can create professional data reporting systems based on these examples according to your business needs!