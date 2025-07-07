# 🤝 贡献指南

感谢你对 EmailWidget 项目的关注！我们欢迎各种形式的贡献，无论是代码、文档、测试还是反馈建议。

## 🎯 贡献方式

### 📝 代码贡献

- 🐛 **修复Bug** - 帮助我们修复已知问题
- ✨ **新功能** - 添加新的Widget或功能
- ⚡ **性能优化** - 提升代码性能和效率
- 🔧 **重构** - 改进代码结构和可维护性

### 📚 文档贡献

- 📖 **完善文档** - 改进现有文档
- 💡 **添加示例** - 提供更多使用示例
- 🌐 **翻译** - 帮助翻译文档到其他语言
- 📹 **教程** - 创建视频或图文教程

### 🧪 测试贡献

- 🔍 **编写测试** - 为现有功能添加测试
- 🐛 **报告Bug** - 发现并报告问题
- 📊 **性能测试** - 测试在不同环境下的性能

## 🚀 快速开始

### 1. 🍴 Fork 项目

点击 GitHub 页面右上角的 "Fork" 按钮，将项目复制到你的账户下。

### 2. 📥 克隆代码

```bash
git clone https://github.com/YOUR_USERNAME/SpiderDaily.git
cd SpiderDaily
```

### 3. 🔧 设置开发环境

```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/macOS
# 或 venv\Scripts\activate  # Windows

# 安装开发依赖
pip install -e ".[dev]"
```

### 4. 🌿 创建分支

```bash
git checkout -b feature/your-feature-name
# 或
git checkout -b bugfix/issue-number
```

### 5. 💻 开始开发

现在你可以开始进行开发了！

## 📋 开发规范

### 🐍 代码风格

我们使用以下工具来保持代码质量：

```bash
# 代码格式化
black email_widget/
isort email_widget/

# 代码检查
flake8 email_widget/
mypy email_widget/
```

### 📝 提交规范

我们使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

```bash
# 功能添加
git commit -m "feat: 添加新的进度条Widget"

# Bug修复
git commit -m "fix: 修复表格渲染中的编码问题"

# 文档更新
git commit -m "docs: 更新API文档"

# 测试
git commit -m "test: 添加TextWidget的单元测试"

# 重构
git commit -m "refactor: 优化Email类的渲染逻辑"
```

### 🧪 测试要求

- 所有新功能都应该有相应的测试
- 修复Bug时应该添加回归测试
- 确保测试覆盖率不下降

```bash
# 运行测试
pytest tests/ -v

# 检查覆盖率
pytest tests/ --cov=email_widget --cov-report=html
```

## 🎨 创建新的Widget

如果你想为 EmailWidget 添加新的组件，请遵循以下步骤：

### 1. 📁 文件结构

```
email_widget/ewidget/widgets/
├── __init__.py
├── your_new_widget.py  # 新Widget文件
└── ...
```

### 2. 📝 Widget基础模板

```python
"""你的新Widget实现

这个模块提供了XXX功能的Widget。
"""
from typing import Optional
from email_widget.core.base import BaseWidget


class YourNewWidget(BaseWidget):
    """你的新Widget类，用于XXX功能。
    
    详细的类说明...
    
    Attributes:
        _your_attr: 属性说明
        
    Examples:
        >>> widget = YourNewWidget()
        >>> widget.set_something("value")
        >>> html = widget.render_html()
    """

    def __init__(self, widget_id: Optional[str] = None):
        """初始化Widget。
        
        Args:
            widget_id: 可选的Widget ID
        """
        super().__init__(widget_id)
        # 初始化你的属性
        self._your_attr = "default_value"

    def set_something(self, value: str) -> 'YourNewWidget':
        """设置某个属性。
        
        Args:
            value: 属性值
            
        Returns:
            返回self以支持链式调用
        """
        self._your_attr = value
        return self

    def _get_template_name(self) -> str:
        """获取模板名称。
        
        Returns:
            模板文件名
        """
        return "your_new_widget.html"

    def render_html(self) -> str:
        """渲染为HTML字符串。
        
        Returns:
            渲染后的HTML字符串
        """
        # 实现你的渲染逻辑
        return f'<div>{self._your_attr}</div>'
```

### 3. 📝 文档要求

- 使用Google风格的docstring
- 提供详细的类和方法说明
- 包含使用示例
- 说明参数和返回值

### 4. 🧪 测试文件

创建对应的测试文件 `tests/test_your_new_widget.py`：

```python
import pytest
from email_widget.widgets import YourNewWidget


class TestYourNewWidget:
    def test_init(self):
        """测试Widget初始化"""
        widget = YourNewWidget()
        assert widget._your_attr == "default_value"

    def test_set_something(self):
        """测试设置属性"""
        widget = YourNewWidget()
        result = widget.set_something("test_value")

        assert widget._your_attr == "test_value"
        assert result is widget  # 测试链式调用

    def test_render_html(self):
        """测试HTML渲染"""
        widget = YourNewWidget()
        widget.set_something("test")

        html = widget.render_html()
        assert "test" in html
```

### 5. 📦 注册Widget

在 `email_widget/ewidget/widgets/__init__.py` 中添加导入：

```python
from .your_new_widget import YourNewWidget

__all__ = [
    # ... 其他Widget
    'YourNewWidget',
]
```

## 📤 提交Pull Request

### 1. ✅ 提交前检查

```bash
# 运行所有测试
pytest tests/ -v

# 检查代码风格
black --check email_widget/
isort --check-only email_widget/
flake8 email_widget/

# 类型检查
mypy email_widget/
```

### 2. 📝 PR描述模板

```markdown
## 📋 变更类型
- [ ] 🐛 Bug修复
- [ ] ✨ 新功能
- [ ] 💥 破坏性变更
- [ ] 📚 文档更新
- [ ] 🔧 代码重构
- [ ] ⚡ 性能优化
- [ ] 🧪 测试改进

## 📝 变更说明
简要描述你的变更内容...

## 🧪 测试说明
- [ ] 已添加单元测试
- [ ] 已通过所有现有测试
- [ ] 已手动测试功能

## 📸 截图/示例
如果是UI相关的变更，请提供截图或示例代码

## 🔗 相关Issue
Fixes #(issue number)
```

### 3. 🔍 代码审查

- 我们会仔细审查每个PR
- 可能会要求进行一些修改
- 请耐心等待审查，并积极响应反馈

## 🐛 报告Bug

### 📝 Bug报告模板

当你发现Bug时，请使用以下模板创建Issue：

```markdown
## 🐛 Bug描述
简要描述遇到的问题...

## 🔄 复现步骤
1. 执行 '...'
2. 点击 '....'
3. 滚动到 '....'
4. 看到错误

## 🎯 期望行为
描述你期望发生的情况...

## 📸 截图
如果适用，添加截图来帮助解释问题

## 🖥️ 环境信息
- OS: [e.g. Windows 10, macOS 12.0, Ubuntu 20.04]
- Python版本: [e.g. 3.10.0]
- EmailWidget版本: [e.g. 0.1.0]

## 📋 额外信息
添加任何其他有关问题的信息...
```

## 💡 功能建议

我们欢迎新功能的建议！请在创建Feature Request时：

1. 🎯 **明确需求** - 详细描述你想要的功能
2. 🤔 **解释原因** - 为什么需要这个功能
3. 💭 **提供方案** - 如果有想法，可以提供实现方案
4. 📝 **举例说明** - 提供使用示例

## 🌟 认可贡献者

我们会在以下地方认可贡献者：

- 📜 **CONTRIBUTORS.md** 文件
- 🎉 **发布说明** 中感谢
- 💬 **社交媒体** 宣传
- 🏆 **特殊徽章** （重大贡献）

## 📞 联系我们

如果你有任何问题或需要帮助：

- 💬 [GitHub Discussions](https://github.com/271374667/SpiderDaily/discussions)
- 🐛 [GitHub Issues](https://github.com/271374667/EmailWidget/issues)
- 📧 [Email](mailto:271374667@qq.com)

---

!!! success "感谢你的贡献！"
    每一个贡献都让 EmailWidget 变得更好。无论贡献大小，我们都非常感谢！🙏 