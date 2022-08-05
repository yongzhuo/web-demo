# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2022/7/16 21:56
# @author   :Mo
# @function :demo of streamlit


"""计算文本的jaccard相似度

启动运行
# shell
# streamlit run demo.py --server.port 8832
# nohup streamlit run demo.py --server.port 8832 > tc_jaccard.log 2>&1 &
# tail -n 1000  -f tc_jaccard.log
# 关闭也很慢

"""


import json

import streamlit as st


st.title("Calculate-Jaccard-Similarity")

st.subheader("Input 👇 ")
sen_1 = st.text_area("sentence-1:", value="你会什么", height=32)
sen_2 = st.text_area("sentence-2:", value="你叫什么", height=32)


def cal_jaccard(sen_1, sen_2):
    """ 计算相似度 """
    try:
        sent_intersection = list(set(list(sen_1)).intersection(set(list(sen_2))))
        sent_union = list(set(list(sen_1)).union(set(list(sen_2))))
        score_jaccard = round(float(len(sent_intersection) / len(sent_union)), 6)
    except:
        score_jaccard = 0.0
    res = {"result": score_jaccard}
    data = {"code": 200, "data": res, "message": "success"}
    return data


score = cal_jaccard(sen_1, sen_2)

st.subheader("Result 👇 ")
st.text(json.dumps(score, ensure_ascii=False, indent=4))

