from datetime import datetime
from Strat import *
from Loader import *


class Simulation():

    def __init__(self, loader, startDate, cash):
        self.idx        = 0
        self.tickerIdxs = {}    
        self.cash       = cash
        self.benchCash  = cash
        self.date       = startDate
        self.startDate  = startDate
        self.epoch      = loader.epoch
        
        #self.normalizeTickerDates(loader)
        self.strats     = []
        self.benchmarks = [BuyAndHold(cash)]

    def run(self):
        while self.step():
            pass
        
    def step(self):
        
        running         = False
        inactiveTickers = {}

        for symbol in loader.activeTickers:
            ticker = loader.tickers[symbol]
            if self.idx >= len(ticker.data): 
                inactiveTickers[symbol]
                continue

            running = True

        if running == False:
            return False

        self.idx += 1
        self.checkDates()
        self.updateStrats(inactiveTickers)
        self.updateBenchmarks(inactiveTickers)
        return True

    def updateStrats(self, inactives):
        for strat in self.strats:
            pass

    def updateBenchmarks(self, inactives):
        for bench in self.benchmarks:
            bench.run(loader.tickers, inactives, self.idx)

    # Debugging tool
    def checkDates(self):
        prevDate = None
        for symbol in loader.activeTickers:
            ticker  = loader.tickers[symbol]
            if self.idx >= len(ticker.data): 
                continue

            curDate = ticker.data[self.idx][0]
            if prevDate != None and curDate != prevDate:
                raise RuntimeError("Dates between tickers do NOT match!")

    def normalizeTickerDates(self, loader):
        #de      = datetime.strptime(self.epoch,     '%Y-%m-%d').date()
        #d0      = datetime.strptime(self.startDate, '%Y-%m-%d').date()
        #bDays   = (d0 - de).days
        #for symbol in loader.activeTickers:
        #    ticker = loader.tickers[symbol]
        #    a = 5
        pass


