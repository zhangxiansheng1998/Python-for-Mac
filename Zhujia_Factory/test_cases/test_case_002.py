import unittest
from Zhujia_Factory.page_object.LoginPage import LoginPage
from Zhujia_Factory.page_object.ShopManagement import ShopManagement
from Common_File.Browser import *
from Zhujia_Factory.data.login_page_element import *


class Shop(unittest.TestCase):

    driver = None
    loginpage = None

    @classmethod
    def setUpClass(cls):
        print('程序开始')
        #cls.driver = webdriver.Chrome(options=Browser().browser_ui())         # 带UI界面启动
        cls.driver = webdriver.Chrome(options=Browser().browser_headless())  # 无头模式启动
        cls.loginpage = LoginPage(cls.driver)
        cls.shoppage = ShopManagement(cls.driver)
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
        self.loginpage.assert_text_equal('登录成功', login_element['assert_box'])

    #@unittest.skip('unittest不执行这条测试用例')
    def test_2_add_shop(self):
        """新增筑家工厂店铺"""
        self.shoppage.add_zhujia_shop()

    #@unittest.skip('unittest不执行这条测试用例')
    def test_3_check_details(self):
        """查看店铺的详情信息"""
        self.shoppage.check_details()

    #@unittest.skip('unittest不执行这条测试用例')
    def test_4_today_income(self):
        """查看今日营业额"""
        self.shoppage.today_income()

    #@unittest.skip('unittest不执行这条测试用例')
    def test_5_custom_income(self):
        """自定义输入收款金额"""
        self.shoppage.custom_income()

    #@unittest.skip('unittest不执行这条测试用例')
    def test_6_income_code(self):
        """查看店铺的收款码"""
        self.shoppage.income_code()

    #@unittest.skip('unittest不执行这条测试用例')
    def test_7_shop_code(self):
        """查看店铺码"""
        self.shoppage.shop_code()


if __name__ == '__main__':
    unittest.main()
