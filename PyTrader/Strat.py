

class Strat():

    def __init__(self, minDays, capital):
        self.minDays    = minDays # Minimum number of days that must be run before applying Strat
        self.holdings   = {}
        self.capital    = capital

    def run(self, stocks, inactive, dayIdx):
        pass

    def sellInactiveTicker(self, inactiveTickers):
        pass


class BuyAndHold(Strat):

    def __init__(self, capital):
        Strat.__init__(self, 0)

    def run(self, stocks, inactive, dayIdx):
        if day != 0:
            return


class DCA(Strat):
    def __init__(self):
        Strat.__init__(self)

    def run(self, stocks, inactive, dayIdx):
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

    def run(self, stocks, inactive, dayIdx):
        for stock in stocks:
            if day == 0:


