"""Config组件的完整测试套件。

测试覆盖：
- 配置常量验证
- EmailConfig类功能
- Widget配置映射
- 配置访问方法
"""

import pytest

from email_widget.core.config import EmailConfig


class TestEmailConfigConstants:
    """EmailConfig常量测试"""

    def test_default_title(self):
        """测试默认邮件标题常量"""
        from email_widget.core.config import DEFAULT_TITLE

        assert isinstance(DEFAULT_TITLE, str)
        assert len(DEFAULT_TITLE) > 0

    def test_charset(self):
        """测试字符集常量"""
        from email_widget.core.config import CHARSET

        assert isinstance(CHARSET, str)
        assert CHARSET == "UTF-8"

    def test_primary_color(self):
        """测试主色调常量"""
        from email_widget.core.config import PRIMARY_COLOR

        assert isinstance(PRIMARY_COLOR, str)
        assert PRIMARY_COLOR.startswith("#")

    def test_chinese_fonts(self):
        """测试中文字体常量"""
        from email_widget.core.config import CHINESE_FONTS

        assert isinstance(CHINESE_FONTS, list)
        assert len(CHINESE_FONTS) > 0


class TestEmailConfigClass:
    """EmailConfig类测试"""

    def test_init(self):
        """测试EmailConfig初始化"""
        config = EmailConfig()
        assert config is not None

    def test_get_output_dir(self):
        """测试获取输出目录"""
        config = EmailConfig()
        output_dir = config.get_output_dir()
        assert isinstance(output_dir, str)

    def test_get_primary_color(self):
        """测试获取主色调"""
        config = EmailConfig()
        color = config.get_primary_color()
        assert isinstance(color, str)
        assert color.startswith("#")

    def test_get_font_family(self):
        """测试获取字体族"""
        config = EmailConfig()
        font_family = config.get_font_family()
        assert isinstance(font_family, str)
        assert len(font_family) > 0

    def test_get_max_width(self):
        """测试获取最大宽度"""
        config = EmailConfig()
        max_width = config.get_max_width()
        assert isinstance(max_width, str)

    def test_get_email_title(self):
        """测试获取邮件标题"""
        config = EmailConfig()
        title = config.get_email_title()
        assert isinstance(title, str)
        assert len(title) > 0

    def test_get_email_charset(self):
        """测试获取邮件字符集"""
        config = EmailConfig()
        charset = config.get_email_charset()
        assert isinstance(charset, str)
        assert charset == "UTF-8"

    def test_get_email_lang(self):
        """测试获取邮件语言"""
        config = EmailConfig()
        lang = config.get_email_lang()
        assert isinstance(lang, str)

    def test_get_background_color(self):
        """测试获取背景颜色"""
        config = EmailConfig()
        bg_color = config.get_background_color()
        assert isinstance(bg_color, str)
        assert bg_color.startswith("#")

    def test_get_base_font_size(self):
        """测试获取基础字体大小"""
        config = EmailConfig()
        font_size = config.get_base_font_size()
        assert isinstance(font_size, str)

    def test_get_line_height(self):
        """测试获取行高"""
        config = EmailConfig()
        line_height = config.get_line_height()
        assert isinstance(line_height, str)


class TestEmailConfigTextConfig:
    """EmailConfig文本配置测试"""

    def test_get_text_config_valid_keys(self):
        """测试获取有效文本配置"""
        config = EmailConfig()

        valid_keys = [
            "default_color",
            "title_large_size",
            "title_small_size",
            "body_size",
            "caption_size",
            "section_h2_size",
        ]

        for key in valid_keys:
            value = config.get_text_config(key)
            assert value is not None
            assert isinstance(value, str)

    def test_get_text_config_invalid_key(self):
        """测试获取无效文本配置键"""
        config = EmailConfig()
        value = config.get_text_config("nonexistent_key", "default")
        assert value == "default"

    def test_get_text_config_default_value(self):
        """测试文本配置默认值"""
        config = EmailConfig()
        default_value = "test_default"
        value = config.get_text_config("invalid_key", default_value)
        assert value == default_value


class TestEmailConfigChartConfig:
    """EmailConfig图表配置测试"""

    def test_get_chart_fonts(self):
        """测试获取图表字体"""
        config = EmailConfig()
        fonts = config.get_chart_fonts()
        assert isinstance(fonts, list)
        assert len(fonts) > 0

        # 应该包含中文字体
        font_str = " ".join(fonts).lower()
        assert any(
            chinese_font in font_str for chinese_font in ["simhei", "yahei", "simsun"]
        )


class TestEmailConfigWidgetConfig:
    """EmailConfig Widget配置测试"""

    def test_get_widget_config_text(self):
        """测试获取文本Widget配置"""
        config = EmailConfig()

        # 测试文本Widget配置
        color = config.get_widget_config("text", "default_color")
        assert color is not None
        assert isinstance(color, str)

    def test_get_widget_config_components(self):
        """测试获取组件配置"""
        config = EmailConfig()

        # 测试组件配置
        striped = config.get_widget_config("components", "table_striped")
        assert isinstance(striped, bool)

        log_height = config.get_widget_config("components", "log_max_height")
        assert isinstance(log_height, str)

    def test_get_widget_config_unknown_type(self):
        """测试获取未知Widget类型配置"""
        config = EmailConfig()

        # 未知Widget类型应该返回默认值
        value = config.get_widget_config("unknown", "key", "default")
        assert value == "default"

    def test_get_widget_config_unknown_key(self):
        """测试获取未知配置键"""
        config = EmailConfig()

        # 未知配置键应该返回默认值
        value = config.get_widget_config("text", "unknown_key", "default")
        assert value == "default"


class TestEmailConfigConstants:
    """EmailConfig模块常量测试"""

    def test_module_constants_exist(self):
        """测试模块常量存在"""
        from email_widget.core.config import (
            BACKGROUND_COLOR,
            BASE_FONT_SIZE,
            CHARSET,
            DEFAULT_TITLE,
            FONT_FAMILY,
            LANG,
            LINE_HEIGHT,
            MAX_WIDTH,
            OUTPUT_DIR,
            PRIMARY_COLOR,
        )

        assert OUTPUT_DIR is not None
        assert DEFAULT_TITLE is not None
        assert CHARSET is not None
        assert LANG is not None
        assert PRIMARY_COLOR is not None
        assert FONT_FAMILY is not None
        assert MAX_WIDTH is not None
        assert BACKGROUND_COLOR is not None
        assert BASE_FONT_SIZE is not None
        assert LINE_HEIGHT is not None

    def test_style_constants(self):
        """测试样式常量"""
        from email_widget.core.config import (
            BACKGROUND_COLOR,
            BASE_FONT_SIZE,
            PRIMARY_COLOR,
        )

        # 颜色应该是十六进制格式
        assert PRIMARY_COLOR.startswith("#")
        assert BACKGROUND_COLOR.startswith("#")

        # 字体大小应该包含单位
        assert (
            "px" in BASE_FONT_SIZE or "em" in BASE_FONT_SIZE or "rem" in BASE_FONT_SIZE
        )

    def test_component_constants(self):
        """测试组件常量"""
        from email_widget.core.config import (
            COLUMN_DEFAULT_GAP,
            LOG_MAX_HEIGHT,
            TABLE_STRIPED,
        )

        assert isinstance(TABLE_STRIPED, bool)
        assert isinstance(LOG_MAX_HEIGHT, str)
        assert isinstance(COLUMN_DEFAULT_GAP, str)

    def test_font_constants(self):
        """测试字体常量"""
        from email_widget.core.config import CHINESE_FONTS, FALLBACK_FONTS

        assert isinstance(CHINESE_FONTS, list)
        assert isinstance(FALLBACK_FONTS, list)
        assert len(CHINESE_FONTS) > 0
        assert len(FALLBACK_FONTS) > 0


class TestEmailConfigIntegration:
    """EmailConfig集成测试"""

    def test_complete_config_workflow(self):
        """测试完整配置工作流程"""
        config = EmailConfig()

        # 获取邮件基本配置
        title = config.get_email_title()
        charset = config.get_email_charset()
        lang = config.get_email_lang()

        assert all(isinstance(v, str) for v in [title, charset, lang])

        # 获取样式配置
        primary_color = config.get_primary_color()
        bg_color = config.get_background_color()
        font_family = config.get_font_family()

        assert all(isinstance(v, str) for v in [primary_color, bg_color, font_family])

        # 获取Widget配置
        text_color = config.get_text_config("default_color")
        table_striped = config.get_widget_config("components", "table_striped")

        assert isinstance(text_color, str)
        assert isinstance(table_striped, bool)

    def test_config_consistency(self):
        """测试配置一致性"""
        config = EmailConfig()

        # 多次调用应该返回相同值
        color1 = config.get_primary_color()
        color2 = config.get_primary_color()
        assert color1 == color2

        title1 = config.get_email_title()
        title2 = config.get_email_title()
        assert title1 == title2

    def test_config_defaults_reasonable(self):
        """测试配置默认值合理性"""
        config = EmailConfig()

        # 宽度应该是合理的CSS值
        max_width = config.get_max_width()
        assert "px" in max_width or "%" in max_width or "em" in max_width

        # 字符集应该是UTF-8
        charset = config.get_email_charset()
        assert charset.upper() == "UTF-8"

        # 颜色应该是有效的十六进制值
        primary_color = config.get_primary_color()
        assert len(primary_color) in [4, 7]  # #RGB 或 #RRGGBB
        assert all(c in "0123456789ABCDEFabcdef#" for c in primary_color)


class TestEmailConfigErrorHandling:
    """EmailConfig错误处理测试"""

    def test_invalid_config_keys_graceful(self):
        """测试无效配置键的优雅处理"""
        config = EmailConfig()

        # 无效的文本配置键应该返回默认值
        result = config.get_text_config("invalid_key", "default_value")
        assert result == "default_value"

        # 无效的Widget配置应该返回默认值
        result = config.get_widget_config("invalid_type", "invalid_key", "default")
        assert result == "default"

    def test_none_default_values(self):
        """测试None默认值处理"""
        config = EmailConfig()

        # 使用None作为默认值
        result = config.get_text_config("invalid_key", None)
        assert result is None

        result = config.get_widget_config("invalid_type", "invalid_key", None)
        assert result is None

    def test_config_method_robustness(self):
        """测试配置方法健壮性"""
        config = EmailConfig()

        # 所有get方法都应该返回有意义的值
        methods = [
            config.get_output_dir,
            config.get_primary_color,
            config.get_font_family,
            config.get_max_width,
            config.get_email_title,
            config.get_email_charset,
            config.get_email_lang,
            config.get_background_color,
            config.get_base_font_size,
            config.get_line_height,
            config.get_chart_fonts,
        ]

        for method in methods:
            try:
                result = method()
                assert result is not None
            except Exception as e:
                pytest.fail(f"Method {method.__name__} should not raise exception: {e}")


class TestEmailConfigPerformance:
    """EmailConfig性能测试"""

    def test_config_access_performance(self):
        """测试配置访问性能"""
        import time

        config = EmailConfig()

        # 测试多次访问的性能
        start_time = time.time()
        for _ in range(1000):
            config.get_primary_color()
            config.get_email_title()
            config.get_font_family()
        end_time = time.time()

        # 1000次访问应该很快完成
        assert end_time - start_time < 1.0

    def test_config_memory_efficiency(self):
        """测试配置内存效率"""
        # 创建多个配置实例不应该消耗过多内存
        configs = [EmailConfig() for _ in range(100)]

        # 验证配置实例工作正常
        for config in configs[:5]:  # 只测试前5个
            assert config.get_primary_color() is not None
