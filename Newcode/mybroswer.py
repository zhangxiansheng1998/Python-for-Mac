import time

from selenium import webdriver

dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
dr.maximize_window()
time.sleep(3)
dr.quit()