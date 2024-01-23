import streamlit as st
import FinanceDataReader as fdr
import mplfinance as mpf
import matplotlib.pyplot as plt

# pip install mplfinance
from datetime import datetime, timedelta

# 시장 데이터를 읽어오는 함수들을 정의한다.
@st.cache_data
def getData(code, datestart, dateend):
    df = fdr.DataReader(code,datestart, dateend ).drop(columns='Change')  # 불필요한 'Change' 컬럼은 버린다.
    return df

# 캐시사용
@st.cache_data
def getSymbols(market='KOSPI', sort='Marcap'):
    df = fdr.StockListing(market)
    ascending = False if sort == 'Marcap' else True
    df.sort_values(by=[sort], ascending= ascending, inplace=True)
    return df[ ['Code', 'Name', 'Market'] ]



# def plotChart(data):
#     chart_style = 'default'
#     marketcolors = mpf.make_marketcolors(up='red', down='blue')
#     mpf_style = mpf.make_mpf_style(base_mpf_style= chart_style, marketcolors=marketcolors)

#     fig, ax = mpf.plot(
#         data,
#         volume=True,
#         type='candle',
#         style=mpf_style,
#         figsize=(10,7),
#         fontscale=1.1,
#         mav=(5,10,20),                      # 이동평균선 3개.
#         mavcolors=('red','green','blue'),   # 이동평균선 색상.
#         returnfig=True                  # Figure 객체 반환.
#     )
#     st.pyplot(fig)

# code='005930'
# date_start = (datetime.today()-timedelta(days=50)).date()
# df = getData(code, date_start, datetime.today().date()) 

# plotChart(df)
# st.write('##### 이동평균선: :red[5일] , :green[10일], :blue[20일].')

#################### 세션 상태를 초기화 한다.
if 'ndays' not in st.session_state:
    st.session_state['ndays'] = 30

if 'code_index' not in st.session_state:
    st.session_state['code_index'] = 0

if 'chart_style' not in st.session_state:
    st.session_state['chart_style'] = 'classic'

if 'volume' not in st.session_state:
    st.session_state['volume'] = True

################### 사이드바에서 폼을 통해서 차트 인자를 설정한다.
with st.sidebar.form(key="chartsetting", clear_on_submit=True):
    st.header('차트 설정')
    ''
    ''
    symbols = getSymbols()
    choices = zip( symbols.Code , symbols.Name , symbols.Market )

    choices = [ ' : '.join( x ) for x in choices ]  # Code, Name, Market을 한개의 문자열로.
        
    choice = st.selectbox( label='종목:', options = choices, index=st.session_state['code_index'] )    
    code_index = choices.index(choice) 
    code = choice.split()[0]      
    ''
    ''
    ndays = st.slider(
        label='기간 (days):', 
        min_value= 5,
        max_value= 365, 
        value=st.session_state['ndays'],
        step = 1)
    ''
    ''
    chart_styles = ['default', 'binance', 'blueskies', 'brasil', 'charles', 'checkers', 'classic', 'yahoo','mike', 'nightclouds', 'sas', 'starsandstripes']
    chart_style = st.selectbox(label='차트 스타일:',options=chart_styles,index = chart_styles.index(st.session_state['chart_style']))
    ''
    ''
    volume = st.checkbox('거래량', value=st.session_state['volume'])
    ''
    ''

    # ok 버튼 클릭시 재실행됨.
    if st.form_submit_button(label="OK"):
        st.session_state['ndays'] = ndays
        st.session_state['code_index'] = code_index
        st.session_state['chart_style'] = chart_style
        st.session_state['volume'] = volume
        st.experimental_rerun()

# 캔들 차트 출력 함수.
def plotChart(data):
    chart_style = st.session_state['chart_style']
    marketcolors = mpf.make_marketcolors(up='red', down='blue')
    mpf_style = mpf.make_mpf_style(base_mpf_style= chart_style, marketcolors=marketcolors)

    fig, ax = mpf.plot(
      data,
      volume=st.session_state['volume'],
      type='candle',
      style=mpf_style,
      figsize=(10,7),
      fontscale=1.1,
      mav=(5,10,20),                      # 이동평균선 3개.
      mavcolors=('red','green','blue'),   # 이동평균선 색상.
      returnfig=True                  # Figure 객체 반환.
    )
    st.pyplot(fig)

date_start = (datetime.today()-timedelta(days=st.session_state['ndays'])).date()
df = getData(code, date_start, datetime.today().date())     
chart_title = choices[st.session_state['code_index'] ]
st.markdown(f'<h3 style="text-align: center; color: red;">{chart_title}</h3>', unsafe_allow_html=True)
plotChart(df)
''
''
st.write('##### 이동평균선: :red[5일] , :green[10일], :blue[20일].')
