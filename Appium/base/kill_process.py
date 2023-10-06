import subprocess
from Appium.base.appium_base_page import Basepage


class Kill_process(Basepage):

    def kill_appium(self):
        output = subprocess.check_output("tasklist", shell=True)
        for line in output.splitlines():
            if b"Appium.exe" in line:
                pid = int(line.split(None, 1)[1].split()[0])
                break
        else:
            print("Appium.exe has not been started.")
            exit()
        # 结束目标进程
        subprocess.call(f"taskkill /PID {pid} /F")
