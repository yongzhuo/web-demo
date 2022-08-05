# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2022/7/22 10:21 
# @author   :Mo
# @function :demo of tornado


import tornado.ioloop
import tornado.web
import json


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        a = self.get_argument('a')
        b = self.get_argument('b')
        c = int(a) + int(b)
        res = {"result": c}
        data = {"code": 200, "data": res, "message": "success"}
        self.write(data)

    def post(self):
        body = self.request.body
        body_decode = body.decode()
        body_json = json.loads(body_decode)
        a = body_json.get("a")
        b = body_json.get("b")
        c = int(a) + int(b)
        res = {"result": c}
        data = {"code": 200, "data": res, "message": "success"}
        self.write(data)


application = tornado.web.Application([(r"/add", MainHandler), ])


if __name__ == "__main__":
    application.listen(8832)
    tornado.ioloop.IOLoop.instance().start()



"""

1.启动
python demo.py

2.访问
GET:  http://localhost:8832/add?a=1&b=2

POST: http://localhost:8832/add
POST请求参数:
{"a":1, "b":2}


"""
