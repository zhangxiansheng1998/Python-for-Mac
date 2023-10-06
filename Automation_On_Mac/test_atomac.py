import atomac
import time


atomac.launchAppByBundleId('paydar.ios.huijinwei')
print('项目已启动')

time.sleep(3)
atomac.terminateAppByBundleId('paydar.ios.huijinwei')
print('项目已关闭')

