import numpy as np
import csv
from datetime import datetime
from Ticker import *
import random

class Loader():
        
    
    def __init__(self):
        self.epoch          = '1970-1-1'
        self.uTickers       = {}
        self.tickers        = {} 
        self.symbols        = []
        self.activeTickers  = {}

    def loadCSV(self, filename='WIKI_PRICES.csv', delimiter=','):
        with open(filename) as csv_file:
            csvReader = csv.reader(csv_file, delimiter=delimiter)
            i = 0
            for line in csvReader:
                if line[0] in self.uTickers:
                    self.uTickers[line[0]].append(line[1:])
                else:
                    self.uTickers[line[0]] = [line[1:]]
                
                # Just for fast testing
                i += 1
                if i >= 1000:
                   break

        self.createTickers()


    def createTickers(self):
        d0 = datetime.strptime(self.epoch, '%Y-%m-%d').date()
        
        for ticker, data in self.uTickers.items():
            if ticker == 'ticker':
                continue

            self.symbols.append(ticker)
            self.tickers[ticker] = Ticker(ticker, data, d0)

    def processTickers(self, num, startDate):

        d0 = datetime.strptime(startDate,  '%Y-%m-%d').date()
        d1 = datetime.strptime(self.epoch, '%Y-%m-%d').date()
        startDateInt = (d0 - d1).days

        if num > len(self.symbols):
            print('Only', len(self.symbols), 'tickers exist. Reverting to only use existing.')
            num = len(self.symbols)
        
        idxs = [i for i in range(num)]
        random.shuffle(idxs)

        choosen = 0
        for idx in idxs:
            symbol  = self.symbols[idx]
            ticker  = self.tickers[symbol]
            if ticker.startDate < startDateInt:
                continue

            self.activeTickers[symbol] = ticker
            choosen += 1

        if choosen < num:
            print('Only', choosen, 'symbols found of the', num, 'desired')
        

        a = 5

