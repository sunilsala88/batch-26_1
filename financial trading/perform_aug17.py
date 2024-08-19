
import yfinance as yf
import pandas_ta as ta
import mplfinance as mpf

data=yf.download('RELIANCE.NS',period='12mo')
print(data)

cagr1=ta.cagr(data['Close'])
print(cagr1)



def CAGR(DF):
    "function to calculate the Cumulative Annual Growth Rate of a trading strategy"
    df = DF.copy()
    df["return"] = DF["Close"].pct_change()
    df["cum_return"] = (1 + df["return"]).cumprod()
    n = len(df)/252
    CAGR = (df["cum_return"][-1])**(1/n) - 1
    return CAGR


cagr2=CAGR(data)
print(cagr2)