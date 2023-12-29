import unittest
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from Browser import *
from base_page import *
from selenium.webdriver.common.by import By
import random

def validate_input(input_var):
    try:
        order_count = int(input_var.get())
        print(f"订单数量: {order_count}")
        messagebox.showinfo("提示", f"正在生成{order_count}笔订单，请稍等!")

        # 启动浏览器
        driver = webdriver.Chrome(options=Browser().browser_ui()) # 带UI界面启动
        # driver = webdriver.Chrome(options=Browser().browser_headless())  # 无头模式启动
        obj = BasePage(driver)
        obj.max()
        obj.visit("http://h.thinkermen.com/wincc_xingeercc/mini2021_1.6.9/index.php?r=login")
        obj.input((By.ID, 'loginname'), "admin")
        obj.input((By.ID, 'nloginpwd'), "123456")
        obj.click((By.CSS_SELECTOR,
                              "body > div.lbl_login_bg > div.new_login_r > div.login_form.clb > div:nth-child(1) > "
                              "div > div:nth-child(3) > button"))
        print("\n登录成功！")

    except ValueError:
        messagebox.showerror("错误", "输入错误，请重新输入！")

class TestOrderGeneration(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.title("ERP订单生成器")
        self.root.geometry("470x50")

    def tearDown(self):
        if hasattr(self, 'root') and self.root.winfo_exists():
            self.root.destroy()


    def create_input_box(self):
        input_var = tk.StringVar()
        input_label = tk.Label(self.root, text="请输入您要生成的订单数量:", font=("Helvetica", 14))
        input_label.grid(row=3, column=0, padx=10, pady=10)

        input_entry = tk.Entry(self.root, textvariable=input_var, width=12)
        input_entry.grid(row=3, column=1, padx=10, pady=10)

        submit_button = tk.Button(self.root, text="提交", command=lambda: validate_input(input_var),
                                  font=("Helvetica", 14))
        submit_button.grid(row=3, column=2, padx=10, pady=10)

    def create_close_button(self):
        close_button = tk.Button(self.root, text="关闭", command=self.root.destroy, font=("Helvetica", 14))
        close_button.grid(row=3, column=10, columnspan=30, pady=10, padx=10)

    def close_window(self):
        self.root.destroy()
        self.stopTest = True  # 停止 unittest 测试

    def test_order_generation(self):
        self.create_input_box()
        self.create_close_button()
        self.root.mainloop()


if __name__ == '__main__':
    unittest.main()
