import os
import time
from pathlib import Path
import yaml


def run():
    print("程序开始运行")
    with open('data/partial_jmx.yaml', 'r', encoding='utf8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    for key, value in data.items():
        Mytime = time.strftime("%Y-%m-%d_%H-%M-%S")
        os.system(
            "jmeter -n -t {}.jmx -l D:/apache-jmeter-5.1/jtl/{}.jtl -e -o D:/apache-jmeter-5.1/report/{}"
                .format(value, Mytime, Mytime))
        linkName = Path('D:/apache-jmeter-5.1/report/' + Mytime + '/index.html').as_uri()
        print("已生成测试报告，具体内容可点击超链接", linkName)

    print("程序已结束,即将关闭窗口")
    time.sleep(5)


with open('data/partial_jmx.yaml', 'r', encoding='utf8') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
for key, value in data.items():
    if key=="execute":
        new_dict=value
        for key,value in new_dict.items():
            print(value)

    #print(value)
#run()
