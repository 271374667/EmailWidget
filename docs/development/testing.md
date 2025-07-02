# 测试指南

本指南介绍 EmailWidget 项目的测试策略、框架使用和最佳实践，帮助确保代码质量和稳定性。

## 🎯 测试策略

### 测试金字塔

EmailWidget 采用经典的测试金字塔策略：

```
        /\
       /  \
      /    \     E2E Tests (少量)
     /______\    - 完整流程测试
    /        \   - 邮件生成测试
   /          \  
  /____________\ Integration Tests (适量)
 /              \ - 组件集成测试
/________________\ - 模板渲染测试
Unit Tests (大量)
- 单个组件测试
- 工具函数测试
- 验证器测试
```

### 测试目标

- **单元测试覆盖率** ≥ 90%
- **集成测试覆盖率** ≥ 80%
- **关键路径测试** 100%
- **性能回归测试** 持续监控

## 🛠️ 测试框架

### 主要工具

| 工具 | 用途 | 版本要求 |
|------|------|----------|
| pytest | 测试框架 | ≥ 7.0 |
| pytest-cov | 覆盖率统计 | ≥ 4.0 |
| pytest-mock | Mock 支持 | ≥ 3.10 |
| pytest-xdist | 并行测试 | ≥ 3.0 |
| pytest-html | HTML 报告 | ≥ 3.1 |

### 安装测试依赖

```powershell
# Windows PowerShell 中安装
pip install pytest pytest-cov pytest-mock pytest-xdist pytest-html

# 或从 requirements-test.txt 安装
pip install -r requirements-test.txt
```

### pytest 配置

项目根目录的 `pytest.ini` 配置：

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
    unit: 单元测试
    integration: 集成测试
    e2e: 端到端测试
    slow: 慢速测试
    performance: 性能测试
```

## 📁 测试目录结构

```
tests/
├── conftest.py                 # pytest 配置和 fixtures
├── test_email.py              # Email 主类测试
├── test_core/                 # 核心模块测试
│   ├── __init__.py
│   ├── test_base.py           # BaseWidget 测试
│   ├── test_config.py         # 配置测试
│   ├── test_validators.py     # 验证器测试
│   ├── test_template_engine.py # 模板引擎测试
│   └── test_cache.py          # 缓存测试
├── test_widgets/              # Widget 组件测试
│   ├── __init__.py
│   ├── test_text_widget.py    # 文本组件测试
│   ├── test_table_widget.py   # 表格组件测试
│   ├── test_progress_widget.py # 进度组件测试
│   └── test_*.py              # 其他组件测试
├── test_utils/                # 工具模块测试
│   ├── __init__.py
│   ├── test_image_utils.py    # 图片工具测试
│   └── test_optional_deps.py  # 可选依赖测试
├── integration/               # 集成测试
│   ├── test_email_generation.py
│   ├── test_template_rendering.py
│   └── test_widget_interaction.py
├── e2e/                      # 端到端测试
│   ├── test_complete_workflows.py
│   └── test_email_output.py
├── performance/              # 性能测试
│   ├── test_rendering_speed.py
│   └── test_memory_usage.py
└── fixtures/                 # 测试数据
    ├── sample_data.json
    ├── test_images/
    └── expected_outputs/
```

## 🧪 单元测试

### 基本测试结构

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

### 使用 Fixtures

在 `conftest.py` 中定义通用 fixtures：

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

### Mock 和 Stub

使用 `pytest-mock` 进行 mock 测试：

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

### 参数化测试

使用 `@pytest.mark.parametrize` 进行参数化测试：

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

## 🔗 集成测试

集成测试验证多个组件协同工作：

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

## 🌐 端到端测试

端到端测试验证完整的用户工作流：

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

## ⚡ 性能测试

监控关键性能指标：

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

## 📊 测试覆盖率

### 生成覆盖率报告

```powershell
# 运行测试并生成覆盖率报告
python -m pytest --cov=email_widget --cov-report=html --cov-report=term

# 查看 HTML 报告
start htmlcov/index.html

# 只查看缺失覆盖的行
python -m pytest --cov=email_widget --cov-report=term-missing
```

### 覆盖率目标

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

## 🔧 测试工具和命令

### 常用测试命令

```powershell
# 基本测试运行
python -m pytest

# 详细输出
python -m pytest -v

# 运行特定测试文件
python -m pytest tests/test_email.py

# 运行特定测试方法
python -m pytest tests/test_email.py::TestEmail::test_add_widget

# 运行标记的测试
python -m pytest -m unit
python -m pytest -m "not slow"

# 并行运行测试
python -m pytest -n auto

# 生成 HTML 报告
python -m pytest --html=report.html --self-contained-html

# 只运行失败的测试
python -m pytest --lf

# 停在第一个失败
python -m pytest -x

# 详细的失败信息
python -m pytest -vv --tb=long
```

### 测试脚本

创建 `scripts/run_tests.py` 脚本：

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

使用脚本：

```powershell
# 运行所有测试
python scripts/run_tests.py

# 只运行单元测试
python scripts/run_tests.py --unit

# 运行测试并生成覆盖率报告
python scripts/run_tests.py --coverage --html
```

## 🚀 持续集成

### GitHub Actions 配置

`.github/workflows/test.yml`：

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

## 📋 测试最佳实践

### 测试原则

1. **AAA 模式** - Arrange, Act, Assert
2. **单一职责** - 每个测试只验证一个功能
3. **独立性** - 测试之间不应相互依赖
4. **可重复** - 测试结果应该是确定的
5. **快速** - 单元测试应该快速执行

### 测试命名

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

### 测试数据

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

### 异常测试

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

## 🎉 总结

遵循本测试指南，您将能够：

1. **编写高质量测试** - 覆盖各种场景和边界条件
2. **保证代码质量** - 通过自动化测试发现问题
3. **提升开发效率** - 快速验证修改的正确性
4. **维护代码稳定性** - 防止回归错误

现在开始为您的代码编写测试吧！良好的测试习惯将让您的代码更加健壮和可维护。🧪✨ 