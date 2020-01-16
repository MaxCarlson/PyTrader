from Loader import Loader
from Simulation import Simulation

startDate = '2000-1-1'

loader = Loader.loadPickle('debugTickers' + startDate)
#loader = Loader.loadPickle('allTickers')
loader.processTickers(500, startDate)

#loader = Loader()
#loader.loadCSV(800, startDate)
#loader.processTickers(500, startDate)
#loader.save('debugTickers' + startDate)

sim = Simulation(loader, '2000-3-1', 20000)
sim.run(loader)