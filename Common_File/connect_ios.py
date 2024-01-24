from appium import webdriver
import time

desired_caps = {
    'platform': 'iOS',  # 使用 'iOS' 而不是 'platformName'
    'platformVersion': 'your_ios_version',
    'deviceName': 'your_device_name',
    'app': 'path/to/your/app',
    'automationName': 'XCUITest',
    'udid': 'your_device_udid',
    'xcodeOrgId': 'your_team_id',
    'xcodeSigningId': 'iPhone Developer'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 在这里编写测试操作，例如点击、输入等
# 示例：点击某个元素
# driver.find_element_by_id('your_element_id').click()

time.sleep(5)  # 等待一段时间，确保测试操作完成

driver.quit()
