from selenium.webdriver.common.by import By
from Zhujia_Factory.config.read_ini import *

website = \
    {
        'url': get_ini_value('environment', 'Prd')
    }

login_element = \
    {
        'username': (By.XPATH, '/html/body/div/div/div/div[2]/form/div[1]/div/div/div/input'),  # 手机号输入框

        'send_code': (By.XPATH, '/html/body/div/div/div/div[2]/form/div[2]/div/button'),  # 获取验证码按钮

        'input_code': (By.XPATH, '/html/body/div/div/div/div[2]/form/div[2]/div/div/div/input'),  # 验证码输入框

        'login_button': (By.XPATH, '//*[@id="app"]/div/div/div[2]/form/button'),  # 登录按钮

        'assert_box': (By.XPATH, '/html/body/div[2]/p')  # 文本框(断言)
    }
