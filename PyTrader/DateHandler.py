from datetime import datetime, timedelta

# TODO: Dates should be handled numerically and 
# transfored back later if needed through this class
# TODO: Abstract this class so it handles any time period, not just days

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

    # Test if the time range ts1-te1 is within the range ts0-te0
    def withinRange(self, ts0, te0, ts1, te1):
        start   = self.strToDate(ts1) <= self.strToDate(ts0)
        end     = self.strToDate(te1) >= self.strToDate(te0)
        return start and end

    def difference(self, first, second):
        d0 = DateHandler.strToDate(first)
        d1 = DateHandler.strToDate(second)
        return (d1 - d0).days

    def dateAfterDays(self, startDate, days):
        d0 = DateHandler.strToDate(startDate)
        return (d0 + timedelta(days=days)).isoformat()