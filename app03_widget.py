
import streamlit as st
import pandas as pd

# 버튼
st.button('클릭')
# st.button('클릭') # 똑같은 버튼 2개 생성 불가
st.button('클릭1')  # 이름이 다르면 가능

# 같은버튼 생성시 key로 구분
st.button('클릭', key=1)
st.button('클릭', key=2)
st.button('클릭', key=3, help=":red[tooltip]!")

# 함수 호출
def myFunc(*args):
    res = 0
    for x in args:
        res += x
    st.write(f'계산 결과 = {res}')

st.button('클릭', key=4, on_click=myFunc, args=[1,2,3])

aa = st.button('클릭', key=5)

## aa 버튼을 클릭했을때 true // 클릭 안했을때 false
if aa:
    st.write(":smile:") # true
else:
    st.write(":sleepy:") # false

''
'---'
''
x = st.checkbox('위 내용에 동의합니다!!')
if x:
    st.write("좋아요")

y = st.radio('메뉴 선택', ["짜장면", "짬뽕"])
st.write(f'선택메뉴 = {y}')

z = st.selectbox('선택하세요', ["짜장면", "짬뽕"])
st.write(f'선택메뉴 = {z}')

# 멀티 select
m = st.multiselect('후식 선택', ['커피', '아이스크림', '과일'])
st.write(f'후식 = {m}')

''
'---'
''
xx = st.select_slider('만족도?', ['매우안좋음', '안좋음', '보통', '좋음', '매우좋음'])
st.write(f'만족도 = {xx}')

yy = st.slider('만족도?', min_value=0, max_value=100, value=50, step=10)
st.write(f'만족도 = {yy}')

zz = st.number_input('점수?', min_value=0, max_value=100, value=50, step=10)
st.write(f'만족도 = {zz}')

''
'---'
''
n = st.text_input('당신의 이름은?')
st.write(f'이름 = {n}')

d = st.date_input('약속 날짜는?')
st.write(f'날짜 = {d}')


t = st.time_input('시간은?')
st.write(f'이름 = {n}', f'약속일 = {d}', f'시간 = {t}')