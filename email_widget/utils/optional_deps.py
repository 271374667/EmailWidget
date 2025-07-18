"""Optional dependency check module

This module provides utility functions for checking and importing optional dependencies, to support progressive feature enablement.
"""

from typing import Any


def check_optional_dependency(module_name: str, extra_name: str | None = None) -> None:
    """Check if optional dependency is available

    Args:
        module_name: Module name
        extra_name: Optional dependency group name

    Raises:
        ImportError: Thrown when dependency is not available, includes installation hints

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
    """Import optional dependency

    Args:
        module_name: Module name
        extra_name: Optional dependency group name

    Returns:
        Imported module object

    Raises:
        ImportError: Thrown when dependency is not available, includes installation hints

    Examples:
        >>> pd = import_optional_dependency("pandas")
        >>> plt = import_optional_dependency("matplotlib.pyplot")
    """
    check_optional_dependency(module_name, extra_name)
    return __import__(module_name, fromlist=[""])


def requires_pandas(func):
    """Decorator: requires pandas dependency to be available

    Args:
        func: Function to be decorated

    Returns:
        Decorated function

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
    """Decorator: requires matplotlib dependency to be available

    Args:
        func: Function to be decorated

    Returns:
        Decorated function

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
    """Pandas functionality mixin class

    Provides common pandas checking methods for classes that need pandas functionality.
    """

    def _check_pandas_available(self) -> None:
        """Check if pandas is available"""
        check_optional_dependency("pandas")

    def _import_pandas(self):
        """Import pandas module"""
        return import_optional_dependency("pandas")


class ChartMixin:
    """Chart functionality mixin class

    Provides common matplotlib checking methods for classes that need chart functionality.
    """

    def _check_matplotlib_available(self) -> None:
        """Check if matplotlib is available"""
        check_optional_dependency("matplotlib")

    def _import_matplotlib_pyplot(self):
        """Import matplotlib.pyplot module"""
        return import_optional_dependency("matplotlib.pyplot")

    def _import_matplotlib_font_manager(self):
        """Import matplotlib.font_manager module"""
        return import_optional_dependency("matplotlib.font_manager")

    def _check_seaborn_available(self) -> None:
        """Check if seaborn is available"""
        check_optional_dependency("seaborn")

    def _import_seaborn(self):
        """Import seaborn module"""
        return import_optional_dependency("seaborn")
