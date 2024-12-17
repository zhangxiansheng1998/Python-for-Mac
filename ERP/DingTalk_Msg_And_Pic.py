import requests
import json
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

# 钉钉机器人的webhook地址
#webhook_url = 'https://oapi.dingtalk.com/robot/send?access_token=YOUR_ACCESS_TOKEN'
timestamp = str(round(time.time() * 1000))
secret = 'SEC26269f4538ec31adf200209b4222406ffe11bf212a55834361df95794ebf4716' #替换成自己的值
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

webhook_url = f'https://oapi.dingtalk.com/robot/send?access_token=4577151a48816d922f0b7973caaeef7828fd456c2a1e78cce1a85af1122aeb99&timestamp={timestamp}&sign={sign}'

# 读取图片文件并编码为base64
with open('./picture/2024-12/2024-12-02/test.jpg', 'rb') as f:
    image_content = base64.b64encode(f.read()).decode('utf-8')

# 构造请求头部
headers = {
    'Content-Type': 'application/json'
}

# 构造请求体
data = {
    "msgtype": "image",
    "image": {
        "base64": image_content
    }
}

# 发送请求
response = requests.post(webhook_url, headers=headers, data=json.dumps(data))

# 打印响应内容
print(response.text)
