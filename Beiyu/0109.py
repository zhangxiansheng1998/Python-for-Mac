import openpyxl

# 打开Excel文件
workbook = openpyxl.load_workbook('/Users/macbook_air/Desktop/12.28～13～24_副本.xlsx')

# 选择工作表
sheet = workbook.active

# 获取A1单元格的值
A1_value = sheet['A1'].value

# 已知A1的值，解出B1和C1的值
# A1 = 15.7 * B1 + 71.8 * C1
# 可以通过一些数学计算求解B1和C1
# 这里假设 A1_value 是一个已知的数值

# 假设 A1_value = 100
# 100 = 15.7 * B1 + 71.8 * C1
# 你可以自行修改A1_value的值

# 解方程得到 B1 和 C1
B1 = (A1_value - 71.8 * (sheet['C1'].value or 0)) / 15.7
C1 = (A1_value - 15.7 * (sheet['B1'].value or 0)) / 71.8

# 输出结果
print(f'B1 的值为：{B1}')
print(f'C1 的值为：{C1}')

# 关闭Excel文件
workbook.close()

