from Loader import Loader
from Simulation import Simulation
from DateHandler import DateHandler

numYears        = 5
numDays         = (365 - 52 * 2) * numYears
startDate       = '2000-1-1'
adjStartDate    = '2000-3-1'
filename        = 'allTickers'
fullFileName    = filename + startDate + '_' + str(numYears)
fileToLoad      = 'WIKI_PRICES.csv'

def main():

    dateHandler = DateHandler()

    loader = Loader.loadPickle(fullFileName)

    #loader = Loader(dateHandler)
    #loader.loadCSV(startDate, numDays, fileToLoad)
    #loader.save(fullFileName)

    sim = Simulation(loader, dateHandler, adjStartDate, 20000)
    sim.run(loader)

if __name__ == "__main__":
    main()

