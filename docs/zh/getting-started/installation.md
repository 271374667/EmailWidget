# 📦 安装指南

## 系统要求

!!! info "环境要求"
    - **Python**: 3.10 或更高版本
    - **操作系统**: Windows, macOS, Linux
    - **内存**: 建议 512MB 以上可用内存

## 安装方式

### 🚀 使用 pip 安装（推荐）

=== "最新稳定版"
    ```bash
    pip install EmailWidget
    ```

=== "指定版本"
    ```bash
    pip install EmailWidget==0.1.0
    ```

=== "升级到最新版"
    ```bash
    pip install EmailWidget -U
    ```

### 🔧 从源码安装

如果你想使用最新的开发版本或参与开发：

```bash
# 克隆仓库
git clone https://github.com/271374667/EmailWidget.git
cd EmailWidget

# 安装开发依赖
pip install -e ".[dev]"
```

## 验证安装

安装完成后，你可以通过以下方式验证安装是否成功：

### 1. 导入测试

```python
try:
    from email_widget import Email
    from email_widget.widgets import TextWidget
    print("✅ EmailWidget 安装成功！")
except ImportError as e:
    print(f"❌ 安装失败: {e}")
```

### 2. 版本检查

```python
import email_widget
print(f"EmailWidget 版本: {email_widget.__version__}")
```

### 3. 创建测试邮件

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

## 可选依赖

EmailWidget 的一些功能需要额外的依赖包：

### 📊 图表功能

如果你需要使用图表组件(这一部分的内容按需安装，默认不会自带)：

```bash
pip install matplotlib seaborn
```

## 常见问题

### ❓ 安装失败怎么办？

=== "权限问题"
    ```bash
    # 使用 --user 参数
    pip install --user EmailWidget
    
    # 或者使用虚拟环境
    python -m venv email_widget_env
    source email_widget_env/bin/activate  # Linux/macOS
    # 或 email_widget_env\Scripts\activate  # Windows
    pip install EmailWidget
    ```

=== "网络问题"
    ```bash
    # 使用国内镜像源
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple EmailWidget
    ```

=== "Python 版本问题"
    ```bash
    # 检查 Python 版本
    python --version
    
    # 如果版本过低，请升级到 Python 3.10+
    ```

### ❓ 图表不能正常显示中文？

这通常是字体配置问题：

```python
# 手动配置中文字体
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
```

EmailWidget 会自动处理这个问题，但如果仍有问题，请检查系统是否安装了中文字体。

### ❓ 在 Jupyter Notebook 中使用

EmailWidget 完全兼容 Jupyter Notebook：

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

## 下一步

安装完成后，你可以：

1. 📚 [创建第一个邮件](first-email.md) - 5分钟快速上手
2. 📖 [了解基本概念](concepts.md) - 理解核心概念
3. 💡 [查看示例代码](../examples/basic.md) - 学习实际用法

---

!!! tip "需要帮助？"
    如果遇到任何安装问题，欢迎在 [GitHub Issues](https://github.com/271374667/EmailWidget/issues) 中提问！ 