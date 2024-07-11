"""
conf.py 路径 url
"""
import os
from datetime import datetime


today = datetime.today()  # 获取当前日期
month_formatted_date = today.strftime("%Y-%m")
formatted_date = today.strftime("%Y-%m-%d")  # 格式化日期为字符串，例如："2024-01-12"
project_path = "/Users/macbook_air/Desktop/MyProject/Gas_Station"
report_path = os.path.join(project_path,
                           f"/Users/macbook_air/Desktop/MyProject/Gas_Station/report/{month_formatted_date}/{formatted_date}/")
case_path = os.path.join(project_path, "test_cases")
