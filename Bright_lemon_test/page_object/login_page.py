from Bright_lemon_test.base.base_page import Basepage
from Bright_lemon_test.data.login_page_element import *


class Loginpage(Basepage):

    def login(self,username,password):
        """登录页面"""
        self.implicitly_wait(10)
        self.visit(website['url'])
        self.max()
        self.click(login_element['account_button'])
        self.input(login_element['username_ele'],username)  # username_ele从字典中取用户名对应的XPATH路径
        self.input(login_element['password_ele'],password)  # password_ele从字典中取密码对应的XPATH路径
        self.click(login_element['login_button'])  # login_button从字典中取登录按钮对应的XPATH路径

    def enterinto_authorization(self):
        """进入亮柠檬认证授权管理系统"""
        self.click(system_name['authorization'])
        self.wait(1)

    def enterinto_lemon_management(self):
        """进入亮柠檬管理系统"""
        self.click(system_name['lemon_management'])
        self.wait(1)

    def enterinto_shop(self):
        """进入亮柠檬门店系统"""
        self.click(system_name['shop'])
        self.wait(1)

    def enterinto_check(self):
        """进入亮柠檬阅片系统"""
        self.click(system_name['check'])
        self.wait(1)

    def enterinto_bigvision_management(self):
        """进入CRM系统"""
        self.click(system_name['bigvision_management'])
        self.wait(1)

