


import yfinance as yf
import pandas_ta as ta
import mplfinance as mpf 


data=yf.download('TSLA',period='5d',interval='1m')
print(data)
sma1=ta.sma(data['Close'])

print(sma1)

ema1=ta.ema(data['Close'])
print(ema1)

#bollinger band

b=ta.bbands(data['Close'])
print(b)


# mpf.plot(data,type='candle',style='yahoo')



# b=mpf.make_addplot(sma1,color='red')
# c=mpf.make_addplot(ema1,color='blue')
# mpf.plot(data,addplot=[b,c],type='candle',style='yahoo')

# bu=mpf.make_addplot(b['BBU_5_2.0'],color='red')
# bm=mpf.make_addplot(b['BBM_5_2.0'],color='blue')
# bl=mpf.make_addplot(b['BBL_5_2.0'],color='green')
# mpf.plot(data,addplot=[bu,bm,bl],type='candle',style='yahoo')


#macd
print(ta.macd(data['Close'],fast=15,slow=30))

#rsi
print(ta.rsi(data['Close']))