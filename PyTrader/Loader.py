import numpy as np
import csv

class Loader():
        
    def __init__(self):
        self.tickers = {}
        return

    def load(self, filename='WIKI_PRICES.csv', delimiter=','):
        with open(filename) as csv_file:
            csvReader = csv.reader(csv_file, delimiter=delimiter)
            for line in csvReader:
                if line[0] in self.tickers:
                    self.tickers[line[0]].append(line[1:])
                else:
                    self.tickers[line[0]] = [line[1:]]

