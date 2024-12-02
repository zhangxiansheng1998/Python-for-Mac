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
        # cls.driver = webdriver.Chrome(options=Browser().browser_ui()) # 带UI界面启动
        cls.driver = webdriver.Chrome(options=Browser().browser_headless())  # 无头模式启动
        cls.obj = BasePage(cls.driver)
        cls.obj.implicitly_wait(15)
        cls.user = int(os.getenv('user', 1))  # 定义环境变量，可以动态的传递user的值，默认为1

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # @unittest.skip('unittest不执行这条测试用例')
    def test_1_login(self):
        """登录门线系统"""
        self.obj.max()
        self.obj.visit("http://mensvsp.thinkerx.com/admin/upIdCard/14596/edit?%2Fadmin%2FupIdCard%2F14596%2Fedit")
        self.obj.input((By.NAME, 'username'), "沈亚敏")
        self.obj.input((By.NAME, 'password'), "123456")
        self.obj.click((By.XPATH, "/html/body/div/div[2]/form/div[3]/div/button"))
        print("\n登录成功！")

    # @unittest.skip('unittest不执行这条测试用例')
    def test_2_generate_order(self):
        """修改收款信息"""
        self.obj.explicitly_wait((By.ID, 'id_card'), 10)
        self.obj.backspace_macos((By.ID, 'id_card'))
        self.obj.explicitly_wait((By.ID, 'bank_card'), 10)
        self.obj.backspace_macos((By.ID, 'bank_card'))
        print("\n页面上身份证和银行卡信息已清空！")
        if self.user == 1:
            self.obj.input((By.ID, 'id_card'), '36233019980509119X')
            self.obj.input((By.ID, 'bank_card'), '6217002000088747870')
            self.obj.click(
                (By.XPATH, '/html/body/div/div/section[2]/div/div/div/form/div[2]/div[2]/div[1]/button'))
            print('\n姓名：倪浩平')
            print('\n身份证信息：', self.obj.get_value((By.ID, 'id_card')))
            print('\n银行卡信息：', self.obj.get_value((By.ID, 'bank_card')))

        elif self.user == 2:
            self.obj.input((By.ID, 'id_card'), '410225199804123432')
            self.obj.input((By.ID, 'bank_card'), '6236682430004532667')
            self.obj.click(
                (By.XPATH, '/html/body/div/div/section[2]/div/div/div/form/div[2]/div[2]/div[1]/button'))
            print('\n姓名：王永康')
            print('\n身份证信息：', self.obj.get_value((By.ID, 'id_card')))
            print('\n银行卡信息：', self.obj.get_value((By.ID, 'bank_card')))

        elif self.user == 3:
            self.obj.input((By.ID, 'id_card'), '320482199610284613')
            self.obj.input((By.ID, 'bank_card'), '6217993000422695224')
            self.obj.click(
                (By.XPATH, '/html/body/div/div/section[2]/div/div/div/form/div[2]/div[2]/div[1]/button'))
            print('\n姓名：徐鹏')
            print('\n身份证信息：', self.obj.get_value((By.ID, 'id_card')))
            print('\n银行卡信息：', self.obj.get_value((By.ID, 'bank_card')))


if __name__ == '__main__':
    unittest.main()
