from selenium.webdriver.common.by import By

'''
    '': (By.XPATH,''),
    # 
'''

button = \
{
    'goods_list': (By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div/div/p[1]'),    # 商品列表按钮

    'add_goods': (By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div/div/p[2]'),    # 新增商品按钮

    'goods_category': (By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div/div/p[3]')  # 商品分类按钮
}

goods_list = \
{
    'search_input_box': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div/div/input'),  # 搜索框

    'search_button': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/button[1]'),  # 查询按钮

    'reset_button': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/button[2]'),  # 重置按钮

    'goods_text': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[5]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[2]/div'),  # 商品名称(断言)

    'select_goods': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[5]/div[1]/div[2]/table/thead/tr/th[1]/div/label/span/span'),  # 选中商品

    'multiple_times_shelf': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[4]/button[2]'),  # 批量上架/下架

    'assert_box': (By.XPATH, '/html/body/div[3]/p'),  # 文本框(断言)

    'on_sale': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]'),  # 在售中

    'off_sale': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[3]'),  # 已下架
}

add_goods = \
{
    'goods_category': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/form[1]/div[2]/div/div/div/div/input'),    # 商品分类下拉框

    'goods_category_1': (By.XPATH, '/html/body/div[2]/div[3]/div/div/div[1]/ul/li[1]/span'),     # 商品分类下拉框-铝型材

    'goods_category_2': (By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div[1]/ul/li[1]/span'),     # 商品分类下拉框-铝合金

    'goods_category_3': (By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/div[1]/ul/li[1]/span'),     # 商品分类下拉框-铝制用品

    'goods_name': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/form[1]/div[3]/div/div[1]/div/input'),       # 商品名称

    'goods_specification': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[8]/form/div/div/div[1]/div/input'),       # 商品规格

    'add_inventory': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[11]/div[2]/div[2]/span[2]'),     # 新增库存

    'goods_price': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[10]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[3]/div/div/div/input'),  # 商品报价-价格

    'goods_unit': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[10]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[4]/div/div/div/input'),   # 商品报价-单位名称

    'confirm': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[1]/button'),  # 确认新增

    'assert_box': (By.XPATH, '/html/body/div[3]/p')   # 文本框(断言)
}