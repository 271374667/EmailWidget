# 工具函数

EmailWidget 提供了一系列辅助工具函数，用于支持图片处理、缓存管理、日志记录等功能。

## 图片工具

### ImageUtils

图片处理工具类，提供图片缓存、格式转换等功能。

#### 主要功能

- **图片缓存管理** - 缓存图片文件避免重复下载
- **格式支持** - 支持多种图片格式（PNG, JPG, GIF等）
- **路径处理** - 统一处理本地和远程图片路径
- **性能优化** - 智能缓存策略提升加载速度

#### 使用示例

```python
from email_widget.utils.image_utils import ImageUtils

# 处理本地图片
local_path = ImageUtils.process_local_image("./charts/sales.png")

# 处理远程图片（自动缓存）
remote_path = ImageUtils.process_remote_image("https://example.com/chart.png")

# 清理图片缓存
ImageUtils.clear_cache()
```

---

## 缓存系统

### get_cache()

获取全局缓存实例。

```python
from email_widget.core.cache import get_cache

cache = get_cache()

# 存储数据
cache.set("key", "value")

# 获取数据
value = cache.get("key")

# 清空缓存
cache.clear()
```

#### 缓存策略

- **LRU算法** - 最近最少使用的数据优先淘汰
- **内存限制** - 自动控制缓存大小避免内存溢出
- **线程安全** - 支持多线程环境使用

---

## 模板引擎

### get_template_engine()

获取全局模板引擎实例。

```python
from email_widget.core.template_engine import get_template_engine

engine = get_template_engine()

# 渲染模板
html = engine.render_safe(
    template_string="<div>{{ content }}</div>",
    context={"content": "Hello World"},
    fallback="<div>Error</div>"
)
```

#### 特性

- **基于Jinja2** - 强大的模板语法支持
- **安全渲染** - 自动错误处理和降级
- **模板缓存** - 提升重复渲染性能
- **上下文验证** - 确保数据安全性

---

## 日志系统

### get_project_logger()

获取项目专用的日志记录器。

```python
from email_widget.core.logger import get_project_logger

logger = get_project_logger()

# 记录不同级别的日志
logger.debug("调试信息")
logger.info("一般信息")
logger.warning("警告信息")
logger.error("错误信息")
logger.critical("严重错误")
```

#### 配置选项

通过环境变量控制日志行为：

```bash
# 设置日志级别
export EMAILWIDGET_LOG_LEVEL=DEBUG

# 禁用日志
export EMAILWIDGET_LOG_LEVEL=NONE
```

---

## 配置工具

### 环境检测

```python
import os
from email_widget.core.config import EmailConfig

def is_development_mode():
    """检测是否为开发环境"""
    return os.getenv("EMAILWIDGET_ENV") == "development"

def get_output_directory():
    """获取输出目录"""
    config = EmailConfig()
    return config.get_output_dir()
```

### 路径处理

```python
from pathlib import Path

def ensure_output_directory(path: str) -> Path:
    """确保输出目录存在"""
    output_path = Path(path)
    output_path.mkdir(parents=True, exist_ok=True)
    return output_path

def sanitize_filename(filename: str) -> str:
    """清理文件名中的非法字符"""
    import re
    return re.sub(r'[<>:"/\\|?*]', '_', filename)
```

---

## 性能工具

### 装饰器

```python
from functools import lru_cache
import time

@lru_cache(maxsize=128)
def expensive_calculation(param):
    """使用LRU缓存的昂贵计算"""
    # 模拟耗时计算
    time.sleep(0.1)
    return f"result_for_{param}"

def timing_decorator(func):
    """性能计时装饰器"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 执行时间: {end_time - start_time:.4f}秒")
        return result
    return wrapper
```

### 内存监控

```python
import psutil
import gc

def get_memory_usage():
    """获取当前内存使用情况"""
    process = psutil.Process()
    memory_info = process.memory_info()
    return {
        "rss": memory_info.rss / 1024 / 1024,  # MB
        "vms": memory_info.vms / 1024 / 1024   # MB
    }

def force_garbage_collection():
    """强制垃圾回收"""
    collected = gc.collect()
    return collected
```

---

## 数据处理工具

### DataFrame 工具

```python
import pandas as pd
from typing import List, Dict, Any

def dataframe_to_dict_list(df: pd.DataFrame) -> List[Dict[str, Any]]:
    """将DataFrame转换为字典列表"""
    return df.to_dict('records')

def validate_dataframe(df: pd.DataFrame) -> bool:
    """验证DataFrame是否适合展示"""
    if df.empty:
        return False
    if df.shape[0] > 1000:  # 行数限制
        return False
    if df.shape[1] > 20:    # 列数限制
        return False
    return True

def format_dataframe_for_display(df: pd.DataFrame) -> pd.DataFrame:
    """格式化DataFrame用于显示"""
    # 处理NaN值
    df_formatted = df.fillna('-')
    
    # 格式化数值列
    for col in df_formatted.select_dtypes(include=['float64']).columns:
        df_formatted[col] = df_formatted[col].round(2)
    
    return df_formatted
```

### 文本处理

```python
import re
from typing import Optional

def truncate_text(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """截断文本到指定长度"""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix

def clean_html_text(text: str) -> str:
    """清理HTML标签"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def format_number(number: float, precision: int = 2) -> str:
    """格式化数字显示"""
    if abs(number) >= 1e9:
        return f"{number/1e9:.{precision}f}B"
    elif abs(number) >= 1e6:
        return f"{number/1e6:.{precision}f}M"
    elif abs(number) >= 1e3:
        return f"{number/1e3:.{precision}f}K"
    else:
        return f"{number:.{precision}f}"
```

---

## 调试工具

### 调试装饰器

```python
import functools
import inspect

def debug_calls(func):
    """调试函数调用的装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = get_project_logger()
        
        # 记录函数调用
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        logger.debug(f"调用 {func.__name__} 参数: {bound_args.arguments}")
        
        try:
            result = func(*args, **kwargs)
            logger.debug(f"{func.__name__} 返回: {type(result).__name__}")
            return result
        except Exception as e:
            logger.error(f"{func.__name__} 异常: {e}")
            raise
    
    return wrapper
```

### 状态检查

```python
def check_system_status():
    """检查系统状态"""
    status = {
        "memory": get_memory_usage(),
        "cache_size": len(get_cache()._data) if hasattr(get_cache(), '_data') else 0,
        "python_version": f"{sys.version_info.major}.{sys.version_info.minor}",
        "platform": platform.system()
    }
    return status

def validate_dependencies():
    """验证依赖库"""
    required_packages = ['jinja2', 'pandas', 'matplotlib']
    missing = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)
    
    return len(missing) == 0, missing
```

---

## 文件操作工具

### 安全文件操作

```python
from pathlib import Path
import shutil
import hashlib

def safe_write_file(content: str, filepath: str, encoding: str = 'utf-8') -> bool:
    """安全写入文件"""
    try:
        path = Path(filepath)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, 'w', encoding=encoding) as f:
            f.write(content)
        return True
    except Exception as e:
        logger = get_project_logger()
        logger.error(f"文件写入失败 {filepath}: {e}")
        return False

def calculate_file_hash(filepath: str) -> Optional[str]:
    """计算文件MD5哈希"""
    try:
        with open(filepath, 'rb') as f:
            file_hash = hashlib.md5()
            chunk_size = 8192
            while chunk := f.read(chunk_size):
                file_hash.update(chunk)
        return file_hash.hexdigest()
    except Exception:
        return None

def backup_file(filepath: str) -> Optional[str]:
    """备份文件"""
    try:
        source = Path(filepath)
        if not source.exists():
            return None
        
        backup_path = source.with_suffix(f"{source.suffix}.backup")
        shutil.copy2(source, backup_path)
        return str(backup_path)
    except Exception:
        return None
```

---

## 网络工具

### HTTP 请求

```python
import requests
from typing import Optional, Dict

def download_file(url: str, local_path: str, timeout: int = 30) -> bool:
    """下载文件到本地"""
    try:
        response = requests.get(url, timeout=timeout, stream=True)
        response.raise_for_status()
        
        with open(local_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        return True
    except Exception as e:
        logger = get_project_logger()
        logger.error(f"文件下载失败 {url}: {e}")
        return False

def check_url_accessible(url: str, timeout: int = 10) -> bool:
    """检查URL是否可访问"""
    try:
        response = requests.head(url, timeout=timeout)
        return response.status_code == 200
    except Exception:
        return False
```

---

## 日期时间工具

```python
from datetime import datetime, timedelta
import pytz

def format_timestamp(timestamp: datetime, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
    """格式化时间戳"""
    return timestamp.strftime(format_str)

def get_chinese_time() -> datetime:
    """获取中国时区时间"""
    china_tz = pytz.timezone('Asia/Shanghai')
    return datetime.now(china_tz)

def time_ago(timestamp: datetime) -> str:
    """计算相对时间"""
    now = datetime.now(timestamp.tzinfo) if timestamp.tzinfo else datetime.now()
    diff = now - timestamp
    
    if diff.days > 0:
        return f"{diff.days}天前"
    elif diff.seconds > 3600:
        hours = diff.seconds // 3600
        return f"{hours}小时前"
    elif diff.seconds > 60:
        minutes = diff.seconds // 60
        return f"{minutes}分钟前"
    else:
        return "刚刚"
```

---

## 使用示例

### 完整工具函数使用

```python
from email_widget import Email
from email_widget.widgets import *
from email_widget.core.logger import get_project_logger
from email_widget.core.cache import get_cache
import pandas as pd

def create_comprehensive_report():
    """使用工具函数创建综合报告"""
    
    # 获取工具实例
    logger = get_project_logger()
    cache = get_cache()
    
    logger.info("开始创建综合报告")
    
    # 检查缓存
    cached_data = cache.get("report_data")
    if cached_data:
        logger.info("使用缓存数据")
        data = cached_data
    else:
        logger.info("生成新数据")
        # 模拟数据生成
        data = {
            "timestamp": get_chinese_time(),
            "memory_usage": get_memory_usage(),
            "system_status": check_system_status()
        }
        cache.set("report_data", data)
    
    # 创建邮件
    email = Email("📊 系统综合报告")
    
    # 添加时间信息
    time_info = format_timestamp(data["timestamp"])
    email.add_text(f"报告生成时间: {time_info}")
    
    # 添加系统状态
    status_table = TableWidget()
    status_table.set_headers(["指标", "值"])
    status_table.add_row(["内存使用(RSS)", f"{data['memory_usage']['rss']:.2f} MB"])
    status_table.add_row(["内存使用(VMS)", f"{data['memory_usage']['vms']:.2f} MB"])
    status_table.add_row(["缓存项数", str(data['system_status']['cache_size'])])
    
    email.add_widget(status_table)
    
    # 导出报告
    output_path = ensure_output_directory("./reports/")
    filename = f"comprehensive_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    safe_filename = sanitize_filename(filename)
    
    file_path = email.export_html(safe_filename, str(output_path))
    
    logger.info(f"报告已生成: {file_path}")
    return file_path

# 使用示例
try:
    report_path = create_comprehensive_report()
    print(f"✅ 报告生成成功: {report_path}")
except Exception as e:
    print(f"❌ 报告生成失败: {e}")
```

---

## 最佳实践

### 1. 错误处理

```python
# ✅ 推荐：使用工具函数的安全版本
success = safe_write_file(content, filepath)
if not success:
    # 处理写入失败
    pass

# ❌ 避免：直接文件操作不处理异常
with open(filepath, 'w') as f:
    f.write(content)  # 可能抛出异常
```

### 2. 资源管理

```python
# ✅ 推荐：合理使用缓存
cache = get_cache()
if cache.get("expensive_data") is None:
    data = expensive_calculation()
    cache.set("expensive_data", data)

# ✅ 推荐：定期清理资源
def cleanup_resources():
    force_garbage_collection()
    ImageUtils.clear_cache()
```

### 3. 日志记录

```python
# ✅ 推荐：使用项目日志记录器
logger = get_project_logger()
logger.info("操作开始")
try:
    # 业务逻辑
    pass
except Exception as e:
    logger.error(f"操作失败: {e}")
```

### 4. 性能监控

```python
# ✅ 推荐：监控性能关键点
@timing_decorator
def critical_function():
    memory_before = get_memory_usage()
    # 执行逻辑
    memory_after = get_memory_usage()
    logger.info(f"内存变化: {memory_after['rss'] - memory_before['rss']:.2f} MB")
``` 