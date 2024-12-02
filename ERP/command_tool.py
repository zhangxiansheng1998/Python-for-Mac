import os
import subprocess

keyword = '是'

while True:
    if keyword == '是':
        while True:
            try:
                # 定义命令选项
                print("===========命令选项================")
                print("【1】生成erp订单")
                print("【2】筑房人测试收款账号修改为徐鹏")
                print("【3】筑房人测试收款账号修改为倪浩平")
                print("【4】获取材神金服失败的订单")
                print("===================================")
                command_choice = int(input("请输入您要运行的命令选项:"))
                if command_choice not in [1, 2, 3, 4]:
                    print("输入的数字有误，请重新输入！")
                else:
                    break
            except ValueError:
                print("输入的不是数字，请重新输入！")

        if command_choice == 1:
            try:
                command = 'cd /Users/macbook_air/Desktop/MyProject/ERP && python3.8 generate_fixed_order.py'
                os.putenv('total_orders', '8')  # 修改环境变量的值
                result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
                print("命令【1】已执行！\n")
            except subprocess.CalledProcessError as e:
                print('\n命令执行过程中发生异常，异常信息如下：', e)
                print("stdout:", e.stdout)
                print("stderr:", e.stderr)
            keyword = input("是否需要继续运行【是/否】")

        elif command_choice == 2:
            try:
                command = 'cd /Users/macbook_air/Desktop/MyProject/ERP && python3.8 modify_account_info.py'
                os.putenv('user', '3')  # 修改环境变量的值
                result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
                print("命令【2】已执行！\n")
            except subprocess.CalledProcessError as e:
                print('\n命令执行过程中发生异常，异常信息如下：', e)
                print("stdout:", e.stdout)
                print("stderr:", e.stderr)
            keyword = input("是否需要继续运行【是/否】")

        elif command_choice == 3:
            try:
                command = 'cd /Users/macbook_air/Desktop/MyProject/ERP && python3.8 modify_account_info.py'
                os.putenv('user', '1')  # 修改环境变量的值
                result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
                print("命令【3】已执行！\n")
            except subprocess.CalledProcessError as e:
                print('\n命令执行过程中发生异常，异常信息如下：', e)
                print("stdout:", e.stdout)
                print("stderr:", e.stderr)
            keyword = input("是否需要继续运行【是/否】")

        elif command_choice == 4:
            try:
                command = ('cd /Users/macbook_air/Desktop/MyProject/ERP && python3.8 get_failed_orders.py && cat -b '
                           '/Users/macbook_air/Desktop/MyProject/ERP/result.txt')
                result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
                print("失败订单:\n", result.stdout)
                print("命令【4】已执行！\n")
            except subprocess.CalledProcessError as e:
                print('\n命令执行过程中发生异常，异常信息如下：', e)
                print("stdout:", e.stdout)
                print("stderr:", e.stderr)
            keyword = input("是否需要继续运行【是/否】")

    if keyword == '否':
        print("程序已结束,即将关闭窗口")
        break

    if keyword != '是' and '否':
        keyword = input("输入有误，请重新输入【是/否】")
