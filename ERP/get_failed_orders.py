import unittest
from Browser import *
from base_page import *
from selenium.webdriver.common.by import By
import re


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
    def test_2_filter_failed_orders(self):
        self.obj.click((By.XPATH, '//*[@id="menu"]/ul/ul/li[3]'))
        self.obj.click((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[1]/div[10]/div/div/div/div/input'))
        self.obj.wait(2)
        self.obj.get_li_value('el-scrollbar__view el-select-dropdown__list', '失败')
        self.obj.click((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[1]/div[12]/div[3]/button[1]'))
        self.obj.wait(5)
        failed_orders_text = self.obj.get_text((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[1]/div[12]/div[2]/span[2]'))
        match = re.search(r'\d+', failed_orders_text)
        if match:
            # 将匹配到的字符串转换为整数
            failed_orders = int(match.group())
            print("失败订单总数:", failed_orders)
        else:
            print("匹配失败")

        failed_reason_xpath = '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[{index}]/td[15]'
        order_number_xpath = '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[{index}]/td[2]'

        """将结果保存到result.txt文件中"""
        with open('result.txt', 'w', encoding='utf-8') as f:
            if 0 < failed_orders <= 20:
                for index in range(1, failed_orders+1):
                    xpath = failed_reason_xpath.format(index=index)
                    xpath2 = order_number_xpath.format(index=index)
                    failed_reason = self.obj.get_text((By.XPATH, xpath))
                    order_number = self.obj.get_text((By.XPATH, xpath2))
                    f.write('订单号: ' + str(order_number) + ', 失败原因: ' + str(failed_reason) + '\n')

            if failed_orders > 20:
                pages = failed_orders // 20 + (1 if failed_orders % 20 > 0 else 0)  # 定义页数，每20条数据为1页
                final_page = (failed_orders % 20) + 1  # 最后一页剩余的数据

                for page in range(2, pages+1):
                    """翻页处理"""
                    self.obj.wait(2)
                    for index in range(1, 21):
                        xpath = failed_reason_xpath.format(index=index)
                        xpath2 = order_number_xpath.format(index=index)
                        failed_reason = self.obj.get_text((By.XPATH, xpath))
                        order_number = self.obj.get_text((By.XPATH, xpath2))
                        f.write('订单号: ' + str(order_number) + ', 失败原因: ' + str(failed_reason) + '\n')

                    self.obj.backspace_macos((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[3]/div/span[3]/div/div/input'))
                    self.obj.input((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[3]/div/span[3]/div/div/input'), '{page}'.format(page=page))
                    self.obj.click((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[1]/div[12]/div[3]/button[1]'))
                    print(f"已翻至第{page}页")

                """最后一页剩余的数据"""
                self.obj.wait(15)
                for index in range(1, final_page):
                    xpath = failed_reason_xpath.format(index=index)
                    xpath2 = order_number_xpath.format(index=index)
                    failed_reason = self.obj.get_text((By.XPATH, xpath))
                    order_number = self.obj.get_text((By.XPATH, xpath2))
                    f.write('订单号: ' + str(order_number) + ', 失败原因: ' + str(failed_reason) + '\n')


if __name__ == '__main__':
    unittest.main()
