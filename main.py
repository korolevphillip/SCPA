import time
from gainers import Gainer
from losers import Loser 
import yfinance as yf
from calculateVolatility import calculateVolatility

def main():
    
    # creating our gainer and loser objects
    gainers = Gainer()
    losers = Loser()
    
    start_time = time.time()

    # printing gainers data 
    df_gainers = gainers.createDataFrame()
    print("Top 10 Gainers Info:\n{}\n".format(df_gainers))

    # printing losers data
    df_losers = losers.createDataFrame()
    print("Top 10 Losers Info:\n{}\n".format(df_losers))

    # printing gainer stock volatility, while appending values to a list
    gainer_vol = []
    print("Evaluating Gainer Stock Volatility...\n")
    for i in range(10):
        vol = calculateVolatility(gainers.getTickerAt(i), gainers.getDayChangeFloatAt(i))
        print(gainers.getTickerAt(i), ": ", vol)
        gainer_vol.append(vol)

    # printing loser stock volatility, while appending values to a list
    loser_vol = []
    print("")
    print("Evaluating Loser Stock Volatility...\n")
    for i in range(10):
        vol = calculateVolatility(losers.getTickerAt(i), losers.getDayChangeFloatAt(i))
        print(losers.getTickerAt(i), ": ", vol)
        loser_vol.append(vol)
    
    # Now, the program suggests 3 gainer stocks to short, these are the 3 most volatile stocks
    print("")
    print("Evaluating Appropriate Stocks to SHORT Based on Highest Volatility...")
    for i in range(3):
        max_vol = max(gainer_vol)
        max_index = gainer_vol.index(max_vol)
        print(gainers.getTickerAt(max_index), " | Price: ", gainers.getPriceAt(max_index), 
              " | % Change 1D: ", gainers.getDayChangeAt(max_index), " | Market Cap: ", gainers.getMarketCapAt(max_index),
              " | Volatility: ", gainer_vol[max_index])
        gainer_vol[max_index] = 0
    
    # Now, the program suggests 3 loser stocks to buy, these are the 3 most volatile stocks
    print("")
    print("Evaluating Appropriate Stocks to BUY Based on Highest Volatility...")
    for i in range(3):
        max_vol = max(loser_vol)
        max_index = loser_vol.index(max_vol)
        print(losers.getTickerAt(max_index), " | Price: ", losers.getPriceAt(max_index), 
              " | % Change 1D: ", losers.getDayChangeAt(max_index), " | Market Cap: ", losers.getMarketCapAt(max_index),
              " | Volatility: ", loser_vol[max_index])
        loser_vol[max_index] = 0

    # recording end time
    end_time = time.time()

    #printing total excution time
    execution_time = end_time - start_time
    print("\nExecution time: ", execution_time, " seconds")
    input('Press ENTER to exit')


    
main()


