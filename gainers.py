import pandas as pd
import requests
import io 

class Gainer:
    # class constructor
    def __init__(self):
        self = self
    
    # creates and returns data frame of top 10 gainers info
    def createDataFrame(self):
        # url used to fetch top daily gainers data
        url_tg = "https://stockanalysis.com/markets/gainers/"

        # fetching data as a browser
        header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
        }

        r_tg = requests.get(url_tg, headers = header)

        # wrapping literal text as a StringIO
        wrapped_tg = io.StringIO(r_tg.text)

        # creating data frame including top 10 daily gainers stocks
        data_frame_tg = pd.read_html(wrapped_tg)[0].head(10)

        return data_frame_tg
    
    # returns list of tickers of top 10 gainer stocks, in order
    def getTickers(self):
        tickers = self.createDataFrame()['Symbol'].tolist()
        return tickers
    
    # returns list of prices of top 10 gainer stocks, in order
    def getPrices(self):
        prices = self.createDataFrame()['Stock Price'].tolist()
        return prices
    
    # returns list of 1-day changes as strings of top 10 gainer stocks, in order
    def getDayChanges(self):
        changes = self.createDataFrame()['% Change'].tolist()
        return changes
    
    # returns list of 1-day changes as floats of top 10 gainer stocks, in order
    def getDayChangesFloat(self):
        temp = self.getDayChanges()
        final = []
        for i in range(10):
            final.append(float(temp[i].replace("%","")))
        return final 
    
    # returns list of market caps of top 10 gainer stocks, in order
    def getMarketCaps(self):
        market_caps = self.createDataFrame()['Market Cap'].tolist()
        return market_caps
    
    # returns ticker symbol at some position, 0 <= position <= 9
    def getTickerAt(self, position):
        if position<0 or position>9:
            print("Position input out of bounds; must be between 0 and 9.")
        ticker = self.getTickers()[position]
        return ticker
    
    # returns price at some position, 0 <= position <= 9
    def getPriceAt(self, position):
        if position<0 or position>9:
            print("Position input out of bounds; must be between 0 and 9.")
        price = self.getPrices()[position]
        return price
    
    # returns day change at some position, 0 <= position <= 9
    def getDayChangeAt(self, position):
        if position<0 or position>9:
            print("Position input out of bounds; must be between 0 and 9.")
        change = self.getDayChanges()[position]
        return change

    # returns day change as a float at some position, 0 <= position <= 9
    def getDayChangeFloatAt(self, position):
        if position<0 or position>9:
            print("Position input out of bounds; must be between 0 and 9.")
        change = self.getDayChangesFloat()[position]
        return change

    # returns market cap at some position, 0 <= position <= 9
    def getMarketCapAt(self, position):
        if position<0 or position>9:
            print("Position input out of bounds; must be between 0 and 9.")
        market_cap = self.getMarketCaps()[position]
        return market_cap 


