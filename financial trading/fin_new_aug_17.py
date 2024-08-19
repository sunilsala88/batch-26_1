

import yfinance as yf
import pandas_ta as ta
import mplfinance as mpf

data=yf.download('TSLA',period='12mo')
print(data)

# #supertrend
# super=ta.supertrend(data['High'],data['Low'],data['Close'],length=10,multiplier=5)
# print(super)
# supertrend1=super['SUPERT_10_5.0']
# print(supertrend1)

# s1=mpf.make_addplot(supertrend1, color='red')
# mpf.plot(data,type='candle',style='yahoo',addplot=s1)

#macd
m=ta.macd(close=data['Close'])
print(m)

s1=mpf.make_addplot(m['MACD_12_26_9'], color='red',panel=1)
s2=mpf.make_addplot(m['MACDs_12_26_9'], color='blue',panel=1)
s3=mpf.make_addplot(m['MACDh_12_26_9'], color='green', panel=1,type='bar')
mpf.plot(data, type='candle', style='yahoo', addplot=[s1,s2,s3])