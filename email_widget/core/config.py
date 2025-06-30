"""配置管理模块

这个模块提供了EmailWidget库的配置管理功能，支持从TOML文件加载配置。
"""
from pathlib import Path
from typing import Dict, Any, Optional, List
import tomli
from contextlib import suppress

class EmailConfig:
    """邮件配置管理类。
    
    这个类负责管理EmailWidget库的所有配置选项，包括邮件样式、Widget配置等。
    支持从TOML配置文件加载用户自定义配置，并与默认配置合并。
    
    配置采用分层结构，主要包含以下部分：
    - email: 邮件基本配置（标题、字符集等）
    - style: 样式配置（颜色、字体、布局等）
    - components: 组件配置
    - widgets: 各个Widget的专用配置
    
    Attributes:
        DEFAULT_CONFIG: 默认配置字典
        _config: 当前生效的配置字典
        
    Examples:
        >>> # 使用默认配置
        >>> config = EmailConfig()
        >>> print(config.get_primary_color())  # #0078d4
        
        >>> # 从文件加载配置
        >>> config = EmailConfig("my_config.toml")
        >>> config.get_email_title()  # 返回配置的标题
        
        >>> # 获取嵌套配置
        >>> font_size = config.get("widgets.text.body_size", "14px")
    """
    
    DEFAULT_CONFIG = {
        "email": {
            "output_dir": ".",
            "default_title": "EmailWidget 邮件报告",
            "charset": "UTF-8",
            "lang": "zh-CN"
        },
        "style": {
            "primary_color": "#0078d4",
            "font_family": "'Segoe UI', Tahoma, Arial, sans-serif",
            "max_width": "800px",
            "background_color": "#ffffff",
            "base_font_size": "14px",
            "line_height": "1.5"
        },
        "components": {
            "table_striped": True,
            "log_max_height": "400px",
            "column_default_gap": "20px"
        },
        "widgets": {
            "text": {
                "default_color": "#323130",
                "title_large_size": "28px",
                "title_small_size": "20px",
                "body_size": "14px",
                "caption_size": "12px",
                "section_h2_size": "24px",
                "section_h3_size": "20px",
                "section_h4_size": "18px",
                "section_h5_size": "16px",
            },
            "chart": {
                "fonts": {
                    "chinese_fonts": ["SimHei", "Microsoft YaHei", "SimSun", "KaiTi", "FangSong"],
                    "fallback_fonts": ["DejaVu Sans", "Arial", "sans-serif"]
                }
            }
        }
    }
    
    def __init__(self, config_path: Optional[str] = None):
        """初始化配置管理器。
        
        Args:
            config_path: 可选的配置文件路径。如果不提供，只使用默认配置和
                        同目录下的config.toml文件（如果存在）
        """
        self._config = self.DEFAULT_CONFIG.copy()
        # 尝试加载默认配置文件
        default_config_path = Path(__file__).parent / "config.toml"
        if default_config_path.exists():
            self._load_config(str(default_config_path))
        # 如果指定了配置文件路径，也加载它
        if config_path:
            self._load_config(config_path)
    
    def _load_config(self, config_path: str) -> None:
        """从TOML文件加载配置。
        
        Args:
            config_path: 配置文件路径
            
        Note:
            如果文件不存在或解析失败，会静默忽略错误，使用默认配置
        """
        config_file = Path(config_path)
        if config_file.exists():
            with suppress(Exception):
                with open(config_file, 'rb') as f:
                    user_config = tomli.load(f)
                    self._merge_config(user_config)
    
    def _merge_config(self, user_config: Dict[str, Any]) -> None:
        """将用户配置合并到默认配置中。
        
        Args:
            user_config: 用户配置字典
        """
        for section, values in user_config.items():
            if section in self._config and isinstance(values, dict):
                self._config[section].update(values)
            else:
                self._config[section] = values
    
    def get(self, key: str, default: Any = None) -> Any:
        """获取配置值。
        
        支持使用点号分隔的键名访问嵌套配置，如 "widgets.text.body_size"
        
        Args:
            key: 配置键名，支持点号分隔的嵌套键
            default: 如果键不存在时返回的默认值
            
        Returns:
            配置值，如果键不存在则返回默认值
            
        Examples:
            >>> config = EmailConfig()
            >>> config.get("email.charset")  # "UTF-8"
            >>> config.get("widgets.text.body_size")  # "14px"
            >>> config.get("nonexistent.key", "fallback")  # "fallback"
        """
        keys = key.split('.')
        value = self._config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def get_output_dir(self) -> str:
        """获取输出目录配置。
        
        Returns:
            输出目录路径字符串
        """
        return self.get("email.output_dir", ".")
    
    def get_primary_color(self) -> str:
        """获取主色调配置。
        
        Returns:
            主色调的十六进制颜色值
        """
        return self.get("style.primary_color", "#0078d4")
    
    def get_font_family(self) -> str:
        """获取字体族配置。
        
        Returns:
            CSS字体族字符串
        """
        return self.get("style.font_family", "'Segoe UI', Tahoma, Arial, sans-serif")
    
    def get_max_width(self) -> str:
        """获取最大宽度配置。
        
        Returns:
            最大宽度的CSS值
        """
        return self.get("style.max_width", "800px")
    
    def get_email_title(self) -> str:
        """获取邮件默认标题。
        
        Returns:
            邮件标题字符串
        """
        return self.get("email.default_title", "EWidget 邮件报告")
    
    def get_email_charset(self) -> str:
        """获取邮件字符集配置。
        
        Returns:
            字符集名称
        """
        return self.get("email.charset", "UTF-8")
    
    def get_email_lang(self) -> str:
        """获取邮件语言配置。
        
        Returns:
            语言代码
        """
        return self.get("email.lang", "zh-CN")
    
    def get_background_color(self) -> str:
        """获取背景颜色配置。
        
        Returns:
            背景颜色的十六进制值
        """
        return self.get("style.background_color", "#ffffff")
    
    def get_base_font_size(self) -> str:
        """获取基础字体大小配置。
        
        Returns:
            字体大小的CSS值
        """
        return self.get("style.base_font_size", "14px")
    
    def get_line_height(self) -> str:
        """获取行高配置。
        
        Returns:
            行高的CSS值
        """
        return self.get("style.line_height", "1.5")
    
    # Widget相关配置
    def get_text_config(self, key: str, default: Any = None) -> Any:
        """获取文本Widget的配置项。
        
        Args:
            key: 配置键名
            default: 默认值
            
        Returns:
            配置值
        """
        return self.get(f"widgets.text.{key}", default)
    
    def get_chart_fonts(self) -> List[str]:
        """获取图表中文字体列表。
        
        Returns:
            字体名称列表，包含中文字体和备用字体
        """
        chinese_fonts = self.get("widgets.chart.fonts.chinese_fonts", ["SimHei", "Microsoft YaHei"])
        fallback_fonts = self.get("widgets.chart.fonts.fallback_fonts", ["DejaVu Sans", "Arial"])
        return chinese_fonts + fallback_fonts
    
    def get_widget_config(self, widget_type: str, key: str, default: Any = None) -> Any:
        """获取指定Widget类型的配置项。
        
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
        return self.get(f"widgets.{widget_type}.{key}", default) 