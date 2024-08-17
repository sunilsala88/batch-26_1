

import yfinance as yf
import pandas_ta as ta
import mplfinance as mpf

data=yf.download('TSLA',period='12mo')
print(data)

#supertrend
super=ta.supertrend(data['High'],data['Low'],data['Close'],length=10,multiplier=5)
print(super)
supertrend1=super['SUPERT_10_5.0']
print(supertrend1)

s1=mpf.make_addplot(supertrend1, color='red')
mpf.plot(data,type='candle',style='yahoo',addplot=s1)