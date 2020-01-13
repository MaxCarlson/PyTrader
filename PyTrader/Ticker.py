from datetime import datetime
import numpy as np
import pickle
import sys

class Ticker():

    def __init__(self, name, data, epoch, maxDays, startDate):
        self.name       = name
        self.data       = np.array([])
        self.startDate  = 0
        self.endDate    = 0
        self.csvToNp(data, epoch, maxDays, startDate)

    @classmethod
    def isViable(self, data, epoch, maxDays, startDate):
        d0 = datetime.strptime(data[0][0], '%Y-%m-%d').date()
        days = (d0 - epoch).days 
        if days > startDate + maxDays:
            return False
        return True

    def csvToNp(self, data, epoch, maxDays, startDate): 
        i       = -1
        array   = []
        prevRow = ''
        started     = False
        for row in data:
            i               += 1
            d1              = datetime.strptime(row[0], '%Y-%m-%d').date()
            dateInt         = (d1 - epoch).days

            # Don't start recording data until a start date, if one has been specified
            # Don't grab tickers past the maxDate

            if dateInt - startDate >= maxDays:
                break

            if started:
                pass
            elif (started == False and dateInt >= startDate) or startDate == -1:
                started         = True
                self.startDate  = dateInt
            else:
                continue

            # Do our best to correct missing data
            idx     = 1
            arow    = [dateInt]
            for v in row[1:]:
                if v == '':
                    found = False
                    for p in range(-1, -5, -1):
                        if data[i+p][idx] != '':
                            v = data[i+p][idx]
                            found = True
                            break

                    # If there is too big a gap, stop trying to fix it
                    if found == False:
                        self.data = array
                        return

                arow.append(float(v))
                idx += 1

            prevRow = row
            array.append(arow)

        self.data       = array
        self.endDate    = self.data[-1][0]

        #pi2 = pickle.dumps(self)
        #s2 = sys.getsizeof(pi2)
        a = 5
