import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import math
import sklearn

df = pd.read_csv('C:/Users/Yash/PycharmProjects/yashML/input/Google.csv',sep=",",parse_dates=['Date'],index_col='Date')
df.head()
df.info()
df.index
df.loc[df['High']==101.740000]
df.corr()
df = df[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
print(df.head())
forecast_col = 'Adj. Close'
df.fillna(value=-99999, inplace=True)
forecast_out = int(math.ceil(0.00001 * len(df)))
df['label'] = df[forecast_col].shift(-forecast_out)
df.tail()