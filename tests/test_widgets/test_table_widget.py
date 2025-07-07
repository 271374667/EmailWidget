"""表格Widget测试模块"""

import pytest

# 尝试导入pandas，如果不可用则跳过相关测试
try:
    import pandas as pd

    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False
    pd = None

from email_widget.core.enums import StatusType
from email_widget.widgets.table_widget import TableCell, TableWidget


class TestTableCell:
    """TableCell测试类"""

    def test_init_default(self):
        """测试默认初始化"""
        cell = TableCell("测试值")

        assert cell.value == "测试值"
        assert cell.status is None
        assert cell.color is None
        assert cell.bold is False
        assert cell.align == "center"

    def test_init_with_all_params(self):
        """测试完整参数初始化"""
        cell = TableCell(
            value="重要数据",
            status=StatusType.ERROR,
            color="#ff0000",
            bold=True,
            align="center",
        )

        assert cell.value == "重要数据"
        assert cell.status == StatusType.ERROR
        assert cell.color == "#ff0000"
        assert cell.bold is True
        assert cell.align == "center"


class TestTableWidget:
    """TableWidget测试类"""

    def setup_method(self):
        """每个测试方法前的设置"""
        self.widget = TableWidget()

    def test_init(self):
        """测试初始化"""
        assert self.widget._dataframe is None
        assert self.widget._title is None
        assert self.widget._headers == []
        assert self.widget._rows == []
        assert self.widget._show_index is False
        assert self.widget._striped is True
        assert self.widget._bordered is True
        assert self.widget._hover_effect is True
        assert self.widget._max_width is None
        assert self.widget._header_bg_color == "#f3f2f1"
        assert self.widget._border_color == "#e1dfdd"

    def test_init_with_widget_id(self):
        """测试使用widget_id初始化"""
        widget = TableWidget("test_id")
        assert widget.widget_id == "test_id"

    @pytest.mark.skipif(not PANDAS_AVAILABLE, reason="pandas not installed")
    def test_set_dataframe(self):
        """测试设置DataFrame"""
        df = pd.DataFrame({"A": [1, 2, 3], "B": ["a", "b", "c"], "C": [1.1, 2.2, 3.3]})

        result = self.widget.set_dataframe(df)

        assert result is self.widget  # 支持链式调用
        assert self.widget._dataframe is not None
        assert list(self.widget._dataframe.columns) == ["A", "B", "C"]
        assert self.widget._headers == ["A", "B", "C"]
        assert len(self.widget._rows) == 3

    @pytest.mark.skipif(not PANDAS_AVAILABLE, reason="pandas not installed")
    def test_set_dataframe_with_status_data(self):
        """测试设置包含状态数据的DataFrame"""
        df = pd.DataFrame(
            {
                "Name": ["项目A", "项目B"],
                "Status": [
                    {"text": "进行中", "status": "info"},
                    {"text": "已完成", "status": "success"},
                ],
            }
        )

        self.widget.set_dataframe(df)

        # 验证状态数据被正确处理
        assert len(self.widget._rows) == 2
        status_cell = self.widget._rows[0][1]  # 第一行的状态列
        assert isinstance(status_cell, TableCell)
        assert status_cell.value == "进行中"
        assert status_cell.status == StatusType.INFO

    def test_set_title(self):
        """测试设置标题"""
        result = self.widget.set_title("数据表格")

        assert result is self.widget
        assert self.widget._title == "数据表格"

    def test_set_headers(self):
        """测试设置表头"""
        headers = ["列1", "列2", "列3"]
        result = self.widget.set_headers(headers)

        assert result is self.widget
        assert self.widget._headers == ["列1", "列2", "列3"]
        # 验证是拷贝而非引用
        headers.append("列4")
        assert len(self.widget._headers) == 3

    def test_add_row(self):
        """测试添加行"""
        row = ["值1", "值2", "值3"]
        result = self.widget.add_row(row)

        assert result is self.widget
        assert len(self.widget._rows) == 1
        assert self.widget._rows[0] == row

    def test_add_row_with_table_cells(self):
        """测试添加包含TableCell的行"""
        cell = TableCell("重要", status=StatusType.WARNING, bold=True)
        row = ["普通值", cell, "其他值"]

        self.widget.add_row(row)

        assert len(self.widget._rows) == 1
        assert self.widget._rows[0][1] is cell

    def test_set_rows(self):
        """测试设置所有行"""
        rows = [["A1", "B1", "C1"], ["A2", "B2", "C2"]]
        result = self.widget.set_rows(rows)

        assert result is self.widget
        assert self.widget._rows == rows

    def test_clear_rows(self):
        """测试清空行"""
        self.widget.add_row(["a", "b", "c"])
        self.widget.add_row(["d", "e", "f"])

        result = self.widget.clear_rows()

        assert result is self.widget
        assert len(self.widget._rows) == 0

    def test_show_index(self):
        """测试设置显示索引"""
        result = self.widget.show_index(True)

        assert result is self.widget
        assert self.widget._show_index is True

        # 测试默认值
        result = self.widget.show_index()
        assert self.widget._show_index is True

    def test_set_striped(self):
        """测试设置斑马纹"""
        result = self.widget.set_striped(False)

        assert result is self.widget
        assert self.widget._striped is False

    def test_set_bordered(self):
        """测试设置边框"""
        result = self.widget.set_bordered(False)

        assert result is self.widget
        assert self.widget._bordered is False

    def test_set_hover_effect(self):
        """测试设置悬停效果"""
        result = self.widget.set_hover_effect(False)

        assert result is self.widget
        assert self.widget._hover_effect is False

    def test_set_max_width(self):
        """测试设置最大宽度"""
        result = self.widget.set_max_width("800px")

        assert result is self.widget
        assert self.widget._max_width == "800px"

    def test_set_header_bg_color(self):
        """测试设置表头背景色"""
        result = self.widget.set_header_bg_color("#ff0000")

        assert result is self.widget
        assert self.widget._header_bg_color == "#ff0000"

    def test_set_border_color(self):
        """测试设置边框颜色"""
        result = self.widget.set_border_color("#00ff00")

        assert result is self.widget
        assert self.widget._border_color == "#00ff00"

    @pytest.mark.skipif(not PANDAS_AVAILABLE, reason="pandas not installed")
    def test_add_data_row_with_existing_dataframe(self):
        """测试在已有DataFrame基础上添加数据行"""
        # 先设置DataFrame
        df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
        self.widget.set_dataframe(df)

        # 添加新行
        result = self.widget.add_data_row([5, 6])

        assert result is self.widget
        assert len(self.widget._dataframe) == 3
        assert self.widget._dataframe.iloc[2]["A"] == 5
        assert self.widget._dataframe.iloc[2]["B"] == 6

    @pytest.mark.skipif(not PANDAS_AVAILABLE, reason="pandas not installed")
    def test_add_data_row_without_dataframe(self):
        """测试在没有DataFrame时添加数据行"""
        result = self.widget.add_data_row([1, 2, 3])

        assert result is self.widget
        assert self.widget._dataframe is not None
        assert len(self.widget._dataframe) == 1

    @pytest.mark.skipif(not PANDAS_AVAILABLE, reason="pandas not installed")
    def test_clear_data(self):
        """测试清空数据"""
        # 设置一些数据
        df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
        self.widget.set_dataframe(df)
        self.widget.add_row(["x", "y"])

        result = self.widget.clear_data()

        assert result is self.widget
        assert self.widget._dataframe is None
        assert len(self.widget._rows) == 0

    def test_set_column_width(self):
        """测试设置列宽"""
        result = self.widget.set_column_width("列A", "200px")

        assert result is self.widget
        assert hasattr(self.widget, "_column_widths")
        assert self.widget._column_widths["列A"] == "200px"

    def test_add_status_cell(self):
        """测试创建状态单元格"""
        cell = self.widget.add_status_cell("成功", StatusType.SUCCESS)

        assert isinstance(cell, TableCell)
        assert cell.value == "成功"
        assert cell.status == StatusType.SUCCESS

    def test_add_colored_cell(self):
        """测试创建彩色单元格"""
        cell = self.widget.add_colored_cell(
            "重要", "#ff0000", bold=True, align="center"
        )

        assert isinstance(cell, TableCell)
        assert cell.value == "重要"
        assert cell.color == "#ff0000"
        assert cell.bold is True
        assert cell.align == "center"

    @pytest.mark.skipif(not PANDAS_AVAILABLE, reason="pandas not installed")
    def test_properties(self):
        """测试属性getter"""
        # 设置数据
        df = pd.DataFrame({"A": [1], "B": [2]})
        self.widget.set_dataframe(df)
        self.widget.set_title("测试表格")
        self.widget.set_headers(["列1", "列2"])
        rows = [["值1", "值2"]]
        self.widget.set_rows(rows)

        # 验证属性
        assert self.widget.dataframe is not None
        assert self.widget.title == "测试表格"
        assert self.widget.headers == ["列1", "列2"]
        assert self.widget.rows == rows

    def test_get_template_name(self):
        """测试获取模板名称"""
        assert self.widget._get_template_name() == "table.html"

    def test_get_template_context_empty(self):
        """测试空表格的模板上下文"""
        context = self.widget.get_template_context()

        # 空表格应该返回基本结构
        assert not context

    def test_get_template_context_with_data(self):
        """测试有数据的表格模板上下文"""
        # 设置表格数据
        self.widget.set_title("测试表格")
        self.widget.set_headers(["列1", "列2"])
        self.widget.add_row(["值1", "值2"])
        self.widget.add_row(["值3", "值4"])
        self.widget.show_index(True)

        context = self.widget.get_template_context()

        # 验证基本数据
        assert context["title"] == "测试表格"
        assert context["headers"] == ["列1", "列2"]
        assert context["show_index"] is True

        # 验证行数据
        assert "rows_data" in context
        assert len(context["rows_data"]) == 2

        # 验证样式
        assert "container_style" in context
        assert "table_style" in context
        assert "th_style" in context
        assert "index_th_style" in context
        assert "index_td_style" in context


class TestTableWidgetIntegration:
    """TableWidget集成测试类"""

    @pytest.mark.skipif(not PANDAS_AVAILABLE, reason="pandas not installed")
    def test_chaining_methods(self):
        """测试方法链式调用"""
        df = pd.DataFrame({"Name": ["项目A", "项目B"], "Status": ["进行中", "已完成"]})

        widget = (
            TableWidget("test_id")
            .set_dataframe(df)
            .set_title("项目状态表")
            .show_index(True)
            .set_striped(True)
            .set_bordered(True)
            .set_max_width("600px")
        )

        assert widget.widget_id == "test_id"
        assert widget.title == "项目状态表"
        assert widget._show_index is True
        assert widget._striped is True
        assert widget._bordered is True
        assert widget._max_width == "600px"

    @pytest.mark.skipif(not PANDAS_AVAILABLE, reason="pandas not installed")
    def test_full_workflow_with_dataframe(self):
        """测试DataFrame完整工作流程"""
        # 创建测试数据
        df = pd.DataFrame(
            {
                "项目名称": ["项目A", "项目B", "项目C"],
                "进度": [80, 100, 45],
                "状态": [
                    {"text": "进行中", "status": "info"},
                    {"text": "已完成", "status": "success"},
                    {"text": "延期", "status": "error"},
                ],
            }
        )

        widget = TableWidget()
        widget.set_title("项目进度报告")
        widget.set_dataframe(df)
        widget.show_index(True)
        widget.set_header_bg_color("#e6f3ff")

        # 获取模板上下文
        context = widget.get_template_context()

        # 验证数据处理
        assert context["title"] == "项目进度报告"
        assert context["headers"] == ["项目名称", "进度", "状态"]
        assert context["show_index"] is True
        assert len(context["rows_data"]) == 3

    def test_full_workflow_with_manual_data(self):
        """测试手动数据完整工作流程"""
        widget = TableWidget()

        # 手动设置表格
        widget.set_title("销售数据")
        widget.set_headers(["产品", "销量", "状态"])

        # 添加带状态的行
        status_cell = widget.add_status_cell("热销", StatusType.SUCCESS)
        widget.add_row(["产品A", "1000", status_cell])

        colored_cell = widget.add_colored_cell("滞销", "#ff6b6b", bold=True)
        widget.add_row(["产品B", "50", colored_cell])

        # 配置样式
        widget.set_striped(True)
        widget.set_bordered(True)
        widget.set_max_width("800px")

        # 获取模板上下文
        context = widget.get_template_context()

        # 验证完整配置
        assert context["title"] == "销售数据"
        assert len(context["rows_data"]) == 2
        assert context["headers"] == ["产品", "销量", "状态"]

    @pytest.mark.skipif(not PANDAS_AVAILABLE, reason="pandas not installed")
    def test_data_operations(self):
        """测试数据操作"""
        widget = TableWidget()

        # 创建初始DataFrame
        df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
        widget.set_dataframe(df)
        assert len(widget.dataframe) == 2

        # 添加数据行
        widget.add_data_row([5, 6])
        assert len(widget.dataframe) == 3

        # 清空数据
        widget.clear_data()
        assert widget.dataframe is None

        # 手动添加行
        widget.set_headers(["X", "Y"])
        widget.add_row(["a", "b"])
        widget.add_row(["c", "d"])
        assert len(widget.rows) == 2

        # 清空行
        widget.clear_rows()
        assert len(widget.rows) == 0

    def test_table_cell_integration(self):
        """测试TableCell集成"""
        widget = TableWidget()
        widget.set_headers(["名称", "状态", "优先级"])

        # 创建不同类型的单元格
        status_cell = TableCell("进行中", status=StatusType.INFO)
        priority_cell = TableCell("高", color="#ff0000", bold=True, align="center")

        widget.add_row(["任务A", status_cell, priority_cell])

        # 验证单元格数据
        row = widget.rows[0]
        assert row[0] == "任务A"
        assert isinstance(row[1], TableCell)
        assert row[1].status == StatusType.INFO
        assert isinstance(row[2], TableCell)
        assert row[2].bold is True
