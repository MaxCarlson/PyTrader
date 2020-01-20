from datetime import datetime, timedelta

class DateHandler():

    def __init__(self, epoch = '1970-1-1', period = 'days'):
        self.epoch      = epoch
        self.epochDate  = DateHandler.strToDate(epoch)

    @classmethod
    def strToDate(cls, str):
        return datetime.strptime(str, '%Y-%m-%d').date()

    def dateToInt(self, date):
        d1 = DateHandler.strToDate(date)
        return (d1 - self.epochDate).days

    def intToDate(self, val):
        pass

    # Is date0 before (<=) date1
    def isAfter(self, date1, date0 = None):
        if not date0:
            d0 = self.epochDate
        else:
            d0 = DateHandler.strToDate(date0)
        d1 = DateHandler.strToDate(date1)
        return d0 <= d1

    # Is the distance in days between (end - start) >= maxDays 
    def withinRange(self, start, end, maxDays):
        return self.difference(start, end) >= maxDays

    def difference(self, first, second):
        d0 = DateHandler.strToDate(first)
        d1 = DateHandler.strToDate(second)
        return (d1 - d0).days

    def dateAfterDays(self, startDate, days):
        d0 = DateHandler.strToDate(startDate)
        return (d0 + timedelta(days=days)).isoformat()