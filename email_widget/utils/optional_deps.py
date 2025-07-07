"""可选依赖检查模块

此模块提供检查和导入可选依赖的工具函数，用于支持渐进式功能启用。
"""

from typing import Any


def check_optional_dependency(module_name: str, extra_name: str | None = None) -> None:
    """检查可选依赖是否可用

    Args:
        module_name: 模块名称
        extra_name: 可选依赖组名称

    Raises:
        ImportError: 当依赖不可用时抛出，包含安装提示

    Examples:
        >>> check_optional_dependency("pandas")
        >>> check_optional_dependency("matplotlib")
    """
    try:
        __import__(module_name)
    except ImportError:
        if module_name in ["pandas"]:
            raise ImportError(
                f"{module_name} is required for this functionality. "
                f"Install with: pip install {module_name}"
            ) from None
        elif module_name in [
            "matplotlib",
            "matplotlib.pyplot",
            "matplotlib.font_manager",
        ]:
            raise ImportError(
                "matplotlib is required for chart functionality. "
                "Install with: pip install matplotlib"
            ) from None
        elif module_name in ["seaborn"]:
            raise ImportError(
                "seaborn is required for advanced chart functionality. "
                "Install with: pip install seaborn"
            ) from None
        else:
            raise ImportError(
                f"{module_name} is required for this functionality. "
                f"Install with: pip install {module_name}"
            ) from None


def import_optional_dependency(module_name: str, extra_name: str | None = None) -> Any:
    """导入可选依赖

    Args:
        module_name: 模块名称
        extra_name: 可选依赖组名称

    Returns:
        导入的模块对象

    Raises:
        ImportError: 当依赖不可用时抛出，包含安装提示

    Examples:
        >>> pd = import_optional_dependency("pandas")
        >>> plt = import_optional_dependency("matplotlib.pyplot")
    """
    check_optional_dependency(module_name, extra_name)
    return __import__(module_name, fromlist=[""])


def requires_pandas(func):
    """装饰器：要求pandas依赖可用

    Args:
        func: 被装饰的函数

    Returns:
        装饰后的函数

    Examples:
        >>> @requires_pandas
        ... def process_dataframe(df):
        ...     return df.head()
    """

    def wrapper(*args, **kwargs):
        check_optional_dependency("pandas")
        return func(*args, **kwargs)

    return wrapper


def requires_matplotlib(func):
    """装饰器：要求matplotlib依赖可用

    Args:
        func: 被装饰的函数

    Returns:
        装饰后的函数

    Examples:
        >>> @requires_matplotlib
        ... def create_chart():
        ...     import matplotlib.pyplot as plt
        ...     return plt.figure()
    """

    def wrapper(*args, **kwargs):
        check_optional_dependency("matplotlib")
        return func(*args, **kwargs)

    return wrapper


class PandasMixin:
    """Pandas功能混入类

    为需要pandas功能的类提供通用的pandas检查方法。
    """

    def _check_pandas_available(self) -> None:
        """检查pandas是否可用"""
        check_optional_dependency("pandas")

    def _import_pandas(self):
        """导入pandas模块"""
        return import_optional_dependency("pandas")


class ChartMixin:
    """图表功能混入类

    为需要图表功能的类提供通用的matplotlib检查方法。
    """

    def _check_matplotlib_available(self) -> None:
        """检查matplotlib是否可用"""
        check_optional_dependency("matplotlib")

    def _import_matplotlib_pyplot(self):
        """导入matplotlib.pyplot模块"""
        return import_optional_dependency("matplotlib.pyplot")

    def _import_matplotlib_font_manager(self):
        """导入matplotlib.font_manager模块"""
        return import_optional_dependency("matplotlib.font_manager")

    def _check_seaborn_available(self) -> None:
        """检查seaborn是否可用"""
        check_optional_dependency("seaborn")

    def _import_seaborn(self):
        """导入seaborn模块"""
        return import_optional_dependency("seaborn")
