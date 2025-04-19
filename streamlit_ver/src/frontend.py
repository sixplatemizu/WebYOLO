import streamlit as st
import requests
from PIL import Image
import io

st.title("WebYOLO11")

uploaded_file = st.file_uploader("上传图片", type=["jpg", "jpeg", "png", "webp"])

if uploaded_file is not None:
    # 显示原始图片
    image = Image.open(uploaded_file)
    st.image(image, caption="原始图片", use_container_width=True)
    
    if st.button("开始检测"):
        # 发送到后端API
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://localhost:8000/detect/", files=files)
        
        if response.status_code == 200:
            # 显示结果图片和下载按钮
            result_image = Image.open(io.BytesIO(response.content))
            st.image(result_image, caption="检测结果", use_container_width=True)

            # 将结果转为字节流供下载
            img_byte_arr = io.BytesIO()
            result_image.save(img_byte_arr, format='JPEG')
            st.download_button(
                label="下载结果图片",
                data=img_byte_arr.getvalue(),
                file_name="detection_result.jpg",
                mime="image/jpeg"
            )
        else:
            st.error("检测失败，请重试")

