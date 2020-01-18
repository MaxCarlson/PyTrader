from datetime import datetime

class DateHandler():

    def __init__(self, epoch = '1970-1-1', period = 'days'):
        self.epoch      = epoch
        self.epochDate  = datetime.strptime(epoch, '%Y-%m-%d').date()

    def dateToInt(self, date):
        d1 = datetime.strptime(date, '%Y-%m-%d').date()
        return (d1 - self.epochDate).days

    def dateDefault(self, date1, date0):
        if not date0:
            d0 = self.epochDate
        else:
            d0 = datetime.strptime(date0, '%Y-%m-%d').date()
        d1 = datetime.strptime(date1, '%Y-%m-%d').date()
        return (d0, d1)

    # Is date0 before (<=) date1
    def onBefore(self, date1, date0 = None):
        d0, d1 = self.dateDefault(date1, date0)
        return d0 <= d1

    # Is date0 after (>=) date1
    def onAfter(self, date1, date0 = None):
        d0, d1 = self.dateDefault(date1, date0)
        return d0 >= d1