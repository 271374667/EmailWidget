"""Email模块测试用例"""

import pytest
from unittest.mock import patch, MagicMock, mock_open
from pathlib import Path
import tempfile
import os
import datetime

from email_widget.email import Email
from email_widget.widgets.text_widget import TextWidget
from email_widget.widgets.progress_widget import ProgressWidget
from email_widget.widgets.table_widget import TableWidget


class TestEmail:
    """Email测试类"""
    
    def setup_method(self):
        """每个测试方法执行前的设置"""
        self.email = Email("Test Subject")
    
    def test_init_default(self):
        """测试默认初始化"""
        email = Email()
        assert email.title == "邮件报告"
        assert email.subtitle is None
        assert email.footer_text is None
        assert email.widgets == []
        assert email.config is not None
        assert email._template_engine is not None
        assert email._logger is not None
        assert isinstance(email._created_at, datetime.datetime)
    
    def test_init_with_title(self):
        """测试带标题的初始化"""
        title = "Test Email Title"
        email = Email(title)
        assert email.title == title
    
    def test_add_widget(self):
        """测试添加组件"""
        widget = TextWidget().set_content("Test content")
        result = self.email.add_widget(widget)
        
        assert result is self.email  # 支持链式调用
        assert len(self.email.widgets) == 1
        assert self.email.widgets[0] is widget
    
    def test_add_widgets_batch(self):
        """测试批量添加组件"""
        widget1 = TextWidget().set_content("Widget 1")
        widget2 = ProgressWidget().set_value(50)
        widgets = [widget1, widget2]
        
        result = self.email.add_widgets(widgets)
        
        assert result is self.email
        assert len(self.email.widgets) == 2
        assert self.email.widgets[0] is widget1
        assert self.email.widgets[1] is widget2
    
    def test_add_multiple_widgets_individually(self):
        """测试逐个添加多个组件"""
        widget1 = TextWidget().set_content("Widget 1")
        widget2 = ProgressWidget().set_value(50)
        
        result = self.email.add_widget(widget1).add_widget(widget2)
        assert result is self.email
        assert len(self.email.widgets) == 2
        assert self.email.widgets[0] is widget1
        assert self.email.widgets[1] is widget2
    
    def test_clear_widgets(self):
        """测试清空组件"""
        widget1 = TextWidget().set_content("Widget 1")
        widget2 = ProgressWidget().set_value(50)
        self.email.add_widget(widget1).add_widget(widget2)
        
        assert len(self.email.widgets) == 2
        
        result = self.email.clear_widgets()
        assert result is self.email
        assert len(self.email.widgets) == 0
    
    def test_remove_widget_by_id(self):
        """测试根据ID移除组件"""
        widget1 = TextWidget("widget1").set_content("Widget 1")
        widget2 = ProgressWidget("widget2").set_value(50)
        
        self.email.add_widget(widget1).add_widget(widget2)
        assert len(self.email.widgets) == 2
        
        result = self.email.remove_widget("widget1")
        assert result is self.email
        assert len(self.email.widgets) == 1
        assert self.email.widgets[0] is widget2
    
    def test_get_widget_by_id(self):
        """测试根据ID获取组件"""
        widget1 = TextWidget("widget1").set_content("Widget 1")
        widget2 = ProgressWidget("widget2").set_value(50)
        
        self.email.add_widget(widget1).add_widget(widget2)
        
        found_widget = self.email.get_widget("widget1")
        assert found_widget is widget1
        
        not_found = self.email.get_widget("non_existent")
        assert not_found is None
    
    def test_set_title(self):
        """测试设置标题"""
        new_title = "New Title"
        result = self.email.set_title(new_title)
        
        assert result is self.email
        assert self.email.title == new_title
    
    def test_set_subtitle(self):
        """测试设置副标题"""
        subtitle = "This is a subtitle"
        result = self.email.set_subtitle(subtitle)
        
        assert result is self.email
        assert self.email.subtitle == subtitle
    
    def test_set_footer(self):
        """测试设置脚注"""
        footer = "This is footer text"
        result = self.email.set_footer(footer)
        
        assert result is self.email
        assert self.email.footer_text == footer
        
        # 测试清空脚注
        result = self.email.set_footer(None)
        assert self.email.footer_text is None
    
    def test_add_title_convenience_method(self):
        """测试添加标题的便捷方法"""
        from email_widget.core.enums import TextType
        
        result = self.email.add_title("Chapter 1", TextType.SECTION_H2)
        
        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], TextWidget)
    
    def test_add_text_convenience_method(self):
        """测试添加文本的便捷方法"""
        result = self.email.add_text("Some content", color="red")
        
        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], TextWidget)
    
    def test_add_table_from_data_convenience_method(self):
        """测试从数据添加表格的便捷方法"""
        data = [["A1", "B1"], ["A2", "B2"]]
        headers = ["Col A", "Col B"]
        
        result = self.email.add_table_from_data(data, headers=headers, title="Test Table")
        
        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], TableWidget)
    
    def test_add_progress_convenience_method(self):
        """测试添加进度条的便捷方法"""
        result = self.email.add_progress(75.0, "Loading", max_value=100.0)
        
        assert result is self.email
        assert len(self.email.widgets) == 1
        assert isinstance(self.email.widgets[0], ProgressWidget)
    
    def test_export_html_with_filename(self):
        """测试导出HTML文件"""
        with tempfile.TemporaryDirectory() as temp_dir:
            filename = "test_email.html"
            
            # 添加一些内容
            self.email.add_text("Test content")
            
            result_path = self.email.export_html(filename, output_dir=temp_dir)
            
            assert isinstance(result_path, Path)
            assert result_path.exists()
            assert result_path.name == filename
            
            # 验证文件内容包含基本HTML结构
            content = result_path.read_text(encoding='utf-8')
            assert "<!DOCTYPE html>" in content
            assert self.email.title in content
    
    def test_export_html_default_filename(self):
        """测试使用默认文件名导出HTML"""
        with tempfile.TemporaryDirectory() as temp_dir:
            result_path = self.email.export_html(output_dir=temp_dir)
            
            assert result_path.exists()
            assert result_path.suffix == '.html'
    
    def test_export_str(self):
        """测试导出HTML字符串"""
        self.email.add_text("Test content")
        
        html_str = self.email.export_str()
        
        assert isinstance(html_str, str)
        assert "<!DOCTYPE html>" in html_str
        assert self.email.title in html_str
    
    def test_get_widget_count(self):
        """测试获取组件数量"""
        assert self.email.get_widget_count() == 0
        
        self.email.add_text("Content 1")
        assert self.email.get_widget_count() == 1
        
        self.email.add_text("Content 2")
        assert self.email.get_widget_count() == 2
    
    def test_len_method(self):
        """测试len()方法"""
        assert len(self.email) == 0
        
        self.email.add_text("Content 1")
        assert len(self.email) == 1
        
        self.email.add_text("Content 2")
        assert len(self.email) == 2
    
    def test_str_representation(self):
        """测试字符串表示"""
        self.email.add_text("Content 1")
        self.email.add_text("Content 2")
        
        str_repr = str(self.email)
        assert "Test Subject" in str_repr
        assert "widgets=2" in str_repr
    
    def test_properties(self):
        """测试属性访问"""
        assert self.email.title == "Test Subject"
        assert self.email.subtitle is None
        assert self.email.footer_text is None
        assert isinstance(self.email.widgets, list)
        assert len(self.email.widgets) == 0
    
    def test_chain_methods(self):
        """测试方法链式调用"""
        result = (self.email
                  .set_title("Chained Title")
                  .set_subtitle("Chained Subtitle")
                  .set_footer("Chained Footer")
                  .add_text("Chained Content"))
        
        assert result is self.email
        assert self.email.title == "Chained Title"
        assert self.email.subtitle == "Chained Subtitle"
        assert self.email.footer_text == "Chained Footer"
        assert len(self.email.widgets) == 1
    
    def test_empty_email_rendering(self):
        """测试空邮件渲染"""
        empty_email = Email("Empty Email")
        html_content = empty_email.export_str()
        
        assert "<!DOCTYPE html>" in html_content
        assert "Empty Email" in html_content


class TestEmailIntegration:
    """Email集成测试类"""
    
    def test_full_workflow(self):
        """测试完整工作流程"""
        from email_widget.core.enums import TextType
        
        email = Email("Integration Test Report")
        
        # 配置邮件
        email.set_subtitle("Daily Data Report")
        email.set_footer("Generated by Data Team")
        
        # 添加各种组件
        email.add_title("Summary", TextType.SECTION_H2)
        email.add_text("This is a summary of today's data.")
        
        email.add_title("Progress", TextType.SECTION_H2)
        email.add_progress(85.0, "Overall Progress")
        
        email.add_title("Data Table", TextType.SECTION_H2)
        data = [["Item A", "100"], ["Item B", "200"]]
        email.add_table_from_data(data, headers=["Item", "Value"])
        
        # 导出并验证
        html_content = email.export_str()
        
        assert "Integration Test Report" in html_content
        assert "Daily Data Report" in html_content
        assert "Generated by Data Team" in html_content
    
    def test_widget_management_workflow(self):
        """测试Widget管理工作流程"""
        email = Email("Widget Management Test")
        
        # 添加多个widget
        email.add_text("Text 1")
        email.add_text("Text 2")
        email.add_progress(30.0, "Progress 1")
        
        assert len(email) == 3
        
        # 清空所有widget
        email.clear_widgets()
        assert len(email) == 0
        
        # 重新添加带ID的widget
        widget1 = TextWidget("w1").set_content("Widget 1")
        widget2 = TextWidget("w2").set_content("Widget 2")
        widget3 = TextWidget("w3").set_content("Widget 3")
        
        email.add_widgets([widget1, widget2, widget3])
        assert len(email) == 3
        
        # 根据ID移除widget
        email.remove_widget("w2")
        assert len(email) == 2
        
        # 验证正确的widget被移除
        assert email.get_widget("w1") is widget1
        assert email.get_widget("w2") is None
        assert email.get_widget("w3") is widget3
    
    def test_export_workflow(self):
        """测试导出工作流程"""
        email = Email("Export Test")
        email.add_text("Export content")
        
        with tempfile.TemporaryDirectory() as temp_dir:
            # 测试自定义文件名导出
            custom_path = email.export_html("custom_report.html", temp_dir)
            assert custom_path.name == "custom_report.html"
            assert custom_path.exists()
            
            # 测试默认文件名导出
            default_path = email.export_html(output_dir=temp_dir)
            assert default_path.exists()
            assert default_path != custom_path
            
            # 验证文件内容
            custom_content = custom_path.read_text(encoding='utf-8')
            
            assert "Export Test" in custom_content
            assert "Export content" in custom_content 