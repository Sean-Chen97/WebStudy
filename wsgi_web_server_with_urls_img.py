# -*- coding = utf-8 -*-
# @Time : 2021/8/27
# @Author : 陈树
# @FileName : WSGI Web.py
# @FilePath : venv
# @Software : PyCharm
# Importing libraries

# Release port： in cmd  --- taskkill /PID 7292 /F

from wsgiref.simple_server import make_server
import re
import os

# 1.Urls dispatch
# 2.Suppose we have a dictionary for different urls - if found, return function, if not found, 404

BASE_DIR = os.path.abspath(__file__)

def book(environ, start_response):
    print("book page ")
    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')] )

    data = """
        <h1>Welcome to Japan area</h1>
            <img src='/static/testimg.gif' />
        <p>看片</p>
    '''
    """

    return [bytes(data, encoding="utf-8"),]


def cloth(environ, start_response):
    print("cloth page ")
    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
    return [bytes('<h3>Cloth好看！ </h3>', encoding="utf-8"), ]


def url_dispacher():
    urls = {
        '/book': book,
        '/cloth': cloth,
    }
    return urls


def img_handler(request_url):
    img_path = re.sub('/static', '/static_data', request_url)

    print("Base",BASE_DIR)

    if os.path.isfile(img_path):
        f = open(img_path, "rb")
        data = f.read()
        return [data, 0]
    return [None, 1]


def run_server(environ, start_response):
    print('hhhhh', environ)

    url_list = url_dispacher() # 拿到所有url
    request_url = environ.get('PATH_INFO')
    print('request url', request_url)

    if request_url in url_list:
        func_data = url_list[request_url](environ, start_response)
        return func_data
    elif request_url.startswith("/static/"):
        #represent it's an image
        img_data, img_status = img_handler(request_url)
        if img_status == 0:
            start_response("200 OK ", [('Content-Type', 'text/html;charset=utf-8')])
            return img_data
    else:
        start_response("404 ", [('Content-Type', 'text/gif;charset=utf-8')])
        return [bytes('<h1 style = "font-size:50px">404, Page not found </h1>', encoding="utf-8"), ]


s = make_server('localhost', 8000, run_server)
s.serve_forever()
