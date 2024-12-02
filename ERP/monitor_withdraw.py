import unittest
from Browser import *
from base_page import *
from selenium.webdriver.common.by import By
from datetime import datetime


class TestCase(unittest.TestCase):

    obj = None
    driver = None
    zj_start_time = "15:00:00" # 中金渠道的自动提现时间
    zj_end_time = "15:10:00" # 中金渠道的自动提现时间
    jn_start_time = "15:30:00" # 中金渠道的自动提现时间
    jn_end_time = "15:40:00" # 江南渠道的自动提现时间

    @classmethod
    def setUpClass(cls):
        print('\n程序开始')
        cls.driver = webdriver.Chrome(options=Browser().browser_ui()) # 带UI界面启动
        #cls.driver = webdriver.Chrome(options=Browser().browser_headless())  # 无头模式启动
        cls.obj = BasePage(cls.driver)
        cls.obj.implicitly_wait(15)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # @unittest.skip('unittest不执行这条测试用例')
    def test_1_login(self):
        """登录材神金服系统"""
        self.obj.max()
        self.obj.visit("http://pay.huijinwei.com/admin/#/login")
        self.obj.input((By.XPATH, '/html/body/div[1]/div/div/div[2]/form/div[1]/div/div/div/input'), "nihaoping")
        self.obj.input((By.XPATH, '/html/body/div[1]/div/div/div[2]/form/div[2]/div/div/div/input'), "thinkerx@123!")
        self.obj.click((By.XPATH, "/html/body/div[1]/div/div/div[2]/form/button"))
        print("\n登录成功！")

    # @unittest.skip('unittest不执行这条测试用例')
    def test_2_zj_withdraw(self):
        global failed_orders
        self.obj.click((By.XPATH, '//*[@id="menu"]/ul/ul/li[5]'))
        self.obj.wait(1)
        self.obj.click((By.XPATH, '/html/body/div[1]/div[2]/div[1]/ul/ul/li[5]/ul/li[2]'))
        self.obj.wait(3)
        self.obj.click((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[5]/div/div/div[1]/div[2]'))
        self.obj.wait(3)
        self.obj.get_li_value('el-scrollbar__view el-select-dropdown__list', '自动提现')
        self.obj.click((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/input[1]'))
        self.obj.backspace_macos((By.XPATH, '/html/body/div[2]/div[4]/div/div[1]/div/div[1]/span[1]/span[2]/div[1]/div/input'))
        self.obj.input((By.XPATH, '/html/body/div[2]/div[4]/div/div[1]/div/div[1]/span[1]/span[2]/div[1]/div/input'),self.zj_start_time)
        self.obj.click((By.XPATH, '/html/body/div[2]/div[4]/div/div[1]/div/div[1]/span[1]/span[2]/div[2]/div[2]/button[2]'))
        self.obj.backspace_macos((By.XPATH, '/html/body/div[2]/div[4]/div/div[1]/div/div[1]/span[3]/span[2]/div/div/input'))
        self.obj.backspace_macos((By.XPATH, '/html/body/div[2]/div[4]/div/div[1]/div/div[1]/span[1]/span[2]/div[1]/div/input'))
        self.obj.click((By.XPATH, '/html/body/div[2]/div[4]/div/div[1]/div/div[1]/span[1]/span[2]/div[2]/div[2]/button[2]'))
        self.obj.backspace_macos((By.XPATH, '/html/body/div[2]/div[4]/div/div[1]/div/div[1]/span[3]/span[2]/div/div/input'))
        self.obj.input((By.XPATH, '/html/body/div[2]/div[4]/div/div[1]/div/div[1]/span[3]/span[2]/div/div/input'),self.zj_end_time)
        self.obj.wait(1)
        self.obj.click((By.XPATH, '/html/body/div[2]/div[4]/div/div[1]/div/div[1]/span[3]/span[2]/div[2]/div[2]/button[2]'))
        self.obj.click((By.XPATH, '/html/body/div[2]/div[4]/div/div[2]/button[2]/span'))
        self.obj.wait(2)
        self.obj.click((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/button[1]'))
        self.obj.wait(2)


if __name__ == '__main__':
    unittest.main()
