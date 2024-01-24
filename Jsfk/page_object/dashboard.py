from selenium.webdriver.common.by import By
from Jsfk.base.base_page import Basepage


class Dashboard(Basepage):
    dashboard_button = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/div[1]/div/ul/div[2]/a/li')
    view_button = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/section/div/button')
    hzcheck = (By.XPATH, '//*[@id="app"]/div/div[1]/div/p[1]')

    def view(self):
        """进入dashboard模块"""
        self.driver.implicitly_wait(10)
        self.click(self.dashboard_button)
        self.click(self.view_button)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])        # 句柄切换到新页面
        self.explicitly_wait(self.hzcheck, 5)
        self.screen()
        self.driver.close()        # 关闭新页面,使用close()关闭
        self.driver.switch_to.window(handles[0])        # 将窗口切换回最开始的页面(虽然关闭了新页面，但如果不切换窗口句柄，浏览器无法定位到元素，会抛出异常)
        self.screen()
