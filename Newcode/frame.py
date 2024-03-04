from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('https://mail.qq.com/')
driver.maximize_window()
driver.switch_to.frame('login_frame')
sleep(1)
driver.find_element(By.XPATH, '//*[@id="u"]').send_keys('596137586')
sleep(1)
driver.find_element(By.XPATH, '//*[@id="p"]').send_keys('nihuochun698')
sleep(1)
driver.find_element(By.XPATH, '//*[@id="login_button"]').click()
driver.quit()
