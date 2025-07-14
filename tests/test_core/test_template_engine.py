"""TemplateEngine模块测试用例 - 完整覆盖率测试"""

import threading
import time
from unittest.mock import patch

import pytest
from jinja2 import TemplateError

from email_widget.core.template_engine import TemplateEngine, get_template_engine


class TestTemplateEngineInitialization:
    """测试TemplateEngine初始化功能"""

    def test_init_default(self):
        """测试默认初始化"""
        engine = TemplateEngine()

        assert engine._env is not None
        assert engine._template_cache == {}
        assert engine._logger is not None

    def test_get_global_template_engine(self):
        """测试获取全局模板引擎实例"""
        engine1 = get_template_engine()
        engine2 = get_template_engine()

        # 应该返回同一个实例（单例模式）
        assert engine1 is engine2
        assert isinstance(engine1, TemplateEngine)

    def test_jinja_environment_setup(self):
        """测试Jinja2环境设置"""
        engine = TemplateEngine()
        assert engine._env is not None
        assert hasattr(engine._env, "from_string")
        assert engine._env.trim_blocks is True
        assert engine._env.lstrip_blocks is True


class TestTemplateCompilation:
    """模板编译测试"""

    def test_get_template_success(self):
        """测试成功编译模板"""
        engine = TemplateEngine()
        template_string = "<div>Hello {{ name }}!</div>"

        template = engine._get_template(template_string)

        assert template is not None
        assert hasattr(template, "render")

    def test_get_template_caching(self):
        """测试模板缓存功能"""
        engine = TemplateEngine()
        template_string = "<div>Hello {{ name }}!</div>"

        # 第一次获取模板
        template1 = engine._get_template(template_string)
        # 第二次获取模板（应该使用缓存）
        template2 = engine._get_template(template_string)

        assert template1 is template2
        assert len(engine._template_cache) == 1

    def test_get_template_syntax_error(self):
        """测试模板语法错误"""
        engine = TemplateEngine()
        invalid_template = "<div>{% for item in items %}</div>"  # 缺少endfor

        with pytest.raises(TemplateError):
            engine._get_template(invalid_template)

    def test_get_template_different_templates(self):
        """测试编译不同模板"""
        engine = TemplateEngine()
        template1_str = "<div>Template 1: {{ data }}</div>"
        template2_str = "<span>Template 2: {{ value }}</span>"

        template1 = engine._get_template(template1_str)
        template2 = engine._get_template(template2_str)

        assert template1 is not template2
        assert len(engine._template_cache) == 2


class TestTemplateRendering:
    """模板渲染测试"""

    def test_render_success(self):
        """测试成功渲染模板"""
        engine = TemplateEngine()
        template_string = "<div>Hello {{ name }}!</div>"
        context = {"name": "World"}

        result = engine.render(template_string, context)

        assert result == "<div>Hello World!</div>"

    def test_render_with_empty_context(self):
        """测试空上下文渲染"""
        engine = TemplateEngine()
        template_string = "<div>Hello World!</div>"

        result = engine.render(template_string, {})

        assert result == "<div>Hello World!</div>"

    def test_render_with_complex_context(self):
        """测试复杂上下文渲染"""
        engine = TemplateEngine()
        template_string = """
        <div>
            <h1>{{ title }}</h1>
            <ul>
            {% for item in items %}
                <li>{{ item.name }}: {{ item.value }}</li>
            {% endfor %}
            </ul>
        </div>
        """
        context = {
            "title": "测试标题",
            "items": [
                {"name": "项目1", "value": "值1"},
                {"name": "项目2", "value": "值2"},
            ],
        }

        result = engine.render(template_string, context)

        assert "测试标题" in result
        assert "项目1" in result
        assert "值1" in result

    def test_render_template_error(self):
        """测试模板渲染错误"""
        engine = TemplateEngine()
        template_string = "<div>{{ undefined_variable.missing_attr }}</div>"

        with pytest.raises(TemplateError):
            engine.render(template_string, {})

    def test_render_syntax_error(self):
        """测试模板语法错误"""
        engine = TemplateEngine()
        invalid_template = "<div>{% invalid syntax %}</div>"

        with pytest.raises(TemplateError):
            engine.render(invalid_template, {})


class TestSafeTemplateRendering:
    """安全模板渲染测试"""

    def test_render_safe_success(self):
        """测试安全渲染成功"""
        engine = TemplateEngine()
        template_string = "<div>Hello {{ name }}!</div>"
        context = {"name": "World"}

        result = engine.render_safe(template_string, context)

        assert result == "<div>Hello World!</div>"

    def test_render_safe_with_fallback(self):
        """测试安全渲染使用降级内容"""
        engine = TemplateEngine()
        invalid_template = "<div>{% invalid syntax %}</div>"
        fallback = "<div>渲染失败</div>"

        result = engine.render_safe(invalid_template, {}, fallback)

        assert result == fallback

    def test_render_safe_default_fallback(self):
        """测试安全渲染默认降级内容"""
        engine = TemplateEngine()
        invalid_template = "<div>{% invalid syntax %}</div>"

        result = engine.render_safe(invalid_template, {})

        assert result == ""

    def test_render_safe_runtime_error(self):
        """测试安全渲染运行时错误"""
        engine = TemplateEngine()
        template_string = "<div>{{ undefined_variable.missing_attr }}</div>"
        fallback = "<div>运行时错误</div>"

        result = engine.render_safe(template_string, {}, fallback)

        assert result == fallback


class TestTemplateValidation:
    """模板验证测试"""

    def test_validate_template_valid(self):
        """测试验证有效模板"""
        engine = TemplateEngine()
        valid_template = "<div>Hello {{ name }}!</div>"

        is_valid = engine.validate_template(valid_template)

        assert is_valid is True

    def test_validate_template_invalid_syntax(self):
        """测试验证无效语法模板"""
        engine = TemplateEngine()
        invalid_template = "<div>{% invalid syntax %}</div>"

        is_valid = engine.validate_template(invalid_template)

        assert is_valid is False

    def test_validate_template_incomplete(self):
        """测试验证不完整模板"""
        engine = TemplateEngine()
        incomplete_template = "<div>{% for item in items %}</div>"  # 缺少endfor

        is_valid = engine.validate_template(incomplete_template)

        assert is_valid is False

    def test_validate_template_empty(self):
        """测试验证空模板"""
        engine = TemplateEngine()
        empty_template = ""

        is_valid = engine.validate_template(empty_template)

        assert is_valid is True

    def test_validate_template_complex_valid(self):
        """测试验证复杂有效模板"""
        engine = TemplateEngine()
        complex_template = """
        {% for item in items %}
            <div class="{{ item.class }}">
                {% if item.name %}
                    <h1>{{ item.name | upper }}</h1>
                {% endif %}
            </div>
        {% endfor %}
        """

        is_valid = engine.validate_template(complex_template)

        assert is_valid is True


class TestCacheManagement:
    """缓存管理测试"""

    def test_clear_cache(self):
        """测试清空缓存"""
        engine = TemplateEngine()

        # 先添加一些模板到缓存
        engine._get_template("<div>Template 1</div>")
        engine._get_template("<div>Template 2</div>")

        assert len(engine._template_cache) == 2

        engine.clear_cache()

        assert len(engine._template_cache) == 0

    def test_get_cache_stats_empty(self):
        """测试获取空缓存统计"""
        engine = TemplateEngine()

        stats = engine.get_cache_stats()

        assert stats["cached_templates"] == 0
        assert stats["cache_size_bytes"] == 0

    def test_get_cache_stats_with_templates(self):
        """测试获取有模板的缓存统计"""
        engine = TemplateEngine()
        template1 = "<div>Template 1</div>"
        template2 = "<span>Template 2</span>"

        engine._get_template(template1)
        engine._get_template(template2)

        stats = engine.get_cache_stats()

        assert stats["cached_templates"] == 2
        expected_size = len(template1) + len(template2)
        assert stats["cache_size_bytes"] == expected_size

    def test_cache_memory_efficiency(self):
        """测试缓存内存效率"""
        engine = TemplateEngine()

        # 添加多个模板
        templates = [f"<div>Template {i}</div>" for i in range(10)]
        for template in templates:
            engine._get_template(template)

        stats = engine.get_cache_stats()
        assert stats["cached_templates"] == 10

        # 清理缓存
        engine.clear_cache()
        stats_after = engine.get_cache_stats()
        assert stats_after["cached_templates"] == 0
        assert stats_after["cache_size_bytes"] == 0


class TestTemplateEngineErrorHandling:
    """模板引擎错误处理测试"""

    def test_render_with_none_template(self):
        """测试使用None模板渲染"""
        engine = TemplateEngine()

        with pytest.raises(TemplateError):
            engine.render(None, {"data": "test"})

    def test_render_with_non_string_template(self):
        """测试使用非字符串模板渲染"""
        engine = TemplateEngine()

        with pytest.raises(TemplateError):
            engine.render(123, {"data": "test"})

    @patch("email_widget.core.template_engine.TemplateEngine._get_template")
    def test_render_template_compilation_error(self, mock_get_template):
        """测试模板编译错误"""
        mock_get_template.side_effect = TemplateError("编译失败")

        engine = TemplateEngine()

        with pytest.raises(TemplateError):
            engine.render("template", {})

    def test_large_template_handling(self):
        """测试大模板处理"""
        engine = TemplateEngine()
        large_template_content = "<div>" + "x" * 10000 + "{{ data }}</div>"

        result = engine.render_safe(large_template_content, {"data": "test"})

        assert "test" in result
        assert len(result) > 10000


class TestTemplateEnginePerformance:
    """模板引擎性能测试"""

    def test_multiple_renders_performance(self):
        """测试多次渲染性能"""
        engine = TemplateEngine()
        template_string = "<div>Hello {{ name }}!</div>"
        context = {"name": "World"}

        # 第一次渲染（编译模板）
        start_time = time.perf_counter()
        result1 = engine.render(template_string, context)
        first_time = time.perf_counter() - start_time

        # 第二次渲染（使用缓存）
        start_time = time.perf_counter()
        result2 = engine.render(template_string, context)
        second_time = time.perf_counter() - start_time

        assert result1 == result2
        assert second_time < first_time  # 缓存应该更快

    def test_concurrent_access_simulation(self):
        """测试并发访问模拟"""
        engine = TemplateEngine()
        template_string = "<div>Thread {{ thread_id }}</div>"
        results = []

        def render_template(thread_id):
            result = engine.render(template_string, {"thread_id": thread_id})
            results.append(result)

        # 创建多个线程
        threads = []
        for i in range(5):
            thread = threading.Thread(target=render_template, args=(i,))
            threads.append(thread)
            thread.start()

        # 等待所有线程完成
        for thread in threads:
            thread.join()

        assert len(results) == 5
        for i, result in enumerate(results):
            assert f"Thread {i}" in result

    def test_cache_effectiveness(self):
        """测试缓存效果"""
        engine = TemplateEngine()
        template_string = "<div>{{ data }}</div>"

        # 第一次访问（未缓存）
        start_time = time.perf_counter()
        template1 = engine._get_template(template_string)
        first_time = time.perf_counter() - start_time

        # 第二次访问（已缓存）
        start_time = time.perf_counter()
        template2 = engine._get_template(template_string)
        second_time = time.perf_counter() - start_time

        # 缓存应该返回同一个对象且更快
        assert template1 is template2
        assert second_time < first_time


class TestTemplateEngineIntegration:
    """模板引擎集成测试"""

    def test_complete_workflow(self):
        """测试完整工作流程"""
        engine = TemplateEngine()

        # 1. 验证模板
        template_string = "<div>Hello {{ name }}!</div>"
        assert engine.validate_template(template_string) is True

        # 2. 渲染模板
        result = engine.render(template_string, {"name": "Integration"})
        assert result == "<div>Hello Integration!</div>"

        # 3. 检查缓存
        stats = engine.get_cache_stats()
        assert stats["cached_templates"] == 1

        # 4. 安全渲染
        safe_result = engine.render_safe(template_string, {"name": "Safe"})
        assert safe_result == "<div>Hello Safe!</div>"

        # 5. 清理缓存
        engine.clear_cache()
        final_stats = engine.get_cache_stats()
        assert final_stats["cached_templates"] == 0

    def test_error_recovery_and_fallback(self):
        """测试错误恢复和降级"""
        engine = TemplateEngine()

        # 测试无效模板的降级
        invalid_template = "<div>{% invalid %}</div>"
        fallback = "<div>Error occurred</div>"

        result = engine.render_safe(invalid_template, {}, fallback)
        assert result == fallback

        # 测试有效模板正常工作
        valid_template = "<div>{{ message }}</div>"
        result = engine.render_safe(valid_template, {"message": "Success"})
        assert result == "<div>Success</div>"

    def test_template_context_isolation(self):
        """测试模板上下文隔离"""
        engine = TemplateEngine()
        template_string = "<div>{{ shared_var }}</div>"

        # 渲染模板1
        result1 = engine.render(template_string, {"shared_var": "Value1"})
        # 渲染模板2
        result2 = engine.render(template_string, {"shared_var": "Value2"})

        assert result1 == "<div>Value1</div>"
        assert result2 == "<div>Value2</div>"
        # 确保上下文没有交叉污染
        assert result1 != result2

    def test_global_template_engine_consistency(self):
        """测试全局模板引擎一致性"""
        # 获取全局实例
        engine1 = get_template_engine()
        engine2 = get_template_engine()

        # 应该是同一个实例
        assert engine1 is engine2

        # 记录初始缓存数量
        initial_stats = engine1.get_cache_stats()
        initial_count = initial_stats["cached_templates"]

        # 在一个实例中添加缓存
        template_string = "<div>Global test</div>"
        engine1._get_template(template_string)

        # 另一个实例应该能看到缓存增加
        stats = engine2.get_cache_stats()
        assert stats["cached_templates"] == initial_count + 1
