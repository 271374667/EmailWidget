# 开发环境搭建

本指南将帮助您在 Windows 10 64位 系统上搭建 EmailWidget 的开发环境。

## 🎯 环境要求

### 系统要求
- **操作系统**: Windows 10 64位 (版本 1903 或更高)
- **内存**: 至少 4GB RAM (推荐 8GB+)
- **存储**: 至少 2GB 可用空间
- **网络**: 稳定的互联网连接（用于下载依赖）

### 必需软件
| 软件 | 版本要求 | 用途 |
|------|----------|------|
| Python | 3.10+ | 核心开发语言 |
| Git | 最新版本 | 版本控制 |
| 代码编辑器 | - | 代码编写（推荐 VS Code 或 PyCharm） |

## 📥 安装基础软件

### 1. 安装 Python 3.10+

#### 方法一：从官网下载（推荐）
1. 访问 [Python 官网](https://www.python.org/downloads/)
2. 下载 Python 3.10 或更高版本的 Windows x86-64 安装包
3. 运行安装程序，**确保勾选**：
   - ✅ "Add Python to PATH"
   - ✅ "Install pip"

#### 方法二：使用 Chocolatey
```powershell
# 以管理员身份运行 PowerShell
# 首先安装 Chocolatey（如果没有）
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# 安装 Python
choco install python3 -y
```

#### 验证安装
```powershell
# 检查 Python 版本
python --version
# 应该显示：Python 3.10.x 或更高

# 检查 pip 版本
pip --version
# 应该显示 pip 版本信息
```

### 2. 安装 Git

#### 方法一：从官网下载
1. 访问 [Git 官网](https://git-scm.com/download/win)
2. 下载 64位 Windows 版本
3. 运行安装程序，使用默认设置即可

#### 方法二：使用 Chocolatey
```powershell
choco install git -y
```

#### 验证安装
```powershell
git --version
# 应该显示：git version x.x.x
```

### 3. 选择代码编辑器

#### 推荐选项

**Visual Studio Code（推荐）**
- 免费、轻量、插件丰富
- [下载地址](https://code.visualstudio.com/)

```powershell
# 使用 Chocolatey 安装
choco install vscode -y
```

**PyCharm Community Edition**
- 专业的 Python IDE
- [下载地址](https://www.jetbrains.com/pycharm/download/)

```powershell
# 使用 Chocolatey 安装
choco install pycharm-community -y
```

## 🔧 项目环境搭建

### 1. 克隆项目

```powershell
# 创建开发目录
mkdir C:\Dev
cd C:\Dev

# 克隆项目（请替换为实际的仓库地址）
git clone https://github.com/your-username/EmailWidget.git
cd EmailWidget
```

### 2. 创建虚拟环境

#### 使用 venv（Python 内置）
```powershell
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
.\venv\Scripts\Activate.ps1

# 如果执行策略限制，先运行：
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### 使用 conda（如果安装了 Anaconda）
```powershell
# 创建环境
conda create -n emailwidget python=3.10 -y

# 激活环境
conda activate emailwidget
```

### 3. 安装项目依赖

```powershell
# 确保虚拟环境已激活
# 升级 pip 到最新版本
python -m pip install --upgrade pip

# 安装项目依赖
pip install -e .

# 安装开发依赖
pip install -r requirements-dev.txt

# 或者如果使用 pyproject.toml
pip install -e .[dev]
```

### 4. 验证安装

```powershell
# 运行测试确保环境正常
python -m pytest tests/ -v

# 检查代码质量工具
python -m pylint email_widget/

# 运行示例代码
python demo/example.py
```

## 🛠️ IDE 配置

### Visual Studio Code 配置

#### 1. 安装推荐插件
```json
{
  "recommendations": [
    "ms-python.python",           // Python 支持
    "ms-python.pylint",           // 代码检查
    "ms-python.black-formatter",  // 代码格式化
    "ms-python.isort",            // 导入排序
    "ms-toolsai.jupyter",         // Jupyter 支持
    "redhat.vscode-yaml",         // YAML 支持
    "yzhang.markdown-all-in-one", // Markdown 支持
    "ms-vscode.test-adapter-converter" // 测试适配器
  ]
}
```

#### 2. 工作区配置 (.vscode/settings.json)
```json
{
    "python.defaultInterpreterPath": "./venv/Scripts/python.exe",
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": [
        "tests"
    ],
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": [
        "--line-length=88"
    ],
    "python.sortImports.args": [
        "--profile",
        "black"
    ],
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    },
    "files.associations": {
        "*.md": "markdown"
    }
}
```

#### 3. 任务配置 (.vscode/tasks.json)
```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "运行测试",
            "type": "shell",
            "command": "${workspaceFolder}/venv/Scripts/python.exe",
            "args": ["-m", "pytest", "tests/", "-v"],
            "group": "test",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "shared"
            }
        },
        {
            "label": "代码检查",
            "type": "shell",
            "command": "${workspaceFolder}/venv/Scripts/python.exe",
            "args": ["-m", "pylint", "email_widget/"],
            "group": "build",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "shared"
            }
        },
        {
            "label": "格式化代码",
            "type": "shell",
            "command": "${workspaceFolder}/venv/Scripts/python.exe",
            "args": ["-m", "black", "email_widget/", "tests/"],
            "group": "build"
        }
    ]
}
```

### PyCharm 配置

#### 1. 设置解释器
1. 打开 **File → Settings → Project → Python Interpreter**
2. 点击齿轮图标 → **Add**
3. 选择 **Existing environment**
4. 选择 `EmailWidget\venv\Scripts\python.exe`

#### 2. 配置代码质量工具
1. **File → Settings → Tools → External Tools**
2. 添加以下工具：

**Black 格式化**
- Name: Black Format
- Program: `$ProjectFileDir$\venv\Scripts\python.exe`
- Arguments: `-m black $FilePath$`
- Working directory: `$ProjectFileDir$`

**Pylint 检查**
- Name: Pylint Check
- Program: `$ProjectFileDir$\venv\Scripts\python.exe`
- Arguments: `-m pylint $FilePath$`
- Working directory: `$ProjectFileDir$`

## 🧪 验证开发环境

### 运行完整测试套件
```powershell
# 激活虚拟环境
.\venv\Scripts\Activate.ps1

# 运行所有测试
python -m pytest tests/ -v --cov=email_widget

# 运行特定测试
python -m pytest tests/test_email.py -v

# 运行代码质量检查
python -m pylint email_widget/
python -m black --check email_widget/
python -m isort --check-only email_widget/
```

### 创建测试报告
```powershell
# 创建一个简单的测试报告
python -c "
from email_widget import Email
email = Email('测试报告')
email.add_title('环境验证成功')
email.add_text('EmailWidget 开发环境已正确配置！')
email.export_html('test_output.html')
print('✅ 测试报告已生成：test_output.html')
"
```

## 🔍 常见问题解决

### Python 相关问题

**Q: 提示 "python 不是内部或外部命令"**
```powershell
# 检查 PATH 环境变量
echo $env:PATH
# 应该包含 Python 安装路径

# 手动添加到 PATH（临时）
$env:PATH += ";C:\Users\你的用户名\AppData\Local\Programs\Python\Python310"
```

**Q: pip 安装速度慢**
```powershell
# 使用国内镜像源
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ package_name

# 或配置永久镜像源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/
```

### 虚拟环境问题

**Q: 无法激活虚拟环境**
```powershell
# 检查执行策略
Get-ExecutionPolicy

# 设置执行策略
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 然后重新激活
.\venv\Scripts\Activate.ps1
```

**Q: 虚拟环境路径问题**
```powershell
# 确保在项目根目录
pwd
# 应该显示 EmailWidget 项目目录

# 重新创建虚拟环境
Remove-Item -Recurse -Force venv
python -m venv venv
```

### Git 相关问题

**Q: Git 克隆失败**
```powershell
# 检查网络连接
ping github.com

# 使用 HTTPS 而不是 SSH
git clone https://github.com/user/repo.git

# 配置代理（如果需要）
git config --global http.proxy http://proxy-server:port
```

### IDE 相关问题

**Q: VS Code 无法识别 Python 解释器**
1. 按 `Ctrl+Shift+P` 打开命令面板
2. 输入 "Python: Select Interpreter"
3. 选择项目虚拟环境中的 Python

**Q: 代码格式化不工作**
1. 确保安装了 Black 扩展
2. 检查 settings.json 配置
3. 手动运行格式化：`Ctrl+Shift+I`

## 📊 性能优化建议

### 提升开发效率
1. **SSD 硬盘** - 显著提升文件读写速度
2. **充足内存** - 至少 8GB，推荐 16GB
3. **关闭杀毒软件实时扫描** - 针对开发目录
4. **使用 Windows Terminal** - 更好的命令行体验

### 优化 Python 环境
```powershell
# 升级 pip 到最新版本
python -m pip install --upgrade pip

# 使用更快的包管理器
pip install uv
# 然后使用 uv 代替 pip
uv pip install package_name
```

## 🚀 下一步

环境搭建完成后，您可以：

1. 📖 **阅读[贡献指南](contributing.md)** - 了解贡献流程
2. 🧩 **学习[创建 Widget](creating-widgets.md)** - 开发自定义组件
3. 🧪 **查看[测试指南](testing.md)** - 编写和运行测试
4. 🔍 **浏览 GitHub Issues** - 找到感兴趣的任务
5. 💻 **开始编码** - 创建您的第一个贡献！

恭喜！您的 EmailWidget 开发环境已经搭建完成。现在可以开始愉快的开发之旅了！ 🎉 