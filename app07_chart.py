# pip install matplotlib
# pip install seaborn

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


myData = np.random.randn(30, 3)
df = pd.DataFrame(data = myData, columns=['x', 'y', 'z'])

'위에서 5개 데이터 :', df.head()

st.line_chart(df)

st.area_chart(df)

st.bar_chart(df)
# '' 이것만쓰면 라인한칸 띄는 것
''
'---' # 줄긋기
''
df = pd.read_csv('data_iris.csv')
'붓꽃데이터', df.head()

cnts = df['Species'].value_counts()
fig = plt.figure(figsize=(7,5))
plt.bar(x=cnts.index, height=cnts.values, color='blue')
plt.ylabel('Counts')
plt.title('Iris Flower Species Counts')
st.pyplot(fig)
''
''
fig2 = plt.figure(figsize=(7,5))             ## legend='brief' --> 자동값?
## legend 옵션에는 auto / brief / full
sb.countplot(x='Species', hue='Species', data=df, legend='auto')
plt.legend(labels=df.Species, loc="lower right") ## "upper left"
st.pyplot(fig2)

