from selenium.webdriver.common.by import By

module={
    'open_school_first_module':(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/div[1]/div/ul/div[3]/li/div'),
    # 基础数据管理
    'open_institution_second_module':(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div[1]/div/ul/div[3]/li/ul/div[2]/a/li'),
    # 筛查机构管理
}

search_institution={
    'institution_search_input':(By.XPATH,'//*[@id="header-box"]/div[1]/div[1]/input'),
    # 搜索框
    'institution_search_button':(By.XPATH,'//*[@id="header-box"]/div[1]/button[1]'),
    # 查询按钮
    'institution_reset_button':(By.XPATH,'//*[@id="header-box"]/div[1]/button[2]')
    # 重置按钮
}

edit_institution={
    'edit_institution_button':(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[8]/div/div/button[1]'),
    # 编辑按钮
    'institution_address':(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/section/div/div[4]/div/div[2]/form/div[4]/div/div/input'),
    # 详细地址
    'click_button':(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/section/div/div[4]/div/div[3]/span/button[2]')
    # 确定按钮
}

download_button={
    'download_wxcode_button':(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[8]/div/div/button[2]')
    # 下载筛查机构二维码按钮
}

