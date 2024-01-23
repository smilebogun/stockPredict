# 가상환경 생성하기
# conda create -n st python=3.9.13

# 가상환경 삭제하기
# conda env remove -n st

# 가상환경 활성/비활성화
# conda activate st <-- 활성
# conda deactivate <-- 비활성

# streamlit 1.19버전 설치하기
# pip install streamlit==1.19.0

# ModuleNotFoundError: No module named 'altair.vegalite.v4
# pip uninstall altair
# pip install altair==4.2.2

# 실행하기
# streamlit run 파일명(예>app01_text.py)

# 실행중지하기 : ctrl+c

import streamlit as st
import pandas as pd

# 마크다운 적용 : *...*
st.title("제목 : *안녕하세요*")
st.header("제목 : *하이*")
st.subheader("제목 : *안녕*")

# 마크다운 적용 안됌
st.text("일반 텍스트, *마크다운*")

st.markdown("*마크다운*을 컴파일해서 출력")
st.markdown("**마크다운**을 볼드채로 컴파일해서 출력")

st.write("텍스트/변수/객체")

a = 100
b = 200
df = pd.DataFrame(data = {"col1":[100, 200, 300], 
                          "col2":['aa', 'bb', 'cc']})
# 딕셔너리 타입이라 {} col에 각 데이터 넣어봄

st.write("a=", a, "and", "b=", b)
st.write("데이터프레임", df)

# 프로그램 코드 출력
myCode = '''
total = 0
for i in range(11):
    total += i
print(total)
'''
st.code(myCode)

# 캡션 출력
st.caption("짧은 설명")

# 매직 커맨드(홀따옴표, 쌍따옴표 사용)
"안녕하세요"
"**스트림릿** 하이!!"
a
b
'데이터 프레임', df

# 색상 지정
"텍스트 :blue[파란색]"
"텍스트 :red[빨간색]"
"텍스트 :green[초록색]"

# 이모티콘
":sunglasses:"
":thumbsup:"
":smile:"

# LaTex 수식을 컴파일해서 출력
st.latex(r'Area = \pi r^2')     # r은 row라고 뜻함



