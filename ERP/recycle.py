from selenium import webdriver
from OCR import *

code_status=True

while True:
    driver = webdriver.Chrome()
    driver.get("http://zkcjcx.jxeea.cn/zkcjcx/")
    driver.maximize_window()

    code_verify()

