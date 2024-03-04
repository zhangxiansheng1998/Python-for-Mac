
import unittest
import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from Appium.base.driver_proxy_settings import *
from Appium.page_object.login_page import *
from Appium.base.kill_process import *

class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('程序开始')
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Driver().driver_property())
        cls.bp = Basepage(cls.driver)
        cls.bp.implicitly_wait(15) # 需要设置隐式等待，否则可能会报错，全局有效，只需设置一次
        cls.lp = Login(cls.driver)


    @classmethod
    def tearDownClass(cls):
        print('程序结束')
        cls.driver.quit()


    def test_login(self):
        print("进入设置页面")
        self.bp.click((By.ID,'android:id/title'))
        print('已进入WiFi页面')
        self.bp.wait(2)
        self.bp.click((By.ID,'android:id/icon'))
        self.bp.wait(2)
        self.bp.click((By.ID,'android:id/icon'))
        self.bp.wait(2)
        self.bp.click((By.ID,'com.android.settings:id/proxy_settings'))
        self.bp.wait(2)
        self.bp.click((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]'))
        self.bp.input((By.ID,'com.android.settings:id/proxy_hostname'),'192.168.110.191')
        self.bp.input((By.ID,'com.android.settings:id/proxy_port'), '8888')
        self.bp.click((By.ID,'com.android.settings:id/save_button'))
        print("Charles代理设置成功")
        self.bp.click((By.ID,'android:id/icon'))
        self.bp.wait(2)

if __name__ == '__main__':
    pytest.main(['-s','test_case_001.py'])
