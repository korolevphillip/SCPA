import yfinance as yf 

# input: stock: str, dayChange: float
# example: calculateVolatility("AAPL")

# exception: average day change is 0, cannot divide by 0 in volatility equation

def calculateVolatility(stock, dayChange):
    # fetch inital data on stock
    stock_data = yf.Ticker(stock)

    # fetch stock price 6 months ago
    six_price = stock_data.history(period = "6mo")["Open"].iloc[0]

    # fetch stock price a couple days before surge (a couple days before previous trading day)
    presurge_price = stock_data.history(period = "6mo")["Close"].iloc[-5]

    # calculate the 6 month change %, and average daily change
    # average daily change is calculated by %6mo/122 --> roughly 126 trading days in 6 mo,
    # and we take our 6 month period as 6 mo ago until 4 days prior to surge
    change = ((presurge_price - six_price)/six_price)*100
    avg_change_daily = change/122

    # implement volatility equation, if avg_change_daily is 0, we simply set it to an extremely small value
    if avg_change_daily != 0:
        volatility = (dayChange - avg_change_daily)*(dayChange/avg_change_daily)
    if avg_change_daily == 0:
        volatility = (dayChange)*(dayChange/0.1)

    # returns a volatility score
    return abs(volatility)/100

print(calculateVolatility("FRBN", 59.33))

