# 高级示例

本页面展示 EmailWidget 的高级功能和自定义扩展，包括自定义组件、主题系统、性能优化等深入应用。

## 自定义组件开发

### 创建自定义 Widget 组件

```python
from email_widget.core.base import BaseWidget
from email_widget.core.enums import TextAlign
from email_widget.core.config import EmailConfig
from email_widget import Email

class MetricCardWidget(BaseWidget):
    """自定义指标卡片组件"""
    
    def __init__(self):
        super().__init__()
        self._title = ""
        self._value = ""
        self._change = 0.0
        self._change_label = ""
        self._icon = "📊"
        self._color_scheme = "primary"
    
    def set_title(self, title: str) -> 'MetricCardWidget':
        """设置卡片标题"""
        self._title = title
        return self
    
    def set_value(self, value: str) -> 'MetricCardWidget':
        """设置主要数值"""
        self._value = value
        return self
    
    def set_change(self, change: float, label: str = "") -> 'MetricCardWidget':
        """设置变化值和标签"""
        self._change = change
        self._change_label = label or f"{change:+.1f}%"
        return self
    
    def set_icon(self, icon: str) -> 'MetricCardWidget':
        """设置图标"""
        self._icon = icon
        return self
    
    def set_color_scheme(self, scheme: str) -> 'MetricCardWidget':
        """设置颜色方案: primary, success, warning, danger"""
        self._color_scheme = scheme
        return self
    
    def _get_color_styles(self) -> dict:
        """获取颜色样式"""
        schemes = {
            'primary': {'bg': '#3498db', 'text': '#ffffff', 'accent': '#2980b9'},
            'success': {'bg': '#2ecc71', 'text': '#ffffff', 'accent': '#27ae60'},
            'warning': {'bg': '#f39c12', 'text': '#ffffff', 'accent': '#e67e22'},
            'danger': {'bg': '#e74c3c', 'text': '#ffffff', 'accent': '#c0392b'}
        }
        return schemes.get(self._color_scheme, schemes['primary'])
    
    def render(self) -> str:
        """渲染组件HTML"""
        colors = self._get_color_styles()
        
        # 变化指标的颜色
        change_color = "#27ae60" if self._change >= 0 else "#e74c3c"
        change_arrow = "↗" if self._change >= 0 else "↘"
        
        return f"""
        <div style="
            background: linear-gradient(135deg, {colors['bg']}, {colors['accent']});
            color: {colors['text']};
            padding: 20px;
            margin: 10px 0;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        ">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <span style="font-size: 24px; margin-right: 10px;">{self._icon}</span>
                <h3 style="margin: 0; font-size: 16px; font-weight: 600; opacity: 0.9;">
                    {self._title}
                </h3>
            </div>
            
            <div style="font-size: 32px; font-weight: 700; margin-bottom: 8px;">
                {self._value}
            </div>
            
            <div style="display: flex; align-items: center; font-size: 14px;">
                <span style="color: {change_color}; font-weight: 600; margin-right: 5px;">
                    {change_arrow} {self._change_label}
                </span>
                <span style="opacity: 0.8;">较上期</span>
            </div>
        </div>
        """

# 使用自定义组件
email = Email("自定义组件演示")

email.add_title("🛠️ 自定义 MetricCard 组件演示", TextType.TITLE_LARGE)

# 创建多个指标卡片
metrics = [
    ("月度收入", "¥1,250,000", 15.8, "primary", "💰"),
    ("新增用户", "2,847", 23.5, "success", "👥"),
    ("转化率", "3.2%", -2.1, "warning", "📈"),
    ("退款率", "1.8%", -5.4, "success", "✅")
]

for title, value, change, scheme, icon in metrics:
    metric_card = MetricCardWidget()
    metric_card.set_title(title) \
               .set_value(value) \
               .set_change(change) \
               .set_color_scheme(scheme) \
               .set_icon(icon)
    
    email.add_widget(metric_card)

email.export_html("custom_components_demo.html")
print("✅ 自定义组件演示已生成：custom_components_demo.html")
```

--8<-- "examples/assets/advanced_html/商务_theme_demo.html"

**自定义组件特点：**
- 继承 BaseWidget 基类
- 支持链式调用
- 自定义样式和布局
- 可复用的业务组件

---

## 主题系统扩展

### 自定义主题和样式

```python
from email_widget import Email, TextWidget, TableWidget
from email_widget.core.config import EmailConfig
from email_widget.core.enums import TextType

class DarkThemeConfig(EmailConfig):
    """深色主题配置"""
    
    @classmethod
    def get_primary_color(cls) -> str:
        return "#1a1a1a"
    
    @classmethod
    def get_background_color(cls) -> str:
        return "#2d2d2d"
    
    @classmethod
    def get_text_color(cls) -> str:
        return "#ffffff"
    
    @classmethod
    def get_accent_color(cls) -> str:
        return "#64ffda"
    
    @classmethod
    def get_border_color(cls) -> str:
        return "#404040"

class BusinessThemeConfig(EmailConfig):
    """商务主题配置"""
    
    @classmethod
    def get_primary_color(cls) -> str:
        return "#2c3e50"
    
    @classmethod
    def get_secondary_color(cls) -> str:
        return "#34495e"
    
    @classmethod
    def get_accent_color(cls) -> str:
        return "#3498db"
    
    @classmethod
    def get_success_color(cls) -> str:
        return "#27ae60"

class ThemedWidget(BaseWidget):
    """支持主题的自定义组件"""
    
    def __init__(self, theme_config=None):
        super().__init__()
        self._theme_config = theme_config or EmailConfig
        self._content = ""
        self._widget_type = "info"
    
    def set_content(self, content: str) -> 'ThemedWidget':
        self._content = content
        return self
    
    def set_type(self, widget_type: str) -> 'ThemedWidget':
        """设置组件类型: info, success, warning, danger"""
        self._widget_type = widget_type
        return self
    
    def render(self) -> str:
        # 根据主题配置获取颜色
        theme_colors = {
            'info': self._theme_config.get_primary_color(),
            'success': self._theme_config.get_success_color(),
            'warning': getattr(self._theme_config, 'get_warning_color', lambda: '#f39c12')(),
            'danger': getattr(self._theme_config, 'get_danger_color', lambda: '#e74c3c')()
        }
        
        bg_color = self._theme_config.get_background_color()
        text_color = self._theme_config.get_text_color()
        border_color = theme_colors.get(self._widget_type, self._theme_config.get_primary_color())
        
        return f"""
        <div style="
            background-color: {bg_color};
            color: {text_color};
            border-left: 4px solid {border_color};
            padding: 15px;
            margin: 10px 0;
            border-radius: 4px;
            font-family: Arial, sans-serif;
        ">
            {self._content}
        </div>
        """

# 主题演示
def create_themed_report(theme_config, theme_name):
    """创建指定主题的报告"""
    email = Email(f"{theme_name}主题演示")
    
    # 设置邮件的主题配置
    email._config = theme_config
    
    email.add_title(f"🎨 {theme_name}主题演示", TextType.TITLE_LARGE)
    
    # 使用主题化组件
    themed_widgets = [
        ("信息提示", "这是一个信息类型的提示框", "info"),
        ("成功消息", "操作已成功完成", "success"),
        ("警告信息", "请注意检查相关设置", "warning"),
        ("错误提示", "发生了一个错误，请重试", "danger")
    ]
    
    for title, content, widget_type in themed_widgets:
        email.add_text(title, type=TextType.SECTION_H3)
        
        themed_widget = ThemedWidget(theme_config)
        themed_widget.set_content(content).set_type(widget_type)
        email.add_widget(themed_widget)
    
    # 创建主题化表格
    table = TableWidget()
    table.set_headers(["功能", "状态", "备注"])
    table.add_row(["用户登录", "✅ 正常", "登录成功率 98.5%"])
    table.add_row(["数据同步", "🔄 处理中", "预计5分钟完成"])
    table.add_row(["邮件发送", "❌ 异常", "SMTP服务器连接失败"])
    
    # 应用主题样式到表格
    table._theme_config = theme_config
    email.add_widget(table)
    
    return email

# 创建不同主题的报告
themes = [
    (EmailConfig, "默认"),
    (DarkThemeConfig, "深色"),
    (BusinessThemeConfig, "商务")
]

for theme_config, theme_name in themes:
    email = create_themed_report(theme_config, theme_name)
    email.export_html(f"{theme_name.lower()}_theme_demo.html")
print(f"✅ {theme_name}主题演示已生成")
```

--8<-- "examples/assets/advanced_html/默认_theme_demo.html"
--8<-- "examples/assets/advanced_html/深色_theme_demo.html"
--8<-- "examples/assets/advanced_html/商务_theme_demo.html"
```

**主题系统特点：**
- 可扩展的配置系统
- 主题化组件支持
- 一致的视觉风格
- 易于切换和定制

---

## 模板引擎扩展

### 自定义模板和过滤器

```python
from jinja2 import Environment, BaseLoader
from email_widget.core.template_engine import TemplateEngine
from email_widget import Email
import re

class CustomTemplateEngine(TemplateEngine):
    """扩展的模板引擎"""
    
    def __init__(self):
        super().__init__()
        # 添加自定义过滤器
        self._env.filters.update({
            'currency': self._currency_filter,
            'percentage': self._percentage_filter,
            'truncate_smart': self._smart_truncate_filter,
            'highlight': self._highlight_filter
        })
    
    def _currency_filter(self, value, currency='¥'):
        """货币格式化过滤器"""
        try:
            num_value = float(value)
            return f"{currency}{num_value:,.2f}"
        except (ValueError, TypeError):
            return str(value)
    
    def _percentage_filter(self, value, decimals=1):
        """百分比格式化过滤器"""
        try:
            num_value = float(value)
            return f"{num_value:.{decimals}f}%"
        except (ValueError, TypeError):
            return str(value)
    
    def _smart_truncate_filter(self, text, length=50, suffix='...'):
        """智能截断过滤器，在单词边界截断"""
        if len(text) <= length:
            return text
        
        truncated = text[:length]
        # 找到最后一个空格位置
        last_space = truncated.rfind(' ')
        if last_space > length * 0.7:  # 如果空格位置合理
            truncated = truncated[:last_space]
        
        return truncated + suffix
    
    def _highlight_filter(self, text, keywords, css_class='highlight'):
        """关键词高亮过滤器"""
        if not keywords:
            return text
        
        if isinstance(keywords, str):
            keywords = [keywords]
        
        highlighted_text = text
        for keyword in keywords:
            pattern = re.compile(re.escape(keyword), re.IGNORECASE)
            highlighted_text = pattern.sub(
                f'<span class="{css_class}" style="background-color: #ffeb3b; padding: 2px 4px;">{keyword}</span>',
                highlighted_text
            )
        
        return highlighted_text

class AdvancedReportWidget(BaseWidget):
    """使用高级模板的报告组件"""
    
    def __init__(self):
        super().__init__()
        self._template_engine = CustomTemplateEngine()
        self._data = {}
        self._template_name = "default"
    
    def set_data(self, data: dict) -> 'AdvancedReportWidget':
        """设置模板数据"""
        self._data = data
        return self
    
    def set_template(self, template_name: str) -> 'AdvancedReportWidget':
        """设置模板名称"""
        self._template_name = template_name
        return self
    
    def render(self) -> str:
        """使用模板渲染组件"""
        # 定义不同的模板
        templates = {
            'sales_summary': """
            <div style="border: 1px solid #ddd; padding: 20px; margin: 10px 0; border-radius: 8px;">
                <h3 style="color: #2c3e50; margin-top: 0;">{{ title }}</h3>
                
                <div style="display: flex; flex-wrap: wrap; gap: 15px; margin-bottom: 20px;">
                    {% for metric in metrics %}
                    <div style="
                        background: linear-gradient(135deg, #3498db, #2980b9);
                        color: white;
                        padding: 15px;
                        border-radius: 8px;
                        min-width: 150px;
                        text-align: center;
                    ">
                        <div style="font-size: 24px; font-weight: bold;">
                            {{ metric.value | currency if metric.type == 'currency' else metric.value }}
                        </div>
                        <div style="font-size: 14px; opacity: 0.9;">{{ metric.label }}</div>
                        {% if metric.change %}
                        <div style="font-size: 12px; margin-top: 5px;">
                            <span style="color: {{ '#4caf50' if metric.change > 0 else '#f44336' }};">
                                {{ metric.change | percentage }}
                            </span>
                        </div>
                        {% endif %}
                    </div>
                    {% endfor %}
                </div>
                
                {% if description %}
                <p style="color: #666; line-height: 1.6;">
                    {{ description | highlight(keywords) }}
                </p>
                {% endif %}
            </div>
            """,
            
            'data_table': """
            <div style="margin: 15px 0;">
                <h4 style="color: #2c3e50;">{{ title }}</h4>
                <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
                    <thead>
                        <tr style="background-color: #f8f9fa;">
                            {% for header in headers %}
                            <th style="padding: 12px; text-align: left; border-bottom: 2px solid #dee2e6;">
                                {{ header }}
                            </th>
                            {% endfor %}
                        </tr>
                    </thead>
                    <tbody>
                        {% for row in rows %}
                        <tr style="{{ 'background-color: #f8f9fa;' if loop.index % 2 == 0 else '' }}">
                            {% for cell in row %}
                            <td style="padding: 10px; border-bottom: 1px solid #dee2e6;">
                                {% if cell.type == 'currency' %}
                                    {{ cell.value | currency }}
                                {% elif cell.type == 'percentage' %}
                                    {{ cell.value | percentage }}
                                {% else %}
                                    {{ cell.value }}
                                {% endif %}
                            </td>
                            {% endfor %}
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
            """
        }
        
        template_content = templates.get(self._template_name, templates['sales_summary'])
        return self._template_engine.render_string(template_content, **self._data)

# 使用高级模板组件
email = Email("高级模板演示")

email.add_title("🔧 高级模板引擎演示", TextType.TITLE_LARGE)

# 销售汇总模板示例
sales_data = {
    'title': '月度销售业绩汇总',
    'metrics': [
        {'label': '总销售额', 'value': 1250000, 'type': 'currency', 'change': 15.8},
        {'label': '新客户数', 'value': '2,847', 'change': 23.5},
        {'label': '客单价', 'value': 438.5, 'type': 'currency', 'change': -2.1},
        {'label': '转化率', 'value': 3.2, 'type': 'percentage', 'change': 0.8}
    ],
    'description': '本月销售业绩表现优秀，总销售额创新高。新客户获取效果显著，但需要关注客单价的下降趋势。',
    'keywords': ['销售额', '新客户', '客单价']
}

sales_widget = AdvancedReportWidget()
sales_widget.set_template('sales_summary').set_data(sales_data)
email.add_widget(sales_widget)

# 数据表格模板示例
table_data = {
    'title': '产品销售明细',
    'headers': ['产品名称', '销售数量', '单价', '销售额', '增长率'],
    'rows': [
        [
            {'value': '智能手机A'},
            {'value': '1,200'},
            {'value': 2999, 'type': 'currency'},
            {'value': 3598800, 'type': 'currency'},
            {'value': 15.8, 'type': 'percentage'}
        ],
        [
            {'value': '平板电脑B'},
            {'value': '800'},
            {'value': 1999, 'type': 'currency'},
            {'value': 1599200, 'type': 'currency'},
            {'value': -5.2, 'type': 'percentage'}
        ]
    ]
}

table_widget = AdvancedReportWidget()
table_widget.set_template('data_table').set_data(table_data)
email.add_widget(table_widget)

email.export_html("advanced_template_demo.html")
print("✅ 高级模板演示已生成：advanced_template_demo.html")
```

--8<-- "examples/assets/advanced_html/advanced_template_demo.html"

**模板引擎扩展特点：**
- 自定义 Jinja2 过滤器
- 灵活的模板系统
- 数据驱动的渲染
- 可复用的模板组件

---

## 性能优化技巧

### 缓存和批量处理优化

```python
from functools import lru_cache
import time
from concurrent.futures import ThreadPoolExecutor
from email_widget import Email
from email_widget.core.cache import Cache

class PerformanceOptimizedEmail(Email):
    """性能优化的邮件类"""
    
    def __init__(self, title: str):
        super().__init__(title)
        self._cache = Cache(max_size=1000)
        self._batch_operations = []
        self._lazy_render = True
    
    @lru_cache(maxsize=128)
    def _get_cached_template(self, template_name: str) -> str:
        """缓存模板内容"""
        # 模拟从文件系统加载模板
        time.sleep(0.01)  # 模拟I/O延迟
        return f"<!-- Cached template: {template_name} -->"
    
    def add_widgets_batch(self, widgets: list, chunk_size: int = 10):
        """批量添加组件，提高性能"""
        def process_chunk(chunk):
            for widget in chunk:
                if hasattr(widget, 'validate'):
                    widget.validate()  # 验证组件
                self._widgets.append(widget)
        
        # 分块处理大量组件
        chunks = [widgets[i:i + chunk_size] for i in range(0, len(widgets), chunk_size)]
        
        with ThreadPoolExecutor(max_workers=4) as executor:
            executor.map(process_chunk, chunks)
    
    def render_async(self) -> str:
        """异步渲染，提高大型报告的性能"""
        def render_widget_chunk(widgets_chunk):
            return ''.join(widget.render() for widget in widgets_chunk)
        
        # 分块渲染组件
        chunk_size = 5
        widget_chunks = [self._widgets[i:i + chunk_size] 
                        for i in range(0, len(self._widgets), chunk_size)]
        
        with ThreadPoolExecutor(max_workers=4) as executor:
            rendered_chunks = list(executor.map(render_widget_chunk, widget_chunks))
        
        return self._template_engine.render('email_template.html', {
            'title': self._title,
            'widgets_html': ''.join(rendered_chunks)
        })

class LazyLoadWidget(BaseWidget):
    """延迟加载的组件"""
    
    def __init__(self):
        super().__init__()
        self._data_loader = None
        self._cache_key = None
        self._rendered_cache = None
    
    def set_data_loader(self, loader_func, cache_key: str = None):
        """设置数据加载函数"""
        self._data_loader = loader_func
        self._cache_key = cache_key or f"widget_{id(self)}"
        return self
    
    def render(self) -> str:
        """延迟渲染，只在需要时加载数据"""
        if self._rendered_cache is not None:
            return self._rendered_cache
        
        # 检查缓存
        if hasattr(self, '_cache') and self._cache_key:
            cached_result = self._cache.get(self._cache_key)
            if cached_result:
                return cached_result
        
        # 加载数据并渲染
        if self._data_loader:
            data = self._data_loader()
            rendered = self._render_with_data(data)
            
            # 缓存结果
            if hasattr(self, '_cache') and self._cache_key:
                self._cache.set(self._cache_key, rendered)
            
            self._rendered_cache = rendered
            return rendered
        
        return "<div><!-- LazyLoadWidget: No data loader --></div>"
    
    def _render_with_data(self, data) -> str:
        """使用数据渲染组件"""
        return f"<div>Loaded data: {len(data) if hasattr(data, '__len__') else 'N/A'} items</div>"

# 性能优化演示
def create_large_dataset():
    """模拟创建大数据集"""
    time.sleep(0.1)  # 模拟数据库查询延迟
    return [f"数据项 {i}" for i in range(1000)]

def optimize_performance_demo():
    """性能优化演示"""
    email = PerformanceOptimizedEmail("性能优化演示")
    
    email.add_title("⚡ 性能优化技术演示", TextType.TITLE_LARGE)
    
    # 演示延迟加载
    lazy_widget = LazyLoadWidget()
    lazy_widget.set_data_loader(create_large_dataset, "large_dataset_v1")
    email.add_widget(lazy_widget)
    
    # 演示批量组件添加
    batch_widgets = []
    for i in range(50):
        text_widget = TextWidget()
        text_widget.set_content(f"批量组件 {i + 1}")
        batch_widgets.append(text_widget)
    
    # 使用批量添加而非逐个添加
    start_time = time.time()
    email.add_widgets_batch(batch_widgets)
    batch_time = time.time() - start_time
    
    # 性能统计
    stats_text = f"""
    **性能优化结果：**
    
    ⚡ **批量处理**
    • 批量添加50个组件用时: {batch_time:.3f}秒
    • 预估比逐个添加快60%
    
    🔄 **缓存优化**
    • 模板缓存命中率: 95%+
    • 数据查询缓存生效
    
    📊 **内存优化**
    • 延迟加载减少初始内存占用
    • 组件渲染按需进行
    """
    
    email.add_text(stats_text.strip())
    
    return email

# 运行性能优化演示
optimized_email = optimize_performance_demo()
optimized_email.export_html("performance_optimization_demo.html")
print("✅ 性能优化演示已生成：performance_optimization_demo.html")
```

--8<-- "examples/assets/advanced_html/performance_optimization_demo.html"

**性能优化特点：**
- 多层缓存策略
- 批量处理优化
- 延迟加载机制
- 异步渲染支持

---

## 响应式布局

### 移动设备适配

```python
class ResponsiveLayoutWidget(BaseWidget):
    """响应式布局组件"""
    
    def __init__(self):
        super().__init__()
        self._columns = []
        self._mobile_stack = True
        self._gap = "20px"
    
    def add_column(self, widget, width_desktop="1fr", width_mobile="100%"):
        """添加列"""
        self._columns.append({
            'widget': widget,
            'width_desktop': width_desktop,
            'width_mobile': width_mobile
        })
        return self
    
    def set_mobile_stack(self, stack: bool):
        """设置移动端是否堆叠"""
        self._mobile_stack = stack
        return self
    
    def render(self) -> str:
        desktop_grid = " ".join(col['width_desktop'] for col in self._columns)
        
        # 生成响应式CSS
        responsive_css = f"""
        <style>
            .responsive-grid {{
                display: grid;
                grid-template-columns: {desktop_grid};
                gap: {self._gap};
                margin: 10px 0;
            }}
            
            @media (max-width: 600px) {{
                .responsive-grid {{
                    grid-template-columns: {"1fr" if self._mobile_stack else desktop_grid};
                }}
            }}
            
            .responsive-column {{
                min-width: 0; /* 防止内容溢出 */
            }}
        </style>
        """
        
        # 生成列内容
        columns_html = ""
        for col in self._columns:
            columns_html += f"""
            <div class="responsive-column">
                {col['widget'].render()}
            </div>
            """
        
        return f"""
        {responsive_css}
        <div class="responsive-grid">
            {columns_html}
        </div>
        """

# 响应式布局演示
email = Email("响应式布局演示")

email.add_title("📱 响应式布局演示", TextType.TITLE_LARGE)

# 创建响应式布局
responsive_layout = ResponsiveLayoutWidget()

# 左列：指标卡片
left_widget = MetricCardWidget()
left_widget.set_title("月度收入") \
          .set_value("¥1,250,000") \
          .set_change(15.8) \
          .set_color_scheme("primary")

# 右列：状态信息
right_widget = TextWidget()
right_widget.set_content("""
**系统状态摘要**

✅ 所有服务正常运行  
📊 数据同步完成  
🔒 安全检查通过  
📈 性能指标良好  
""")

# 添加到响应式布局
responsive_layout.add_column(left_widget, "2fr", "100%") \
                .add_column(right_widget, "1fr", "100%") \
                .set_mobile_stack(True)

email.add_widget(responsive_layout)

# 添加移动优化说明
mobile_info = """
**📱 移动端优化特性：**

• **自适应布局** - 桌面端多列，移动端单列
• **触摸友好** - 按钮和链接适合手指操作  
• **字体缩放** - 文字大小自动适配屏幕
• **图片响应** - 图片自动缩放适配容器
"""

email.add_text(mobile_info.strip())

email.export_html("responsive_layout_demo.html")
print("✅ 响应式布局演示已生成：responsive_layout_demo.html")
```

--8<-- "examples/assets/advanced_html/responsive_layout_demo.html"

**响应式特点：**
- CSS Grid 布局系统
- 移动端适配策略
- 触摸友好设计
- 自适应组件尺寸

---

## 学习总结

通过高级示例，您已经掌握了：

### 🛠️ 高级技能
- **自定义组件** - 继承 BaseWidget 创建专业组件
- **主题系统** - 可扩展的样式配置体系
- **模板引擎** - 自定义过滤器和模板系统
- **性能优化** - 缓存、批量处理、异步渲染

### 🎨 设计能力
- 组件化开发思维
- 主题驱动的设计系统
- 响应式布局适配
- 用户体验优化

### 💡 架构思维
- 可扩展的系统设计
- 性能优化策略
- 缓存和延迟加载
- 模块化和复用性

### 🚀 实战应用
- 企业级组件库开发
- 多主题邮件系统
- 高性能报告生成
- 移动端友好设计

继续学习 [实际应用](real-world.md)，看看这些技术在真实项目中的综合运用！
