# coding=utf-8
from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {
                'platformName': 'Android',
                'deviceName': '192.168.254.103:5555',
                # 这里版本号只能写9，不能写成9.0，否则会报错
                'platformVersion': '9',
                # apk包名
                'appPackage': 'paydar.huijinwei',
                # apk的launcherActivity
                'appActivity': 'io.dcloud.PandoraEntryActivity',
                #以下两行代码可以让输入框中能输入中文
                'unicodeKeyboard':'True',
                'resetkeyboard':'True'
                }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
print('程序开始')
driver.start_activity('paydar.huijinwei','io.dcloud.PandoraEntryActivity')
driver.find_element(By.ID,'com.baidu.browser.apps:id/eqt').click()
driver.find_element(By.ID,'com.baidu.browser.apps:id/cdo').send_keys('中国')
driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/com.baidu.searchbox.widget.SlidingPaneLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView').click()
sleep(5)
driver.quit()
print('程序结束')
