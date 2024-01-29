from Common_File.base_page import BasePage
from Zhujia_Factory.data.shop_management_element import *


class ShopManagement(BasePage):

    def add_zhujia_shop(self):
        """新增筑家工厂店铺"""
        self.click(button['shop_list'])
        self.click(button['add_shop'])
        self.input(add_shop['shop_name'],self.timeformate)
        self.click((By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[2]/div/form/div[5]/div[2]/div[1]/div/div/div/span/span'))
        self.wait(1)
        self.get_li_value('el-scrollbar__view el-select-dropdown__list','江苏省')
        self.click((By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[2]/div/form/div[5]/div[2]/div[2]/div/div/div/span/span'))
        self.wait(1)
        self.get_li_value('el-scrollbar__view el-select-dropdown__list', '无锡市')
        self.click((By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[2]/div/form/div[5]/div[2]/div[3]/div/div/div/span'))
        self.wait(1)
        self.get_li_value('el-scrollbar__view el-select-dropdown__list', '滨湖区')
        self.input(add_shop['logo'],'/Volumes/Disk/MyProject/Zhujia_Factory/data/background.jpg')
        self.wait(1)
        self.click(add_shop['submit'])

    def add_erp_shop(self):
        """新增ERP店铺"""
        pass