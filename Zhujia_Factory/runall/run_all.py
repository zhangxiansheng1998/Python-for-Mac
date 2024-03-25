import sys

sys.path.append("/Users/macbook_air/Desktop/MyProject")  # 将目录加入环境变量，否则命令行下运行代码时会报错

import unittest
import os
from BeautifulReport import BeautifulReport
from Zhujia_Factory.base.E_mail import *
from Zhujia_Factory.config.conf import *


def create_folder_for_today():
    """在report目录下生成当天日期的目录"""
    # 获取当前日期
    today = datetime.today()
    # 格式化日期为字符串，例如："2024-01-12"
    month_formatted_date = today.strftime("%Y-%m")
    formatted_date = today.strftime("%Y-%m-%d")

    # 构建目录路径
    month_folder_path = os.path.join('../report', month_formatted_date)
    folder_path = os.path.join('../report', month_formatted_date, formatted_date)

    # 检查目录是否已经存在，如果不存在则创建
    if not os.path.exists(month_folder_path):
        os.makedirs(month_folder_path)
        print(f"文件夹'{month_formatted_date}'创建成功")

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"文件夹'{formatted_date}'创建成功")

def Runall():
    """生成测试报告"""
    create_folder_for_today()
    # now = time.strftime("%Y-%m-%d~%H-%M-%S")  # 获取当前时间
    today = datetime.today()  # 获取当前日期
    month_formatted_date = today.strftime("%Y-%m")
    formatted_date = today.strftime("%Y-%m-%d")  # 格式化日期为字符串，例如："2024-01-12"
    suite_tests = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
    # "*tests.py"匹配当前目录下所有tests.py结尾的用例
    BeautifulReport(suite_tests).report(filename='{htmlname}.html'.format(htmlname=now),
                                        description='WEB自动化测试报告',
                                        report_dir=f'../report/{month_formatted_date}/{formatted_date}')
    # description 对应html文件中的用例名称，log_path 表示html文件存放的位置


def Create_Email():
    """创建邮件正文中的html内容"""
    create_folder_for_today_two()
    NewReport = new_report(report_path)
    data = extract_test_summary_with_regex(NewReport)
    html_content = generate_html(data)
    save_html(html_content)


def Send_Email():
    """发送邮件"""
    NewReport = new_report(report_path)
    send_mail(NewReport)


if __name__ == '__main__':
    Runall()
    Create_Email()
    Send_Email()
