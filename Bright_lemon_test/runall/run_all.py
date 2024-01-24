import unittest
import pytest
from Bright_lemon_test.base.E_mail import *
from BeautifulReport import BeautifulReport
import HTMLTestRunner
import ddt

def runall():
    now = time.strftime("%Y-%m-%d_%H-%M-%S")  # 获取当前时间
    report = report_path + now + ".html"  # 拼接报告绝对路径
    reportfile = open(report, "wb")  # 生成以当前时间为前缀的报告

    """使用unittest中的HTMLTestRunner生成的测试报告，样式较为简单，QQ、阿里云邮箱不能正常显示样式，但163邮箱可以正常显示样式"""
    dis = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=reportfile,
        title='亮柠檬系统UI自动化测试报告',
        description='执行结果')
    runner.run(dis)

    """使用pytest自带的插件生成的测试报告，样式较为简单，样式较为简单，QQ、163、阿里云邮箱邮箱可以正常显示样式"""

    # pytest.main(['-s', 'E:/pycharm/Bright_lemon_test/test_cases', '--html=../report/{filename}.html'.format(
    # filename=now)])
    # 执行文件夹下的所有.py文件，路径写到上级目录即可 注意：只有这种方式是通过pytest生成的测试报告，只有这种方法才会执行语句@pytest.mark.skip(
    # )，跳过测试用例的执行，其他两种方法对语句@pytest.mark.skip()是不生效的，依然会执行测试用例

    """使用unittest插件BeautifulReport生成的测试报告，样式较为美观，QQ、163、阿里云邮箱中不能正常显示样式，但直接打开文件是可以正常显示的"""
    # suite_tests = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
    # # "."表示当前目录，"*tests.py"匹配当前目录下所有tests.py结尾的用例
    # BeautifulReport(suite_tests).report(filename='{htmlname}.html'.format(htmlname=now), description='UI自动化测试',
    #                                     report_dir='../report')
    # # description 对应html文件中的用例名称，report_dir 表示html文件存放的位置


def Email():
    NewReport = new_report(report_path)
    send_mail(NewReport)


if __name__ == '__main__':
    runall()
    Email()
