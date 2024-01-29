import time
from PIL import ImageGrab
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://h.thinkermen.com/wincc_xingeercc/mini2021_1.6.9/index.php?r=finance/payOrder&gid=1433")
driver.find_element_by_id('loginname').send_keys('admin')
driver.find_element_by_id('nloginpwd').send_keys('123456')
print("\n登录成功！")
time.sleep(15)

left = 1000  # 左上角横坐标
top = 300      # 左上角纵坐标
right = 1920 # 右下角横坐标，这里假设屏幕宽度为1920
bottom = 600 # 右下角纵坐标，这里假设要截取的高度为100像素

# 使用ImageGrab模块截取屏幕上指定区域的图像
screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

# 保存截图为文件
screenshot.save("screenshot.png")

driver.quit()