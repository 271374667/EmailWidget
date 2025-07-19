# Development Environment Setup

This guide will help you set up a development environment for EmailWidget on Windows 10 64-bit system.

## 🎯 Environment Requirements

### System Requirements
- **Operating System**: Windows 10 64-bit (version 1903 or higher)
- **Memory**: At least 4GB RAM (8GB+ recommended)
- **Storage**: At least 2GB available space
- **Network**: Stable internet connection (for downloading dependencies)

### Required Software
| Software | Version Requirement | Purpose |
|----------|-------------------|---------|
| Python | 3.10+ | Core development language |
| Git | Latest version | Version control |
| Code Editor | - | Code editing (VS Code or PyCharm recommended) |

## 📥 Installing Base Software

### 1. Installing Python 3.10+

#### Method 1: Download from Official Website (Recommended)
1. Visit [Python Official Website](https://www.python.org/downloads/)
2. Download Python 3.10 or higher Windows x86-64 installer
3. Run the installer and **make sure to check**:
   - ✅ "Add Python to PATH"
   - ✅ "Install pip"

#### Method 2: Using Chocolatey
```powershell
# Run PowerShell as Administrator
# First install Chocolatey (if not already installed)
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install Python
choco install python3 -y
```

#### Verify Installation
```powershell
# Check Python version
python --version
# Should display: Python 3.10.x or higher

# Check pip version
pip --version
# Should display pip version information
```

### 2. Installing Git

#### Method 1: Download from Official Website
1. Visit [Git Official Website](https://git-scm.com/download/win)
2. Download 64-bit Windows version
3. Run the installer with default settings

#### Method 2: Using Chocolatey
```powershell
choco install git -y
```

#### Verify Installation
```powershell
git --version
# Should display: git version x.x.x
```

### 3. Choose Code Editor

#### Recommended Options

**Visual Studio Code (Recommended)**
- Free, lightweight, rich plugin ecosystem
- [Download Link](https://code.visualstudio.com/)

```powershell
# Install using Chocolatey
choco install vscode -y
```

**PyCharm Community Edition**
- Professional Python IDE
- [Download Link](https://www.jetbrains.com/pycharm/download/)

```powershell
# Install using Chocolatey
choco install pycharm-community -y
```

## 🔧 Project Environment Setup

### 1. Clone Project

```powershell
# Create development directory
mkdir C:\Dev
cd C:\Dev

# Clone project (replace with actual repository URL)
git clone https://github.com/your-username/EmailWidget.git
cd EmailWidget
```

### 2. Create Virtual Environment

#### Using venv (Python built-in)
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# If execution policy restrictions, run first:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Using conda (if Anaconda is installed)
```powershell
# Create environment
conda create -n emailwidget python=3.10 -y

# Activate environment
conda activate emailwidget
```

### 3. Install Project Dependencies

```powershell
# Make sure virtual environment is activated
# Upgrade pip to latest version
python -m pip install --upgrade pip

# Install project dependencies
pip install -e .

# Install development dependencies
pip install -r requirements-dev.txt

# Or if using pyproject.toml
pip install -e .[dev]
```

### 4. Verify Installation

```powershell
# Run tests to ensure environment is working
python -m pytest tests/ -v

# Check code quality tools
python -m pylint email_widget/

# Run example code
python demo/example.py
```

## 🛠️ IDE Configuration

### Visual Studio Code Configuration

#### 1. Install Recommended Extensions
```json
{
  "recommendations": [
    "ms-python.python",           // Python support
    "ms-python.pylint",           // Code linting
    "ms-python.black-formatter",  // Code formatting
    "ms-python.isort",            // Import sorting
    "ms-toolsai.jupyter",         // Jupyter support
    "redhat.vscode-yaml",         // YAML support
    "yzhang.markdown-all-in-one", // Markdown support
    "ms-vscode.test-adapter-converter" // Test adapter
  ]
}
```

#### 2. Workspace Configuration (.vscode/settings.json)
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

#### 3. Task Configuration (.vscode/tasks.json)
```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Run Tests",
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
            "label": "Code Lint",
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
            "label": "Format Code",
            "type": "shell",
            "command": "${workspaceFolder}/venv/Scripts/python.exe",
            "args": ["-m", "black", "email_widget/", "tests/"],
            "group": "build"
        }
    ]
}
```

### PyCharm Configuration

#### 1. Set Interpreter
1. Open **File → Settings → Project → Python Interpreter**
2. Click gear icon → **Add**
3. Select **Existing environment**
4. Choose `EmailWidget\venv\Scripts\python.exe`

#### 2. Configure Code Quality Tools
1. **File → Settings → Tools → External Tools**
2. Add the following tools:

**Black Formatting**
- Name: Black Format
- Program: `$ProjectFileDir$\venv\Scripts\python.exe`
- Arguments: `-m black $FilePath$`
- Working directory: `$ProjectFileDir$`

**Pylint Check**
- Name: Pylint Check
- Program: `$ProjectFileDir$\venv\Scripts\python.exe`
- Arguments: `-m pylint $FilePath$`
- Working directory: `$ProjectFileDir$`

## 🧪 Verify Development Environment

### Run Complete Test Suite
```powershell
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Run all tests
python -m pytest tests/ -v --cov=email_widget

# Run specific tests
python -m pytest tests/test_email.py -v

# Run code quality checks
python -m pylint email_widget/
python -m black --check email_widget/
python -m isort --check-only email_widget/
```

### Create Test Report
```powershell
# Create a simple test report
python -c "
from email_widget import Email
email = Email('Test Report')
email.add_title('Environment Verification Successful')
email.add_text('EmailWidget development environment has been configured correctly!')
email.export_html('test_output.html')
print('✅ Test report generated: test_output.html')
"
```

## 🔍 Common Issue Resolution

### Python-related Issues

**Q: "python is not recognized as an internal or external command"**
```powershell
# Check PATH environment variable
echo $env:PATH
# Should include Python installation path

# Manually add to PATH (temporary)
$env:PATH += ";C:\Users\YourUsername\AppData\Local\Programs\Python\Python310"
```

**Q: Slow pip installation**
```powershell
# Use domestic mirror source
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ package_name

# Or configure permanent mirror source
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/
```

### Virtual Environment Issues

**Q: Cannot activate virtual environment**
```powershell
# Check execution policy
Get-ExecutionPolicy

# Set execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then reactivate
.\venv\Scripts\Activate.ps1
```

**Q: Virtual environment path issues**
```powershell
# Make sure in project root directory
pwd
# Should show EmailWidget project directory

# Recreate virtual environment
Remove-Item -Recurse -Force venv
python -m venv venv
```

### Git-related Issues

**Q: Git clone failure**
```powershell
# Check network connection
ping github.com

# Use HTTPS instead of SSH
git clone https://github.com/user/repo.git

# Configure proxy (if needed)
git config --global http.proxy http://proxy-server:port
```

### IDE-related Issues

**Q: VS Code cannot recognize Python interpreter**
1. Press `Ctrl+Shift+P` to open command palette
2. Type "Python: Select Interpreter"
3. Select Python from project virtual environment

**Q: Code formatting not working**
1. Make sure Black extension is installed
2. Check settings.json configuration
3. Manually run formatting: `Ctrl+Shift+I`

## 📊 Performance Optimization Suggestions

### Improve Development Efficiency
1. **SSD Hard Drive** - Significantly improves file I/O speed
2. **Sufficient Memory** - At least 8GB, 16GB recommended
3. **Disable Real-time Antivirus Scanning** - For development directories
4. **Use Windows Terminal** - Better command line experience

### Optimize Python Environment
```powershell
# Upgrade pip to latest version
python -m pip install --upgrade pip

# Use faster package manager
pip install uv
# Then use uv instead of pip
uv pip install package_name
```

## 🚀 Next Steps

After completing environment setup, you can:

1. 📖 **Read [Contributing Guide](contributing.md)** - Learn contribution process
2. 🧩 **Learn [Creating Widgets](creating-widgets.md)** - Develop custom components
3. 🧪 **Check [Testing Guide](testing.md)** - Write and run tests
4. 🔍 **Browse GitHub Issues** - Find interesting tasks
5. 💻 **Start Coding** - Create your first contribution!

Congratulations! Your EmailWidget development environment is now set up. Happy coding! 🎉