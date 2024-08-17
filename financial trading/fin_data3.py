import yfinance as yf

data=yf.download('TSLA',period='7d',interval='1m')
print(data)

ag_dict={'Open':'first','High':'max','Low':'min','Close':'last','Volume':'sum'}

# day_min=60*24


# rdata=data.resample(f'{day_min}T').agg(ag_dict)

# rdata=rdata.dropna()
# print(rdata)


day_min=15

rdata=data.resample(f'{day_min}T').agg(ag_dict)

rdata=rdata.dropna()
print(rdata.head(80))