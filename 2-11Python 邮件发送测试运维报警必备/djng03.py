# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 15:06
# @Author  : if
# @File    : djng03.py
# @Software: PyCharm
import requests
import json

url = "https://oapi.dingtalk.com/robot/send?access_token=369fce11dec09a010bd6ef2c15a7d322f833d266380f8b1f69c7d111bfc42e06"
headers = {
    "Content-Type": "application/json",
    "Chartset": "utf-8"
}

request_data = {
    "msgtype": "link",
    "link": {
        "text":"2019年考研国家线正式公布 2019年考研复试录取工作展开",
       "title": "考研究生",
        "picUrl": "https://img04.sogoucdn.com/v2/thumb/resize/w/120/h/90/zi/on/iw/90.0/ih/67.5?t=2&url=http%3A%2F%2Fpic.baike.soso.com%2Fugc%2Fbaikepic2%2F6150%2Fcut-20181029112521-659563047_jpg_437_349_35847.jpg%2F300&appid=200524&referer=http://baike.sogou.com/v93804.htm?fromTitle=%E5%9B%BE%E7%89%87",
        "messageUrl": "http://www.southmoney.com/shuju/hysj/201903/3056404.html"
    }
}
send_data = json.dumps(request_data)
reponse = requests.post(url=url,headers=headers,data=send_data)
content = reponse.content.decode()

print(content)
