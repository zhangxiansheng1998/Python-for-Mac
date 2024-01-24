import wda

# 终端需要运行命令 tidevice -u [设备的udid] wdaproxy -B [手机上webdriveragent的bundleId] --port 8100
# tidevice -u 9dde9a1c9c3c01a1cbac0dd36339278a527f7235 wdaproxy -B com.facebook.WebDriverAgentRunnerForZhangXianSheng.xctrunner --port 8100
# tidevice -u 00008110-000155691AF2801E wdaproxy -B com.facebook.WebDriverAgentRunnerForZhangXianSheng.xctrunner --port 8100

c = wda.Client('http://localhost:8100') # 8100为启动WDA设置的端口号

c.xpath('//*[@label="付哒"]').click()

print('已打开')