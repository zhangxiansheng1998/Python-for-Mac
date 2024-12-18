import pytest
import json

# 假设你的 JSON 文件是这样的
json_data = '''
[
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]
'''

# 解析 JSON 数据
data_list = json.loads(json_data)

# 使用 pytest.mark.parametrize 来参数化测试函数
# 这里我们通过解包的方式将 data_list 中的每个字典作为参数传递给测试函数
@pytest.mark.parametrize("data", data_list)
def test_json_data(data):
    # 在测试函数中使用传入的数据
    # 假设你有一个函数需要这些数据作为输入
    # 这里我们只是简单地检查数据是否存在
    print(data['id'])
    # 你可以根据实际需求添加更多的断言或测试逻辑

# 如果你想要直接从命令行运行 pytest，可以添加一个 main 函数
# 但通常不需要这样做，因为你可以直接在命令行中运行 pytest
# pytest 会自动发现并运行所有以 test_ 开头的函数或文件
if __name__ == "__main__":
    pytest.main(['-s','test_allure.py'])
