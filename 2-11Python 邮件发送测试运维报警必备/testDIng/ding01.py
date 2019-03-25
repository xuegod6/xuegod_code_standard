# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 17:15
# @Author  : if
# @File    : ding01.py
# @Software: PyCharm
import requests
import json

url= "https://oapi.dingtalk.com/robot/send?access_token=e1b9f69f6d839a2aeb2bc2e777a589cba6b597ef7fd2bb2d8a91f1eb301e14b4"

headers = {
    "Content-Type": "application/json",
    "Chartset": "utf-8"
}

request_data = {
    "msgtype":"text",
    "text":{
        "content":"服务器消息设置"
    },
    "at":{
        # 被@人的手机号
        "atMobiles": [],
        # 控制@所有人
        "isAtAll": True
    }
}

send_data = json.dumps(request_data)

response = requests.post(url=url,headers=headers,data=send_data)

content = response.content.decode()

print(content)
