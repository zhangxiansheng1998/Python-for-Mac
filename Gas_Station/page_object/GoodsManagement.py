import time
from Gas_Station.base.base_page import BasePage
from Gas_Station.data.goods_management_element import *


class GoodsManagement(BasePage):

    def search_goods(self):
        """查询商品信息"""
        self.click(button['goods_list'])
        self.input(goods_list['search_input_box'], '测试上传视频后，编辑时能否看到视频')
        self.click(goods_list['search_button'])
        self.wait(5)
        self.assert_text_equal('测试上传视频后，编辑时能否看到视频', goods_list['goods_text'])
        self.click(goods_list['reset_button'])

    def shelf_goods(self):
        """上下架商品"""
        self.wait(3)
        self.click(goods_list['select_goods'])
        self.click(goods_list['multiple_times_shelf'])
        self.wait(3)
        self.assert_text_equal('下架成功', goods_list['assert_box'])
        self.click(goods_list['off_sale'])
        self.wait(1)
        self.click(goods_list['select_goods'])
        self.click(goods_list['multiple_times_shelf'])
        self.wait(3)
        self.assert_text_equal('上架成功', goods_list['assert_box'])

    def add_goods(self):
        """新增商品"""
        self.click(button['add_goods'])
        self.wait(1)
        self.click(add_goods['goods_category'])
        self.click(add_goods['goods_category_1'])
        self.click(add_goods['goods_category_2'])
        self.click(add_goods['goods_category_3'])
        myTime = time.strftime("%Y-%m-%d~%H-%M-%S")
        self.input((add_goods['goods_name']), myTime)
        self.input((add_goods['goods_specification']), '规格')
        self.click(add_goods['add_inventory'])
        self.input((add_goods['goods_price']), '100')
        self.input((add_goods['goods_unit']), '厘米')
        self.click(add_goods['confirm'])
        self.wait(2)
        self.assert_text_equal('操作成功！', add_goods['assert_box'])

    def add_category(self):
        """新增一二三级分类"""
        self.click(button['goods_category'])
