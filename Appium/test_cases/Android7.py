# coding=utf-8
from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {
                'platformName': 'Android',
                'deviceName': '192.168.254.103:5555',
                # 这里版本号只能写9，不能写成7.0，否则会报错
                'platformVersion': '7',
                # apk包名
                'appPackage': 'com.android.launcher3',
                # apk的launcherActivity
                'appActivity': '.Launcher',
                #以下两行代码可以让输入框中能输入中文
                'unicodeKeyboard':'True',
                'resetkeyboard':'True'
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
print('程序开始')
driver.start_activity('com.android.settings','.Settings')
sleep(3)
driver.quit()
print('程序结束')
