import time
import unittest
import pytest
from appium import webdriver
from Appium.page_object.search_page import *
from Newcode.driver import *


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('程序开始')
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Driver().driver_property())
        cls.bdsearch = Baidusearch(cls.driver)

    @classmethod
    def tearDownClass(cls):
        print('程序结束')
        cls.driver.quit()

    def test1_search(self):
        self.driver.start_activity('com.android.settings', '.Settings')
        time.sleep(2)


if __name__ == '__main__':
    pytest.main(['-s','garbage3.py'])
