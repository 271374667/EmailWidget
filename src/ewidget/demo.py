"""EWidget演示文件

展示所有可用的Widget组件和使用方法
"""
import pandas as pd
from datetime import datetime

from src.ewidget import (
    Email, 
    TableWidget, TableCell,
    ImageWidget,
    LogWidget, LogEntry,
    AlertWidget,
    TextWidget,
    ProgressWidget,
    CircularProgressWidget,
    CardWidget,
    StatusWidget,
    QuoteWidget,
    ColumnWidget,
    ChartWidget,
    LogLevel, StatusType, AlertType, TextAlign, ProgressTheme, LayoutType
)

def create_demo_email():
    """创建演示邮件"""
    
    # 创建邮件主体
    email = Email("EWidget 组件演示")
    
    # 1. 标题文本
    title_text = TextWidget()
    title_text.set_content("EWidget 组件库完整演示").set_font_size("24px").set_align(TextAlign.CENTER).set_bold(True)
    email.add_widget(title_text)
    
    # 2. 介绍文本
    intro_text = TextWidget()
    intro_text.set_content(
        "这是一个完整的EWidget组件演示，展示了所有可用的组件类型。\n"
        "EWidget是一个面向对象的邮件HTML组件库，采用Fluent Design风格。"
    ).set_font_size("16px").set_color("#605e5c")
    email.add_widget(intro_text)
    
    # 3. 警告框演示
    note_alert = AlertWidget()
    note_alert.set_content("这是一个信息提示框，用于显示重要的提示信息。").set_alert_type(AlertType.NOTE)
    email.add_widget(note_alert)
    
    warning_alert = AlertWidget()
    warning_alert.set_content("这是一个警告提示框，用于显示需要注意的警告信息。").set_alert_type(AlertType.WARNING)
    email.add_widget(warning_alert)
    
    # 4. 表格演示
    table_widget = TableWidget()
    table_widget.set_title("爬虫任务执行结果")
    
    # 创建示例数据
    df = pd.DataFrame({
        "任务名称": ["网站A数据采集", "网站B内容抓取", "API数据同步", "图片下载任务"],
        "执行状态": [
            {"text": "成功", "status": "success"},
            {"text": "失败", "status": "error"}, 
            {"text": "运行中", "status": "info"},
            {"text": "等待中", "status": "warning"}
        ],
        "执行时间": ["2024-01-15 10:30:00", "2024-01-15 10:32:15", "2024-01-15 10:35:00", "2024-01-15 10:40:00"],
        "耗时(秒)": ["12.5", "8.2", "45.1", "0.0"]
    })
    table_widget.set_dataframe(df).show_index(True)
    email.add_widget(table_widget)
    
    # 5. 进度条演示
    progress1 = ProgressWidget()
    progress1.set_label("总体进度").set_value(75).set_theme(ProgressTheme.PRIMARY)
    email.add_widget(progress1)
    
    progress2 = ProgressWidget()
    progress2.set_label("错误率").set_value(15).set_theme(ProgressTheme.ERROR)
    email.add_widget(progress2)
    
    # 6. 状态信息演示
    status_widget = StatusWidget()
    status_widget.set_title("系统运行状态").set_layout(LayoutType.HORIZONTAL)
    status_widget.add_status_item("总任务数", "156", StatusType.INFO)
    status_widget.add_status_item("成功任务", "142", StatusType.SUCCESS)
    status_widget.add_status_item("失败任务", "8", StatusType.ERROR)
    status_widget.add_status_item("运行时间", "2小时30分", StatusType.PRIMARY)
    email.add_widget(status_widget)
    
    # 7. 卡片组件演示
    card1 = CardWidget()
    card1.set_title("数据采集统计").set_icon("📊")
    card1.set_content("今日共采集数据 1,234 条，较昨日增长 15.6%")
    card1.add_metadata("数据源", "5个网站")
    card1.add_metadata("更新频率", "每小时")
    card1.add_metadata("数据质量", "优秀")
    
    card2 = CardWidget()
    card2.set_title("系统性能").set_icon("⚡")
    card2.set_content("系统运行稳定，CPU使用率 25%，内存使用率 45%")
    card2.add_metadata("响应时间", "< 200ms")
    card2.add_metadata("可用性", "99.9%")
    
    card3 = CardWidget()
    card3.set_title("存储状态").set_icon("💾")
    card3.set_content("数据库运行正常，存储空间充足")
    card3.add_metadata("已用空间", "2.3 TB")
    card3.add_metadata("剩余空间", "1.7 TB")
    
    # 8. 列布局演示
    column_widget = ColumnWidget()
    column_widget.set_columns(3).set_gap("15px")
    column_widget.add_widgets([card1, card2, card3])
    email.add_widget(column_widget)
    
    # 9. 圆形进度条演示
    circular_progress1 = CircularProgressWidget()
    circular_progress1.set_value(85).set_label("数据完整性").set_theme(ProgressTheme.SUCCESS).set_size("120px")
    
    circular_progress2 = CircularProgressWidget()
    circular_progress2.set_value(92).set_label("系统可用性").set_theme(ProgressTheme.PRIMARY).set_size("120px")
    
    circular_progress3 = CircularProgressWidget()
    circular_progress3.set_value(68).set_label("处理效率").set_theme(ProgressTheme.WARNING).set_size("120px")
    
    # 圆形进度条列布局
    circular_column = ColumnWidget()
    circular_column.set_columns(3).add_widgets([circular_progress1, circular_progress2, circular_progress3])
    email.add_widget(circular_column)
    
    # 10. 日志输出演示
    log_widget = LogWidget()
    log_widget.set_title("系统运行日志")
    
    # 添加示例日志
    sample_logs = [
        "2025-01-15 10:30:27.713 | INFO     | spider.main:start_task:45 - 开始执行爬虫任务",
        "2025-01-15 10:30:28.156 | DEBUG    | spider.parser:parse_data:23 - 解析页面数据完成",
        "2025-01-15 10:30:28.892 | WARNING  | spider.network:request:67 - 网络请求超时，正在重试",
        "2025-01-15 10:30:29.445 | INFO     | spider.storage:save_data:89 - 数据保存成功，共123条记录",
        "2025-01-15 10:30:30.123 | ERROR    | spider.main:handle_error:156 - 处理异常: 连接被拒绝"
    ]
    
    for log_line in sample_logs:
        log_widget.append_log(log_line)
    
    log_widget.set_max_height("300px")
    email.add_widget(log_widget)
    
    # 11. 引用样式演示
    quote_widget = QuoteWidget()
    quote_widget.set_content("优秀的代码不仅仅是能运行的代码，更是易于理解、维护和扩展的代码。")
    quote_widget.set_author("Clean Code")
    quote_widget.set_source("Robert C. Martin")
    quote_widget.set_quote_type(StatusType.SUCCESS)
    email.add_widget(quote_widget)
    
    # 12. 图表演示（使用占位符图片）
    chart_widget = ChartWidget()
    chart_widget.set_title("数据采集趋势图")
    chart_widget.set_image_url("https://via.placeholder.com/600x300/0078d4/ffffff?text=Chart+Placeholder")
    chart_widget.set_description("过去7天的数据采集量变化趋势")
    chart_widget.set_data_summary("平均每日采集 1,156 条数据，峰值出现在周三")
    email.add_widget(chart_widget)
    
    # 13. 图片演示
    image_widget = ImageWidget()
    image_widget.set_image_url("https://via.placeholder.com/400x200/107c10/ffffff?text=Success+Image")
    image_widget.set_title("系统架构图")
    image_widget.set_description("SpiderDaily 系统的整体架构设计")
    image_widget.set_alt_text("系统架构图")
    email.add_widget(image_widget)
    
    # 14. 结尾文本
    footer_text = TextWidget()
    footer_text.set_content(
        "以上展示了EWidget组件库的所有主要组件。\n"
        "每个组件都支持丰富的自定义选项和面向对象的操作方法。"
    ).set_align(TextAlign.CENTER).set_color("#8e8e93").set_font_size("14px")
    email.add_widget(footer_text)
    
    return email

def main():
    """主函数"""
    print("创建EWidget演示邮件...")
    
    # 创建演示邮件
    demo_email = create_demo_email()
    
    # 导出HTML文件
    output_path = demo_email.export("ewidget_demo")
    print(f"演示邮件已导出到: {output_path}")
    
    # 显示统计信息
    print(f"邮件标题: {demo_email.title}")
    print(f"包含组件数量: {len(demo_email)}")
    print("\n组件列表:")
    for i, widget in enumerate(demo_email.widgets, 1):
        print(f"  {i}. {widget.__class__.__name__} (ID: {widget.widget_id})")

if __name__ == "__main__":
    main() 