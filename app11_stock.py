import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import time
import FinanceDataReader as fdr
import plotly as pl

# pip install finance-datareader # 주가데이터
# pip install bs4 --> beautifulsoup4
# pip install plotly # 차트 만드는 라이브러리

df = fdr.StockListing('KOSPI')
# print(df.head())
print(df)       # 콘솔에 출력
st.dataframe(df)    # 웹에 출력

# 삼성전자
code = '005930'
df = fdr.DataReader(code)
# fdr.DataReader(코드번호, 시작날짜, 종료날짜보다 하루 +1) -- 날짜 안적으면 10년치
df = fdr.DataReader(code, "2024")
print(df)
st.dataframe(df)    # 웹에 출력
st.dataframe(df.sort_values(by=['Date'], ascending=False)) # .sort_values 정렬

# 환율정보                                 # 오늘은 1/19인데 1/20로 입력해야함
df = fdr.DataReader("USD/KRW", "2024-01-01", "2024-01-20")
print(df)
st.dataframe(df)    # 웹에 출력

# 비트코인
df = fdr.DataReader("BTC/KRW", "2024-01-01", "2024-01-20")
st.dataframe(df)    # 웹에 출력

# import matplotlib.pyplot as plt
# df['Close'].plot()
# plt.show()
fig = plt.figure(figsize=(7, 5))
plt.plot(df.Close)
plt.xticks(rotation=90) # 겹치는거 방지
st.pyplot(fig)

# Date, 인덱스
list_x = []
for idx in df.index:
    list_x.append(idx)
list_y = []
for Close in df.Close:
    list_y.append(Close)

# import seaborn as sb
fig2 = plt.figure(figsize=(7, 5))
sb.lineplot(x='Date', y='Close', markers='o', data=df, color='red')
plt.xticks(list_x, rotation=90) # 겹치는거 방지
st.pyplot(fig2)

###### lineplot의 모든 종가 출력
fig3 = plt.figure(figsize=(11, 5))

for i in range(len(list_x)):
    cValue = df.Close[i]
    plt.text(df.index[i], cValue, '%.1f' %cValue, ha="center", va='bottom', size=7)

sb.lineplot(x='Date', y='Close', markers='o', data=df, color='red')
plt.xticks(list_x, rotation=90) # 겹치는거 방지
st.pyplot(fig3)

###### lineplot의 최대값 종가 출력
fig4 = plt.figure(figsize=(11, 5))

# {종가:날짜, 종가:날짜,....}
dic = {y:x for x, y in zip(df.index, df.Close)}

print("키", max(dic))         # 종가 최대값
print("값", dic[max(dic)])    # 

sb.lineplot(x='Date', y='Close', markers='o', data=df, color='red')
plt.text(dic[max(dic)], max(dic), '%.1f' %max(dic), ha="center", va='bottom', size=7)
plt.xticks(list_x, rotation=90) # 겹치는거 방지
st.pyplot(fig4)



