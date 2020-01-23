import csv
import random
import pickle
import numpy as np
import pandas as pd
from Ticker import Ticker
from datetime import datetime
from DateHandler import DateHandler
import multiprocessing



class Loader():
        
    
    def __init__(self, dateHandler):
        self.epoch          = '1970-1-1'
        self.dateHandler    = dateHandler
        self.tickers        = {} 

    def loadCSV(self, startDate='', maxDays=365*10, filename='', delimiter=','):
        idx     = 0
        dbg     = 0
        df      = pd.read_csv(filename)

        while idx < len(df):
            if idx >= len(df):
                break

            symbol  = df.iat[idx, 0]
            #if idx != 0:
            #    val = df.iat[idx-1, 0]
            data    = df.loc[df['ticker'].isin([symbol])]
            data    = data.drop('ticker', 1)
            idx     += len(data)

            # TODO: Need to factor in weekends and holidays when adjusting date ranges
            viable, startIdx, endIdx = Ticker.isViable(data, self.dateHandler, startDate, maxDays)
            if not viable:
                continue

            data = data[startIdx:endIdx]
            self.tickers[symbol] = Ticker(symbol, data, startDate)

            # Debugging
            dbg += 1
            if dbg >= 50:
                break
            
        a = 5
        
    @classmethod
    def loadPickle(self, filename, extension = '.bin'):
        with open(filename + extension, 'rb') as pickleFile:
            return pickle.load(pickleFile)

    def save(self, filename, extension = '.bin'):
        filename += extension
        fileHandle = open(filename, 'wb')
        pickle.dump(self, fileHandle)


