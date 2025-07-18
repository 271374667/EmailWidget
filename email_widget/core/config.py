"""Configuration management module

This module provides configuration management functionality for the EmailWidget library, using directly declared constants.
"""

from pathlib import Path
from typing import Any

# Configuration constant declarations
OUTPUT_DIR: Path = Path(".")
DEFAULT_TITLE: str = "EmailWidget Email Report"
CHARSET: str = "UTF-8"
LANG: str = "en-US"

# Style constants
PRIMARY_COLOR: str = "#0078d4"
FONT_FAMILY: str = "'Segoe UI', Tahoma, Arial, sans-serif"
MAX_WIDTH: str = "800px"
BACKGROUND_COLOR: str = "#ffffff"
BASE_FONT_SIZE: str = "14px"
LINE_HEIGHT: str = "1.5"

# Component constants
TABLE_STRIPED: bool = True
LOG_MAX_HEIGHT: str = "400px"
COLUMN_DEFAULT_GAP: str = "20px"

# Text Widget constants
TEXT_DEFAULT_COLOR: str = "#323130"
TITLE_LARGE_SIZE: str = "28px"
TITLE_SMALL_SIZE: str = "20px"
BODY_SIZE: str = "14px"
CAPTION_SIZE: str = "12px"
SECTION_H2_SIZE: str = "24px"
SECTION_H3_SIZE: str = "20px"
SECTION_H4_SIZE: str = "18px"
SECTION_H5_SIZE: str = "16px"

# Chart font constants
CHINESE_FONTS: list[str] = ["SimHei", "Microsoft YaHei", "SimSun", "KaiTi", "FangSong"]
FALLBACK_FONTS: list[str] = ["DejaVu Sans", "Arial", "sans-serif"]


class EmailConfig:
    """Email configuration management class.

    This class manages all configuration options for the EmailWidget library, including email styles, Widget configurations, etc.
    Uses directly declared constants to provide configuration values.

    Examples:
        >>> config = EmailConfig()
        >>> print(config.get_primary_color())  # #0078d4
        >>> config.get_email_title()  # Returns the configured title
    """

    def __init__(self):
        """Initialize the configuration manager."""
        pass

    def get_output_dir(self) -> str:
        """Get output directory configuration.

        Returns:
            Output directory path string
        """
        return str(OUTPUT_DIR)

    def get_primary_color(self) -> str:
        """Get primary color configuration.

        Returns:
            Primary color hexadecimal value
        """
        return PRIMARY_COLOR

    def get_font_family(self) -> str:
        """Get font family configuration.

        Returns:
            CSS font family string
        """
        return FONT_FAMILY

    def get_max_width(self) -> str:
        """Get maximum width configuration.

        Returns:
            Maximum width CSS value
        """
        return MAX_WIDTH

    def get_email_title(self) -> str:
        """Get default email title.

        Returns:
            Email title string
        """
        return DEFAULT_TITLE

    def get_email_charset(self) -> str:
        """Get email charset configuration.

        Returns:
            Charset name
        """
        return CHARSET

    def get_email_lang(self) -> str:
        """Get email language configuration.

        Returns:
            Language code
        """
        return LANG

    def get_background_color(self) -> str:
        """Get background color configuration.

        Returns:
            Background color hexadecimal value
        """
        return BACKGROUND_COLOR

    def get_base_font_size(self) -> str:
        """Get base font size configuration.

        Returns:
            Font size CSS value
        """
        return BASE_FONT_SIZE

    def get_line_height(self) -> str:
        """Get line height configuration.

        Returns:
            Line height CSS value
        """
        return LINE_HEIGHT

    # Widget-related configuration
    def get_text_config(self, key: str, default: Any = None) -> Any:
        """Get text Widget configuration item.

        Args:
            key: Configuration key name
            default: Default value

        Returns:
            Configuration value
        """
        # Return corresponding constant based on key
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
        """Get chart Chinese font list.

        Returns:
            Font name list, including Chinese fonts and fallback fonts
        """
        return CHINESE_FONTS + FALLBACK_FONTS

    def get_widget_config(self, widget_type: str, key: str, default: Any = None) -> Any:
        """Get configuration item for specified Widget type.

        Args:
            widget_type: Widget type name (e.g., "text", "chart", "table")
            key: Configuration key name
            default: Default value

        Returns:
            Configuration value

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
