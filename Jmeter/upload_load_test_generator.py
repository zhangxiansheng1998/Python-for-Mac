import os
import time
from pathlib import Path
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def run():
    Mytime = time.strftime("%Y-%m-%d~%H-%M-%S")
    print("程序开始运行")
    print("请选择您要运行的jmx脚本：")
    root = Tk()
    root.withdraw()
    filename = askopenfilename()
    print("当前文件：", filename)
    jmx_path = "/Volumes/Disk/apache-jmeter-5.1.1/jmeter/jmx"
    path = "{}".format(filename)

    # 判断文件是否存在
    while True:
        if os.path.exists(path):
            os.system(
                "jmeter -n -t {} -l /Volumes/Disk/apache-jmeter-5.1.1/jmeter/jtl/{}.jtl -e -o /Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/{}"
                    .format(filename, Mytime, Mytime))
            linkName = Path('/Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/' + Mytime + '/index.html').as_uri()
            print("已生成测试报告，具体内容可点击超链接",linkName)
            report_path = Path('/Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/'+ Mytime).as_uri()
            print("测试报告路径：", report_path)

            keyword = input("您是否需要继续运行[是/否]")

            while True:
                if keyword == '是':
                    new_Mytime = time.strftime("%Y-%m-%d~%H-%M-%S")
                    new_root = Tk()
                    new_root.withdraw()
                    new_filename = askopenfilename()
                    new_path = "{}".format(new_filename)
                    if os.path.exists(new_path):
                        os.system(
                            "jmeter -n -t {} -l /Volumes/Disk/apache-jmeter-5.1.1/jmeter/jtl/{}.jtl -e -o /Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/{}"
                                .format(new_filename, new_Mytime, new_Mytime))
                        linkName = Path('/Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/' + new_Mytime + '/index.html').as_uri()
                        print("已生成测试报告，具体内容可点击超链接", linkName)
                        report_path = Path('/Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/' + new_Mytime).as_uri()
                        print("测试报告路径：", report_path)
                        keyword = input("您是否需要继续运行[是/否]")
                    else:
                        print("当前目录下不存在{}.jmx文件".format(new_filename))
                        new_path = "{}".format(new_filename)

                if keyword == '否':
                    print("程序已结束,即将关闭窗口")
                    time.sleep(3)
                    break

                if keyword != '是' or '否':
                    keyword = input("输入有误，请重新输入[是/否]")
            break

        else:
            filename = input("当前目录下不存在{}文件，请重新输入：".format(filename))
            path = "{}".format(filename)

run()

