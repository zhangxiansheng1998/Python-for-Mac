import os
import re
import time
import hmac
import hashlib
import base64
import urllib.parse
import jenkins
import json
import urllib3
from urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
import os

timestamp = str(round(time.time() * 1000))
secret = 'SEC26269f4538ec31adf200209b4222406ffe11bf212a55834361df95794ebf4716' #替换成自己的值
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
# print(timestamp)
# print(sign)
#钉钉通知的接口地址
url = f'https://oapi.dingtalk.com/robot/send?access_token=4577151a48816d922f0b7973caaeef7828fd456c2a1e78cce1a85af1122aeb99&timestamp={timestamp}&sign={sign}' #钉钉群的token


#利用python发送钉钉  在钉钉需要点击 查看测试报告的话 就需要把报告发送到服务器 再把地址参数传下面  就去掉jenkins所有操作
# jenkins登录地址
jenkins_url = "http://127.0.0.1:8080/"#Jenkins地址
# 获取jenkins对象
server = jenkins.Jenkins(jenkins_url, username='admin', password='3c778ef3c32842d9b386502915031ab5') #Jenkins登录名 ，密码
# job名称
job_name = "job/Zhujia_Factory/" #Jenkins运行任务名称
# job的url地址
job_url = jenkins_url + job_name
# 获取最后一次构建
job_last_build_url = server.get_info(job_name)['lastBuild']['url']
# 报告地址
report_url = job_last_build_url

'''
钉钉推送方法：
读取order.txt文件内的数据，循环遍历获取需要的值
使用钉钉机器人的接口，拼接后推送消息
'''

def DingTalkSend():
    #服务器地址路径/var/lib/jenkins/workspace/ERP/order.txt
    #本地地址路径order.txt
    with open('summary.txt', 'r', encoding='utf-8') as file:
        # 读取文件内容
        content = file.read()

    # 钉钉推送
    con = {"msgtype": "text",
           "text": {
               "content": "筑家工厂-UI测试"
                          "\n测试概述:" + "\n"
                          "" + content +
                          "\n构建地址：\n" + job_url +
                          "\n报告地址：\n" + report_url + "\n"
           },
           "at": {
               "atMobiles": [
                   "15180381485"  # 如果需要@某人，这里写他的手机号
               ],
               "isAtAll": 1  # 如果需要@所有人，这些写1
           }

           }
    try:
        urllib3.disable_warnings()
        http = urllib3.PoolManager()
        jd = json.dumps(con)
        jd = bytes(jd, 'utf-8')
        http.request('POST', url, body=jd, headers={'Content-Type': 'application/json'})

    except Exception as e:
        print(e)


if __name__ == '__main__':
    DingTalkSend()