# 发布流程

本指南详细说明 EmailWidget 项目的版本管理策略、发布流程和最佳实践。

## 🎯 版本管理策略

### 语义化版本控制

EmailWidget 遵循 [语义化版本控制 2.0.0](https://semver.org/lang/zh-CN/) 规范：

```
主版本号.次版本号.修订号 (MAJOR.MINOR.PATCH)
```

**版本递增规则：**
- **主版本号 (MAJOR)** - 不兼容的 API 变更
- **次版本号 (MINOR)** - 向下兼容的功能增加
- **修订号 (PATCH)** - 向下兼容的错误修复

### 版本示例

| 版本 | 类型 | 说明 |
|------|------|------|
| 1.0.0 | 主版本 | 首个稳定版本 |
| 1.1.0 | 次版本 | 新增 ChartWidget 组件 |
| 1.1.1 | 修订 | 修复 TableWidget 样式问题 |
| 2.0.0 | 主版本 | 重构 Widget 基类，API 不兼容 |
| 2.1.0-alpha.1 | 预发布 | Alpha 版本 |
| 2.1.0-beta.1 | 预发布 | Beta 版本 |
| 2.1.0-rc.1 | 预发布 | Release Candidate |

### 预发布版本

对于重大更新，使用预发布版本进行测试：

- **Alpha (α)** - 内部测试版本，功能不完整
- **Beta (β)** - 公开测试版本，功能基本完整
- **RC (Release Candidate)** - 发布候选版本，接近最终版本

## 🌟 分支策略

### Git Flow 工作流

```
main (主分支)
├── develop (开发分支)
│   ├── feature/new-widget (功能分支)
│   ├── feature/chart-enhancement (功能分支)
│   └── ...
├── release/v1.2.0 (发布分支)
├── hotfix/urgent-bug-fix (热修复分支)
└── ...
```

### 分支说明

**main 分支**
- 始终保持稳定状态
- 只接受来自 release 和 hotfix 分支的合并
- 每次合并都对应一个发布版本
- 使用 tag 标记版本

**develop 分支**
- 开发分支，集成最新功能
- 功能分支的合并目标
- 定期合并到 release 分支

**feature/* 分支**
- 功能开发分支
- 从 develop 分支创建
- 完成后合并回 develop 分支

**release/* 分支**
- 发布准备分支
- 从 develop 分支创建
- 只进行 bug 修复和发布准备
- 完成后合并到 main 和 develop

**hotfix/* 分支**
- 紧急修复分支
- 从 main 分支创建
- 修复后合并到 main 和 develop

## 🚀 发布流程

### 1. 发布前准备

#### 检查代码质量
```powershell
# 运行所有测试
python -m pytest tests/ -v

# 检查代码覆盖率
python -m pytest --cov=email_widget --cov-fail-under=90

# 代码风格检查
python -m pylint email_widget/
python -m black --check email_widget/
python -m isort --check-only email_widget/

# 类型检查
python -m mypy email_widget/
```

#### 检查依赖
```powershell
# 检查依赖安全性
pip audit

# 检查过时依赖
pip list --outdated

# 更新依赖版本
pip-review --local --interactive
```

#### 更新文档
- 确保 API 文档是最新的
- 更新示例代码
- 检查 README.md
- 更新变更日志

### 2. 创建发布分支

```powershell
# 从 develop 创建发布分支
git checkout develop
git pull origin develop
git checkout -b release/v1.2.0

# 推送发布分支
git push -u origin release/v1.2.0
```

### 3. 版本号更新

#### 更新 pyproject.toml
```toml
[project]
name = "email-widget"
version = "1.2.0"
description = "Create beautiful HTML email reports with Python"
# ... 其他配置
```

#### 更新 __init__.py
```python
# email_widget/__init__.py
__version__ = "1.2.0"
__author__ = "EmailWidget Team"
__email__ = "support@emailwidget.com"

# ... 其他导入
```

#### 更新 CHANGELOG.md
```markdown
# 变更日志

## [1.2.0] - 2024-01-15

### 新增
- 新增 ChartWidget 组件支持图表展示
- 添加深色主题支持
- 新增移动端响应式布局

### 改进
- 优化 TableWidget 渲染性能
- 改进缓存机制，提升 50% 渲染速度
- 增强错误处理和日志记录

### 修复
- 修复 ProgressWidget 在 Outlook 中的显示问题
- 解决中文字符编码问题
- 修复内存泄漏问题

### 已知问题
- 在某些老版本 Outlook 中图表可能显示异常

## [1.1.1] - 2024-01-01

### 修复
- 修复 TableWidget 边框样式问题
- 解决 Email 导出时的路径问题
```

### 4. 发布测试

#### 构建测试
```powershell
# 清理构建目录
if (Test-Path dist) { Remove-Item -Recurse -Force dist }
if (Test-Path build) { Remove-Item -Recurse -Force build }

# 构建分发包
python -m build

# 检查构建结果
python -m twine check dist/*
```

#### 安装测试
```powershell
# 在虚拟环境中测试安装
python -m venv test_env
test_env\Scripts\Activate.ps1

# 从构建包安装
pip install dist/email_widget-1.2.0-py3-none-any.whl

# 运行基本测试
python -c "from email_widget import Email; print('安装成功')"

# 清理测试环境
deactivate
Remove-Item -Recurse -Force test_env
```

#### 集成测试
```powershell
# 运行完整测试套件
python -m pytest tests/ -v --tb=short

# 运行性能测试
python -m pytest tests/performance/ -v
```

### 5. 代码审查和批准

#### 创建 Pull Request
- 从 release/v1.2.0 到 main 分支
- 详细描述本次发布的变更
- 附加测试报告和性能基准

#### 审查清单
- [ ] 所有测试通过
- [ ] 代码覆盖率 ≥ 90%
- [ ] 文档已更新
- [ ] 变更日志已更新
- [ ] 版本号已正确更新
- [ ] 构建包测试通过
- [ ] 性能测试通过
- [ ] 安全扫描通过

### 6. 正式发布

#### 合并发布分支
```powershell
# 合并到 main 分支
git checkout main
git pull origin main
git merge --no-ff release/v1.2.0
git push origin main

# 合并回 develop 分支
git checkout develop
git pull origin develop
git merge --no-ff release/v1.2.0
git push origin develop

# 删除发布分支
git branch -d release/v1.2.0
git push origin --delete release/v1.2.0
```

#### 创建 Git 标签
```powershell
# 创建带注释的标签
git tag -a v1.2.0 -m "Release version 1.2.0

新增功能:
- ChartWidget 组件
- 深色主题支持
- 移动端响应式布局

性能改进:
- 渲染速度提升 50%
- 优化内存使用

Bug 修复:
- 修复 Outlook 兼容性问题
- 解决中文编码问题"

# 推送标签
git push origin v1.2.0
```

#### 发布到 PyPI
```powershell
# 发布到测试 PyPI（可选）
python -m twine upload --repository testpypi dist/*

# 发布到正式 PyPI
python -m twine upload dist/*
```

#### GitHub Release
1. 访问 GitHub 仓库的 Releases 页面
2. 点击 "Create a new release"
3. 选择刚创建的标签 v1.2.0
4. 填写发布标题和说明
5. 上传构建的分发包
6. 发布 Release

### 7. 发布后续工作

#### 验证发布
```powershell
# 从 PyPI 安装验证
pip install --upgrade email-widget

# 检查版本
python -c "import email_widget; print(email_widget.__version__)"
```

#### 更新文档网站
```powershell
# 构建和部署文档
mkdocs gh-deploy --force
```

#### 通知用户
- 发送发布公告邮件
- 更新项目主页
- 在社交媒体发布消息
- 通知主要用户和合作伙伴

## 🔥 热修复流程

### 紧急 Bug 修复

当生产环境出现严重问题时，使用热修复流程：

```powershell
# 1. 从 main 分支创建热修复分支
git checkout main
git pull origin main
git checkout -b hotfix/urgent-security-fix

# 2. 修复问题
# ... 编写修复代码 ...

# 3. 更新版本号（修订号 +1）
# 例如：从 1.2.0 更新到 1.2.1

# 4. 运行测试
python -m pytest tests/ -v

# 5. 提交修复
git add .
git commit -m "hotfix: 修复安全漏洞 CVE-2024-0001"

# 6. 合并到 main 和 develop
git checkout main
git merge --no-ff hotfix/urgent-security-fix
git push origin main

git checkout develop
git merge --no-ff hotfix/urgent-security-fix
git push origin develop

# 7. 创建标签并发布
git tag -a v1.2.1 -m "Hotfix release 1.2.1 - Security fix"
git push origin v1.2.1

# 8. 清理分支
git branch -d hotfix/urgent-security-fix
```

## 📊 发布指标

### 关键指标监控

**发布频率**
- 主版本：6-12 个月
- 次版本：1-2 个月
- 修订版本：按需发布

**质量指标**
- 测试覆盖率 ≥ 90%
- 代码质量评分 ≥ 8.0/10
- 已知 Bug 数量 ≤ 5

**性能指标**
- 渲染速度回归 ≤ 5%
- 内存使用增长 ≤ 10%
- 包大小增长 ≤ 20%

### 发布后监控

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

## 🎯 发布最佳实践

### 发布前检查清单

**代码质量**
- [ ] 所有单元测试通过
- [ ] 集成测试通过
- [ ] 端到端测试通过
- [ ] 代码覆盖率达标
- [ ] 静态代码分析通过
- [ ] 安全扫描无高危漏洞

**文档更新**
- [ ] API 文档最新
- [ ] 用户指南更新
- [ ] 示例代码有效
- [ ] 变更日志完整
- [ ] README.md 更新

**版本管理**
- [ ] 版本号符合语义化规范
- [ ] 标签命名正确
- [ ] 分支合并无冲突
- [ ] 构建包完整

**发布准备**
- [ ] 依赖版本锁定
- [ ] 性能基准测试
- [ ] 兼容性测试
- [ ] 发布说明准备

### 回滚计划

如果发布后发现严重问题，按以下步骤回滚：

```powershell
# 1. 紧急从 PyPI 撤回（如果可能）
# 联系 PyPI 管理员或使用 yank 功能

# 2. 创建热修复版本
git checkout main
git checkout -b hotfix/rollback-v1.2.0

# 3. 回滚有问题的更改
git revert <问题提交的哈希>

# 4. 发布回滚版本
# 更新版本号到 1.2.1
# 按正常流程发布

# 5. 通知用户升级
echo "发送紧急升级通知"
```

## 📞 发布支持

### 发布团队职责

**发布经理**
- 协调整个发布流程
- 确保时间表遵守
- 沟通发布状态

**质量保证**
- 执行测试计划
- 验证功能完整性
- 确认性能指标

**文档团队**
- 更新用户文档
- 准备发布说明
- 维护示例代码

**运维团队**
- 监控发布过程
- 处理基础设施问题
- 执行回滚计划

### 发布沟通

**内部沟通**
- 发布前一周：发布预告
- 发布当天：发布进度更新
- 发布后：发布总结报告

**外部沟通**
- 发布公告邮件
- GitHub Release Notes
- 社区论坛公告
- 社交媒体发布

## 🎉 总结

完善的发布流程确保：

1. **质量保证** - 多层测试和验证
2. **风险控制** - 完整的回滚计划
3. **用户体验** - 平滑的升级过程
4. **团队协作** - 清晰的职责分工

遵循本发布指南，您将能够安全、高效地发布 EmailWidget 的新版本，为用户提供稳定可靠的功能。🚀✨ 