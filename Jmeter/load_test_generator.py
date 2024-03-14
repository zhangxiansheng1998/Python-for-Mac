import os
import re
import time
from pathlib import Path


def modify_jmx_file(file_path, new_num_threads):
    """修改jmx文件中的线程数"""
    with open(file_path, 'r') as file:
        jmx_content = file.read()

    # 使用正则表达式匹配并替换数字
    pattern = r'<stringProp name="ThreadGroup.num_threads">(\d+)</stringProp>'
    replacement = f'<stringProp name="ThreadGroup.num_threads">{new_num_threads}</stringProp>'
    modified_content = re.sub(pattern, replacement, jmx_content, count=1)

    # 将修改后的内容写回文件
    with open(file_path, 'w') as file:
        file.write(modified_content)

    print(f"已成功将线程数量修改为：{new_num_threads}")


def read_jmx_tread(file_path):
    """读取jmx文件中的线程数"""
    with open(file_path, 'r') as file:
        jmx_content = file.read()

    # 使用正则表达式匹配并替换数字
    pattern = r'<stringProp name="ThreadGroup.num_threads">(\d+)</stringProp>'
    match = re.search(pattern, jmx_content)

    if match:
        thread_count = match.group(1)  # group(1) 提取括号中的匹配内容
        print(f"当前文件线程数为: {thread_count}")
    else:
        print("未找到线程数")


def run(filename):
    print("程序开始运行")
    answer = input("是否需要修改线程数【是/否】")
    if answer == "是":
        try:
            # 尝试获取用户输入的数字
            num_threads = int(input("请输入新的线程数："))
            # 如果输入成功，则更新线程数
            modify_jmx_file(filename, num_threads)
        except ValueError:
            # 如果输入的不是数字，则捕获异常并打印错误信息
            print("输入的不是一个有效的数字，线程数保持不变。")
    elif answer == "否":
        # 如果用户输入否，则不修改线程数，并打印信息
        print("不修改线程数")
        read_jmx_tread(filename)
    else:
        # 如果用户输入既不是是也不是否，则打印提示信息
        print("输入有误，请输入是或否")

    Mytime = time.strftime("%Y-%m-%d~%H-%M-%S")
    path = "{}".format(filename)

    # 判断文件是否存在
    while True:
        if os.path.exists(path):
            os.system(
                "jmeter -n -t {} -l /Volumes/Disk/apache-jmeter-5.1.1/jmeter/jtl/{}.jtl -e -o /Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/{}"
                .format(filename, Mytime, Mytime))
            linkName = Path('/Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/' + Mytime + '/index.html').as_uri()
            print("已生成测试报告，具体内容可点击超链接", linkName)
            report_path = Path('/Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/' + Mytime).as_uri()
            print("测试报告路径：", report_path)

            keyword = input("您是否需要继续运行【是/否】")

            while True:
                if keyword == '是':
                    answer = input("是否需要修改线程数【是/否】")
                    if answer == "是":
                        try:
                            # 尝试获取用户输入的数字
                            num_threads = int(input("请输入新的线程数："))
                            # 如果输入成功，则更新线程数
                            modify_jmx_file(filename, num_threads)
                        except ValueError:
                            # 如果输入的不是数字，则捕获异常并打印错误信息
                            print("输入的不是一个有效的数字，线程数保持不变。")
                    elif answer == "否":
                        # 如果用户输入否，则不修改线程数，并打印信息
                        print("不修改线程数")
                        read_jmx_tread(filename)
                    else:
                        # 如果用户输入既不是是也不是否，则打印提示信息
                        print("输入有误，请输入是或否")

                    new_Mytime = time.strftime("%Y-%m-%d~%H-%M-%S")
                    new_path = "{}".format(filename)
                    if os.path.exists(new_path):
                        os.system(
                            "jmeter -n -t {} -l /Volumes/Disk/apache-jmeter-5.1.1/jmeter/jtl/{}.jtl -e -o /Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/{}"
                            .format(filename, new_Mytime, new_Mytime))
                        linkName = Path(
                            '/Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/' + new_Mytime + '/index.html').as_uri()
                        print("已生成测试报告，具体内容可点击超链接", linkName)
                        report_path = Path('/Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/' + new_Mytime).as_uri()
                        print("测试报告路径：", report_path)

                    else:
                        print("当前目录下不存在{}.jmx文件".format(filename))

                    keyword = input("您是否需要继续运行【是/否】")

                if keyword == '否':
                    print("程序已结束,即将关闭窗口")
                    break

                if keyword != '是' and '否':
                    keyword = input("输入有误，请重新输入【是/否】")
            break

        else:
            filename = input("当前目录下不存在{}文件，请重新输入：".format(filename))
            path = "{}".format(filename)


# 运行的脚本路径
run('/Volumes/Disk/apache-jmeter-5.1.1/jmeter/jmx/jsfk.jmx')
