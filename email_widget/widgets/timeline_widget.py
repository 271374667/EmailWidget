"""时间线组件模块

提供TimelineWidget类，用于在邮件中创建时间线展示。
支持多种事件类型、时间格式和样式配置。
"""

from datetime import datetime
from typing import Any

from email_widget.core.base import BaseWidget
from email_widget.core.enums import StatusType
from email_widget.core.validators import TypeValidator


class TimelineWidget(BaseWidget):
    """时间线组件，用于创建事件时间线展示。

    TimelineWidget 用于显示一系列按时间顺序排列的事件，每个事件可以有不同的状态、描述和时间戳。
    适用于项目进度、历史记录、流程步骤等场景。

    Attributes:
        events (List[Dict[str, Any]]): 时间线事件列表
        title (str): 时间线标题
        show_time (bool): 是否显示时间信息
        reverse_order (bool): 是否按时间倒序排列

    Examples:
        基础用法:
        ```python
        timeline = TimelineWidget()
        timeline.add_event("项目启动", "2024-01-01", "项目正式开始")
        timeline.add_event("需求确认", "2024-01-15", "完成需求分析文档")
        timeline.add_event("开发完成", "2024-02-28", "代码开发完成")
        ```

        使用链式调用:
        ```python
        timeline = (TimelineWidget()
            .set_title("项目里程碑")
            .add_event("立项", "2024-01-01", status_type="success")
            .add_event("开发中", "2024-01-15", status_type="primary")
            .show_timestamps(True))
        ```

        自定义事件类型:
        ```python
        timeline = TimelineWidget()
        timeline.add_event("系统上线", "2024-03-01", "生产环境部署", "success")
        timeline.add_event("发现bug", "2024-03-05", "用户反馈问题", "error")
        timeline.add_event("修复完成", "2024-03-06", "问题已解决", "success")
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
        ">{{ title }}</h3>
        {% endif %}
        
        <div style="position: relative;">
            <!-- 时间线主线 -->
            {% if events|length > 1 %}
            <div style="
                position: absolute;
                left: 18px;
                top: 30px;
                bottom: 30px;
                width: 2px;
                background: #e1dfdd;
                z-index: 1;
            "></div>
            {% endif %}
            
            <!-- 事件列表 -->
            {% for event in events %}
            <div style="
                position: relative;
                display: flex;
                align-items: flex-start;
                margin-bottom: {% if not loop.last %}24px{% else %}0{% endif %};
                z-index: 2;
            ">
                <!-- 事件点 -->
                <div style="
                    width: 36px;
                    height: 36px;
                    border-radius: 50%;
                    background: {{ event.status_color }};
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin-right: 16px;
                    flex-shrink: 0;
                    border: 3px solid #ffffff;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    position: relative;
                    z-index: 3;
                ">
                    <span style="
                        color: #ffffff;
                        font-size: 14px;
                        font-weight: 600;
                    ">{{ event.status_icon }}</span>
                </div>
                
                <!-- 事件内容 -->
                <div style="
                    flex: 1;
                    background: #f8f9fa;
                    border: 1px solid #e9ecef;
                    border-radius: 8px;
                    padding: 16px;
                    margin-top: 6px;
                ">
                    <div style="
                        display: flex;
                        justify-content: space-between;
                        align-items: flex-start;
                        margin-bottom: {% if event.description %}8px{% else %}0{% endif %};
                    ">
                        <h4 style="
                            color: #323130;
                            margin: 0;
                            font-size: 14px;
                            font-weight: 600;
                            line-height: 1.3;
                        ">{{ event.title }}</h4>
                        {% if show_time and event.time_display %}
                        <span style="
                            color: #8e8e93;
                            font-size: 12px;
                            font-weight: 500;
                            margin-left: 12px;
                            white-space: nowrap;
                        ">{{ event.time_display }}</span>
                        {% endif %}
                    </div>
                    {% if event.description %}
                    <div style="
                        color: #605e5c;
                        font-size: 13px;
                        line-height: 1.4;
                        margin: 0;
                    ">{{ event.description }}</div>
                    {% endif %}
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
    """

    def __init__(self):
        """初始化时间线组件。"""
        super().__init__()
        self._events: list[dict[str, Any]] = []
        self._title: str = ""
        self._show_time: bool = False
        self._reverse_order: bool = False

        # 初始化验证器
        self._str_validator = TypeValidator(str)
        self._bool_validator = TypeValidator(bool)

        # 状态主题映射
        self._status_themes = {
            "success": {"color": "#107c10", "icon": "✓", "text": "成功"},
            "warning": {"color": "#ff8c00", "icon": "!", "text": "警告"},
            "error": {"color": "#d13438", "icon": "✗", "text": "错误"},
            "info": {"color": "#0078d4", "icon": "i", "text": "信息"},
            "primary": {"color": "#0078d4", "icon": "●", "text": "主要"},
            "default": {"color": "#8e8e93", "icon": "○", "text": "默认"},
        }

    def _get_template_name(self) -> str:
        """获取模板名称。"""
        return "timeline_widget.html"

    def add_event(
        self,
        title: str,
        time: str | datetime | None = None,
        description: str = "",
        status_type: str | StatusType | None = None,
    ) -> "TimelineWidget":
        """添加时间线事件。

        Args:
            title (str): 事件标题
            time (Union[str, datetime, None]): 事件时间，可选
            description (str): 事件描述
            status_type (Union[str, StatusType, None]): 状态类型

        Returns:
            TimelineWidget: 返回self以支持链式调用

        Examples:
            ```python
            timeline.add_event("项目启动", "2024-01-01", "项目正式开始")
            timeline.add_event("里程碑达成", datetime.now(), "重要节点", "success")
            timeline.add_event("问题发现", None, "发现系统bug", "error")
            ```
        """
        if not self._str_validator.validate(title):
            raise TypeError(
                f"title参数必须是字符串类型，当前类型为: {type(title).__name__}"
            )

        # 处理状态类型
        if status_type is None:
            status_key = "default"
        elif isinstance(status_type, StatusType):
            status_key = status_type.value
        else:
            status_key = str(status_type)

        # 验证状态类型
        if status_key not in self._status_themes:
            status_key = "default"

        theme = self._status_themes[status_key]

        # 处理时间显示
        time_display = ""
        time_sort_key = datetime.now()  # 默认排序键

        if time is not None:
            if isinstance(time, str):
                time_display = time
                # 尝试解析字符串为datetime用于排序
                try:
                    if len(time) == 10 and "-" in time:  # YYYY-MM-DD格式
                        time_sort_key = datetime.strptime(time, "%Y-%m-%d")
                    elif len(time) == 19 and " " in time:  # YYYY-MM-DD HH:MM:SS格式
                        time_sort_key = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
                    else:
                        time_sort_key = datetime.now()
                except ValueError:
                    time_sort_key = datetime.now()
            elif isinstance(time, datetime):
                time_display = time.strftime("%Y-%m-%d %H:%M")
                time_sort_key = time

        event = {
            "title": title,
            "description": description,
            "time_display": time_display,
            "time_sort_key": time_sort_key,
            "status_color": theme["color"],
            "status_icon": theme["icon"],
            "status_text": theme["text"],
        }

        self._events.append(event)
        self._sort_events()  # 每次添加后重新排序
        return self

    def _sort_events(self):
        """根据时间对事件进行排序。"""
        self._events.sort(key=lambda x: x["time_sort_key"], reverse=self._reverse_order)

    def set_title(self, title: str) -> "TimelineWidget":
        """设置时间线标题。

        Args:
            title (str): 时间线标题

        Returns:
            TimelineWidget: 返回self以支持链式调用
        """
        if not self._str_validator.validate(title):
            raise TypeError(
                f"title参数必须是字符串类型，当前类型为: {type(title).__name__}"
            )
        self._title = title
        return self

    def show_timestamps(self, show: bool = True) -> "TimelineWidget":
        """设置是否显示时间戳。

        Args:
            show (bool): 是否显示时间信息

        Returns:
            TimelineWidget: 返回self以支持链式调用
        """
        if not self._bool_validator.validate(show):
            raise TypeError(
                f"show参数必须是布尔类型，当前类型为: {type(show).__name__}"
            )
        self._show_time = show
        return self

    def set_reverse_order(self, reverse: bool = True) -> "TimelineWidget":
        """设置是否按时间倒序排列。

        Args:
            reverse (bool): 是否倒序排列（最新的在前）

        Returns:
            TimelineWidget: 返回self以支持链式调用
        """
        if not self._bool_validator.validate(reverse):
            raise TypeError(
                f"reverse参数必须是布尔类型，当前类型为: {type(reverse).__name__}"
            )
        self._reverse_order = reverse
        self._sort_events()  # 重新排序
        return self

    def clear_events(self) -> "TimelineWidget":
        """清空所有事件。

        Returns:
            TimelineWidget: 返回self以支持链式调用
        """
        self._events.clear()
        return self

    def remove_event(self, index: int) -> "TimelineWidget":
        """根据索引移除事件。

        Args:
            index (int): 要移除的事件索引

        Returns:
            TimelineWidget: 返回self以支持链式调用

        Raises:
            IndexError: 当索引超出范围时
        """
        if not self._str_validator.validate(str(index)) or not isinstance(index, int):
            raise TypeError(
                f"index参数必须是整数类型，当前类型为: {type(index).__name__}"
            )
        if 0 <= index < len(self._events):
            self._events.pop(index)
        else:
            raise IndexError(
                f"索引 {index} 超出范围，当前有 {len(self._events)} 个事件"
            )
        return self

    @property
    def events(self) -> list[dict[str, Any]]:
        """获取所有时间线事件。

        Returns:
            List[Dict[str, Any]]: 事件列表
        """
        return self._events.copy()

    @property
    def title(self) -> str:
        """获取时间线标题。

        Returns:
            str: 时间线标题
        """
        return self._title

    @property
    def event_count(self) -> int:
        """获取事件总数。

        Returns:
            int: 事件总数
        """
        return len(self._events)

    def get_template_context(self) -> dict[str, Any]:
        """获取模板渲染上下文。

        Returns:
            Dict[str, Any]: 模板上下文数据
        """
        return {
            "events": self._events,
            "title": self._title,
            "show_time": self._show_time,
            "reverse_order": self._reverse_order,
        }
