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
    """Text widget unit tests"""
    
    def setup_method(self):
        """Setup before each test method"""
        self.widget = TextWidget()
    
    def test_initialization(self):
        """Test initialization state"""
        assert self.widget._content == ""
        assert self.widget._text_type == TextType.BODY
        assert self.widget._align == TextAlign.LEFT
    
    def test_set_content(self):
        """Test setting content"""
        content = "Test content"
        result = self.widget.set_content(content)
        
        # Test return value (method chaining)
        assert result is self.widget
        # Test state change
        assert self.widget._content == content
    
    def test_set_content_validation(self):
        """Test content validation"""
        # Test valid input
        self.widget.set_content("Valid content")
        assert self.widget._content == "Valid content"
        
        # Test invalid input
        with pytest.raises(TypeError):
            self.widget.set_content(123)  # Not a string
        
        with pytest.raises(ValueError):
            self.widget.set_content("")  # Empty string
    
    def test_set_type(self):
        """Test setting text type"""
        self.widget.set_type(TextType.TITLE_LARGE)
        assert self.widget._text_type == TextType.TITLE_LARGE
    
    def test_set_align(self):
        """Test setting alignment"""
        self.widget.set_align(TextAlign.CENTER)
        assert self.widget._align == TextAlign.CENTER
    
    def test_render_basic(self):
        """Test basic rendering"""
        self.widget.set_content("Test text")
        html = self.widget.render()
        
        assert "Test text" in html
        assert "<" in html and ">" in html  # Contains HTML tags
    
    def test_render_with_styling(self):
        """Test rendering with styling"""
        self.widget.set_content("Title text") \
                  .set_type(TextType.TITLE_LARGE) \
                  .set_align(TextAlign.CENTER) \
                  .set_color("#ff0000")
        
        html = self.widget.render()
        
        assert "Title text" in html
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
        """Test HTML tags for different text types"""
        self.widget.set_content("Test").set_type(text_type)
        html = self.widget.render()
        assert f"<{expected_tag}" in html
    
    def test_chain_methods(self):
        """Test method chaining"""
        result = self.widget.set_content("Test") \
                           .set_type(TextType.TITLE_LARGE) \
                           .set_align(TextAlign.CENTER) \
                           .set_color("#blue")
        
        assert result is self.widget
        assert self.widget._content == "Test"
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
    """Create sample email object"""
    return Email("Test Email")

@pytest.fixture
def sample_text_widget():
    """Create sample text widget"""
    widget = TextWidget()
    widget.set_content("Test content")
    return widget

@pytest.fixture
def sample_dataframe():
    """Create sample DataFrame"""
    return pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Tokyo']
    })

@pytest.fixture
def temp_output_dir(tmp_path):
    """Create temporary output directory"""
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    return output_dir

@pytest.fixture
def mock_image_path():
    """Mock image path"""
    return "tests/fixtures/test_images/sample.png"

# Tests using fixtures
class TestEmailGeneration:
    
    def test_add_widget(self, sample_email, sample_text_widget):
        """Test adding widget"""
        sample_email.add_widget(sample_text_widget)
        assert len(sample_email._widgets) == 1
        assert sample_email._widgets[0] is sample_text_widget
    
    def test_export_html(self, sample_email, sample_text_widget, temp_output_dir):
        """Test HTML export"""
        sample_email.add_widget(sample_text_widget)
        output_path = temp_output_dir / "test.html"
        
        sample_email.export_html(str(output_path))
        
        assert output_path.exists()
        content = output_path.read_text(encoding='utf-8')
        assert "Test content" in content
```

### Mock and Stub

Using `pytest-mock` for mock testing:

```python
import pytest
from unittest.mock import Mock, patch
from email_widget.utils.image_utils import ImageUtils

class TestImageUtils:
    """Image utility tests"""
    
    @patch('requests.get')
    def test_download_image_success(self, mock_get):
        """Test successful image download"""
        # Set mock return value
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b'fake_image_data'
        mock_get.return_value = mock_response
        
        # Execute test
        result = ImageUtils.download_image("http://example.com/image.jpg")
        
        # Verify result
        assert result == b'fake_image_data'
        mock_get.assert_called_once_with("http://example.com/image.jpg")
    
    @patch('requests.get')
    def test_download_image_failure(self, mock_get):
        """Test image download failure"""
        # Set mock to raise exception
        mock_get.side_effect = ConnectionError("Network error")
        
        # Verify exception
        with pytest.raises(ConnectionError):
            ImageUtils.download_image("http://example.com/image.jpg")
    
    def test_validate_image_format(self, mocker):
        """Test image format validation"""
        # Use mocker fixture
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
    """Color validator tests"""
    
    @pytest.mark.parametrize("color,expected", [
        ("#ff0000", True),          # Standard hex
        ("#FF0000", True),          # Uppercase hex
        ("#f00", True),             # Short hex
        ("red", True),              # Color name
        ("rgb(255,0,0)", True),     # RGB format
        ("rgba(255,0,0,0.5)", True), # RGBA format
        ("invalid", False),         # Invalid color
        ("", False),                # Empty string
        ("#gggggg", False),         # Invalid hex
    ])
    def test_color_validation(self, color, expected):
        """Test validation of various color formats"""
        validator = ColorValidator()
        
        if expected:
            # Should pass validation
            validator.validate(color)  # Should not raise exception
        else:
            # Should fail validation
            with pytest.raises(ValueError):
                validator.validate(color)
    
    @pytest.mark.parametrize("rgb_value", [0, 128, 255])
    def test_rgb_values(self, rgb_value):
        """Test RGB value range"""
        color = f"rgb({rgb_value},{rgb_value},{rgb_value})"
        validator = ColorValidator()
        validator.validate(color)  # Should pass validation
```

## 🔗 Integration Testing

Integration tests verify multiple components working together:

```python
import pytest
import pandas as pd
from email_widget import Email
from email_widget.widgets import TextWidget, TableWidget, ProgressWidget

class TestWidgetIntegration:
    """Widget integration tests"""
    
    def test_email_with_multiple_widgets(self):
        """Test email with multiple widgets"""
        email = Email("Integration Test Email")
        
        # Add title
        title = TextWidget()
        title.set_content("Test Report").set_type(TextType.TITLE_LARGE)
        email.add_widget(title)
        
        # Add table
        table = TableWidget()
        table.set_headers(["Name", "Age"])
        table.add_row(["John", "25"])
        table.add_row(["Jane", "30"])
        email.add_widget(table)
        
        # Add progress bar
        progress = ProgressWidget()
        progress.set_value(75).set_label("Completion")
        email.add_widget(progress)
        
        # Render email
        html = email.export_str()
        
        # Verify all widgets are in output
        assert "Test Report" in html
        assert "John" in html
        assert "Jane" in html
        assert "75%" in html or "75.0%" in html
    
    def test_dataframe_to_table_integration(self):
        """Test DataFrame and table widget integration"""
        # Create test data
        df = pd.DataFrame({
            'Product': ['A', 'B', 'C'],
            'Sales': [100, 200, 150],
            'Price': [10.5, 20.0, 15.8]
        })
        
        email = Email("Data Report")
        
        # Use convenience method to create table from DataFrame
        email.add_table_from_df(df, title="Product Sales Data")
        
        html = email.export_str()
        
        # Verify data is correctly rendered
        assert "Product Sales Data" in html
        assert "Product" in html and "Sales" in html and "Price" in html
        assert "100" in html and "200" in html and "150" in html
    
    @pytest.mark.integration
    def test_template_engine_integration(self):
        """Test template engine integration"""
        email = Email("Template Test")
        
        # Use custom template
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
    """End-to-end tests"""
    
    @pytest.mark.e2e
    def test_complete_report_generation(self):
        """Test complete report generation workflow"""
        # 1. Create email
        email = Email("Monthly Business Report")
        
        # 2. Add title and description
        email.add_title("January 2024 Business Report", TextType.TITLE_LARGE)
        email.add_text("This report contains key business metrics and analysis.")
        
        # 3. Add key metrics
        email.add_card("Total Revenue", "$1,250,000", "💰")
        email.add_card("New Users", "2,847", "👥")
        
        # 4. Add detailed data table
        data = [
            ["Product A", "$500,000", "1,200"],
            ["Product B", "$750,000", "1,647"]
        ]
        email.add_table_from_data(data, ["Product", "Revenue", "Sales"])
        
        # 5. Add progress metrics
        email.add_progress(85, "Goal Completion", ProgressTheme.SUCCESS)
        
        # 6. Add alert
        email.add_alert("Need to focus on Product A inventory next month", AlertType.WARNING)
        
        # 7. Export to HTML
        with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as f:
            email.export_html(f.name)
            
            # 8. Verify file generation
            output_path = Path(f.name)
            assert output_path.exists()
            
            # 9. Verify content completeness
            content = output_path.read_text(encoding='utf-8')
            assert "Monthly Business Report" in content
            assert "$1,250,000" in content
            assert "Product A" in content
            assert "85%" in content or "85.0%" in content
            assert "inventory" in content
            
            # 10. Verify HTML structure
            assert "<html" in content
            assert "</html>" in content
            assert "<head>" in content
            assert "<body>" in content
    
    @pytest.mark.e2e
    @pytest.mark.slow
    def test_large_dataset_performance(self):
        """Test large dataset performance"""
        import time
        
        # Create large amount of data
        email = Email("Large Data Test")
        
        # Add large table
        large_data = []
        for i in range(1000):
            large_data.append([f"Item{i}", f"Value{i}", f"Description{i}"])
        
        start_time = time.time()
        email.add_table_from_data(large_data, ["Item", "Value", "Description"])
        
        # Rendering time should be within reasonable range
        html = email.export_str()
        end_time = time.time()
        
        # Performance assertions (adjust based on actual conditions)
        assert (end_time - start_time) < 10.0  # Should complete within 10 seconds
        assert len(html) > 10000  # Ensure content is generated
        assert "Item999" in html  # Ensure all data is included
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
    """Performance tests"""
    
    @pytest.mark.performance
    def test_rendering_speed(self):
        """Test rendering speed"""
        email = Email("Performance Test")
        
        # Add multiple widgets
        for i in range(100):
            email.add_text(f"Text content {i}")
        
        # Measure rendering time
        start_time = time.perf_counter()
        html = email.export_str()
        end_time = time.perf_counter()
        
        render_time = end_time - start_time
        
        # Assert rendering time
        assert render_time < 1.0, f"Rendering time too long: {render_time:.3f}s"
        assert len(html) > 1000, "Output content too short"
    
    @pytest.mark.performance
    def test_memory_usage(self):
        """Test memory usage"""
        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss
        
        # Create many objects
        emails = []
        for i in range(50):
            email = Email(f"Test Email {i}")
            for j in range(20):
                email.add_text(f"Content {i}-{j}")
            emails.append(email)
        
        # Check memory growth
        peak_memory = process.memory_info().rss
        memory_increase = peak_memory - initial_memory
        
        # Assert reasonable memory usage (adjust based on actual conditions)
        assert memory_increase < 100 * 1024 * 1024, f"Memory usage too high: {memory_increase / 1024 / 1024:.1f}MB"
    
    @pytest.mark.performance
    def test_cache_effectiveness(self):
        """Test cache effectiveness"""
        from email_widget.core.cache import Cache
        
        cache = Cache(max_size=100)
        
        # First access (not cached)
        start_time = time.perf_counter()
        result1 = cache.get_or_set("test_key", lambda: expensive_operation())
        first_time = time.perf_counter() - start_time
        
        # Second access (cached)
        start_time = time.perf_counter()
        result2 = cache.get("test_key")
        second_time = time.perf_counter() - start_time
        
        # Cache should significantly improve performance
        assert result1 == result2
        assert second_time < first_time / 10, "Cache did not significantly improve performance"

def expensive_operation():
    """Simulate expensive operation"""
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
# Set coverage requirements in pytest.ini
[tool:pytest]
addopts = --cov-fail-under=90

# Exclude certain files
--cov-config=.coveragerc

# .coveragerc file content
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
Test runner script
"""
import subprocess
import sys
import argparse
from pathlib import Path

def run_command(cmd, description):
    """Run command and check result"""
    print(f"\n🔄 {description}...")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✅ {description} successful")
        if result.stdout:
            print(result.stdout)
    else:
        print(f"❌ {description} failed")
        print(result.stderr)
        return False
    return True

def main():
    parser = argparse.ArgumentParser(description="Run EmailWidget tests")
    parser.add_argument("--unit", action="store_true", help="Run only unit tests")
    parser.add_argument("--integration", action="store_true", help="Run only integration tests")
    parser.add_argument("--e2e", action="store_true", help="Run only end-to-end tests")
    parser.add_argument("--performance", action="store_true", help="Run only performance tests")
    parser.add_argument("--coverage", action="store_true", help="Generate coverage report")
    parser.add_argument("--html", action="store_true", help="Generate HTML report")
    
    args = parser.parse_args()
    
    # Base test command
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
    
    # Ensure reports directory exists
    Path("reports").mkdir(exist_ok=True)
    
    # Run tests
    success = run_command(pytest_cmd, "Running tests")
    
    if success:
        print("\n🎉 All tests passed!")
    else:
        print("\n💥 Tests failed!")
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
# Good test names
def test_set_title_with_valid_string_updates_title():
    pass

def test_render_returns_html_with_title_content():
    pass

def test_add_widget_with_none_raises_type_error():
    pass

# Avoid these test names
def test_title():  # Too vague
    pass

def test_1():  # Meaningless
    pass
```

### Test Data

```python
# Use meaningful test data
def test_user_registration():
    user_data = {
        "name": "John Doe",
        "email": "john@example.com",
        "age": 25
    }
    # Instead of
    # user_data = {"a": "b", "c": "d"}
```

### Exception Testing

```python
def test_invalid_input_handling():
    """Test handling of invalid input"""
    widget = TextWidget()
    
    # Test specific exception type and message
    with pytest.raises(ValueError, match="Content cannot be empty"):
        widget.set_content("")
    
    with pytest.raises(TypeError, match="Content must be a string"):
        widget.set_content(123)
```

## 🎉 Summary

Following this testing guide, you will be able to:

1. **Write high-quality tests** - Cover various scenarios and edge cases
2. **Ensure code quality** - Discover issues through automated testing
3. **Improve development efficiency** - Quickly verify correctness of changes
4. **Maintain code stability** - Prevent regression errors

Now start writing tests for your code! Good testing habits will make your code more robust and maintainable. 🧪✨