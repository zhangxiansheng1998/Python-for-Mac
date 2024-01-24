import unittest
from Browser import *
from base_page import *
from selenium.webdriver.common.by import By
import random

while True:
    try:
        # 定义订单生成的个数
        total_orders = int(input("\n请输入您要生成的订单数量:"))
        print("\n输入正确！")
        # 如果用户输入的是数字，则跳出循环
        break
    except ValueError:
        print("\n输入错误，请重新输入！")


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n程序开始')
        # cls.driver = webdriver.Chrome(options=Browser().browser_ui()) # 带UI界面启动
        cls.driver = webdriver.Chrome(options=Browser().browser_headless())  # 无头模式启动
        cls.loginpage = BasePage(cls.driver)
        cls.loginpage.implicitly_wait(15)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print('\n程序结束')

    # @unittest.skip('unittest不执行这条测试用例')
    def test_1_login(self):
        """登录ERP系统"""
        self.loginpage.max()
        self.loginpage.visit("http://h.thinkermen.com/wincc_xingeercc/mini2021_1.5.7/index.php?r=login")
        self.loginpage.input((By.ID, 'loginname'), "admin")
        self.loginpage.input((By.ID, 'nloginpwd'), "123456")
        self.loginpage.click((By.CSS_SELECTOR,
                              "body > div.lbl_login_bg > div.new_login_r > div.login_form.clb > div:nth-child(1) > "
                              "div > div:nth-child(3) > button"))
        self.loginpage.explicitly_wait((By.ID, 'add_order'), 10)
        print("\n登录成功！")

    # @unittest.skip('unittest不执行这条测试用例')
    def test_2_generate_order(self):
        """生成订单"""
        for i in range(total_orders):
            myTime = time.strftime("%Y-%m-%d~%H-%M-%S")
            self.loginpage.click((By.ID, 'add_order'))
            self.loginpage.switch_to_newest_window()
            self.loginpage.explicitly_wait((By.XPATH, '/html/body/div[10]/div[2]/div[3]/ul/li[2]/div'), 10)
            self.loginpage.click((By.XPATH, '/html/body/div[10]/div[2]/div[3]/ul/li[2]/div'))
            self.loginpage.switch_to_newest_window()
            self.loginpage.explicitly_wait((By.ID, 'customer_name'), 10)
            self.loginpage.input((By.ID, 'customer_name'), "倪浩平")
            self.loginpage.wait(2)
            self.loginpage.click((By.XPATH, '/html/body/form/div[1]/div[1]/div/div[2]/div/dl[2]/dd/div/ul/li'))
            self.loginpage.explicitly_wait((By.NAME, 'zonggao'), 10)
            self.loginpage.input((By.NAME, 'zonggao'), "1000")
            self.loginpage.input((By.NAME, 'zongkuan'), "200")
            self.loginpage.input((By.NAME, 'shuliang'), "1")
            self.loginpage.input((By.NAME, 'yanse'), "黑色")
            # 生成0.01到0.2之间的随机浮点数,保留小数点2位
            random_number = round(random.uniform(0.01, 0.2), 2)
            self.loginpage.input((By.NAME, 'danjia'), "{}".format(random_number))
            self.loginpage.click((By.ID, 'start_count'))
            self.loginpage.explicitly_wait((By.ID, 'save_order'), 10)
            self.loginpage.click((By.ID, 'save_order'))
            self.loginpage.explicitly_wait((By.CSS_SELECTOR,
                                  '#order_factory > div.aui_state_focus.aui_state_lock > div > table > tbody > '
                                  'tr:nth-child(2) > td.aui_c > div > table > tbody > tr:nth-child(2) > td.aui_main > '
                                  'div > div > div.system_overlay_btn > button.sbt_white.fr.mr10.group_orders'), 10)
            self.loginpage.click((By.CSS_SELECTOR,
                                  '#order_factory > div.aui_state_focus.aui_state_lock > div > table > tbody > '
                                  'tr:nth-child(2) > td.aui_c > div > table > tbody > tr:nth-child(2) > td.aui_main > '
                                  'div > div > div.system_overlay_btn > button.sbt_white.fr.mr10.group_orders'))
            self.loginpage.switch_to_newest_window()
            self.loginpage.explicitly_wait((By.XPATH, '//*[@id="rows"]/div[2]'), 10)
            ul_num = self.loginpage.get_ul_number((By.XPATH, '//*[@id="rows"]/div[2]'))
            """翻页处理"""
            if 0 < ul_num < 30:
                self.loginpage.click((By.XPATH, f'//*[@id="rows"]/div[2]/ul[{ul_num}]/li[4]/a'))
                self.loginpage.switch_to_newest_window()
                self.loginpage.wait(5)
                self.loginpage.erp_order_screenshot(myTime)
                self.loginpage.close()
                self.loginpage.switch_to_newest_window()
                self.loginpage.explicitly_wait((By.XPATH, '//*[@id="order_factory"]/div[9]/div[1]/li'), 10)
                self.loginpage.click((By.XPATH, '//*[@id="order_factory"]/div[9]/div[1]/li'))

            if ul_num >= 30:
                self.loginpage.click((By.CSS_SELECTOR, '#pager > div.jPag-control-front > a'))
                print('\n当前页面订单大于30个，正在跳转最新页面')
                self.loginpage.explicitly_wait((By.XPATH, '//*[@id="rows"]/div[2]'), 10)
                ul_num = self.loginpage.get_ul_number((By.XPATH, '//*[@id="rows"]/div[2]'))
                self.loginpage.click((By.XPATH, f'//*[@id="rows"]/div[2]/ul[{ul_num}]/li[4]/a'))
                self.loginpage.switch_to_newest_window()
                self.loginpage.wait(5)
                self.loginpage.erp_order_screenshot(myTime)
                self.loginpage.close()
                self.loginpage.switch_to_newest_window()
                self.loginpage.explicitly_wait((By.XPATH, '//*[@id="order_factory"]/div[9]/div[1]/li'), 10)
                self.loginpage.click((By.XPATH, '//*[@id="order_factory"]/div[9]/div[1]/li'))

            print("\n订单金额:", random_number, "元")
            print("\n截图时间:", myTime)

        print("\n总共生成", total_orders, "个订单")
        print("\n订单地址", 'http://h.thinkermen.com/wincc_xingeercc/mini2021_1.5.7/index.php?r=order/factory')


if __name__ == '__main__':
    unittest.main()
