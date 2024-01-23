
import streamlit as st
import time

# 진행바 50%
st.progress(value=50)

# 눈송이 특수효과
st.snow()
st.balloons()
''
'---'
''
st.error('에러 메세지')
st.success('성공 메세지')
st.warning('경고 메세지')
st.info('공지 메세지')
''
'---'
''
with st.spinner(text='실행중...'):
    time.sleep(3.0)
    st.success('Done!')


