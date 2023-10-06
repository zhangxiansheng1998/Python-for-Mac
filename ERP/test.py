import tkinter as tk
from tkinter import messagebox
import webbrowser

def submit_order():
    try:
        order_quantity = int(entry.get())
        messagebox.showinfo("成功", f"订单数量：{order_quantity}笔，正在生成中！")
        webbrowser.open("http://www.baidu.com")  # 在浏览器中打开百度网页
    except ValueError:
        messagebox.showerror("错误", "输入有误，请重新输入！")

def close_window():
    root.destroy()  # 关闭窗口

# 创建主窗口
root = tk.Tk()
root.title("ERP订单生成器")
root.geometry("470x60")  # 设置窗口大小

# 添加标签和输入框
label = tk.Label(root, text="请输入您要生成的订单数量:", font=("Helvetica", 14))
label.pack(side=tk.LEFT, padx=10, pady=10)

entry = tk.Entry(root, font=("Helvetica", 14), width=12)  # 设置输入框的宽度
entry.pack(side=tk.LEFT, padx=10, pady=10)

# 添加确定按钮
submit_button = tk.Button(root, text="确定", command=submit_order, font=("Helvetica", 14), width=6)  # 缩短按钮文本
submit_button.pack(side=tk.LEFT, padx=10, pady=10)

# 添加关闭按钮
close_button = tk.Button(root, text="关闭", command=close_window, font=("Helvetica", 14), width=6)  # 缩短按钮文本
close_button.pack(side=tk.RIGHT, padx=10, pady=10)

# 运行主循环
root.mainloop()
