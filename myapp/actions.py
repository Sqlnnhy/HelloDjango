# -*- coding:utf-8 -*-
import logging

from wechatpy.client import WeChatClient
import sys
reload(sys)
sys.setdefaultencoding('utf8')


logger = logging.getLogger('myapp')
AppID = 'wxad25526b9589c4c9'
AppSecret = '27b5ffa5802f8664ff0c38eefe6983c5'

client = WeChatClient(appid=AppID, secret=AppSecret)


def fun(user_id):
    logger.info('action')
    user = client.user.get(user_id)
    logger.info(user)
    menu = client.menu.get()
    logger.info(menu)
    client.message.send_text('user_id', 'content')


def register_user(user_id):
    user = client.user.get(user_id)
    logger.info(user['city'])
"""
{u'province': u'\u6e56\u5357',
 u'city': u'\u957f\u6c99',
 u'subscribe_time': 1488615214,
 u'headimgurl': u'http://wx.qlogo.cn/mmopen/KAtVzB12T0wia4diby568c7Ac6NwJEYk7ibciaSicwGVWr4FpDgPagpf9ia5bmxGdwVMHaDVQsQUSyEzF2NIw6Hmia8VPPksUIcMOuR/0',
 u'language': u'zh_CN',
 u'openid': u'oVzJKs4YxP7qwuEy45tZ9sl3l_kI',
 u'country': u'\u4e2d\u56fd',
 u'tagid_list': [],
 u'remark': u'', u'sex': 1,
 u'subscribe': 1,
 u'unionid': u'opm8mw4YHXF-wGi0iLQq7_lvvzdU',
 u'nickname': u'\u66f8',
 u'groupid': 0}
"""


def get_menu():
    logger.info('client.access_token: %s' % client.access_token)
    logger.info(client.menu.get())
    return client.menu.get()


def wx_menu():
    logger.info(client.menu.get())
    client.menu.delete()
    logger.info(client.menu.get())
    client.menu.create({
        "button": [
            {
                "type": "view",
                "name": "主菜单",
                "url": "http://wxabc.tmqyt.com/admin/",
                "sub_button": [{
                        "type": "view",
                        "name": "子菜单1",
                        "url": "http://www.baidu.com",
                    },
                    {
                        "type": "view",
                        "name": "子菜单2",
                        "url": "http://www.baidu.com",
                    }]
            }
        ]
    })
    logger.info(client.menu.get())


# 客服消息
def send_msg(msg):
    client.message.send_text('oVzJKs4YxP7qwuEy45tZ9sl3l_kI', msg)


# 群发消息
def send_mass_msg(msg):
    client.message.send_mass_text(0, msg, True)

