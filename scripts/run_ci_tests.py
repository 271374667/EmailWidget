#!/usr/bin/env python3
"""
CI测试运行脚本

此脚本模拟GitHub Actions中的测试运行流程，用于本地验证。
"""

import os
import subprocess
import sys
from pathlib import Path


def run_command(cmd: str, description: str) -> bool:
    """运行命令并返回是否成功"""
    print(f"\n🔧 {description}")
    print(f"📋 运行命令: {cmd}")
    print("=" * 50)

    result = subprocess.run(cmd, shell=True, capture_output=False, text=True)

    if result.returncode == 0:
        print(f"✅ {description} - 成功")
        return True
    else:
        print(f"❌ {description} - 失败 (退出码: {result.returncode})")
        return False


def main():
    """主测试流程"""
    print("🚀 EmailWidget CI测试流程")
    print("=" * 50)

    # 确保在项目根目录
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)
    print(f"📁 工作目录: {project_root}")

    success_count = 0
    total_count = 0

    # 测试步骤
    test_steps = [
        ("python -m pytest tests/ --tb=short -q", "运行基础测试套件"),
        (
            "python -m pytest tests/ --cov=email_widget --cov-report=html --tb=short",
            "运行覆盖率测试",
        ),
        (
            "python -m pytest tests/test_core/ tests/test_utils/ tests/test_email.py -v",
            "运行核心模块测试",
        ),
    ]

    # 可选的代码质量检查（如果工具可用）
    optional_steps = [
        (
            "python -c \"import ruff; print('ruff available')\" && ruff check email_widget/ tests/ || echo 'ruff not available'",
            "代码质量检查",
        ),
        # (
        #     "python -c \"import mypy; print('mypy available')\" && mypy email_widget/ --ignore-missing-imports || echo 'mypy not available'",
        #     "类型检查",
        # ),
    ]

    print("\n📋 执行测试步骤:")

    # 执行主要测试
    for cmd, desc in test_steps:
        total_count += 1
        if run_command(cmd, desc):
            success_count += 1

    # 执行可选检查
    print("\n🔍 执行可选检查:")
    for cmd, desc in optional_steps:
        run_command(cmd, desc)  # 不计入成功/失败统计

    # 总结结果
    print("\n" + "=" * 50)
    print("📊 测试结果总结:")
    print(f"✅ 成功: {success_count}/{total_count}")
    print(f"❌ 失败: {total_count - success_count}/{total_count}")

    if success_count == total_count:
        print("🎉 所有测试通过！CI准备就绪!")
        sys.exit(0)
    else:
        print("⚠️ 部分测试失败，请检查上面的错误信息")
        sys.exit(1)


if __name__ == "__main__":
    main()
