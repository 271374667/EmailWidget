"""EmailWidget完整功能演示

展示所有13个Widget组件的完整功能和使用方法。
注意：本演示需要可选依赖支持，请根据需要安装：
- 表格功能：pip install pandas
- 图表功能：pip install matplotlib seaborn
"""

from email_widget import (
    AlertWidget,
    ButtonWidget,
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
    LogLevel,
    ProgressTheme,
    TextAlign,
    TextType,
)


def create_comprehensive_demo():
    """创建包含所有组件的综合演示邮件"""
    
    # 创建邮件主体
    email = Email("EmailWidget 完整功能演示")
    email.set_subtitle("展示所有13个Widget组件的完整功能")
    email.set_footer("本演示由 EmailWidget v0.4.6 生成 | 更多信息请访问 GitHub")
    
    # ========== 1. 文本组件 (TextWidget) ==========
    email.add_text("1. 文本组件 (TextWidget)", text_type=TextType.SECTION_H2)
    
    # 展示所有文本类型
    email.add_text("大标题文本", text_type=TextType.TITLE_LARGE)
    email.add_text("小标题文本", text_type=TextType.TITLE_SMALL)
    email.add_text("二级章节标题", text_type=TextType.SECTION_H2)
    email.add_text("三级章节标题", text_type=TextType.SECTION_H3)
    email.add_text("四级章节标题", text_type=TextType.SECTION_H4)
    email.add_text("五级章节标题", text_type=TextType.SECTION_H5)
    email.add_text(
        "这是正文文本，可以包含较长的内容。支持换行\n"
        "以及多行文本的显示。这是默认的文本类型。",
        text_type=TextType.BODY
    )
    email.add_text("这是说明文本，通常用于补充说明", text_type=TextType.CAPTION)
    
    # 文本对齐和样式
    text_center = TextWidget()
    text_center.set_content("居中对齐的文本").set_align(TextAlign.CENTER).set_color("#007bff")
    email.add_widget(text_center)
    
    text_right = TextWidget()
    text_right.set_content("右对齐的文本").set_align(TextAlign.RIGHT).set_font_size("18px")
    email.add_widget(text_right)
    
    # ========== 2. 按钮组件 (ButtonWidget) - 新增组件 ==========
    email.add_text("2. 按钮组件 (ButtonWidget) - 新增组件", text_type=TextType.SECTION_H2)
    
    # 基础按钮
    btn_basic = ButtonWidget()
    btn_basic.set_text("点击查看详情").set_href("https://example.com/details")
    email.add_widget(btn_basic)
    
    # 自定义样式按钮
    btn_custom = ButtonWidget()
    btn_custom.set_text("立即购买")
    btn_custom.set_href("https://shop.example.com")
    btn_custom.set_background_color("#22c55e")
    btn_custom.set_text_color("#ffffff")
    btn_custom.set_width("200px")
    btn_custom.set_align("center")
    btn_custom.set_padding("12px 24px")
    btn_custom.set_border_radius("8px")
    btn_custom.set_font_size("16px")
    email.add_widget(btn_custom)
    
    # 带边框的按钮
    btn_outlined = ButtonWidget()
    btn_outlined.set_text("了解更多")
    btn_outlined.set_href("https://docs.example.com")
    btn_outlined.set_background_color("transparent")
    btn_outlined.set_text_color("#3b82f6")
    btn_outlined.set_border("2px solid #3b82f6")
    btn_outlined.set_align("center")
    email.add_widget(btn_outlined)
    
    # 按钮组（使用列布局）
    btn_group = ColumnWidget()
    btn_group.set_columns(3)
    
    btn1 = ButtonWidget().set_full_button("主要操作", "https://example.com/primary", "#3b82f6")
    btn2 = ButtonWidget().set_full_button("成功操作", "https://example.com/success", "#22c55e")
    btn3 = ButtonWidget().set_full_button("危险操作", "https://example.com/danger", "#ef4444")
    
    btn_group.add_widgets([btn1, btn2, btn3])
    email.add_widget(btn_group)
    
    # ========== 3. 警告框组件 (AlertWidget) ==========
    email.add_text("3. 警告框组件 (AlertWidget)", text_type=TextType.SECTION_H2)
    
    # 所有警告类型演示
    alert_note = AlertWidget()
    alert_note.set_full_alert(
        "这是一个注意提示框，用于显示一般性的提示信息。",
        AlertType.NOTE,
        "注意事项"
    )
    email.add_widget(alert_note)
    
    alert_tip = AlertWidget()
    alert_tip.set_content("💡 专业提示：使用链式调用可以让代码更简洁")
    alert_tip.set_alert_type(AlertType.TIP)
    alert_tip.set_icon("💡")
    email.add_widget(alert_tip)
    
    alert_important = AlertWidget()
    alert_important.set_content("重要：请在执行操作前备份数据")
    alert_important.set_alert_type(AlertType.IMPORTANT)
    email.add_widget(alert_important)
    
    alert_warning = AlertWidget()
    alert_warning.set_content("警告：此操作不可撤销，请谨慎操作")
    alert_warning.set_alert_type(AlertType.WARNING)
    email.add_widget(alert_warning)
    
    alert_caution = AlertWidget()
    alert_caution.set_content("危险：系统检测到异常活动，请立即检查")
    alert_caution.set_alert_type(AlertType.CAUTION)
    email.add_widget(alert_caution)
    
    # ========== 4. 表格组件 (TableWidget) ==========
    email.add_text("4. 表格组件 (TableWidget)", text_type=TextType.SECTION_H2)
    
    if PANDAS_AVAILABLE:
        # 使用DataFrame创建表格
        df = pd.DataFrame({
            "产品名称": ["iPhone 15", "MacBook Pro", "iPad Air", "AirPods Pro", "Apple Watch"],
            "销量": [1250, 580, 920, 1500, 830],
            "单价": ["¥5,999", "¥12,999", "¥4,599", "¥1,999", "¥2,999"],
            "总收入": ["¥7,498,750", "¥7,539,420", "¥4,231,080", "¥2,998,500", "¥2,489,170"],
            "状态": [
                {"text": "热销", "status": "success"},
                {"text": "正常", "status": "info"},
                {"text": "库存低", "status": "warning"},
                {"text": "缺货", "status": "error"},
                {"text": "正常", "status": "info"},
            ]
        })
        
        table = TableWidget()
        table.set_title("产品销售统计表")
        table.set_dataframe(df)
        table.show_index(True)
        table.set_striped(True)
        email.add_widget(table)
    else:
        # 手动创建表格
        table = TableWidget()
        table.set_title("任务执行状态")
        table.set_headers(["任务ID", "任务名称", "开始时间", "状态", "进度"])
        table.add_row(["#001", "数据采集", "10:30:00", "运行中", "75%"])
        table.add_row(["#002", "数据清洗", "11:15:00", "完成", "100%"])
        table.add_row(["#003", "数据分析", "14:00:00", "等待", "0%"])
        table.add_row(["#004", "报告生成", "15:30:00", "失败", "45%"])
        table.set_striped(True)
        email.add_widget(table)
    
    # ========== 5. 进度条组件 (ProgressWidget) ==========
    email.add_text("5. 进度条组件 (ProgressWidget)", text_type=TextType.SECTION_H2)
    
    # 不同主题的进度条
    progress_primary = ProgressWidget()
    progress_primary.set_label("总体进度").set_value(75).set_theme(ProgressTheme.PRIMARY)
    email.add_widget(progress_primary)
    
    progress_success = ProgressWidget()
    progress_success.set_label("已完成任务").set_value(92).set_theme(ProgressTheme.SUCCESS)
    email.add_widget(progress_success)
    
    progress_warning = ProgressWidget()
    progress_warning.set_label("CPU使用率").set_value(68).set_theme(ProgressTheme.WARNING)
    email.add_widget(progress_warning)
    
    progress_error = ProgressWidget()
    progress_error.set_label("错误率").set_value(15).set_theme(ProgressTheme.ERROR)
    email.add_widget(progress_error)
    
    progress_info = ProgressWidget()
    progress_info.set_label("内存使用").set_value(45).set_theme(ProgressTheme.INFO)
    email.add_widget(progress_info)
    
    # 演示进度条的增量和减量操作
    progress_demo = ProgressWidget()
    progress_demo.set_label("动态进度演示").set_value(50)
    progress_demo.increment(20)  # 增加到70%
    progress_demo.decrement(10)  # 减少到60%
    email.add_widget(progress_demo)
    
    # ========== 6. 圆形进度条组件 (CircularProgressWidget) ==========
    email.add_text("6. 圆形进度条组件 (CircularProgressWidget)", text_type=TextType.SECTION_H2)
    
    circular_layout = ColumnWidget()
    circular_layout.set_columns(4)
    
    # 不同大小和主题
    circular1 = CircularProgressWidget()
    circular1.set_value(95).set_label("系统健康度").set_theme(ProgressTheme.SUCCESS).set_size("100px")
    
    circular2 = CircularProgressWidget()
    circular2.set_value(78).set_label("存储使用").set_theme(ProgressTheme.PRIMARY).set_size("120px")
    
    circular3 = CircularProgressWidget()
    circular3.set_value(62).set_label("网络负载").set_theme(ProgressTheme.WARNING).set_size("140px")
    
    circular4 = CircularProgressWidget()
    circular4.set_value(25).set_label("错误比例").set_theme(ProgressTheme.ERROR).set_size("100px")
    
    circular_layout.add_widgets([circular1, circular2, circular3, circular4])
    email.add_widget(circular_layout)
    
    # ========== 7. 状态组件 (StatusWidget) ==========
    email.add_text("7. 状态组件 (StatusWidget)", text_type=TextType.SECTION_H2)
    
    # 水平布局状态
    status_h = StatusWidget()
    status_h.set_title("系统监控面板")
    status_h.set_layout(LayoutType.HORIZONTAL)
    status_h.add_status_item("在线用户", "1,234", StatusType.SUCCESS)
    status_h.add_status_item("今日访问", "45.6K", StatusType.INFO)
    status_h.add_status_item("错误次数", "12", StatusType.ERROR)
    status_h.add_status_item("平均响应", "156ms", StatusType.WARNING)
    email.add_widget(status_h)
    
    # 垂直布局状态
    status_v = StatusWidget()
    status_v.set_title("服务器状态")
    status_v.set_layout(LayoutType.VERTICAL)
    status_v.add_status_item("服务器状态", "运行中", StatusType.SUCCESS)
    status_v.add_status_item("最后更新", "2分钟前", StatusType.INFO)
    status_v.add_status_item("队列长度", "128", StatusType.WARNING)
    email.add_widget(status_v)
    
    # ========== 8. 卡片组件 (CardWidget) ==========
    email.add_text("8. 卡片组件 (CardWidget)", text_type=TextType.SECTION_H2)
    
    cards_layout = ColumnWidget()
    cards_layout.set_columns(3)
    
    # 使用不同图标的卡片
    card1 = CardWidget()
    card1.set_title("数据分析").set_icon(IconType.CHART)
    card1.set_content("本月共处理数据 125.6GB，分析报告 89 份")
    card1.add_metadata("准确率", "99.2%")
    card1.add_metadata("处理速度", "12.5 MB/s")
    
    card2 = CardWidget()
    card2.set_title("系统状态").set_icon(IconType.SERVER)
    card2.set_content("系统安全运行 365 天，未发现安全威胁")
    card2.add_metadata("防火墙", "已启用")
    card2.add_metadata("最后扫描", "1小时前")
    
    card3 = CardWidget()
    card3.set_title("数据处理").set_icon(IconType.DATA)
    card3.set_content("本周处理数据 234 万条，处理成功率 96%")
    card3.add_metadata("响应时间", "< 2小时")
    card3.add_metadata("成功率", "96%")
    
    cards_layout.add_widgets([card1, card2, card3])
    email.add_widget(cards_layout)
    
    # 更多图标类型展示
    cards_layout2 = ColumnWidget()
    cards_layout2.set_columns(3)
    
    card4 = CardWidget()
    card4.set_title("网络状态").set_icon(IconType.WEB)
    card4.set_content("网络连接稳定，延迟 < 10ms")
    
    card5 = CardWidget()
    card5.set_title("数据库状态").set_icon(IconType.DATABASE)
    card5.set_content("数据库运行正常，查询响应快速")
    
    card6 = CardWidget()
    card6.set_title("处理状态").set_icon(IconType.PROCESSING)
    card6.set_content("正在处理中的任务：15 个")
    
    cards_layout2.add_widgets([card4, card5, card6])
    email.add_widget(cards_layout2)
    
    # ========== 9. 引用组件 (QuoteWidget) ==========
    email.add_text("9. 引用组件 (QuoteWidget)", text_type=TextType.SECTION_H2)
    
    # 不同类型的引用
    quote1 = QuoteWidget()
    quote1.set_content("简洁是终极的复杂。")
    quote1.set_author("莱昂纳多·达·芬奇")
    quote1.set_quote_type(StatusType.PRIMARY)
    email.add_widget(quote1)
    
    quote2 = QuoteWidget()
    quote2.set_content(
        "任何傻瓜都能写出计算机可以理解的代码。"
        "好的程序员能写出人类可以理解的代码。"
    )
    quote2.set_author("Martin Fowler")
    quote2.set_source("《重构》")
    quote2.set_quote_type(StatusType.SUCCESS)
    email.add_widget(quote2)
    
    # ========== 10. 日志组件 (LogWidget) ==========
    email.add_text("10. 日志组件 (LogWidget)", text_type=TextType.SECTION_H2)
    
    log = LogWidget()
    log.set_title("系统运行日志")
    log.set_max_height("400px")
    
    # 添加各种级别的日志
    log.append_log("2025-01-15 10:30:00.123 | DEBUG    | app.core:init:23 - 初始化核心模块")
    log.append_log("2025-01-15 10:30:01.456 | INFO     | app.server:start:45 - 服务器启动成功，监听端口 8080")
    log.append_log("2025-01-15 10:30:02.789 | INFO     | app.db:connect:67 - 数据库连接成功")
    log.append_log("2025-01-15 10:30:05.123 | WARNING  | app.api:auth:89 - 检测到未授权的API访问尝试")
    log.append_log("2025-01-15 10:30:10.456 | ERROR    | app.service:process:123 - 处理请求时发生错误: NullPointerException")
    log.append_log("2025-01-15 10:30:15.789 | CRITICAL | app.monitor:check:156 - 系统内存使用率超过90%，触发告警")
    log.append_log("2025-01-15 10:30:20.123 | INFO     | app.task:complete:178 - 定时任务执行完成，处理记录 1000 条")
    log.append_log("2025-01-15 10:30:25.456 | DEBUG    | app.cache:update:200 - 缓存更新完成，命中率 85.6%")
    
    # 设置日志显示选项
    log.show_timestamp(True).show_level(True).show_source(True)
    email.add_widget(log)
    
    # ========== 11. 图表组件 (ChartWidget) ==========
    email.add_text("11. 图表组件 (ChartWidget)", text_type=TextType.SECTION_H2)
    
    if CHARTS_AVAILABLE:
        # 创建示例图表
        chart = ChartWidget()
        chart.set_title("月度销售趋势分析")
        chart.set_description("2024年各月销售额变化趋势（单位：万元）")
        
        # 准备数据
        months = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
        sales = [120, 135, 128, 145, 162, 178, 185, 176, 195, 210, 188, 225]
        
        # 创建图表
        plt.figure(figsize=(12, 6))
        sns.set_style("whitegrid")
        
        # 绘制柱状图和折线图
        ax = plt.gca()
        bars = ax.bar(months, sales, color='skyblue', alpha=0.7, label='销售额')
        line = ax.plot(months, sales, color='red', marker='o', linewidth=2, markersize=8, label='趋势线')
        
        # 添加数值标签
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                   f'{int(height)}', ha='center', va='bottom')
        
        ax.set_title('2024年月度销售趋势', fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('月份', fontsize=12)
        ax.set_ylabel('销售额（万元）', fontsize=12)
        ax.set_ylim(0, 250)
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        chart.set_chart(plt)
        chart.set_data_summary("全年销售额共计 1,979 万元，12月达到峰值 225 万元")
        email.add_widget(chart)
        
        # 第二个图表：饼图
        chart2 = ChartWidget()
        chart2.set_title("产品类别销售占比")
        chart2.set_description("各产品类别在总销售额中的占比分布")
        
        plt.figure(figsize=(8, 8))
        categories = ['电子产品', '服装配饰', '家居用品', '食品饮料', '其他']
        sizes = [35, 25, 20, 15, 5]
        colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
        explode = (0.1, 0, 0, 0, 0)  # 突出显示第一块
        
        plt.pie(sizes, explode=explode, labels=categories, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        plt.title('产品类别销售占比', fontsize=16, fontweight='bold', pad=20)
        
        chart2.set_chart(plt)
        email.add_widget(chart2)
    else:
        alert_chart = AlertWidget()
        alert_chart.set_content("图表功能需要安装 matplotlib 和 seaborn 库")
        alert_chart.set_alert_type(AlertType.NOTE)
        email.add_widget(alert_chart)
    
    # ========== 12. 图片组件 (ImageWidget) ==========
    email.add_text("12. 图片组件 (ImageWidget)", text_type=TextType.SECTION_H2)
    
    # 网络图片
    img1 = ImageWidget()
    img1.set_image_url("https://via.placeholder.com/800x400/3b82f6/ffffff?text=EmailWidget+Demo")
    img1.set_title("产品展示图")
    img1.set_description("EmailWidget 组件库的功能展示")
    img1.set_alt_text("EmailWidget Demo")
    email.add_widget(img1)
    
    # 多图展示（使用列布局）
    img_layout = ColumnWidget()
    img_layout.set_columns(3)
    
    img2 = ImageWidget()
    img2.set_image_url("https://via.placeholder.com/300x200/22c55e/ffffff?text=Success")
    img2.set_title("成功案例")
    
    img3 = ImageWidget()
    img3.set_image_url("https://via.placeholder.com/300x200/f59e0b/ffffff?text=Warning")
    img3.set_title("注意事项")
    
    img4 = ImageWidget()
    img4.set_image_url("https://via.placeholder.com/300x200/ef4444/ffffff?text=Error")
    img4.set_title("错误示例")
    
    img_layout.add_widgets([img2, img3, img4])
    email.add_widget(img_layout)
    
    # ========== 13. 列布局组件 (ColumnWidget) ==========
    email.add_text("13. 列布局组件 (ColumnWidget)", text_type=TextType.SECTION_H2)
    
    # 展示不同列数的布局
    email.add_text("两列布局示例：", text_type=TextType.CAPTION)
    
    col2 = ColumnWidget()
    col2.set_columns(2)
    
    # 左列内容
    left_content = TextWidget()
    left_content.set_content("左侧列内容\n这里可以放置任何Widget组件")
    left_content.set_type(TextType.BODY)
    
    # 右列内容
    right_progress = ProgressWidget()
    right_progress.set_label("右侧进度条").set_value(80)
    
    col2.add_widgets([left_content, right_progress])
    email.add_widget(col2)
    
    # 复杂布局示例
    email.add_text("复杂布局示例：", text_type=TextType.CAPTION)
    
    complex_layout = ColumnWidget()
    complex_layout.set_columns(3).set_gap("20px")
    
    # 创建三个不同的内容块
    block1 = CardWidget()
    block1.set_title("统计数据").set_content("本月新增用户 1,234 人")
    
    block2 = QuoteWidget()
    block2.set_content("保持简单").set_author("KISS原则")
    
    block3 = StatusWidget()
    block3.add_status_item("状态", "正常", StatusType.SUCCESS)
    
    complex_layout.add_widgets([block1, block2, block3])
    email.add_widget(complex_layout)
    
    # ========== 总结 ==========
    email.add_text("功能总结", text_type=TextType.SECTION_H2)
    
    summary_text = TextWidget()
    summary_text.set_content(
        "以上展示了 EmailWidget 的全部 13 个组件：\n"
        "1. TextWidget - 文本组件（8种文本类型）\n"
        "2. ButtonWidget - 按钮组件（新增）\n"
        "3. AlertWidget - 警告框组件（5种警告类型）\n"
        "4. TableWidget - 表格组件\n"
        "5. ProgressWidget - 进度条组件（5种主题）\n"
        "6. CircularProgressWidget - 圆形进度条\n"
        "7. StatusWidget - 状态显示组件\n"
        "8. CardWidget - 卡片组件（10种图标）\n"
        "9. QuoteWidget - 引用组件\n"
        "10. LogWidget - 日志组件（6种日志级别）\n"
        "11. ChartWidget - 图表组件\n"
        "12. ImageWidget - 图片组件\n"
        "13. ColumnWidget - 列布局组件"
    )
    summary_text.set_align(TextAlign.CENTER)
    summary_text.set_color("#666666")
    email.add_widget(summary_text)
    
    # 创建一个漂亮的结尾
    end_quote = QuoteWidget()
    end_quote.set_content("感谢使用 EmailWidget！希望它能帮助您创建更美观的邮件报告。")
    end_quote.set_author("EmailWidget 开发团队")
    end_quote.set_quote_type(StatusType.SUCCESS)
    email.add_widget(end_quote)
    
    return email


def main():
    """主函数"""
    print("=" * 60)
    print("EmailWidget 完整功能演示")
    print("=" * 60)
    
    # 创建演示邮件
    print("正在创建演示邮件...")
    demo_email = create_comprehensive_demo()
    
    # 导出HTML文件
    output_path = demo_email.export_html("emailwidget_full_demo")
    print(f"✅ 演示邮件已导出到: {output_path}")
    
    # 显示统计信息
    print("\n📊 邮件统计信息:")
    print(f"  - 邮件标题: {demo_email.title}")
    print(f"  - 邮件副标题: {demo_email.subtitle}")
    print(f"  - 包含组件数量: {len(demo_email)} 个")
    
    # 统计各类组件数量
    widget_count = {}
    for widget in demo_email.widgets:
        widget_type = widget.__class__.__name__
        widget_count[widget_type] = widget_count.get(widget_type, 0) + 1
    
    print("\n📋 组件类型统计:")
    for widget_type, count in sorted(widget_count.items()):
        print(f"  - {widget_type}: {count} 个")
    
    print("\n✨ 演示完成！请查看生成的 HTML 文件。")
    print("=" * 60)


if __name__ == "__main__":
    main()