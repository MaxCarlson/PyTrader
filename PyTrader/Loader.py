import csv
import random
import pickle
import numpy as np
from Ticker import *
from datetime import datetime

import sys

class Loader():
        
    
    def __init__(self):
        self.epoch          = '1970-1-1'
        self.tickers        = {} 
        self.symbols        = []
        self.activeTickers  = {}

    def loadCSV(self, daysPerTicker=1000000, startDate=None, filename='WIKI_PRICES.csv', delimiter=','):
        
        uTickers = {}
        with open(filename) as csv_file:
            i = 0
            csvReader = csv.reader(csv_file, delimiter=delimiter)
            for line in csvReader:

                if line[0] in uTickers:
                    uTickers[line[0]].append(line[1:])
                else:
                    uTickers[line[0]] = [line[1:]]
                
                # Just for fast testing
                #if i > 1 and len(line[0]) > 1:
                #    break
                i += 1
                if i >= 1000000:
                    break

        self.createTickers(uTickers, daysPerTicker, startDate)
        
    @classmethod
    def loadPickle(self, filename):
        with open(filename, 'rb') as pickleFile:
            return pickle.load(pickleFile)

    def save(self, filename):
        fileHandle = open(filename, 'wb')
        pickle.dump(self, fileHandle)

    def createTickers(self, uTickers, daysPerTicker, startDateStr):

        d0 = datetime.strptime(self.epoch, '%Y-%m-%d').date()
        if startDateStr != None:
            ds          = datetime.strptime(startDateStr, '%Y-%m-%d').date()
            startDate   = (ds - d0).days
        else:
            startDate = -1

        for ticker, data in uTickers.items():
            if ticker == 'ticker':
                continue

            self.symbols.append(ticker)
            self.tickers[ticker] = Ticker(ticker, data, d0, daysPerTicker, startDate)

        self.save('smallTickers' + startDate + '.bin')

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
            if ticker.startDate > startDateInt:
                continue

            self.activeTickers[symbol] = ticker
            choosen += 1

        if choosen < num:
            print('Only', choosen, 'symbols found of the', num, 'desired that fit the requirements')
        

        #a = 5

