"""LogWidget组件的完整测试套件

该测试文件确保LogWidget及其相关类的100%代码覆盖率，
包括所有新增的策略模式功能和向后兼容性。
"""

from datetime import datetime
from typing import Optional
from unittest.mock import Mock

import pytest

from email_widget.core.enums import LogLevel
from email_widget.widgets.log_widget import (
    LogEntry,
    LogParser,
    LoGuruLogParser,
    LogWidget,
    PlainTextParser,
    StandardLoggingParser,
    TimestampLogParser,
)


class TestLogEntry:
    """测试LogEntry数据结构"""

    def test_init_with_all_parameters(self):
        """测试使用所有参数初始化LogEntry"""
        timestamp = datetime(2024, 7, 7, 10, 30, 0)
        entry = LogEntry(
            message="测试消息",
            level=LogLevel.ERROR,
            timestamp=timestamp,
            module="test_module",
            function="test_function",
            line_number=123,
        )

        assert entry.message == "测试消息"
        assert entry.level == LogLevel.ERROR
        assert entry.timestamp == timestamp
        assert entry.module == "test_module"
        assert entry.function == "test_function"
        assert entry.line_number == 123

    def test_init_with_minimal_parameters(self):
        """测试使用最少参数初始化LogEntry"""
        entry = LogEntry("最小消息")

        assert entry.message == "最小消息"
        assert entry.level == LogLevel.INFO  # 默认值
        assert isinstance(entry.timestamp, datetime)  # 自动生成
        assert entry.module == ""  # 默认空字符串
        assert entry.function == ""  # 默认空字符串
        assert entry.line_number is None

    def test_init_with_none_timestamp(self):
        """测试timestamp为None时自动生成当前时间"""
        entry = LogEntry("消息", timestamp=None)
        assert isinstance(entry.timestamp, datetime)


class TestLoGuruLogParser:
    """测试LoGuruLogParser解析器"""

    def setup_method(self):
        self.parser = LoGuruLogParser()

    def test_parser_name(self):
        """测试解析器名称"""
        assert self.parser.parser_name == "LoGuruLogParser"

    def test_can_parse_valid_loguru_format(self):
        """测试能识别有效的Loguru格式"""
        log_line = (
            "2024-07-07 10:30:00.123 | INFO | my_app.main:run:45 - Application started"
        )
        assert self.parser.can_parse(log_line) is True

    def test_can_parse_invalid_format(self):
        """测试不能识别无效格式"""
        assert self.parser.can_parse("Invalid log format") is False
        assert self.parser.can_parse("INFO: Simple log") is False
        assert self.parser.can_parse("") is False

    def test_parse_valid_loguru_log(self):
        """测试解析有效的Loguru日志"""
        log_line = "2024-07-07 10:30:00.123 | WARNING | my_app.database:connect:88 - Connection slow"
        result = self.parser.parse(log_line)

        assert result is not None
        assert isinstance(result, LogEntry)
        assert result.message == "Connection slow"
        assert result.level == LogLevel.WARNING
        assert result.timestamp == datetime(2024, 7, 7, 10, 30, 0, 123000)
        assert result.module == "my_app.database"
        assert result.function == "connect"
        assert result.line_number == 88

    def test_parse_with_invalid_timestamp(self):
        """测试解析包含无效时间戳的日志"""
        log_line = "invalid-timestamp | INFO | module:func:123 - Message"
        result = self.parser.parse(log_line)
        # 由于正则不匹配，应该返回None
        assert result is None

    def test_parse_with_invalid_level(self):
        """测试解析包含无效日志级别的日志"""
        log_line = "2024-07-07 10:30:00.123 | INVALID_LEVEL | module:func:123 - Message"
        result = self.parser.parse(log_line)
        # 正则不匹配有效级别，返回None
        assert result is None

    def test_parse_with_non_numeric_line_number(self):
        """测试解析包含非数字行号的日志"""
        log_line = "2024-07-07 10:30:00.123 | INFO | module:func:abc - Message"
        result = self.parser.parse(log_line)
        # 正则要求数字行号，所以这个不会匹配
        assert result is None

    def test_parse_non_matching_format(self):
        """测试解析不匹配格式返回None"""
        assert self.parser.parse("Random text") is None
        assert self.parser.parse("") is None

    def test_parse_with_whitespace(self):
        """测试解析包含前后空白的日志"""
        log_line = "  2024-07-07 10:30:00.123 | INFO | module:func:123 - Message  "
        result = self.parser.parse(log_line)
        assert result is not None
        assert result.message == "Message"


class TestStandardLoggingParser:
    """测试StandardLoggingParser解析器"""

    def setup_method(self):
        self.parser = StandardLoggingParser()

    def test_parser_name(self):
        """测试解析器名称"""
        assert self.parser.parser_name == "StandardLoggingParser"

    def test_can_parse_valid_standard_format(self):
        """测试能识别有效的标准logging格式"""
        assert self.parser.can_parse("WARNING:root:hello world") is True
        assert self.parser.can_parse("ERROR:my_module:Connection failed") is True
        assert self.parser.can_parse("INFO::Empty logger name") is True

    def test_can_parse_invalid_format(self):
        """测试不能识别无效格式"""
        assert self.parser.can_parse("Invalid format") is False
        assert self.parser.can_parse("2024-07-07 | INFO | message") is False
        assert self.parser.can_parse("") is False

    def test_parse_valid_standard_log(self):
        """测试解析有效的标准logging日志"""
        log_line = "WARNING:root:hello world"
        result = self.parser.parse(log_line)

        assert result is not None
        assert isinstance(result, LogEntry)
        assert result.message == "hello world"
        assert result.level == LogLevel.WARNING
        assert result.module == "root"
        assert isinstance(result.timestamp, datetime)

    def test_parse_with_empty_logger_name(self):
        """测试解析空logger名称的日志"""
        log_line = "ERROR::Connection failed"
        result = self.parser.parse(log_line)

        assert result is not None
        assert result.message == "Connection failed"
        assert result.level == LogLevel.ERROR
        assert result.module == ""

    def test_parse_with_invalid_level(self):
        """测试解析无效级别的日志"""
        log_line = "INVALID:root:message"
        result = self.parser.parse(log_line)
        # 正则不匹配，返回None
        assert result is None

    def test_parse_non_matching_format(self):
        """测试解析不匹配格式返回None"""
        assert self.parser.parse("Random text") is None
        assert self.parser.parse("") is None


class TestTimestampLogParser:
    """测试TimestampLogParser解析器"""

    def setup_method(self):
        self.parser = TimestampLogParser()

    def test_parser_name(self):
        """测试解析器名称"""
        assert self.parser.parser_name == "TimestampLogParser"

    def test_can_parse_valid_timestamp_format(self):
        """测试能识别有效的时间戳格式"""
        assert (
            self.parser.can_parse("2025-07-07 15:24:39,055 - WARNING - hello world")
            is True
        )
        assert (
            self.parser.can_parse("2024-01-01 00:00:00,000 - ERROR - Error message")
            is True
        )

    def test_can_parse_invalid_format(self):
        """测试不能识别无效格式"""
        assert self.parser.can_parse("Invalid format") is False
        assert self.parser.can_parse("WARNING:root:message") is False
        assert self.parser.can_parse("") is False

    def test_parse_valid_timestamp_log(self):
        """测试解析有效的时间戳日志"""
        log_line = "2025-07-07 15:24:39,055 - WARNING - hello world"
        result = self.parser.parse(log_line)

        assert result is not None
        assert isinstance(result, LogEntry)
        assert result.message == "hello world"
        assert result.level == LogLevel.WARNING
        assert result.timestamp == datetime(2025, 7, 7, 15, 24, 39, 55000)

    def test_parse_with_invalid_timestamp(self):
        """测试解析无效时间戳的日志"""
        log_line = "invalid-date - WARNING - message"
        result = self.parser.parse(log_line)
        # 正则不匹配，返回None
        assert result is None

    def test_parse_with_invalid_level(self):
        """测试解析无效级别的日志"""
        log_line = "2025-07-07 15:24:39,055 - INVALID - message"
        result = self.parser.parse(log_line)
        # 正则不匹配，返回None
        assert result is None

    def test_parse_non_matching_format(self):
        """测试解析不匹配格式返回None"""
        assert self.parser.parse("Random text") is None
        assert self.parser.parse("") is None


class TestPlainTextParser:
    """测试PlainTextParser解析器"""

    def setup_method(self):
        self.parser = PlainTextParser()

    def test_parser_name(self):
        """测试解析器名称"""
        assert self.parser.parser_name == "PlainTextParser"

    def test_can_parse_always_true(self):
        """测试PlainTextParser总是返回True"""
        assert self.parser.can_parse("任何文本") is True
        assert self.parser.can_parse("") is True
        assert self.parser.can_parse("123!@#$%^&*()") is True

    def test_parse_valid_text(self):
        """测试解析有效文本"""
        text = "这是一段普通文本"
        result = self.parser.parse(text)

        assert result is not None
        assert isinstance(result, LogEntry)
        assert result.message == "> 这是一段普通文本"
        assert result.level == LogLevel.INFO
        assert isinstance(result.timestamp, datetime)

    def test_parse_empty_text(self):
        """测试解析空文本返回None"""
        assert self.parser.parse("") is None
        assert self.parser.parse("   ") is None

    def test_parse_text_with_whitespace(self):
        """测试解析包含前后空白的文本"""
        result = self.parser.parse("  文本内容  ")
        assert result is not None
        assert result.message == "> 文本内容"


class MockCustomParser(LogParser):
    """用于测试的模拟解析器"""

    def can_parse(self, log_line: str) -> bool:
        return "CUSTOM:" in log_line

    def parse(self, log_line: str) -> Optional["LogEntry"]:
        if self.can_parse(log_line):
            message = log_line.replace("CUSTOM:", "")
            return LogEntry(message, LogLevel.DEBUG)
        return None

    @property
    def parser_name(self) -> str:
        return "MockCustomParser"


class TestLogWidget:
    """测试LogWidget主类"""

    def setup_method(self):
        self.widget = LogWidget()

    def test_init_default(self):
        """测试默认初始化"""
        widget = LogWidget()
        assert len(widget._log_parsers) == 4  # 四个默认解析器
        assert isinstance(widget._log_parsers[0], LoGuruLogParser)
        assert isinstance(widget._log_parsers[1], StandardLoggingParser)
        assert isinstance(widget._log_parsers[2], TimestampLogParser)
        assert isinstance(widget._log_parsers[3], PlainTextParser)

    def test_init_with_widget_id(self):
        """测试使用自定义widget_id初始化"""
        widget = LogWidget("custom_id")
        assert widget.widget_id == "custom_id"

    def test_add_log_parser(self):
        """测试添加自定义解析器"""
        custom_parser = MockCustomParser()
        result = self.widget.add_log_parser(custom_parser)

        # 测试链式调用
        assert result is self.widget

        # 测试解析器已添加并且PlainTextParser仍在最后
        assert len(self.widget._log_parsers) == 5
        assert self.widget._log_parsers[-2] is custom_parser
        assert isinstance(self.widget._log_parsers[-1], PlainTextParser)

    def test_add_log_parser_without_plain_text(self):
        """测试在没有PlainTextParser的情况下添加解析器"""
        # 移除PlainTextParser
        self.widget._log_parsers = [
            parser
            for parser in self.widget._log_parsers
            if not isinstance(parser, PlainTextParser)
        ]

        custom_parser = MockCustomParser()
        self.widget.add_log_parser(custom_parser)

        # 应该添加解析器但不会重新添加PlainTextParser
        assert self.widget._log_parsers[-1] is custom_parser

    def test_append_log_loguru_format(self):
        """测试追加Loguru格式日志"""
        log_line = (
            "2024-07-07 10:30:00.123 | INFO | my_app.main:run:45 - Application started"
        )
        result = self.widget.append_log(log_line)

        # 测试链式调用
        assert result is self.widget

        # 测试日志已添加
        assert len(self.widget._logs) == 1
        assert self.widget._logs[0].message == "Application started"
        assert self.widget._logs[0].level == LogLevel.INFO

    def test_append_log_standard_format(self):
        """测试追加标准logging格式日志"""
        log_line = "WARNING:root:hello world"
        self.widget.append_log(log_line)

        assert len(self.widget._logs) == 1
        assert self.widget._logs[0].message == "hello world"
        assert self.widget._logs[0].level == LogLevel.WARNING

    def test_append_log_timestamp_format(self):
        """测试追加时间戳格式日志"""
        log_line = "2025-07-07 15:24:39,055 - ERROR - Connection failed"
        self.widget.append_log(log_line)

        assert len(self.widget._logs) == 1
        assert self.widget._logs[0].message == "Connection failed"
        assert self.widget._logs[0].level == LogLevel.ERROR

    def test_append_log_plain_text(self):
        """测试追加纯文本日志"""
        log_line = "这是一段普通文本"
        self.widget.append_log(log_line)

        assert len(self.widget._logs) == 1
        assert self.widget._logs[0].message == "> 这是一段普通文本"
        assert self.widget._logs[0].level == LogLevel.INFO

    def test_append_log_empty_string(self):
        """测试追加空字符串"""
        self.widget.append_log("")
        assert len(self.widget._logs) == 0

    def test_append_log_with_custom_parser(self):
        """测试使用自定义解析器追加日志"""
        custom_parser = MockCustomParser()
        self.widget.add_log_parser(custom_parser)

        self.widget.append_log("CUSTOM:自定义消息")

        assert len(self.widget._logs) == 1
        assert self.widget._logs[0].message == "自定义消息"
        assert self.widget._logs[0].level == LogLevel.DEBUG

    def test_set_logs(self):
        """测试设置日志列表"""
        logs = [
            "2024-07-07 10:30:00.123 | INFO | app:main:45 - Started",
            "WARNING:root:Warning message",
            "Plain text message",
        ]
        result = self.widget.set_logs(logs)

        # 测试链式调用
        assert result is self.widget

        # 测试日志已设置
        assert len(self.widget._logs) == 3
        assert self.widget._logs[0].message == "Started"
        assert self.widget._logs[1].message == "Warning message"
        assert self.widget._logs[2].message == "> Plain text message"

    def test_set_logs_clears_existing(self):
        """测试设置日志列表会清空现有日志"""
        # 先添加一些日志
        self.widget.append_log("Initial log")
        assert len(self.widget._logs) == 1

        # 设置新日志
        self.widget.set_logs(["New log"])
        assert len(self.widget._logs) == 1
        assert self.widget._logs[0].message == "> New log"

    def test_clear(self):
        """测试清空日志"""
        self.widget.append_log("Some log")
        assert len(self.widget._logs) == 1

        result = self.widget.clear()

        # 测试链式调用
        assert result is self.widget

        # 测试日志已清空
        assert len(self.widget._logs) == 0

    def test_set_title(self):
        """测试设置标题"""
        result = self.widget.set_title("测试标题")

        # 测试链式调用
        assert result is self.widget

        # 测试标题已设置
        assert self.widget._title == "测试标题"
        assert self.widget.title == "测试标题"

    def test_set_max_height(self):
        """测试设置最大高度"""
        result = self.widget.set_max_height("500px")

        # 测试链式调用
        assert result is self.widget

        # 测试高度已设置
        assert self.widget._max_height == "500px"
        assert self.widget.max_height == "500px"

    def test_filter_by_level(self):
        """测试按级别过滤"""
        result = self.widget.filter_by_level(LogLevel.WARNING)

        # 测试链式调用
        assert result is self.widget

        # 测试过滤级别已设置
        assert self.widget._filter_level == LogLevel.WARNING

    def test_set_log_level_alias(self):
        """测试set_log_level方法（filter_by_level的别名）"""
        result = self.widget.set_log_level(LogLevel.ERROR)

        # 测试链式调用
        assert result is self.widget

        # 测试过滤级别已设置
        assert self.widget._filter_level == LogLevel.ERROR

    def test_show_timestamp(self):
        """测试显示/隐藏时间戳"""
        result = self.widget.show_timestamp(False)

        # 测试链式调用
        assert result is self.widget

        # 测试设置已生效
        assert self.widget._show_timestamp is False

        # 测试默认值
        widget2 = LogWidget()
        widget2.show_timestamp()
        assert widget2._show_timestamp is True

    def test_show_level(self):
        """测试显示/隐藏级别"""
        result = self.widget.show_level(False)

        # 测试链式调用
        assert result is self.widget

        # 测试设置已生效
        assert self.widget._show_level is False

    def test_show_source(self):
        """测试显示/隐藏来源信息"""
        result = self.widget.show_source(False)

        # 测试链式调用
        assert result is self.widget

        # 测试设置已生效
        assert self.widget._show_source is False

    def test_add_log_entry(self):
        """测试手动添加日志条目"""
        timestamp = datetime(2024, 7, 7, 10, 0, 0)
        result = self.widget.add_log_entry(
            "手动添加的消息",
            level=LogLevel.DEBUG,
            timestamp=timestamp,
            module="test_module",
            function="test_func",
            line_number=42,
        )

        # 测试链式调用
        assert result is self.widget

        # 测试日志已添加
        assert len(self.widget._logs) == 1
        entry = self.widget._logs[0]
        assert entry.message == "手动添加的消息"
        assert entry.level == LogLevel.DEBUG
        assert entry.timestamp == timestamp
        assert entry.module == "test_module"
        assert entry.function == "test_func"
        assert entry.line_number == 42

    def test_add_log_entry_minimal(self):
        """测试使用最少参数手动添加日志条目"""
        self.widget.add_log_entry("简单消息")

        assert len(self.widget._logs) == 1
        entry = self.widget._logs[0]
        assert entry.message == "简单消息"
        assert entry.level == LogLevel.INFO  # 默认值

    def test_logs_property_no_filter(self):
        """测试无过滤时的logs属性"""
        # 添加不同级别的日志
        self.widget.add_log_entry("Debug", LogLevel.DEBUG)
        self.widget.add_log_entry("Info", LogLevel.INFO)
        self.widget.add_log_entry("Warning", LogLevel.WARNING)

        logs = self.widget.logs
        assert len(logs) == 3

    def test_logs_property_with_filter(self):
        """测试有过滤时的logs属性"""
        # 添加不同级别的日志
        self.widget.add_log_entry("Debug", LogLevel.DEBUG)
        self.widget.add_log_entry("Info", LogLevel.INFO)
        self.widget.add_log_entry("Warning", LogLevel.WARNING)
        self.widget.add_log_entry("Error", LogLevel.ERROR)

        # 设置过滤级别为WARNING
        self.widget.filter_by_level(LogLevel.WARNING)

        filtered_logs = self.widget.logs
        assert len(filtered_logs) == 2  # 只有WARNING和ERROR
        assert all(log.level.value in ["WARNING", "ERROR"] for log in filtered_logs)

    def test_parse_single_log_empty_string(self):
        """测试解析空字符串"""
        result = self.widget._parse_single_log("")
        assert result is None

        result = self.widget._parse_single_log("   ")
        assert result is None

    def test_parse_single_log_with_parser_exception(self):
        """测试解析器抛出异常的处理"""
        # 创建一个会抛出异常的模拟解析器
        failing_parser = Mock(spec=LogParser)
        failing_parser.can_parse.side_effect = Exception("解析器错误")
        failing_parser.parser_name = "FailingParser"

        # 添加失败的解析器
        self.widget._log_parsers.insert(0, failing_parser)

        # 解析应该继续使用其他解析器
        result = self.widget._parse_single_log("普通文本")
        assert result is not None
        assert result.message == "> 普通文本"

    def test_get_level_color(self):
        """测试获取日志级别颜色"""
        assert self.widget._get_level_color(LogLevel.DEBUG) == "#888888"
        assert self.widget._get_level_color(LogLevel.INFO) == "#4fc3f7"
        assert self.widget._get_level_color(LogLevel.WARNING) == "#ffb74d"
        assert self.widget._get_level_color(LogLevel.ERROR) == "#f44336"
        assert self.widget._get_level_color(LogLevel.CRITICAL) == "#d32f2f"

    def test_get_level_background(self):
        """测试获取日志级别背景色"""
        assert self.widget._get_level_background(LogLevel.DEBUG) == "#f8f8f8"
        assert self.widget._get_level_background(LogLevel.INFO) == "#e6f3ff"
        assert self.widget._get_level_background(LogLevel.WARNING) == "#fff4e6"
        assert self.widget._get_level_background(LogLevel.ERROR) == "#ffebee"
        assert self.widget._get_level_background(LogLevel.CRITICAL) == "#ffebee"

    def test_get_template_name(self):
        """测试获取模板名称"""
        assert self.widget._get_template_name() == "log_output.html"

    def test_get_template_context_empty_logs(self):
        """测试空日志时的模板上下文"""
        context = self.widget.get_template_context()
        assert context == {}

    def test_get_template_context_with_logs(self):
        """测试有日志时的模板上下文"""
        # 添加一条Loguru格式的日志
        self.widget.append_log(
            "2024-07-07 10:30:00.123 | WARNING | module:func:123 - Test message"
        )
        self.widget.set_title("测试标题")

        context = self.widget.get_template_context()

        # 验证基本结构
        assert "logs" in context
        assert "title" in context
        assert "container_style" in context
        assert context["title"] == "测试标题"

        # 验证日志数据
        logs_data = context["logs"]
        assert len(logs_data) == 1
        log_data = logs_data[0]
        assert log_data["message"] == "Test message"
        assert log_data["level"] == "WARNING"
        assert log_data["source"] == "module:func:123"

        # 验证显示标志
        assert context["show_timestamp"] is True
        assert context["show_level"] is True
        assert context["show_source"] is True

    def test_get_template_context_hidden_fields(self):
        """测试隐藏字段时的模板上下文"""
        self.widget.append_log("WARNING:root:Test message")
        self.widget.show_timestamp(False).show_level(False).show_source(False)

        context = self.widget.get_template_context()

        assert context["show_timestamp"] is False
        assert context["show_level"] is False
        assert context["show_source"] is False

    def test_get_template_context_without_source_info(self):
        """测试没有来源信息的日志模板上下文"""
        self.widget.append_log(
            "WARNING:root:Test message"
        )  # 标准格式，无函数和行号信息

        context = self.widget.get_template_context()
        logs_data = context["logs"]
        log_data = logs_data[0]

        # 标准logging格式只有模块名，没有函数和行号
        assert log_data["source"] == "root"  # 只有模块名


class TestBackwardCompatibility:
    """测试向后兼容性"""

    def test_existing_loguru_parsing_still_works(self):
        """测试现有的Loguru解析功能仍然正常工作"""
        widget = LogWidget()

        # 使用原有的Loguru格式
        log_messages = [
            "2024-07-07 10:30:00.123 | INFO | my_app.main:run:45 - Application started successfully.",
            "2024-07-07 10:31:15.456 | WARNING | my_app.database:connect:88 - Connection is slow.",
            "2024-07-07 10:32:05.789 | ERROR | my_app.api:request:152 - Failed to fetch data from API.",
        ]

        widget.set_logs(log_messages)

        # 验证解析结果与原有行为一致
        assert len(widget.logs) == 3
        assert widget.logs[0].level == LogLevel.INFO
        assert widget.logs[0].message == "Application started successfully."
        assert widget.logs[1].level == LogLevel.WARNING
        assert widget.logs[2].level == LogLevel.ERROR

    def test_all_existing_methods_still_work(self):
        """测试所有现有方法仍然正常工作"""
        widget = LogWidget()

        # 测试所有现有的链式调用方法
        result = (
            widget.set_title("测试日志")
            .set_max_height("300px")
            .filter_by_level(LogLevel.WARNING)
            .show_timestamp(True)
            .show_level(True)
            .show_source(False)
            .add_log_entry("测试消息", LogLevel.INFO)
            .append_log(
                "2024-07-07 10:30:00.123 | WARNING | app:main:45 - Warning message"
            )
            .clear()
        )

        # 验证链式调用返回widget本身
        assert result is widget

        # 验证clear方法正常工作
        assert len(widget.logs) == 0


class TestEdgeCases:
    """测试边界情况和异常处理"""

    def test_multiple_same_format_parsers(self):
        """测试添加多个相同格式的解析器"""
        widget = LogWidget()

        # 添加另一个Loguru解析器
        widget.add_log_parser(LoGuruLogParser())

        # 应该使用第一个匹配的解析器
        widget.append_log("2024-07-07 10:30:00.123 | INFO | app:main:45 - Test message")
        assert len(widget.logs) == 1

    def test_parser_order_matters(self):
        """测试解析器顺序的重要性"""
        widget = LogWidget()

        # 清空默认解析器，手动控制顺序
        widget._log_parsers.clear()
        widget._log_parsers.append(PlainTextParser())  # 先添加PlainText
        widget._log_parsers.append(LoGuruLogParser())  # 后添加Loguru

        # PlainText解析器会先匹配，因为它总是返回True
        widget.append_log("2024-07-07 10:30:00.123 | INFO | app:main:45 - Test message")

        # 应该被PlainText解析器处理
        assert widget.logs[0].message.startswith(">")

    def test_very_long_log_message(self):
        """测试非常长的日志消息"""
        long_message = "X" * 10000
        log_line = f"INFO:root:{long_message}"

        widget = LogWidget()
        widget.append_log(log_line)

        assert len(widget.logs) == 1
        assert widget.logs[0].message == long_message

    def test_unicode_and_special_characters(self):
        """测试Unicode和特殊字符"""
        special_messages = [
            "INFO:测试:这是中文消息 🚀",
            "WARNING:тест:Русский текст",
            "ERROR:テスト:日本語のメッセージ",
            "DEBUG:root:Special chars: !@#$%^&*()",
        ]

        widget = LogWidget()
        for msg in special_messages:
            widget.append_log(msg)

        assert len(widget.logs) == 4

        # 验证消息内容正确解析
        expected_messages = [
            "这是中文消息 🚀",
            "Русский текст",
            "日本語のメッセージ",
            "Special chars: !@#$%^&*()",
        ]

        for i, log in enumerate(widget.logs):
            assert log.message == expected_messages[i]


if __name__ == "__main__":
    pytest.main(
        [
            __file__,
            "-v",
            "--cov=email_widget.widgets.log_widget",
            "--cov-report=term-missing",
        ]
    )
