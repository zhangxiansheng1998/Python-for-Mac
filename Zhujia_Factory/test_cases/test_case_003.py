import unittest
from Zhujia_Factory.page_object.LoginPage import LoginPage
from Zhujia_Factory.page_object.GoodsManagement import GoodsManagement
from Common_File.Browser import *
from Zhujia_Factory.data.login_page_element import *


class Goods(unittest.TestCase):

    driver = None
    loginpage = None

    @classmethod
    def setUpClass(cls):
        print('程序开始')
        #cls.driver = webdriver.Chrome(options=Browser().browser_ui())         # 带UI界面启动
        cls.driver = webdriver.Chrome(options=Browser().browser_headless())  # 无头模式启动
        cls.loginpage = LoginPage(cls.driver)
        cls.goodspage = GoodsManagement(cls.driver)
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
        self.loginpage.assert_text_euqal('登录成功', login_element['assert_box'])

    #@unittest.skip('unittest不执行这条测试用例')
    def test_2_search_goods(self):
        """查询商品信息"""
        self.goodspage.search_goods()

    #@unittest.skip('unittest不执行这条测试用例')
    def test_3_shelf_goods(self):
        """上下架商品"""
        self.goodspage.shelf_goods()

    #@unittest.skip('unittest不执行这条测试用例')
    def test_4_add_goods(self):
        """新增商品"""
        self.goodspage.add_goods()


if __name__ == '__main__':
    unittest.main()