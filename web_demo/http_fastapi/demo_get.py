# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2022/7/16 21:56
# @author   :Mo
# @function :get-demo of flask


from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get('/add/a={a}/b={b}')
def calculate(a: int = None, b: int = None):
    c = a + b
    res = {"result": c}
    data = {"code": 200, "data": res, "message": "success"}
    return data


if __name__ == '__main__':

    uvicorn.run(app=app,
                host="0.0.0.0",
                port=8832,
                workers=1)


"""

1.启动
python demo_get.py

2.访问
带界面: http://localhost:8832/docs
点击"GET"; 点击"Try it out"; 输入a,b元素; 点击Exectue

GET:  http://localhost:8832/add?a=1&b=2


"""

