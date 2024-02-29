import re

# 打开文件并读取内容
with open('result.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 初始化变量
order_numbers = []
failed_reasons = []
numbers = []

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

    # 输出结果
    #print(f"序号: {number}, 订单号: {order_number}, 失败原因: {failed_reason}")
    #print(f"序号: {str(number)}, 订单号: {str(order_number)}, 失败原因: {failed_reason}")
    result = []
    result.append(f"序号: {str(number)}, 订单号: {str(order_number)}, 失败原因: {failed_reason}")

print(numbers)
print(order_numbers)
print(failed_reasons)
