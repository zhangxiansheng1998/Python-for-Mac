from Gas_Station.base.base_page import BasePage
from Gas_Station.data.login_page_element import *


class LoginPage(BasePage):

    def login_without_sending_code(self, keyword):
        """使用固定验证码登录系统，即不发送验证码"""
        self.visit(website['url'])
        self.max()
        self.input(login_element['keyword'], keyword)  # username从字典中取用户名对应的XPATH路径
        self.click(login_element['search'])  # login_button从字典中取登录按钮对应的XPATH路径

