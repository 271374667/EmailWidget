# ❓ 常见问题

这里收集了EmailWidget使用过程中的常见问题和解决方案。如果你遇到的问题不在此列表中，欢迎在[GitHub Issues](https://github.com/271374667/EmailWidget/issues)中提问。

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

## 🆘 获取更多帮助

如果以上FAQ没有解决你的问题，可以通过以下方式获取帮助：

### 📖 文档资源
- [用户指南](../user-guide/index.md) - 详细使用教程
- [API参考](../api/index.md) - 完整API文档
- [示例代码](../examples/index.md) - 实际应用案例

### 🤝 社区支持
- [GitHub Issues](https://github.com/271374667/EmailWidget/issues) - 问题报告和功能请求
- [GitHub Discussions](https://github.com/271374667/EmailWidget/discussions) - 社区讨论
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