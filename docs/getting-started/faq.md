# ❓ 常见问题

这里收集了EmailWidget使用过程中的常见问题和解决方案。如果你遇到的问题不在此列表中，欢迎在[GitHub Issues](https://github.com/271374667/SpiderDaily/issues)中提问。

## 🚀 安装相关

### ❓ 安装失败：权限不足

**问题**：在Windows或MacOS上安装时提示权限不足

**解决方案**：

=== "Windows"
    ```batch
    # 方案1：使用用户安装
    pip install --user EmailWidget
    
    # 方案2：以管理员身份运行命令提示符
    # 右键选择"以管理员身份运行"
    pip install EmailWidget
    
    # 方案3：使用虚拟环境
    python -m venv email_env
    email_env\Scripts\activate
    pip install EmailWidget
    ```

=== "MacOS/Linux"
    ```bash
    # 方案1：使用用户安装
    pip install --user EmailWidget
    
    # 方案2：使用sudo（不推荐）
    sudo pip install EmailWidget
    
    # 方案3：使用虚拟环境（推荐）
    python3 -m venv email_env
    source email_env/bin/activate
    pip install EmailWidget
    ```

### ❓ 安装慢或失败：网络问题

**问题**：下载速度慢或连接超时

**解决方案**：

```bash
# 使用国内镜像源
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple EmailWidget

# 或者设置默认镜像源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip install EmailWidget

# 其他镜像源选择
# 阿里云：https://mirrors.aliyun.com/pypi/simple/
# 中科大：https://pypi.mirrors.ustc.edu.cn/simple/
# 华为云：https://repo.huaweicloud.com/repository/pypi/simple/
```

### ❓ Python版本不兼容

**问题**：提示Python版本过低

**解决方案**：

```bash
# 检查当前Python版本
python --version

# EmailWidget需要Python 3.10+
# 如果版本过低，请升级Python或使用虚拟环境

# 使用特定Python版本创建虚拟环境
python3.10 -m venv email_env
source email_env/bin/activate  # Linux/MacOS
# 或 email_env\Scripts\activate  # Windows

pip install EmailWidget
```

## 📊 图表相关

### ❓ 图表中文字体显示为方块

**问题**：matplotlib图表中的中文显示为方块或乱码

**解决方案**：

EmailWidget会自动处理中文字体，但如果仍有问题：

```python
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 方案1：设置系统字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 方案2：检查可用字体
available_fonts = [f.name for f in font_manager.fontManager.ttflist]
chinese_fonts = [f for f in available_fonts if '微软雅黑' in f or 'SimHei' in f]
print("可用中文字体：", chinese_fonts)

# 方案3：使用EmailWidget的字体设置
from email_widget import Email
email = Email("测试")
email.config.set_font_family("Microsoft YaHei")  # 这会影响整个邮件
```

### ❓ 图表在不同设备上显示异常

**问题**：图表在其他设备或邮件客户端中显示不正常

**解决方案**：

```python
# 1. 设置固定DPI和尺寸
fig, ax = plt.subplots(figsize=(10, 6), dpi=100)

# 2. 使用Web安全字体
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']

# 3. 保存为高质量图片
plt.savefig('chart.png', dpi=150, bbox_inches='tight', 
            facecolor='white', edgecolor='none')

# 4. 在ChartWidget中设置
from email_widget.widgets import ChartWidget
chart = ChartWidget()
chart.set_chart(plt, dpi=150, format='png')
```

### ❓ 图表文件过大

**问题**：导出的HTML文件体积过大

**解决方案**：

```python
# 1. 降低图片质量
from email_widget.core.config import EmailConfig
config = EmailConfig()
config.set_image_quality(0.7)  # 0.1-1.0，默认0.8

# 2. 设置图表尺寸
fig, ax = plt.subplots(figsize=(8, 5))  # 减小尺寸

# 3. 使用SVG格式（适合简单图表）
chart = ChartWidget()
chart.set_chart(plt, format='svg')

# 4. 压缩图片
chart.set_image_compression(True)
```

## 📧 邮件相关

### ❓ 邮件在Outlook中显示异常

**问题**：生成的HTML在Outlook中布局错乱

**解决方案**：

```python
# 1. 启用Outlook兼容模式
from email_widget.core.config import EmailConfig
config = EmailConfig()
config.enable_outlook_compatibility(True)

# 2. 使用表格布局而非Flexbox
config.set_layout_mode("table")  # 默认是 "flexbox"

# 3. 避免使用复杂CSS
# Outlook对CSS支持有限，EmailWidget会自动处理大部分情况

# 4. 测试在不同版本的Outlook中的显示效果
email = Email("测试邮件")
email.config = config
# ... 添加内容
email.export_html("outlook_test.html")
```

### ❓ 邮件在移动设备上显示不佳

**问题**：在手机或平板上查看邮件时布局异常

**解决方案**：

```python
# 1. 启用响应式设计（默认已启用）
config = EmailConfig()
config.enable_responsive_design(True)

# 2. 设置移动端断点
config.set_mobile_breakpoint(768)  # 像素

# 3. 调整字体大小
config.set_mobile_font_scale(1.2)  # 移动端字体放大20%

# 4. 使用ColumnWidget进行布局
from email_widget.widgets import ColumnWidget
col = ColumnWidget()
col.set_columns([6, 6])  # 两列布局，在移动端自动变为单列
```

### ❓ 邮件大小超过限制

**问题**：生成的HTML文件太大，邮件客户端无法正常显示

**解决方案**：

```python
# 1. 启用HTML压缩
config = EmailConfig()
config.enable_minify_html(True)

# 2. 减少图片数量和质量
config.set_image_quality(0.6)
config.set_max_image_width(800)

# 3. 分页显示大量数据
from email_widget.widgets import TableWidget
table = TableWidget()
table.set_pagination(True)
table.set_page_size(20)  # 每页20条记录

# 4. 使用外部图片链接而非内嵌
# 将图片上传到图床，使用URL引用
```

## 🎨 样式相关

### ❓ 自定义样式不生效

**问题**：设置的CSS样式没有应用到组件上

**解决方案**：

```python
# 1. 检查CSS选择器优先级
widget = TextWidget()
widget.set_style("color: red !important;")  # 使用!important

# 2. 使用类选择器
widget.set_css_class("my-custom-class")

# 3. 在Email级别设置全局样式
email = Email("测试")
email.add_custom_css("""
.my-custom-class {
    color: red;
    font-weight: bold;
}
""")

# 4. 检查样式冲突
# EmailWidget有默认样式，可能与自定义样式冲突
config = EmailConfig()
config.disable_default_styles(True)  # 禁用默认样式
```

### ❓ 深色模式支持

**问题**：如何支持深色模式

**解决方案**：

```python
# 1. 启用深色模式检测
config = EmailConfig()
config.enable_dark_mode_detection(True)

# 2. 设置深色模式颜色
config.set_dark_mode_colors({
    'background': '#1a1a1a',
    'text': '#ffffff',
    'border': '#404040'
})

# 3. 为组件设置深色模式样式
widget = TextWidget()
widget.set_dark_mode_style("color: #ffffff; background: #2d2d2d;")

# 4. 使用CSS媒体查询
email.add_custom_css("""
@media (prefers-color-scheme: dark) {
    .widget {
        background-color: #2d2d2d;
        color: #ffffff;
    }
}
""")
```

## 🔧 性能相关

### ❓ 生成HTML速度慢

**问题**：包含大量数据时，生成HTML速度很慢

**解决方案**：

```python
# 1. 启用模板缓存
config = EmailConfig()
config.enable_template_cache(True)

# 2. 批量操作
# 避免逐个添加Widget，使用批量方法
widgets = [TextWidget().set_content(f"内容{i}") for i in range(100)]
email.add_widgets(widgets)  # 批量添加

# 3. 使用生成器处理大数据
def create_table_rows():
    for i in range(1000):
        yield [f"数据{i}", f"值{i}"]

table = TableWidget()
table.set_headers(["列1", "列2"])
table.add_rows_from_generator(create_table_rows())

# 4. 延迟渲染
email.set_lazy_rendering(True)  # 按需渲染组件
```

### ❓ 内存占用过高

**问题**：处理大量数据时内存占用过高

**解决方案**：

```python
# 1. 使用数据流处理
import pandas as pd
from email_widget.widgets import TableWidget

# 分块读取大文件
for chunk in pd.read_csv('large_file.csv', chunksize=1000):
    table = TableWidget()
    table.set_data_from_dataframe(chunk)
    email.add_widget(table)

# 2. 及时清理资源
matplotlib.pyplot.close('all')  # 关闭matplotlib图形
del large_dataframe  # 删除大对象

# 3. 使用内存映射
import numpy as np
data = np.memmap('large_data.dat', dtype='float32', mode='r')

# 4. 设置内存限制
config = EmailConfig()
config.set_memory_limit(512)  # MB
```

## 🐛 调试相关

### ❓ 如何调试模板渲染问题

**问题**：自定义模板不能正确渲染

**解决方案**：

```python
# 1. 启用调试模式
import logging
logging.basicConfig(level=logging.DEBUG)

from email_widget.core.logger import logger
logger.set_level("DEBUG")

# 2. 检查模板变量
widget = TextWidget()
context = widget.get_template_context()
print("模板上下文：", context)

# 3. 手动渲染模板
from email_widget.core.template_engine import TemplateEngine
engine = TemplateEngine()
template = engine.get_template("text_widget.html")
html = template.render(**context)
print("渲染结果：", html)

# 4. 验证模板语法
try:
    email.export_html("test.html")
except Exception as e:
    print(f"渲染错误：{e}")
    import traceback
    traceback.print_exc()
```

### ❓ 如何查看详细错误信息

**问题**：程序出错但错误信息不够详细

**解决方案**：

```python
# 1. 启用详细日志
from email_widget.core.logger import logger
logger.enable_file_logging("email_widget.log")
logger.set_level("DEBUG")

# 2. 使用try-catch捕获详细错误
try:
    email = Email("测试")
    # ... 你的代码
    email.export_html("test.html")
except Exception as e:
    logger.error(f"邮件生成失败：{e}")
    import traceback
    traceback.print_exc()

# 3. 验证数据
widget = TextWidget()
widget.set_content("测试内容")
if not widget.validate():
    print("Widget验证失败：", widget.get_validation_errors())

# 4. 检查配置
config = EmailConfig()
print("配置验证：", config.validate())
```

## 🔗 集成相关

### ❓ 与Jupyter Notebook集成

**问题**：在Jupyter中使用EmailWidget的最佳实践

**解决方案**：

```python
# 1. 在Jupyter中预览HTML
from IPython.display import HTML, display

email = Email("Jupyter测试")
# ... 添加内容
html_content = email.export_str()
display(HTML(html_content))

# 2. 设置图表在线显示
%matplotlib inline
import matplotlib.pyplot as plt

# 3. 处理路径问题
import os
os.chdir('/path/to/your/project')  # 设置工作目录

# 4. 使用异步操作（适用于大数据）
import asyncio
async def generate_report():
    # 异步生成报告
    pass
```

### ❓ 与Pandas集成

**问题**：如何更好地处理Pandas数据

**解决方案**：

```python
import pandas as pd
from email_widget.widgets import TableWidget

# 1. 直接从DataFrame创建表格
df = pd.read_csv('data.csv')
table = TableWidget()
table.set_data_from_dataframe(df)

# 2. 处理大型DataFrame
# 分页显示
table.set_pagination(True)
table.set_page_size(50)

# 3. 数据预处理
df_clean = df.dropna()  # 删除空值
df_formatted = df_clean.round(2)  # 格式化数字
table.set_data_from_dataframe(df_formatted)

# 4. 添加数据摘要
summary = df.describe()
summary_table = TableWidget()
summary_table.set_title("数据摘要")
summary_table.set_data_from_dataframe(summary)
```

### ❓ 与Web框架集成

**问题**：如何在Flask/Django中使用

**解决方案**：

=== "Flask"
    ```python
    from flask import Flask, render_template_string
    from email_widget import Email, TextWidget
    
    app = Flask(__name__)
    
    @app.route('/report')
    def generate_report():
        email = Email("Web报告")
        email.add_widget(TextWidget().set_content("Web生成的报告"))
        
        html_content = email.export_str()
        return html_content
    
    # 或者作为模板变量
    @app.route('/report2')
    def generate_report2():
        email = Email("Web报告")
        html_content = email.export_str()
        return render_template_string("""
        <html>
        <body>
            {{ report_content|safe }}
        </body>
        </html>
        """, report_content=html_content)
    ```

=== "Django"
    ```python
    # views.py
    from django.http import HttpResponse
    from email_widget import Email, TextWidget
    
    def generate_report(request):
        email = Email("Django报告")
        email.add_widget(TextWidget().set_content("Django生成的报告"))
        
        html_content = email.export_str()
        return HttpResponse(html_content, content_type='text/html')
    
    # 或者使用模板
    from django.shortcuts import render
    
    def report_view(request):
        email = Email("Django报告")
        html_content = email.export_str()
        return render(request, 'report.html', {
            'report_content': html_content
        })
    ```

## 🆘 获取更多帮助

如果以上FAQ没有解决你的问题，可以通过以下方式获取帮助：

### 📖 文档资源
- [用户指南](../user-guide/index.md) - 详细使用教程
- [API参考](../api/index.md) - 完整API文档
- [示例代码](../examples/index.md) - 实际应用案例

### 🤝 社区支持
- [GitHub Issues](https://github.com/271374667/SpiderDaily/issues) - 问题报告和功能请求
- [GitHub Discussions](https://github.com/271374667/SpiderDaily/discussions) - 社区讨论
- [Bilibili视频](https://space.bilibili.com/282527875) - 视频教程

### 💡 问题反馈模板

在提交问题时，请提供以下信息：

```markdown
**环境信息**
- EmailWidget版本：
- Python版本：
- 操作系统：
- 相关依赖版本：

**问题描述**
[详细描述遇到的问题]

**复现步骤**
1. 第一步
2. 第二步
3. ...

**期望行为**
[描述期望的正确行为]

**实际行为**
[描述实际发生的情况]

**代码示例**
```python
# 最小复现代码
```

**错误信息**
```
[粘贴完整的错误堆栈]
```

**附加信息**
[任何其他相关信息]
```

---

!!! tip "💡 提示"
    
    大多数问题都可以通过仔细阅读文档和查看示例代码来解决。建议在提交问题前先搜索已有的Issues，可能有人已经遇到并解决了类似问题。 