# 开发指南

欢迎来到 EmailWidget 开发指南！本指南将帮助您了解如何参与 EmailWidget 项目的开发，从环境搭建到代码贡献的完整流程。

## 🎯 开发指南概览

### 📖 [贡献指南](contributing.md)
学习如何为 EmailWidget 项目做出贡献：
- **代码贡献流程** - Fork、开发、测试、提交 PR
- **问题报告** - Bug 报告和功能请求规范
- **代码规范** - 编码标准和最佳实践
- **文档贡献** - 改进文档和示例

### 🛠️ [开发环境搭建](setup.md)
快速搭建 Windows 10 开发环境：
- **环境要求** - Python、IDE、依赖工具
- **项目克隆** - 代码下载和初始化
- **依赖安装** - 开发和测试依赖
- **验证安装** - 环境检查和测试运行

### 🧩 [创建自定义 Widget](creating-widgets.md)
学习如何开发自定义组件：
- **Widget 架构** - 基类继承和接口设计
- **开发流程** - 从设计到实现的完整步骤
- **最佳实践** - 代码质量和性能优化
- **示例教程** - 完整的 Widget 开发案例

### 🧪 [测试指南](testing.md)
确保代码质量的测试策略：
- **测试框架** - pytest 使用和配置
- **单元测试** - 组件和函数测试
- **集成测试** - 完整功能测试
- **测试覆盖率** - 代码覆盖率要求和报告

### 🚀 [发布流程](release.md)
了解项目版本发布流程：
- **版本管理** - 语义化版本控制
- **发布准备** - 代码检查和文档更新
- **CI/CD 流程** - 自动化构建和测试
- **发布后续** - 版本标签和变更日志

## 🚀 快速开始

### 第一次贡献
如果您是第一次参与开源项目，建议按以下顺序进行：

1. **📖 阅读贡献指南** - 了解项目规范和流程
2. **🛠️ 搭建开发环境** - 准备本地开发环境
3. **🔍 找个小问题** - 从简单的 issue 开始
4. **💻 编写代码** - 实现功能或修复 bug
5. **🧪 运行测试** - 确保代码质量
6. **📝 提交 PR** - 提交 Pull Request

### 开发者路径

#### 🌱 初级开发者
- 修复简单的 bug
- 改进文档和示例
- 添加单元测试
- 优化代码注释

#### 🌿 中级开发者
- 开发新的 Widget 组件
- 实现功能增强
- 重构现有代码
- 编写集成测试

#### 🌳 高级开发者
- 设计新的架构特性
- 性能优化和调优
- 制定开发规范
- 指导新贡献者

## 🛠️ 开发工具推荐

### IDE 和编辑器
- **PyCharm Professional** - 功能强大的 Python IDE
- **Visual Studio Code** - 轻量级，插件丰富
- **Sublime Text** - 快速响应的文本编辑器

### 必备插件（VS Code）
```json
{
  "recommendations": [
    "ms-python.python",
    "ms-python.pylint",
    "ms-python.black-formatter",
    "ms-python.isort",
    "ms-toolsai.jupyter",
    "redhat.vscode-yaml",
    "yzhang.markdown-all-in-one"
  ]
}
```

### 命令行工具
- **Git** - 版本控制
- **Python 3.10+** - 开发语言
- **pip/uv** - 包管理
- **pytest** - 测试框架

## 📋 开发规范

### 代码风格
- **格式化工具**: Black (line-length=88)
- **导入排序**: isort
- **代码检查**: pylint, flake8
- **类型提示**: mypy

### 提交规范
使用 [Conventional Commits](https://www.conventionalcommits.org/) 格式：

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

**类型说明**：
- `feat`: 新功能
- `fix`: 修复 bug
- `docs`: 文档更新
- `style`: 代码格式化
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建过程或辅助工具变动

### 分支管理
- `main` - 主分支，保持稳定
- `develop` - 开发分支，集成新功能
- `feature/*` - 功能分支
- `bugfix/*` - 修复分支
- `hotfix/*` - 紧急修复分支

## 🌟 贡献认可

### 贡献者列表
所有贡献者都会在项目中得到认可：
- README.md 贡献者列表
- 发布说明中的致谢
- 项目文档中的署名

### 贡献类型
我们认可多种形式的贡献：
- 💻 **代码** - 新功能、bug 修复、性能优化
- 📖 **文档** - 改进文档、添加示例、翻译
- 🎨 **设计** - UI/UX 改进、图标设计
- 🐛 **测试** - bug 报告、测试用例、质量保证
- 💡 **想法** - 功能建议、架构讨论
- 🔍 **审查** - 代码审查、pull request 反馈

## 📞 获取帮助

### 交流渠道
- **GitHub Issues** - 问题报告和功能请求
- **GitHub Discussions** - 社区讨论和问答
- **开发者邮件** - 私密问题和商务合作

### 常见问题

**Q: 我是 Python 新手，可以贡献吗？**  
A: 当然可以！我们有很多适合新手的 "good first issue" 标签的问题。

**Q: 如何确保我的代码符合项目标准？**  
A: 运行 `pytest` 和 `pylint`，确保所有测试通过且无代码质量问题。

**Q: 我应该在哪个分支上开发？**  
A: 从 `develop` 分支创建你的功能分支，开发完成后提交 PR 到 `develop`。

**Q: 提交 PR 后多久能得到反馈？**  
A: 我们通常在 2-3 个工作日内回复，复杂的 PR 可能需要更长时间。

## 🎉 欢迎加入

EmailWidget 是一个开放、友好的开源项目。无论您的技能水平如何，我们都欢迎您的参与！

### 参与方式
1. ⭐ **Star 项目** - 支持项目发展
2. 🍴 **Fork 项目** - 开始您的贡献之旅
3. 🐛 **报告问题** - 帮助改进项目质量
4. 💡 **提出建议** - 分享您的想法
5. 📖 **改进文档** - 让文档更加完善
6. 💻 **贡献代码** - 直接参与开发

让我们一起把 EmailWidget 打造成最好用的 Python 邮件报告库！

---

**开始您的开发之旅：**
1. 查看 [开发环境搭建](setup.md) 准备环境
2. 阅读 [贡献指南](contributing.md) 了解流程
3. 浏览 [GitHub Issues](https://github.com/emailwidget/emailwidget/issues) 寻找合适的任务
4. 开始编码和贡献！ 