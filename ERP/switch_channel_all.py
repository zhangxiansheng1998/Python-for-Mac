import unittest
from Browser import *
from base_page import *
from selenium.webdriver.common.by import By


class TestCase(unittest.TestCase):
    obj = None
    driver = None

    @classmethod
    def setUpClass(cls):
        print('\n程序开始')
        cls.driver = webdriver.Chrome(options=Browser().browser_ui())  # 带UI界面启动
        #cls.driver = webdriver.Chrome(options=Browser().browser_headless())  # 无头模式启动
        cls.obj = BasePage(cls.driver)
        cls.obj.implicitly_wait(15)
        cls.channel = int(os.getenv('channel', 1))  # 定义环境变量，可以动态的传递channel的值，默认为1

    @classmethod
    def tearDownClass(cls):
        print('\n程序结束')
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
    def test_2_switch_channel_all(self):
        """修改支付渠道"""
        self.obj.click((By.XPATH, '//*[@id="menu"]/ul/ul/li[2]'))
        self.obj.click((By.XPATH, '/html/body/div[1]/div[2]/div[1]/ul/ul/li[2]/ul/li[1]'))
        self.obj.wait(2)
        self.obj.click((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div'))
        self.obj.wait(2)
        if self.channel == 1:
            channel_value = "江南农商行-汇锦微"
            self.obj.get_option_value("/html/body/div[2]/div[2]/div/div/div[1]/ul/li", "江南农商行-必答")
        elif self.channel == 2:
            channel_value = "江南农商行-必答"
            self.obj.get_option_value("/html/body/div[2]/div[2]/div/div/div[1]/ul/li", "江南农商行-汇锦微")
        self.obj.click((By.XPATH, '//*[@id="main"]/div/div[1]/div[2]/button[1]'))
        self.obj.wait(2)

        tr_number = 1

        while True:
            self.obj.click((By.XPATH, f'/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[{tr_number}]/td[11]/div/button[4]/span/span'))
            self.obj.click((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[5]/div/div/div/form/div/div/div/div/div[1]/div[2]'))
            self.obj.wait(1)
            self.obj.get_option_value("/html/body/div[2]/div[4]/div/div/div[1]/ul/li", channel_value)
            self.obj.wait(1)
            self.obj.click((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[5]/div/div/footer/button'))
            self.obj.wait(1)
            """判断修改成功后的文字提示"""
            if self.obj.get_text((By.XPATH, '/html/body/div[3]/p')) == "已修改进支付渠道":
                print("\n渠道修改成功！")
            elif self.obj.get_text((By.XPATH, '/html/body/div[3]/p')) == "失败,服务器内部错误":
                print("\n渠道修改失败！")
                tr_number += 1
            elif self.obj.get_text((By.XPATH, '/html/body/div[4]/p')) == "修改进支付渠道失败":
                print("\n渠道修改失败！")
                tr_number += 1


if __name__ == '__main__':
    unittest.main()