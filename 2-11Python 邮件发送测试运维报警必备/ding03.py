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
def WriteLogByDing():
    #请求头
    headers = {
        "Content-Type": "application/json",
        "Chartset": "utf-8"
    }
    #发送请求的数据
    request_data = {
        "actionCard": {
            "title": "阿里云挂了，那个丢了女朋友的运维小伙伴，你还好吗？",
            "text": "![screenshot](@lADOpwk3K80C0M0FoA) \n #### 云中炸雷惊春梦立春之后，“云中炸雷”昨天算是响了。周日一大早，阿里云故障导致用户APP和网站业务受影响的消息，如病毒一样蔓延开来，不出意外地刷屏朋友圈，就像亚马逊云、微软云、谷歌云、腾讯云曾经享受过的“待遇”一般，各种揣测、攻击、担忧、建议铺天盖地而来。",
                                                                                                          "hideAvatar": "0",
    "btnOrientation": "0",
    "singleTitle": "阅读全文",
    "singleURL": "https://baijiahao.baidu.com/s?id=1627034689681342290&wfr=spider&for=pc"
    },
    "msgtype": "actionCard"
    }
    #把发送的数据转化为json
    send_data = json.dumps(request_data)
    #发起请求
    response = requests.post(url=url,headers=headers,data=send_data)
    #获取返回的结果
    content = response.content.decode()
    print(content)

if __name__ == '__main__':  #入口函数  防止文件被导入时直接启动
    # content = input("请输入您的消息：")

    WriteLogByDing() #调用函数