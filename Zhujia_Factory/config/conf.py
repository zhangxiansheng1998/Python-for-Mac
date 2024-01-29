"""
conf.py 路径 url
"""
import os
from datetime import datetime


def choose_path():
    while True:
        try:
            today = datetime.today()  # 获取当前日期
            formatted_date = today.strftime("%Y-%m-%d")  # 格式化日期为字符串，例如："2024-01-12"
            choice = int(input("请输入要运行的路径【1】本地【2】外接硬盘:"))
            if choice == 1:
                project_path = "/Users/macbook_air/Desktop/backup/MyProject/Zhujia_Factory"
                report_path = os.path.join(project_path,
                                           f"/Users/macbook_air/Desktop/backup/MyProject/Zhujia_Factory/report/{formatted_date}/")
                case_path = os.path.join(project_path, "test_cases")
                return project_path, report_path, case_path
            elif choice == 2:
                project_path = "/Volumes/Disk/MyProject/Zhujia_Factory"
                report_path = os.path.join(project_path,
                                           f"/Volumes/Disk/MyProject/Zhujia_Factory/report/{formatted_date}/")
                case_path = os.path.join(project_path, "test_cases")
                return project_path, report_path, case_path
            else:
                print("输入的数字不是1或2，请重新输入！")
        except ValueError:
            print("输入的不是数字，请重新输入！")


"""选择在本地还是外接硬盘上跑代码"""
project_path, report_path, case_path = choose_path()
