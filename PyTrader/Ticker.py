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
        self.fields     = fields

    @classmethod
    def isViable(cls, data, dateHandler, maxDays, startDate):
        endDate = dateHandler.dateAfterDays(startDate, maxDays)
        wrange  = dateHandler.withinRange(startDate, endDate, data.iat[0, 0], data.iat[-1, 0])
        start   = None
        end     = None
        idx     = 0

        if not wrange: return (False, 0, 0)

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

        return (wrange, start, end)

    def getData(self, field, dateIdx):
        return self.data.iat[dateIdx, self.data.columns.get_loc(field)]

    def getDataPeriod(self, field, start, end):
        dat = self.data.loc[start:end, field]
        return  dat