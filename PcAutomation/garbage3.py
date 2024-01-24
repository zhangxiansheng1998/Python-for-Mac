import os
import subprocess

output = subprocess.check_output("adb connect 127.0.0.1:16384", shell=True)
output.decode('gbk')
string_data = output.decode('utf-8')

def find_substring_in(s, string_data):
    if s in string_data:
        print("adb已经连接模拟器")
    else:
        print("adb还没有连接模拟器,正在连接中")
        #os.system("adb connect 127.0.0.1:16384")
find_substring_in("already connected to 127.0.0.1:16384",string_data)


