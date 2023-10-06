import time
import unittest
import pytest
from appium import webdriver
from Appium.base.driver import *
from Appium.base.adb import *
from Appium.page_object.login_page import *
from Appium.base.appium_base_page import Basepage
from Appium.base.kill_process import *

class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('程序开始')
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Driver().driver_property())
        cls.cons = Connect_simulator(cls.driver)
        cls.cons.find_substring_in("already connected to 127.0.0.1:16384",cls.cons.string_data) # adb连接模拟器
        cls.imp_wait = Basepage(cls.driver)
        cls.imp_wait.implicitly_wait(15) # 需要设置隐式等待，否则可能会报错，全局有效，只需设置一次
        cls.lp = Login(cls.driver)

    @classmethod
    def tearDownClass(cls):
        print('程序结束')
        cls.driver.quit()


    def test_login(self):
        self.lp.login_success()


if __name__ == '__main__':
    pytest.main(['-s','test_case_001.py'])
