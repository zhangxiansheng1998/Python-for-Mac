class Driver():

    def __init__(self):
        self.desired_caps = None

    def android_driver_property(self):
        """配置安卓12（模拟器）"""
        self.desired_caps = {
            'platformName': 'Android',
            'deviceName': '127.0.0.1:16384',
            # 这里版本号只能写9，不能写成9.0，否则会报错
            'platformVersion': '12',
            # apk的Package包
            'appPackage': 'com.tencent.xin',
            # apk的Activity界面
            'appActivity': 'io.dcloud.PandoraEntryActivity',
            # Android10以上必填,不填appium会报错
            'automationName': 'UiAutomator2'
        }
        return self.desired_caps

    def ios16_driver_property(self):
        """配置iPhone 8"""
        self.desired_caps = {
            'platformName': 'ios',
            'platformVersion': '16.4.1',
            'deviceName': 'iPhone 8',
            # ipa包名
            'bundleId': 'com.tencent.xin',
            # 设备udid
            'udid': '9dde9a1c9c3c01a1cbac0dd36339278a527f7235',
            'automationName': 'XCUITest'
        }
        return self.desired_caps

    def ios17_driver_property(self):
        """配置iPhone 13 Pro Max"""
        self.desired_caps = {
            'platformName': 'ios',
            'platformVersion': '17.0.3',
            'deviceName': 'iPhone 13 Pro Max',
            # ipa包名
            'bundleId': 'com.tencent.xin',
            # 设备udid
            'udid': '00008110-000155691AF2801E',
            'automationName': 'XCUITest'
        }
        return self.desired_caps



