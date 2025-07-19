# Release Process

This guide details the version management strategy, release process, and best practices for the EmailWidget project.

## 🎯 Version Management Strategy

### Semantic Versioning

EmailWidget follows [Semantic Versioning 2.0.0](https://semver.org/) specification:

```
MAJOR.MINOR.PATCH
```

**Version increment rules:**
- **MAJOR** - Incompatible API changes
- **MINOR** - Backward-compatible functionality additions
- **PATCH** - Backward-compatible bug fixes

### Version Examples

| Version | Type | Description |
|---------|------|-------------|
| 1.0.0 | Major | First stable release |
| 1.1.0 | Minor | Added ChartWidget component |
| 1.1.1 | Patch | Fixed TableWidget styling issue |
| 2.0.0 | Major | Refactored Widget base class, API incompatible |
| 2.1.0-alpha.1 | Pre-release | Alpha version |
| 2.1.0-beta.1 | Pre-release | Beta version |
| 2.1.0-rc.1 | Pre-release | Release Candidate |

### Pre-release Versions

For major updates, use pre-release versions for testing:

- **Alpha (α)** - Internal testing version, incomplete features
- **Beta (β)** - Public testing version, features mostly complete
- **RC (Release Candidate)** - Release candidate version, close to final version

## 🌟 Branching Strategy

### Git Flow Workflow

```
main (main branch)
├── develop (development branch)
│   ├── feature/new-widget (feature branch)
│   ├── feature/chart-enhancement (feature branch)
│   └── ...
├── release/v1.2.0 (release branch)
├── hotfix/urgent-bug-fix (hotfix branch)
└── ...
```

### Branch Descriptions

**main branch**
- Always maintains stable state
- Only accepts merges from release and hotfix branches
- Each merge corresponds to a release version
- Uses tags to mark versions

**develop branch**
- Development branch, integrates latest features
- Target for feature branch merges
- Regularly merged to release branch

**feature/* branches**
- Feature development branches
- Created from develop branch
- Merged back to develop branch when complete

**release/* branches**
- Release preparation branches
- Created from develop branch
- Only bug fixes and release preparation
- Merged to main and develop when complete

**hotfix/* branches**
- Emergency fix branches
- Created from main branch
- Merged to main and develop after fixes

## 🚀 Release Process

### 1. Pre-release Preparation

#### Check Code Quality
```powershell
# Run all tests
python -m pytest tests/ -v

# Check code coverage
python -m pytest --cov=email_widget --cov-fail-under=90

# Code style checks
python -m pylint email_widget/
python -m black --check email_widget/
python -m isort --check-only email_widget/

# Type checking
python -m mypy email_widget/
```

#### Check Dependencies
```powershell
# Check dependency security
pip audit

# Check outdated dependencies
pip list --outdated

# Update dependency versions
pip-review --local --interactive
```

#### Update Documentation
- Ensure API documentation is up-to-date
- Update example code
- Check README.md
- Update changelog

### 2. Create Release Branch

```powershell
# Create release branch from develop
git checkout develop
git pull origin develop
git checkout -b release/v1.2.0

# Push release branch
git push -u origin release/v1.2.0
```

### 3. Version Number Updates

#### Update pyproject.toml
```toml
[project]
name = "email-widget"
version = "1.2.0"
description = "Create beautiful HTML email reports with Python"
# ... other configurations
```

#### Update __init__.py
```python
# email_widget/__init__.py
__version__ = "1.2.0"
__author__ = "EmailWidget Team"
__email__ = "support@emailwidget.com"

# ... 其他导入
```

#### Update CHANGELOG.md
```markdown
# Changelog

## [1.2.0] - 2024-01-15

### Added
- New ChartWidget component for chart display
- Dark theme support
- Mobile responsive layout

### Improved
- Optimized TableWidget rendering performance
- Improved caching mechanism, 50% faster rendering
- Enhanced error handling and logging

### Fixed
- Fixed ProgressWidget display issue in Outlook
- Resolved Chinese character encoding issue
- Fixed memory leak issue

### Known Issues
- Charts may display abnormally in some older Outlook versions

## [1.1.1] - 2024-01-01

### Fixed
- Fixed TableWidget border styling issue
- Resolved Email export path issue
```

### 4. Release Testing

#### Build Testing
```powershell
# Clean build directories
if (Test-Path dist) { Remove-Item -Recurse -Force dist }
if (Test-Path build) { Remove-Item -Recurse -Force build }

# Build distribution packages
python -m build

# Check build results
python -m twine check dist/*
```

#### Installation Testing
```powershell
# Test installation in virtual environment
python -m venv test_env
test_env\Scripts\Activate.ps1

# Install from build package
pip install dist/email_widget-1.2.0-py3-none-any.whl

# Run basic test
python -c "from email_widget import Email; print('Installation successful')"

# Clean up test environment
deactivate
Remove-Item -Recurse -Force test_env
```

#### Integration Testing
```powershell
# Run complete test suite
python -m pytest tests/ -v --tb=short

# Run performance tests
python -m pytest tests/performance/ -v
```

### 5. Code Review and Approval

#### Create Pull Request
- From release/v1.2.0 to main branch
- Detailed description of release changes
- Attach test reports and performance benchmarks

#### Review Checklist
- [ ] All tests pass
- [ ] Code coverage ≥ 90%
- [ ] Documentation updated
- [ ] Changelog updated
- [ ] Version number correctly updated
- [ ] Build package tests pass
- [ ] Performance tests pass
- [ ] Security scans pass

### 6. Official Release

#### Merge Release Branch
```powershell
# Merge to main branch
git checkout main
git pull origin main
git merge --no-ff release/v1.2.0
git push origin main

# Merge back to develop branch
git checkout develop
git pull origin develop
git merge --no-ff release/v1.2.0
git push origin develop

# Delete release branch
git branch -d release/v1.2.0
git push origin --delete release/v1.2.0
```

#### Create Git Tag
```powershell
# Create annotated tag
git tag -a v1.2.0 -m "Release version 1.2.0

New Features:
- ChartWidget component
- Dark theme support
- Mobile responsive layout

Performance Improvements:
- 50% faster rendering
- Optimized memory usage

Bug Fixes:
- Fixed Outlook compatibility issues
- Resolved Chinese encoding issues"

# Push tag
git push origin v1.2.0
```

#### Publish to PyPI
```powershell
# Publish to test PyPI (optional)
python -m twine upload --repository testpypi dist/*

# Publish to official PyPI
python -m twine upload dist/*
```

#### GitHub Release
1. Visit GitHub repository's Releases page
2. Click "Create a new release"
3. Select the newly created tag v1.2.0
4. Fill in release title and description
5. Upload built distribution packages
6. Publish Release

### 7. Post-release Work

#### Verify Release
```powershell
# Install from PyPI to verify
pip install --upgrade email-widget

# Check version
python -c "import email_widget; print(email_widget.__version__)"
```

#### Update Documentation Website
```powershell
# Build and deploy documentation
mkdocs gh-deploy --force
```

#### Notify Users
- Send release announcement email
- Update project homepage
- Post on social media
- Notify key users and partners

## 🔥 Hotfix Process

### Emergency Bug Fixes

When serious issues occur in production, use the hotfix process:

```powershell
# 1. Create hotfix branch from main
git checkout main
git pull origin main
git checkout -b hotfix/urgent-security-fix

# 2. Fix the issue
# ... write fix code ...

# 3. Update version number (patch +1)
# e.g., from 1.2.0 to 1.2.1

# 4. Run tests
python -m pytest tests/ -v

# 5. Commit fix
git add .
git commit -m "hotfix: fix security vulnerability CVE-2024-0001"

# 6. Merge to main and develop
git checkout main
git merge --no-ff hotfix/urgent-security-fix
git push origin main

git checkout develop
git merge --no-ff hotfix/urgent-security-fix
git push origin develop

# 7. Create tag and release
git tag -a v1.2.1 -m "Hotfix release 1.2.1 - Security fix"
git push origin v1.2.1

# 8. Clean up branch
git branch -d hotfix/urgent-security-fix
```

## 📊 Release Metrics

### Key Metrics Monitoring

**Release Frequency**
- Major versions: 6-12 months
- Minor versions: 1-2 months
- Patch versions: As needed

**Quality Metrics**
- Test coverage ≥ 90%
- Code quality score ≥ 8.0/10
- Known bugs ≤ 5

**Performance Metrics**
- Rendering speed regression ≤ 5%
- Memory usage growth ≤ 10%
- Package size growth ≤ 20%

### Post-release Monitoring

```python
# scripts/monitor_release.py
import requests
import time
from datetime import datetime

def check_pypi_availability(package_name, version):
    """检查 PyPI 包是否可用"""
    url = f"https://pypi.org/pypi/{package_name}/{version}/json"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"✅ {package_name} v{version} 在 PyPI 上可用")
            return True
        else:
            print(f"❌ {package_name} v{version} 在 PyPI 上不可用")
            return False
    except Exception as e:
        print(f"❌ 检查 PyPI 时出错: {e}")
        return False

def check_installation(package_name, version):
    """检查包是否可以正常安装"""
    import subprocess
    
    try:
        # 创建临时虚拟环境
        subprocess.run(["python", "-m", "venv", "temp_env"], check=True)
        
        # 激活环境并安装包
        if os.name == 'nt':  # Windows
            activate_cmd = r"temp_env\Scripts\Activate.ps1"
            install_cmd = f"temp_env\\Scripts\\pip install {package_name}=={version}"
        else:  # Unix/Linux
            activate_cmd = "source temp_env/bin/activate"
            install_cmd = f"temp_env/bin/pip install {package_name}=={version}"
        
        subprocess.run(install_cmd, shell=True, check=True)
        print(f"✅ {package_name} v{version} 安装成功")
        
        # 清理
        subprocess.run(["rm", "-rf", "temp_env"], check=True)
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ 安装失败: {e}")
        return False

def monitor_release(package_name, version, duration_minutes=30):
    """监控发布状态"""
    print(f"开始监控 {package_name} v{version} 的发布状态...")
    start_time = time.time()
    
    while time.time() - start_time < duration_minutes * 60:
        if check_pypi_availability(package_name, version):
            if check_installation(package_name, version):
                print(f"🎉 {package_name} v{version} 发布成功!")
                return True
        
        print(f"⏳ 等待 30 秒后重试...")
        time.sleep(30)
    
    print(f"⏰ 监控超时 ({duration_minutes} 分钟)")
    return False

if __name__ == "__main__":
    monitor_release("email-widget", "1.2.0")
```

## 🎯 Release Best Practices

### Pre-release Checklist

**Code Quality**
- [ ] All unit tests pass
- [ ] Integration tests pass
- [ ] End-to-end tests pass
- [ ] Code coverage meets standards
- [ ] Static code analysis passes
- [ ] Security scan shows no high-risk vulnerabilities

**Documentation Updates**
- [ ] API documentation up-to-date
- [ ] User guide updated
- [ ] Example code valid
- [ ] Changelog complete
- [ ] README.md updated

**Version Management**
- [ ] Version number follows semantic versioning
- [ ] Tag naming correct
- [ ] Branch merges without conflicts
- [ ] Build packages complete

**Release Preparation**
- [ ] Dependency versions locked
- [ ] Performance benchmark tests
- [ ] Compatibility tests
- [ ] Release notes prepared

### Rollback Plan

If serious issues are discovered after release, rollback following these steps:

```powershell
# 1. Emergency withdrawal from PyPI (if possible)
# Contact PyPI administrators or use yank feature

# 2. Create hotfix version
git checkout main
git checkout -b hotfix/rollback-v1.2.0

# 3. Rollback problematic changes
git revert <hash-of-problematic-commit>

# 4. Release rollback version
# Update version number to 1.2.1
# Follow normal release process

# 5. Notify users to upgrade
echo "Send urgent upgrade notification"
```

## 📞 Release Support

### Release Team Responsibilities

**Release Manager**
- Coordinate entire release process
- Ensure timeline adherence
- Communicate release status

**Quality Assurance**
- Execute test plans
- Verify feature completeness
- Confirm performance metrics

**Documentation Team**
- Update user documentation
- Prepare release notes
- Maintain example code

**DevOps Team**
- Monitor release process
- Handle infrastructure issues
- Execute rollback plans

### Release Communication

**Internal Communication**
- One week before release: Release announcement
- Release day: Release progress updates
- After release: Release summary report

**External Communication**
- Release announcement email
- GitHub Release Notes
- Community forum announcements
- Social media posts

## 🎉 Summary

A comprehensive release process ensures:

1. **Quality Assurance** - Multi-layer testing and validation
2. **Risk Control** - Complete rollback plans
3. **User Experience** - Smooth upgrade process
4. **Team Collaboration** - Clear responsibility division

Following this release guide, you will be able to safely and efficiently release new versions of EmailWidget, providing users with stable and reliable functionality. 🚀✨