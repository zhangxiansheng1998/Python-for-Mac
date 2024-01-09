import unittest
import pytest
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Appium.base.driver import *
from Appium.base.kill_process import *


class TestCase(unittest.TestCase):
    obj = None
    driver = None

    @classmethod
    def setUpClass(cls):
        print('程序开始')
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Driver().ios16_driver_property())
        # cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Driver().ios17_driver_property())
        cls.obj = BasePage(cls.driver)
        cls.obj.implicitly_wait(15)  # 需要设置隐式等待，否则可能会报错，全局有效，只需设置一次

    @classmethod
    def tearDownClass(cls):
        print('程序结束')
        cls.driver.quit()

    def check_login_status(self):
        """判断当前页面是否登录系统，如果未登录，则给出相应提示；如果已登录，会退出当前账户"""
        try:
            expect_value = self.obj.get_text((By.NAME, '扫一扫'))
            if expect_value == '扫一扫':
                print('当前处于登录状态，正在退出系统')
                self.obj.click((By.NAME, '我的'))
                self.obj.click((By.NAME, '系统设置'))
                self.obj.click((By.NAME, '退出登录'))
                self.obj.click((By.NAME, '确认'))
        except NoSuchElementException:
            print('当前处于未登录状态，无需退出系统')
        except Exception as e:
            print(f'当前程序发生异常，异常信息如下: {e}\n')

    # @unittest.skip()
    def test_1_login_success(self):
        """登录成功"""
        self.check_login_status()
        self.obj.input((By.NAME, '请输入手机号'), '15180381485')
        self.obj.click((By.NAME, ''))
        self.obj.click((By.NAME, '登录/注册'))
        self.obj.click((By.NAME, ''))
        self.obj.input((By.XPATH, '//XCUIElementTypeOther[@name="pages/login/code/code[4]"]/XCUIElementTypeTextField'),
                       '654321')
        print('登录成功')

    # @unittest.skip()
    def test_2_login_fail(self):
        """登录失败"""
        self.check_login_status()
        self.obj.input((By.NAME, '请输入手机号'), '15180381485')
        self.obj.click((By.NAME, ''))
        self.obj.click((By.NAME, '登录/注册'))
        self.obj.click((By.NAME, ''))
        self.obj.input((By.XPATH, '//XCUIElementTypeOther[@name="pages/login/code/code[10]"]/XCUIElementTypeTextField'),
                       '123456')


if __name__ == '__main__':
    pytest.main(['-s', 'test_case_001.py'])
