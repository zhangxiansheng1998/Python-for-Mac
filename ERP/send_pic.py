import os
import subprocess
from datetime import datetime


def open_finder_directory(base_path):
    # 获取当天日期并格式化为 yyyy-mm-dd
    current_date = datetime.now().strftime("%Y-%m-%d")

    # 构建要打开的目录路径
    directory_path = os.path.join(base_path, current_date)

    # 检查目录是否存在，如果不存在则创建
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    # 使用subprocess打开Finder并导航到指定目录
    subprocess.run(["open", directory_path])

def run_applescript(script):
    try:
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, check=True)
        output = result.stdout.strip()  # 获取脚本执行的输出并去除首尾的空格和换行符
        return output
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return None



# 调用函数，传入基础目录
open_finder_directory("/Volumes/Disk/MyProject/ERP/picture/")
