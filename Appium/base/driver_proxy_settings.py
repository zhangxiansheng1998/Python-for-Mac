class Driver():

    def __init__(self):
        self.desired_caps = None

    def driver_property(self):
        """配置模拟器"""
        self.desired_caps = {
            'platformName': 'Android',
            'deviceName': '127.0.0.1:16384',
            # 这里版本号只能写9，不能写成9.0，否则会报错
            'platformVersion': '12',
            # apk的Package包
            'appPackage': 'com.android.settings',
            # apk的Activity界面
            'appActivity': 'com.android.settings.Settings',
            # Android10以上必填,不填appium会报错
            'automationName': 'UiAutomator2'
        }
        return self.desired_caps
