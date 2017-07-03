# -*- coding: utf-8 -*-
import json

from requests import post

API_URL = "http://www.tuling123.com/openapi/api"
APIkey = "3ebf34b4ca9a4c3f95aa70dcec365852"


def robot_reply(user_id, content):
    """
    发送文本消息

    """
    data = {
        'key': APIkey,
        'userid': user_id,
        'info': content
    }
    response = post(API_URL, data=data)
    if response.status_code == 200:
        res_dict = response.json()
        status = res_dict.get('code')
        test = res_dict.get('text')
        if status == 100000:
            return test
        else:
            return '暂时无法提供服务'

    return '暂时无法提供服务'

if __name__ == '__main__':
    res = robot_reply('12311', '你好')

    print res
