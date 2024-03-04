import atomac
from time import sleep
from atomac.AXKeyCodeConstants import *
bundle_id = 'com.apple.Maps'

# bs = atomac.AXClasses.AXKeyCodeConstants.BACKSPACE
# part 1, 启动应用并获取应用信息
atomac.launchAppByBundleId(bundle_id)
sleep(2)
ato = atomac.getAppRefByBundleId(bundle_id)
print(ato)

# part 2, 获取当前应用windows
cur_win = ato.windows()[0]
print(cur_win)

# part 3, 查找元素
# findFirst，返回第一个匹配的元素
# findFirstR，递归查找，返回第一个匹配的元素（当查找的元素Parent非标准窗口时使用）
# 在AXClasses.py文件中可以找到很多已经定义好的方法
# dt = cur_win.radioButtonsR('地图')[0]   # 也可以
dt = cur_win.findFirstR(AXRole='AXRadioButton', AXTitle='地图')
gj = cur_win.findFirstR(AXRole='AXRadioButton', AXTitle='公交')
wx = cur_win.findFirstR(AXRole='AXRadioButton', AXTitle='卫星')


# part 6, 输入内容（输入键盘字符，US_keyboard）
s1 = cur_win.findFirstR(AXRole='AXTextField', AXRoleDescription='搜索文本栏')
s1_p = s1.AXPosition
s1_s = s1.AXSize
s1.tripleClickMouse((s1_p[0] + s1_s[0] / 2, s1_p[1] + s1_s[1] / 2))
s1.sendKeys('7983')

# part 7, 输入键盘上的修饰符
sleep(1)
s1.sendKeys([BACKSPACE])
# 回车
s1.sendKeys([RETURN])