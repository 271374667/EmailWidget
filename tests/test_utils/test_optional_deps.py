"""可选依赖检查模块测试

本模块提供email_widget.utils.optional_deps的完整测试覆盖，
包括正常情况、异常情况、边界条件等所有代码路径。
"""

from unittest.mock import MagicMock, patch

import pytest

from email_widget.utils.optional_deps import (
    PandasMixin,
    check_optional_dependency,
    import_optional_dependency,
    requires_pandas,
)


class TestCheckOptionalDependency:
    """测试check_optional_dependency函数"""

    @pytest.mark.parametrize(
        "module_name,extra_name",
        [
            ("os", None),
            ("sys", "system"),
            ("json", "json"),
            ("math", None),
        ],
    )
    def test_check_existing_module_success(self, module_name: str, extra_name: str):
        """测试检查存在的模块时成功通过"""
        # 这些都是标准库模块，应该总是存在
        try:
            check_optional_dependency(module_name, extra_name)
        except ImportError:
            pytest.fail(f"不应该对存在的模块 {module_name} 抛出ImportError")

    @pytest.mark.parametrize(
        "module_name,extra_name,expected_message",
        [
            (
                "non_existent_module_123",
                None,
                "non_existent_module_123 is required for this functionality. Install with: pip install non_existent_module_123",
            ),
            (
                "fake_pandas",
                "pandas",
                "fake_pandas is required for this functionality. Install with: pip install fake_pandas",
            ),
            (
                "imaginary_lib",
                "charts",
                "imaginary_lib is required for this functionality. Install with: pip install imaginary_lib",
            ),
        ],
    )
    def test_check_non_existent_module_raises_import_error(
        self, module_name: str, extra_name: str, expected_message: str
    ):
        """测试检查不存在的模块时抛出ImportError并包含正确消息"""
        with pytest.raises(ImportError) as exc_info:
            check_optional_dependency(module_name, extra_name)

        assert str(exc_info.value) == expected_message
        # 验证异常链被正确设置（from None）
        assert exc_info.value.__cause__ is None

    def test_check_with_mock_import_failure(self):
        """测试模拟导入失败的情况"""
        # 由于__import__是内置函数，我们使用builtins模块来patch
        import builtins

        original_import = builtins.__import__

        def mock_import(name, *args, **kwargs):
            if name == "mocked_module":
                raise ImportError("模拟导入失败")
            return original_import(name, *args, **kwargs)

        with patch.object(builtins, "__import__", mock_import):
            with pytest.raises(ImportError) as exc_info:
                check_optional_dependency("mocked_module", "extra")

            expected_msg = "mocked_module is required for this functionality. Install with: pip install mocked_module"
            assert str(exc_info.value) == expected_msg

    def test_check_with_empty_strings(self):
        """测试空字符串参数的边界条件"""
        # 空字符串会引发ValueError而不是ImportError
        with pytest.raises(ValueError) as exc_info:
            check_optional_dependency("", None)

        assert "Empty module name" in str(exc_info.value)

        with pytest.raises(ValueError) as exc_info:
            check_optional_dependency("", "")

        assert "Empty module name" in str(exc_info.value)


class TestImportOptionalDependency:
    """测试import_optional_dependency函数"""

    @pytest.mark.parametrize(
        "module_name,extra_name",
        [
            ("os", None),
            ("sys", "system"),
            ("json", "json"),
        ],
    )
    def test_import_existing_module_success(self, module_name: str, extra_name: str):
        """测试导入存在的模块时返回正确的模块对象"""
        result = import_optional_dependency(module_name, extra_name)

        # 验证返回的是模块对象
        assert hasattr(result, "__name__")
        # 验证模块名称正确
        expected_name = module_name.split(".")[0]  # 处理子模块情况
        assert result.__name__ == expected_name

    def test_import_submodule_success(self):
        """测试导入子模块的情况"""
        result = import_optional_dependency("os.path", "system")

        # 验证返回的是子模块
        assert hasattr(result, "__name__")
        # Windows上os.path实际是ntpath，我们检查它是path模块即可
        assert "path" in result.__name__ or result.__name__ in ["posixpath", "ntpath"]

    @pytest.mark.parametrize(
        "module_name,extra_name",
        [
            ("non_existent_module_456", None),
            ("fake_library", "optional"),
        ],
    )
    def test_import_non_existent_module_raises_import_error(
        self, module_name: str, extra_name: str
    ):
        """测试导入不存在的模块时抛出ImportError"""
        with pytest.raises(ImportError) as exc_info:
            import_optional_dependency(module_name, extra_name)

        # 验证错误消息格式
        expected_msg = f"{module_name} is required for this functionality. Install with: pip install {module_name}"
        assert str(exc_info.value) == expected_msg

    def test_import_with_mock_success(self):
        """测试模拟成功导入的情况"""
        import builtins

        original_import = builtins.__import__
        mock_module = MagicMock()
        mock_module.__name__ = "mocked_module"

        def mock_import(name, *args, **kwargs):
            if name == "mocked_module":
                return mock_module
            return original_import(name, *args, **kwargs)

        with patch.object(builtins, "__import__", mock_import):
            result = import_optional_dependency("mocked_module", "extra")
            assert result is mock_module

    def test_import_calls_check_dependency(self):
        """测试import_optional_dependency内部调用check_optional_dependency"""
        with patch(
            "email_widget.utils.optional_deps.check_optional_dependency"
        ) as mock_check:
            import builtins

            original_import = builtins.__import__
            mock_module = MagicMock()

            def mock_import(name, *args, **kwargs):
                if name == "test_module":
                    return mock_module
                return original_import(name, *args, **kwargs)

            with patch.object(builtins, "__import__", mock_import):
                import_optional_dependency("test_module", "test_extra")
                mock_check.assert_called_once_with("test_module", "test_extra")


class TestRequiresPandasDecorator:
    """测试requires_pandas装饰器"""

    def test_decorator_with_pandas_available(self):
        """测试pandas可用时装饰器正常工作"""

        @requires_pandas
        def sample_function(x: int, y: int = 2) -> int:
            """示例函数"""
            return x * y

        # 模拟pandas可用
        with patch(
            "email_widget.utils.optional_deps.check_optional_dependency"
        ) as mock_check:
            result = sample_function(3, 4)

            assert result == 12
            mock_check.assert_called_once_with("pandas")

    def test_decorator_with_pandas_unavailable(self):
        """测试pandas不可用时装饰器抛出异常"""

        @requires_pandas
        def sample_function(x: int) -> int:
            """示例函数"""
            return x * 2

        # 模拟pandas不可用
        with patch(
            "email_widget.utils.optional_deps.check_optional_dependency"
        ) as mock_check:
            mock_check.side_effect = ImportError("pandas is required")

            with pytest.raises(ImportError) as exc_info:
                sample_function(5)

            assert "pandas is required" in str(exc_info.value)
            mock_check.assert_called_once_with("pandas")

    def test_decorator_preserves_function_signature(self):
        """测试装饰器不改变函数签名和行为"""

        def original_function(a: str, b: int = 10) -> str:
            """原始函数文档"""
            return f"{a}-{b}"

        decorated_function = requires_pandas(original_function)

        # 测试在pandas可用的情况下
        with patch("email_widget.utils.optional_deps.check_optional_dependency"):
            result = decorated_function("test", 20)
            assert result == "test-20"

            # 测试关键字参数
            result = decorated_function("hello", b=30)
            assert result == "hello-30"

            # 测试位置参数
            result = decorated_function("world")
            assert result == "world-10"

    def test_decorator_with_exception_in_function(self):
        """测试被装饰函数内部抛出异常时的行为"""

        @requires_pandas
        def function_with_error():
            """会抛出异常的函数"""
            raise ValueError("函数内部错误")

        with patch("email_widget.utils.optional_deps.check_optional_dependency"):
            with pytest.raises(ValueError) as exc_info:
                function_with_error()

            assert "函数内部错误" in str(exc_info.value)

    def test_decorator_with_no_args_function(self):
        """测试装饰器用于无参数函数"""

        @requires_pandas
        def no_args_function():
            """无参数函数"""
            return "success"

        with patch("email_widget.utils.optional_deps.check_optional_dependency"):
            result = no_args_function()
            assert result == "success"

    def test_decorator_with_args_and_kwargs(self):
        """测试装饰器处理*args和**kwargs"""

        @requires_pandas
        def flexible_function(*args, **kwargs):
            """灵活参数函数"""
            return {"args": args, "kwargs": kwargs}

        with patch("email_widget.utils.optional_deps.check_optional_dependency"):
            result = flexible_function(1, 2, 3, key1="value1", key2="value2")

            assert result["args"] == (1, 2, 3)
            assert result["kwargs"] == {"key1": "value1", "key2": "value2"}


class TestPandasMixin:
    """测试PandasMixin类"""

    def setup_method(self):
        """每个测试方法前的设置"""
        self.mixin = PandasMixin()

    def test_mixin_initialization(self):
        """测试混入类的初始化"""
        assert isinstance(self.mixin, PandasMixin)
        assert hasattr(self.mixin, "_check_pandas_available")
        assert hasattr(self.mixin, "_import_pandas")

    def test_check_pandas_available_success(self):
        """测试pandas可用时检查成功"""
        with patch(
            "email_widget.utils.optional_deps.check_optional_dependency"
        ) as mock_check:
            self.mixin._check_pandas_available()
            mock_check.assert_called_once_with("pandas")

    def test_check_pandas_available_failure(self):
        """测试pandas不可用时抛出异常"""
        with patch(
            "email_widget.utils.optional_deps.check_optional_dependency"
        ) as mock_check:
            mock_check.side_effect = ImportError("pandas not available")

            with pytest.raises(ImportError) as exc_info:
                self.mixin._check_pandas_available()

            assert "pandas not available" in str(exc_info.value)
            mock_check.assert_called_once_with("pandas")

    def test_import_pandas_success(self):
        """测试成功导入pandas"""
        mock_pandas = MagicMock()
        mock_pandas.__name__ = "pandas"

        with patch(
            "email_widget.utils.optional_deps.import_optional_dependency"
        ) as mock_import:
            mock_import.return_value = mock_pandas

            result = self.mixin._import_pandas()

            assert result is mock_pandas
            mock_import.assert_called_once_with("pandas")

    def test_import_pandas_failure(self):
        """测试导入pandas失败"""
        with patch(
            "email_widget.utils.optional_deps.import_optional_dependency"
        ) as mock_import:
            mock_import.side_effect = ImportError("pandas import failed")

            with pytest.raises(ImportError) as exc_info:
                self.mixin._import_pandas()

            assert "pandas import failed" in str(exc_info.value)
            mock_import.assert_called_once_with("pandas")


class TestIntegrationScenarios:
    """集成测试场景"""

    def test_full_workflow_pandas_available(self):
        """测试pandas可用时的完整工作流程"""
        # 模拟pandas可用
        import builtins

        original_import = builtins.__import__
        mock_pandas = MagicMock()
        mock_pandas.__name__ = "pandas"

        def mock_import(name, *args, **kwargs):
            if name == "pandas":
                return mock_pandas
            return original_import(name, *args, **kwargs)

        with patch.object(builtins, "__import__", mock_import):
            # 1. 检查依赖
            check_optional_dependency("pandas")

            # 2. 导入依赖
            imported_pandas = import_optional_dependency("pandas")
            assert imported_pandas is mock_pandas

            # 3. 使用装饰器
            @requires_pandas
            def use_pandas():
                return "pandas_used"

            result = use_pandas()
            assert result == "pandas_used"

            # 4. 使用混入类
            mixin = PandasMixin()
            mixin._check_pandas_available()
            imported_via_mixin = mixin._import_pandas()
            assert imported_via_mixin is mock_pandas

    def test_full_workflow_pandas_unavailable(self):
        """测试pandas不可用时的完整工作流程"""
        # 模拟pandas不可用
        import builtins

        original_import = builtins.__import__

        def mock_import(name, *args, **kwargs):
            if name == "pandas":
                raise ImportError("No module named 'pandas'")
            return original_import(name, *args, **kwargs)

        with patch.object(builtins, "__import__", mock_import):
            # 1. 检查依赖应该失败
            with pytest.raises(ImportError) as exc_info:
                check_optional_dependency("pandas")
            assert "pandas is required" in str(exc_info.value)

            # 2. 导入依赖应该失败
            with pytest.raises(ImportError):
                import_optional_dependency("pandas")

            # 3. 装饰器应该失败
            @requires_pandas
            def use_pandas():
                return "should_not_reach"

            with pytest.raises(ImportError):
                use_pandas()

            # 4. 混入类应该失败
            mixin = PandasMixin()
            with pytest.raises(ImportError):
                mixin._check_pandas_available()
            with pytest.raises(ImportError):
                mixin._import_pandas()

    @pytest.mark.parametrize(
        "scenario,module_name,extra_name",
        [
            ("基础库", "os", None),
            ("子模块", "urllib.parse", "network"),
            ("复杂名称", "some_complex_library_name", "extra_features"),
        ],
    )
    def test_various_module_scenarios(
        self, scenario: str, module_name: str, extra_name: str
    ):
        """测试各种模块场景的参数化测试"""
        # 测试存在的模块（使用标准库）
        if module_name in ["os", "urllib.parse"]:
            # 这些应该成功
            check_optional_dependency(module_name, extra_name)
            result = import_optional_dependency(module_name, extra_name)
            assert result is not None
        else:
            # 这些应该失败（假设的第三方库）
            with pytest.raises(ImportError):
                check_optional_dependency(module_name, extra_name)
            with pytest.raises(ImportError):
                import_optional_dependency(module_name, extra_name)

    def test_mock_third_party_library_failure(self):
        """测试模拟第三方库导入失败"""
        import builtins

        original_import = builtins.__import__

        def mock_import(name, *args, **kwargs):
            if name == "matplotlib":
                raise ImportError("No module named 'matplotlib'")
            return original_import(name, *args, **kwargs)

        with patch.object(builtins, "__import__", mock_import):
            with pytest.raises(ImportError):
                check_optional_dependency("matplotlib")
            with pytest.raises(ImportError):
                import_optional_dependency("matplotlib")


class TestEdgeCases:
    """边界条件和异常情况测试"""

    def test_none_module_name(self):
        """测试None作为模块名的情况"""
        with pytest.raises(TypeError):
            check_optional_dependency(None, "extra")

    def test_numeric_module_name(self):
        """测试数字作为模块名的情况"""
        with pytest.raises(ImportError):
            check_optional_dependency("123", "numeric")

    def test_special_characters_in_module_name(self):
        """测试模块名包含特殊字符的情况"""
        special_names = [
            "module-with-dash",
            "module.with.dots",
            "module_with_underscores",
        ]

        for name in special_names:
            with pytest.raises(ImportError):
                check_optional_dependency(name, "special")

    def test_very_long_module_name(self):
        """测试很长的模块名"""
        long_name = "a" * 1000
        with pytest.raises(ImportError) as exc_info:
            check_optional_dependency(long_name, "long")

        assert long_name in str(exc_info.value)

    def test_unicode_module_name(self):
        """测试Unicode字符的模块名"""
        unicode_name = "模块名称"
        with pytest.raises(ImportError) as exc_info:
            check_optional_dependency(unicode_name, "unicode")

        assert unicode_name in str(exc_info.value)

    def test_whitespace_in_names(self):
        """测试名称中包含空白字符的情况"""
        with pytest.raises(ImportError) as exc_info:
            check_optional_dependency("module name", "extra name")

        expected_msg = "module name is required for this functionality. Install with: pip install module name"
        assert str(exc_info.value) == expected_msg


class TestErrorMessageFormat:
    """测试错误消息格式的一致性"""

    @pytest.mark.parametrize(
        "module_name,extra_name,expected_format",
        [
            (
                "non_existent_test_lib_123",
                None,
                "non_existent_test_lib_123 is required for this functionality. Install with: pip install non_existent_test_lib_123",
            ),
            (
                "fake_pandas_lib",
                "pandas",
                "fake_pandas_lib is required for this functionality. Install with: pip install fake_pandas_lib",
            ),
            (
                "imaginary_plotting_lib",
                "plotting",
                "imaginary_plotting_lib is required for this functionality. Install with: pip install imaginary_plotting_lib",
            ),
        ],
    )
    def test_error_message_consistency(
        self, module_name: str, extra_name: str, expected_format: str
    ):
        """测试错误消息格式的一致性"""
        with pytest.raises(ImportError) as exc_info:
            check_optional_dependency(module_name, extra_name)

        assert str(exc_info.value) == expected_format

    def test_error_message_with_empty_string(self):
        """测试空字符串的错误消息"""
        with pytest.raises(ValueError) as exc_info:
            check_optional_dependency("", "")

        assert "Empty module name" in str(exc_info.value)

    def test_error_message_in_import_function(self):
        """测试import函数中的错误消息与check函数一致"""
        module_name = "non_existent_test_module"
        extra_name = "test_extra"

        # 获取check函数的错误消息
        with pytest.raises(ImportError) as check_exc:
            check_optional_dependency(module_name, extra_name)

        # 获取import函数的错误消息
        with pytest.raises(ImportError) as import_exc:
            import_optional_dependency(module_name, extra_name)

        # 验证消息一致
        assert str(check_exc.value) == str(import_exc.value)
