"""EmailWidget性能工具

提供性能监控、测量和优化功能。
"""
import time
import functools
from typing import Dict, Any, Callable, Optional
from contextlib import contextmanager

from email_widget.core.logger import get_project_logger


class PerformanceMonitor:
    """性能监控器
    
    用于监控和记录各种操作的性能指标。
    """
    
    def __init__(self):
        """初始化性能监控器"""
        self._logger = get_project_logger()
        self._metrics: Dict[str, Dict[str, Any]] = {}
    
    def record_operation(self, operation_name: str, duration: float, 
                        metadata: Optional[Dict[str, Any]] = None) -> None:
        """记录操作性能指标
        
        Args:
            operation_name: 操作名称
            duration: 操作耗时（秒）
            metadata: 额外的元数据
        """
        if operation_name not in self._metrics:
            self._metrics[operation_name] = {
                'count': 0,
                'total_time': 0.0,
                'min_time': float('inf'),
                'max_time': 0.0,
                'avg_time': 0.0
            }
        
        metrics = self._metrics[operation_name]
        metrics['count'] += 1
        metrics['total_time'] += duration
        metrics['min_time'] = min(metrics['min_time'], duration)
        metrics['max_time'] = max(metrics['max_time'], duration)
        metrics['avg_time'] = metrics['total_time'] / metrics['count']
        
        if metadata:
            metrics.setdefault('metadata', []).append(metadata)
        
        self._logger.debug(f"性能记录: {operation_name} 耗时 {duration:.4f}s")
    
    def get_metrics(self) -> Dict[str, Dict[str, Any]]:
        """获取所有性能指标
        
        Returns:
            性能指标字典
        """
        return self._metrics.copy()
    
    def get_operation_metrics(self, operation_name: str) -> Optional[Dict[str, Any]]:
        """获取特定操作的性能指标
        
        Args:
            operation_name: 操作名称
            
        Returns:
            操作的性能指标，如果不存在则返回None
        """
        return self._metrics.get(operation_name)
    
    def clear_metrics(self) -> None:
        """清空所有性能指标"""
        self._metrics.clear()
        self._logger.debug("清空性能指标")
    
    def log_summary(self) -> None:
        """输出性能摘要日志"""
        if not self._metrics:
            self._logger.info("没有性能数据")
            return
        
        self._logger.info("=== 性能摘要 ===")
        for operation, metrics in self._metrics.items():
            self._logger.info(
                f"{operation}: 调用{metrics['count']}次, "
                f"平均{metrics['avg_time']:.4f}s, "
                f"最小{metrics['min_time']:.4f}s, "
                f"最大{metrics['max_time']:.4f}s"
            )


# 全局性能监控器
_global_monitor: Optional[PerformanceMonitor] = None


def get_performance_monitor() -> PerformanceMonitor:
    """获取全局性能监控器实例
    
    Returns:
        PerformanceMonitor实例
    """
    global _global_monitor
    if _global_monitor is None:
        _global_monitor = PerformanceMonitor()
    return _global_monitor


@contextmanager
def measure_time(operation_name: str, metadata: Optional[Dict[str, Any]] = None):
    """性能测量上下文管理器
    
    Args:
        operation_name: 操作名称
        metadata: 额外的元数据
        
    Examples:
        >>> with measure_time("image_processing"):
        ...     # 处理图片的代码
        ...     pass
    """
    start_time = time.time()
    try:
        yield
    finally:
        duration = time.time() - start_time
        get_performance_monitor().record_operation(operation_name, duration, metadata)


def performance_monitor(operation_name: Optional[str] = None):
    """性能监控装饰器
    
    Args:
        operation_name: 操作名称，如果不提供则使用函数名
        
    Examples:
        >>> @performance_monitor("render_widget")
        ... def render_html(self):
        ...     return "<div>content</div>"
    """
    def decorator(func: Callable) -> Callable:
        name = operation_name or f"{func.__module__}.{func.__qualname__}"
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with measure_time(name):
                return func(*args, **kwargs)
        return wrapper
    return decorator


class MemoryOptimizer:
    """内存优化工具
    
    提供内存使用优化的实用方法。
    """
    
    @staticmethod
    def clear_large_objects(*objects) -> None:
        """清理大对象引用
        
        Args:
            *objects: 要清理的对象
        """
        logger = get_project_logger()
        
        for obj in objects:
            if obj is not None:
                try:
                    # 尝试调用对象的清理方法
                    if hasattr(obj, 'close'):
                        obj.close()
                    elif hasattr(obj, 'clear'):
                        obj.clear()
                    
                    # 删除引用
                    del obj
                    
                except Exception as e:
                    logger.warning(f"清理对象时出错: {e}")
        
        # 建议垃圾回收
        import gc
        gc.collect()
        
        logger.debug(f"清理了 {len(objects)} 个大对象")
    
    @staticmethod
    def get_memory_usage() -> Dict[str, Any]:
        """获取当前内存使用情况
        
        Returns:
            内存使用信息字典
        """
        try:
            import psutil
            import os
            
            process = psutil.Process(os.getpid())
            memory_info = process.memory_info()
            
            return {
                'rss_mb': memory_info.rss / 1024 / 1024,  # 物理内存
                'vms_mb': memory_info.vms / 1024 / 1024,  # 虚拟内存
                'percent': process.memory_percent()        # 内存使用百分比
            }
        except ImportError:
            return {'error': 'psutil not available'}
        except Exception as e:
            return {'error': str(e)} 