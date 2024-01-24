import time
import unittest
import pytest
from Jsfk.page_object.dashboard import Dashboard
from Jsfk.page_object.home_page import Homepage
from Jsfk.page_object.login_page import Loginpage
from Jsfk.page_object.school_managemen import Schoolmanagement
from Jsfk.page_object.institution_management import Insmanagement
from Jsfk.base.browser import *
from Jsfk.config.myddt import ddt,file_data

@ddt
class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        print('程序开始')
        cls.driver = webdriver.Chrome(options=Browser().browser_ui())             # 带UI界面启动
        #cls.driver=webdriver.Chrome(options=Browser().browser_headless())      # 无头模式启动
        cls.loginpage = Loginpage(cls.driver)
        cls.homepage = Homepage(cls.driver)
        cls.dashboard=Dashboard(cls.driver)
        cls.schoolmanagement=Schoolmanagement(cls.driver)
        cls.insmanagement=Insmanagement(cls.driver)

    @classmethod
    def tearDownClass(cls):
        print("\n")
        print('程序结束')
        cls.driver.quit()

    #@unittest.skip('unittest不执行这条测试用例')
    @file_data('../data/login_page_data.yaml')
    def test1_login(self,username,password):
        self.loginpage.login(username,password)

    #@unittest.skip('unittest不执行这条测试用例')
    def test3_dashboard(self):
        """进入dashboard"""
        self.dashboard.view()


if __name__ == '__main__':
    pytest.main(['-s','test_case_jsfk_001.py'])





