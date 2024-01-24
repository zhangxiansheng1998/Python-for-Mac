

def run():
    print('正在生成一笔订单，请稍等')
    print("具体实现代码XXX：")
    keyword = input("已生成一笔订单，请问您是否需要继续生成？[是/否]")
    while True:
        if keyword == '是':
            print("具体实现代码XXX：")
            keyword = input("已生成一笔订单，请问您是否需要继续生成？[是/否]")
            while True:
                if keyword == '是':
                    print("具体实现代码XXX：")
                    keyword = input("已生成一笔订单，请问您是否需要继续生成？[是/否]")
                else:
                    break
        if keyword == '否':
            print("程序已结束,即将关闭窗口")
            break

        if keyword != '是' or '否':
            keyword = input("输入有误，请重新输入[是/否]")

run()

