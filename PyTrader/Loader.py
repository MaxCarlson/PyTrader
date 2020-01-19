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


