# 🤝 Contributing Guide

Thank you for your interest in the EmailWidget project! We welcome all forms of contributions, whether code, documentation, testing, or feedback suggestions.

## 🎯 Ways to Contribute

### 📝 Code Contributions

- 🐛 **Bug Fixes** - Help us fix known issues
- ✨ **New Features** - Add new Widgets or functionality
- ⚡ **Performance Optimization** - Improve code performance and efficiency
- 🔧 **Refactoring** - Improve code structure and maintainability

### 📚 Documentation Contributions

- 📖 **Improve Documentation** - Enhance existing documentation
- 💡 **Add Examples** - Provide more usage examples
- 🌐 **Translation** - Help translate documentation to other languages
- 📹 **Tutorials** - Create video or illustrated tutorials

### 🧪 Testing Contributions

- 🔍 **Write Tests** - Add tests for existing functionality
- 🐛 **Report Bugs** - Find and report issues
- 📊 **Performance Testing** - Test performance in different environments

## 🚀 Quick Start

### 1. 🍴 Fork the Project

Click the "Fork" button in the top right corner of the GitHub page to copy the project to your account.

### 2. 📥 Clone the Code

```bash
git clone https://github.com/YOUR_USERNAME/SpiderDaily.git
cd SpiderDaily
```

### 3. 🔧 Setup Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or venv\Scripts\activate  # Windows

# Install development dependencies
pip install -e ".[dev]"
```

### 4. 🌿 Create Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/issue-number
```

### 5. 💻 Start Development

Now you can start developing!

## 📋 Development Standards

### 🐍 Code Style

We use the following tools to maintain code quality:

```bash
# Code formatting
black email_widget/
isort email_widget/

# Code linting
flake8 email_widget/
mypy email_widget/
```

### 📝 Commit Standards

We use [Conventional Commits](https://www.conventionalcommits.org/) specification:

```bash
# Feature addition
git commit -m "feat: add new progress bar Widget"

# Bug fix
git commit -m "fix: fix encoding issue in table rendering"

# Documentation update
git commit -m "docs: update API documentation"

# Testing
git commit -m "test: add unit tests for TextWidget"

# Refactoring
git commit -m "refactor: optimize Email class rendering logic"
```

### 🧪 Testing Requirements

- All new features should have corresponding tests
- Bug fixes should include regression tests
- Ensure test coverage doesn't decrease

```bash
# Run tests
pytest tests/ -v

# Check coverage
pytest tests/ --cov=email_widget --cov-report=html
```

## 🎨 Creating New Widgets

If you want to add new components to EmailWidget, please follow these steps:

### 1. 📁 File Structure

```
email_widget/ewidget/widgets/
├── __init__.py
├── your_new_widget.py  # New Widget file
└── ...
```

### 2. 📝 Widget Base Template

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

### 3. 📝 Documentation Requirements

- Use Google-style docstrings
- Provide detailed class and method descriptions
- Include usage examples
- Describe parameters and return values

### 4. 🧪 Test Files

Create corresponding test file `tests/test_your_new_widget.py`:

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

### 5. 📦 Register Widget

Add import in `email_widget/ewidget/widgets/__init__.py`:

```python
from .your_new_widget import YourNewWidget

__all__ = [
    # ... 其他Widget
    'YourNewWidget',
]
```

## 📤 Submitting Pull Request

### 1. ✅ Pre-submission Checklist

```bash
# Run all tests
pytest tests/ -v

# Check code style
black --check email_widget/
isort --check-only email_widget/
flake8 email_widget/

# Type checking
mypy email_widget/
```

### 2. 📝 PR Description Template

```markdown
## 📋 Change Type
- [ ] 🐛 Bug fix
- [ ] ✨ New feature
- [ ] 💥 Breaking change
- [ ] 📚 Documentation update
- [ ] 🔧 Code refactoring
- [ ] ⚡ Performance optimization
- [ ] 🧪 Test improvement

## 📝 Change Description
Brief description of your changes...

## 🧪 Testing Description
- [ ] Added unit tests
- [ ] Passed all existing tests
- [ ] Manually tested functionality

## 📸 Screenshots/Examples
If UI-related changes, please provide screenshots or example code

## 🔗 Related Issues
Fixes #(issue number)
```

### 3. 🔍 Code Review

- We carefully review every PR
- May request some modifications
- Please be patient for review and actively respond to feedback

## 🐛 Reporting Bugs

### 📝 Bug Report Template

When you find a bug, please create an Issue using the following template:

```markdown
## 🐛 Bug Description
Brief description of the problem encountered...

## 🔄 Steps to Reproduce
1. Execute '...'
2. Click '....'
3. Scroll to '....'
4. See error

## 🎯 Expected Behavior
Describe what you expected to happen...

## 📸 Screenshots
If applicable, add screenshots to help explain the problem

## 🖥️ Environment Information
- OS: [e.g. Windows 10, macOS 12.0, Ubuntu 20.04]
- Python version: [e.g. 3.10.0]
- EmailWidget version: [e.g. 0.1.0]

## 📋 Additional Information
Add any other information about the problem...
```

## 💡 Feature Suggestions

We welcome suggestions for new features! When creating a Feature Request, please:

1. 🎯 **Clear Requirements** - Describe the feature you want in detail
2. 🤔 **Explain Reasons** - Why is this feature needed
3. 💭 **Provide Solutions** - If you have ideas, provide implementation solutions
4. 📝 **Give Examples** - Provide usage examples

## 🌟 Recognizing Contributors

We recognize contributors in the following places:

- 📜 **CONTRIBUTORS.md** file
- 🎉 **Release notes** acknowledgments
- 💬 **Social media** promotion
- 🏆 **Special badges** (for major contributions)

## 📞 Contact Us

If you have any questions or need help:

- 💬 [GitHub Discussions](https://github.com/271374667/SpiderDaily/discussions)
- 🐛 [GitHub Issues](https://github.com/271374667/EmailWidget/issues)
- 📧 [Email](mailto:271374667@qq.com)

---

!!! success "Thank you for your contribution!"
    Every contribution makes EmailWidget better. Regardless of the size of the contribution, we are very grateful! 🙏