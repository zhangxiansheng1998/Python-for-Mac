from appium import webdriver

desired_caps = {
    'platformName': 'iOS',
    'platformVersion': '14.5',
    'deviceName': 'iPhone 11',
    'app': '/path/to/your/app.app',
    'automationName': 'XCUITest',
    'udid': 'your_device_udid',
    'bundleId': 'your.bundle.identifier',
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

try:
    # 在这里编写你的测试步骤
    element = driver.find_element_by_id('your_element_id')
    element.click()

    # 等待一段时间
    driver.implicitly_wait(5)

    # 示例：验证标题文本
    title_element = driver.find_element_by_xpath('//XCUIElementTypeNavigationBar/XCUIElementTypeStaticText')
    assert title_element.text == 'Expected Title', 'Title verification failed'

finally:
    # 关闭Appium会话
    driver.quit()
