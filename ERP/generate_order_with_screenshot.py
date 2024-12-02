from Browser import *
from base_page import *
from selenium.webdriver.common.by import By
import unittest
from PIL import Image
import io


class TestCase(unittest.TestCase):
    obj = None
    driver = None

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
        """登录ERP系统"""
        self.obj.max()
        self.obj.visit("http://mt-hwc.thinkermen.com/wincc_xingeercc/mini2021_1.7.7/index.php?r=main/index")
        self.obj.input((By.ID, 'loginname'), "倪浩")
        self.obj.input((By.ID, 'nloginpwd'), "123654")
        self.obj.click((By.CSS_SELECTOR,
                        "body > div.lbl_login_bg > div.new_login_r > div.login_form.clb > div:nth-child(1) > "
                        "div > div:nth-child(3) > button"))
        print("\n登录成功！")

    # @unittest.skip('unittest不执行这条测试用例')
    def test_2_generate_order(self):
        """生成订单"""
        self.obj.wait(5)
        self.obj.click((By.ID, 'order_list'))
        self.obj.switch_to_newest_window()
        self.obj.click((By.XPATH, '/html/body/div[79]/div[1]/div[2]/ul[1]/li[11]/a'))
        self.obj.switch_to_newest_window()
        self.obj.wait(3)
        """
        screenshot = self.driver.get_screenshot_as_png()
        screenshot_img = Image.open(io.BytesIO(screenshot))
        partial_screenshot = screenshot_img.crop((1950, 350, 3150, 900))

        # 部分截图
        partial_screenshot.save("partial_screenshot.png")
        """
        self.obj.partial_screenshot(1950, 350, 3150, 900)


if __name__ == '__main__':
    unittest.main()
