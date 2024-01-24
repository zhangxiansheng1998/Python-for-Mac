from Fudafu.base.appium_base_page import *
import re


class LoginPage(BasePage):


    def login_success_with_code(self):
        """登录成功"""
        self.wait(3)
        print('开始搜索')
        self.click((By.NAME, '搜索'))
        self.input((By.XPATH, '//XCUIElementTypeSearchField'),'付哒付')
        self.wait(3)
        print('已点击搜索框')
    
    def login_fail_with_code(self, phone, code):
        """登录失败"""
        self.input((By.NAME, '请输入手机号'), phone)
        self.click((By.NAME, ''))
        self.click((By.NAME, '登录/注册'))
        self.click((By.NAME, ''))
        self.input((By.XPATH, '//XCUIElementTypeTextField'), code)

