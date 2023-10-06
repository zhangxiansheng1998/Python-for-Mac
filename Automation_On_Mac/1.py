import time
import pyautogui
import atomac


def simulate_key_press(a, b):
    atomac.launchAppByBundleId('paydar.ios.huijinwei')
    print('项目已启动')
    # 模拟按下指定的键
    pyautogui.click(x=a, y=b)
    time.sleep(3)
    print('已点击')
    time.sleep(3)
    atomac.terminateAppByBundleId('paydar.ios.huijinwei')
    print('项目已关闭')


if __name__ == "__main__":
    # 示例：模拟按下 A 键
    simulate_key_press(100, 200)
