from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner')
driver.maximize_window()
js1 = "var q=document.documentElement.scrollTop=1000"
driver.execute_script(js1)
js2="return window.getComputedStyle(document.querySelector('.Virus_1-1-350_1KG-A3'),':before').getPropertyValue('content')"
res2 = eval(driver.execute_script(js2))  # eval()函数可以去除字符串里面的双引号
print(res2)
js3="return window.getComputedStyle(document.querySelector('.Virus_1-1-350_1KG-A3'),':after').getPropertyValue('content')"
res3 = eval(driver.execute_script(js3))
print(res3)
driver.quit()