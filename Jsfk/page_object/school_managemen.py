from Jsfk.base.base_page import Basepage
from Jsfk.data.school_management_element import *
import time


class Schoolmanagement(Basepage):

    def enter_into_school_management(self):
        """进入学校管理模块"""
        self.explicitly_wait(module['open_school_first_module'], 5)
        self.click(module['open_school_first_module'])  # 点击基础数据管理模块
        self.screen()
        self.click(module['open_school_second_module'])  # 点击学校管理模块
        self.screen()

    def add_school(self, school_name, contactor, mobile):
        """新增学校"""
        self.click(add_school['add_school_button'])  # 点击新增按钮
        self.screen()
        self.input(add_school['add_school_name'], school_name)  # 输入学校名称
        self.wait(1)
        self.click(add_school['add_whole_province'])  # 获取所有省的列表
        self.driver.execute_script("arguments[0].click();",
        self.locator(add_school['add_province']))  # 定位add_province中包含江西省的信息并选中
        self.click(add_school['add_whole_city'])  # 获取所有市的列表
        self.driver.execute_script("arguments[0].click();",
        self.locator(add_school['add_city']))  # 定位add_city中包含上饶市的信息并选中
        self.click(add_school['add_whole_county'])  # 获取所有县的列表
        self.driver.execute_script("arguments[0].click();",
        self.locator(add_school['add_county']))  # 定位add_county中包含鄱阳县的信息并选中
        self.click(add_school['location'])  # 点击拾取坐标
        self.input(add_school['address'], school_name)  # 输入学校名称
        school_list = self.driver.find_element(By.XPATH, '//*[@class="el-autocomplete-suggestion el-popper"]/div/div/ul')  # 获取学校列表
        school_list.find_elements(By.TAG_NAME, 'li')[0].click()  # 定位学校列表中第一个地址
        self.js_scroll_bottom()  # 页面滚到底部
        self.click(add_school['school_type'])  # 选择学校类型
        self.input(add_school['contactor'], contactor)  # 输入联系人
        self.input(add_school['mobile'], mobile)  # 输入联系电话
        self.click(add_school['click_button'])  # 确定按钮
        self.click(add_school['close_button'])  # 若为第二次添加，则无法重复添加重名学校，选择关闭该窗口

    def search_school(self, school_name):
        """搜索学校"""
        self.input(search_school['school_search_input'], school_name)  # 传递school_name作为搜索的关键字
        self.click(search_school['school_search_button'])  # 点击查询按钮
        self.screen()
        self.click(search_school['school_reset_button'])  # 点击重置按钮

    def edit_school(self):
        """编辑学校"""
        self.click(edit_school['edit_school_button'])
        self.backspace(edit_school['detail_address'])  # 清空详细地址
        update_address = time.strftime("%Y-%m-%d/%H:%M:%S",
        time.localtime(time.time()))  # 修改后的地址的文本格式为2022-3-18/15:16:20
        self.input(edit_school['detail_address'], update_address)  # 修改详细地址
        self.click(edit_school['click_button'])

    def class_management(self):
        """搜索班级"""
        self.click(search_class['class_management'])  # 点击班级管理按钮
        self.click(search_class['whole_class_list'])  # 点击班级列表中的的下拉框
        self.driver.execute_script("arguments[0].click();",
        self.locator(search_class['class_list']))  # 定位class_lists中包含初一1班的信息并选中
        self.click(search_class['class_search_button'])  # 搜索按钮
        self.click(search_class['class_reset_button'])  # 重置按钮

    def student_management(self):
        """搜索学生信息"""
        self.click(search_student['student_management'])  # 点击学生管理按钮
        self.input(search_student['student_search_input'], '程五少')
        self.click(search_student['student_search_button'])
        self.click(search_student['student_reset_button'])
