from selenium.webdriver.common.by import By

website={'url':'https://jsfk-console-test.bigvisiontech.com/login'}

login_element={
    'username_ele':(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div/div/form/div[1]/div/div/input'),
    'password_ele':(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div/div/form/div[2]/div/div/input'),
    'login_button': (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div/form/div[3]/div/button')
}