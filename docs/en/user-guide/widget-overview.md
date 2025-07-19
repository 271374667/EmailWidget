# Widget Overview

EmailWidget provides a rich widget library that covers various common content types in emails. This page showcases all available widgets and their preview effects.

<div class="main-content">
    <div class="component-grid">
        <!-- First row: Text Widget & Table Widget -->
        <div class="component-row">
            <div class="component-item">
                <h3><a href="../text-widget/">TextWidget</a></h3>
                <p>Used to display various text content, supports multiple styles and formats</p>
                <div class="component-preview">
                    <div style="background: #f8f9fa; border: 1px solid #e9ecef; border-radius: 4px; padding: 16px; margin: 16px 0;">
                        <h2 style="color: #0078d4; text-align: center; margin: 0; font-size: 18px;">This is important text</h2>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">Title</span>
                    <span class="tag">Content</span>
                    <span class="tag">Section</span>
                </div>
            </div>
            <div class="component-item">
                <h3><a href="../table-widget/">TableWidget</a></h3>
                <p>Display structured data, supports headers, index columns, striped styles, etc.</p>
                <div class="component-preview">
                    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0;">
                        <table style="width: 100%; border-collapse: collapse; font-size: 12px;">
                            <thead>
                                <tr style="background: #f8f9fa;">
                                    <th style="padding: 8px; text-align: left; border-bottom: 2px solid #e9ecef; font-weight: 600;">Item</th>
                                    <th style="padding: 8px; text-align: left; border-bottom: 2px solid #e9ecef; font-weight: 600;">Status</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr style="background: #ffffff;">
                                    <td style="padding: 8px; border-bottom: 1px solid #e9ecef;">User Registration</td>
                                    <td style="padding: 8px; border-bottom: 1px solid #e9ecef; color: #107c10; font-weight: 600;">Normal</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">Data</span>
                    <span class="tag">Statistics</span>
                    <span class="tag">Status</span>
                </div>
            </div>
        </div>

        <!-- Second row: Image Widget & Chart Widget -->
        <div class="component-row">
            <div class="component-item">
                <h3><a href="../image-widget/">ImageWidget</a></h3>
                <p>Display image content, supports titles, descriptions, and various layout options</p>
                <div class="component-preview">
                    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0; text-align: center;">
                        <h4 style="color: #323130; margin-bottom: 8px; font-size: 14px;">Data Trend Chart</h4>
                        <div style="background: #f3f2f1; padding: 20px; border-radius: 4px; color: #605e5c; font-size: 12px;">
                            [Image Placeholder]
                        </div>
                        <p style="color: #605e5c; margin-top: 8px; font-size: 12px;">Shows user growth trend for the last 30 days</p>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">Image</span>
                    <span class="tag">Display</span>
                    <span class="tag">Description</span>
                </div>
            </div>
            <div class="component-item">
                <h3><a href="../chart-widget/">ChartWidget</a></h3>
                <p>Specifically designed for displaying charts, supports multiple chart types and data summaries</p>
                <div class="component-preview">
                    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0; text-align: center;">
                        <h4 style="color: #323130; margin-bottom: 8px; font-size: 14px;">Monthly Sales Statistics</h4>
                        <div style="background: #f8f9fa; padding: 30px; border-radius: 4px; border: 1px dashed #dee2e6; color: #6c757d; font-size: 12px;">
                            [Chart Placeholder]
                        </div>
                        <div style="font-size: 11px; color: #8e8e93; margin-top: 8px; padding-top: 8px; border-top: 1px solid #f3f2f1;">
                            Total Sales: ¥1,250,000
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">Chart</span>
                    <span class="tag">Data</span>
                    <span class="tag">Visualization</span>
                </div>
            </div>
        </div>

        <!-- Third row: Progress Widget & Circular Progress Widget -->
        <div class="component-row">
            <div class="component-item">
                <h3><a href="../progress-widget/">ProgressWidget</a></h3>
                <p>Display task or process completion progress, supports multiple themes</p>
                <div class="component-preview">
                    <div style="margin: 16px 0;">
                        <div style="font-size: 12px; font-weight: 600; color: #323130; margin-bottom: 8px;">Project Progress</div>
                        <div style="width: 100%; height: 16px; background: #e1dfdd; border-radius: 8px; overflow: hidden; position: relative;">
                            <div style="width: 75%; height: 100%; background: #107c10; border-radius: 8px;"></div>
                            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 10px; font-weight: 600; color: #ffffff;">75%</div>
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">Progress</span>
                    <span class="tag">Status</span>
                    <span class="tag">Percentage</span>
                </div>
            </div>
            <div class="component-item">
                <h3><a href="../circular-progress-widget/">CircularProgressWidget</a></h3>
                <p>Display progress in circular format, suitable for showing percentage data</p>
                <div class="component-preview">
                    <div style="text-align: center; margin: 16px 0;">
                        <div style="width: 80px; height: 80px; border-radius: 50%; background: conic-gradient(#0078d4 0deg, #0078d4 316.8deg, #e1dfdd 316.8deg); margin: 0 auto; display: flex; align-items: center; justify-content: center;">
                            <div style="width: 60px; height: 60px; background: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; color: #323130; font-size: 12px;">88%</div>
                        </div>
                        <div style="margin-top: 8px; font-size: 12px; color: #323130;">System Performance</div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">Circular</span>
                    <span class="tag">Progress</span>
                    <span class="tag">KPI</span>
                </div>
            </div>
        </div>

        <!-- Fourth row: Status Widget & Alert Widget -->
        <div class="component-row">
            <div class="component-item">
                <h3><a href="../status-widget/">StatusWidget</a></h3>
                <p>Display information for multiple status items, supports horizontal and vertical layouts</p>
                <div class="component-preview">
                    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0;">
                        <h4 style="font-size: 14px; font-weight: 600; color: #323130; margin-bottom: 8px;">System Status</h4>
                        <div style="margin: 4px 0; padding: 4px 0; border-bottom: 1px solid #f3f2f1; font-size: 12px;">
                            <div style="font-weight: 500; color: #605e5c;">CPU Usage</div>
                            <div style="color: #107c10; font-weight: 600;">45%</div>
                        </div>
                        <div style="margin: 4px 0; padding: 4px 0; font-size: 12px;">
                            <div style="font-weight: 500; color: #605e5c;">Memory Usage</div>
                            <div style="color: #ff8c00; font-weight: 600;">78%</div>
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">Status</span>
                    <span class="tag">Monitoring</span>
                    <span class="tag">System</span>
                </div>
            </div>
            <div class="component-item">
                <h3><a href="../alert-widget/">AlertWidget</a></h3>
                <p>Display various types of alert messages, supports GitHub-style alert boxes</p>
                <div class="component-preview">
                    <div style="background: #dbeafe; border: 1px solid #3b82f6; border-left: 4px solid #3b82f6; border-radius: 4px; padding: 12px; margin: 16px 0; color: #1e40af; font-size: 12px;">
                        <div style="display: flex; align-items: center; margin-bottom: 4px; font-weight: 600;">
                            <span style="margin-right: 6px;">ℹ️</span>
                            <span>Note</span>
                        </div>
                        <div style="line-height: 1.3;">This is an important notice</div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">Alert</span>
                    <span class="tag">Notice</span>
                    <span class="tag">Notification</span>
                </div>
            </div>
        </div>

        <!-- Fifth row: Card Widget & Quote Widget -->
        <div class="component-row">
            <div class="component-item">
                <h3><a href="../card-widget/">CardWidget</a></h3>
                <p>Card container for organizing and displaying related information</p>
                <div class="component-preview">
                    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 8px; padding: 16px; margin: 16px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                        <div style="display: flex; align-items: center; margin-bottom: 8px;">
                            <span style="margin-right: 8px; font-size: 16px;">📊</span>
                            <h4 style="font-size: 14px; font-weight: 600; color: #323130; margin: 0;">Data Statistics</h4>
                        </div>
                        <div style="font-size: 12px; color: #605e5c; line-height: 1.4;">
                            This month added 1,234 new users, up 15.8% year-over-year
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">Card</span>
                    <span class="tag">Container</span>
                    <span class="tag">Information</span>
                </div>
            </div>
            <div class="component-item">
                <h3><a href="../quote-widget/">QuoteWidget</a></h3>
                <p>Display quoted content, supports author and source information</p>
                <div class="component-preview">
                    <div style="border-left: 4px solid #0078d4; padding: 12px 16px; margin: 16px 0; background: #f8f9fa; border-radius: 0 4px 4px 0;">
                        <div style="font-style: italic; color: #323130; font-size: 12px; line-height: 1.4; margin-bottom: 8px;">
                            "Good code is its own best documentation."
                        </div>
                        <div style="font-size: 11px; color: #605e5c; text-align: right;">
                            — Steve McConnell
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">Quote</span>
                    <span class="tag">Text</span>
                    <span class="tag">Author</span>
                </div>
            </div>
        </div>

        <!-- Sixth row: Button Widget & Column Widget -->
        <div class="component-row">
            <div class="component-item">
                <h3><a href="../button-widget/">ButtonWidget</a></h3>
                <p>Create clickable buttons, supports multiple styles and email client compatibility</p>
                <div class="component-preview">
                    <div style="text-align: center; margin: 16px 0;">
                        <a href="#" style="display: inline-block; background: #3b82f6; color: #ffffff; padding: 12px 24px; text-decoration: none; border-radius: 6px; font-weight: 600; font-size: 14px; border: none; cursor: pointer;">
                            Get Started
                        </a>
                        <div style="margin-top: 12px;">
                            <a href="#" style="display: inline-block; background: #22c55e; color: #ffffff; padding: 10px 20px; text-decoration: none; border-radius: 6px; font-weight: 500; font-size: 12px; margin: 0 4px;">
                                Purchase
                            </a>
                            <a href="#" style="display: inline-block; background: #6b7280; color: #ffffff; padding: 10px 20px; text-decoration: none; border-radius: 6px; font-weight: 500; font-size: 12px; margin: 0 4px;">
                                Learn More
                            </a>
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">Button</span>
                    <span class="tag">Link</span>
                    <span class="tag">Interaction</span>
                </div>
            </div>
            <div class="component-item">
                <h3><a href="../column-widget/">ColumnWidget</a></h3>
                <p>Multi-column layout manager, supports responsive column layouts</p>
                <div class="component-preview">
                    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0;">
                        <div style="display: flex; gap: 8px;">
                            <div style="flex: 1; background: #f8f9fa; padding: 8px; border-radius: 4px; text-align: center; font-size: 11px; color: #605e5c;">
                                Column 1
                            </div>
                            <div style="flex: 1; background: #f8f9fa; padding: 8px; border-radius: 4px; text-align: center; font-size: 11px; color: #605e5c;">
                                Column 2
                            </div>
                            <div style="flex: 1; background: #f8f9fa; padding: 8px; border-radius: 4px; text-align: center; font-size: 11px; color: #605e5c;">
                                Column 3
                            </div>
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">Layout</span>
                    <span class="tag">Multi-column</span>
                    <span class="tag">Responsive</span>
                </div>
            </div>
        </div>

        <!-- Seventh row: Checklist Widget & Log Widget -->
        <div class="component-row">
            <div class="component-item">
                <h3><a href="../checklist-widget/">ChecklistWidget</a></h3>
                <p>Create task lists and to-do items, supports multiple statuses and progress statistics</p>
                <div class="component-preview">
                    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0;">
                        <h4 style="color: #323130; margin-bottom: 12px; font-size: 14px; font-weight: 600;">Project Progress Checklist</h4>
                        <div style="background: #f8f9fa; border: 1px solid #e9ecef; border-radius: 4px; padding: 8px; margin-bottom: 12px; font-size: 12px;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                                <span style="color: #605e5c; font-weight: 500;">Progress</span>
                                <span style="color: #323130; font-weight: 600;">2/3 (66.7%)</span>
                            </div>
                            <div style="width: 100%; height: 6px; background: #e1dfdd; border-radius: 3px; overflow: hidden;">
                                <div style="width: 66.7%; height: 100%; background: #ff8c00; border-radius: 3px;"></div>
                            </div>
                        </div>
                        <div style="font-size: 12px;">
                            <div style="display: flex; align-items: center; padding: 4px 0; margin-bottom: 3px;">
                                <div style="width: 14px; height: 14px; border: 2px solid #107c10; border-radius: 2px; margin-right: 8px; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 600; color: #ffffff; background: #107c10;">✓</div>
                                <div style="flex: 1; color: #8e8e93; text-decoration: line-through;">Requirements Analysis</div>
                                <div style="color: #107c10; font-size: 10px; font-weight: 600;">Complete</div>
                            </div>
                            <div style="display: flex; align-items: center; padding: 4px 0; margin-bottom: 3px;">
                                <div style="width: 14px; height: 14px; border: 2px solid #107c10; border-radius: 2px; margin-right: 8px; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 600; color: #ffffff; background: #107c10;">✓</div>
                                <div style="flex: 1; color: #8e8e93; text-decoration: line-through;">Design Review</div>
                                <div style="color: #107c10; font-size: 10px; font-weight: 600;">Complete</div>
                            </div>
                            <div style="display: flex; align-items: center; padding: 4px 0;">
                                <div style="width: 14px; height: 14px; border: 2px solid #8e8e93; border-radius: 2px; margin-right: 8px; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 600; color: #8e8e93;">○</div>
                                <div style="flex: 1; color: #323130; font-weight: 500;">Development Implementation</div>
                                <div style="color: #8e8e93; font-size: 10px; font-weight: 600;">To-do</div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">Checklist</span>
                    <span class="tag">Progress</span>
                    <span class="tag">Tasks</span>
                </div>
            </div>
            <div class="component-item">
                <h3><a href="../log-widget/">LogWidget</a></h3>
                <p>Display log information, supports different log levels</p>
                <div class="component-preview">
                    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0;">
                        <div style="font-family: 'Courier New', monospace; font-size: 11px;">
                            <div style="margin: 2px 0; color: #107c10;">[INFO] System started successfully</div>
                            <div style="margin: 2px 0; color: #ff8c00;">[WARN] Disk space low</div>
                            <div style="margin: 2px 0; color: #d13438;">[ERROR] Connection failed</div>
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">Log</span>
                    <span class="tag">Monitoring</span>
                    <span class="tag">Debug</span>
                </div>
            </div>
        </div>

        <!-- Eighth row: Separator Widget & Timeline Widget -->
        <div class="component-row">
            <div class="component-item">
                <h3><a href="../separator-widget/">SeparatorWidget</a></h3>
                <p>Create visual separators, supports multiple styles for dividing email content sections</p>
                <div class="component-preview">
                    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0;">
                        <div style="text-align: center;">
                            <div style="font-size: 11px; color: #605e5c; margin-bottom: 8px;">Solid Separator</div>
                            <div style="width: 80%; height: 0; border-top: 2px solid #0078d4; margin: 8px auto;"></div>
                            <div style="font-size: 11px; color: #605e5c; margin: 8px 0;">Dashed Separator</div>
                            <div style="width: 80%; height: 0; border-top: 2px dashed #ff8c00; margin: 8px auto;"></div>
                            <div style="font-size: 11px; color: #605e5c; margin: 8px 0;">Dotted Separator</div>
                            <div style="width: 80%; height: 0; border-top: 2px dotted #107c10; margin: 8px auto;"></div>
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">Separator</span>
                    <span class="tag">Layout</span>
                    <span class="tag">Division</span>
                </div>
            </div>
            <div class="component-item">
                <h3><a href="../timeline-widget/">TimelineWidget</a></h3>
                <p>Display time-series events, supports status markers and timestamp display</p>
                <div class="component-preview">
                    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0;">
                        <h4 style="color: #323130; margin-bottom: 12px; font-size: 14px; font-weight: 600;">Project Progress</h4>
                        <div style="position: relative; padding-left: 24px;">
                            <div style="position: absolute; left: 8px; top: 0; bottom: 0; width: 2px; background: #e1dfdd;"></div>
                            <div style="margin-bottom: 12px; position: relative; font-size: 12px;">
                                <div style="position: absolute; left: -20px; top: 2px; width: 12px; height: 12px; border-radius: 50%; background: #107c10; border: 2px solid #ffffff; box-shadow: 0 0 0 2px #107c10;"></div>
                                <div style="font-weight: 600; color: #323130; margin-bottom: 2px;">Project Launch</div>
                                <div style="color: #605e5c; font-size: 11px;">Project officially started</div>
                            </div>
                            <div style="margin-bottom: 12px; position: relative; font-size: 12px;">
                                <div style="position: absolute; left: -20px; top: 2px; width: 12px; height: 12px; border-radius: 50%; background: #0078d4; border: 2px solid #ffffff; box-shadow: 0 0 0 2px #0078d4;"></div>
                                <div style="font-weight: 600; color: #323130; margin-bottom: 2px;">Requirements Analysis</div>
                                <div style="color: #605e5c; font-size: 11px;">Requirements research completed</div>
                            </div>
                            <div style="position: relative; font-size: 12px;">
                                <div style="position: absolute; left: -20px; top: 2px; width: 12px; height: 12px; border-radius: 50%; background: #8e8e93; border: 2px solid #ffffff; box-shadow: 0 0 0 2px #8e8e93;"></div>
                                <div style="font-weight: 600; color: #323130; margin-bottom: 2px;">Development Implementation</div>
                                <div style="color: #605e5c; font-size: 11px;">Code development in progress</div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">Timeline</span>
                    <span class="tag">Events</span>
                    <span class="tag">Progress</span>
                </div>
            </div>
        </div>

        <!-- Ninth row: Metric Widget -->
        <div class="component-row">
            <div class="component-item">
                <h3><a href="../metric-widget/">MetricWidget</a></h3>
                <p>Display key data metrics, supports trend analysis and multiple layouts</p>
                <div class="component-preview">
                    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0;">
                        <h4 style="color: #323130; margin-bottom: 12px; font-size: 14px; font-weight: 600; text-align: center;">Key Metrics</h4>
                        <div style="display: flex; gap: 12px; justify-content: space-around;">
                            <div style="text-align: center; background: #f3f9f1; border: 1px solid #c8e6c5; border-radius: 6px; padding: 12px; flex: 1;">
                                <div style="font-size: 18px; font-weight: 700; color: #107c10; margin-bottom: 4px;">12K<span style="font-size: 12px; color: #8e8e93;">users</span></div>
                                <div style="font-size: 10px; font-weight: 500; color: #605e5c; text-transform: uppercase; margin-bottom: 6px;">Active Users</div>
                                <div style="font-size: 10px; font-weight: 600; color: #107c10; display: flex; align-items: center; justify-content: center;">
                                    <span style="margin-right: 2px;">↗</span>
                                    <span>+15.6%</span>
                                </div>
                            </div>
                            <div style="text-align: center; background: #fff9f0; border: 1px solid #ffd6a5; border-radius: 6px; padding: 12px; flex: 1;">
                                <div style="font-size: 18px; font-weight: 700; color: #ff8c00; margin-bottom: 4px;">¥1.2M</div>
                                <div style="font-size: 10px; font-weight: 500; color: #605e5c; text-transform: uppercase; margin-bottom: 6px;">Monthly Revenue</div>
                                <div style="font-size: 10px; font-weight: 600; color: #ff8c00; display: flex; align-items: center; justify-content: center;">
                                    <span style="margin-right: 2px;">→</span>
                                    <span>+8.2%</span>
                                </div>
                            </div>
                            <div style="text-align: center; background: #f0f6ff; border: 1px solid #a5c8f0; border-radius: 6px; padding: 12px; flex: 1;">
                                <div style="font-size: 18px; font-weight: 700; color: #0078d4; margin-bottom: 4px;">3.2<span style="font-size: 12px; color: #8e8e93;">%</span></div>
                                <div style="font-size: 10px; font-weight: 500; color: #605e5c; text-transform: uppercase; margin-bottom: 6px;">Conversion Rate</div>
                                <div style="font-size: 10px; font-weight: 600; color: #0078d4; display: flex; align-items: center; justify-content: center;">
                                    <span style="margin-right: 2px;">●</span>
                                    <span>+0.3%</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">Metrics</span>
                    <span class="tag">KPI</span>
                    <span class="tag">Trends</span>
                </div>
            </div>
            <div class="component-item">
                <h3>More Widgets</h3>
                <p>More powerful widgets are under development...</p>
                <div class="component-preview">
                    <div style="background: #ffffff; border: 1px solid #e1dfdd; border-radius: 4px; padding: 16px; margin: 16px 0; text-align: center;">
                        <div style="color: #8e8e93; font-size: 14px; font-weight: 500; margin: 20px 0;">
                            🚧 Coming Soon
                        </div>
                        <div style="color: #605e5c; font-size: 12px; line-height: 1.4;">
                            We are continuously adding new widgets<br/>
                            to provide you with richer email content
                        </div>
                    </div>
                </div>
                <div class="component-tags">
                    <span class="tag">In Development</span>
                    <span class="tag">Coming Soon</span>
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

## 🎯 All Widget Preview

![image-20250702215350732](https://271374667.github.io/picx-images-hosting/EmailWidget/PixPin_2025-07-12_10-02-42.7snhz8im11.webp)