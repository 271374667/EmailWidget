"""EWidget简单使用示例"""
import pandas as pd

from email_widget.ewidget import (
    Email, TableWidget, AlertWidget, TextWidget, 
    ProgressWidget, CardWidget, StatusWidget,
    AlertType, StatusType, ProgressTheme, TextAlign
)

def create_simple_report():
    """创建一个简单的爬虫报告"""
    
    # 1. 创建邮件
    email = Email("爬虫任务报告")
    
    # 2. 添加标题
    title = TextWidget()
    title.set_content("爬虫任务执行报告").set_font_size("22px").set_align(TextAlign.CENTER).set_bold(True)
    email.add_widget(title)
    
    # 3. 添加成功提示
    success_alert = AlertWidget()
    success_alert.set_content("所有爬虫任务已成功完成！").set_alert_type(AlertType.TIP)
    email.add_widget(success_alert)
    
    # 4. 添加进度条
    progress = ProgressWidget()
    progress.set_label("任务完成进度").set_value(100).set_theme(ProgressTheme.SUCCESS)
    email.add_widget(progress)
    
    # 5. 添加统计卡片
    stats_card = CardWidget()
    stats_card.set_title("执行统计").set_icon("📊")
    stats_card.set_content("本次共执行 5 个爬虫任务，全部成功完成")
    stats_card.add_metadata("总耗时", "2分30秒")
    stats_card.add_metadata("数据量", "1,234 条")
    stats_card.add_metadata("成功率", "100%")
    email.add_widget(stats_card)
    
    return email

def main():
    """主函数"""
    print("创建简单爬虫报告...")
    
    # 创建报告
    report = create_simple_report()
    
    # 导出HTML
    output_path = report.export("spider_report")
    print(f"报告已导出到: {output_path}")

if __name__ == "__main__":
    main() 