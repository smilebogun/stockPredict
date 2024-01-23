
import streamlit as st

# 사이드 바
# st.sidebar.title("스트림 연습")
# st.sidebar.header("스트림 연습")
# st.sidebar.subheader("스트림 연습")
# st.sidebar.write('''
#         ---
#         ''')
# z = st.selectbox('선택하세요', ["짜장면", "짬뽕"])
# st.write(f'선택메뉴 = {z}')

with st.sidebar:
    # 사이드 바
    st.title("스트림 연습")
    st.header("스트림 연습")
    st.subheader("스트림 연습")
    st.write('''
             ---
             ''')
    z = st.selectbox('선택하세요', ["짜장면", "짬뽕"])
    st.write(f'선택메뉴 = {z}')

col1, col2, col3 = st.columns(3) # 비율 1:1:1
with col1:
    st.header(':blue[제목 1]')
    st.image('https://static.streamlit.io/examples/cat.jpg')
with col2:
    st.header(':blue[제목 2]')
    st.image('https://static.streamlit.io/examples/dog.jpg')
with col3:
    st.header(':blue[제목 3]')
    st.image('https://static.streamlit.io/examples/owl.jpg')
''
'---'
''
col1, col2, col3 = st.columns([1,3,1])  #비율을 1:3:1 로 정할 수 있음
with col1:
    st.header(':blue[제목 1]')
    st.image('https://static.streamlit.io/examples/cat.jpg')
with col2:
    st.header(':blue[제목 2]')
    st.image('https://static.streamlit.io/examples/dog.jpg')
with col3:
    st.header(':blue[제목 3]')
    st.image('https://static.streamlit.io/examples/owl.jpg')
''
'---'
''
tab1, tab2, tab3 = st.tabs(['cat', 'dog', 'owl'])
with tab1:
    st.header(':blue[야옹]')
    st.image('https://static.streamlit.io/examples/cat.jpg')
with tab2:
    st.header(':blue[멍멍]')
    st.image('https://static.streamlit.io/examples/dog.jpg')
with tab3:
    st.header(':blue[부엉]')
    st.image('https://static.streamlit.io/examples/owl.jpg')
''
'---'
''
# 탭과 칼럼을 같이 사용
tab1, tab2 = st.tabs(['왼쪽', '오른쪽'])
with tab1:
    col1, col2, col3 = st.columns(3) # 비율 1:1:1
    with col1:
        st.header(':blue[제목 1]')
        st.image('https://static.streamlit.io/examples/cat.jpg')
    with col2:
        st.header(':blue[제목 2]')
        st.image('https://static.streamlit.io/examples/dog.jpg')
    with col3:
        st.header(':blue[제목 3]')
        st.image('https://static.streamlit.io/examples/owl.jpg')
with tab2:
    col1, col2, col3 = st.columns([1,1,3]) # 비율 1:1:3
    with col1:
        st.header(':blue[제목 1]')
        st.image('https://static.streamlit.io/examples/cat.jpg')
    with col2:
        st.header(':blue[제목 2]')
        st.image('https://static.streamlit.io/examples/dog.jpg')
    with col3:
        st.header(':blue[제목 3]')
        st.image('https://static.streamlit.io/examples/owl.jpg')
''
'---'
''
a = st.expander('Expander')
a.write("멍멍 사진")
a.image('https://static.streamlit.io/examples/dog.jpg', width=100)
''
'---'
''
# empty : 특정 장소에 하나의 요소를 출력할 공간을 만들어줌
b = st.empty()
b.write('**start**버튼을 누르세요!!')

c1, c2, c3, x = st.columns([1,1,1,5])
start = c1.button('start', key=1)
clear = c2.button('clear', key=2)
reset = c3.button('reset', key=3)

import time
if start:
    with b:
        for i in range(6):
            t = 5 - i
            st.write(f'카운트다운 {t}초')
            time.sleep(1)
if clear:
    b.empty() # b 공간을 비움
''
'---'
''
# container와 empty 차이
# container : 내려가면서 다른위치에 카운트됌
# empty : 같은 위치에서 카운트됌
c = st.container()
c.write('**start**버튼을 누르세요!!')

cc1, cc2, cc3, _ = st.columns([1,1,1,5])
start = cc1.button('start', key=4)
clear = cc2.button('clear', key=5)
reset = cc3.button('reset', key=6)

import time
if start:
    with c:
        for i in range(6):
            t = 5 - i
            st.write(f'카운트다운 {t}초')
            time.sleep(1)
if clear:
    c.empty() # b 공간을 비움

# for i in range(10):
#     st.snow()
#     time.sleep(1)


