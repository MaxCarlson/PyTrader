import numpy as np
import csv
from datetime import datetime
from Ticker import *

class Loader():
        
    
    def __init__(self):
        self.epoch      = '1970-1-1'
        self.tickers    = {}

    def load(self, filename='WIKI_PRICES.csv', delimiter=','):
        with open(filename) as csv_file:
            csvReader = csv.reader(csv_file, delimiter=delimiter)
            i = 0
            for line in csvReader:
                if line[0] in self.tickers:
                    self.tickers[line[0]].append(line[1:])
                else:
                    self.tickers[line[0]] = [line[1:]]
                
                i += 1
                if i >= 100:
                    break

        self.process()


    def process(self):
        d0 = datetime.strptime(self.epoch, '%Y-%m-%d').date()
        
        for ticker, data in self.tickers.items():
            if ticker == 'ticker':
                continue
            t = Ticker(ticker, data, d0)

        

        a = 5

