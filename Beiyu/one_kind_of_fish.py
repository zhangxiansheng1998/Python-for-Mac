import numpy as np
import pandas as pd
import os

# 设置随机种子，以确保生成的随机数可重复
np.random.seed(42)

# 定义生成的数的总和的目标值
target_sum = 4550000*0.997

# 定义每个数必须为29.2的倍数（倍数为正整数）
multiple = 29.2

# 定义占比条件
prob_3000_to_8000 = 0.1
prob_8000_to_12000 = 0.75
prob_12000_to_20000 = 0.15

# 生成符合要求的随机数
random_numbers = []
random_multiples = []

while sum(random_numbers) < target_sum:
    num = int(np.random.randint(3000 / multiple, 20000 / multiple + 1) * multiple)
    if num <= 8000 and np.random.rand() < prob_3000_to_8000:
        random_numbers.append(num)
        random_multiples.append(int(num / 29.2))
    elif 8000 < num <= 12000 and np.random.rand() < prob_8000_to_12000:
        random_numbers.append(num)
        random_multiples.append(int(num / 29.2))
    elif 12000 < num <= 20000 and np.random.rand() < prob_12000_to_20000:
        random_numbers.append(num)
        random_multiples.append(int(num / 29.2))

# 将倍数和数值保存到Excel文档
df = pd.DataFrame({
    'n': random_numbers,
    'x': random_multiples
})

# 创建保存文件的目录
output_directory = 'output'
os.makedirs(output_directory, exist_ok=True)

# 构建输出文件路径
output_file_path = os.path.join(output_directory, '455W_all_balck.xlsx')

# 保存Excel文件
df.to_excel(output_file_path, index=False)

print(f"文件保存成功：{output_file_path}")