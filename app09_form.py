import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import time

def getData(name, age, gender):
    data = {'이름':name, '나이':age, '성별':gender}
    time.sleep(2)
    return data

e = st.empty()
                # clear_on_submit=True이면 submit 후에 폼데이터를 지움(초기화)
with st.form(key = 'myForm', clear_on_submit=True):
    name = st.text_input('이름은 ?')
    age = st.slider('나이는?', 1, 100, 20)
    gender = st.radio('성별은?', ['남', '여'])
    submitted = st.form_submit_button('확인')
    if submitted:
        e.write(getData(name, age, gender))
