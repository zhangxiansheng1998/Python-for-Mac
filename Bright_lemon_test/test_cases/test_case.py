import time
import unittest
import pytest
from selenium import webdriver
from Bright_lemon_test.page_object.login_page import Loginpage
from ddt import ddt, file_data, data
from Bright_lemon_test.base.browser import *
from Bright_lemon_test.page_object.shop_page import Shoppage

@ddt
class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        print('程序开始')
        cls.driver = webdriver.Chrome(options=Browser().browser_ui())             # 带UI界面启动
        #cls.driver=webdriver.Chrome(options=Browser().browser_headless())      # 无头模式启动
        cls.loginpage = Loginpage(cls.driver)
        cls.chooseshop= Shoppage(cls.driver)
        print('已经执行完测试用例')

    @classmethod
    def tearDownClass(cls):
        print('程序结束')
        cls.driver.quit()


    #@unittest.skip('unittest不执行这条测试用例')

    @file_data('../data/login_page_data.yaml')
    def test1_login(self, username, password):
        try:
            self.loginpage.login(username,password)
            self.loginpage.enterinto_shop()  # 进入亮柠檬门店系统
        except Exception as e:
            print('报错信息:{}'.format(e))


    @unittest.skip('unittest不执行这条测试用例')
    def test2_add_client(self):
        self.chooseshop.choose_shop()
        self.chooseshop.create_client()

    @unittest.skip('unittest不执行这条测试用例')
    def test3_normal_process(self):
        self.chooseshop.registration_type_normal()
        self.chooseshop.normal_process()


if __name__ == '__main__':
    pytest.main(['-s','test_case_001.py'])
