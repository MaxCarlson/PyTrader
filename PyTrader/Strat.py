

class Strat():

    def __init__(self, minDays):
        self.minDays = minDays # Minimum number of days that must be run before applying Strat
        pass

    def run(self, close, days):
        pass


class BuyAndHold(Strat):

    def __init__(self, minDays):
        Strat.__init__(self, minDays)

    def run(self, close, days):
        if days != 0:
            return


class DCA(Strat):
    def __init__(self):
        Strat.__init__(self)


class MACDStrat(Strat):

    def __init__(self, short = 12, long = 26):
        Strat.__init__(self, long)
        self.emaLong        = 0
        self.emaShort       = 0
        self.longPeriod     = long
        self.shortPeriod    = short
        self.longSmoothing  = 2 / (longPeriod + 1)
        self.shortSmoothing = 2 / (shortPeriod + 1)

    def run(self, close, days):
        self.emaLong  = (close - self.emaLong)  * self.longSmoothing  + self.emaLong
        self.emaShort = (close - self.emaShort) * self.shortSmoothing + self.emaShort


