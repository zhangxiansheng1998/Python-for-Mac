class Driver():

    def __init__(self):
        self.desired_caps = None

    def driver_property(self):
        """配置雷电模拟器"""
        self.desired_caps = {
            'platformName': 'Android',
            'deviceName': '192.168.163.101:5555',
            # 这里版本号如果是9，只能写9，不能写成9.0，否则会报错
            'platformVersion': '7.1.2',
            # apk包名
            'appPackage': 'com.android.launcher3',
            # apk的launcherActivity
            'appActivity': '.Launcher',
            # 以下两行代码可以让输入框中能输入中文
            'unicodeKeyboard': 'True',
            'resetkeyboard': 'True'}
        return self.desired_caps
