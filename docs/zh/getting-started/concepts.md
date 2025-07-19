# 📚 基本概念

在深入使用EmailWidget之前，理解其核心概念将帮助你更好地构建邮件报告。本章将介绍EmailWidget的设计理念和关键概念。

## 📧 Email类详解

### 基本概念

`Email`类是EmailWidget的核心，它充当所有Widget的容器和管理器：

```python
from email_widget import Email, TextWidget

# 创建邮件对象
email = Email(title="报告标题")

# 设置元信息
email.set_subtitle("副标题")
email.set_footer("脚注信息")

# 管理Widget
email.add_widget(TextWidget('Hello, World!'))
email.remove_widget("Hello, World!")
email.clear_widgets()

# 导出结果
html_content = email.export_str()
file_path = email.export_html("report.html")
```

### 生命周期

Email对象的典型生命周期：

1. **创建** - 初始化邮件对象
2. **配置** - 设置标题、副标题、脚注等
3. **添加内容** - 添加各种Widget组件
4. **渲染** - 生成HTML内容
5. **导出** - 保存为文件或获取字符串

### 特性功能

=== "便捷方法"
    
    ```python
    # 直接添加常用内容
    email.add_text("标题", text_type="title_large")
    email.add_table_from_data(data, headers)
    email.add_progress(75, "完成度")
    email.add_chart_from_plt(title="图表")
    ```

=== "Widget管理"
    
    ```python
    # 获取Widget
    widget = email.get_widget("my_widget_id")
    
    # 移除Widget
    email.remove_widget("widget_id")
    
    # 清空所有Widget
    email.clear_widgets()
    
    # 获取Widget数量
    count = email.get_widget_count()
    ```

=== "链式调用"
    
    ```python
    # 流畅的API设计
    email = (Email("标题")
             .set_subtitle("副标题")
             .set_footer("脚注")
             .add_widget(widget1)
             .add_widget(widget2))
    ```

## 🧩 Widget组件系统

### 设计理念

所有Widget组件都继承自`BaseWidget`，确保API的一致性：

```python
from email_widget.core.base import BaseWidget

class MyCustomWidget(BaseWidget):
    def __init__(self):
        super().__init__()
        self.widget_type = "custom"
    
    def render(self) -> str:
        # 渲染逻辑
        return self._render_template("custom.html", context)
```

### 公共特性

所有Widget都具有以下共同特性：

=== "标识管理"
    
    ```python
    # 设置唯一ID
    widget.set_widget_id("my_unique_id")
    
    # 获取ID
    widget_id = widget.widget_id
    
    # 获取类型
    widget_type = widget.widget_type
    ```

=== "模板渲染"
    
    ```python
    # 获取渲染上下文
    context = widget.get_template_context()
    
    # 渲染为HTML
    html = widget.render_html()
    ```

### Widget分类

EmailWidget提供12种专业组件，按功能分类：

#### 📝 内容组件
- **TextWidget** - 文本内容，8种样式
- **ImageWidget** - 图片展示，多源支持
- **QuoteWidget** - 引用样式，作者信息

#### 📊 数据组件  
- **TableWidget** - 数据表格，DataFrame集成
- **ChartWidget** - 图表展示，matplotlib支持
- **LogWidget** - 日志显示，级别分类

#### 📈 指标组件
- **ProgressWidget** - 线性进度条，5种主题
- **CircularProgressWidget** - 圆形进度，多种尺寸
- **StatusWidget** - 状态管理，动态更新

#### 🎨 界面组件
- **AlertWidget** - 警告提醒，5种类型
- **CardWidget** - 信息卡片，图标支持
- **ColumnWidget** - 布局容器，响应式设计


## 🎯 最佳实践

### 代码组织

建议的代码组织方式：

```python
# 1. 导入必要的库
from email_widget import Email, TextWidget, TableWidget, EmailConfig
from email_widget.core.enums import TextType


# 2. 数据准备
def prepare_data():
    return {"sales": [100, 200, 300]}


# 3. 邮件构建
def build_email(data):
    email = Email("销售报告")
    # 添加内容
    email.add_widget(
        TextWidget().set_content("销售数据分析").set_type(TextType.TITLE_LARGE)
    )

    return email


# 4. 主函数
def main():
    data = prepare_data()
    email = build_email(data)
    email.export_html("report.html")
```

## 🚀 下一步

现在你已经理解了EmailWidget的核心概念，可以：

- 查看 [用户指南](../user-guide/index.md) 学习各组件详细用法
- 浏览 [API参考](../api/index.md) 了解完整API
- 研究 [示例代码](../examples/index.md) 学习实际应用
- 阅读 [开发指南](../development/index.md) 参与项目开发