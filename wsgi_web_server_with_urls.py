# -*- coding = utf-8 -*-
# @Time : 2021/8/27
# @Author : 陈树
# @FileName : WSGI Web.py
# @FilePath : venv
# @Software : PyCharm
# Importing libraries

# Release port： in cmd  --- taskkill /PID 7292 /F

from wsgiref.simple_server import make_server

# 1.Urls dispatch
# 2.Suppose we have a dictionary for different urls - if found, return function, if not found, 404


def book(environ, start_response):
    print("book page ")
    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')] )
    return [bytes('<h3>Book好看！ </h3>', encoding="utf-8"),]


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


def run_server(environ, start_response):
    print('hhhhh', environ)

    url_list = url_dispacher() #拿到所有url
    request_url = environ.get('PATH_INFO')
    print('request url', request_url)

    if request_url in url_list:
        func_data = url_list[request_url](environ, start_response)
        return func_data
    else:
        start_response("404 ", [('Content-Type', 'text/html;charset=utf-8')])
        return [bytes('<h1 style = "font-size:50px">404, Page not found </h1>', encoding="utf-8"), ]


s = make_server('localhost', 8000, run_server)
s.serve_forever()
