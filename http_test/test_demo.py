#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhangluping
@file: user.py
@time: 2018/07/23
"""
from http_test.project_util.project_request import *
from util.assert_util import check_json_result_value

def appointmentBorrow():
	url = "/bt/appoint-borrow"
	data = {
		"appointmentAmount":1000,
		"appointmentDays":"7"
	}
	result = r_post_base_rep(url, datas=data)

def user_check_exist():
    url = "/user/check/exist"
    result = r_post_base_rep(url, datas="admin")
    check_json_result_value(url, result, 'id', '1')


def user_upload_file():
    url = "/user/upload-files"
    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"files\"; filename=\"C:\\Users\\zhangluping\\Desktop\\20180711-M2迭代一待完成功能.txt\"\r\nContent-Type: text/plain\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ip\"\r\n\r\n1.1.1.1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    result = r_post_base_rep(url, datas=payload)


if __name__ == "__main__":
    user_upload_file()
