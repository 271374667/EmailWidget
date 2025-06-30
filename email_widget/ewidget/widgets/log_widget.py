"""日志Widget实现"""
import re
from typing import List, Optional, Dict, Any
from datetime import datetime

from email_widget.ewidget.base import BaseWidget
from email_widget.ewidget.enums import LogLevel

class LogEntry:
    """日志条目类"""
    
    def __init__(self, 
                 message: str,
                 level: LogLevel = LogLevel.INFO,
                 timestamp: Optional[datetime] = None,
                 module: Optional[str] = None,
                 function: Optional[str] = None,
                 line_number: Optional[int] = None):
        self.message = message
        self.level = level
        self.timestamp = timestamp or datetime.now()
        self.module = module or ""
        self.function = function or ""
        self.line_number = line_number

class LogWidget(BaseWidget):
    """日志Widget类"""
    
    LOG_PATTERN = re.compile(
        r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}) \| '
        r'(DEBUG|INFO|WARNING|ERROR|CRITICAL)\s+\| '
        r'([^:]+):([^:]+):(\d+) - (.+)'
    )
    
    def __init__(self, widget_id: Optional[str] = None):
        super().__init__(widget_id)
        self._logs: List[LogEntry] = []
        self._title: Optional[str] = None
        self._max_height: str = "400px"
        self._show_timestamp: bool = True
        self._show_level: bool = True
        self._show_source: bool = True
        self._filter_level: Optional[LogLevel] = None
        self._background_color: str = "#faf9f8"
        self._border_color: str = "#e1dfdd"
    
    def set_log_level(self, level: LogLevel) -> 'LogWidget':
        """设置日志过滤级别"""
        self._filter_level = level
        return self
    
    def append_log(self, log: str) -> 'LogWidget':
        """追加单条日志"""
        parsed_entry = self._parse_single_log(log)
        if parsed_entry:
            self._logs.append(parsed_entry)
        return self
    
    def set_logs(self, logs: List[str]) -> 'LogWidget':
        """设置日志列表"""
        self._logs.clear()
        for log in logs:
            self.append_log(log)
        return self
    
    def clear(self) -> 'LogWidget':
        """清空日志"""
        self._logs.clear()
        return self
    
    def set_title(self, title: str) -> 'LogWidget':
        """设置标题"""
        self._title = title
        return self
    
    def set_max_height(self, height: str) -> 'LogWidget':
        """设置最大高度"""
        self._max_height = height
        return self
    
    def set_log_level(self, level: LogLevel) -> 'LogWidget':
        """设置日志级别过滤"""
        self._filter_level = level
        return self
    
    def append_log(self, log: str) -> 'LogWidget':
        """添加单条日志"""
        log_entry = self._parse_single_log(log)
        if log_entry:
            self._logs.append(log_entry)
        return self
    
    def set_logs(self, logs: list[str]) -> 'LogWidget':
        """设置日志列表"""
        self._logs.clear()
        for log_line in logs:
            self.append_log(log_line)
        return self
    
    def clear(self) -> 'LogWidget':
        """清空日志"""
        self._logs.clear()
        return self
    
    def filter_by_level(self, level: LogLevel) -> 'LogWidget':
        """按级别过滤日志"""
        self._filter_level = level
        return self
    
    def show_timestamp(self, show: bool = True) -> 'LogWidget':
        """设置是否显示时间戳"""
        self._show_timestamp = show
        return self
    
    def show_level(self, show: bool = True) -> 'LogWidget':
        """设置是否显示日志级别"""
        self._show_level = show
        return self
    
    def show_source(self, show: bool = True) -> 'LogWidget':
        """设置是否显示来源信息"""
        self._show_source = show
        return self
    
    def add_log_entry(self, 
                      message: str,
                      level: LogLevel = LogLevel.INFO,
                      timestamp: Optional[datetime] = None,
                      module: Optional[str] = None,
                      function: Optional[str] = None,
                      line_number: Optional[int] = None) -> 'LogWidget':
        """添加日志条目"""
        entry = LogEntry(message, level, timestamp, module, function, line_number)
        self._logs.append(entry)
        return self
    
    def _parse_single_log(self, log_line: str) -> Optional[LogEntry]:
        """解析单条loguru日志"""
        match = self.LOG_PATTERN.match(log_line.strip())
        if match:
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
                line_number=int(line_num) if line_num.isdigit() else None
            )
        return None
    
    def _get_level_color(self, level: LogLevel) -> str:
        """获取日志级别颜色 - 深色主题适配"""
        colors = {
            LogLevel.DEBUG: "#888888",
            LogLevel.INFO: "#4fc3f7",
            LogLevel.WARNING: "#ffb74d",
            LogLevel.ERROR: "#f44336",
            LogLevel.CRITICAL: "#d32f2f"
        }
        return colors.get(level, "#ffffff")
    
    def _get_level_background(self, level: LogLevel) -> str:
        """获取日志级别背景色"""
        backgrounds = {
            LogLevel.DEBUG: "#f8f8f8",
            LogLevel.INFO: "#e6f3ff",
            LogLevel.WARNING: "#fff4e6",
            LogLevel.ERROR: "#ffebee",
            LogLevel.CRITICAL: "#ffebee"
        }
        return backgrounds.get(level, "#ffffff")
    
    @property
    def logs(self) -> List[LogEntry]:
        """获取过滤后的日志列表"""
        if self._filter_level:
            level_order = {
                LogLevel.DEBUG: 0,
                LogLevel.INFO: 1,
                LogLevel.WARNING: 2,
                LogLevel.ERROR: 3,
                LogLevel.CRITICAL: 4
            }
            min_level = level_order[self._filter_level]
            return [log for log in self._logs if level_order[log.level] >= min_level]
        return self._logs
    
    @property
    def title(self) -> Optional[str]:
        """获取标题"""
        return self._title
    
    @property
    def max_height(self) -> str:
        """获取最大高度"""
        return self._max_height
    
    def _get_template_name(self) -> str:
        return "log_output.html"
    
    def render_html(self) -> str:
        """渲染为HTML"""
        if not self._logs:
            return ""
        
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
        
        html = f'<div style="{container_style}">'
        
        # 标题
        if self._title:
            html += f'<h3 style="margin: 0 0 16px 0; font-size: 16px; font-weight: 600; color: #ffffff;">{self._title}</h3>'
        
        # 日志条目 - 不换行，使用横向滚动
        for log_entry in self.logs:
            level_color = self._get_level_color(log_entry.level)
            
            entry_style = f"""
                padding: 4px 0;
                margin: 2px 0;
                white-space: nowrap;
                color: #ffffff;
            """
            
            html += f'<div style="{entry_style}">'
            
            # 时间戳
            if self._show_timestamp:
                timestamp_str = log_entry.timestamp.strftime("%Y-%m-%d %H:%M:%S")
                html += f'<span style="color: #888888; margin-right: 8px;">{timestamp_str}</span>'
            
            # 日志级别
            if self._show_level:
                html += f'<span style="color: {level_color}; font-weight: bold; margin-right: 8px;">[{log_entry.level.value}]</span>'
            
            # 来源信息
            if self._show_source and (log_entry.module or log_entry.function):
                source = f"{log_entry.module}:{log_entry.function}"
                if log_entry.line_number:
                    source += f":{log_entry.line_number}"
                html += f'<span style="color: #cccccc; margin-right: 8px;">({source})</span>'
            
            # 消息内容
            html += f'<span style="color: #ffffff;">{log_entry.message}</span>'
            html += '</div>'
        
        html += '</div>'
        return html 