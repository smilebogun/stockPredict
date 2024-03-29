import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


_, col, _ = st.columns([1,3,1])
col.header('시각화 연습')

df_iris = sb.load_dataset('iris')
colors = {"setosa":"red", "versicolor":"green", "virginica":"blue"}

with st.sidebar:
    selectX = st.selectbox("X 선택 :", ["sepal_length", "sepal_width", "petal_length", "petal_width"])
    ''
    selectY = st.selectbox("Y 선택 :", ["sepal_length", "sepal_width", "petal_length", "petal_width"])
    ''
    selectSpecies = st.multiselect("품종선택 (:red[다중])", ["setosa", "versicolor", "virginica"])
    ''
    sel_alpha = st.slider('투명도 설정:', 0.0, 1.0, 0.5)

# 산전도로 입력값 출력하기

if selectSpecies:
    fig = plt.figure(figsize=(7,5))
    for sp in selectSpecies:
        df = df_iris[df_iris.species==sp]
        plt.scatter(df[selectX], df[selectY], alpha=sel_alpha, label=sp)
    plt.legend(loc="lower right")
    plt.xlabel(selectX)
    plt.ylabel(selectY)
    plt.title("Iris Scatter Plot")
    st.pyplot(fig)
else:
    st.warning("붓꽃 품종을 선택하세요!!")


