import os
import re
import time
import hmac
import hashlib
import base64
import urllib.parse
import jenkins
import json
import urllib3
from urllib3.exceptions import InsecureRequestWarning

with open('result.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 初始化变量
order_numbers = []
failed_reasons = []
numbers = []
data = []
result = ""
# 遍历文件的每一行
for line_number, line in enumerate(lines, start=1):
    # 使用正则表达式提取订单号
    order_number_match = re.search(r'订单号: (.*),', line)
    if order_number_match:
        order_number = order_number_match.group(1)
        order_numbers.append(order_number)

    # 使用正则表达式提取失败原因
    failed_reason_match = re.search(r'失败原因: (.*)', line)
    if failed_reason_match:
        failed_reason = failed_reason_match.group(1)
        failed_reasons.append(failed_reason)

    # 生成序号
    number = line_number
    numbers.append(number)
    data.append(f"序号: {str(number)}, 订单号: {str(order_number)}, 失败原因: {failed_reason}")
    # print(f"序号: {str(number)}, 订单号: {str(order_number)}, 失败原因: {str(failed_reason)}")

# 钉钉推送

for item in data:
    result = result + item + "\n"

print(result)
print(type(result))
