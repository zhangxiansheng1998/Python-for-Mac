from tkinter import Tk
from tkinter.filedialog import askopenfilename

# 创建根窗口
root = Tk()
root.withdraw()

# 打开文件对话框并选择文件
file_path = askopenfilename()

# 上传文件的代码，这里仅输出文件路径

print("选择的文件路径：", file_path)