import requests
import json
from prettytable import PrettyTable


def send_request(url, method, dataformat, request_body):
    """
    发送HTTP请求
    :param url: 请求的URL
    :param method: 请求方法（GET, POST, PUT, DELETE）
    :param dataformat: 数据格式（JSON, FORM）
    :param request_body: 请求体
    :return: 响应对象
    """
    try:
        if method.upper() == 'GET':
            response = requests.get(url, params=request_body)
        elif method.upper() == 'POST' and dataformat.upper() == 'JSON':
            response = requests.post(url, json=request_body)
        elif method.upper() == 'POST' and dataformat.upper() == 'FORM':
            response = requests.post(url, data=request_body)  # 注意这里使用data而不是params
        elif method.upper() == 'PUT':
            response = requests.put(url, json=request_body)
        elif method.upper() == 'DELETE':
            response = requests.delete(url, json=request_body)
        else:
            raise ValueError(f"暂不支持的HTTP方法: {method}")
        return response
    except requests.RequestException as e:
        print(f"请求失败: {e}")
        return None


def compare_results(expect_result, actual_result):
    """
    比较预期结果和实际结果
    :param expect_result: 预期结果（字典）
    :param actual_result: 实际结果（字典）
    :return: 比较结果（字符串）
    """
    for key, value in expect_result.items():
        if key not in actual_result or actual_result[key] != value:
            return "结果不一致"
    return "结果一致"


def run_test():
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
        dataformat = req_data['DataFormat']
        requestbody = req_data['RequestBody']
        rsp_data = send_request(url, method, dataformat, requestbody)

        # 针对响应内容进行判断
        ExpectResult = req_data['ExpectResult']
        ActualResult = json.loads(rsp_data.text)

        # 针对失败的订单进行打印
        Failed_Results = PrettyTable(["Number", "Url", "Method", "RequestBody", "ExpectCode", "ActualCode"])
        Failed_Results.align["Number"] = "l"
        Failed_Results.padding_width = 1
        Failed_Results.add_row([request_count, req_data['Url'], req_data['Method'], req_data['RequestBody'], req_data['ExpectCode'], rsp_data.status_code])

        if rsp_data.status_code == int(req_data['ExpectCode']) and compare_results(ExpectResult, ActualResult) == "结果一致":
            print(f"断言成功：实际结果与预期结果一致！")
        elif rsp_data.status_code == int(req_data['ExpectCode']) and compare_results(ExpectResult, ActualResult) == "结果不一致":
            print(f"断言失败：实际结果与预期结果不一致！")
            print("ExpectResult:", ExpectResult)
            print("ActualResult:", ActualResult)
        elif rsp_data.status_code != int(req_data['ExpectCode']) and compare_results(ExpectResult, ActualResult) == "结果一致":
            print(f"断言失败：ExpectCode与ActualCode不一致！")
            print(Failed_Results)
        else:
            print(f"断言失败：实际结果与ActualCode都不一致！")
            print(Failed_Results)
            print("ExpectResult:", ExpectResult)
            print("ActualResult:", ActualResult)


run_test()
