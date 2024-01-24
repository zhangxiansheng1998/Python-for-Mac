import unittest
from BeautifulReport import BeautifulReport
from Jsfk.base.E_mail import *

def runall():
    now = time.strftime("%Y-%m-%d_%H-%M-%S")  # 获取当前时间
    report = report_path + now + ".html"  # 拼接报告绝对路径
    reportfile = open(report, "wb")  # 生成以当前时间为前缀的报告


    """使用unittest插件BeautifulReport生成的测试报告，样式较为美观，QQ、163、阿里云邮箱中不能正常显示样式，但是直接打开文件是可以正常显示样式的"""
    suite_tests = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
    # # "."表示当前目录，"*tests.py"匹配当前目录下所有tests.py结尾的用例
    BeautifulReport(suite_tests).report(filename='{htmlname}.html'.format(htmlname=now), description='UI自动化测试',report_dir='../report')
    # # description 对应html文件中的用例名称，log_path 表示html文件存放的位置


def Email():
    NewReport = new_report(report_path)
    send_mail(NewReport)


if __name__ == '__main__':
    runall()
    Email()
