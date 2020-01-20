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

    @classmethod
    def isViable(cls, data, dateHandler, maxDays, startDate):
        before  = dateHandler.isAfter(data.iat[0, 0])
        wrange  = dateHandler.withinRange(data.iat[0, 0], data.iat[-1, 0], maxDays) # TODO: These are messed up. Check 3rd ticker AAL to fix
        start   = None
        end     = None
        idx     = 0
        endDate = dateHandler.dateAfterDays(startDate, maxDays)

        if not (before and wrange): return (False, 0, 0)

        # TODO: Realistically, this work only needs to be done once
        # Incorporate that!
        for date in data['date']:
            diffS = dateHandler.difference(date, startDate)
            diffE = dateHandler.difference(date, endDate)
            if not start and diffS <= 0:
                start = idx
            if diffE <= 0:
                end = idx
                break
            idx += 1

        return (before and wrange, start, end)

    def getData(self, field, dateIdx):
        return self.data.at[dateIdx, field]

    def getDataPeriod(self, field, start, end):
        dat = self.data.loc[start:end, field]
        return  dat