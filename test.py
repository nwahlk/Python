import requests
import json


webhook = 'https://oapi.dingtalk.com/robot/send?access_token=xxx'
#xxx替换成自己机器人的token

headers = {
    "Content-Type" : "application/json",
    "Charset" : "UTF-8"
}
message = {
    "msgtype": "text", 
    "text": {
        "content": "通知: 我就是我, 是不一样的烟火"  #机器人发送内容 创建机器人时自定义关键词是什么前面就必须以什么开头
    }, 
    "at": {
        "atMobiles": [
            "187xxxxxxxx"  #发送内容时艾特187xxx的手机号
        ], 
        "isAtAll": False   #是否艾特全体这里选择否
    }
}

r = requests.post(url=webhook,headers=headers,data=json.dumps(message))
print(r.text)
