#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhangluping
@file: assert_util.py
@time: 2018/07/20
"""
import json
import traceback


def get_json_point_value(result, key):
    try:
        result_json = json.loads(result)
    except Exception, e:
        exception_msg = traceback.format_exc()
        print (exception_msg)
        raise Exception("返回结果非json数据！")
    # 找到key对应的节点值
    keys = key.split('/')
    for key_item in keys:
        if key_item in result_json.keys():
            result_json = result_json[key_item]
        else:
            raise Exception("未能在返回json中找到对应的节点{0}:{1}".format(key, key_item))
    return result_json


def check_json_result_eval(url, result, key, eval_str):
    # type: (str, str, str, str) -> bool
    """
    检查接口返回的json数据
    :rtype: 返回检查是否通过
    :param url: 请求路径
    :param result:  返回数据（未json格式化）
    :param key: 需要检查的数据项采用x/y/z进行分割
    :param eval_str: 逻辑表达式，比如 is not None
    """
    try:
        result_json = get_json_point_value(result, key)
    except Exception, e:
        exception_msg = traceback.format_exc()
        print_highlight("URL:{0}，验证结果发生异常！".format(url))
        print_highlight(exception_msg)
        return False
    if eval('result_json ' + eval_str):
        return True
    else:
        print_highlight("URL:{0}，验证{1}节点数据失败！".format(url, key), "期望值:{0}".format(result_json + eval_str),
                        "实际值:{0}".format(result_json))


def check_json_result_value(url, result, key, check_value=''):
    # type: (str, str, str, str) -> bool
    """
    检查接口返回的json数据
    :rtype: 返回检查是否通过
    :param url: 请求路径
    :param result:  返回数据（未json格式化）
    :param key: 需要检查的数据项采用x/y/z进行分割
    :param check_value:  对比的数值，如果为空，则认为不校验值
    """
    try:
        result_json = get_json_point_value(result, key)
    except Exception, e:
        exception_msg = traceback.format_exc()
        print_highlight("URL:{0}，验证结果发生异常！".format(url))
        print_highlight(exception_msg)
        return False
    if result_json == check_value:
        return True
    else:
        print_highlight("URL:{0}，验证{1}节点数据失败！".format(url, key), "期望值:{0}".format(get_str(check_value)),
                        "实际值:{0}".format(get_str(result_json)))


def print_highlight(*msgs):
    # 格式：\033[显示方式;前景色;背景色m
    for msg in msgs:
        print('\033[1;30;41m' + msg + '\033[0m')


def print_url_highlight(url, *msgs):
    # 格式：\033[显示方式;前景色;背景色m
    print('\033[1;30;41m' + 'URL: '),
    print url,
    print('\033[0m')
    print('\033[1;30;41m' + 'MSG: ')
    for msg in msgs:
        print('    ' + msg)
    print('\033[0m')


def get_str(data):
    if type(data) == unicode:
        return data.encode('utf-8')
    else:
        return data