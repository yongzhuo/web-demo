# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2022/7/16 21:56
# @author   :Mo
# @function :demo of pywebio


from pywebio.input import input, TEXT, FLOAT, input_update, input_control, textarea
from pywebio.output import put_text, put_tabs, put_table, put_file, put_code
from pywebio import start_server


def cal_jaccard():
    sen_1 = input("请输入第一个句子：", type=TEXT)
    sen_2 = input("请输入第二个句子：", type=TEXT)
    try:
        sent_intersection = list(set(list(sen_1)).intersection(set(list(sen_2))))
        sent_union = list(set(list(sen_1)).union(set(list(sen_2))))
        score_jaccard = round(float(len(sent_intersection) / len(sent_union)), 6)
    except:
        score_jaccard = 0.0
    res = {"result": score_jaccard}
    data = {"code": 200, "data": res, "message": "success"}
    # put_text(data)
    put_text(data)


if __name__ == '__main__':
    start_server(cal_jaccard, port=8832)


"""

1.启动
python demo.py

2.访问
地址:  http://localhost:8832
请输入第一个句子：你是谁呀
请输入第二个句子：你叫什么

关闭似乎很慢
"""

