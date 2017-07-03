# -*- coding: utf-8 -*-

import logging
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from wechatpy.events import SubscribeEvent, UnsubscribeEvent, MassSendJobFinishEvent
from wechatpy.messages import TextMessage, VoiceMessage, ImageMessage, VideoMessage, LinkMessage, \
    LocationMessage
from wechatpy.events import BaseEvent
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.parser import parse_message
from wechatpy.replies import create_reply
from wechatpy.utils import check_signature

from myapp.actions import fun, register_user, wx_menu, get_menu, send_msg, send_mass_msg
from myapp.api import get_article
from myapp.forms import TextForm
from myapp.robotapi import robot_reply

logger = logging.getLogger('myapp')


WECHAT_TOKEN = 'sayhello'
AppID = 'wxad25526b9589c4c9'
AppSecret = '27b5ffa5802f8664ff0c38eefe6983c5'


@csrf_exempt
def index(request):
    if request.method == 'GET':
        # 检验合法性
        # 从 request 中提取基本信息 (signature, timestamp, nonce, xml)
        signature = request.GET.get('signature', '')
        timestamp = request.GET.get('timestamp', '')
        nonce = request.GET.get('nonce', '')
        echo_str = request.GET.get('echostr', '')
        logger.info('echo_str: %s' % echo_str)
        try:
            check_signature(WECHAT_TOKEN, signature, timestamp, nonce)
        except InvalidSignatureException:
            echo_str = 'error'
        response = HttpResponse(echo_str, content_type="text/plain")
        return response

    # POST
    message = parse_message(request.body)

    logger.info(type(message))

    if isinstance(message, TextMessage):
        content = message.content.strip()  # 当前会话内容

        reply_text = robot_reply(message.source, content)
        logger.info('target: %s, source: %s, id: %s' % (message.target, message.source, message.id))
        reply = create_reply(reply_text, message=message)
        logger.info(reply)
        return HttpResponse(reply, content_type="application/xml")

    elif isinstance(message, VoiceMessage):

        reply_text = '语音信息我听不懂/:P-(/:P-(/:P-('
    elif isinstance(message, ImageMessage):
        reply_text = '图片信息我也看不懂/:P-(/:P-(/:P-('
    elif isinstance(message, VideoMessage):
        reply_text = '视频我不会看/:P-('
    elif isinstance(message, LinkMessage):
        reply_text = '链接信息'
    elif isinstance(message, LocationMessage):
        label = message.label
        logger.info(label)
        reply_text = label
    elif isinstance(message, BaseEvent):  # 事件信息
        logger.info(message.type)
        if isinstance(message, SubscribeEvent):  # 关注事件(包括普通关注事件和扫描二维码造成的关注事件)
            reply_text = '事件信息'
            logger.info('关注')
            logger.info(message.target)
            register_user(message.source)
        if isinstance(message, UnsubscribeEvent):  # 取消关注
            logger.info('取消关注')
            reply_text = ''

        if isinstance(message, MassSendJobFinishEvent):
            logger.info('群发消息事件')
            reply_text = ''

    reply = create_reply(reply_text, message=message)
    return HttpResponse(reply, content_type="application/xml")


@csrf_exempt
def add_view(request):
    if request.method == 'POST':
        logger.info(request.body)
        form = TextForm(request.POST)
        logger.info(form)
        msg = form.data.get('a')
        logger.info(msg)
        send_mass_msg(msg)
        logger.info('send message!!')
    else:
        form = TextForm()
    return render(request, 'index.html', {'form': form})


def boot_view(request):

    return render(request, 'boots.html')


def rss_view(request):
    url = 'https://www.huxiu.com/rss/0.xml'
    art = get_article(url)

    return render(request, 'index.html', {'art': art})

