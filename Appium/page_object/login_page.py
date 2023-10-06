
from Appium.base.appium_base_page import Basepage
from Appium.data.login_page_element import login_element

class Login(Basepage):

    def login_success(self):
        """正常登录"""
        self.click(login_element['accept_protocol'])
        self.wait(3)
        self.input(login_element['login_input'], '18662832373')
        self.wait(3)
        self.click(login_element['login_accept_protocol'])
        self.click(login_element['login_button'])
        self.click(login_element['login_as_admin'])
        self.input(login_element['code'], '111111')
        self.wait(5)
        print("登录成功")
