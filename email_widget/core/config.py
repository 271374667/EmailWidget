"""配置管理模块

这个模块提供了EmailWidget库的配置管理功能，使用直接声明的常量.
"""

from pathlib import Path
from typing import Any

# 配置常量声明
OUTPUT_DIR: Path = Path(".")
DEFAULT_TITLE: str = "EmailWidget 邮件报告"
CHARSET: str = "UTF-8"
LANG: str = "zh-CN"

# 样式常量
PRIMARY_COLOR: str = "#0078d4"
FONT_FAMILY: str = "'Segoe UI', Tahoma, Arial, sans-serif"
MAX_WIDTH: str = "800px"
BACKGROUND_COLOR: str = "#ffffff"
BASE_FONT_SIZE: str = "14px"
LINE_HEIGHT: str = "1.5"

# 组件常量
TABLE_STRIPED: bool = True
LOG_MAX_HEIGHT: str = "400px"
COLUMN_DEFAULT_GAP: str = "20px"

# 文本Widget常量
TEXT_DEFAULT_COLOR: str = "#323130"
TITLE_LARGE_SIZE: str = "28px"
TITLE_SMALL_SIZE: str = "20px"
BODY_SIZE: str = "14px"
CAPTION_SIZE: str = "12px"
SECTION_H2_SIZE: str = "24px"
SECTION_H3_SIZE: str = "20px"
SECTION_H4_SIZE: str = "18px"
SECTION_H5_SIZE: str = "16px"

# 图表字体常量
CHINESE_FONTS: list[str] = ["SimHei", "Microsoft YaHei", "SimSun", "KaiTi", "FangSong"]
FALLBACK_FONTS: list[str] = ["DejaVu Sans", "Arial", "sans-serif"]


class EmailConfig:
    """邮件配置管理类.

    这个类负责管理EmailWidget库的所有配置选项，包括邮件样式、Widget配置等.
    使用直接声明的常量提供配置值.

    Examples:
        >>> config = EmailConfig()
        >>> print(config.get_primary_color())  # #0078d4
        >>> config.get_email_title()  # 返回配置的标题
    """

    def __init__(self):
        """初始化配置管理器."""
        pass

    def get_output_dir(self) -> str:
        """获取输出目录配置.

        Returns:
            输出目录路径字符串
        """
        return str(OUTPUT_DIR)

    def get_primary_color(self) -> str:
        """获取主色调配置.

        Returns:
            主色调的十六进制颜色值
        """
        return PRIMARY_COLOR

    def get_font_family(self) -> str:
        """获取字体族配置.

        Returns:
            CSS字体族字符串
        """
        return FONT_FAMILY

    def get_max_width(self) -> str:
        """获取最大宽度配置.

        Returns:
            最大宽度的CSS值
        """
        return MAX_WIDTH

    def get_email_title(self) -> str:
        """获取邮件默认标题.

        Returns:
            邮件标题字符串
        """
        return DEFAULT_TITLE

    def get_email_charset(self) -> str:
        """获取邮件字符集配置.

        Returns:
            字符集名称
        """
        return CHARSET

    def get_email_lang(self) -> str:
        """获取邮件语言配置.

        Returns:
            语言代码
        """
        return LANG

    def get_background_color(self) -> str:
        """获取背景颜色配置.

        Returns:
            背景颜色的十六进制值
        """
        return BACKGROUND_COLOR

    def get_base_font_size(self) -> str:
        """获取基础字体大小配置.

        Returns:
            字体大小的CSS值
        """
        return BASE_FONT_SIZE

    def get_line_height(self) -> str:
        """获取行高配置.

        Returns:
            行高的CSS值
        """
        return LINE_HEIGHT

    # Widget相关配置
    def get_text_config(self, key: str, default: Any = None) -> Any:
        """获取文本Widget的配置项.

        Args:
            key: 配置键名
            default: 默认值

        Returns:
            配置值
        """
        # 根据key返回对应的常量
        text_config_map = {
            "default_color": TEXT_DEFAULT_COLOR,
            "title_large_size": TITLE_LARGE_SIZE,
            "title_small_size": TITLE_SMALL_SIZE,
            "body_size": BODY_SIZE,
            "caption_size": CAPTION_SIZE,
            "section_h2_size": SECTION_H2_SIZE,
            "section_h3_size": SECTION_H3_SIZE,
            "section_h4_size": SECTION_H4_SIZE,
            "section_h5_size": SECTION_H5_SIZE,
        }
        return text_config_map.get(key, default)

    def get_chart_fonts(self) -> list[str]:
        """获取图表中文字体列表.

        Returns:
            字体名称列表，包含中文字体和备用字体
        """
        return CHINESE_FONTS + FALLBACK_FONTS

    def get_widget_config(self, widget_type: str, key: str, default: Any = None) -> Any:
        """获取指定Widget类型的配置项.

        Args:
            widget_type: Widget类型名称（如 "text", "chart", "table"）
            key: 配置键名
            default: 默认值

        Returns:
            配置值

        Examples:
            >>> config = EmailConfig()
            >>> config.get_widget_config("text", "body_size", "14px")
            >>> config.get_widget_config("chart", "default_dpi", 150)
        """
        if widget_type == "text":
            return self.get_text_config(key, default)
        elif widget_type == "components":
            component_config_map = {
                "table_striped": TABLE_STRIPED,
                "log_max_height": LOG_MAX_HEIGHT,
                "column_default_gap": COLUMN_DEFAULT_GAP,
            }
            return component_config_map.get(key, default)
        return default
