from Zhujia_Factory.base.base_page import BasePage
from Zhujia_Factory.data.login_page_element import *


class LoginPage(BasePage):

    def login_without_sending_code(self, username, code):
        """使用固定验证码登录系统，即不发送验证码"""
        self.visit(website['url'])
        self.max()
        self.input(login_element['username'], username)  # username从字典中取用户名对应的XPATH路径
        self.input(login_element['input_code'], code)  # input_code从字典中取密码对应的XPATH路径
        self.click(login_element['login_button'])  # login_button从字典中取登录按钮对应的XPATH路径

    def login_with_sending_code(self, username, code):
        """发送验证码登录系统"""
        self.visit(website['url'])
        self.max()
        self.input(login_element['username'], username)  # username从字典中取用户名对应的XPATH路径
        self.click(login_element['send_code'])  # send_code从字典中取用户名对应的XPATH路径
        self.wait(1)
        self.input(login_element['input_code'], code)  # input_code从字典中取密码对应的XPATH路径
        self.click(login_element['login_button'])  # login_button从字典中取登录按钮对应的XPATH路径
