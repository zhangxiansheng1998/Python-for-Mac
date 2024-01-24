import random
from appium import webdriver
from jsfk_test.base.base_page import *
from selenium.webdriver.common.by import By


class BV1000S(Basepage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_app(self, host='127.0.0.1', port=4723):
        # 配置信息
        # 包含：平台名、系统、BV1000S的绝对路径
        desired_caps = {
            'platformName': 'Windows',
            'deviceName': 'WindowsPC',
            'app': 'D:\BV1000S\OCTGui.exe'}

        # 开启WinAppDriver服务,如果不开启，将无法打开应用程序
        os.startfile('C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe')

        # 打开应用程序
        self.driver = webdriver.Remote('http://{}:{}'.format(host, port), desired_caps)

        # 如果不等待，容易报错
        self.wait(3)

    def login(self):
        """登录BV1000S"""
        self.click((By.XPATH, '/Window/Custom/Group/Group/Button[1]'))
        # 点击登录按钮

    def add_paient(self):
        """创建患者"""
        self.click((By.XPATH, '/Window/Custom/Group/Group[2]/Group/CheckBox'))
        # 点击注册按钮
        self.input((By.XPATH, '/Window/Group[2]/Edit[1]'), '患者{num}'.format(num=random.randint(1, 99999)))
        # 输入患者姓名
        self.click((By.XPATH, '/Window/Button[1]'))
        # 保存信息

    def check(self):
        """检查"""
        self.click((By.XPATH, '/Window/Custom/Group/Group[6]/Group/Button[5]'))
        # 点击采集按钮
        self.wait(5)
        self.click((By.XPATH, '/Window/Custom/Group/Group[4]/Group[1]/Button[1]'))
        # 点击下一步


if __name__ == '__main__':
    auto = BV1000S(webdriver.Remote)
    auto.open_app()
    auto.login()
