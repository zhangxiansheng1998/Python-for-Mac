from selenium.webdriver.common.by import By

'''
    '': (By.XPATH,''),
    # 
'''

button = {
    'shop_list': (By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div/div/p[1]'),
    # 店铺列表按钮
    'add_shop': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[1]/div[2]/button[1]')
    # 新增店铺按钮
}

shop_list = {
    'shop_status': (By.XPATH,
                    '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr['
                    '1]/td[5]/div/div/span'),
    # 营业状态开关
    'shop_details': (By.XPATH,
                     '//*[@id="main"]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[8]/div/button['
                     '1]/span/span'),
    # 查看详情
    'shop_details_return': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[1]/div[2]/button/span'),
    'today_income': (By.XPATH,
                     '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr['
                     '1]/td[8]/div/button[2]/span/span'),
    # 今日营业额
    'today_income_close': (By.XPATH, '//*[@id="main"]/div[2]/div[3]/div/div/header/button/i/svg'),
    # 今日营业额-关闭按钮
    'custom_income': (By.XPATH,
                      '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr['
                      '1]/td[8]/div/button[3]/span/span'),
    # 自定义收款
    'enter_amount': (By.XPATH, '/html/body/div[3]/div/div/div[2]/div[2]/div[1]/div/input'),
    # 自定义收款-金额输入框
    'custom_income_confirm': (By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]'),
    # 自定义收款-确认按钮
    'custom_income_cancel': (By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]'),
    # 自定义收款-取消按钮
    'custom_income_close': (By.XPATH, '/html/body/div[3]/div/div/div[1]/button'),
    # 自定义收款-关闭按钮
    'income_code': (By.XPATH,
                    '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr['
                    '1]/td[8]/div/button[4]/span/span'),
    # 收款码
    'shop_code': (By.XPATH,
                  '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr['
                  '1]/td[8]/div/button[5]/span/span'),
    # 店铺码
    'delete_shop': (By.XPATH,
                    '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr['
                    '1]/td[8]/div/button[6]/span/span'),
    # 注销店铺
    'get_code': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div/div/div/form/div[2]/div/button'),
    # 获取验证码
    'enter_code': (By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div/div/div/form/div['
                            '2]/div/div/div/input'),
    # 输入验证码
    'delete_shop_confirm': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div/div/footer/span/button['
                                      '2]/span'),
    # 注销店铺-确认注销按钮
    'delete_shop_cancel': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div/div/footer/span/button[1]'),
    # 注销店铺-取消按钮
    'delete_shop_close': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div/div/header/button/i/svg'),
    # 注销店铺-关闭按钮
    'add_shop_button': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[1]/div[2]/button[1]'),
    # 新增店铺按钮
    'refresh_shop_button': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[1]/div[2]/button[2]')
    # 刷新店铺按钮
}

add_shop = {
    'platform_zhujia': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/form/div[1]/div[2]/div[1]/label/span[1]'),
    # 平台类型-筑家工厂
    'platform_erp': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/form/div[1]/div[2]/div[2]/label/span[1]'),
    # 平台类型-erp
    'shop_name': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/form/div[2]/div/div[1]/div/input'),
    # 店铺名称
    'shop_type_1': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/form/div[3]/div[2]/div[1]/label/span[1]/span'),
    # 店铺类型-零售商
    'shop_type_2': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/form/div[3]/div[2]/div[2]/label/span[1]/span'),
    # 店铺类型-产品供应商
    'shop_type_3': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/form/div[3]/div[2]/div[3]/label/span[1]/span'),
    # 店铺类型-材料供应商
    'shop_type_4': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/form/div[3]/div[2]/div[4]/label/span[1]/span'),
    # 店铺类型-原材料供应商
    'server_phone': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/form/div[4]/div/div/div/input'),
    # 客服电话
    'logo': (By.CSS_SELECTOR, 'input[type=file]'),
    # logo
    'submit': (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[1]/div[2]/button')
    # 提交验证按钮

}
