"""EmailWidget模板引擎

基于Jinja2的轻量级模板渲染引擎，支持模板字符串渲染和错误处理。
"""
from typing import Dict, Any, Optional
from jinja2 import Environment, BaseLoader, Template, TemplateError
from contextlib import suppress

from email_widget.core.logger import get_project_logger


class StringTemplateLoader(BaseLoader):
    """字符串模板加载器
    
    用于直接从字符串加载模板，而不是从文件系统。
    """
    
    def get_source(self, environment: Environment, template: str) -> tuple:
        """获取模板源代码
        
        Args:
            environment: Jinja2环境
            template: 模板字符串
            
        Returns:
            (源代码, 模板名, 是否最新) 的元组
        """
        return template, None, lambda: True


class TemplateEngine:
    """模板渲染引擎
    
    提供统一的模板渲染接口，支持模板缓存和错误处理。
    """
    
    def __init__(self):
        """初始化模板引擎"""
        self._logger = get_project_logger()
        
        # 创建Jinja2环境
        self._env = Environment(
            loader=StringTemplateLoader(),
            autoescape=False,  # 邮件HTML不需要自动转义
            trim_blocks=True,
            lstrip_blocks=True
        )
        
        # 模板缓存 {template_string: Template}
        self._template_cache: Dict[str, Template] = {}
        
        self._logger.debug("模板引擎初始化完成")
    
    def _get_template(self, template_string: str) -> Template:
        """获取编译后的模板对象
        
        Args:
            template_string: 模板字符串
            
        Returns:
            编译后的Template对象
        """
        # 检查缓存
        if template_string in self._template_cache:
            return self._template_cache[template_string]
        
        try:
            # 编译模板
            template = self._env.from_string(template_string)
            
            # 缓存模板
            self._template_cache[template_string] = template
            
            self._logger.debug(f"编译并缓存模板，长度: {len(template_string)} 字符")
            return template
            
        except TemplateError as e:
            self._logger.error(f"模板编译失败: {e}")
            raise
    
    def render(self, template_string: str, context: Dict[str, Any]) -> str:
        """渲染模板
        
        Args:
            template_string: 模板字符串
            context: 模板上下文数据
            
        Returns:
            渲染后的HTML字符串
            
        Raises:
            TemplateError: 模板渲染失败时抛出
        """
        try:
            template = self._get_template(template_string)
            result = template.render(**context)
            
            self._logger.debug(f"模板渲染成功，输出长度: {len(result)} 字符")
            return result
            
        except TemplateError as e:
            self._logger.error(f"模板渲染失败: {e}")
            raise
        except Exception as e:
            self._logger.error(f"模板渲染出现未知错误: {e}")
            raise TemplateError(f"模板渲染失败: {e}")
    
    def render_safe(self, template_string: str, context: Dict[str, Any], 
                   fallback: str = "") -> str:
        """安全渲染模板
        
        在渲染失败时返回降级内容而不是抛出异常。
        
        Args:
            template_string: 模板字符串
            context: 模板上下文数据
            fallback: 渲染失败时的降级内容
            
        Returns:
            渲染后的HTML字符串或降级内容
        """
        try:
            return self.render(template_string, context)
        except Exception as e:
            self._logger.warning(f"模板安全渲染失败，使用降级内容: {e}")
            return fallback
    
    def validate_template(self, template_string: str) -> bool:
        """验证模板语法
        
        Args:
            template_string: 模板字符串
            
        Returns:
            模板语法是否正确
        """
        try:
            self._env.from_string(template_string)
            return True
        except TemplateError:
            return False
        except Exception:
            return False
    
    def clear_cache(self) -> None:
        """清空模板缓存"""
        self._template_cache.clear()
        self._logger.debug("清空模板缓存")
    
    def get_cache_stats(self) -> Dict[str, Any]:
        """获取缓存统计信息
        
        Returns:
            缓存统计信息字典
        """
        return {
            'cached_templates': len(self._template_cache),
            'cache_size_bytes': sum(
                len(template_str) for template_str in self._template_cache.keys()
            )
        }


# 全局模板引擎实例
_global_template_engine: Optional[TemplateEngine] = None


def get_template_engine() -> TemplateEngine:
    """获取全局模板引擎实例
    
    Returns:
        TemplateEngine实例
    """
    global _global_template_engine
    if _global_template_engine is None:
        _global_template_engine = TemplateEngine()
    return _global_template_engine 