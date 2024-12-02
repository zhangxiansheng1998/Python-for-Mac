""""
BasePage类是POM中的基类，主要用于提供常用的函数为页面对象进行服务
"""
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.by import By
import os
from datetime import datetime
from PIL import Image
import io


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeformate = time.strftime("%Y-%m-%d~%H-%M-%S")
        self.current_date = datetime.now().strftime("%Y-%m-%d")

    def visit(self, url):
        """访问网页"""
        try:
            self.driver.get(url)
        except Exception as e:
            print("\n输入的URL地址{}不正确，请重新输入".format(url))
            print("\n捕获的异常信息为:", e)

    def locator(self, loc):
        """定位单个元素"""
        return self.driver.find_element(*loc)

    def locators(self, loc):
        """定位一组元素"""
        return self.driver.find_elements(*loc)

    def input(self, loc, txt):
        """输入"""
        return self.locator(loc).send_keys(txt)

    def click(self, loc):
        """点击某个元素"""
        return self.locator(loc).click()

    def wait(self, seconds):
        """强制等待"""
        time.sleep(seconds)

    def implicitly_wait(self, seconds):
        """隐式等待，只需设置一次，全局有效，每隔0.5s查询一次"""
        self.driver.implicitly_wait(seconds)

    def explicitly_wait(self, loc, seconds):
        """显式等待   loc：元素   seconds：等待时间"""
        WebDriverWait(self.driver, seconds).until(lambda x: x.find_element(*loc))

    def max(self):
        """放大窗口"""
        self.driver.maximize_window()

    def select_all_windows(self, loc):
        """全选"""
        self.driver.find_element(*loc).send_keys(Keys.CONTROL, 'a')

    def copy_windows(self, loc):
        """复制"""
        self.driver.find_element(*loc).send_keys(Keys.CONTROL, 'c')

    def paste_windows(self, loc):
        """粘贴"""
        self.driver.find_element(*loc).send_keys(Keys.CONTROL, 'v')

    def backspace_windows(self, loc):
        """删除"""
        self.select_all_windows(loc)
        self.driver.find_element(*loc).send_keys(Keys.BACKSPACE)

    def select_all_macos(self, loc):
        """全选"""
        self.driver.find_element(*loc).send_keys(Keys.COMMAND, 'a')

    def copy_macos(self, loc):
        """复制"""
        self.driver.find_element(*loc).send_keys(Keys.COMMAND, 'c')

    def paste_macos(self, loc):
        """粘贴"""
        self.driver.find_element(*loc).send_keys(Keys.COMMAND, 'v')

    def backspace_macos(self, loc):
        """删除"""
        self.select_all_macos(loc)
        self.driver.find_element(*loc).send_keys(Keys.BACKSPACE)

    def js_scroll_bottom(self):
        """浏览器滚动到底部"""
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)

    def js_scroll_top(self):
        """浏览器滚动到顶部"""
        js = "var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)

    def screen(self):
        """截图"""
        self.driver.get_screenshot_as_file(u"../picture/" + self.timeformate + ".png")

    def get_text(self, loc):
        """获取元素对应的文本内容(元素本身有内容)"""
        return self.locator(loc).text

    def get_value(self, loc):
        """获取元素value属性中文本内容(元素本身没有内容，但是value值有内容)"""
        return self.locator(loc).get_attribute("value")

    def get_li_value(self,ul_class,value):
        """点击下拉框中某个特定的值   ul_class：ul的class值   value：要查询的值"""
        self.driver.find_element_by_xpath('//ul[@class="{}"]/li/span[contains(text(),"{}")]'.format(ul_class,value)).click()

    def screen_template(self, loc):
        """定位失败时，截图并关闭浏览器"""
        self.driver.get_screenshot_as_file(u"../picture/failure/" + self.timeformate + ".png")
        print('\n未定位到元素:{element}, 已截图'.format(element=loc))
        self.driver.quit()

    def locator_png(self, loc):
        """定位单个元素（如果报错，会自动截图）"""
        try:
            return self.driver.find_element(*loc)
        except:
            self.screen_template(loc)

    def locators_png(self, loc):
        """定位一组元素（如果报错，会自动截图）"""
        try:
            return self.driver.find_elements(*loc)
        except:
            self.screen_template(loc)

    def click_png(self, loc):
        """点击某个元素（如果报错，会自动截图）"""
        try:
            self.locator(loc).click()
        except:
            self.screen_template(loc)

    def input_png(self, loc, txt):
        """输入内容（如果报错，会自动截图）"""
        try:
            self.locator(loc).send_keys(txt)
        except:
            self.screen_template(loc)

    def get_text_png(self, loc):
        """获取元素对应的文本内容（如果报错，会自动截图）"""
        try:
            return self.locator(loc).text
        except:
            self.screen_template(loc)

    def quit(self):
        """退出浏览器"""
        self.wait(1)
        self.driver.quit()

    def assert_text_equal(self, expectation, reality):
        """断言元素本身对应的文本内容   expectation：预期值   reality：实际值（传入元素）"""
        global new_reality
        try:
            new_reality = self.get_text(reality)
            assert expectation == new_reality
            print("\n断言成功! 预期值'{}'与实际值'{}'一致".format(expectation, new_reality))
        except Exception as e:
            print("\n断言失败! 预期值'{}'与实际值'{}'不一致".format(expectation, new_reality))
            assert False

    def assert_value_equal(self, expectation, reality):
        """断言元素value属性中的文本内容   expectation：预期值   reality：实际值（传入元素）"""
        global new_reality
        try:
            new_reality = self.get_value(reality)
            assert expectation == new_reality
            print("\n断言成功! 预期值'{}'与实际值'{}'一致".format(expectation, new_reality))
        except Exception as e:
            print("\n断言失败! 预期值'{}'与实际值'{}'不一致".format(expectation, new_reality))
            assert False

    def imitate_two_keyboard(self):
        """模拟键盘按键"""
        try:
            #pyautogui.press('f12')
            print('暂未使用')
        except Exception as e:
            print("\n按键失败!捕获到相应的异常为：",e)
            assert False

    def switch_to_newest_window(self):
        """切换浏览器最新一个窗口句柄"""
        try:
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[-1])
        except Exception as e:
            print("\n窗口切换失败!捕获到相应的异常为：",e)
            assert False

    def get_ul_number(self, ul):
        """获取ul列表的个数"""
        try:
            ul_list = self.locator(ul)
            li_list = ul_list.find_elements(By.TAG_NAME,'ul')
            return len(li_list)
        except Exception as e:
            print("\n元素定位失败!捕获到相应的异常为：",e)
            assert False

    def erp_order_screenshot(self, myTime):
        """截图"""
        screenshot_root = "picture"
        # 设置截图保存的根目录
        screenshot_folder = os.path.join(screenshot_root, self.current_date)
        # 拼接保存截图的文件夹路径
        os.makedirs(screenshot_folder, exist_ok=True)
        # 创建文件夹（如果不存在）
        screenshot_path = os.path.join(screenshot_folder, f"{myTime}.png")
        self.driver.save_screenshot(screenshot_path)

    def partial_screenshot(self,left,upper,right,lower):
        screenshot = self.driver.get_screenshot_as_png()
        screenshot_img = Image.open(io.BytesIO(screenshot))
        partial_screenshot = screenshot_img.crop((left, upper, right, lower))
        today = datetime.today()
        month_formatted_date = today.strftime("%Y-%m")
        formatted_date = today.strftime("%Y-%m-%d")
        month_folder_path = os.path.join('../report', month_formatted_date)
        folder_path = os.path.join('../report', month_formatted_date, formatted_date)

        # 检查目录是否已经存在，如果不存在则创建
        if not os.path.exists(month_folder_path):
            os.makedirs(month_folder_path)
            print(f"文件夹'{month_formatted_date}'创建成功")

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"文件夹'{formatted_date}'创建成功")


        partial_screenshot.save(f"../report{month_formatted_date}/{formatted_date}/partial_screenshot.png")

    def close(self):
        """关闭浏览器窗口"""
        self.driver.close()

