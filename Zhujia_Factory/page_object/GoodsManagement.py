from Common_File.base_page import BasePage
from Zhujia_Factory.data.goods_management_element import *


class GoodsManagement(BasePage):

    def search_goods(self):
        """查询商品信息"""
        self.click(button['goods_list'])




