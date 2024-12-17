

expect_result = {'expire': 43200,'token': '111'}

actual_result = {'token': 'eyJ0eXAiOsvJpOIGtbUGgQ', 'expire': 43200}


def is_subset(expect_result, actual_result):
    # 遍历expect_result中的每个键值对
        for key, value in expect_result.items():
            # 如果键不存在于actual_result中，或者值不相等，则返回False
            if key not in actual_result or actual_result[key] != value:
                print(key )
                return "失败"
        # 如果所有键值对都存在于actual_result中，则返回True
        return "成功"

result = is_subset(expect_result, actual_result)
print(result)
