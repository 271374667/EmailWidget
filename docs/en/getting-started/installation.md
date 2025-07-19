# 📦 Installation Guide

## System Requirements

!!! info "Environment Requirements"
    - **Python**: 3.10 or higher
    - **Operating System**: Windows, macOS, Linux
    - **Memory**: Recommended 512MB+ available memory

## Installation Methods

### 🚀 Install with pip (Recommended)

=== "Latest Stable Version"
    ```bash
    pip install EmailWidget
    ```

=== "Specific Version"
    ```bash
    pip install EmailWidget==0.1.0
    ```

=== "Upgrade to Latest"
    ```bash
    pip install EmailWidget -U
    ```

### 🔧 Install from Source

If you want to use the latest development version or participate in development:

```bash
# Clone repository
git clone https://github.com/271374667/EmailWidget.git
cd EmailWidget

# Install development dependencies
pip install -e ".[dev]"
```

## Verify Installation

After installation, you can verify the installation was successful in the following ways:

### 1. Import Test

```python
try:
    from email_widget import Email
    from email_widget.widgets import TextWidget
    print("✅ EmailWidget 安装成功！")
except ImportError as e:
    print(f"❌ 安装失败: {e}")
```

### 2. Version Check

```python
import email_widget
print(f"EmailWidget 版本: {email_widget.__version__}")
```

### 3. Create Test Email

```python
from email_widget import Email
from email_widget.widgets import TextWidget
from email_widget.core.enums import TextType

# 创建测试邮件
email = Email("安装测试")
email.add_widget(
    TextWidget()
    .set_content("EmailWidget 安装成功！🎉")
    .set_type(TextType.TITLE_LARGE)
)

# 导出测试文件
file_path = email.export_html("installation_test.html")
print(f"测试文件已生成: {file_path}")
```

## Optional Dependencies

Some features of EmailWidget require additional dependencies:

### 📊 Chart Features

If you need to use chart components (this content is installed on-demand, not included by default):

```bash
pip install matplotlib seaborn
```

## Common Issues

### ❓ Installation Failed?

=== "Permission Issues"
    ```bash
    # Use --user parameter
    pip install --user EmailWidget
    
    # Or use virtual environment
    python -m venv email_widget_env
    source email_widget_env/bin/activate  # Linux/macOS
    # or email_widget_env\Scripts\activate  # Windows
    pip install EmailWidget
    ```

=== "Network Issues"
    ```bash
    # Use domestic mirror source
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple EmailWidget
    ```

=== "Python Version Issues"
    ```bash
    # Check Python version
    python --version
    
    # If version is too low, please upgrade to Python 3.10+
    ```

### ❓ Charts Not Displaying Chinese Text Properly?

This is usually a font configuration issue:

```python
# 手动配置中文字体
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
```

EmailWidget will automatically handle this issue, but if problems persist, please check if Chinese fonts are installed on your system.

### ❓ Using in Jupyter Notebook

EmailWidget is fully compatible with Jupyter Notebook:

```python
from email_widget import Email
from email_widget.widgets import TextWidget

# 创建邮件
email = Email("Jupyter 测试")
email.add_widget(TextWidget().set_content("在 Jupyter 中使用 EmailWidget"))

# 预览 HTML（在 Jupyter 中直接显示）
from IPython.display import HTML
HTML(email.export_str())
```

## Next Steps

After installation, you can:

1. 📚 [Create Your First Email](first-email.md) - 5-minute quick start
2. 📖 [Understand Basic Concepts](concepts.md) - Learn core concepts
3. 💡 [View Example Code](../examples/basic.md) - Learn practical usage

---

!!! tip "Need Help?"
    If you encounter any installation issues, please feel free to ask in [GitHub Issues](https://github.com/271374667/EmailWidget/issues)!