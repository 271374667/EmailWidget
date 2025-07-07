"""
Pytest配置文件

提供测试所需的fixtures和配置
"""

import os
import tempfile
from pathlib import Path
from unittest.mock import MagicMock

import pytest


@pytest.fixture
def temp_dir():
    """创建临时目录fixture"""
    with tempfile.TemporaryDirectory() as tmp_dir:
        yield Path(tmp_dir)


@pytest.fixture
def temp_file():
    """创建临时文件fixture"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        temp_path = tmp_file.name
        yield temp_path
        try:
            os.unlink(temp_path)
        except:
            pass


@pytest.fixture
def mock_logger():
    """模拟logger fixture"""
    return MagicMock()


@pytest.fixture
def mock_cache():
    """模拟缓存fixture"""
    cache = MagicMock()
    cache.get.return_value = None
    cache.set.return_value = None
    cache.clear.return_value = None
    cache.get_info.return_value = {"cache_size": 0, "max_size": 100}
    return cache


@pytest.fixture(autouse=True)
def clean_loggers():
    """自动清理测试产生的logger"""
    import logging

    # 测试前记录现有logger
    existing_loggers = set(logging.Logger.manager.loggerDict.keys())

    yield

    # 测试后清理新创建的logger
    current_loggers = set(logging.Logger.manager.loggerDict.keys())
    new_loggers = current_loggers - existing_loggers

    for logger_name in new_loggers:
        if logger_name.startswith(("test_", "email_widget")):
            logger = logging.getLogger(logger_name)
            # 关闭所有handler
            for handler in logger.handlers[:]:
                handler.close()
                logger.removeHandler(handler)
            # 从manager中删除
            if logger_name in logging.Logger.manager.loggerDict:
                del logging.Logger.manager.loggerDict[logger_name]


@pytest.fixture
def sample_widget_data():
    """提供示例Widget数据"""
    return {
        "text_content": "Sample text content",
        "progress_value": 75,
        "color": "#0066cc",
        "font_size": "16px",
        "width": "300px",
        "height": "20px",
    }


# 测试标记
def pytest_configure(config):
    """配置自定义标记"""
    config.addinivalue_line("markers", "unit: mark test as a unit test")
    config.addinivalue_line("markers", "integration: mark test as an integration test")
    config.addinivalue_line("markers", "slow: mark test as slow running")
