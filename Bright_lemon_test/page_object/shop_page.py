from Bright_lemon_test.base.base_page import Basepage
from Bright_lemon_test.data.shop_page_element import *
import random


class Shoppage(Basepage):

    def choose_shop(self):
        """选择进入某家门店"""
        self.click(choose_shop['drop_down_button'])
        self.driver.execute_script("arguments[0].click();", self.locator(choose_shop['add_shop']))
        self.click(choose_shop['confirm_button'])

    def create_client(self):
        """建档"""
        self.implicitly_wait(10)
        self.click(shop_module['file_library']) # 进入档案库模块
        self.click(client['add_client'])
        self.input(client['contactor'],'测试{rad}'.format(rad=random.randint(1,9999)))
        contactor=self.get_text(client['contactor_input'])
        print(contactor)
        self.explicitly_wait(client['gender_drop_down_button'],30)
        self.click(client['gender_drop_down_button']) # 点击性别下拉框
        self.wait(2)
        self.get_list_value(self.locators(client['gender_li']),"女")  # 使用get_list_value函数进行循环判断，如果出现目标文字，点击，然后退出循环
        self.driver.execute_script("arguments[0].removeAttribute('readonly');", self.locator(client['birthday'])) # 对输入框去除readonly属性
        self.input(client['birthday'],'2000-06-01')  # 去除readonly属性后，输入框中支持手动输入日期
        self.click(client['sava_info'])

    def registration_type_normal(self):
        """选择常规诊断"""
        self.implicitly_wait(10)
        self.click(client['first_registration'])
        self.click(client['registration_type_normal'])

    def normal_process(self):
        """常规诊断/预约流程"""
        self.implicitly_wait(10)
        self.click(process['default_position'])  # 取消默认的套餐
        self.click(process['eyesight-check'])  # 重新选择视力检验套餐
        self.click(process['universal_button'])  # 创建检查单
        self.click(process['confirm_check'])  # 确认开单
        self.wait(2)
        self.click(process['universal_button'])  # 开始检查
        self.click(process['eyesight_type'])  # 视标类型选择C视标
        self.click(process['right_eye_far_eyesight'])  # 点击右眼远视力（裸眼) 的输入框
        self.get_list_value(self.locators(process['right_eye_far_eyesight_li']),'2.0')
        self.click(process['next_one']) # 下一个
        self.click(process['universal_button'])  # 完成检查
        self.click(process['choose_doctor'])  # 选择医生
        self.wait(4)
        self.click(process['start_check'])  # 开始问诊
        self.click(process['default_position'])  # 取消默认的套餐
        self.click(process['check'])  # 重新选择问诊套餐
        self.click(process['universal_button'])  # 创建检查单
        self.click(process['confirm_check'])  # 确认开单
        self.wait(2)
        self.click(process['start_check_again'])  # 开始问诊
        self.click(process['regular_check'])  # 在问诊中选择定期检查项
        self.click(process['next_one'])  # 下一个
        self.click(process['start_check_again'])  # 开检查单
        self.click(process['OCTBv1000'])  # 选择OCTBv1000
        self.click(process['universal_button'])  # 创建检查单
        self.click(process['confirm_check'])  # 确认开单
        self.wait(2)
        self.click(process['universal_button'])  # 开始检查
        self.click(process['next_one'])  # 下一个
        self.click(process['universal_button'])  # 完成检查
        self.wait(2)
        self.click(process['reverse_order'])  # 点击时间倒序
        self.wait(2)
        self.click(process['locate_client'])  # 定位刚刚诊断过的患者
        self.wait(2)
        self.click(process['start_check'])  # 开始诊断
        self.click(process['add_check'])  # 添加诊断按钮
        self.wait(2)
        self.click(process['add_check_item_button'])  # 添加诊断条目按钮
        self.click(process['macular_degeneration'])  # 添加黄斑变性
        self.click(process['add_check_item'])  # 添加按钮
        self.wait(2)
        self.click(process['eyes'])  # 点击眼别下拉框
        self.wait(2)
        self.get_list_value(self.locators(process['eyes_li']), '左眼')
        self.wait(2)
        self.click(process['related_check_item'])  # 点击关联检查项下拉框
        self.wait(2)
        self.get_list_value(self.locators(process['related_check_item_li']), 'OCTBv1000')  # 选择关联检查项为OCTBv1000
        self.click(process['save']) # 保存诊断的疾病
        self.click(process['assert_check'])  # 确认诊断
        self.wait(2)
        self.click(process['assert_plan'])  # 直接点击确认方案
        self.click(process['save_again'])  # 再次点击保存
        self.wait(2)
        self.click(process['reservation_for_check'])  # 点击预约复查
        self.input((process['reservation_date']),'2022-05-30 09:30:00')  # 输入预约日期
        self.click(process['reservation_date_save'])  # 保存预约日期
        self.wait(2)
        self.input((process['reservation_mobile']),'15180381485')  # 输入预约的手机号
        self.click(process['reservation_content'])  # 点击复查内容下拉框
        self.wait(2)
        self.get_list_value(self.locators(process['reservation_content_li']), '复测套餐')  # 选择复测套餐
        self.wait(2)
        self.click(process['reservation_save'])  # 保存预约
        self.wait(2)






















