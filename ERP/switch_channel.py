import unittest
from Browser import *
from base_page import *
from selenium.webdriver.common.by import By


class TestCase(unittest.TestCase):
    obj = None
    driver = None

    name = input("请输入要修改的用户名称:")
    
    while True:
        try:
            channel = int(input("请输入修改后的渠道名称【1】中金【2】江南农商行-必答【3】江南农商行-汇锦微:"))
            if channel in [1, 2, 3]:
                break  # 如果输入合法数字，退出循环
            else:
                print("输入错误，请重新输入！")
        except ValueError:
            print("输入错误，请重新输入！")

    @classmethod
    def setUpClass(cls):
        print('\n程序开始')
        #cls.driver = webdriver.Chrome(options=Browser().browser_ui())  # 带UI界面启动
        cls.driver = webdriver.Chrome(options=Browser().browser_headless())  # 无头模式启动
        cls.obj = BasePage(cls.driver)
        cls.obj.implicitly_wait(15)

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
    def test_2_switch_channel(self):
        """修改支付渠道"""
        self.obj.click((By.XPATH, '//*[@id="menu"]/ul/ul/li[2]'))
        self.obj.click((By.XPATH, '/html/body/div[1]/div[2]/div[1]/ul/ul/li[2]/ul/li[1]'))
        self.obj.wait(2)
        self.obj.input((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/div/div/input'), self.name)
        self.obj.click((By.XPATH, '//*[@id="main"]/div/div[1]/div[2]/button[1]'))

        current_channel = self.obj.get_text((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[6]/div'))

        """渠道不同，修改渠道的按钮位置也有所不同，需要进行判断"""
        if current_channel == '中金':
            self.obj.click((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[9]/div/button[4]/span/span'))
        else:
            self.obj.click((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[9]/div/button[3]/span/span'))

        self.obj.click((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[4]/div/div/div/form/div/div/div/div/div/div/input'))
        
        if self.channel == 1:
            self.obj.get_li_value('el-scrollbar__view el-select-dropdown__list', '中金')
            self.new_current_channel = '【中金】'

        elif self.channel == 2:
            self.obj.get_li_value('el-scrollbar__view el-select-dropdown__list', '江南农商行-必答')
            self.new_current_channel = '【江南农商行-必答】'

        elif self.channel == 3:
            self.obj.get_li_value('el-scrollbar__view el-select-dropdown__list', '江南农商行-汇锦微')
            self.new_current_channel = '【江南农商行-汇锦微】'

        self.obj.wait(1)
        self.obj.click((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[4]/div/div/footer/button'))
        self.obj.wait(1)
        print(f'支付渠道已切换成{self.new_current_channel}')


if __name__ == '__main__':
    unittest.main()
