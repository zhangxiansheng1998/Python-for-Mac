from Browser import *
from base_page import *
from selenium.webdriver.common.by import By
import random
import os
import unittest


class TestCase(unittest.TestCase):
    obj = None
    driver = None

    @classmethod
    def setUpClass(cls):
        print('\n程序开始')
        #cls.driver = webdriver.Chrome(options=Browser().browser_ui()) # 带UI界面启动
        cls.driver = webdriver.Chrome(options=Browser().browser_headless())  # 无头模式启动
        cls.obj = BasePage(cls.driver)
        cls.obj.implicitly_wait(15)
        cls.total_orders = int(os.getenv('total_orders', 1))  # #定义环境变量，可以动态的传递total_orders的值，默认为1

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # @unittest.skip('unittest不执行这条测试用例')
    def test_1_login(self):
        """登录ERP系统"""
        self.obj.max()
        self.obj.visit("http://h.thinkermen.com/wincc_xingeercc/mini2021_1.7.3/index.php?r=login")
        self.obj.input((By.ID, 'loginname'), "admin")
        self.obj.input((By.ID, 'nloginpwd'), "123456")
        self.obj.click((By.CSS_SELECTOR,
                        "body > div.lbl_login_bg > div.new_login_r > div.login_form.clb > div:nth-child(1) > "
                        "div > div:nth-child(3) > button"))
        print("\n登录成功！")

    # @unittest.skip('unittest不执行这条测试用例')
    def test_2_generate_order(self):
        """生成订单"""
        self.obj.wait(5)
        for i in range(self.total_orders):
            myTime = time.strftime("%Y-%m-%d~%H-%M-%S")
            self.obj.click((By.XPATH, '/html/body/div[3]/div[17]/div[2]/div[2]/a[1]/div[1]/img'))
            self.obj.switch_to_newest_window()
            self.obj.explicitly_wait((By.XPATH, '/html/body/div[16]/div[2]/div[3]/ul/li[2]/div'), 10)
            self.obj.click((By.XPATH, '/html/body/div[16]/div[2]/div[3]/ul/li[2]/div'))
            self.obj.switch_to_newest_window()
            self.obj.explicitly_wait((By.ID, 'customer_name'), 10)
            self.obj.input((By.ID, 'customer_name'), "倪浩平")
            self.obj.wait(2)
            self.obj.click((By.XPATH, '/html/body/form/div[1]/div/div[1]/div[1]/div[2]/div/dl[2]/dd/div/ul/li'))
            self.obj.explicitly_wait((By.NAME, 'zonggao'), 10)
            self.obj.input((By.NAME, 'zonggao'), "1000")
            self.obj.input((By.NAME, 'zongkuan'), "200")
            self.obj.input((By.NAME, 'shuliang'), "1")
            self.obj.input((By.NAME, 'yanse'), "黑色")
            # 生成0.02到0.2元之间的随机浮点数,保留小数点后2位
            random_number = round(random.uniform(0.02, 0.2), 2)
            self.obj.input((By.NAME, 'danjia'), "{}".format(random_number))
            self.obj.click((By.ID, 'start_count'))
            self.obj.explicitly_wait((By.ID, 'save_order'), 10)
            self.obj.click((By.ID, 'save_order'))
            self.obj.explicitly_wait((By.CSS_SELECTOR,
                                      '#order_factory > div.aui_state_focus.aui_state_lock > div > table > tbody > '
                                      'tr:nth-child(2) > td.aui_c > div > table > tbody > tr:nth-child(2) > td.aui_main > '
                                      'div > div > div.system_overlay_btn > button.sbt_white.fr.mr10.group_orders'), 10)
            self.obj.click((By.CSS_SELECTOR,
                            '#order_factory > div.aui_state_focus.aui_state_lock > div > table > tbody > '
                            'tr:nth-child(2) > td.aui_c > div > table > tbody > tr:nth-child(2) > td.aui_main > '
                            'div > div > div.system_overlay_btn > button.sbt_white.fr.mr10.group_orders'))
            self.obj.switch_to_newest_window()
            self.obj.explicitly_wait((By.XPATH, '//*[@id="rows"]/div[2]'), 10)
            ul_num = self.obj.get_ul_number((By.XPATH, '//*[@id="rows"]/div[2]'))
            """翻页处理"""
            if 0 < ul_num < 30:
                self.obj.click((By.XPATH, f'//*[@id="rows"]/div[2]/ul[{ul_num}]/li[4]/a'))
                self.obj.switch_to_newest_window()
                self.obj.wait(5)
                self.obj.erp_order_screenshot(myTime)
                self.obj.switch_to_newest_window()
                self.obj.explicitly_wait((By.XPATH, '/html/body/div[81]/div/li'), 10)
                self.obj.click((By.XPATH, '/html/body/div[81]/div/li'))

            if ul_num >= 30:
                self.obj.click((By.CSS_SELECTOR, '#pager > div.jPag-control-front > a'))
                print('\n当前页面订单大于30个，正在跳转最新页面')
                self.obj.explicitly_wait((By.XPATH, '//*[@id="rows"]/div[2]'), 10)
                ul_num = self.obj.get_ul_number((By.XPATH, '//*[@id="rows"]/div[2]'))
                self.obj.click((By.XPATH, f'//*[@id="rows"]/div[2]/ul[{ul_num}]/li[4]/a'))
                self.obj.switch_to_newest_window()
                self.obj.wait(5)
                self.obj.erp_order_screenshot(myTime)
                self.obj.switch_to_newest_window()
                self.obj.explicitly_wait((By.XPATH, '/html/body/div[81]/div/li'), 10)
                self.obj.click((By.XPATH, '/html/body/div[81]/div/li'))

            print("\n第", i + 1, "笔订单")
            print("\n订单金额:", random_number, "元")
            print("\n截图时间:", myTime)

        print("\n总共生成", self.total_orders, "个订单")
        print("\n订单地址", 'http://h.thinkermen.com/wincc_xingeercc/mini2021_1.7.3/index.php?r=order/factory')


if __name__ == '__main__':
    unittest.main()