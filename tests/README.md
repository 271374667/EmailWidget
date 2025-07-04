# EmailWidget 测试套件

本目录包含EmailWidget项目的完整测试套件，涵盖了所有核心模块和Widget组件的功能测试。


## 🚀 运行测试

### 安装测试依赖

```bash
# 安装项目依赖
pip install -r requirements-test.txt

# 或者使用uv（推荐）
uv sync
```

### 基本测试命令

```bash
# 运行所有测试
pytest

# 运行测试并显示详细输出
pytest -v

# 运行特定测试文件
pytest tests/test_email.py

# 运行特定测试类
pytest tests/test_widgets/test_table_widget.py::TestTableWidget

# 运行特定测试方法
pytest tests/test_email.py::TestEmail::test_add_widget
```

### 高级测试选项

```bash
# 安静模式运行（只显示进度）
pytest --quiet

# 显示测试覆盖率
pytest --cov=email_widget

# 生成HTML覆盖率报告
pytest --cov=email_widget --cov-report=html

# 仅运行失败的测试
pytest --lf

# 停止在第一个失败的测试
pytest -x

# 并行运行测试（需要安装pytest-xdist）
pytest -n auto
```

### 按模块运行测试

```bash
# 运行核心模块测试
pytest tests/test_core/

# 运行工具模块测试
pytest tests/test_utils/

# 运行Widget组件测试
pytest tests/test_widgets/

# 运行主Email类测试
pytest tests/test_email.py
```

## 📋 测试内容概览

### Core模块测试

#### Logger测试 (`test_core/test_logger.py`)
- ✅ EmailWidgetLogger单例模式
- ✅ 日志级别配置
- ✅ 便捷函数（debug, info, warning, error, critical）
- ✅ 格式化器配置
- ✅ 环境变量控制

#### Validators测试 (`test_core/test_validators.py`)
- ✅ 非空字符串验证器
- ✅ URL验证器
- ✅ 颜色验证器
- ✅ 尺寸验证器
- ✅ 范围验证器
- ✅ 邮箱验证器
- ✅ 复合验证器

### Utils模块测试

#### ImageUtils测试 (`test_utils/test_image_utils.py`)
- ✅ Base64图片处理
- ✅ MIME类型检测
- ✅ URL请求处理
- ✅ 图片源处理（本地文件、URL、data URI）
- ✅ 缓存机制
- ✅ 错误处理

### Widget组件测试

#### AlertWidget测试
- ✅ 警告类型支持（NOTE, TIP, IMPORTANT, WARNING, CAUTION）
- ✅ 自定义标题和图标
- ✅ 内容验证
- ✅ 样式生成
- ✅ 模板上下文

#### TextWidget测试
- ✅ 文本类型（标题、正文、标题、段落等）
- ✅ 样式设置（字体、颜色、对齐等）
- ✅ 章节编号管理
- ✅ 多行文本处理
- ✅ 链式调用

#### ProgressWidget测试
- ✅ 进度值设置和验证
- ✅ 主题颜色支持
- ✅ 增量/减量操作
- ✅ 百分比计算
- ✅ 自定义样式

#### TableWidget测试
- ✅ DataFrame集成
- ✅ 手动数据设置
- ✅ 表格样式配置
- ✅ 状态单元格
- ✅ 彩色单元格
- ✅ 行/列操作

#### ImageWidget测试
- ✅ 图片URL和路径支持
- ✅ 尺寸设置和验证
- ✅ 标题和描述
- ✅ 边框样式
- ✅ 响应式设计

#### CardWidget测试
- ✅ 卡片内容和状态
- ✅ 图标支持
- ✅ 元数据管理
- ✅ 样式配置
- ✅ 模板渲染

####其他Widget测试
- ✅ CircularProgressWidget - 圆形进度条
- ✅ ColumnWidget - 列布局管理
- ✅ QuoteWidget - 引用组件
- ✅ StatusWidget - 状态信息展示

### Email主类测试

#### 基本功能
- ✅ 邮件初始化和配置
- ✅ Widget管理（添加、移除、清空）
- ✅ 标题、副标题、脚注设置
- ✅ 便捷方法（add_text, add_table等）

#### 导出功能
- ✅ HTML字符串导出
- ✅ HTML文件导出
- ✅ 自定义文件名和路径
- ✅ 模板渲染

#### 集成功能
- ✅ 完整工作流程
- ✅ Widget管理流程
- ✅ 导出工作流程
- ✅ 链式调用

## 🔧 测试配置

### pytest.ini 配置
```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    --strict-markers
    --disable-warnings
    --tb=short
filterwarnings =
    ignore::DeprecationWarning
    ignore::PendingDeprecationWarning
```

### 测试依赖
- `pytest` - 测试框架
- `pytest-cov` - 覆盖率测试
- `pytest-mock` - Mock支持
- `pandas` - DataFrame测试（可选）

## 🐛 调试测试

### 常见问题

1. **导入错误**
   ```bash
   # 确保正确安装项目
   pip install -e .
   ```

2. **依赖缺失**
   ```bash
   # 安装测试依赖
   pip install -r requirements-test.txt
   ```

3. **路径问题**
   ```bash
   # 从项目根目录运行测试
   cd /path/to/EmailWidget
   pytest
   ```

### 调试单个测试
```bash
# 详细输出模式
pytest tests/test_email.py::TestEmail::test_add_widget -v -s

# 使用pdb调试
pytest tests/test_email.py::TestEmail::test_add_widget --pdb

# 捕获所有输出
pytest tests/test_email.py::TestEmail::test_add_widget -s --capture=no
```

## 📊 测试报告

运行测试后可以生成详细的测试报告：

```bash
# 生成JUnit XML报告
pytest --junitxml=test-results.xml

# 生成HTML报告
pytest --html=test-report.html --self-contained-html

# 生成覆盖率报告
pytest --cov=email_widget --cov-report=html --cov-report=term
```

## 🤝 贡献指南

添加新功能时，请确保：

1. ✅ 为新功能编写对应的测试
2. ✅ 所有现有测试仍然通过
3. ✅ 测试覆盖率不降低
4. ✅ 遵循项目的测试风格和约定
5. ✅ 更新相关文档

提交前运行完整测试套件：
```bash
pytest --cov=email_widget --cov-report=term-missing
```