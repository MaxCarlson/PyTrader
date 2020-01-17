from Asset import Asset
import pandas as pd


# TODO: Define a print for Start
# TODO: integrate a graph utility
class Strat():

    def __init__(self, minDays, capital, dailies = None, monthlies = None):
        self.assets         = {}
        self.minDays        = minDays # Minimum number of days that must be run before applying Strat
        self.capital        = capital
        self.principal      = capital
        self.dailyReturns   = [] if dailies   else None
        self.monthlyReturns = [] if monthlies else None

    def initialize(self, stocks, dayIdx):
        pass

    def run(self, stocks, inactives, dayIdx):
        self.sellInactives(stocks, inactives, dayIdx)

    def percentReturn(self):
        return 0 # TODO

    def purchase(self, symbol, ticker, num, dayIdx, field = 'adj_close'):
        price   = ticker.getData(field, dayIdx)
        asset   = self.assets.get(symbol)
        if not asset: 
            asset = Asset()
        
        netCost = asset.increasePosition(num, price)
        self.assets[symbol] = asset
        self.capital -= netCost

    def sellAllHoldings(self, stocks, dayIdx):
        self.sellInactives(stocks, [key for key, a in self.assets.items()], dayIdx)

    # If we have no more data for a stock, sell it off
    def sellInactives(self, stocks, inactives, dayIdx):
        if len(inactives) <= 0: return

        sold = False
        for inactive in inactives:
            price = stocks[inactive].getData('adj_close', dayIdx - 1)
            asset = self.assets[inactive]
            
            if asset.size(): 
                sold = True
            asset.decreasePosition(asset.size(), price)
        self.capital += asset.totalReturn


# Simulate an Index fund of all the stocks in our backtest
# Equal distribution of assets across all stocks
# TODO: Inactive tickers will skew the overall results downwards since
# percent return is calculated by summing all returns and averaging them.
# - Need to simulate reinvesting the money that would come back to us after the selloff
class BuyAndHold(Strat):

    def __init__(self, capital):
        Strat.__init__(self, 0, capital)

    def run(self, stocks, inactives, dayIdx):
        Strat.run(self, stocks, inactives, dayIdx)

    def initialize(self, stocks, dayIdx):
        self.capital = 0
        for symbol, ticker in stocks.items():
            self.purchase(symbol, ticker, 1, dayIdx)
        self.capital = -self.capital
    
    def percentReturn(self):
        percent = sum([a.percentReturn for key, a in self.assets.items()])
        percent /= len(self.assets)
        return percent

                

class DCA(Strat):
    def __init__(self):
        Strat.__init__(self)

    def run(self, stocks, inactives, dayIdx):
        pass


class MACDStrat(Strat):
    class MACD():
        def __init__(self):
            self.emaLong  = 0
            self.emaShort = 0

        def update(self, close, shortSmoothing, longSmoothing):
            self.emaLong  = (close - self.emaLong)  * longSmoothing  + self.emaLong
            self.emaShort = (close - self.emaShort) * shortSmoothing + self.emaShort

    def __init__(self, capital, short = 12, long = 26):
        Strat.__init__(self, long, capital)
        self.macds  = {}
        self.longPeriod     = long
        self.shortPeriod    = short
        self.longSmoothing  = 2 / (self.longPeriod + 1)
        self.shortSmoothing = 2 / (self.shortPeriod + 1)

    def initialize(self, stocks, dayIdx):
        for symbol, ticker in stocks.items():
            macd = self.MACD()
            self.macds[symbol] = macd
            macd.update(ticker.getData('adj_close', dayIdx), self.shortSmoothing, self.longSmoothing)
            
    def run(self, stocks, inactives, dayIdx):
        Strat.run(self, stocks, inactives, dayIdx)

        for symbol, macd in self.macds.items():
            ticker = stocks.get(symbol)
            macd.update(ticker.getData('adj_close', dayIdx), self.shortSmoothing, self.longSmoothing)

