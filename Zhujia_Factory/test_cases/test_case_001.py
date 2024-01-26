import unittest
import pytest
from Zhujia_Factory.page_object.login_page import LoginPage
from Common_File.Browser import *
from Zhujia_Factory.data.login_page_element import *


class Login(unittest.TestCase):

    loginpage = None
    driver = None

    @classmethod
    def setUpClass(cls):
        print('程序开始')
        #cls.driver = webdriver.Chrome(options=Browser().browser_ui())             # 带UI界面启动
        cls.driver = webdriver.Chrome(options=Browser().browser_headless())      # 无头模式启动
        cls.loginpage = LoginPage(cls.driver)
        cls.loginpage.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        print("\n")
        cls.driver.quit()
        print('程序结束')

    #@unittest.skip('unittest不执行这条测试用例')
    def test_1_login_success(self):
        """使用万能验证码的手机号登录系统"""
        self.loginpage.login_without_sending_code('18662832373', '111111')
        self.loginpage.wait(1)
        self.loginpage.assert_text_euqal('登录成功', assert_element['assert_box'])

    #@unittest.skip('unittest不执行这条测试用例')
    def test_2_login_fail(self):
        """不发送验证码登录系统"""
        self.loginpage.login_without_sending_code('17320509658', '111111')
        self.loginpage.wait(3)
        self.loginpage.assert_text_euqal('验证码失效,请先发送验证码', assert_element['assert_box'])

    #@unittest.skip('unittest不执行这条测试用例')
    def test_3_login_fail(self):
        """发送验证码，但是输入错误的验证码登录系统"""
        self.loginpage.login_with_sending_code('15180381485', '111111')
        self.loginpage.wait(3)
        self.loginpage.assert_text_euqal('验证码错误', assert_element['assert_box'])


if __name__ == '__main__':
    pytest.main(['-s', 'test_case_001.py'])
