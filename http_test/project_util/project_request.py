#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhangluping
@file: project_request.py
@time: 2018/07/19
"""
import util.request_util as request_util

HOST_IP_PORT = "http://localhost:8099"

HEADER_POST_COMMON = {
    'content-type': "application/json",
    'cache-control': "no-cache",
}

HEADER_POST_MULTIPART = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'cache-control': "no-cache",
}


class BaseRequest:
    def __init__(self, datas=None):
        self.commons = None
        self.datas = datas
        pass


class BasePage:
    def __init__(self):
        self.pageNum = 1
        self.pageSize = 10


def r_post(url, headers={}, datas=None, cookies={}):
    request_util.HEADER_POST = HEADER_POST_COMMON
    request_util.HOST_IP_PORT = HOST_IP_PORT
    return request_util.r_post(url, headers, datas, cookies)

def r_post_file(url, headers={}, datas=None, cookies={}):
    request_util.HEADER_POST = HEADER_POST_MULTIPART
    request_util.HOST_IP_PORT = HOST_IP_PORT
    return request_util.r_post(url, headers, datas, cookies)

def r_post_base_rep(url, headers={}, datas=None, cookies={}):
    request_util.HEADER_POST = HEADER_POST_COMMON
    request_util.HOST_IP_PORT = HOST_IP_PORT
    base_rep = BaseRequest()
    base_rep.datas = datas
    return request_util.r_post(url, headers, base_rep, cookies)
