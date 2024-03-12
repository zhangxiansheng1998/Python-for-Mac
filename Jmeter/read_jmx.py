import os
import re

"""修改jmx脚本中的线程数，当然持续时间、循环次数等参数都可以修改"""


def modify_jmx_file(file_path, new_num_threads):
    # 读取JMX文件内容
    with open(file_path, 'r') as file:
        jmx_content = file.read()

    # 使用正则表达式匹配并替换数字
    pattern = r'<stringProp name="ThreadGroup.num_threads">(\d+)</stringProp>'
    replacement = f'<stringProp name="ThreadGroup.num_threads">{new_num_threads}</stringProp>'
    modified_content = re.sub(pattern, replacement, jmx_content, count=1)

    # 将修改后的内容写回文件
    with open(file_path, 'w') as file:
        file.write(modified_content)

    print(f"已成功将线程数量修改为：{new_num_threads}")


os.system("rm -rf /Volumes/Disk/apache-jmeter-5.1.1/jmeter/jtl/1.jtl")

os.system("rm -rf /Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/1")

# 使用函数
modify_jmx_file('/Volumes/Disk/apache-jmeter-5.1.1/jmeter/jmx/jsfk.jmx', 3)

# 运行修改后的jmx脚本
os.system(
    "jmeter -n -t /Volumes/Disk/apache-jmeter-5.1.1/jmeter/jmx/jsfk.jmx -l /Volumes/Disk/apache-jmeter-5.1.1/jmeter/jtl/1.jtl -e -o /Volumes/Disk/apache-jmeter-5.1.1/jmeter/report/1")
