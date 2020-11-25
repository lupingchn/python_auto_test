# -*- coding:utf-8 _*-
"""
@author:zhangluping
@file: project_request.py
@time: 2018/07/19
"""
import json
import sys
import time
reload(sys)  
sys.setdefaultencoding('utf8')
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn

IP = '127.0.0.1'
HTTP_PORT = 8880

class TestHTTPHandle(BaseHTTPRequestHandler):

    def do_PUT(self):
        self.headers['content-length']
        content_len = int(self.headers['content-length'])
        post_body = self.rfile.read(content_len)
        print("content_len:", content_len)

        self.send_response(200)
        self.send_header("Content-type", "application/json;charset=utf-8")
        self.end_headers()

    def do_POST(self):
        path = self.path
        print("-------------Got HTTP POST Data--------------")
        self.headers['content-length']
        content_len = int(self.headers['content-length'])
        post_body = self.rfile.read(content_len)
        print("postbody:", post_body)
        # 根据HTTP请求，取出self中想要的字段信息，此处代码省略。比如取出api信息和json信息
        #
        self.send_response(200)
        self.send_header("Content-type", "application/json;charset=utf-8")
        self.end_headers()

        respond_json = {0}
        willSend = False

        # 根据请求的api信息，指定response data
        if (path == "/aa"):
            willSend = True
            respond_json = {'code': 200,
                            'message': {'a_first': 'address_a_post', 'a_decond': 321, 'a_third': 'phone_a_post'},
                            'aa_param': 'POST'}
        elif (path == "/bb"):
            willSend = True
            respond_json = {'code': 200,
                            'message': {'b_first': 'address_b_post', 'b_decond': 321, 'b_third': 'phone_b_post'},
                            'bb_param': 'POST'}
        else:
            willSend = True
            respond_json = {'error': 'url有误'}
            print("NO Match api.")

        if (willSend):
            d2 = json.dumps(respond_json)
            self.wfile.write(d2.encode("utf-8"))
            print("HTTP response is sent.")
        #self.wfile.close()


    def do_GET(self):
        path = self.path
        query = path.split('?')
        api = query[0]
        print("-------------Got HTTP GET Data--------------")

        self.send_response(200)
        self.send_header("Content-type", "application/json;charset=utf-8")
        self.end_headers()
        respond_json = {0}
        willSend = False
        # willSend = True

        # 根据请求的api信息，指定response data
        if (api == "/aa"):
            willSend = True
            respond_json = {'code': 200,
                        'message': {'a_first': 'addressid_a', 'a_decond': 321, 'a_third': 'phone_a'}, 'aa_param': 'GET'}
        elif (api == "/bb"):
            willSend = True
            respond_json = {'code': 200,
                        'message': {'b_first': 'addressid_b', 'b_decond': 321, 'b_third': 'phone_b'}, 'bb_param': 'GET'}
        else:
            willSend = True
            respond_json = {'message': 'url有误'}
            print("NO Match api.")

        if (willSend):
            d2 = json.dumps(respond_json)
            self.wfile.write(d2.encode('UTF-8'))
            print("HTTP response is sent.")



class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    server = ThreadedHTTPServer((IP,HTTP_PORT), TestHTTPHandle)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()