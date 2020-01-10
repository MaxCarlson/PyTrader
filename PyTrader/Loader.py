import numpy as np
import csv
from datetime import *

class Loader():
        
    def __init__(self):
        self.tickers = {}

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
        epoch   = '1970-1-1'
        dateStr = self.tickers['A'][0][0]
        d0      = datetime.strptime(epoch,   '%Y-%m-%d').date()
        d1      = datetime.strptime(dateStr, '%Y-%m-%d').date()
        dateInt = (d1 - d0).days
        a = 5

