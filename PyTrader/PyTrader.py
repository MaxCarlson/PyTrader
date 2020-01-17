from Loader import Loader
from Simulation import Simulation

numYears        = 5
numDays         = (365 - 52 * 2) * numYears
startDate       = '2000-1-1'
filename        = '500Tickers'
fullFileName    = filename + startDate + '_' + str(numYears)

loader = Loader()

loader = Loader.loadPickle(fullFileName)

#loader.loadCSV(numDays, startDate)
#loader.processTickers(500, startDate)
#loader.save(fullFileName)

sim = Simulation(loader, '2000-3-1', 20000)
sim.run(loader)

