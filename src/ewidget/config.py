"""配置管理模块"""
from pathlib import Path
from typing import Dict, Any, Optional, List
import tomli
from contextlib import suppress

class EmailConfig:
    """邮件配置管理类"""
    
    DEFAULT_CONFIG = {
        "email": {
            "output_dir": ".",
            "default_template_dir": "src/ewidget/templates",
            "default_title": "EWidget 邮件报告",
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
                "section_h5_size": "16px"
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
        self._config = self.DEFAULT_CONFIG.copy()
        # 尝试加载默认配置文件
        default_config_path = Path(__file__).parent / "config.toml"
        if default_config_path.exists():
            self._load_config(str(default_config_path))
        # 如果指定了配置文件路径，也加载它
        if config_path:
            self._load_config(config_path)
    
    def _load_config(self, config_path: str) -> None:
        """加载配置文件"""
        config_file = Path(config_path)
        if config_file.exists():
            with suppress(Exception):
                with open(config_file, 'rb') as f:
                    user_config = tomli.load(f)
                    self._merge_config(user_config)
    
    def _merge_config(self, user_config: Dict[str, Any]) -> None:
        """合并用户配置"""
        for section, values in user_config.items():
            if section in self._config and isinstance(values, dict):
                self._config[section].update(values)
            else:
                self._config[section] = values
    
    def get(self, key: str, default: Any = None) -> Any:
        """获取配置值"""
        keys = key.split('.')
        value = self._config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def get_output_dir(self) -> str:
        """获取输出目录"""
        return self.get("email.output_dir", ".")
    
    def get_template_dir(self) -> str:
        """获取模板目录"""
        return self.get("email.default_template_dir", "src/ewidget/templates")
    
    def get_primary_color(self) -> str:
        """获取主色调"""
        return self.get("style.primary_color", "#0078d4")
    
    def get_font_family(self) -> str:
        """获取字体族"""
        return self.get("style.font_family", "'Segoe UI', Tahoma, Arial, sans-serif")
    
    def get_max_width(self) -> str:
        """获取最大宽度"""
        return self.get("style.max_width", "800px")
    
    def get_email_title(self) -> str:
        """获取邮件标题"""
        return self.get("email.default_title", "EWidget 邮件报告")
    
    def get_email_charset(self) -> str:
        """获取邮件字符集"""
        return self.get("email.charset", "UTF-8")
    
    def get_email_lang(self) -> str:
        """获取邮件语言"""
        return self.get("email.lang", "zh-CN")
    
    def get_background_color(self) -> str:
        """获取背景颜色"""
        return self.get("style.background_color", "#ffffff")
    
    def get_base_font_size(self) -> str:
        """获取基础字体大小"""
        return self.get("style.base_font_size", "14px")
    
    def get_line_height(self) -> str:
        """获取行高"""
        return self.get("style.line_height", "1.5")
    
    # Widget相关配置
    def get_text_config(self, key: str, default: Any = None) -> Any:
        """获取文本Widget配置"""
        return self.get(f"widgets.text.{key}", default)
    
    def get_chart_fonts(self) -> List[str]:
        """获取图表中文字体列表"""
        chinese_fonts = self.get("widgets.chart.fonts.chinese_fonts", ["SimHei", "Microsoft YaHei"])
        fallback_fonts = self.get("widgets.chart.fonts.fallback_fonts", ["DejaVu Sans", "Arial"])
        return chinese_fonts + fallback_fonts
    
    def get_widget_config(self, widget_type: str, key: str, default: Any = None) -> Any:
        """获取指定Widget的配置"""
        return self.get(f"widgets.{widget_type}.{key}", default) 