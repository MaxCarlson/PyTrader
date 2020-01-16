from Asset import Asset

class Strat():

    def __init__(self, minDays, capital):
        self.minDays        = minDays # Minimum number of days that must be run before applying Strat
        self.holdings       = {}
        self.capital        = capital
        self.principal      = capital
        self.dailyReturns   = []

    def initialize(self):
        pass

    def run(self, stocks, inactives, dayIdx):
        pass

    def getReturn(self):
        pass

    def sellInactiveTicker(self, stocks, inactives, dayIdx):
        sold = False
        for inactive in inactives:
            price = stocks[inactive].getData('adjClose', dayIdx - 1)
            asset = self.holdings[inactive]
            
            if asset.size(): 
                sold = True
            asset.decreasePosition(asset.size(), price)
        self.capital += asset.totalReturn




# Simulate and Index fund of all the stocks in our backtest
# Equal distribution of assets across all stocks
class BuyAndHold(Strat):

    def __init__(self, capital, fee = 0):
        Strat.__init__(self, 0, capital)

    def run(self, stocks, inactives, dayIdx):
        if dayIdx == 0:
            self.firstDay(stocks, inactives, dayIdx)

    def firstDay(self, stocks, inactives, dayIdx):
        if len(inactives) > 0:
            self.sellInactiveTicker(stocks, inactives, dayIdx)

        for symbol, ticker in stocks.items():
                adjClose = ticker.getData('adj_close', dayIdx)
                asset = Asset()
                asset.increasePosition(1, adjClose)
                self.holdings[symbol] = asset

    def getReturn(self):
        pass




class DCA(Strat):
    def __init__(self):
        Strat.__init__(self)

    def run(self, stocks, inactives, dayIdx):
        pass


class MACDStrat(Strat):
    class MACD:
        def __init__(self, short = 12, long = 26):
            self.emaLong        = 0
            self.emaShort       = 0
            self.longPeriod     = long
            self.shortPeriod    = short
            self.longSmoothing  = 2 / (longPeriod + 1)
            self.shortSmoothing = 2 / (shortPeriod + 1)

        def update(self, stocks, close, day, capital):
            self.emaLong  = (close - self.emaLong)  * self.longSmoothing  + self.emaLong
            self.emaShort = (close - self.emaShort) * self.shortSmoothing + self.emaShort

    def __init__(self, capital, short = 12, long = 26):
        Strat.__init__(self, long)
        self.macds = {}

    def run(self, stocks, inactives, dayIdx):
        for stock in stocks:
            if day == 0:
                pass

