# 组件概览

EmailWidget 提供了丰富的组件库，涵盖了邮件中常见的各种内容类型。本页面展示了所有可用的组件及其预览效果。

<div class="main-content">
    <div class="component-grid">
        <!-- 第一行：文本组件 & 表格组件 -->
        <div class="component-row">
            <div class="component-item">
                <h3><a href="../text-widget/">TextWidget 文本组件</a></h3>
                <p>用于显示各种文本内容，支持多种样式和格式</p>
                <div class="component-preview">
                    <div style="background: #f8f9fa; border: 1px solid #e9ecef; border-radius: 4px; padding: 16px; margin: 16px 0;">
                        <h2 style="color: #0078d4; text-align: center; margin: 0; font-size: 18px;">这是一段重要文本</h2>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">标题</span>
                    <span class="tag">正文</span>
                    <span class="tag">章节</span>
                </div>
            </div>
            <div class="component-item">
                <h3><a href="../table-widget/">TableWidget 表格组件</a></h3>
                <p>展示结构化数据，支持表头、索引列、条纹样式等</p>
                <div class="component-preview">
                    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0;">
                        <table style="width: 100%; border-collapse: collapse; font-size: 12px;">
                            <thead>
                                <tr style="background: #f8f9fa;">
                                    <th style="padding: 8px; text-align: left; border-bottom: 2px solid #e9ecef; font-weight: 600;">项目</th>
                                    <th style="padding: 8px; text-align: left; border-bottom: 2px solid #e9ecef; font-weight: 600;">状态</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr style="background: #ffffff;">
                                    <td style="padding: 8px; border-bottom: 1px solid #e9ecef;">用户注册</td>
                                    <td style="padding: 8px; border-bottom: 1px solid #e9ecef; color: #107c10; font-weight: 600;">正常</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">数据</span>
                    <span class="tag">统计</span>
                    <span class="tag">状态</span>
                </div>
            </div>
        </div>

        <!-- 第二行：图片组件 & 图表组件 -->
        <div class="component-row">
            <div class="component-item">
                <h3><a href="../image-widget/">ImageWidget 图片组件</a></h3>
                <p>展示图片内容，支持标题、描述和多种布局选项</p>
                <div class="component-preview">
                    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0; text-align: center;">
                        <h4 style="color: #323130; margin-bottom: 8px; font-size: 14px;">数据趋势图</h4>
                        <div style="background: #f3f2f1; padding: 20px; border-radius: 4px; color: #605e5c; font-size: 12px;">
                            [图片占位符]
                        </div>
                        <p style="color: #605e5c; margin-top: 8px; font-size: 12px;">显示最近30天的用户增长趋势</p>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">图片</span>
                    <span class="tag">展示</span>
                    <span class="tag">说明</span>
                </div>
            </div>
            <div class="component-item">
                <h3><a href="../chart-widget/">ChartWidget 图表组件</a></h3>
                <p>专门用于展示图表，支持多种图表类型和数据摘要</p>
                <div class="component-preview">
                    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0; text-align: center;">
                        <h4 style="color: #323130; margin-bottom: 8px; font-size: 14px;">月度销售统计</h4>
                        <div style="background: #f8f9fa; padding: 30px; border-radius: 4px; border: 1px dashed #dee2e6; color: #6c757d; font-size: 12px;">
                            [图表占位符]
                        </div>
                        <div style="font-size: 11px; color: #8e8e93; margin-top: 8px; padding-top: 8px; border-top: 1px solid #f3f2f1;">
                            总销售额: ¥1,250,000
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">图表</span>
                    <span class="tag">数据</span>
                    <span class="tag">可视化</span>
                </div>
            </div>
        </div>

        <!-- 第三行：进度组件 & 圆形进度组件 -->
        <div class="component-row">
            <div class="component-item">
                <h3><a href="../progress-widget/">ProgressWidget 进度条</a></h3>
                <p>显示任务或进程的完成进度，支持多种主题</p>
                <div class="component-preview">
                    <div style="margin: 16px 0;">
                        <div style="font-size: 12px; font-weight: 600; color: #323130; margin-bottom: 8px;">项目完成进度</div>
                        <div style="width: 100%; height: 16px; background: #e1dfdd; border-radius: 8px; overflow: hidden; position: relative;">
                            <div style="width: 75%; height: 100%; background: #107c10; border-radius: 8px;"></div>
                            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 10px; font-weight: 600; color: #ffffff;">75%</div>
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">进度</span>
                    <span class="tag">状态</span>
                    <span class="tag">百分比</span>
                </div>
            </div>
            <div class="component-item">
                <h3><a href="../circular-progress-widget/">CircularProgressWidget 圆形进度条</a></h3>
                <p>以圆形方式显示进度，适合展示百分比数据</p>
                <div class="component-preview">
                    <div style="text-align: center; margin: 16px 0;">
                        <div style="width: 80px; height: 80px; border-radius: 50%; background: conic-gradient(#0078d4 0deg, #0078d4 316.8deg, #e1dfdd 316.8deg); margin: 0 auto; display: flex; align-items: center; justify-content: center;">
                            <div style="width: 60px; height: 60px; background: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; color: #323130; font-size: 12px;">88%</div>
                        </div>
                        <div style="margin-top: 8px; font-size: 12px; color: #323130;">系统性能</div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">圆形</span>
                    <span class="tag">进度</span>
                    <span class="tag">KPI</span>
                </div>
            </div>
        </div>

        <!-- 第四行：状态组件 & 警告组件 -->
        <div class="component-row">
            <div class="component-item">
                <h3><a href="../status-widget/">StatusWidget 状态信息</a></h3>
                <p>展示多个状态项的信息，支持水平和垂直布局</p>
                <div class="component-preview">
                    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0;">
                        <h4 style="font-size: 14px; font-weight: 600; color: #323130; margin-bottom: 8px;">系统状态</h4>
                        <div style="margin: 4px 0; padding: 4px 0; border-bottom: 1px solid #f3f2f1; font-size: 12px;">
                            <div style="font-weight: 500; color: #605e5c;">CPU使用率</div>
                            <div style="color: #107c10; font-weight: 600;">45%</div>
                        </div>
                        <div style="margin: 4px 0; padding: 4px 0; font-size: 12px;">
                            <div style="font-weight: 500; color: #605e5c;">内存使用率</div>
                            <div style="color: #ff8c00; font-weight: 600;">78%</div>
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">状态</span>
                    <span class="tag">监控</span>
                    <span class="tag">系统</span>
                </div>
            </div>
            <div class="component-item">
                <h3><a href="../alert-widget/">AlertWidget 警告组件</a></h3>
                <p>显示各种类型的警告信息，支持GitHub风格的提示框</p>
                <div class="component-preview">
                    <div style="background: #dbeafe; border: 1px solid #3b82f6; border-left: 4px solid #3b82f6; border-radius: 4px; padding: 12px; margin: 16px 0; color: #1e40af; font-size: 12px;">
                        <div style="display: flex; align-items: center; margin-bottom: 4px; font-weight: 600;">
                            <span style="margin-right: 6px;">ℹ️</span>
                            <span>注意</span>
                        </div>
                        <div style="line-height: 1.3;">这是一条重要的提示信息</div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">警告</span>
                    <span class="tag">提示</span>
                    <span class="tag">通知</span>
                </div>
            </div>
        </div>

        <!-- 第五行：卡片组件 & 引用组件 -->
        <div class="component-row">
            <div class="component-item">
                <h3><a href="../card-widget/">CardWidget 卡片组件</a></h3>
                <p>卡片容器，用于组织和展示相关信息</p>
                <div class="component-preview">
                    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 8px; padding: 16px; margin: 16px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                        <div style="display: flex; align-items: center; margin-bottom: 8px;">
                            <span style="margin-right: 8px; font-size: 16px;">📊</span>
                            <h4 style="font-size: 14px; font-weight: 600; color: #323130; margin: 0;">数据统计</h4>
                        </div>
                        <div style="font-size: 12px; color: #605e5c; line-height: 1.4;">
                            本月新增用户 1,234 人，同比增长 15.8%
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">卡片</span>
                    <span class="tag">容器</span>
                    <span class="tag">信息</span>
                </div>
            </div>
            <div class="component-item">
                <h3><a href="../quote-widget/">QuoteWidget 引用组件</a></h3>
                <p>展示引用内容，支持作者和来源信息</p>
                <div class="component-preview">
                    <div style="border-left: 4px solid #0078d4; padding: 12px 16px; margin: 16px 0; background: #f8f9fa; border-radius: 0 4px 4px 0;">
                        <div style="font-style: italic; color: #323130; font-size: 12px; line-height: 1.4; margin-bottom: 8px;">
                            "优秀的代码是其自身最好的文档。"
                        </div>
                        <div style="font-size: 11px; color: #605e5c; text-align: right;">
                            — Steve McConnell
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">引用</span>
                    <span class="tag">文本</span>
                    <span class="tag">作者</span>
                </div>
            </div>
        </div>

        <!-- 第六行：按钮组件 & 列布局组件 -->
        <div class="component-row">
            <div class="component-item">
                <h3><a href="../button-widget/">ButtonWidget 按钮组件</a></h3>
                <p>创建可点击的按钮，支持多种样式和邮件客户端兼容</p>
                <div class="component-preview">
                    <div style="text-align: center; margin: 16px 0;">
                        <a href="#" style="display: inline-block; background: #3b82f6; color: #ffffff; padding: 12px 24px; text-decoration: none; border-radius: 6px; font-weight: 600; font-size: 14px; border: none; cursor: pointer;">
                            立即开始
                        </a>
                        <div style="margin-top: 12px;">
                            <a href="#" style="display: inline-block; background: #22c55e; color: #ffffff; padding: 10px 20px; text-decoration: none; border-radius: 6px; font-weight: 500; font-size: 12px; margin: 0 4px;">
                                购买
                            </a>
                            <a href="#" style="display: inline-block; background: #6b7280; color: #ffffff; padding: 10px 20px; text-decoration: none; border-radius: 6px; font-weight: 500; font-size: 12px; margin: 0 4px;">
                                了解更多
                            </a>
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">按钮</span>
                    <span class="tag">链接</span>
                    <span class="tag">交互</span>
                </div>
            </div>
            <div class="component-item">
                <h3><a href="../column-widget/">ColumnWidget 列布局组件</a></h3>
                <p>多列布局管理器，支持响应式列布局</p>
                <div class="component-preview">
                    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0;">
                        <div style="display: flex; gap: 8px;">
                            <div style="flex: 1; background: #f8f9fa; padding: 8px; border-radius: 4px; text-align: center; font-size: 11px; color: #605e5c;">
                                列 1
                            </div>
                            <div style="flex: 1; background: #f8f9fa; padding: 8px; border-radius: 4px; text-align: center; font-size: 11px; color: #605e5c;">
                                列 2
                            </div>
                            <div style="flex: 1; background: #f8f9fa; padding: 8px; border-radius: 4px; text-align: center; font-size: 11px; color: #605e5c;">
                                列 3
                            </div>
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">布局</span>
                    <span class="tag">多列</span>
                    <span class="tag">响应式</span>
                </div>
            </div>
        </div>

        <!-- 第七行：清单组件 & 日志组件 -->
        <div class="component-row">
            <div class="component-item">
                <h3><a href="../checklist-widget/">ChecklistWidget 清单组件</a></h3>
                <p>创建任务清单和待办事项，支持多种状态和进度统计</p>
                <div class="component-preview">
                    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0;">
                        <h4 style="color: #323130; margin-bottom: 12px; font-size: 14px; font-weight: 600;">项目进度清单</h4>
                        <div style="background: #f8f9fa; border: 1px solid #e9ecef; border-radius: 4px; padding: 8px; margin-bottom: 12px; font-size: 12px;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                                <span style="color: #605e5c; font-weight: 500;">完成进度</span>
                                <span style="color: #323130; font-weight: 600;">2/3 (66.7%)</span>
                            </div>
                            <div style="width: 100%; height: 6px; background: #e1dfdd; border-radius: 3px; overflow: hidden;">
                                <div style="width: 66.7%; height: 100%; background: #ff8c00; border-radius: 3px;"></div>
                            </div>
                        </div>
                        <div style="font-size: 12px;">
                            <div style="display: flex; align-items: center; padding: 4px 0; margin-bottom: 3px;">
                                <div style="width: 14px; height: 14px; border: 2px solid #107c10; border-radius: 2px; margin-right: 8px; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 600; color: #ffffff; background: #107c10;">✓</div>
                                <div style="flex: 1; color: #8e8e93; text-decoration: line-through;">需求分析</div>
                                <div style="color: #107c10; font-size: 10px; font-weight: 600;">完成</div>
                            </div>
                            <div style="display: flex; align-items: center; padding: 4px 0; margin-bottom: 3px;">
                                <div style="width: 14px; height: 14px; border: 2px solid #107c10; border-radius: 2px; margin-right: 8px; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 600; color: #ffffff; background: #107c10;">✓</div>
                                <div style="flex: 1; color: #8e8e93; text-decoration: line-through;">设计评审</div>
                                <div style="color: #107c10; font-size: 10px; font-weight: 600;">完成</div>
                            </div>
                            <div style="display: flex; align-items: center; padding: 4px 0;">
                                <div style="width: 14px; height: 14px; border: 2px solid #8e8e93; border-radius: 2px; margin-right: 8px; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 600; color: #8e8e93;">○</div>
                                <div style="flex: 1; color: #323130; font-weight: 500;">开发实施</div>
                                <div style="color: #8e8e93; font-size: 10px; font-weight: 600;">待办</div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">清单</span>
                    <span class="tag">进度</span>
                    <span class="tag">任务</span>
                </div>
            </div>
            <div class="component-item">
                <h3><a href="../log-widget/">LogWidget 日志组件</a></h3>
                <p>展示日志信息，支持不同级别的日志显示</p>
                <div class="component-preview">
                    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0;">
                        <div style="font-family: 'Courier New', monospace; font-size: 11px;">
                            <div style="margin: 2px 0; color: #107c10;">[INFO] 系统启动成功</div>
                            <div style="margin: 2px 0; color: #ff8c00;">[WARN] 磁盘空间不足</div>
                            <div style="margin: 2px 0; color: #d13438;">[ERROR] 连接失败</div>
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">日志</span>
                    <span class="tag">监控</span>
                    <span class="tag">调试</span>
                </div>
            </div>
        </div>

        <!-- 第八行：分隔符组件 & 时间线组件 -->
        <div class="component-row">
            <div class="component-item">
                <h3><a href="../separator-widget/">SeparatorWidget 分隔符组件</a></h3>
                <p>创建视觉分隔线，支持多种样式，用于分割邮件内容区块</p>
                <div class="component-preview">
                    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0;">
                        <div style="text-align: center;">
                            <div style="font-size: 11px; color: #605e5c; margin-bottom: 8px;">实线分隔符</div>
                            <div style="width: 80%; height: 0; border-top: 2px solid #0078d4; margin: 8px auto;"></div>
                            <div style="font-size: 11px; color: #605e5c; margin: 8px 0;">虚线分隔符</div>
                            <div style="width: 80%; height: 0; border-top: 2px dashed #ff8c00; margin: 8px auto;"></div>
                            <div style="font-size: 11px; color: #605e5c; margin: 8px 0;">点线分隔符</div>
                            <div style="width: 80%; height: 0; border-top: 2px dotted #107c10; margin: 8px auto;"></div>
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">分隔</span>
                    <span class="tag">布局</span>
                    <span class="tag">分割</span>
                </div>
            </div>
            <div class="component-item">
                <h3><a href="../timeline-widget/">TimelineWidget 时间线组件</a></h3>
                <p>展示时间序列事件，支持状态标记和时间戳显示</p>
                <div class="component-preview">
                    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0;">
                        <h4 style="color: #323130; margin-bottom: 12px; font-size: 14px; font-weight: 600;">项目进展</h4>
                        <div style="position: relative; padding-left: 24px;">
                            <div style="position: absolute; left: 8px; top: 0; bottom: 0; width: 2px; background: #e1dfdd;"></div>
                            <div style="margin-bottom: 12px; position: relative; font-size: 12px;">
                                <div style="position: absolute; left: -20px; top: 2px; width: 12px; height: 12px; border-radius: 50%; background: #107c10; border: 2px solid #ffffff; box-shadow: 0 0 0 2px #107c10;"></div>
                                <div style="font-weight: 600; color: #323130; margin-bottom: 2px;">项目启动</div>
                                <div style="color: #605e5c; font-size: 11px;">项目正式开始</div>
                            </div>
                            <div style="margin-bottom: 12px; position: relative; font-size: 12px;">
                                <div style="position: absolute; left: -20px; top: 2px; width: 12px; height: 12px; border-radius: 50%; background: #0078d4; border: 2px solid #ffffff; box-shadow: 0 0 0 2px #0078d4;"></div>
                                <div style="font-weight: 600; color: #323130; margin-bottom: 2px;">需求分析</div>
                                <div style="color: #605e5c; font-size: 11px;">完成需求调研</div>
                            </div>
                            <div style="position: relative; font-size: 12px;">
                                <div style="position: absolute; left: -20px; top: 2px; width: 12px; height: 12px; border-radius: 50%; background: #8e8e93; border: 2px solid #ffffff; box-shadow: 0 0 0 2px #8e8e93;"></div>
                                <div style="font-weight: 600; color: #323130; margin-bottom: 2px;">开发实现</div>
                                <div style="color: #605e5c; font-size: 11px;">代码开发中</div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">时间线</span>
                    <span class="tag">事件</span>
                    <span class="tag">进度</span>
                </div>
            </div>
        </div>

        <!-- 第九行：指标组件 -->
        <div class="component-row">
            <div class="component-item">
                <h3><a href="../metric-widget/">MetricWidget 指标组件</a></h3>
                <p>展示关键数据指标，支持趋势分析和多种布局</p>
                <div class="component-preview">
                    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0;">
                        <h4 style="color: #323130; margin-bottom: 12px; font-size: 14px; font-weight: 600; text-align: center;">核心指标</h4>
                        <div style="display: flex; gap: 12px; justify-content: space-around;">
                            <div style="text-align: center; background: #f3f9f1; border: 1px solid #c8e6c5; border-radius: 6px; padding: 12px; flex: 1;">
                                <div style="font-size: 18px; font-weight: 700; color: #107c10; margin-bottom: 4px;">12K<span style="font-size: 12px; color: #8e8e93;">人</span></div>
                                <div style="font-size: 10px; font-weight: 500; color: #605e5c; text-transform: uppercase; margin-bottom: 6px;">活跃用户</div>
                                <div style="font-size: 10px; font-weight: 600; color: #107c10; display: flex; align-items: center; justify-content: center;">
                                    <span style="margin-right: 2px;">↗</span>
                                    <span>+15.6%</span>
                                </div>
                            </div>
                            <div style="text-align: center; background: #fff9f0; border: 1px solid #ffd6a5; border-radius: 6px; padding: 12px; flex: 1;">
                                <div style="font-size: 18px; font-weight: 700; color: #ff8c00; margin-bottom: 4px;">¥1.2M</div>
                                <div style="font-size: 10px; font-weight: 500; color: #605e5c; text-transform: uppercase; margin-bottom: 6px;">月收入</div>
                                <div style="font-size: 10px; font-weight: 600; color: #ff8c00; display: flex; align-items: center; justify-content: center;">
                                    <span style="margin-right: 2px;">→</span>
                                    <span>+8.2%</span>
                                </div>
                            </div>
                            <div style="text-align: center; background: #f0f6ff; border: 1px solid #a5c8f0; border-radius: 6px; padding: 12px; flex: 1;">
                                <div style="font-size: 18px; font-weight: 700; color: #0078d4; margin-bottom: 4px;">3.2<span style="font-size: 12px; color: #8e8e93;">%</span></div>
                                <div style="font-size: 10px; font-weight: 500; color: #605e5c; text-transform: uppercase; margin-bottom: 6px;">转化率</div>
                                <div style="font-size: 10px; font-weight: 600; color: #0078d4; display: flex; align-items: center; justify-content: center;">
                                    <span style="margin-right: 2px;">●</span>
                                    <span>+0.3%</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">指标</span>
                    <span class="tag">KPI</span>
                    <span class="tag">趋势</span>
                </div>
            </div>
            <div class="component-item">
                <h3>更多组件</h3>
                <p>更多强大的组件正在开发中...</p>
                <div class="component-preview">
                    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0; text-align: center;">
                        <div style="color: #8e8e93; font-size: 14px; font-weight: 500; margin: 20px 0;">
                            🚧 敬请期待
                        </div>
                        <div style="color: #605e5c; font-size: 12px; line-height: 1.4;">
                            我们正在不断添加新的组件<br/>
                            为您提供更丰富的邮件内容
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">开发中</span>
                    <span class="tag">敬请期待</span>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
.main-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

.component-grid {
    display: flex;
    flex-direction: column;
    gap: 30px;
}

.component-row {
    display: flex;
    gap: 30px;
    justify-content: space-between;
}

.component-item {
    flex: 1;
    background: #ffffff;
    border: 1px solid #e1dfdd;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    transition: box-shadow 0.3s ease;
    height: 350px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.component-item:hover {
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
}

.component-item h3 {
    margin: 0 0 8px 0;
    font-size: 18px;
    font-weight: 600;
}

.component-item h3 a {
    color: #0078d4;
    text-decoration: none;
}

.component-item h3 a:hover {
    text-decoration: underline;
}

.component-item p {
    margin: 0 0 16px 0;
    color: #605e5c;
    font-size: 14px;
    line-height: 1.5;
}

.component-preview {
    margin: 16px 0;
    min-height: 120px;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    flex-grow: 1;
}

.component-preview > div {
    width: 90%;
    max-width: 100%;
}

.component-tags {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-top: auto;
    padding-top: 16px;
}

.tag {
    background: #f3f2f1;
    color: #323130;
    padding: 4px 8px;
    border-radius: 12px;
    font-size: 12px;
    font-weight: 500;
}

@media (max-width: 768px) {
    .component-row {
        flex-direction: column;
        gap: 20px;
    }
    
    .component-item {
        height: auto;
        min-height: 300px;
    }
    
    .main-content {
        padding: 16px;
    }
}
</style>

## 🎯 所有组件预览

![image-20250702215350732](https://271374667.github.io/picx-images-hosting/EmailWidget/PixPin_2025-07-12_10-02-42.7snhz8im11.webp)
