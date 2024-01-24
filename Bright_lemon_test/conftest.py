import pytest
from py._xmlgen import html
from datetime import datetime
"""
控制pytest插件生成的HTML报告的样式文件，位置位于项目的根目录下
"""

@pytest.mark.parametrize
def pytest_configure(config):
    config._metadata.pop("JAVA_HOME") # 删除 java_home
    config._metadata.pop("Packages") #删除 {"pluggy": "1.0.0", "py": "1.11.0", "pytest": "6.2.5"}的值
    config._metadata.pop("Platform") # 删除平台名称
    config._metadata.pop("Plugins") # 删除pytest插件名
    config._metadata.pop("Python") # 删除python版本
    config._metadata["类型"] = "UI自动化测试"
    config._metadata["项目名称"] = "亮柠檬系统" # 添加项目名称
    config._metadata["项目网址"] = "https://jsfk-console-test.bigvisiontech.com" # 添加接口地址


@pytest.mark.parametrize
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门：质量部")])
    prefix.extend([html.p("测试人员：倪浩平")])


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(0, html.th("结果"))  # 表头添加result
    cells.insert(1, html.th("描述"))  # 表头添加Description
    cells.insert(2, html.th("结束时间", class_="sortable time", col="time"))
    cells.insert(3, html.th("模块名称"))
    cells.insert(4,html.th("所用时间"))
    cells.pop(-4)#删除因输入中文而多出来的单元格
    cells.pop(-3)
    cells.pop(-2)
    cells.pop(-1)


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))  # 表头对应的内容
    cells.insert(2, html.td(datetime.now(), class_="col-time"))
    cells.pop(-1)  # 删除link


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):  # Description取值为用例说明__doc__
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")