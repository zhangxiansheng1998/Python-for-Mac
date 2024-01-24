from Jsfk.base.base_page import Basepage
from Jsfk.data.login_page_element import *


class Loginpage(Basepage):

    def login(self, username, password):
        """登录页面"""
        self.visit(website['url'])
        self.max()
        self.input(login_element['username_ele'], username)  # username_ele从字典中取用户名对应的XPATH路径
        self.input(login_element['password_ele'], password)  # password_ele从字典中取密码对应的XPATH路径
        self.click(login_element['login_button'])  # login_button从字典中取登录按钮对应的XPATH路径
