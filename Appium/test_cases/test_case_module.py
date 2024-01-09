import unittest
import pytest
from appium import webdriver
from Appium.base.driver import *
from Appium.base.appium_base_page import BasePage
from selenium.webdriver.common.by import By
from Appium.base.kill_process import *


class TestCase(unittest.TestCase):
    obj = None
    driver = None

    @classmethod
    def setUpClass(cls):
        print('程序开始')
        print('程序开始')
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Driver().ios16_driver_property())
        # cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Driver().ios17_driver_property())
        cls.obj = BasePage(cls.driver)
        cls.obj.implicitly_wait(15) # 需要设置隐式等待，否则可能会报错，全局有效，只需设置一次

    @classmethod
    def tearDownClass(cls):
        print('程序结束')
        cls.driver.quit()

    def test_1_login(self):
        print('执行的代码')


if __name__ == '__main__':
    pytest.main(['-s','test_case_001.py'])
