import os
import time
from pathlib import Path
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Mytime = time.strftime("%Y-%m-%d~%H-%M-%S")
filename = r'/Volumes/Disk/apache-jmeter-5.1.1/jmeter/jmx/jsfk-it-local.jmx'
print("当前文件：", filename)
jmx_path = "/Volumes/Disk/apache-jmeter-5.1.1/jmeter/jmx"
path = "{}".format(filename)
os.system("jmeter -n -t {} -GGLOBAL_THREADS=10 -l /Volumes/Disk/apache-jmeter-5.1.1/jmeter/jtl/{}.jtl -e -o /Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/{}".format(filename, Mytime, Mytime))
linkName = Path('/Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/' + Mytime + '/index.html').as_uri()
print("已生成测试报告，具体内容可点击超链接",linkName)
report_path = Path('/Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/'+ Mytime).as_uri()
print("测试报告路径：", report_path)
