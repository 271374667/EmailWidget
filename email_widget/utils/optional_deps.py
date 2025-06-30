"""可选依赖检查模块

此模块提供检查和导入可选依赖的工具函数，用于支持渐进式功能启用。
"""
from typing import Any, Optional


def check_optional_dependency(module_name: str, extra_name: Optional[str] = None) -> None:
    """检查可选依赖是否可用
    
    Args:
        module_name: 模块名称
        extra_name: 可选依赖组名称
        
    Raises:
        ImportError: 当依赖不可用时抛出，包含安装提示
        
    Examples:
        >>> check_optional_dependency("pandas", "pandas")
        >>> check_optional_dependency("matplotlib", "charts")
    """
    try:
        __import__(module_name)
    except ImportError:
        extra_hint = f"[{extra_name}]" if extra_name else ""
        raise ImportError(
            f"{module_name} is required for this functionality. "
            f"Install with: pip install email-widget{extra_hint}"
        ) from None


def import_optional_dependency(module_name: str, extra_name: Optional[str] = None) -> Any:
    """导入可选依赖
    
    Args:
        module_name: 模块名称  
        extra_name: 可选依赖组名称
        
    Returns:
        导入的模块对象
        
    Raises:
        ImportError: 当依赖不可用时抛出，包含安装提示
        
    Examples:
        >>> pd = import_optional_dependency("pandas", "pandas")
        >>> plt = import_optional_dependency("matplotlib.pyplot", "charts")
    """
    check_optional_dependency(module_name, extra_name)
    return __import__(module_name, fromlist=[''])


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
        check_optional_dependency("pandas", "pandas")
        return func(*args, **kwargs)
    return wrapper


class PandasMixin:
    """Pandas功能混入类
    
    为需要pandas功能的类提供通用的pandas检查方法。
    """
    
    def _check_pandas_available(self) -> None:
        """检查pandas是否可用"""
        check_optional_dependency("pandas", "pandas")
    
    def _import_pandas(self):
        """导入pandas模块"""
        return import_optional_dependency("pandas", "pandas") 