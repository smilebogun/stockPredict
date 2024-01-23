import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import time

# if A in B: B안에 A가 있으면 true
# if A not in B: B안에 A가 없으면 true
# B는 iterable 객체 == 리스트, 튜플, 문자열, 딕셔너리

# session_state : 본래 JAVA에서는 키와밸류형태였는데, Python에서는 딕셔너리 형태임
# session 초기화
if 'cnt' not in st.session_state:
    st.session_state['cnt'] = 0

x = st.empty()

col1, col2, _ = st.columns([1,1,5])

if col1.button('+1'):
    st.session_state['cnt'] += 1

if col2.button('clear'):
    st.session_state['cnt'] = 0

x.write(f'Counter = {st.session_state["cnt"]}')

''
'---'
''
def getData(name, age, gender):
    data = {'이름':name, '나이':age, '성별':gender} 
    # {}딕셔너리형태 : 맵처럼 키와 밸류
    time.sleep(2)
    return data

e = st.empty()  # 버튼을 누를시 데이터가 날라가기때문에 세션에 저장해서 사용해야 함

# session_state.keys() : 세션의 키값들
def hasClicked():       # 함수기능 : 세션의 키값을 리턴해줌
    if 'clicked' in st.session_state.keys():
        return True # clicked 란 값이 세션에 있으면
    else:
        return False

if hasClicked():        # 함수가 실행되면, 폼의 입력받아서 출력
    with st.form(key = 'myForm', clear_on_submit=True):
        name = st.text_input('이름은 ?')
        age = st.slider('나이는?', 1, 100, 20)
        gender = st.radio('성별은?', ['남', '여'])
        submitted = st.form_submit_button('확인')
        if submitted:
            e.write(getData(name, age, gender))
else:
    if st.button('Show Form'):  # 함수가 실행안되면 버튼이 보이고 버튼을 누르면,
        st.session_state['clicked'] = True  # Show Form버튼 클릭되면 함수호출
        st.experimental_rerun()     # 다시화면을띄워서 본다

