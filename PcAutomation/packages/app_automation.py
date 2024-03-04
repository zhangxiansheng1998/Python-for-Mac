import win32gui
from appium import webdriver
from Appium.page_object.login_page import *
from Appium.base.appium_base_page import *
from selenium import webdriver
import subprocess


class Auto(Basepage):
    """selenium版本不能过高4.0以上，也不能过低3.0以下，当前版本3.141.0兼容性较好，不容易报错"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def create_driver(self, host='127.0.0.1', port=4723):
        # 配置信息
        # 包含：平台名、系统、应用程序的绝对路径
        desired_caps = {'platformName': 'Windows',
                        'deviceName': 'WindowsPC',
                        'app': r'C:\Users\小平のNotebook\AppData\Local\Programs\Appium\Appium.exe',
                        'ms:waitForAppLaunch': '10',  # 如果WinAppDriver没有找到启动的app，就会报错，这段代码可以让其等待一段时间，单位秒，而且是强制等待
                        }
        # 开启WinAppDriver服务,如果不开启，将无法打开应用程序
        os.startfile(r'D:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe')
        # 打开应用程序
        self.driver = webdriver.Remote('http://{}:{}'.format(host, port), desired_caps)

    def open_appium(self):
        self.explicitly_wait((By.XPATH, '/Pane/Document/Edit[2]'), 30)  # 必须使用显示等待，隐式等待和强制等待都会报错
        self.backspace((By.XPATH, '/Pane/Document/Edit[2]'))  # 全选并删除端口号
        self.input((By.XPATH, '/Pane/Document/Edit[2]'), '4722')  # 输入端口号4722
        self.click((By.XPATH, '/Pane/Document/Button[4]'))  # 启动appium服务器
        self.wait(2)
        print("正在关闭appium")

    def open_postman(self):
        os.startfile(r'C:\Users\小平のNotebook\AppData\Local\Postman\Postman.exe')
        #self.handle = win32gui.FindWindow(None, u'Chrome_WidgetWin_1')

        # GetDesktopWindow 获得代表整个屏幕的一个窗口（桌面窗口）句柄
        hd = win32gui.GetDesktopWindow()
        # 获取所有子窗口
        hwndChildList = []
        win32gui.EnumChildWindows(hd, lambda hwnd, param: param.append(hwnd), hwndChildList)

        for hwnd in hwndChildList:
            if win32gui.GetWindowText(hwnd) == "Postman":
                print("句柄：", hwnd, "标题：", win32gui.GetWindowText(hwnd))
                break
        hwnd = win32gui.FindWindow(0, win32gui.GetWindowText(hwnd))  # 寻找窗口
        if not hwnd:
            print("找不到该窗口")
        else:
            win32gui.SetForegroundWindow(hwnd)  # 前置窗口

        print("已切换窗口")
        self.explicitly_wait((By.XPATH, '/Pane[3]/TitleBar/Button[2]'), 30)  # 必须使用显示等待，隐式等待和强制等待都会报错
        self.click((By.XPATH, '/Pane[3]/TitleBar/Button[2]'))  # 放大窗口
        self.click((By.XPATH, '/Pane/Document/Pane/Document/Group/Group[4]/Group[6]/Text[1]'))  # 选择jsfk
        print('已点击jsfk')
        self.click((By.XPATH, '/Pane/Document/Pane/Document/Group/Group[4]/Group[6]/Text[7]'))  # 点击login接口
        print('已点击login接口')
        self.click((By.XPATH, '/Pane/Document/Pane/Document/Group/Group[4]/Group[7]/Group[7]/Group[5]'))  # 点击发送按钮
        print('已点击发送接口')
        self.wait(2)
        print("正在关闭postman")


    def close_driver(self):
        output = subprocess.check_output("tasklist", shell=True)
        # 搜索目标进程并获取其PID
        for line in output.splitlines():
            if b"WinAppDriver.exe" in line:
                pid = int(line.split(None, 1)[1].split()[0])
                print('正在关闭WinAppDriver')
                break
        else:
            print("WinAppDriver.exe has not been started.")
            exit()
        # 结束目标进程
        subprocess.call(f"taskkill /PID {pid} /F")


if __name__ == '__main__':
    driver = None
    auto = Auto(driver)
    auto.create_driver()
    auto.open_appium()
    auto.open_postman()
    auto.close_driver()
