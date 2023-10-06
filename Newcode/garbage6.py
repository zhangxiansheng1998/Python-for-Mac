import time
import keyboard
import pyautogui
from selenium import webdriver



driver = webdriver.Chrome()
driver.get('http://admin.huijinwei.com/login')
driver.maximize_window()
#pyautogui.press('f9')
#keyboard.press('f12')
#keyboard.release('f12')

time.sleep(5)

driver.quit()
