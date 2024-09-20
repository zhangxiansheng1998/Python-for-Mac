import unittest
from Gas_Station.page_object.LoginPage import LoginPage
from Gas_Station.base.browser import *
from Gas_Station.data.login_page_element import *


class Login(unittest.TestCase):

    loginpage = None
    driver = None

    @classmethod
    def setUpClass(cls):
        print('程序开始')
        cls.driver = webdriver.Chrome(options=Browser().browser_ui())             # 带UI界面启动
        #cls.driver = webdriver.Chrome(options=Browser().browser_headless())      # 无头模式启动
        cls.loginpage = LoginPage(cls.driver)
        cls.loginpage.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        print("\n")
        cls.driver.quit()
        print('程序结束')

    #@unittest.skip('unittest不执行这条测试用例')
    def test_1_login_fail(self):
        """搜索功能"""
        self.loginpage.login_without_sending_code('selenium')


if __name__ == '__main__':
    unittest.main()
