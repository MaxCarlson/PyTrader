from Loader import *
from Simulation import *

loader = Loader.loadPickle('smallTickers2000-1-1.bin')
#loader = Loader.loadPickle('allTickers.bin')
#loader = Loader()
#loader.loadCSV(800, '2000-1-1')
loader.processTickers(500, '2000-1-1')

sim = Simulation(loader, '2000-3-1', 20000)
sim.run()