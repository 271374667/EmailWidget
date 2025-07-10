"""日志Widget实现"""

import re
from abc import ABC, abstractmethod
from datetime import datetime
from typing import TYPE_CHECKING, Any, Optional

from email_widget.core.base import BaseWidget
from email_widget.core.enums import LogLevel

if TYPE_CHECKING:
    pass


class LogParser(ABC):
    """日志解析器抽象基类。

    这个抽象基类定义了所有日志解析器必须实现的接口。
    每个具体的解析器都应该能够检查是否能解析特定格式的日志行，
    并将其转换为LogEntry对象。

    Examples:
        ```python
        class MyCustomParser(LogParser):
            def can_parse(self, log_line: str) -> bool:
                return "CUSTOM:" in log_line

            def parse(self, log_line: str) -> Optional[LogEntry]:
                if self.can_parse(log_line):
                    # 解析逻辑
                    return LogEntry("解析后的消息", LogLevel.INFO)
                return None

            @property
            def parser_name(self) -> str:
                return "CustomParser"
        ```
    """

    @abstractmethod
    def can_parse(self, log_line: str) -> bool:
        """检查是否能解析该日志行。

        Args:
            log_line (str): 待检查的日志行。

        Returns:
            bool: 如果可以解析返回True，否则返回False。
        """
        pass

    @abstractmethod
    def parse(self, log_line: str) -> Optional["LogEntry"]:
        """解析日志行，返回LogEntry对象。

        Args:
            log_line (str): 待解析的日志行。

        Returns:
            Optional[LogEntry]: 解析成功返回LogEntry对象，失败返回None。
        """
        pass

    @property
    @abstractmethod
    def parser_name(self) -> str:
        """解析器名称。

        Returns:
            str: 解析器的唯一名称标识。
        """
        pass


class LogEntry:
    """表示单个日志条目的数据结构。

    这个类用于封装从日志字符串中解析出来或手动创建的日志信息，
    包括消息内容、日志级别、时间戳以及来源（模块、函数、行号）。

    Attributes:
        message (str): 日志消息内容。
        level (LogLevel): 日志级别，默认为 `LogLevel.INFO`。
        timestamp (datetime): 日志记录的时间戳，默认为当前时间。
        module (Optional[str]): 记录日志的模块名称。
        function (Optional[str]): 记录日志的函数名称。
        line_number (Optional[int]): 记录日志的代码行号。

    Examples:
        ```python
        from datetime import datetime
        from email_widget.core.enums import LogLevel

        # 创建一个信息级别的日志条目
        info_log = LogEntry("用户登录成功", level=LogLevel.INFO, timestamp=datetime.now())

        # 创建一个错误级别的日志条目，包含来源信息
        error_log = LogEntry("数据库连接失败", level=LogLevel.ERROR,
                             module="db_connector", function="connect", line_number=123)
        ```
    """

    def __init__(
        self,
        message: str,
        level: LogLevel = LogLevel.INFO,
        timestamp: datetime | None = None,
        module: str | None = None,
        function: str | None = None,
        line_number: int | None = None,
    ):
        """初始化LogEntry。

        Args:
            message (str): 日志消息内容。
            level (LogLevel): 日志级别，默认为 `LogLevel.INFO`。
            timestamp (Optional[datetime]): 日志记录的时间戳，默认为当前时间。
            module (Optional[str]): 记录日志的模块名称。
            function (Optional[str]): 记录日志的函数名称。
            line_number (Optional[int]): 记录日志的代码行号。
        """
        self.message = message
        self.level = level
        self.timestamp = timestamp or datetime.now()
        self.module = module or ""
        self.function = function or ""
        self.line_number = line_number


class LoGuruLogParser(LogParser):
    """Loguru格式日志解析器。

    解析Loguru库生成的日志格式：
    "2024-07-07 10:30:00.123 | INFO | my_app.main:run:45 - Application started"

    这是原有LogWidget默认支持的格式。
    """

    LOG_PATTERN = re.compile(
        r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}) \| "
        r"(DEBUG|INFO|WARNING|ERROR|CRITICAL)\s+\| "
        r"([^:]+):([^:]+):(\d+) - (.+)"
    )

    def can_parse(self, log_line: str) -> bool:
        """检查是否为Loguru格式的日志行"""
        return bool(self.LOG_PATTERN.match(log_line.strip()))

    def parse(self, log_line: str) -> Optional["LogEntry"]:
        """解析Loguru格式的日志行"""
        match = self.LOG_PATTERN.match(log_line.strip())
        if not match:
            return None

        timestamp_str, level_str, module, function, line_num, message = match.groups()

        try:
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S.%f")
        except ValueError:
            timestamp = datetime.now()

        try:
            level = LogLevel(level_str)
        except ValueError:
            level = LogLevel.INFO

        return LogEntry(
            message=message,
            level=level,
            timestamp=timestamp,
            module=module,
            function=function,
            line_number=int(line_num) if line_num.isdigit() else None,
        )

    @property
    def parser_name(self) -> str:
        return "LoGuruLogParser"


class StandardLoggingParser(LogParser):
    """标准logging库格式日志解析器。

    解析Python标准库logging模块生成的日志格式：
    "WARNING:root:hello world"
    "ERROR:my_module:Connection failed"
    """

    LOG_PATTERN = re.compile(r"(DEBUG|INFO|WARNING|ERROR|CRITICAL):([^:]*):(.+)")

    def can_parse(self, log_line: str) -> bool:
        """检查是否为标准logging格式的日志行"""
        return bool(self.LOG_PATTERN.match(log_line.strip()))

    def parse(self, log_line: str) -> Optional["LogEntry"]:
        """解析标准logging格式的日志行"""
        match = self.LOG_PATTERN.match(log_line.strip())
        if not match:
            return None

        level_str, logger_name, message = match.groups()

        try:
            level = LogLevel(level_str)
        except ValueError:
            level = LogLevel.INFO

        return LogEntry(
            message=message,
            level=level,
            timestamp=datetime.now(),
            module=logger_name if logger_name else None,
        )

    @property
    def parser_name(self) -> str:
        return "StandardLoggingParser"


class TimestampLogParser(LogParser):
    """时间戳格式日志解析器。

    解析带时间戳的简单日志格式：
    "2025-07-07 15:24:39,055 - WARNING - hello world"
    "2025-01-15 10:30:45,123 - ERROR - Connection timeout"
    """

    LOG_PATTERN = re.compile(
        r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) - (DEBUG|INFO|WARNING|ERROR|CRITICAL) - (.+)"
    )

    def can_parse(self, log_line: str) -> bool:
        """检查是否为时间戳格式的日志行"""
        return bool(self.LOG_PATTERN.match(log_line.strip()))

    def parse(self, log_line: str) -> Optional["LogEntry"]:
        """解析时间戳格式的日志行"""
        match = self.LOG_PATTERN.match(log_line.strip())
        if not match:
            return None

        timestamp_str, level_str, message = match.groups()

        try:
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S,%f")
        except ValueError:
            timestamp = datetime.now()

        try:
            level = LogLevel(level_str)
        except ValueError:
            level = LogLevel.INFO

        return LogEntry(
            message=message,
            level=level,
            timestamp=timestamp,
        )

    @property
    def parser_name(self) -> str:
        return "TimestampLogParser"


class PlainTextParser(LogParser):
    """纯文本日志解析器。

    这是兜底解析器，将任何文本都视为INFO级别的日志消息。
    输出格式使用 "> 文本内容" 的形式。
    """

    def can_parse(self, log_line: str) -> bool:
        """纯文本解析器总是返回True，作为兜底解析器"""
        return True

    def parse(self, log_line: str) -> Optional["LogEntry"]:
        """将任何文本解析为INFO级别的日志条目"""
        text = log_line.strip()
        if not text:
            return None

        # 使用 "> 文本内容" 格式
        message = f"> {text}"

        return LogEntry(
            message=message,
            level=LogLevel.INFO,
            timestamp=datetime.now(),
        )

    @property
    def parser_name(self) -> str:
        return "PlainTextParser"


class LogWidget(BaseWidget):
    """创建一个用于在邮件中优雅地显示日志信息的代码块。

    该微件特别适合展示程序运行日志、错误报告或任何需要按时间顺序和
    严重性级别呈现的信息。它能够自动解析 `loguru` 格式的日志字符串，
    并根据日志级别（如 INFO, WARNING, ERROR）以不同的颜色高亮显示，
    使其内容清晰易读。

    核心功能:
        - **Loguru 格式解析**: 自动解析包含时间戳、级别、来源和消息的日志行。
        - **级别高亮**: 为不同的日志级别（DEBUG, INFO, WARNING, ERROR, CRITICAL）应用不同的颜色。
        - **内容过滤**: 可以设置一个最低日志级别，只显示该级别及以上的日志。
        - **显示控制**: 可以选择性地显示或隐藏时间戳、日志级别和来源信息。
        - **滚动条**: 当日志内容超出预设的最大高度时，会自动显示滚动条。

    Examples:
        接收一个 `loguru` 格式的日志列表并显示：

        ```python
        from email_widget.widgets import LogWidget
        from email_widget.core.enums import LogLevel

        log_messages = [
            "2024-07-07 10:30:00.123 | INFO     | my_app.main:run:45 - Application started successfully.",
            "2024-07-07 10:31:15.456 | WARNING  | my_app.database:connect:88 - Connection is slow.",
            "2024-07-07 10:32:05.789 | ERROR    | my_app.api:request:152 - Failed to fetch data from API."
        ]

        log_viewer = (LogWidget()
                      .set_title("Application Run Log")
                      .set_logs(log_messages)
                      .set_max_height("300px")
                      .filter_by_level(LogLevel.WARNING)) # 只显示 WARNING 和 ERROR

        # 假设 email 是一个 Email 对象
        # email.add_widget(log_viewer)
        ```

        通过 `add_log_entry` 方法逐条添加日志：

        ```python
        manual_log = (LogWidget()
                      .set_title("Manual Log Entries")
                      .add_log_entry("User logged in.", level=LogLevel.INFO, module="auth")
                      .add_log_entry("Invalid password attempt.", level=LogLevel.WARNING, module="auth"))
        ```
    """

    # 模板定义
    TEMPLATE = """
    {% if logs %}
        <div style="{{ container_style }}">
            {% if title %}
                <h3 style="{{ title_style }}">{{ title }}</h3>
            {% endif %}
            {% for log_entry in logs %}
                <div style="{{ entry_style }}">
                    {% if show_timestamp %}
                        <span style="{{ timestamp_style }}">{{ log_entry.timestamp_str }}</span>
                    {% endif %}
                    {% if show_level %}
                        <span style="{{ log_entry.level_style }}">[{{ log_entry.level }}]</span>
                    {% endif %}
                    {% if show_source and log_entry.source %}
                        <span style="{{ source_style }}">({{ log_entry.source }})</span>
                    {% endif %}
                    <span style="{{ message_style }}">{{ log_entry.message }}</span>
                </div>
            {% endfor %}
        </div>
    {% endif %}
    """

    def __init__(self, widget_id: str | None = None):
        """初始化LogWidget。

        Args:
            widget_id (Optional[str]): 可选的Widget ID。
        """
        super().__init__(widget_id)
        self._logs: list[LogEntry] = []
        self._title: str | None = None
        self._max_height: str = "400px"
        self._show_timestamp: bool = True
        self._show_level: bool = True
        self._show_source: bool = True
        self._filter_level: LogLevel | None = None
        self._background_color: str = "#faf9f8"
        self._border_color: str = "#e1dfdd"

        # 初始化解析器链，按优先级排序
        self._log_parsers: list[LogParser] = [
            LoGuruLogParser(),
            StandardLoggingParser(),
            TimestampLogParser(),
            PlainTextParser(),  # 兜底解析器，必须放在最后
        ]

    def set_log_level(self, level: LogLevel) -> "LogWidget":
        """设置日志过滤级别。

        只有达到或高于此级别的日志才会被显示。

        Args:
            level (LogLevel): 最低日志级别。

        Returns:
            LogWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = LogWidget().set_log_level(LogLevel.WARNING) # 只显示WARNING及以上日志
        """
        self._filter_level = level
        return self

    def append_log(self, log: str) -> "LogWidget":
        """追加单条日志字符串。

        日志字符串会被自动解析为 `LogEntry` 对象并添加到日志列表中。

        Args:
            log (str): 单条日志字符串。

        Returns:
            LogWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = LogWidget().append_log("2024-07-07 10:00:00 | INFO | app:main - 应用启动")
        """
        parsed_entry = self._parse_single_log(log)
        if parsed_entry:
            self._logs.append(parsed_entry)
        return self

    def set_logs(self, logs: list[str]) -> "LogWidget":
        """设置日志列表。

        此方法会清空现有日志，并解析新的日志字符串列表。

        Args:
            logs (List[str]): 日志字符串列表。

        Returns:
            LogWidget: 返回self以支持链式调用。

        Examples:
            >>> logs = ["INFO: App started", "ERROR: Failed to connect"]
            >>> widget = LogWidget().set_logs(logs)
        """
        self._logs.clear()
        for log in logs:
            self.append_log(log)
        return self

    def clear(self) -> "LogWidget":
        """清空所有日志。

        Returns:
            LogWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = LogWidget().clear()
        """
        self._logs.clear()
        return self

    def set_title(self, title: str) -> "LogWidget":
        """设置日志组件的标题。

        Args:
            title (str): 标题文本。

        Returns:
            LogWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = LogWidget().set_title("系统运行日志")
        """
        self._title = title
        return self

    def set_max_height(self, height: str) -> "LogWidget":
        """设置日志显示区域的最大高度。

        当日志内容超出此高度时，将出现滚动条。

        Args:
            height (str): CSS高度值，如 "400px", "50vh"。

        Returns:
            LogWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = LogWidget().set_max_height("300px")
        """
        self._max_height = height
        return self

    def filter_by_level(self, level: LogLevel) -> "LogWidget":
        """按日志级别过滤显示。

        只有级别等于或高于指定 `level` 的日志条目才会被显示。

        Args:
            level (LogLevel): 过滤的最低日志级别。

        Returns:
            LogWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = LogWidget().filter_by_level(LogLevel.ERROR) # 只显示ERROR和CRITICAL日志
        """
        self._filter_level = level
        return self

    def show_timestamp(self, show: bool = True) -> "LogWidget":
        """设置是否显示日志条目的时间戳。

        Args:
            show (bool): 是否显示时间戳，默认为True。

        Returns:
            LogWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = LogWidget().show_timestamp(False) # 隐藏时间戳
        """
        self._show_timestamp = show
        return self

    def show_level(self, show: bool = True) -> "LogWidget":
        """设置是否显示日志条目的级别。

        Args:
            show (bool): 是否显示级别，默认为True。

        Returns:
            LogWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = LogWidget().show_level(False) # 隐藏级别
        """
        self._show_level = show
        return self

    def show_source(self, show: bool = True) -> "LogWidget":
        """设置是否显示日志条目的来源信息（模块、函数、行号）。

        Args:
            show (bool): 是否显示来源信息，默认为True。

        Returns:
            LogWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = LogWidget().show_source(False) # 隐藏来源信息
        """
        self._show_source = show
        return self

    def add_log_entry(
        self,
        message: str,
        level: LogLevel = LogLevel.INFO,
        timestamp: datetime | None = None,
        module: str | None = None,
        function: str | None = None,
        line_number: int | None = None,
    ) -> "LogWidget":
        """手动添加一个日志条目。

        此方法允许直接创建 `LogEntry` 对象并添加到日志列表中，
        适用于非Loguru格式的日志或需要自定义日志内容的情况。

        Args:
            message (str): 日志消息内容。
            level (LogLevel): 日志级别，默认为 `LogLevel.INFO`。
            timestamp (Optional[datetime]): 日志记录的时间戳，默认为当前时间。
            module (Optional[str]): 记录日志的模块名称。
            function (Optional[str]): 记录日志的函数名称。
            line_number (Optional[int]): 记录日志的代码行号。

        Returns:
            LogWidget: 返回self以支持链式调用。

        Examples:
            >>> widget = LogWidget().add_log_entry("自定义消息", level=LogLevel.DEBUG)
        """
        entry = LogEntry(message, level, timestamp, module, function, line_number)
        self._logs.append(entry)
        return self

    def add_log_parser(self, log_parser: LogParser) -> "LogWidget":
        """添加自定义日志解析器到解析器链中。

        新添加的解析器会插入到PlainTextParser之前，
        确保PlainTextParser始终作为兜底解析器。

        Args:
            log_parser (LogParser): 要添加的日志解析器实例。

        Returns:
            LogWidget: 返回self以支持链式调用。

        Examples:
            >>> custom_parser = MyCustomLogParser()
            >>> widget = LogWidget().add_log_parser(custom_parser)
        """
        # 移除PlainTextParser（如果存在）
        plain_text_parser = None
        for i, parser in enumerate(self._log_parsers):
            if isinstance(parser, PlainTextParser):
                plain_text_parser = self._log_parsers.pop(i)
                break

        # 添加新解析器
        self._log_parsers.append(log_parser)

        # 重新添加PlainTextParser作为兜底解析器
        if plain_text_parser:
            self._log_parsers.append(plain_text_parser)

        return self

    def _parse_single_log(self, log_line: str) -> Optional["LogEntry"]:
        """使用解析器链解析单条日志。

        按照解析器链的顺序尝试解析日志行，
        返回第一个成功解析的结果。

        Args:
            log_line (str): 待解析的日志行。

        Returns:
            Optional[LogEntry]: 解析成功返回LogEntry对象，失败返回None。
        """
        if not log_line or not log_line.strip():
            return None

        # 按顺序尝试每个解析器
        for parser in self._log_parsers:
            try:
                if parser.can_parse(log_line):
                    result = parser.parse(log_line)
                    if result is not None:
                        return result
            except Exception as e:
                # 记录解析器异常，但继续尝试下一个解析器
                self._logger.debug(f"解析器 {parser.parser_name} 解析失败: {e}")
                continue

        return None

    def _get_level_color(self, level: LogLevel) -> str:
        """获取日志级别颜色 - 深色主题适配"""
        colors = {
            LogLevel.DEBUG: "#888888",
            LogLevel.INFO: "#4fc3f7",
            LogLevel.WARNING: "#ffb74d",
            LogLevel.ERROR: "#f44336",
            LogLevel.CRITICAL: "#d32f2f",
        }
        return colors.get(level, "#ffffff")

    def _get_level_background(self, level: LogLevel) -> str:
        """获取日志级别背景色"""
        backgrounds = {
            LogLevel.DEBUG: "#f8f8f8",
            LogLevel.INFO: "#e6f3ff",
            LogLevel.WARNING: "#fff4e6",
            LogLevel.ERROR: "#ffebee",
            LogLevel.CRITICAL: "#ffebee",
        }
        return backgrounds.get(level, "#ffffff")

    @property
    def logs(self) -> list[LogEntry]:
        """获取过滤后的日志列表。

        如果设置了 `filter_level`，则只返回符合过滤条件的日志。

        Returns:
            List[LogEntry]: 过滤后的日志条目列表。
        """
        if self._filter_level:
            level_order = {
                LogLevel.DEBUG: 0,
                LogLevel.INFO: 1,
                LogLevel.WARNING: 2,
                LogLevel.ERROR: 3,
                LogLevel.CRITICAL: 4,
            }
            min_level = level_order[self._filter_level]
            return [log for log in self._logs if level_order[log.level] >= min_level]
        return self._logs

    @property
    def title(self) -> str | None:
        """获取日志组件的标题。

        Returns:
            Optional[str]: 标题文本或None。
        """
        return self._title

    @property
    def max_height(self) -> str:
        """获取日志显示区域的最大高度。

        Returns:
            str: 最大高度的CSS值。
        """
        return self._max_height

    def _get_template_name(self) -> str:
        return "log_output.html"

    def get_template_context(self) -> dict[str, Any]:
        """获取模板渲染所需的上下文数据"""
        if not self._logs:
            return {}

        # 深色背景的容器样式
        container_style = f"""
            background: #1e1e1e;
            border: 1px solid #333333;
            border-radius: 4px;
            margin: 16px 0;
            padding: 16px;
            max-height: {self._max_height};
            overflow-x: auto;
            overflow-y: auto;
            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
            font-size: 13px;
            line-height: 1.4;
            color: #ffffff;
        """

        title_style = (
            "margin: 0 0 16px 0; font-size: 16px; font-weight: 600; color: #ffffff;"
        )

        entry_style = """
            padding: 4px 0;
            margin: 2px 0;
            white-space: nowrap;
            color: #ffffff;
        """

        timestamp_style = "color: #888888; margin-right: 8px;"
        source_style = "color: #cccccc; margin-right: 8px;"
        message_style = "color: #ffffff;"

        # 处理日志条目
        logs_data = []
        for log_entry in self.logs:
            level_color = self._get_level_color(log_entry.level)
            level_style = f"color: {level_color}; font-weight: bold; margin-right: 8px;"

            # 构建来源信息
            source = None
            if self._show_source and (log_entry.module or log_entry.function):
                parts = []
                if log_entry.module:
                    parts.append(log_entry.module)
                if log_entry.function:
                    parts.append(log_entry.function)
                if log_entry.line_number:
                    parts.append(str(log_entry.line_number))
                source = ":".join(parts) if parts else None

            logs_data.append(
                {
                    "timestamp_str": log_entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                    "level": log_entry.level.value,
                    "level_style": level_style,
                    "source": source,
                    "message": log_entry.message,
                }
            )

        return {
            "logs": logs_data,
            "title": self._title,
            "container_style": container_style,
            "title_style": title_style,
            "entry_style": entry_style,
            "timestamp_style": timestamp_style,
            "source_style": source_style,
            "message_style": message_style,
            "show_timestamp": self._show_timestamp,
            "show_level": self._show_level,
            "show_source": self._show_source,
        }
