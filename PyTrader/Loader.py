import csv
import random
import pickle
import numpy as np
import pandas as pd
from Ticker import Ticker
from datetime import datetime
from DateHandler import DateHandler

class Loader():
        
    
    def __init__(self, dateHandler):
        self.epoch          = '1970-1-1'
        self.dateHandler    = dateHandler
        self.tickers        = {} 
        self.symbols        = []
        self.activeTickers  = {}
        self.fields         = {}

    def loadCSV(self, startDate='', daysPerTicker=1000000, filename='', delimiter=','):
        idx = -1
        num = 0
        df  = pd.read_csv(filename)
        prevSymbol = None
        for symbol in df['ticker']:
            idx += 1
            if not prevSymbol:          prevSymbol = symbol
            if symbol == prevSymbol:    continue

            dfTicker    = df.iloc[0:idx-1, 1:-1]
            ticker      = Ticker(prevSymbol, dfTicker, self.fields, startDate)
            if not ticker.isViable(self.dateHandler, daysPerTicker, startDate):
                continue
            self.tickers[prevSymbol] = ticker
            prevSymbol = symbol

            num += 1
            if num >= 50:
                break
        
    @classmethod
    def loadPickle(self, filename, extension = '.bin'):
        with open(filename + extension, 'rb') as pickleFile:
            return pickle.load(pickleFile)

    def save(self, filename, extension = '.bin'):
        filename += extension
        fileHandle = open(filename, 'wb')
        pickle.dump(self, fileHandle)

    def createTickers(self, uTickers, daysPerTicker, startDateStr):

        d0 = datetime.strptime(self.epoch, '%Y-%m-%d').date()
        if startDateStr != '':
            ds          = datetime.strptime(startDateStr, '%Y-%m-%d').date()
            startDate   = (ds - d0).days
        else:
            startDate = -1

        for ticker, data in uTickers.items():

            # Fill out fields
            if ticker == 'ticker': 
                idx = 0
                for field in data[0]:
                    self.fields[field] = idx
                    idx += 1
                continue

            if Ticker.isViable(data, d0, daysPerTicker, startDate) == False:
                continue

            # Create ticker
            self.symbols.append(ticker)
            t = Ticker(ticker, data, self.fields, d0, daysPerTicker, startDate)
            t.csvToNp(data, d0, daysPerTicker, startDate)
            self.tickers[ticker] = t

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

            self.activeTickers[symbol] = ticker
            choosen += 1

        if choosen < num:
            print('Only', choosen, 'symbols found of the', num, 'desired that fit the requirements')
        

        #a = 5

