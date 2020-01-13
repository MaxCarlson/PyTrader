from datetime import datetime
from Strat import *
from Loader import *


class Simulation():

    def __init__(self, loader, startDate, cash):
        self.epoch      = loader.epoch
        self.date       = startDate
        self.startDate  = startDate
        self.cash       = cash
        #self.
        self.normalizeTickerDates(loader)
        
    def step(self):
        pass

    def normalizeTickerDates(self, loader):

        de      = datetime.strptime(self.epoch,     '%Y-%m-%d').date()
        d0      = datetime.strptime(self.startDate, '%Y-%m-%d').date()
        bDays   = (d0 - de).days

        for symbol in loader.activeTickers:
            ticker  = loader.tickers[symbol]
            ticker.startDate += bDays - ticker.startDate
            a = 5
    
