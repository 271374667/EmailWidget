# Testing Guide

This guide introduces the testing strategy, framework usage, and best practices for the EmailWidget project to help ensure code quality and stability.

## 🎯 Testing Strategy

### Testing Pyramid

EmailWidget adopts the classic testing pyramid strategy:

```
        /\
       /  \
      /    \     E2E Tests (Few)
     /______\    - Complete workflow tests
    /        \   - Email generation tests
   /          \  
  /____________\ Integration Tests (Some)
 /              \ - Component integration tests
/________________\ - Template rendering tests
Unit Tests (Many)
- Individual component tests
- Utility function tests
- Validator tests
```

### Testing Goals

- **Unit Test Coverage** ≥ 90%
- **Integration Test Coverage** ≥ 80%
- **Critical Path Testing** 100%
- **Performance Regression Testing** Continuous monitoring

## 🛠️ Testing Framework

### Main Tools

| Tool | Purpose | Version Requirement |
|------|---------|-------------------|
| pytest | Testing framework | ≥ 7.0 |
| pytest-cov | Coverage statistics | ≥ 4.0 |
| pytest-mock | Mock support | ≥ 3.10 |
| pytest-xdist | Parallel testing | ≥ 3.0 |
| pytest-html | HTML reports | ≥ 3.1 |

### Installing Test Dependencies

```powershell
# Install in Windows PowerShell
pip install pytest pytest-cov pytest-mock pytest-xdist pytest-html

# Or install from requirements-test.txt
pip install -r requirements-test.txt
```

### pytest Configuration

`pytest.ini` configuration in project root:

```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    --strict-markers
    --strict-config
    --verbose
    --cov=email_widget
    --cov-report=html
    --cov-report=term-missing
    --cov-fail-under=90
markers =
    unit: Unit tests
    integration: Integration tests
    e2e: End-to-end tests
    slow: Slow tests
    performance: Performance tests
```

## 📁 Test Directory Structure

```
tests/
├── conftest.py                 # pytest configuration and fixtures
├── test_email.py              # Email main class tests
├── test_core/                 # Core module tests
│   ├── __init__.py
│   ├── test_base.py           # BaseWidget tests
│   ├── test_config.py         # Configuration tests
│   ├── test_validators.py     # Validator tests
│   ├── test_template_engine.py # Template engine tests
│   └── test_cache.py          # Cache tests
├── test_widgets/              # Widget component tests
│   ├── __init__.py
│   ├── test_text_widget.py    # Text component tests
│   ├── test_table_widget.py   # Table component tests
│   ├── test_progress_widget.py # Progress component tests
│   └── test_*.py              # Other component tests
├── test_utils/                # Utility module tests
│   ├── __init__.py
│   ├── test_image_utils.py    # Image utility tests
│   └── test_optional_deps.py  # Optional dependency tests
├── integration/               # Integration tests
│   ├── test_email_generation.py
│   ├── test_template_rendering.py
│   └── test_widget_interaction.py
├── e2e/                      # End-to-end tests
│   ├── test_complete_workflows.py
│   └── test_email_output.py
├── performance/              # Performance tests
│   ├── test_rendering_speed.py
│   └── test_memory_usage.py
└── fixtures/                 # Test data
    ├── sample_data.json
    ├── test_images/
    └── expected_outputs/
```

## 🧪 Unit Testing

### Basic Test Structure

```python
import pytest
from email_widget.widgets.text_widget import TextWidget
from email_widget.core.enums import TextType, TextAlign

class TestTextWidget:
    """文本组件单元测试"""
    
    def setup_method(self):
        """每个测试方法前的初始化"""
        self.widget = TextWidget()
    
    def test_initialization(self):
        """测试初始化状态"""
        assert self.widget._content == ""
        assert self.widget._text_type == TextType.BODY
        assert self.widget._align == TextAlign.LEFT
    
    def test_set_content(self):
        """测试设置内容"""
        content = "测试内容"
        result = self.widget.set_content(content)
        
        # 测试返回值（链式调用）
        assert result is self.widget
        # 测试状态变化
        assert self.widget._content == content
    
    def test_set_content_validation(self):
        """测试内容验证"""
        # 测试有效输入
        self.widget.set_content("有效内容")
        assert self.widget._content == "有效内容"
        
        # 测试无效输入
        with pytest.raises(TypeError):
            self.widget.set_content(123)  # 不是字符串
        
        with pytest.raises(ValueError):
            self.widget.set_content("")  # 空字符串
    
    def test_set_type(self):
        """测试设置文本类型"""
        self.widget.set_type(TextType.TITLE_LARGE)
        assert self.widget._text_type == TextType.TITLE_LARGE
    
    def test_set_align(self):
        """测试设置对齐方式"""
        self.widget.set_align(TextAlign.CENTER)
        assert self.widget._align == TextAlign.CENTER
    
    def test_render_basic(self):
        """测试基本渲染"""
        self.widget.set_content("测试文本")
        html = self.widget.render()
        
        assert "测试文本" in html
        assert "<" in html and ">" in html  # 包含 HTML 标签
    
    def test_render_with_styling(self):
        """测试带样式的渲染"""
        self.widget.set_content("标题文本") \
                  .set_type(TextType.TITLE_LARGE) \
                  .set_align(TextAlign.CENTER) \
                  .set_color("#ff0000")
        
        html = self.widget.render()
        
        assert "标题文本" in html
        assert "text-align: center" in html
        assert "color: #ff0000" in html
    
    @pytest.mark.parametrize("text_type,expected_tag", [
        (TextType.TITLE_LARGE, "h1"),
        (TextType.TITLE_SMALL, "h2"),
        (TextType.SECTION_H2, "h2"),
        (TextType.SECTION_H3, "h3"),
        (TextType.BODY, "p"),
        (TextType.CAPTION, "small")
    ])
    def test_render_html_tags(self, text_type, expected_tag):
        """测试不同文本类型的 HTML 标签"""
        self.widget.set_content("测试").set_type(text_type)
        html = self.widget.render()
        assert f"<{expected_tag}" in html
    
    def test_chain_methods(self):
        """测试链式调用"""
        result = self.widget.set_content("测试") \
                           .set_type(TextType.TITLE_LARGE) \
                           .set_align(TextAlign.CENTER) \
                           .set_color("#blue")
        
        assert result is self.widget
        assert self.widget._content == "测试"
        assert self.widget._text_type == TextType.TITLE_LARGE
        assert self.widget._align == TextAlign.CENTER
        assert self.widget._color == "#blue"
```

### Using Fixtures

Define common fixtures in `conftest.py`:

```python
import pytest
import pandas as pd
from pathlib import Path
from email_widget import Email
from email_widget.widgets import TextWidget, TableWidget

@pytest.fixture
def sample_email():
    """创建示例邮件对象"""
    return Email("测试邮件")

@pytest.fixture
def sample_text_widget():
    """创建示例文本组件"""
    widget = TextWidget()
    widget.set_content("测试内容")
    return widget

@pytest.fixture
def sample_dataframe():
    """创建示例 DataFrame"""
    return pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Tokyo']
    })

@pytest.fixture
def temp_output_dir(tmp_path):
    """创建临时输出目录"""
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    return output_dir

@pytest.fixture
def mock_image_path():
    """模拟图片路径"""
    return "tests/fixtures/test_images/sample.png"

# 使用 fixture 的测试
class TestEmailGeneration:
    
    def test_add_widget(self, sample_email, sample_text_widget):
        """测试添加组件"""
        sample_email.add_widget(sample_text_widget)
        assert len(sample_email._widgets) == 1
        assert sample_email._widgets[0] is sample_text_widget
    
    def test_export_html(self, sample_email, sample_text_widget, temp_output_dir):
        """测试导出 HTML"""
        sample_email.add_widget(sample_text_widget)
        output_path = temp_output_dir / "test.html"
        
        sample_email.export_html(str(output_path))
        
        assert output_path.exists()
        content = output_path.read_text(encoding='utf-8')
        assert "测试内容" in content
```

### Mock and Stub

Using `pytest-mock` for mock testing:

```python
import pytest
from unittest.mock import Mock, patch
from email_widget.utils.image_utils import ImageUtils

class TestImageUtils:
    """图片工具测试"""
    
    @patch('requests.get')
    def test_download_image_success(self, mock_get):
        """测试成功下载图片"""
        # 设置 mock 返回值
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b'fake_image_data'
        mock_get.return_value = mock_response
        
        # 执行测试
        result = ImageUtils.download_image("http://example.com/image.jpg")
        
        # 验证结果
        assert result == b'fake_image_data'
        mock_get.assert_called_once_with("http://example.com/image.jpg")
    
    @patch('requests.get')
    def test_download_image_failure(self, mock_get):
        """测试下载图片失败"""
        # 设置 mock 抛出异常
        mock_get.side_effect = ConnectionError("网络错误")
        
        # 验证异常
        with pytest.raises(ConnectionError):
            ImageUtils.download_image("http://example.com/image.jpg")
    
    def test_validate_image_format(self, mocker):
        """测试图片格式验证"""
        # 使用 mocker fixture
        mock_is_valid = mocker.patch.object(ImageUtils, '_is_valid_format')
        mock_is_valid.return_value = True
        
        result = ImageUtils.validate_format("image.jpg")
        
        assert result is True
        mock_is_valid.assert_called_once_with("image.jpg")
```

### Parametrized Testing

Using `@pytest.mark.parametrize` for parametrized testing:

```python
import pytest
from email_widget.core.validators import ColorValidator

class TestColorValidator:
    """颜色验证器测试"""
    
    @pytest.mark.parametrize("color,expected", [
        ("#ff0000", True),          # 标准十六进制
        ("#FF0000", True),          # 大写十六进制
        ("#f00", True),             # 短十六进制
        ("red", True),              # 颜色名称
        ("rgb(255,0,0)", True),     # RGB 格式
        ("rgba(255,0,0,0.5)", True), # RGBA 格式
        ("invalid", False),         # 无效颜色
        ("", False),                # 空字符串
        ("#gggggg", False),         # 无效十六进制
    ])
    def test_color_validation(self, color, expected):
        """测试各种颜色格式的验证"""
        validator = ColorValidator()
        
        if expected:
            # 应该通过验证
            validator.validate(color)  # 不应该抛出异常
        else:
            # 应该验证失败
            with pytest.raises(ValueError):
                validator.validate(color)
    
    @pytest.mark.parametrize("rgb_value", [0, 128, 255])
    def test_rgb_values(self, rgb_value):
        """测试 RGB 值范围"""
        color = f"rgb({rgb_value},{rgb_value},{rgb_value})"
        validator = ColorValidator()
        validator.validate(color)  # 应该通过验证
```

## 🔗 Integration Testing

Integration tests verify multiple components working together:

```python
import pytest
import pandas as pd
from email_widget import Email
from email_widget.widgets import TextWidget, TableWidget, ProgressWidget

class TestWidgetIntegration:
    """组件集成测试"""
    
    def test_email_with_multiple_widgets(self):
        """测试邮件包含多个组件"""
        email = Email("集成测试邮件")
        
        # 添加标题
        title = TextWidget()
        title.set_content("测试报告").set_type(TextType.TITLE_LARGE)
        email.add_widget(title)
        
        # 添加表格
        table = TableWidget()
        table.set_headers(["姓名", "年龄"])
        table.add_row(["张三", "25"])
        table.add_row(["李四", "30"])
        email.add_widget(table)
        
        # 添加进度条
        progress = ProgressWidget()
        progress.set_value(75).set_label("完成度")
        email.add_widget(progress)
        
        # 渲染邮件
        html = email.export_str()
        
        # 验证所有组件都在输出中
        assert "测试报告" in html
        assert "张三" in html
        assert "李四" in html
        assert "75%" in html or "75.0%" in html
    
    def test_dataframe_to_table_integration(self):
        """测试 DataFrame 与表格组件集成"""
        # 创建测试数据
        df = pd.DataFrame({
            '产品': ['A', 'B', 'C'],
            '销量': [100, 200, 150],
            '价格': [10.5, 20.0, 15.8]
        })
        
        email = Email("数据报告")
        
        # 使用便捷方法从 DataFrame 创建表格
        email.add_table_from_df(df, title="产品销售数据")
        
        html = email.export_str()
        
        # 验证数据正确渲染
        assert "产品销售数据" in html
        assert "产品" in html and "销量" in html and "价格" in html
        assert "100" in html and "200" in html and "150" in html
    
    @pytest.mark.integration
    def test_template_engine_integration(self):
        """测试模板引擎集成"""
        email = Email("模板测试")
        
        # 使用自定义模板
        custom_widget = CustomTemplateWidget()
        custom_widget.set_template("Hello {{name}}!")
        custom_widget.set_data(name="World")
        
        email.add_widget(custom_widget)
        html = email.export_str()
        
        assert "Hello World!" in html
```

## 🌐 End-to-End Testing

End-to-end tests verify complete user workflows:

```python
import pytest
from pathlib import Path
import tempfile
from email_widget import Email

class TestE2EWorkflows:
    """端到端测试"""
    
    @pytest.mark.e2e
    def test_complete_report_generation(self):
        """测试完整报告生成流程"""
        # 1. 创建邮件
        email = Email("月度业务报告")
        
        # 2. 添加标题和说明
        email.add_title("2024年1月业务报告", TextType.TITLE_LARGE)
        email.add_text("本报告包含主要业务指标和分析。")
        
        # 3. 添加关键指标
        email.add_card("总收入", "¥1,250,000", "💰")
        email.add_card("新用户", "2,847", "👥")
        
        # 4. 添加详细数据表格
        data = [
            ["产品A", "¥500,000", "1,200"],
            ["产品B", "¥750,000", "1,647"]
        ]
        email.add_table_from_data(data, ["产品", "收入", "销量"])
        
        # 5. 添加进度指标
        email.add_progress(85, "目标完成度", ProgressTheme.SUCCESS)
        
        # 6. 添加提醒
        email.add_alert("下月需要重点关注产品A的库存情况", AlertType.WARNING)
        
        # 7. 导出为 HTML
        with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as f:
            email.export_html(f.name)
            
            # 8. 验证文件生成
            output_path = Path(f.name)
            assert output_path.exists()
            
            # 9. 验证内容完整性
            content = output_path.read_text(encoding='utf-8')
            assert "月度业务报告" in content
            assert "¥1,250,000" in content
            assert "产品A" in content
            assert "85%" in content or "85.0%" in content
            assert "库存情况" in content
            
            # 10. 验证 HTML 结构
            assert "<html" in content
            assert "</html>" in content
            assert "<head>" in content
            assert "<body>" in content
    
    @pytest.mark.e2e
    @pytest.mark.slow
    def test_large_dataset_performance(self):
        """测试大数据集性能"""
        import time
        
        # 创建大量数据
        email = Email("大数据测试")
        
        # 添加大表格
        large_data = []
        for i in range(1000):
            large_data.append([f"项目{i}", f"值{i}", f"描述{i}"])
        
        start_time = time.time()
        email.add_table_from_data(large_data, ["项目", "值", "描述"])
        
        # 渲染时间应该在合理范围内
        html = email.export_str()
        end_time = time.time()
        
        # 性能断言（根据实际情况调整）
        assert (end_time - start_time) < 10.0  # 应该在10秒内完成
        assert len(html) > 10000  # 确保内容已生成
        assert "项目999" in html  # 确保所有数据都包含
```

## ⚡ Performance Testing

Monitor key performance metrics:

```python
import pytest
import time
import psutil
import os
from email_widget import Email

class TestPerformance:
    """性能测试"""
    
    @pytest.mark.performance
    def test_rendering_speed(self):
        """测试渲染速度"""
        email = Email("性能测试")
        
        # 添加多个组件
        for i in range(100):
            email.add_text(f"文本内容 {i}")
        
        # 测量渲染时间
        start_time = time.perf_counter()
        html = email.export_str()
        end_time = time.perf_counter()
        
        render_time = end_time - start_time
        
        # 断言渲染时间
        assert render_time < 1.0, f"渲染时间过长: {render_time:.3f}秒"
        assert len(html) > 1000, "输出内容太少"
    
    @pytest.mark.performance
    def test_memory_usage(self):
        """测试内存使用"""
        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss
        
        # 创建大量对象
        emails = []
        for i in range(50):
            email = Email(f"测试邮件 {i}")
            for j in range(20):
                email.add_text(f"内容 {i}-{j}")
            emails.append(email)
        
        # 检查内存增长
        peak_memory = process.memory_info().rss
        memory_increase = peak_memory - initial_memory
        
        # 断言内存使用合理（根据实际情况调整）
        assert memory_increase < 100 * 1024 * 1024, f"内存使用过多: {memory_increase / 1024 / 1024:.1f}MB"
    
    @pytest.mark.performance
    def test_cache_effectiveness(self):
        """测试缓存效果"""
        from email_widget.core.cache import Cache
        
        cache = Cache(max_size=100)
        
        # 第一次访问（未缓存）
        start_time = time.perf_counter()
        result1 = cache.get_or_set("test_key", lambda: expensive_operation())
        first_time = time.perf_counter() - start_time
        
        # 第二次访问（已缓存）
        start_time = time.perf_counter()
        result2 = cache.get("test_key")
        second_time = time.perf_counter() - start_time
        
        # 缓存应该显著提升性能
        assert result1 == result2
        assert second_time < first_time / 10, "缓存没有显著提升性能"

def expensive_operation():
    """模拟耗时操作"""
    time.sleep(0.1)
    return "expensive_result"
```

## 📊 Test Coverage

### Generate Coverage Reports

```powershell
# Run tests and generate coverage report
python -m pytest --cov=email_widget --cov-report=html --cov-report=term

# View HTML report
start htmlcov/index.html

# View only missing coverage lines
python -m pytest --cov=email_widget --cov-report=term-missing
```

### Coverage Goals

```python
# pytest.ini 中设置覆盖率要求
[tool:pytest]
addopts = --cov-fail-under=90

# 排除某些文件
--cov-config=.coveragerc

# .coveragerc 文件内容
[run]
source = email_widget
omit = 
    */tests/*
    */venv/*
    setup.py
    */migrations/*

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError
```

## 🔧 Testing Tools and Commands

### Common Test Commands

```powershell
# Basic test run
python -m pytest

# Verbose output
python -m pytest -v

# Run specific test file
python -m pytest tests/test_email.py

# Run specific test method
python -m pytest tests/test_email.py::TestEmail::test_add_widget

# Run marked tests
python -m pytest -m unit
python -m pytest -m "not slow"

# Run tests in parallel
python -m pytest -n auto

# Generate HTML report
python -m pytest --html=report.html --self-contained-html

# Run only failed tests
python -m pytest --lf

# Stop at first failure
python -m pytest -x

# Detailed failure information
python -m pytest -vv --tb=long
```

### Test Scripts

Create `scripts/run_tests.py` script:

```python
#!/usr/bin/env python
"""
测试运行脚本
"""
import subprocess
import sys
import argparse
from pathlib import Path

def run_command(cmd, description):
    """运行命令并检查结果"""
    print(f"\n🔄 {description}...")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✅ {description} 成功")
        if result.stdout:
            print(result.stdout)
    else:
        print(f"❌ {description} 失败")
        print(result.stderr)
        return False
    return True

def main():
    parser = argparse.ArgumentParser(description="运行 EmailWidget 测试")
    parser.add_argument("--unit", action="store_true", help="只运行单元测试")
    parser.add_argument("--integration", action="store_true", help="只运行集成测试")
    parser.add_argument("--e2e", action="store_true", help="只运行端到端测试")
    parser.add_argument("--performance", action="store_true", help="只运行性能测试")
    parser.add_argument("--coverage", action="store_true", help="生成覆盖率报告")
    parser.add_argument("--html", action="store_true", help="生成 HTML 报告")
    
    args = parser.parse_args()
    
    # 基本测试命令
    pytest_cmd = "python -m pytest"
    
    if args.unit:
        pytest_cmd += " -m unit"
    elif args.integration:
        pytest_cmd += " -m integration"
    elif args.e2e:
        pytest_cmd += " -m e2e"
    elif args.performance:
        pytest_cmd += " -m performance"
    
    if args.coverage:
        pytest_cmd += " --cov=email_widget --cov-report=term-missing"
        if args.html:
            pytest_cmd += " --cov-report=html"
    
    if args.html:
        pytest_cmd += " --html=reports/test_report.html --self-contained-html"
    
    # 确保报告目录存在
    Path("reports").mkdir(exist_ok=True)
    
    # 运行测试
    success = run_command(pytest_cmd, "运行测试")
    
    if success:
        print("\n🎉 所有测试通过!")
    else:
        print("\n💥 测试失败!")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

Using the script:

```powershell
# Run all tests
python scripts/run_tests.py

# Run only unit tests
python scripts/run_tests.py --unit

# Run tests and generate coverage report
python scripts/run_tests.py --coverage --html
```

## 🚀 Continuous Integration

### GitHub Actions Configuration

`.github/workflows/test.yml`:

```yaml
name: Tests

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: windows-latest
    strategy:
      matrix:
        python-version: [3.10, 3.11, 3.12]

    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements-test.txt
        pip install -e .
    
    - name: Run tests
      run: |
        python -m pytest --cov=email_widget --cov-report=xml
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
        fail_ci_if_error: true
```

## 📋 Testing Best Practices

### Testing Principles

1. **AAA Pattern** - Arrange, Act, Assert
2. **Single Responsibility** - Each test should verify only one functionality
3. **Independence** - Tests should not depend on each other
4. **Repeatability** - Test results should be deterministic
5. **Fast** - Unit tests should execute quickly

### Test Naming

```python
# 好的测试名称
def test_set_title_with_valid_string_updates_title():
    pass

def test_render_returns_html_with_title_content():
    pass

def test_add_widget_with_none_raises_type_error():
    pass

# 避免的测试名称
def test_title():  # 太模糊
    pass

def test_1():  # 没有意义
    pass
```

### Test Data

```python
# 使用有意义的测试数据
def test_user_registration():
    user_data = {
        "name": "张三",
        "email": "zhangsan@example.com",
        "age": 25
    }
    # 而不是
    # user_data = {"a": "b", "c": "d"}
```

### Exception Testing

```python
def test_invalid_input_handling():
    """测试无效输入的处理"""
    widget = TextWidget()
    
    # 测试具体的异常类型和消息
    with pytest.raises(ValueError, match="内容不能为空"):
        widget.set_content("")
    
    with pytest.raises(TypeError, match="内容必须是字符串"):
        widget.set_content(123)
```

## 🎉 Summary

Following this testing guide, you will be able to:

1. **Write high-quality tests** - Cover various scenarios and edge cases
2. **Ensure code quality** - Discover issues through automated testing
3. **Improve development efficiency** - Quickly verify correctness of changes
4. **Maintain code stability** - Prevent regression errors

Now start writing tests for your code! Good testing habits will make your code more robust and maintainable. 🧪✨