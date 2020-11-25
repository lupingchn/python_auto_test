#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhangluping
@file: request_util.py
@time: 2018/07/20
"""

import json
import requests
from string import Template

HEADER_POST = {}
COOKIES = {}
HOST_IP_PORT = None


def r_post(url, headers={}, datas=None, cookies={}):
    print '------------------------------------------------------------------------------------------------------------'
    print "url: " + url
    try:
        if headers is None or headers.__len__() == 0:
            headers = HEADER_POST
        if datas is None:
            print_request(headers)
            response = requests.request("POST", HOST_IP_PORT + url, headers=headers, cookies=cookies)
        else:
            if headers.get('content-type') == "application/json":
                data_str = json.dumps(datas, default=lambda o: o.__dict__, sort_keys=True, indent=4, ensure_ascii=False).replace('\n','').replace(' ', '')
                print_request(headers, data_str)
                response = requests.request("POST", HOST_IP_PORT + url, headers=headers, cookies=cookies, data=data_str)
            else:
                response = requests.request("POST", HOST_IP_PORT + url, headers=headers, cookies=cookies, data=datas)
        print_response(response)
        return response.text
    except Exception as err:
        print err


def r_get(url, headers={}, datas=None, cookies={}):
    print '------------------------------------------------------------------------------------------------------------'
    print "url: " + url
    try:
        if headers is None or headers.__len__() == 0:
            headers = HEADER_POST
        if datas is None:
            print_request(headers)
            response = requests.request("GET", HOST_IP_PORT + url, headers=headers, cookies=cookies)
        else:
            response = requests.request("GET", HOST_IP_PORT + url, headers=headers, cookies=cookies, params=datas)
        print_response(response)
        return response.text
    except Exception as err:
        print err

def print_request(headers=None, data=None):
    __request_template = Template(
        '''    request : {
        header: ${headers}
        data: ${data}
    },''')
    __request_string = __request_template.safe_substitute(headers=headers, data=data)
    print __request_string


def print_response(response):
    __response_template = Template(
        '''    response : {
        code: ${code} ,
        headers:${headers}
        text: ${text} 
    }''')
    __response_string = __response_template.safe_substitute(code=str(response.status_code), headers=response.headers, text=response.text)
    print __response_string


def get_cookies_dict(cookies):
    __cookie_dict = {}
    for h in cookies:
        __cookie_dict.pop(h, cookies[h])
    return __cookie_dict
