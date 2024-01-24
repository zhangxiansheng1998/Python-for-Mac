from appium import webdriver
from jsfk_test.base.base_page import *
from selenium.webdriver.common.by import By


class Auto(Basepage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    def open_weixin(self, host='127.0.0.1', port=4723):
        # 配置信息
        # 包含：平台名、系统、应用程序的绝对路径
        desired_caps = {'platformName': 'Windows',
                        'deviceName': 'WindowsPC',
                        'app': r"C:\Program Files\Genymobile\Genymotion\genymotion.exe"}

        # 开启WinAppDriver服务,如果不开启，将无法打开应用程序
        os.startfile('C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe')
        # 打开应用程序
        self.driver = webdriver.Remote('http://{}:{}'.format(host, port), desired_caps)
        self.wait(3) # 如果不等待，容易报错

    def click_method(self):
        self.click((By.XPATH,'/Window/Custom/TabItem/Pane[2]/Table/Group[1]/Button[1]'))
        # 点击最右边的...按钮
        self.click((By.XPATH,'/Window/Menu/MenuItem[1]/Text'))
        # 打开Android7.0对应的虚拟机


if __name__ == '__main__':
    driver=None
    auto=Auto(driver)
    auto.open_weixin()
    auto.click_method()