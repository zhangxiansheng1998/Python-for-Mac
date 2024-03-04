from Appium.base.appium_base_page import *
import re


class LoginPage(BasePage):

    def check_login_out_status(self):
        """判断当前页面是否登录系统如果已登录，会退出当前账户；如果未登录，则给出相应提示"""
        try:
            expect_value = self.get_text((By.NAME, '扫一扫'))
            if expect_value == '扫一扫':
                print('当前处于登录状态，正在退出系统')
                self.click((By.NAME, '我的'))
                self.click((By.NAME, '系统设置'))
                self.click((By.NAME, '退出登录'))
                self.click((By.NAME, '确认'))
        except NoSuchElementException:
            print('当前处于未登录状态，无需退出系统')
        except Exception as e:
            print(f'当前程序发生异常，异常信息如下: {e}\n')

    def check_login_in_status(self):
        """判断当前页面是否登录系统，如果已登录，则不做其他处理；如果未登录，将进行登录操作"""
        try:
            expect_value = self.get_text((By.NAME, '扫一扫'))
            if expect_value == '扫一扫':
                print('当前处于登录状态，无需退出系统')
        except NoSuchElementException:
            print('当前处于未登录状态，正在登录系统')
            self.login_success_with_code('13321105094')
        except Exception as e:
            print(f'当前程序发生异常，异常信息如下: {e}\n')

    def login_success_with_code(self,phone):
        """登录成功"""
        self.input((By.NAME, '请输入手机号'), phone)
        self.click((By.NAME, ''))
        self.click((By.NAME, '登录/注册'))
        self.click((By.NAME, ''))
        try:
            self.explicitly_wait((By.NAME, 'NotificationShortLookView'),10)
            message = self.get_text((By.NAME, 'NotificationShortLookView'))
            # 使用正则表达式提取验证码
            match = re.search(r'您的验证码是(\d+)', message)

            if match:
                verification_code = match.group(1)
                print("验证码:", verification_code)
            else:
                print("未找到验证码！")

        except Exception as e:
            print("验证码元素未找到，异常信息为：", e)
        self.input((By.XPATH, '//XCUIElementTypeTextField'), verification_code)
        self.wait(1)
        print('登录成功')
    
    def login_fail_with_code(self, phone, code):
        """登录失败"""
        self.input((By.NAME, '请输入手机号'), phone)
        self.click((By.NAME, ''))
        self.click((By.NAME, '登录/注册'))
        self.click((By.NAME, ''))
        self.input((By.XPATH, '//XCUIElementTypeTextField'), code)

