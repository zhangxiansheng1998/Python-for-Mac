import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://xytd1.cn/forum.php?mod=viewthread&tid=56911')
driver.maximize_window()
ele=driver.find_element(By.XPATH,'//*[@id="deanheader"]/div/div[4]/div/ul/li[2]/a')
ele.click()
driver.get('http://xytd1.cn/connect.php?mod=login&op=init&referer=http%3A%2F%2Fxytd1.cn%2Fforum.php%3Fmod'
           '%3Dviewthread%26tid%3D56911&statfrom=login')
# 扫二维码
time.sleep(15)
js = "var q=document.documentElement.scrollTop=13000"
driver.execute_script(js)
content = driver.find_element_by_xpath('//*[@id="fastpostmessage"]')
while True:
    content.send_keys('很棒的资源，受教了，希望能出一个更详细的教程{num}'.format(num=random.randint(1,100000)))
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[10]/div[8]/div[4]/div[17]/form/table/tbody/tr/td[2]/p/button/strong').click()
    time.sleep(16)











