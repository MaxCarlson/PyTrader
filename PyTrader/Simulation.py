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
        self.inactiveSymbols = {}
        
        #self.normalizeTickerDates(loader)
        self.strats     = []
        self.benchmarks = [BuyAndHold(cash)]

    def run(self, loader):
        while self.step(loader):
            pass
        self.printReturns()

        a = 5
        
    def step(self, loader):
        
        running         = False
        newlyInactives  = {}
        for symbol in loader.activeTickers:
            if symbol in self.inactiveSymbols:
                continue
            ticker = loader.tickers[symbol]
            if self.idx >= len(ticker.data): 
                newlyInactives[symbol] = ticker
                continue

            running = True


        #self.checkDates(loader) # debugging
        
        self.updateStrats(loader, newlyInactives)
        self.updateBenchmarks(loader, newlyInactives)
        self.idx += 1
        self.inactiveSymbols.update(newlyInactives)
        return running

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

    def printReturns(self):
        print("Benchmarks: ")
        for bench in self.benchmarks:
            print(type(bench).__name__, bench.percentReturn(), '%\n')


