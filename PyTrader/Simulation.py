from datetime import datetime
from Strat import Strat, BuyAndHold
from Loader import Loader


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

    def run(self, loader):
        while self.step(loader):
            pass
        
    def step(self, loader):
        
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

        self.checkDates(loader)
        self.updateStrats(loader, inactiveTickers)
        self.updateBenchmarks(loader, inactiveTickers)
        self.idx += 1
        return True

    def updateStrats(self, loader, inactives):
        for strat in self.strats:
            pass

    def updateBenchmarks(self, loader, inactives):
        for bench in self.benchmarks:
            bench.run(loader.tickers, inactives, self.idx)

    # Debugging tool
    def checkDates(self, loader):
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


