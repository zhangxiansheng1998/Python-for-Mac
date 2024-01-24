import unittest
import pytest
from appium import webdriver
from Fudafu.base.driver import *
from Fudafu.base.appium_base_page import *
from Fudafu.page_object.login_page import LoginPage


class Login(unittest.TestCase):
    basepage = None
    driver = None

    @classmethod
    def setUpClass(cls):
        print('程序开始')
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Driver().ios16_driver_property())
        # cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Driver().ios17_driver_property())
        cls.basepage = BasePage(cls.driver)
        cls.basepage.implicitly_wait(10)  # 需要设置隐式等待，否则可能会报错，全局有效，只需设置一次
        cls.loginpage = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        print('程序结束')
        cls.driver.quit()

    #@unittest.skip("Skip the case")
    def test_1_login_success(self):
        """登录成功"""
        self.loginpage.login_success_with_code()

    @unittest.skip("Skip the case")
    def test_2_login_fail(self):
        """登录失败"""
        self.loginpage.login_fail_with_code('13321105094','123456')


if __name__ == "__main__":
    unittest.main()
