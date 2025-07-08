"""EWidget演示文件

展示所有可用的Widget组件和使用方法
注意：本演示需要可选依赖支持，请根据需要安装：
- 表格功能：pip install pandas
- 图表功能：pip install matplotlib seaborn
"""

from email_widget import (
    AlertWidget,
    CardWidget,
    ChartWidget,
    CircularProgressWidget,
    ColumnWidget,
    Email,
    ImageWidget,
    LogWidget,
    ProgressWidget,
    QuoteWidget,
    StatusType,
    StatusWidget,
    TableWidget,
    TextWidget,
)
from email_widget.utils.optional_deps import (
    check_optional_dependency,
    import_optional_dependency,
)

try:
    # 检查matplotlib和seaborn是否可用
    check_optional_dependency("matplotlib")
    check_optional_dependency("seaborn")
    plt = import_optional_dependency("matplotlib.pyplot")
    sns = import_optional_dependency("seaborn")
    CHARTS_AVAILABLE = True
except ImportError as e:
    print(f"Charts not available: {e}")
    CHARTS_AVAILABLE = False

try:
    # 检查pandas是否可用
    check_optional_dependency("pandas")
    pd = import_optional_dependency("pandas")
    PANDAS_AVAILABLE = True
except ImportError as e:
    print(f"Pandas not available: {e}")
    PANDAS_AVAILABLE = False

from email_widget.core.enums import (
    AlertType,
    IconType,
    LayoutType,
    ProgressTheme,
    TextAlign,
    TextType,
)


def create_demo_email():
    """创建演示邮件"""

    # 创建邮件主体
    email = Email("EWidget 组件演示")

    # 1. 大标题
    title_text = TextWidget()
    title_text.set_content("EWidget 组件库完整演示").set_type(TextType.TITLE_LARGE)
    email.add_widget(title_text)

    # 2. 小标题
    subtitle_text = TextWidget()
    subtitle_text.set_content("展示所有可用的Widget组件和新功能").set_type(
        TextType.TITLE_SMALL
    )
    email.add_widget(subtitle_text)

    # 3. 介绍文本
    intro_text = TextWidget()
    intro_text.set_content(
        "这是一个完整的EWidget组件演示，展示了所有可用的组件类型。\n"
        "EWidget是一个面向对象的邮件HTML组件库，采用Fluent Design风格。"
    ).set_type(TextType.BODY)
    email.add_widget(intro_text)

    # 4. 补充说明
    caption_text = TextWidget()
    caption_text.set_content(
        "本演示包含了最新的功能：TextType枚举、深色日志主题、IconType枚举、base64图片嵌入等"
    ).set_type(TextType.CAPTION)
    email.add_widget(caption_text)

    # 5. 章节标题演示
    section1 = TextWidget()
    section1.set_content("基础组件展示").set_type(TextType.SECTION_H2)
    email.add_widget(section1)

    section1_1 = TextWidget()
    section1_1.set_content("警告框组件").set_type(TextType.SECTION_H3)
    email.add_widget(section1_1)

    # 3. 警告框演示
    note_alert = AlertWidget()
    note_alert.set_content(
        "这是一个信息提示框，用于显示重要的提示信息。"
    ).set_alert_type(AlertType.NOTE)
    email.add_widget(note_alert)

    warning_alert = AlertWidget()
    warning_alert.set_content(
        "这是一个警告提示框，用于显示需要注意的警告信息。"
    ).set_alert_type(AlertType.WARNING)
    email.add_widget(warning_alert)

    section1_2 = TextWidget()
    section1_2.set_content("表格组件").set_type(TextType.SECTION_H3)
    email.add_widget(section1_2)

    # 4. 表格演示
    table_widget = TableWidget()
    table_widget.set_title("爬虫任务执行结果")

    if PANDAS_AVAILABLE:
        # 创建示例数据（需要pandas）
        df = pd.DataFrame(
            {
                "任务名称": [
                    "网站A数据采集",
                    "网站B内容抓取",
                    "API数据同步",
                    "图片下载任务",
                ],
                "执行状态": [
                    {"text": "成功", "status": "success"},
                    {"text": "失败", "status": "error"},
                    {"text": "运行中", "status": "info"},
                    {"text": "等待中", "status": "warning"},
                ],
                "执行时间": [
                    "2024-01-15 10:30:00",
                    "2024-01-15 10:32:15",
                    "2024-01-15 10:35:00",
                    "2024-01-15 10:40:00",
                ],
                "耗时(秒)": ["12.5", "8.2", "45.1", "0.0"],
            }
        )
        table_widget.set_dataframe(df).show_index(True)
    else:
        # 使用手动数据（不需要pandas）
        table_widget.set_headers(["任务名称", "执行状态", "执行时间", "耗时(秒)"])
        table_widget.add_row(["网站A数据采集", "成功", "2024-01-15 10:30:00", "12.5"])
        table_widget.add_row(["网站B内容抓取", "失败", "2024-01-15 10:32:15", "8.2"])
        table_widget.add_row(["API数据同步", "运行中", "2024-01-15 10:35:00", "45.1"])
        table_widget.add_row(["图片下载任务", "等待中", "2024-01-15 10:40:00", "0.0"])
        table_widget.show_index(True)

    email.add_widget(table_widget)

    # 5. 进度条演示 - 展示面向对象方法
    progress1 = ProgressWidget()
    progress1.set_label("总体进度").set_value(60).set_theme(ProgressTheme.PRIMARY)
    # 演示增量操作
    progress1.increment(15)  # 增加到75%
    email.add_widget(progress1)

    progress2 = ProgressWidget()
    progress2.set_label("错误率").set_value(20).set_theme(ProgressTheme.ERROR)
    # 演示减量操作
    progress2.decrement(5)  # 减少到15%
    email.add_widget(progress2)

    # 完成状态的进度条
    progress3 = ProgressWidget()
    progress3.set_label("数据验证").set_theme(
        ProgressTheme.SUCCESS
    ).complete()  # 设为100%
    email.add_widget(progress3)

    section2 = TextWidget()
    section2.set_content("高级组件展示").set_type(TextType.SECTION_H2)
    email.add_widget(section2)

    section2_1 = TextWidget()
    section2_1.set_content("状态信息组件").set_type(TextType.SECTION_H3)
    email.add_widget(section2_1)

    # 6. 状态信息演示
    status_widget = StatusWidget()
    status_widget.set_title("系统运行状态").set_layout(LayoutType.HORIZONTAL)
    status_widget.add_status_item("总任务数", "156", StatusType.INFO)
    status_widget.add_status_item("成功任务", "142", StatusType.SUCCESS)
    status_widget.add_status_item("失败任务", "8", StatusType.ERROR)
    status_widget.add_status_item("运行时间", "2小时30分", StatusType.PRIMARY)
    email.add_widget(status_widget)

    # 7. 卡片组件演示 - 使用新的IconType枚举
    card1 = CardWidget()
    card1.set_title("数据采集统计").set_icon(IconType.DATA)
    card1.set_content("今日共采集数据 1,234 条，较昨日增长 15.6%")
    card1.add_metadata("数据源", "5个网站")
    card1.add_metadata("更新频率", "每小时")
    card1.add_metadata("数据质量", "优秀")

    card2 = CardWidget()
    card2.set_title("系统性能").set_icon(IconType.CPU)
    card2.set_content("系统运行稳定，CPU使用率 25%，内存使用率 45%")
    card2.add_metadata("响应时间", "< 200ms")
    card2.add_metadata("可用性", "99.9%")

    card3 = CardWidget()
    card3.set_title("存储状态").set_icon(IconType.STORAGE)
    card3.set_content("数据库运行正常，存储空间充足")
    card3.add_metadata("已用空间", "2.3 TB")
    card3.add_metadata("剩余空间", "1.7 TB")

    # 默认图标卡片
    card4 = CardWidget()
    card4.set_title("默认图标演示")  # 不设置图标，使用默认INFO图标
    card4.set_content("这个卡片使用了默认的Info图标")
    card4.add_metadata("图标类型", "默认Info图标")

    # 8. 列布局演示
    column_widget = ColumnWidget()
    # column_widget.set_columns(2).set_gap("15px")
    column_widget.add_widgets([card1, card2, card3, card4])
    # column_widget.add_widgets([card1, card2])
    email.add_widget(column_widget)

    # 9. 圆形进度条演示
    circular_progress1 = CircularProgressWidget()
    circular_progress1.set_value(85).set_label("数据完整性").set_theme(
        ProgressTheme.SUCCESS
    ).set_size("120px")

    circular_progress2 = CircularProgressWidget()
    circular_progress2.set_value(92).set_label("系统可用性").set_theme(
        ProgressTheme.PRIMARY
    ).set_size("120px")

    circular_progress3 = CircularProgressWidget()
    circular_progress3.set_value(68).set_label("处理效率").set_theme(
        ProgressTheme.WARNING
    ).set_size("120px")

    # 圆形进度条列布局
    circular_column = ColumnWidget()
    circular_column.set_columns(3).add_widgets(
        [circular_progress1, circular_progress2, circular_progress3]
    )
    email.add_widget(circular_column)

    # 10. 日志输出演示 - 使用面向对象方法
    log_widget = LogWidget()
    log_widget.set_title("系统运行日志")

    # 使用面向对象方法添加日志
    log_widget.append_log(
        "2025-01-15 10:30:27.713 | INFO     | spider.main:start_task:45 - 开始执行爬虫任务"
    )
    log_widget.append_log(
        "2025-01-15 10:30:28.156 | DEBUG    | spider.parser:parse_data:23 - 解析页面数据完成"
    )
    log_widget.append_log(
        "2025-01-15 10:30:28.892 | WARNING  | spider.network:request:67 - 网络请求超时，正在重试"
    )
    log_widget.append_log(
        "2025-01-15 10:30:29.445 | INFO     | spider.storage:save_data:89 - 数据保存成功，共123条记录"
    )
    log_widget.append_log(
        "2025-01-15 10:30:30.123 | ERROR    | spider.main:handle_error:156 - 处理异常: 连接被拒绝"
    )
    log_widget.append_log(
        "2025-01-15 10:30:31.234 | CRITICAL | spider.main:critical_error:200 - 系统出现严重错误"
    )

    # 设置日志级别过滤和样式
    log_widget.set_max_height("300px").show_timestamp(True).show_level(
        True
    ).show_source(True)
    email.add_widget(log_widget)

    # 11. 引用样式演示
    quote_widget = QuoteWidget()
    quote_widget.set_content(
        "优秀的代码不仅仅是能运行的代码，更是易于理解、维护和扩展的代码。"
    )
    quote_widget.set_author("Clean Code")
    quote_widget.set_source("Robert C. Martin")
    quote_widget.set_quote_type(StatusType.SUCCESS)
    email.add_widget(quote_widget)

    # 12. 图表演示（使用seaborn生成）
    if CHARTS_AVAILABLE:
        chart_widget = ChartWidget()
        chart_widget.set_title("数据采集趋势图")
        chart_widget.set_description("过去7天的数据采集量变化趋势")
        chart_widget.set_data_summary("平均每日采集 1,156 条数据，峰值出现在周三")

        # 创建示例数据并绘制图表
        days = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
        data_counts = [980, 1150, 1420, 1200, 1050, 890, 1100]

        plt.figure(figsize=(10, 6))
        sns.set_style("whitegrid")
        ax = sns.lineplot(
            x=days, y=data_counts, marker="o", linewidth=2.5, markersize=8
        )
        ax.set_title("数据采集趋势图", fontsize=16, fontweight="bold")
        ax.set_xlabel("日期", fontsize=12)
        ax.set_ylabel("采集数量", fontsize=12)
        ax.grid(True, alpha=0.3)

        # 设置图表到widget
        chart_widget.set_chart(plt)
        email.add_widget(chart_widget)
    else:
        # 如果没有图表库，显示提示信息
        chart_note = TextWidget()
        chart_note.set_content(
            "📊 图表演示跳过 - 需要安装 matplotlib 和 seaborn"
        ).set_type(TextType.CAPTION)
        email.add_widget(chart_note)

    # 13. 图片演示
    image_widget = ImageWidget()
    image_widget.set_image_url("https://placehold.co/600x400")
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
    output_path = demo_email.export_html("ewidget_demo")
    print(f"演示邮件已导出到: {output_path}")

    # 显示统计信息
    print(f"邮件标题: {demo_email.title}")
    print(f"包含组件数量: {len(demo_email)}")
    print("\n组件列表:")
    for i, widget in enumerate(demo_email.widgets, 1):
        print(f"  {i}. {widget.__class__.__name__} (ID: {widget.widget_id})")


if __name__ == "__main__":
    main()
