from selenium.webdriver.common.by import By

'''
    '': (By.XPATH,''),
    # 
'''

button = {
    'goods_list': (By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div/div/p[1]'),    # 商品列表按钮

    'add_goods': (By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div/div/p[2]'),    # 新增商品按钮

    'goods_category': (By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div/div/p[3]')  # 商品分类按钮
}

goods_list = {
    'search_input_box': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div/div/input'),  # 搜索框
    'search_button': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/button[1]'),  # 查询按钮
    'reset_button': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/button[2]'),  # 重置按钮
}