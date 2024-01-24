from selenium.webdriver.common.by import By
    #'':(By.XPATH,''),


choose_shop={
    'drop_down_button':(By.XPATH,'//*[@id="home"]/div/div/div[1]/div[2]/div/div[2]/form/div/div/div/div/span/span/i'),
    # 门店下拉按钮
    'add_shop':(By.XPATH,'//div[@class="el-select-dropdown el-popper"]//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li/span[contains(text(),"赣州第一")]'),
    # 定位赣州第一分店
    'confirm_button':(By.XPATH,'//*[@id="home"]/div/div/div[1]/div[2]/div/div[3]/span/button')
    # 确定按钮
}

shop_module={
    'file_library':(By.XPATH,'//*[@id="home"]/div/div/div[2]/div[2]/div/a/img')
    # 档案库模块
}

client={
    'add_client':(By.XPATH,'//*[@id="home"]/div[1]/div[2]/div/div[2]/div[1]/button'),
    # 创建患者按钮
    'contactor':(By.XPATH,'//*[@id="home newFiles"]/div[1]/div[2]/div[1]/div[2]/form/div[1]/div/div[1]/input'),
    # 联系人
    'contactor_input':(By.XPATH,'//*[@id="home newFiles"]/div[1]/div[2]/div[1]/div[2]/form/div[1]/div/div/input'),
    # 联系人输入框
    'gender_drop_down_button':(By.XPATH,'//*[@id="home newFiles"]/div[1]/div[2]/div[1]/div[2]/form/div[2]/div/div/div/span/span/i'),
    # 性别下拉框
    'gender_li':(By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li'),
    # 性别列表li
    'birthday':(By.XPATH,'//*[@id="home newFiles"]/div[1]/div[2]/div[1]/div[2]/form/div[3]/div/div/input'),
    # 出生日期
    'mobile':(By.XPATH,'//*[@id="home newFiles"]/div[1]/div[2]/div[1]/div[2]/form/div[4]/div/div/input'),
    # 手机号，非必填
    'id':(By.XPATH,'//*[@id="home newFiles"]/div[1]/div[2]/div[1]/div[2]/form/div[5]/div/div/input'),
    # 身份证号码，非必填
    'sava_info':(By.XPATH,'//*[@id="home newFiles"]/div[1]/div[2]/div[2]/button[1]/span'),
    # 保存个人信息按钮
    'first_registration':(By.XPATH, '//*[@id="home newFiles"]/div[1]/div[2]/div[2]/button[2]/span'),
    # 首诊挂号按钮
    'registration_type_normal':(By.XPATH,'//*[@id="home newFiles"]/div[4]/div/div[2]/div[1]'),
    # 常规
}

process={
    'default_position': (By.XPATH, '//*[@id="home"]/div[1]/div[3]/div[2]/div/div[2]/div/div/a'),
    # 视力检验的默认位置
    'eyesight-check': (By.XPATH, '//*[@id="home"]/div[1]/div[3]/div[1]/div/div[2]/div[3]/div'),
    # 视力检验
    'check': (By.XPATH, '//*[@id="home"]/div[1]/div[3]/div[1]/div/div[2]/div[4]/div/a'),
    # 问诊
    'universal_button':(By.XPATH,'//*[@id="home"]/div[1]/div[4]/button'),
    # 通用按钮，包括创建检查单、开始检查、完成检查
    'confirm_check':(By.XPATH,'//*[@id="nopaddingD"]/div/div[2]/div/button'),
    # 确认开单
    'eyesight_type':(By.XPATH,'//*[@id="VisionTest"]/div/div[2]/table/tbody/tr[2]/td[1]/div[3]/label'),
    # 视标类型，当前视标为C视标
    'right_eye_far_eyesight':(By.XPATH,'//*[@id="VisionTest"]/div/div[2]/table/tbody/tr[2]/td[3]/div/div/input'),
    # 右眼远视力（裸眼)
    'right_eye_far_eyesight_li': (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li'),
    # 右眼远视力（裸眼)列表li
    'next_one': (By.XPATH, '//*[@id="home"]/div/div[2]/div[3]/div/button'),
    # 下一个
    'choose_doctor': (By.XPATH, '//*[@id="home"]/div[2]/div/div[2]/div'),
    # 选择医生
     'start_check': (By.XPATH, '//*[@id="home"]/div[1]/div[5]/button'),
    # 开始问诊、开始诊断
    'start_check_again': (By.XPATH, '//*[@id="home"]/div/div[4]/button'),
    # 开始问诊、开检查单
    'regular_check': (By.XPATH, '//*[@id="Inquery"]/div/div[2]/table/tbody/tr[1]/td[2]/div/label[1]'),
    # 定期检查
    'OCTBv1000':(By.XPATH,'//*[@id="home"]/div[1]/div[3]/div[1]/div/div[2]/div[3]/div/a'),
    # OCTBv1000
    'reverse_order': (By.XPATH, '//*[@id="home"]/div/div[2]/div/div[2]/div[1]/button'),
    # 时间倒序
    'locate_client': (By.XPATH, '//*[@id="home"]/div/div[2]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]'),
    # 定位刚刚诊断过的患者
    'add_check':(By.XPATH,'//*[@id="home"]/div/div[4]/button[1]'),
    # 添加诊断
    'add_check_item_button': (By.XPATH, '//*[@id="home"]/div[1]/div[4]/button[2]'),
    # 添加诊断条目按钮
    'macular_degeneration': (By.XPATH, '//*[@id="home"]/div[2]/div/div/section/div/div[1]/div[2]/div[1]/div[2]/div/div[1]'),
    # 黄斑变性
    'add_check_item': (By.XPATH, '//*[@id="TreatmentPlan"]/div/div[3]/div[2]/div/div[1]/div[3]/table/tbody/tr/td[3]/div/button'),
    # 添加诊断条目
    'eyes': (By.XPATH, '//*[@id="home"]/div[3]/div/div[2]/form/div[2]/div/div/div/input'),
    # 眼别下拉框
    'eyes_li': (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li'),
    # 眼别列表li
    'related_check_item': (By.XPATH, '//*[@id="home"]/div[3]/div/div[2]/form/div[3]/div/div/div/input'),
    # 关联检查项下拉框
    'related_check_item_li': (By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li'),
    # 关联检查项列表li
    'save': (By.XPATH, '//*[@id="home"]/div[3]/div/div[3]/span/button[2]'),
    # 保存按钮
    'assert_check': (By.XPATH, '//*[@id="home"]/div[1]/div[4]/button[1]'),
    # 确认诊断
    'assert_plan': (By.XPATH, '//*[@id="home"]/div[1]/div[4]/button'),
    # 直接确认方案
    'save_again': (By.XPATH, '//*[@id="home"]/div[4]/div/div[2]/div[2]/button[2]'),
    # 保存按钮
    'reservation_for_check': (By.XPATH, '//*[@id="TreatmentPlan"]/div/div[2]/div[1]/div[4]/div/div[2]/button'),
    # 预约复查
    'reservation_date': (By.XPATH, '//*[@id="home"]/div[5]/div/div[2]/div[1]/div/input'),
    # 预约日期
    'reservation_date_save': (By.XPATH, '//*[@id="home"]/div[5]/div/div[2]/div[1]/span'),
    # 点击空白处保存
    'reservation_mobile': (By.XPATH, '//*[@id="home"]/div[5]/div/div[2]/div[3]/div/input'),
    # 预约的手机号
    'reservation_content': (By.XPATH, '//*[@id="home"]/div[5]/div/div[2]/div[4]/div/div[2]/input'),
    # 复查内容下拉框
    'reservation_content_li': (By.XPATH, '/html/body/div[7]/div[1]/div[1]/ul/li'),
    # 复查内容列表li
    'reservation_save': (By.XPATH, '//*[@id="home"]/div[5]/div/div[2]/div[5]/button[2]'),
    # 预约保存按钮

}

