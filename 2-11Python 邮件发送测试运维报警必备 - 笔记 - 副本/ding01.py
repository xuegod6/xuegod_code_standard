# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 14:47
# @Author  : if
# @File    : ding01.py
# @Software: PyCharm
import requests
import json
#请求的地址
url = "https://oapi.dingtalk.com/robot/send?access_token=369fce11dec09a010bd6ef2c15a7d322f833d266380f8b1f69c7d111bfc42e06"
#触发函数
def WriteLogByDing(content):
    #请求头
    headers = {
        "Content-Type": "application/json",
        "Chartset": "utf-8"
    }
    #发送请求的数据
    request_data={
        "msgtype":"text",
        "text": {
            "content": content,
        },
        "at": {
            "atMobiles": [],
            "isAtAll": True
        }
    }
    #把发送的数据转化为json
    send_data = json.dumps(request_data)
    #发起请求
    response = requests.post(url=url,headers=headers,data=send_data)
    #获取返回的结果
    content = response.content.decode()
    print(content)

if __name__ == '__main__':  #入口函数  防止文件被导入时直接启动
    content = input("请输入您的消息：")

    WriteLogByDing(content) #调用函数