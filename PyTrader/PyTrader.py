from Loader import *
from Simulation import *

loader = Loader.loadPickle('allTickers.bin')
#loader = Loader()
#loader.loadCSV()
loader.processTickers(500, '2000-1-1')

sim = Simulation(loader, '2000-3-1')