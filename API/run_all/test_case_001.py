import requests
import json

file = '../data/test_suit_001.json'

# 读取JSON文件中的数据
with open(file, 'r') as file:
    requests_data = json.load(file)

# 初始化计数器
request_count = 0

# 循环遍历每个请求数据并发送请求
for req_data in requests_data:
    request_count += 1  # 每次循环递增计数器
    print(f'【test_suit_001.json】第{request_count}个请求')
    url = req_data['url']
    method = req_data['method']
    if method.upper() == 'POST':
        response = requests.post(url, json=req_data['data'])
    elif method.upper() == 'GET':
        response = requests.get(url, params=req_data['params'])
    else:
        print(f"暂不支持的HTTP方法: {method}")
        continue  # 跳过不支持的方法

    # 输出响应内容或进行其他处理
    print(response.text)
    print("==============================================================================================================================")