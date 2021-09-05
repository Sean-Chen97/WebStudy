# -*- coding = utf-8 -*-
# @Time : 2021/8/27
# @Author : 陈树
# @FileName : WSGI Web.py
# @FilePath : venv
# @Software : PyCharm
# Importing libraries

# Release port： in cmd  --- taskkill /PID 7292 /F

from wsgiref.simple_server import make_server

def run_server(environ, start_response):

    start_response("200 OK",[('Content-Type','text/html;charset=utf-8')] )

    return [bytes('<h2>好看！ </h2>', encoding="utf-8")]

s = make_server('localhost',8000,run_server)
s.serve_forever()