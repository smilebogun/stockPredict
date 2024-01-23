
import streamlit as st
import pandas as pd

df = pd.DataFrame(data = {"col1":[100, 200, 300], 
                          "col2":['aa', 'bb', 'cc']})

st.write(df)
st.dataframe(df)
st.table(df)

# JSON 데이터 출력 ==> 딕셔너리 형태로 표현해야 함 {}
st.json({'name':'홍길동', 'age':22, 'gender':'male'})

# Metric() 함수를 이용한 데이터 출력(변화가 있는 데이터)
st.metric(label='온도', value='13℃', delta='3℃')
st.metric(label='카카오뱅크', value='55,000', delta='-1000')

# 이미지 데이터
st.image("OIP-1eSn_DkdvhsY2h1nFyntvAHaJE.jpeg", width=100)



