import json
import random
import time
import requests
from urllib.parse import quote
import os
from datetime import datetime

# 函数_文本取出中间文本------------------------------------------------------------------------------------------
def get_middletext(content, start_content, end_content):
    start_index = content.index(start_content) + len(start_content)
    end_index = content.index(end_content)
    middle_text = content[start_index: end_index]
    return middle_text

# 函数获取union------------------------------------------------------------------------------------------
def get_xiaoyueyuedu_union(CK):
    url = "http://1709266805.zhangyameng.top/?cate=0"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2b) NetType/WIFI Language/zh_CN",
        "cookie": CK}
    rm = requests.get(url=url, headers=headers).text
    rm1=get_middletext(rm, 'var unionid="', ' var domain')
    return get_middletext(rm1, '', '";')

# 函数获取uk------------------------------------------------------------------------------------------
def get_xiaoyueyuedu_uk(CK,union):
    url = "http://1709621144.zhangyameng.top/yunonline/v1/wtmpdomain"
    headers = {
        "Host": "1709265404.zhangyameng.top",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Connection": "keep-alive",
        "Accept-Language": "zh-cn",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin":"http://1709265404.zhangyameng.top",
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2a) NetType/WIFI Language/zh_CN",
        "Connection": "keep-alive",
        "Content-Length": "36",
        "Cookie":CK}
    rm = requests.post(url=url, headers=headers,data="unionid="+union).text
    return get_middletext(rm, "uk=", '&t=')

# 函数获取主页------------------------------------------------------------------------------------------
def get_xiaoyueyuedu_zhuye(CK,union):
    url = f"http://1709621144.zhangyameng.top/yunonline/v1/gold?unionid={union}&time={int(datetime.now().timestamp()*1000)}"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2b) NetType/WIFI Language/zh_CN",
        "cookie": CK}
    rm=json.loads(requests.get(url=url, headers=headers).text)
    rm1=rm["data"]
    return "【总"+ str(rm1["last_gold"]) + "币】【今日已读" + str(rm1["day_read"]) + "篇】【今日获取" + str(rm1["day_gold"]) + "币】【今日剩余" + str(rm1["remain_read"]) + "篇】"


# 函数提现------------------------------------------------------------------------------------------
def get_xiaoyueyuedu_tixian(CK,union):
    url = f"http://1709621144.zhangyameng.top/yunonline/v1/gold?unionid={union}&time={int(datetime.now().timestamp()*1000)}"
    headers = {
            "User-Agent": "Mozilla/5.0 (iPad; CPU OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2b) NetType/WIFI Language/zh_CN",
            "cookie": CK}
    rm=json.loads(requests.get(url=url, headers=headers).text)
    rm5=rm["data"]["last_gold"]
    rm7= int(rm5)
    #如果大于9000金币就转换成余额
    if rm7>=9000:
        url = "http://1709266805.zhangyameng.top/?cate=0"
        headers = {
                "User-Agent": "Mozilla/5.0 (iPad; CPU OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2b) NetType/WIFI Language/zh_CN",
                "cookie": CK}
        rm2 = requests.get(url=url, headers=headers).text
        #unionid
        rm3=get_middletext(rm2, 'exchange?', 'qrcode')
        union_id=get_middletext(rm2, 'exchange?', '&request_id')
        signid=get_middletext(rm2, '&request_id=', '&qrcode')
        #转换成余额
        url = "http://1709635000.zhangyameng.top/yunonline/v1/user_gold"
        headers = {
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f28) NetType/WIFI Language/zh_CN",
                "Host": "1709635000.zhangyameng.top",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Connection":" keep-alive",
                "Accept-Encoding":"gzip, deflate",
                "Accept-Language":"zh-cn",
                "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Origin":"http://1709635000.zhangyameng.top",
                "Connection": "keep-alive",
                "Content-Length": "96",
                "cookie": CK}
        requests.post(url=url, headers=headers,data=rm3+"gold="+str(int(int(rm5)/1000)) +"000").text
        #提现
        url = "http://1709644855.zhangyameng.top/yunonline/v1/withdraw"
        headers = {
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f28) NetType/WIFI Language/zh_CN",
                "Host": "1709644855.zhangyameng.top",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Connection":" keep-alive",
                "Accept-Encoding":"gzip, deflate",
                "Accept-Language":"zh-cn",
                "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Origin":"http://1709635000.zhangyameng.top",
                "Connection": "keep-alive",
                "Content-Length": "96",
                "cookie": CK}
        tx=requests.post(url=url, headers=headers,data=union_id+"&signid="+signid+"&ua=1&ptype=0&paccount=&pname=").text
        return tx
    else:
        return "【余额不足,暂不提现："+str(rm["data"]["last_gold"])+"】"


# 主程序------------------------------------------------------------------------------------------
print("共获取到"+str(len(os.getenv("xiaoyueCK").split("\n"))) +"个账号")

for CK in os.getenv("xiaoyueCK").split("\n"):
    try:
        union = get_xiaoyueyuedu_union(CK)
    except ValueError:
        print("未获取到iu，请检查CK是否正确！")
    else:
        print("查询信息成功"+get_xiaoyueyuedu_zhuye(CK,union))
        headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f28) NetType/WIFI Language/zh_CN",
            "cookie": CK}
        time.sleep(1)
        for x in range(1, 50):
            # 生成时间戳
            shijianchuo = int(datetime.now().timestamp()*1000)
            # 获取uk
            uk=get_xiaoyueyuedu_uk(CK,union)
            #阅读
            fanhuizhi = requests.get(
                    url=f"https://nsr.zsf2023e458.cloud/yunonline/v1/do_read?uk={uk}&time={shijianchuo}&psgn=&v=3.0 ",
                    headers=headers).text
            if  json.loads(fanhuizhi)["errcode"] == 407:
                print(fanhuizhi)
                print(get_xiaoyueyuedu_tixian(CK,union))
                break
            else:
                data2=json.loads(fanhuizhi)["data"]
                if fanhuizhi.find("chksm") != -1:
                        requests.get(
                            url=f"https://wxpusher.zjiecode.com/api/send/message/?appToken=你的推送平台的&content=%E9%B1%BC%E5%84%BF%E9%98%85%E8%AF%BB%28%E8%AF%B7%E5%9C%A820%E7%A7%92%E5%86%85%E7%82%B9%E5%87%BB%E6%A3%80%E6%B5%8B%E9%93%BE%E6%8E%A5%29&uid=你的推送平台的&url={quote(data2['link'])}")
                        print("检测文章：" + data2['link'])
                        print("验证文章检测中……")
                        time.sleep(25)
                        print("检测结束")
                        data = requests.get(
                            url=f"https://nsr.zsf2023e458.cloud/yunonline/v1/get_read_gold?uk={uk}&time=32&timestamp={shijianchuo}",
                            headers=headers).text
                else:
                    print("推送文章：" + data2['link'])
                    time.sleep(random.randint(9, 11))
                    data =json.loads( requests.get(
                            url=f"https://nsr.zsf2023e458.cloud/yunonline/v1/get_read_gold?uk={uk}&time=32&timestamp={shijianchuo}",
                            headers=headers).text)
                    xinxi=(data["data"])
                    print("【每篇"+str(xinxi["gold"]) +"币】"+"【今日已读"+str(xinxi["day_read"])+"篇】"+"【今日获取"+str(xinxi["day_gold"])+"币】"+"【今日剩余"+str(xinxi["remain_read"])+"篇】"+"【总"+str(xinxi["last_gold"])+"币】")
