from selenium.webdriver.common.by import By

website={'url':'https://jsfk-console-test.bigvisiontech.com/login'}

login_element={
    'account_button':(By.XPATH,'//*[@id="login_box"]/div/div[1]/img'),
    'username_ele':(By.XPATH,'//*[@id="login_form_pwd"]/div[1]/div/div/input'),
    'password_ele':(By.XPATH,'//*[@id="login_form_pwd"]/div[2]/div/input'),
    'login_button': (By.XPATH, '//*[@id="login_form_pwd"]/div[3]/button[1]')
}

system_name={'authorization':(By.XPATH,'//*[@id="projectList"]/div/div[2]/div[1]/div/img'), # 亮柠檬认证授权管理系统
             'lemon_management':(By.XPATH,'//*[@id="projectList"]/div/div[2]/div[2]/div/img'), # 亮柠檬管理系统
             'shop':(By.XPATH,'//*[@id="projectList"]/div/div[2]/div[3]/div/img'), # 亮柠檬门店系统
             'check':(By.XPATH,'//*[@id="projectList"]/div/div[2]/div[4]/div/img'), # 亮柠檬阅片系统
             'bigvision_management':(By.XPATH,'//*[@id="projectList"]/div/div[2]/div[5]/div/img') # CRM系统
}