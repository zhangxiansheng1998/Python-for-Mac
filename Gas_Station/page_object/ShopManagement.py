from Gas_Station.base.base_page import BasePage
from Gas_Station.data.shop_management_element import *


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
        self.input(add_shop['logo'],'/Volumes/Disk/MyProject/Gas_Station/data/background.jpg')
        self.wait(1)
        self.click(add_shop['submit'])
        self.wait(2)
        self.assert_text_equal('新增店铺成功', (By.ID,'message_1'))

    def add_erp_shop(self):
        """新增ERP店铺"""
        pass

    def check_details(self):
        """查看店铺的详情信息"""
        self.explicitly_wait(shop_list['shop_details'],10)
        self.click(shop_list['shop_details'])
        self.wait(2)
        self.assert_text_equal('店铺详情',(By.ID,'page-title'))
        self.click(shop_list['shop_details_return'])

    def today_income(self):
        """查看今日营业额"""
        self.explicitly_wait(shop_list['today_income'],10)
        self.click(shop_list['today_income'])
        self.wait(2)
        self.assert_text_equal('店铺今日统计', shop_list['today_income_text'])
        self.click(shop_list['today_income_close'])

    def custom_income(self):
        """自定义输入收款金额"""
        self.explicitly_wait(shop_list['custom_income'],10)
        self.click(shop_list['custom_income'])
        self.input(shop_list['enter_amount'],'5')
        self.click(shop_list['custom_income_confirm'])
        self.wait(2)
        self.assert_text_equal('￥5.00', shop_list['custom_income_text'])
        self.click(shop_list['custom_income_close_two'])

    def income_code(self):
        """查看店铺的收款码"""
        self.explicitly_wait(shop_list['income_code'],10)
        self.click(shop_list['income_code'])
        self.wait(2)
        self.assert_text_equal('店铺收款码', shop_list['income_code_text'])
        self.click(shop_list['income_code_close'])

    def shop_code(self):
        """查看店铺码"""
        self.explicitly_wait(shop_list['shop_code'],10)
        self.click(shop_list['shop_code'])
        self.wait(2)
        self.assert_text_equal('店铺码', shop_list['shop_code_text'])
        self.click(shop_list['shop_code_close'])


