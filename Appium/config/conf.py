"""
conf.py 路径 url
"""
import os
from datetime import datetime


today = datetime.today()  # 获取当前日期
formatted_date = today.strftime("%Y-%m-%d")  # 格式化日期为字符串，例如："2024-01-12"
project_path = "/Users/macbook_air/Desktop/MyProject/Appium"
report_path = os.path.join(project_path,
                           f"/Users/macbook_air/Desktop/MyProject/Appium/report/{formatted_date}/")
case_path = os.path.join(project_path, "test_cases")
