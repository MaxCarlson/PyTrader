from datetime import datetime
from Strat import Strat, BuyAndHold, MACDStrat
from Loader import Loader

# TODO: Date needs to be handled better and made into a human readable format
# Also have to add in the concept of proper weeks/months
class Simulation():

    def __init__(self, loader, startDate, cash):
        self.idx        = 0
        self.start      = False
        self.tickerIdxs = {}    
        self.cash       = cash
        self.benchCash  = cash
        self.date       = startDate
        self.startDate  = startDate
        self.epoch      = loader.epoch
        self.inactiveSymbols = {}
        
        #self.normalizeTickerDates(loader)
        self.strats     = [MACDStrat(cash)]
        self.benchmarks = [BuyAndHold(cash)]

    def run(self, loader):
        while self.step(loader):
            pass
        self.printReturns()
        
    def step(self, loader):
 
        running         = False
        newlyInactives  = {}
        for symbol in loader.activeTickers:
            if symbol in self.inactiveSymbols:
                continue
            ticker = loader.activeTickers[symbol]
            if self.idx >= len(ticker.data): # TODO: This is broken!!!
                newlyInactives[symbol] = ticker 
                continue

            running = True

        # Inactivete dead symbols and see if 
        # we can start our sim if it hasn't already started
        #self.checkDates(loader) # debugging
        self.inactiveSymbols.update(newlyInactives)
        self.startSim(loader)
        
        self.updateStrats(loader, newlyInactives)
        self.updateBenchmarks(loader, newlyInactives)
        self.idx += 1
        return running

    # Are we ready to start the sim?
    def startSim(self, loader):
        if self.start: return

        self.start = True
        for strat in self.strats:
            self.start &= self.idx >= strat.minDays - 1
        if self.start:
            for strat in self.strats:       strat.dayZero(loader.activeTickers, self.inactiveSymbols, self.idx)
            for bench in self.benchmarks:   bench.dayZero(loader.activeTickers, self.inactiveSymbols, self.idx)

    def updateStrats(self, loader, inactives):
        for strat in self.strats:
            if self.idx == 0:
                strat.initialize(loader.activeTickers, self.idx)
            if self.start:
                strat.run(loader.activeTickers, inactives, self.idx)
            else:
                Strat.run(strat, loader.activeTickers, inactives, self.idx)

    def updateBenchmarks(self, loader, inactives):
        for bench in self.benchmarks:
            if self.idx == 0:
                bench.initialize(loader.activeTickers, self.idx)
            if self.start:
                bench.run(loader.activeTickers, inactives, self.idx)
            else:
                Strat.run(bench, loader.activeTickers, inactives, self.idx)

    # Debugging tool
    def checkDates(self, loader):
        prevDate = None
        for symbol in loader.activeTickers:
            ticker  = loader.activeTickers[symbol]
            if self.idx >= len(ticker.data): 
                continue

            curDate = ticker.data[self.idx][0]
            if prevDate != None and curDate != prevDate:
                raise RuntimeError("Dates between tickers do NOT match!")

    def printReturns(self):
        print("Benchmarks: ")
        for bench in self.benchmarks:
            print(type(bench).__name__, bench.percentReturn(), '%\n')


