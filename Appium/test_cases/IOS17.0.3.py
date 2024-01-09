from time import sleep
from appium import webdriver

desired_caps = {
                'platformName': 'ios',
                'platformVersion': '17',
                'deviceName': 'iPhone 13 Pro Max',
                # ipa包名
                'bundleId': 'paydar.ios.huijinwei',
                # 设备udid
                'udid': '00008110-000155691AF2801E',
                'automationName': 'XCUITest'
                }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
# 如果运行后提示'platformName' can't be blank，因为appium-python-client版本太高导致的
# 降级即可，与此同时selenium的版本也会随之降级 pip3 install appium-python-client==1.1.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
print('程序开始')
sleep(5)
driver.quit()
print('程序结束')
