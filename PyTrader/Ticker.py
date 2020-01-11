from datetime import datetime
import numpy as np

class Ticker():

    def __init__(self, name, data, epoch):
        self.name       = name
        self.data       = np.array([])
        self.startDate  = 0
        self.csvToNp(data, epoch)


    def csvToNp(self, data, epoch):
        i       = 0
        array   = []
        prevRow = ''
        for row in data:
            d1              = datetime.strptime(row[0], '%Y-%m-%d').date()
            dateInt         = (d1 - epoch).days
            if i == 0:
                self.startDate = dateInt

            # Do our best to correct missing data
            arow = [dateInt]
            idx = 1
            for v in row[1:]:
                if v == '':
                    v = prevRow[idx]
                arow.append(float(v))
                idx += 1

            i+=1
            prevRow = row
            array.append(arow)
        
        self.data = array
