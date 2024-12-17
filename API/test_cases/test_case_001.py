import requests
import json
from prettytable import PrettyTable


def Run_test():
    file = '../data/test_case_001.json'

    # 读取JSON文件中的数据
    with open(file, 'r') as file:
        requests_data = json.load(file)

    # 初始化计数器
    request_count = 0

    # 循环遍历每个请求数据并发送请求
    for req_data in requests_data:
        request_count += 1  # 每次循环递增计数器
        url = req_data['Url']
        method = req_data['Method']
        if method.upper() == 'GET':
            response = requests.get(url, params=req_data['RequestBody'])
        elif method.upper() == 'POST':
            response = requests.post(url, json=req_data['RequestBody'])
        elif method.upper() == 'PUT':
            response = requests.put(url, json=req_data['RequestBody'])
        elif method.upper() == 'DELETE':
            response = requests.delete(url, json=req_data['RequestBody'])
        else:
            print(f"暂不支持的HTTP方法: {method}")
            continue  # 跳过不支持的方法

        # 针对响应内容进行判断
        expect_result = req_data['ExpectResult']
        actual_result = json.loads(response.text)

        def is_subset(expect_result, actual_result):
            # 遍历expect_result中的每个键值对
            for key, value in expect_result.items():
                # 如果键不存在于actual_result中，或者值不相等，则返回"结果不一致"
                if key not in actual_result or actual_result[key] != value:
                    return "结果不一致"
            # 如果所有键值对都存在于actual_result中，则返回"结果一致"
            return "结果一致"

        # 针对失败的订单进行打印 
        Failed_Results = PrettyTable(["Number", "Url", "Method", "RequestBody", "ExpectCode", "ActualCode"])
        Failed_Results.align["Number"] = "l"
        Failed_Results.padding_width = 1
        Failed_Results.add_row([request_count, req_data['Url'], req_data['Method'], req_data['RequestBody'], req_data['ExpectCode'], response.status_code])

        if response.status_code == int(req_data['ExpectCode']) and is_subset(expect_result, actual_result) == "结果一致":
            print(f"断言成功：实际结果与预期结果一致！")

        elif response.status_code == int(req_data['ExpectCode']) and is_subset(expect_result, actual_result) == "结果不一致":
            print(f"断言失败：实际结果与预期结果不一致！")
            print(Failed_Results)

        elif response.status_code != int(req_data['ExpectCode']) and is_subset(expect_result, actual_result) == "结果一致":
            print(f"断言失败：ExpectCode与ActualCode不一致！")
            print(Failed_Results)
        else:
            print(f"断言失败：实际结果与ActualCode都不一致！")
            print(Failed_Results)


Run_test()