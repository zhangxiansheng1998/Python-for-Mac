import unittest
import pytest
from appium import webdriver
from Appium.page_object.login_page import *
from Appium.base.driver import *


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('程序开始')
        cls.driver = webdriver.Remote('http://127.0.0.1:4722/wd/hub', Driver().driver_property())
        #cls.bdsearch = Baidusearch(cls.driver)

    @classmethod
    def tearDownClass(cls):
        print('程序结束')
        cls.driver.quit()

    def test1_search(self):
        #self.bdsearch.baidu_search()
        print("即将关闭")


if __name__ == '__main__':
    pytest.main(['-s','test_case_001.py'])
