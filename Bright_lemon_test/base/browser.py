from selenium import webdriver


class Browser(object):

    def __init__(self):
        self.Chrome_options_ui = None
        self.Chrome_options_headless = None

    def browser_ui(self):
        """设置浏览器的属性，去掉“chrome正受到自动化测试软件的控制”的提示文字"""
        self.Chrome_options_ui = webdriver.ChromeOptions()
        self.Chrome_options_ui.add_experimental_option('useAutomationExtension', False)
        self.Chrome_options_ui.add_experimental_option('excludeSwitches', ['enable-automation'])
        prefs = {"": "", 'credentials_enable_service': False, 'profile.password_manager_enabled': False}
        self.Chrome_options_ui.add_experimental_option('prefs', prefs)  # 关闭chrome浏览器提示保存密码的弹窗
        return self.Chrome_options_ui


    def browser_headless(self):
        """设置浏览器属性为无头浏览器，由于没有界面，所以不需要去掉提示文字，headless、window-size"""
        self.Chrome_options_headless = webdriver.ChromeOptions()
        self.Chrome_options_headless.add_argument('--headless')
        self.Chrome_options_headless.add_argument("--window-size=1920,1080")  # 设置浏览器的窗口大小，根据自己的电脑尺寸设置
        return self.Chrome_options_headless
