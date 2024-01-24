import requests
import time
from selenium.webdriver.common.by import By
from Jsfk.base.base_page import Basepage


class Homepage(Basepage):
    img = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/section/div/img')

    def get_picture(self):
        """下载首页图片"""
        self.driver.implicitly_wait(10)
        #  使用get_attribute()方法获取对应属性的属性值，src属性值就是图片地址
        url = self.locator(self.img).get_attribute('src')

        # 通过requests发送一个get请求到图片地址，返回的响应就是图片内容
        r = requests.get(url)

        # 将获取到的图片二进制流写入本地文件
        timeformate = time.strftime("%Y-%m-%d %H-%M-%S")        # 以 x-x-x x-x-x的时间格式显示

        with open('../picture/homepage_pic/' + timeformate + '.png', 'wb') as f:
            # 对于图片类型的通过r.content方式访问响应内容，将响应内容写入png文件中
            f.write(r.content)
