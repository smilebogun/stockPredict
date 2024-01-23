# 주식가격 시계열 예측 - 자기회귀 (AR).

# 필요한 라이브러리를 불러온다.    
import FinanceDataReader as fdr
import mplfinance as mpf
import pandas as pd
import matplotlib.pyplot as plt
import warnings
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression              # 선형회귀 모형.
# pip install scikit-learn
warnings.filterwarnings("ignore")                              # 성가신 warning을 꺼준다.
   
# 시장 데이터를 읽어오는 함수들을 정의한다.
def getData(code, datestart, dateend):
  df = fdr.DataReader(code, datestart, dateend ).drop(columns='Change')  
  return df

def getSymbols(market='KOSPI', sort='Marcap'):
  df = fdr.StockListing(market)
  ascending = False if sort == 'Marcap' else True
  df.sort_values(by=[sort], ascending = ascending, inplace=True)
  return df[['Code', 'Name', 'Market']]

# code에 해당하는 주식 데이터를 받아온다.
code = '005930'              # 삼성전자.
#code = '373220'             # LG 에너지솔루션.
date_start = (datetime.today()-timedelta(days=100)).date()          # 시분초 떼어내고 년월일 날짜만.
df = getData(code, date_start, datetime.today().date())     

# 캔들차트를 출력해 본다 (이동평균 없이).
#chart_style = 'default'                                             # 'default', 'binance', 'classic', 'yahoo', 등 중에서 선택.
chart_style = 'classic'
marketcolors = mpf.make_marketcolors(up='red', down='blue')         # 양봉/음봉 선택.
mpf_style = mpf.make_mpf_style(base_mpf_style=chart_style, marketcolors=marketcolors)

fig, ax = mpf.plot(
    data=df,                            # 받아온 데이터.      
    volume=True,                       # True 또는 False.                   
    type='candle',                      # 캔들 차트.
    style=mpf_style,                    # 위에서 정의.
    figsize=(10,7),
    fontscale=1.1,
    returnfig=True                      # Figure 객체 반환.
)

# 여기에서 예측선을 추가한다. 
n = len(df)                 # 시계열의 길이.
pred_ndays = 10             # 미래 예측 기간.
print(df['Close'])
print(df['Close'].shape) # 행이몇개인지 찍어볼때 --> 69행
print('------------------')
print(df[['Close']].shape) # 행이 2차원형태로 바뀜 [['...']]
print('------------------')
df = df[['Close']].reset_index(drop=True)  
# 인덱스 초기화하겠다 1번 칼럼, -> 날짜대신 인덱스 0번부터 시작 됌

df['m1'] = df['Close'].shift(1) # 이동한다, t-1스탭, 현재값을 m1의 한단계 밑으로 이동
df['m2'] = df['Close'].shift(2) # t-2스탭
df['m3'] = df['Close'].shift(3) # t-3스탭
df['m4'] = df['Close'].shift(4) # t-4스탭
df['m5'] = df['Close'].shift(5) # t-5스탭
# 하고나서 5번배열부터 데이터 확인 ==> 과거 5일전 데이터 확인을 해볼 수 있다.
# 즉, 과거 m1 ~ m5의 데이터를 확인해서 Close 데이터를 예측

print(df.head(10)) # 즉 칼럼1의 이전값은 칼럼2(m1)
df = df.iloc[5:] # 5배열부터 짤라서 df에 다시 넣음(결측치 NaN 없는부분부터 사용하기 위해 슬라이싱 처리)
print(df) # 5번배열부터 출력 됌


# 선형회귀 기반 AR(5)모형 학습.
model = LinearRegression() # 학습
model.fit(df[['m1','m2','m3','m4','m5']], df['Close']) # , df['Close'] 정답을 알려줌?

# 선형회귀 기반 AR(5)모형 예측.
rdf = df['Close'][-5:] # 뒤 5개를 짤라와서 최근데이터(recent_df)라고 함

for step in range(pred_ndays):        # 미래 예측. 과거데이터를 만들어서 concat으로 합쳐줌
    past = pd.DataFrame(data={ f'm{i}': [rdf.iloc[-i]] for i in range(1,6)} ) 
    predicted = model.predict(past)[0]  
    print("----", pd.Series({n + step:predicted}))
    rdf = pd.concat( [rdf, pd.Series({n + step:predicted}) ])

print(rdf)

# ax에 추가
ax[0].plot(rdf, color='green', marker='o', linestyle='--', linewidth=1.5, label='AR(5)')
ax[0].legend(loc='best')

plt.show()