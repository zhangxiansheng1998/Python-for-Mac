import os
import time
from pathlib import Path

def run():
    Mytime = time.strftime("%Y-%m-%d~%H-%M-%S")
    print("程序开始运行")
    filename = input("请输入您要运行的jmx文件名：")
    jmx_path = "/Volumes/Disk/apache-jmeter-5.1.1/jmeter/jmx"
    path = "/Volumes/Disk/apache-jmeter-5.1.1/jmeter/jmx/{}.jmx".format(filename)

    # 判断文件是否存在
    while True:
        if os.path.exists(path):
            print('文件名输入正确，请稍等')
            os.system(
                "jmeter -n -t /Volumes/Disk/apache-jmeter-5.1.1/jmeter/jmx/{}.jmx -l /Volumes/Disk/apache-jmeter-5.1.1/jmeter/jtl/{}.jtl -e -o /Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/{}"
                    .format(filename, Mytime, Mytime))
            linkName = Path('/Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/' + Mytime + '/index.html').as_uri()
            print("已生成测试报告，具体内容可点击超链接",linkName)
            report_path = Path('/Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/'+ Mytime).as_uri()
            print("测试报告路径：", report_path)

            keyword = input("您是否需要继续运行[是/否]")

            while True:
                if keyword == '是':
                    new_Mytime = time.strftime("%Y-%m-%d~%H-%M-%S")
                    new_filename = input("请输入您要运行的jmx文件名：")
                    new_path = "/Volumes/Disk/apache-jmeter-5.1.1/jmeter/jmx/{}.jmx".format(new_filename)
                    if os.path.exists(new_path):
                        print('文件名输入正确，请稍等')
                        os.system(
                            "jmeter -n -t /Volumes/Disk/apache-jmeter-5.1.1/jmeter/jmx/{}.jmx -l /Volumes/Disk/apache-jmeter-5.1.1/jmeter/jtl/{}.jtl -e -o /Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/{}"
                                .format(new_filename, new_Mytime, new_Mytime))
                        linkName = Path('/Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/' + new_Mytime + '/index.html').as_uri()
                        print("已生成测试报告，具体内容可点击超链接", linkName)
                        report_path = Path('/Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/' + new_Mytime).as_uri()
                        print("测试报告路径：", report_path)
                        keyword = input("您是否需要继续运行[是/否]")
                    else:
                        print("当前目录下{}不存在{}.jmx文件".format(jmx_path,new_filename))
                        new_path = "/Volumes/Disk/apache-jmeter-5.1.1/jmeter/jmx/{}.jmx".format(new_filename)

                if keyword == '否':
                    print("程序已结束,即将关闭窗口")
                    time.sleep(3)
                    break

                if keyword != '是' or '否':
                    keyword = input("输入有误，请重新输入[是/否]")
            break

        else:
            filename = input("当前目录下{}不存在{}.jmx文件，请重新输入：".format(jmx_path,filename))
            path = "/Volumes/Disk/apache-jmeter-5.1.1/jmeter/jmx/{}.jmx".format(filename)

run()

