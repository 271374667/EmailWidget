"""配置管理模块"""
from pathlib import Path
from typing import Dict, Any, Optional
import tomli
from contextlib import suppress

class EmailConfig:
    """邮件配置管理类"""
    
    DEFAULT_CONFIG = {
        "email": {
            "output_dir": ".",
            "default_template_dir": "src/ewidget/templates"
        },
        "style": {
            "primary_color": "#0078d4",
            "font_family": "'Segoe UI', Tahoma, Arial, sans-serif",
            "max_width": "800px"
        },
        "components": {
            "table_striped": True,
            "log_max_height": "400px",
            "column_default_gap": "20px"
        }
    }
    
    def __init__(self, config_path: Optional[str] = None):
        self._config = self.DEFAULT_CONFIG.copy()
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