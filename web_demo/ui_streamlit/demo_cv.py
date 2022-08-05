# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2022/7/16 21:56
# @author   :Mo
# @function :cv-demo of streamlit


"""展示图片

启动运行
# shell
# windows:   streamlit run demo_cv.py --server.port 8832
# linux:     nohup streamlit run demo_cv.py --server.port 8832 > tc_jaccard.log 2>&1 &
# linux:     tail -n 1000  -f tc_jaccard.log
# 关闭也很慢

"""


import streamlit as st
import numpy as np
import cv2


st.title("Show-Images")
IMAGE_TYPE = "jpg/jpeg/png/web"
file_container = st.expander("Check your uploaded image of {}".format(IMAGE_TYPE))
uploaded_file = st.file_uploader(
        "",
        key="1",
        help="To activate 'wide mode', go to the hamburger menu > Settings > turn on 'wide mode'",
        type=["jpg", "jpeg", "png", "web"],
    )

if uploaded_file is not None:
    file_container = st.expander("Check your uploaded image of {}".format(IMAGE_TYPE))
    # 将传入的文件转为Opencv格式
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    # 展示图片
    st.subheader("Result 👇 ")
    st.image(opencv_image, channels="BGR")



