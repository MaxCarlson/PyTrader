from datetime import datetime
import numpy as np
import pickle
import sys

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
            idx     = 1
            arow    = [dateInt]
            for v in row[1:]:
                if v == '':
                    found = False
                    for p in range(-1, -10, -1):
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

            i+=1
            prevRow = row
            array.append(arow)
        
        self.data = array

        #pi2 = pickle.dumps(self)
        #s2 = sys.getsizeof(pi2)
        a = 5
