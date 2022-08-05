# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2022/7/16 21:56
# @author   :Mo
# @function :post-demo of fastapi


from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn


app = FastAPI()


class Item(BaseModel):
    a: int = None
    b: int = None


@app.post('/add')
def calculate(request_data: Item):
    a = request_data.a
    b = request_data.b
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
python demo_post.py

2.访问
带界面: http://localhost:8832/docs
点击"GET"; 点击"Try it out"; 输入a,b元素; 点击Exectue

POST: http://localhost:8832/add
POST请求参数:
{"a":1, "b":2}


"""

