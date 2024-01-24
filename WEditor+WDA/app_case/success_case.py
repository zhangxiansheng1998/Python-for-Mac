import wda

c = wda.Client('http://localhost:8100') # 8100为启动WDA设置的端口号
# c.app_current() # 显示当前应用信息，主要用于获取bundleId，也可以使用tidevice ps 命令
c.session().app_activate("com.apple.Preferences")  # 打开设置
# c.session().app_terminate("com.apple.Preferences") # 退出设置
c(name="搜索").set_text("NFC")  # 搜索 NFC
c(name="NFC").click() # 点击NFC
c(xpath='//Switch').exists # 判断NFC开关是否存在
c(xpath='//Switch').get().value # 获取NFC开关状态