



import yfinance as yf
import pandas_ta as ta
import mplfinance as mpf
import numpy as np

data=yf.download('TSLA',period='12mo')
print(data)

#inside
# d=ta.cdl_inside(data['Open'],data['High'],data['Low'],data['Close'])

# print(d)
# d.replace(0, np.nan, inplace=True)
# d=d.abs()*data['High']
# print(d)


# s1=mpf.make_addplot(d, color='red',type='scatter')
# mpf.plot(data,type='candle',style='yahoo',addplot=s1)

#doji
# d1=ta.cdl_doji(data['Open'],data['High'],data['Low'],data['Close'])
# print(d1)

# d1.replace(0, np.nan, inplace=True)
# d1=d1*data['High']
# print(d1)

# s1=mpf.make_addplot(d1, color='red',type='scatter')
# mpf.plot(data,type='candle',style='yahoo',addplot=s1)





def shooting_star(ohlc_df):    
    """returns dataframe with shooting star candle column"""
    df = ohlc_df.copy()
    df["sstar"] = (((df["High"] - df["Low"])>3*(df["Open"] - df["Close"])) & \
                   ((df["High"] - df["Close"])/(.001 + df["High"] - df["Low"]) > 0.6) & \
                   ((df["High"] - df["Open"])/(.001 + df["High"] - df["Low"]) > 0.6)) & \
                   (abs(df["Close"] - df["Open"]) > 0.1* (df["High"] - df["Low"]))
    return df


d3=shooting_star(data)['sstar']
print(d3)

d3.replace(False, np.nan, inplace=True)
d3.replace(True, 1, inplace=True)
d3=d3*data['High']
print(d3)

s1=mpf.make_addplot(d3, color='red',type='scatter')
mpf.plot(data,type='candle',style='yahoo',addplot=s1)