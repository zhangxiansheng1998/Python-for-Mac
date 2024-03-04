import unittest
from appium import webdriver
from Appium.base.driver import *
from Appium.base.appium_base_page import BasePage
from Appium.page_object.login_page import LoginPage
from Appium.page_object.payment_code_page import PaymentCodePage


class PaymentCode(unittest.TestCase):
    basepage = None
    driver = None

    @classmethod
    def setUpClass(cls):
        print('程序开始')
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Driver().ios16_driver_property())
        # cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Driver().ios17_driver_property())
        cls.basepage = BasePage(cls.driver)
        cls.basepage.implicitly_wait(15) # 需要设置隐式等待，否则可能会报错，全局有效，只需设置一次
        cls.loginpage = LoginPage(cls.driver)
        cls.paymentcode = PaymentCodePage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        print('程序结束')
        cls.driver.quit()

    #@unittest.skip("Skip the case")
    def test_1_payment_code(self):
        """设置固定金额，并保存收款码"""
        self.loginpage.check_login_in_status()
        self.paymentcode.set_amount_and_save_code(13.68)

    @unittest.skip("Skip the case")
    def test_2_payment_code(self):
        """切换店铺收款码并保存"""
        self.paymentcode.change_shop_and_save_code()

    @unittest.skip("Skip the case")
    def test_3_payment_code(self):
        """清除金额"""
        self.paymentcode.clear_amount()


if __name__ == "__main__":
    unittest.main()
