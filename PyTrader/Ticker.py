from datetime import datetime
import numpy as np
import pandas as pd
import pickle
import sys
import DateHandler as DateHandler

class Ticker():

    def __init__(self, name, data, fields, startDate):
        self.name       = name
        self.data       = data
        self.startDate  = 0
        self.endDate    = 0
        self.fields     = fields

    def isViable(self, dateHandler, maxDays, startDate):
        before  = dateHandler.isAfter(self.data.iat[0, 0])
        wrange  = dateHandler.withinRange(self.data.iat[0, 0], self.data.iat[-1, 0], maxDays)
        return before and wrange

    def getData(self, field, dateIdx):
        return self.data.at[dateIdx, field]

    def getDataPeriod(self, field, start, end):
        dat = self.data.loc[start:end, field]
        return  dat