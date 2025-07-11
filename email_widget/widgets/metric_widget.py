"""指标组件模块

提供MetricWidget类，用于在邮件中展示关键数据指标。
支持多种指标类型、趋势显示和样式配置。
"""

from typing import Any

from email_widget.core.base import BaseWidget
from email_widget.core.enums import StatusType
from email_widget.core.validators import TypeValidator


class MetricWidget(BaseWidget):
    """指标组件，用于展示关键数据指标。

    MetricWidget 用于显示重要的数据指标，包括数值、标题、趋势变化等信息。
    适用于仪表板、KPI展示、数据监控等场景。

    Attributes:
        metrics (List[Dict[str, Any]]): 指标列表
        title (str): 指标组标题
        layout (str): 布局方式（horizontal/vertical）
        show_trend (bool): 是否显示趋势

    Examples:
        基础用法:
        ```python
        metric = MetricWidget()
        metric.add_metric("用户总数", "12,345", "人")
        metric.add_metric("月活跃", "8,456", "人", "+15.6%", "success")
        metric.add_metric("转化率", "3.2", "%", "-0.8%", "warning")
        ```

        使用链式调用:
        ```python
        metric = (MetricWidget()
            .set_title("核心指标")
            .add_metric("销售额", "¥1,250,000", "", "+12.3%", "success")
            .add_metric("订单量", "2,456", "单", "-3.2%", "error")
            .set_layout("horizontal"))
        ```

        多指标展示:
        ```python
        metric = MetricWidget()
        metric.set_title("系统性能")
        metric.add_metric("CPU使用率", "45.2", "%", "+2.1%", "warning")
        metric.add_metric("内存使用", "78.5", "%", "-1.3%", "success")
        metric.add_metric("磁盘空间", "23.8", "GB", "+5.2GB", "info")
        ```
    """

    TEMPLATE = """
    <div style="
        background: #ffffff;
        border: 1px solid #e1dfdd;
        border-radius: 8px;
        padding: 20px;
        margin: 16px 0;
        font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
    ">
        {% if title %}
        <h3 style="
            color: #323130;
            margin: 0 0 20px 0;
            font-size: 16px;
            font-weight: 600;
            text-align: center;
        ">{{ title }}</h3>
        {% endif %}
        
        <div style="
            display: {% if layout == 'horizontal' %}flex{% else %}block{% endif %};
            {% if layout == 'horizontal' %}
            flex-wrap: wrap;
            justify-content: space-around;
            align-items: stretch;
            {% endif %}
            gap: {% if layout == 'horizontal' %}16px{% else %}12px{% endif %};
        ">
            {% for metric in metrics %}
            <div style="
                {% if layout == 'horizontal' %}
                flex: 1;
                min-width: 150px;
                max-width: 250px;
                {% else %}
                width: 100%;
                {% endif %}
                background: {{ metric.background_color }};
                border: 1px solid {{ metric.border_color }};
                border-radius: 8px;
                padding: 16px;
                text-align: center;
                margin-bottom: {% if layout == 'vertical' %}12px{% else %}0{% endif %};
                position: relative;
                transition: transform 0.2s ease;
            ">
                <!-- 指标值 -->
                <div style="
                    font-size: 28px;
                    font-weight: 700;
                    color: {{ metric.value_color }};
                    line-height: 1.1;
                    margin-bottom: 4px;
                ">
                    {{ metric.value }}{% if metric.unit %}<span style="font-size: 18px; font-weight: 500; color: #8e8e93;">{{ metric.unit }}</span>{% endif %}
                </div>
                
                <!-- 指标标题 -->
                <div style="
                    font-size: 13px;
                    font-weight: 500;
                    color: #605e5c;
                    margin-bottom: {% if metric.trend or metric.description %}8px{% else %}0{% endif %};
                    text-transform: uppercase;
                    letter-spacing: 0.5px;
                ">{{ metric.label }}</div>
                
                {% if metric.trend %}
                <!-- 趋势显示 -->
                <div style="
                    font-size: 12px;
                    font-weight: 600;
                    color: {{ metric.trend_color }};
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin-bottom: {% if metric.description %}6px{% else %}0{% endif %};
                ">
                    <span style="margin-right: 4px;">{{ metric.trend_icon }}</span>
                    <span>{{ metric.trend }}</span>
                </div>
                {% endif %}
                
                {% if metric.description %}
                <!-- 描述信息 -->
                <div style="
                    font-size: 11px;
                    color: #8e8e93;
                    line-height: 1.3;
                    margin-top: 6px;
                ">{{ metric.description }}</div>
                {% endif %}
            </div>
            {% endfor %}
        </div>
    </div>
    """

    def __init__(self):
        """初始化指标组件。"""
        super().__init__()
        self._metrics: list[dict[str, Any]] = []
        self._title: str = ""
        self._layout: str = "horizontal"  # horizontal / vertical
        self._show_trend: bool = True

        # 初始化验证器
        self._str_validator = TypeValidator(str)
        self._bool_validator = TypeValidator(bool)

        # 趋势主题映射
        self._trend_themes = {
            "success": {
                "color": "#107c10",
                "bg": "#f3f9f1",
                "border": "#c8e6c5",
                "icon": "↗",
            },
            "warning": {
                "color": "#ff8c00",
                "bg": "#fff9f0",
                "border": "#ffd6a5",
                "icon": "→",
            },
            "error": {
                "color": "#d13438",
                "bg": "#fdf2f2",
                "border": "#f5c6cb",
                "icon": "↘",
            },
            "info": {
                "color": "#0078d4",
                "bg": "#f0f6ff",
                "border": "#a5c8f0",
                "icon": "→",
            },
            "primary": {
                "color": "#0078d4",
                "bg": "#f0f6ff",
                "border": "#a5c8f0",
                "icon": "●",
            },
            "neutral": {
                "color": "#8e8e93",
                "bg": "#fafafa",
                "border": "#e1dfdd",
                "icon": "—",
            },
        }

    def _get_template_name(self) -> str:
        """获取模板名称。"""
        return "metric_widget.html"

    def add_metric(
        self,
        label: str,
        value: str | int | float,
        unit: str = "",
        trend: str = "",
        trend_type: str | StatusType | None = None,
        description: str = "",
    ) -> "MetricWidget":
        """添加指标。

        Args:
            label (str): 指标标题
            value (Union[str, int, float]): 指标值
            unit (str): 单位，可选
            trend (str): 趋势变化，可选（如 "+12.3%", "-5.6%"）
            trend_type (Union[str, StatusType, None]): 趋势类型
            description (str): 描述信息，可选

        Returns:
            MetricWidget: 返回self以支持链式调用

        Examples:
            ```python
            metric.add_metric("用户数", 12345, "人")
            metric.add_metric("增长率", "15.6", "%", "+2.3%", "success", "环比增长")
            metric.add_metric("收入", "¥1,250,000", "", "+12.3%", "success")
            ```
        """
        if not self._str_validator.validate(label):
            raise TypeError(
                f"label参数必须是字符串类型，当前类型为: {type(label).__name__}"
            )

        # 处理趋势类型
        if trend and trend_type is None:
            # 自动判断趋势类型
            if trend.startswith("+"):
                trend_key = "success"
            elif trend.startswith("-"):
                trend_key = "error"
            else:
                trend_key = "neutral"
        elif trend_type is None:
            trend_key = "neutral"
        elif isinstance(trend_type, StatusType):
            trend_key = trend_type.value
        else:
            trend_key = str(trend_type)

        # 验证趋势类型
        if trend_key not in self._trend_themes:
            trend_key = "neutral"

        theme = self._trend_themes[trend_key]

        # 处理指标值显示
        if isinstance(value, (int, float)):
            # 格式化数字
            if isinstance(value, float):
                if value >= 1000000:
                    display_value = f"{value / 1000000:.1f}M"
                elif value >= 1000:
                    display_value = f"{value / 1000:.1f}K"
                else:
                    display_value = f"{value:.1f}"
            else:
                if value >= 1000000:
                    display_value = f"{value // 1000000}M"
                elif value >= 1000:
                    display_value = f"{value // 1000}K"
                else:
                    display_value = str(value)
        else:
            display_value = str(value)

        metric = {
            "label": label,
            "value": display_value,
            "unit": unit,
            "trend": trend,
            "trend_type": trend_key,
            "trend_color": theme["color"],
            "trend_icon": theme["icon"],
            "description": description,
            "background_color": theme["bg"],
            "border_color": theme["border"],
            "value_color": "#323130" if trend_key == "neutral" else theme["color"],
        }

        self._metrics.append(metric)
        return self

    def set_title(self, title: str) -> "MetricWidget":
        """设置指标组标题。

        Args:
            title (str): 指标组标题

        Returns:
            MetricWidget: 返回self以支持链式调用
        """
        if not self._str_validator.validate(title):
            raise TypeError(
                f"title参数必须是字符串类型，当前类型为: {type(title).__name__}"
            )
        self._title = title
        return self

    def set_layout(self, layout: str) -> "MetricWidget":
        """设置布局方式。

        Args:
            layout (str): 布局方式，'horizontal' 或 'vertical'

        Returns:
            MetricWidget: 返回self以支持链式调用
        """
        if not self._str_validator.validate(layout):
            raise TypeError(
                f"layout参数必须是字符串类型，当前类型为: {type(layout).__name__}"
            )
        if layout not in ["horizontal", "vertical"]:
            raise ValueError(
                f"layout必须是 'horizontal' 或 'vertical'，当前值为: {layout}"
            )
        self._layout = layout
        return self

    def show_trends(self, show: bool = True) -> "MetricWidget":
        """设置是否显示趋势。

        Args:
            show (bool): 是否显示趋势信息

        Returns:
            MetricWidget: 返回self以支持链式调用
        """
        if not self._bool_validator.validate(show):
            raise TypeError(
                f"show参数必须是布尔类型，当前类型为: {type(show).__name__}"
            )
        self._show_trend = show
        return self

    def clear_metrics(self) -> "MetricWidget":
        """清空所有指标。

        Returns:
            MetricWidget: 返回self以支持链式调用
        """
        self._metrics.clear()
        return self

    def remove_metric(self, index: int) -> "MetricWidget":
        """根据索引移除指标。

        Args:
            index (int): 要移除的指标索引

        Returns:
            MetricWidget: 返回self以支持链式调用

        Raises:
            IndexError: 当索引超出范围时
        """
        if not isinstance(index, int):
            raise TypeError(
                f"index参数必须是整数类型，当前类型为: {type(index).__name__}"
            )
        if 0 <= index < len(self._metrics):
            self._metrics.pop(index)
        else:
            raise IndexError(
                f"索引 {index} 超出范围，当前有 {len(self._metrics)} 个指标"
            )
        return self

    @property
    def metrics(self) -> list[dict[str, Any]]:
        """获取所有指标。

        Returns:
            List[Dict[str, Any]]: 指标列表
        """
        return self._metrics.copy()

    @property
    def title(self) -> str:
        """获取指标组标题。

        Returns:
            str: 指标组标题
        """
        return self._title

    @property
    def metric_count(self) -> int:
        """获取指标总数。

        Returns:
            int: 指标总数
        """
        return len(self._metrics)

    @property
    def layout(self) -> str:
        """获取布局方式。

        Returns:
            str: 布局方式
        """
        return self._layout

    def get_template_context(self) -> dict[str, Any]:
        """获取模板渲染上下文。

        Returns:
            Dict[str, Any]: 模板上下文数据
        """
        # 过滤不显示趋势的指标
        filtered_metrics = self._metrics.copy()
        if not self._show_trend:
            for metric in filtered_metrics:
                metric["trend"] = ""

        return {
            "metrics": filtered_metrics,
            "title": self._title,
            "layout": self._layout,
            "show_trend": self._show_trend,
        }
