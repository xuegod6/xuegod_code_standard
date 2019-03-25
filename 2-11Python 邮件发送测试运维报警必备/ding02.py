# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 14:47
# @Author  : if
# @File    : ding01.py
# @Software: PyCharm
import requests
import json
url = "https://oapi.dingtalk.com/robot/send?access_token=369fce11dec09a010bd6ef2c15a7d322f833d266380f8b1f69c7d111bfc42e06"

headers = {
    "Content-Type": "application/json",
    "Chartset": "utf-8"
}
request_data={
    "msgtype":"text",
    "text": {
        "content": "我是你们的if老师，这是机器人测试！"
    },
    "at": {
        "atMobiles": [],
        "isAtAll": True
    }
}
send_data = json.dumps(request_data)

response = requests.post(url=url,headers=headers,data=send_data)

content = response.content.decode()
print(content)
