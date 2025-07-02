# 核心模块

核心模块提供了 EmailWidget 的基础架构，包括 Widget 基类、模板引擎、缓存系统等核心组件。

## BaseWidget

::: email_widget.core.base.BaseWidget

所有 Widget 的抽象基类，定义了 Widget 的基本接口和通用功能。

### 类签名

```python
class BaseWidget(ABC):
    def __init__(self, widget_id: Optional[str] = None)
```

### 属性

| 属性名 | 类型 | 说明 |
|--------|------|------|
| `widget_id` | `str` | Widget 的唯一标识符 |
| `parent` | `Optional[Email]` | 包含此 Widget 的 Email 容器 |

### 抽象方法

子类必须实现以下抽象方法：

#### `_get_template_name()` {: #_get_template_name}

```python
@abstractmethod
def _get_template_name(self) -> str
```

获取 Widget 对应的模板名称。

**Returns:**
- `str`: 模板文件名称

#### `get_template_context()` {: #get_template_context}

```python
@abstractmethod
def get_template_context(self) -> Dict[str, Any]
```

获取模板渲染所需的上下文数据。

**Returns:**
- `Dict[str, Any]`: 模板上下文数据字典

### 核心方法

#### `render_html()` {: #render_html}

```python
def render_html(self) -> str
```

将 Widget 渲染为 HTML 字符串。

**Returns:**
- `str`: 渲染后的 HTML 字符串

**说明:**
使用模板引擎渲染 Widget，包含完整的容错机制。如果渲染失败，会返回错误提示的 HTML。

**示例:**
```python
class MyWidget(BaseWidget):
    TEMPLATE = "<div>{{ content }}</div>"
    
    def _get_template_name(self):
        return "my_widget.html"
    
    def get_template_context(self):
        return {"content": "Hello World"}

widget = MyWidget()
html = widget.render_html()
print(html)  # <div>Hello World</div>
```

#### `set_widget_id()` {: #set_widget_id}

```python
def set_widget_id(self, widget_id: str) -> 'BaseWidget'
```

设置 Widget 的 ID。

**Parameters:**
- `widget_id` (`str`): 新的 Widget ID

**Returns:**
- `BaseWidget`: 返回 self 以支持链式调用

**示例:**
```python
widget = MyWidget()
widget.set_widget_id("my_custom_id")
print(widget.widget_id)  # my_custom_id
```

### 内部方法

#### `_set_parent()` {: #_set_parent}

```python
def _set_parent(self, parent: 'Email') -> None
```

设置 Widget 的父容器。这是一个内部方法，当 Widget 被添加到 Email 容器时会自动调用。

#### `_generate_id()` {: #_generate_id}

```python
def _generate_id(self) -> str
```

生成唯一的 Widget ID。

**Returns:**
- `str`: 格式为 `{类名小写}_{8位随机十六进制字符}` 的唯一 ID

#### `_render_error_fallback()` {: #_render_error_fallback}

```python
def _render_error_fallback(self, error_msg: str = "") -> str
```

渲染失败时的降级处理。

**Parameters:**
- `error_msg` (`str`): 错误信息

**Returns:**
- `str`: 降级 HTML 字符串

### 继承示例

```python
from email_widget.core.base import BaseWidget
from typing import Dict, Any

class CustomWidget(BaseWidget):
    """自定义 Widget 示例"""
    
    TEMPLATE = """
    <div style="{{ container_style }}">
        <h3>{{ title }}</h3>
        <p>{{ content }}</p>
    </div>
    """
    
    def __init__(self, widget_id: Optional[str] = None):
        super().__init__(widget_id)
        self._title = ""
        self._content = ""
    
    def _get_template_name(self) -> str:
        return "custom_widget.html"
    
    def get_template_context(self) -> Dict[str, Any]:
        return {
            "title": self._title,
            "content": self._content,
            "container_style": "padding: 16px; border: 1px solid #ccc;"
        }
    
    def set_title(self, title: str) -> 'CustomWidget':
        self._title = title
        return self
    
    def set_content(self, content: str) -> 'CustomWidget':
        self._content = content
        return self

# 使用示例
widget = CustomWidget()
widget.set_title("自定义标题").set_content("自定义内容")
html = widget.render_html()
```

---

## TemplateEngine

::: email_widget.core.template_engine.TemplateEngine

基于 Jinja2 的模板引擎，负责 Widget 模板的渲染。

### 主要功能

- **模板渲染**: 使用 Jinja2 渲染 Widget 模板
- **缓存管理**: 模板编译缓存提升性能
- **错误处理**: 安全的模板渲染和错误恢复
- **上下文处理**: 自动处理模板上下文数据

### 核心方法

#### `render_safe()` {: #render_safe}

```python
def render_safe(self, template_str: str, context: Dict[str, Any], 
               fallback: str = "") -> str
```

安全地渲染模板字符串。

**Parameters:**
- `template_str` (`str`): 模板字符串
- `context` (`Dict[str, Any]`): 模板上下文数据
- `fallback` (`str`): 渲染失败时的降级内容

**Returns:**
- `str`: 渲染后的 HTML 字符串

### 获取实例

```python
from email_widget.core.template_engine import get_template_engine

engine = get_template_engine()
html = engine.render_safe(
    "<div>{{ name }}</div>", 
    {"name": "EmailWidget"}
)
```

---

## ImageCache

::: email_widget.core.cache.ImageCache

LRU 缓存系统，用于提升模板渲染和图片处理性能。

### 主要功能

- **LRU 策略**: 最近最少使用的缓存淘汰策略
- **内存管理**: 自动管理缓存大小和内存使用
- **多类型支持**: 支持字符串、图片等多种数据类型缓存
- **性能监控**: 提供缓存命中率统计

### 核心方法

#### `get()` {: #cache_get}

```python
def get(self, key: str) -> Optional[Any]
```

从缓存中获取数据。

#### `set()` {: #cache_set}

```python
def set(self, key: str, value: Any) -> None
```

向缓存中存储数据。

#### `clear()` {: #cache_clear}

```python
def clear() -> None
```

清空所有缓存数据。

### 使用示例

```python
from email_widget.core.cache import get_cache

cache = get_cache()

# 存储数据
cache.set("user_data", {"name": "张三", "age": 30})

# 获取数据
user_data = cache.get("user_data")
if user_data:
    print(f"用户: {user_data['name']}")
```

---

## Logger

::: email_widget.core.logger.get_project_logger

项目日志系统，提供结构化的日志记录功能。

### 日志级别

| 级别 | 说明 | 使用场景 |
|------|------|----------|
| `DEBUG` | 调试信息 | 开发阶段的详细信息 |
| `INFO` | 一般信息 | 正常操作记录 |
| `WARNING` | 警告信息 | 可能的问题提醒 |
| `ERROR` | 错误信息 | 错误但不致命的问题 |
| `CRITICAL` | 严重错误 | 系统级严重问题 |

### 获取 Logger

```python
from email_widget.core.logger import get_project_logger

logger = get_project_logger()

# 记录不同级别的日志
logger.debug("调试信息: 模板渲染开始")
logger.info("邮件创建成功")
logger.warning("使用了过时的方法")
logger.error("Widget 渲染失败")
logger.critical("系统内存不足")
```

### 环境变量配置

可以通过环境变量控制日志行为：

```bash
# 设置日志级别
export EMAILWIDGET_LOG_LEVEL=DEBUG

# 禁用日志输出
export EMAILWIDGET_LOG_LEVEL=NONE
```

---

## 设计模式

### 抽象工厂模式

BaseWidget 使用抽象工厂模式，统一了所有 Widget 的创建接口：

```python
# 所有 Widget 都遵循相同的创建模式
text_widget = TextWidget().set_content("文本")
table_widget = TableWidget().set_headers(["列1", "列2"])
chart_widget = ChartWidget().set_image_url("chart.png")
```

### 模板方法模式

Widget 的渲染过程使用模板方法模式：

```python
# BaseWidget 定义渲染框架
def render_html(self) -> str:
    # 1. 获取模板（子类实现）
    template = self._get_template_name()
    # 2. 获取上下文（子类实现）  
    context = self.get_template_context()
    # 3. 渲染模板（基类实现）
    return self._template_engine.render_safe(template, context)
```

### 单例模式

模板引擎和缓存系统使用单例模式：

```python
# 全局共享同一个实例
engine1 = get_template_engine()
engine2 = get_template_engine()
assert engine1 is engine2  # True
```

---

## 最佳实践

### 1. 继承 BaseWidget

创建自定义 Widget 时，继承 BaseWidget 并实现必要的抽象方法：

```python
class MyWidget(BaseWidget):
    def _get_template_name(self):
        return "my_widget.html"
    
    def get_template_context(self):
        return {"data": self._data}
```

### 2. 模板设计

- 使用内联样式确保邮件客户端兼容性
- 提供合理的默认值
- 使用条件渲染处理可选内容

```python
TEMPLATE = """
{% if title %}
    <h3>{{ title }}</h3>
{% endif %}
<div style="color: {{ color|default('#333') }};">
    {{ content }}
</div>
"""
```

### 3. 错误处理

在模板上下文中提供错误处理：

```python
def get_template_context(self):
    try:
        data = self._process_data()
    except Exception as e:
        self._logger.error(f"数据处理失败: {e}")
        data = {"error": "数据处理失败"}
    
    return data
```

### 4. 性能优化

- 利用缓存避免重复计算
- 延迟加载大型资源
- 使用生成器处理大数据集

```python
@lru_cache(maxsize=128)
def _expensive_calculation(self, param):
    # 耗时计算
    return result
``` 