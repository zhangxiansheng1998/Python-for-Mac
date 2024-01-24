from selenium.webdriver.common.by import By
import random

module={
    'open_school_first_module':(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/div[1]/div/ul/div[3]/li/div'),
    #基础数据管理
    'open_school_second_module':(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/div[1]/div/ul/div[3]/li/ul/div[1]/a/li/span'),
    #学校管理
}

add_school={
    'add_school_button':(By.XPATH,'//*[@id="header-box"]/button'),
    # 添加学校按钮
    'add_school_name':(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/section/div/div[4]/div/div[2]/form/div[1]/div/div[1]/input'),
    # 学校名称
    'add_whole_province':(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div/div[1]/div/div/div/div/span/span/i'),
    # 定位所有省(一组元素)--下拉框
    'add_province':(By.XPATH,'//div[@class="el-select-dropdown el-popper"]//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li/span[contains(text(),"江西省")]'),
    # 定位某个特定的省
    'add_whole_city':(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div/div[2]/div/div/div/div/span/span/i'),
    # 定位所有市(一组元素)--下拉框
    'add_city':(By.XPATH,'//div[@class="el-select-dropdown el-popper"]//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li/span[contains(text(),"上饶市")]'),
    # 定位某个特定的市
    'add_whole_county':(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div/div[3]/div/div/div/div/span/span/i'),
    # 定位所有县(一组元素)--下拉框
    'add_county':(By.XPATH,'//div[@class="el-select-dropdown el-popper"]//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li/span[contains(text(),"鄱阳县")]'),
    # 定位某个特定的县
    'location':(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/section/div/div[4]/div/div[2]/form/div[3]/div/div[2]/span'),
    # 拾取坐标元素
    'address':(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/section/div/div[4]/div/div[2]/form/div[4]/div[2]/div/input'),
    # 点击拾取坐标元素后，弹出的地址输入框
    'school_type':(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/section/div/div[4]/div/div[2]/form/div[7]/div/div[1]/label[{x}]'.format(x=random.randint(1,4))),
    # 学校类型，label中的下标值1、2、3、4分别对应幼儿园、小学、初中、高中
    'contactor':(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/section/div/div[4]/div/div[2]/form/div[8]/div/div/input'),
    # 联系人
    'mobile':(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/section/div/div[4]/div/div[2]/form/div[9]/div/div/input'),
    # 联系电话
    'click_button':(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/section/div/div[4]/div/div[3]/span/button[2]'),
    # 确认按钮
    'close_button':(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/section/div/div[4]/div/div[1]/button/i'),
    # 右上角关闭窗口按钮
}

search_school={
    'school_search_input':(By.XPATH,'//*[@id="header-box"]/div/div[1]/input'),
    # 搜索框
    'school_search_button':(By.XPATH,'//*[@id="header-box"]/div/button[1]'),
    # 查询按钮
    'school_reset_button':(By.XPATH,'//*[@id="header-box"]/div/button[2]'),
    # 重置按钮
}

edit_school={
    'edit_school_button':(By.XPATH,'/html/body/div/div/div[2]/div[2]/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[9]/div/div/button[1]'),
    # 编辑按钮
    'detail_address':(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/section/div/div[4]/div/div[2]/form/div[4]/div/div/input'),
    # 详细地址
    'click_button': (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/section/div/div[4]/div/div[3]/span/button[2]'),
    # 确认按钮
}

search_class={
    'class_management':(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[9]/div/div/button[2]'),
    # 班级管理按钮
    'whole_class_list':(By.XPATH,'//*[@id="header-box"]/div[1]/div/div/span/span/i'),
    # 班级列表(一组元素)
    'class_list':(By.XPATH,'//div[@class="el-select-dropdown el-popper"]//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li/span[contains(text(),"初一1班")]'),
    # 定位某个班级
    'class_search_button':(By.XPATH,'//*[@id="header-box"]/div[1]/button[1]'),
    # 查询按钮
    'class_reset_button':(By.XPATH, '//*[@id="header-box"]/div[1]/button[2]')
    # 重置按钮
}

search_student={
    'student_management':(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/div/button[2]'),
    # 学生管理按钮
    'student_search_input':(By.XPATH,'//*[@id="header-box"]/div[1]/div/input'),
    # 搜索框
    'student_search_button':(By.XPATH,'//*[@id="header-box"]/div[1]/button[1]'),
    # 查询按钮
    'student_reset_button':(By.XPATH, '//*[@id="header-box"]/div[1]/button[2]')
    # 重置按钮
}
