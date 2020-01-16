

class Asset():

    def __init__(self):
        self.avgBuyPrice    = 0
        self.avgSellPrice   = 0
        self.totalPurchased = 0
        self.totalSold      = 0
        self.totalReturn    = 0
        self.percentReturn  = 0


    def size(self):
        return self.totalPurchased - self.totalSold

    def increasePosition(self, numPurchased, price):
        self.avgBuyPrice    = (self.totalPurchased * self.avgBuyPrice + numPurchased * price) / (self.totalPurchased + numPurchased)
        self.totalPurchased += num

    def decreasePosition(self, numToSell, price, slippage = 0): # TODO: Slippage
        self.avgSellPrice   = (self.totalSold * self.avgSellPrice + numToSell * price) / (self.totalSold + numToSell)
        percentReturn       = (100 / self.avgBuyPrice) * price
        self.percentReturn  = (self.percentReturn * self.totalSold + percentReturn * numToSell) / (self.totalPurchased + numToSell)
        self.totalSold      += numToSell
        self.totalReturn    += numToSell * price

