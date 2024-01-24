import subprocess
# 获取所有进程列表
output = subprocess.check_output("tasklist", shell=True)
# 搜索目标进程并获取其PID
for line in output.splitlines():
    if b"Appium.exe" in line:
        pid = int(line.split(None, 1)[1].split()[0])
        break
else:
    print("Appium.exe has not been started.")
    exit()
# 结束目标进程
subprocess.call(f"taskkill /PID {pid} /F")
