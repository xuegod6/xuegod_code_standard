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
     "msgtype": "markdown",
     "markdown": {"title":"杭州天气",
"text":"#### 杭州天气  \n > 9度，@1825718XXXX 西北风1级，空气良89，相对温度73%\n\n > ![screenshot](http://i01.lw.aliimg.com/media/lALPBbCc1ZhJGIvNAkzNBLA_1200_588.png)\n  > ###### 10点20分发布 [天气](http://www.thinkpage.cn/) "
     },
    "at": {
        "atMobiles": [],
        "isAtAll": True
    }
 }
send_data = json.dumps(request_data)
reponse = requests.post(url=url,headers=headers,data=send_data)
content = reponse.content.decode()

print(content)
