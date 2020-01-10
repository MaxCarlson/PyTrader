from datetime import datetime
import numpy as np

class Ticker():

    def __init__(self, name, data, epoch):
        self.name = name
        self.data = np.array([])

        self.csvToNp(data, epoch)


    def csvToNp(self, data, epoch):
        i = 0
        array = []
        for row in data:
            d1              = datetime.strptime(row[0], '%Y-%m-%d').date()
            dateInt         = (d1 - epoch).days
            arow            = [dateInt] + [float(x) for x in row[1:]]
            array.append(arow)
            i+=1
        self.data = array
        a = 5
