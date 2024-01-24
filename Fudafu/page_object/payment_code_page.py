from Fudafu.base.appium_base_page import *


class PaymentCodePage(BasePage):

    def set_amount_and_save_code(self, number):
        """设置固定金额的收款码，并保存"""
        self.click((By.NAME, '收款码'))
        self.click((By.NAME, '设置金额'))
        number_str = str(number)
        for digit in number_str:
            digit_xpath = (By.NAME, f'{digit}')
            self.click(digit_xpath)

        self.click((By.NAME, '确认'))
        self.click((By.NAME, '保存收款码'))
        print(f'金额:{number}元对应的收款码已保存至相册')
        self.click((By.NAME, '我已知晓'))
        return number

    def change_shop_and_save_code(self):
        """切换店铺收款码并保存"""
        self.click((By.NAME, ''))
        self.click((By.NAME, 'ABCD'))
        print(f'收款码已切换成店铺：ABCD')
        self.click((By.NAME, '保存收款码'))
        print(f'店铺:ABCD对应的收款码已保存至相册')


    def clear_amount(self):
        """清除金额"""
        self.click((By.NAME, '清除金额'))
        print('金额已清除')
