import subprocess
from Fudafu.base.appium_base_page import BasePage


class Connect_simulator(BasePage):
    output = subprocess.check_output("adb connect 127.0.0.1:16384", shell=True)
    output.decode('gbk')
    string_data = output.decode('utf-8')  # byte转string

    def find_substring_in(driver, s, sub):

        if s in sub:
            print("adb服务已启动，请稍等...")
        else:
            print("adb正在连接中，请等待...")
