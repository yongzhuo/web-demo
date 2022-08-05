# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2022/7/16 21:56
# @author   :Mo
# @function :demo of flask


from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        params = request.args
    else:
        params = request.form if request.form else request.json
    a = params.get("a", 0)
    b = params.get("b", 0)
    c = int(a) + int(b)
    res = {"result": c}
    return jsonify(code=200,
                   data=res,
                   message="success"
                   )


if __name__ == "__main__":
    app.run(host="0.0.0.0",
            threaded=True,
            debug=False,
            port=8832)

"""

1.启动
python demo.py

2.访问
GET:  http://localhost:8832/add?a=1&b=2

POST: http://localhost:8832/add
POST请求参数:
{"a":1, "b":2}

"""

