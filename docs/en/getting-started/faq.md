# ❓ Frequently Asked Questions

This section collects common questions and solutions encountered while using EmailWidget. If your problem is not listed here, please feel free to ask in [GitHub Issues](https://github.com/271374667/EmailWidget/issues).

## 🚀 Installation Related

### ❓ Installation Failed: Insufficient Permissions

**Problem**: Permission denied when installing on Windows or MacOS

**Solution**:

=== "Windows"
    ```batch
    # Option 1: User installation
    pip install --user EmailWidget
    
    # Option 2: Run command prompt as administrator
    # Right-click and select "Run as administrator"
    pip install EmailWidget
    
    # Option 3: Use virtual environment
    python -m venv email_env
    email_env\Scripts\activate
    pip install EmailWidget
    ```

=== "MacOS/Linux"
    ```bash
    # Option 1: User installation
    pip install --user EmailWidget
    
    # Option 2: Use sudo (not recommended)
    sudo pip install EmailWidget
    
    # Option 3: Use virtual environment (recommended)
    python3 -m venv email_env
    source email_env/bin/activate
    pip install EmailWidget
    ```

### ❓ Slow Installation or Failure: Network Issues

**Problem**: Slow download speed or connection timeout

**Solution**:

```bash
# Use domestic mirror source
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple EmailWidget

# Or set default mirror source
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip install EmailWidget

# Other mirror source options
# Alibaba Cloud: https://mirrors.aliyun.com/pypi/simple/
# USTC: https://pypi.mirrors.ustc.edu.cn/simple/
# Huawei Cloud: https://repo.huaweicloud.com/repository/pypi/simple/
```

### ❓ Python Version Incompatibility

**Problem**: Python version too low error

**Solution**:

```bash
# Check current Python version
python --version

# EmailWidget requires Python 3.10+
# If version is too low, please upgrade Python or use virtual environment

# Create virtual environment with specific Python version
python3.10 -m venv email_env
source email_env/bin/activate  # Linux/MacOS
# or email_env\Scripts\activate  # Windows

pip install EmailWidget
```

## 📊 Chart Related

### ❓ Chinese Text in Charts Displays as Squares

**Problem**: Chinese text in matplotlib charts displays as squares or garbled characters

**Solution**:

EmailWidget automatically handles Chinese fonts, but if issues persist:

```python
import matplotlib.pyplot as plt
from matplotlib import font_manager

# Option 1: Set system fonts
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# Option 2: Check available fonts
available_fonts = [f.name for f in font_manager.fontManager.ttflist]
chinese_fonts = [f for f in available_fonts if 'YaHei' in f or 'SimHei' in f]
print("Available Chinese fonts:", chinese_fonts)

# Option 3: Use EmailWidget's font settings
from email_widget import Email
email = Email("Test")
email.config.set_font_family("Microsoft YaHei")  # This affects the entire email
```

## 🐛 Debugging Related

### ❓ How to Debug Template Rendering Issues

**Problem**: Custom templates don't render correctly

**Solution**:

```python
# 1. Enable debug mode
import logging
logging.basicConfig(level=logging.DEBUG)

from email_widget.core.logger import logger
logger.set_level("DEBUG")

# 2. Check template variables
widget = TextWidget()
context = widget.get_template_context()
print("Template context:", context)

# 3. Manually render template
from email_widget.core.template_engine import TemplateEngine
engine = TemplateEngine()
template = engine.get_template("text_widget.html")
html = template.render(**context)
print("Render result:", html)

# 4. Validate template syntax
try:
    email.export_html("test.html")
except Exception as e:
    print(f"Render error: {e}")
    import traceback
    traceback.print_exc()
```

## 🔗 Integration Related

### ❓ Integration with Jupyter Notebook

**Problem**: Best practices for using EmailWidget in Jupyter

**Solution**:

```python
# 1. Preview HTML in Jupyter
from IPython.display import HTML, display

email = Email("Jupyter Test")
# ... add content
html_content = email.export_str()
display(HTML(html_content))
```

### ❓ Integration with Pandas

**Problem**: How to better handle Pandas data

**Solution**:

```python
import pandas as pd
from email_widget.widgets import TableWidget

# 1. Create table directly from DataFrame
df = pd.read_csv('data.csv')
table = TableWidget()
table.set_data_from_dataframe(df)

# 3. Data preprocessing
df_clean = df.dropna()  # Remove null values
df_formatted = df_clean.round(2)  # Format numbers
table.set_data_from_dataframe(df_formatted)

# 4. Add data summary
summary = df.describe()
summary_table = TableWidget()
summary_table.set_title("Data Summary")
summary_table.set_data_from_dataframe(summary)
```

## 🆘 Get More Help

If the above FAQ doesn't solve your problem, you can get help through the following channels:

### 📖 Documentation Resources
- [User Guide](../user-guide/index.md) - Detailed usage tutorials
- [API Reference](../api/index.md) - Complete API documentation
- [Example Code](../examples/index.md) - Real-world use cases

### 🤝 Community Support
- [GitHub Issues](https://github.com/271374667/EmailWidget/issues) - Bug reports and feature requests
- [GitHub Discussions](https://github.com/271374667/EmailWidget/discussions) - Community discussions
- [Bilibili Videos](https://space.bilibili.com/282527875) - Video tutorials

### 💡 Issue Report Template

When submitting issues, please provide the following information:

```markdown
**Environment Information**
- EmailWidget Version:
- Python Version:
- Operating System:
- Related Dependency Versions:

**Problem Description**
[Detailed description of the problem encountered]

**Reproduction Steps**
1. First step
2. Second step
3. ...

**Expected Behavior**
[Describe the expected correct behavior]

**Actual Behavior**
[Describe what actually happened]

**Code Example**
```python
# Minimal reproduction code
```

**Error Information**
```
[Paste complete error stack trace]
```

**Additional Information**
[Any other relevant information]
```

---