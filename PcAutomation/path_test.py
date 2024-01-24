import os


def run():
    print("程序开始运行")
    filename = input("请输入您要运行的jmx文件名：")
    path = "D:/apache-jmeter-5.1/jmx/{}.jmx".format(filename)
    # 判断文件是否存在
    while True:
        if os.path.exists(path):
            print('文件存在，程序运行中！')
            break
        else:
            filename = input("当前目录下不存在{}.jmx文件，请重新输入：".format(filename))
            path = "D:/apache-jmeter-5.1/jmx/{}.jmx".format(filename)


run()