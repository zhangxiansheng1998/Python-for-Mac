import time
from Jsfk.base.base_page import Basepage
from Jsfk.data.institution_management_element import *


class Insmanagement(Basepage):

    def enter_into_institution_management(self):
        """进入筛查机构模块"""
        if self.locator(module['open_school_first_module']).text == '学校管理':
            # 根据是否显示‘学校管理’四个字，判断有没有点击基础数据管理这个按钮
            # 如果点击了，那么直接点击筛查机构管理;如果没有，那么先点击基础数据管理，再点击筛查机构管理
            self.explicitly_wait(module['open_institution_second_module'], 10)
            self.click(module['open_institution_second_module'])  # 点击筛查机构管理模块
        else:
            self.click(module['open_school_first_module'])
            self.click(module['open_institution_second_module'])  # 点击筛查机构管理模块

    def institution_operations(self):
        """修改、搜索筛查机构"""
        self.input(search_institution['institution_search_input'], '湖州筛查中心')  # 搜索
        self.click(search_institution['institution_search_button'])  # 点击查询按钮
        self.screen()
        self.click(search_institution['institution_reset_button'])  # 点击重置按钮
        self.click(edit_institution['edit_institution_button'])  # 点击编辑按钮
        self.backspace(edit_institution['institution_address'])  # 清空详细地址的内容
        self.explicitly_wait(edit_institution['institution_address'], 5)
        self.screen()
        update_address = time.strftime("%Y-%m-%d/%H:%M:%S",
                                       time.localtime(time.time()))  # 修改后的地址的文本格式为2022-3-18/15:16:20
        self.input(edit_institution['institution_address'], update_address)
        self.click(edit_institution['click_button'])
        self.screen()
        self.click(download_button['download_wxcode_button'])
