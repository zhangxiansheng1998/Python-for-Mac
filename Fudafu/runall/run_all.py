import unittest
from BeautifulReport import BeautifulReport
from Fudafu.base.E_mail import *
from Fudafu.config.conf import *
import os
from datetime import datetime
from Fudafu.base.generate_email_template import *


def create_folder_for_today():
    """在report目录下生成当天日期的目录"""
    # 获取当前日期
    today = datetime.today()
    # 格式化日期为字符串，例如："2024-01-12"
    formatted_date = today.strftime("%Y-%m-%d")

    # 构建目录路径
    folder_path = os.path.join('../report', formatted_date)

    # 检查目录是否已经存在，如果不存在则创建
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"文件夹'{formatted_date}'创建成功")


def Runall():
    create_folder_for_today()
    now = time.strftime("%Y-%m-%d~%H-%M-%S")  # 获取当前时间
    today = datetime.today()  # 获取当前日期
    formatted_date = today.strftime("%Y-%m-%d")  # 格式化日期为字符串，例如："2024-01-12"

    """使用unittest插件BeautifulReport生成的测试报告，样式较为美观，QQ、163、阿里云邮箱中不能正常显示样式，但是直接打开文件是可以正常显示样式的"""
    suite_tests = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
    # # "."表示当前目录，"*tests.py"匹配当前目录下所有tests.py结尾的用例
    BeautifulReport(suite_tests).report(filename='{htmlname}.html'.format(htmlname=now),
                                        description='APP自动化测试报告',
                                        report_dir=f'../report/{formatted_date}')
    # # description 对应html文件中的用例名称，log_path 表示html文件存放的位置


def Create_Email():
    create_folder_for_today_two()
    NewReport = new_report(report_path)
    data = extract_test_summary_with_regex(NewReport)
    html_content = generate_html(data)
    save_html(html_content)


def Send_Email():
    NewReport = new_report(report_path)
    send_mail(NewReport)


if __name__ == '__main__':
    Runall()
    Create_Email()
    Send_Email()
