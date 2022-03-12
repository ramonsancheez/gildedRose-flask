class GildedRose():
    def __init__(self):
        self.stock = []
    
    def add(self, newItem):
        self.stock.append(newItem)

    def updateStock(self):
        for item in self.stock:
            item.updateQuality()

    def printStock(self):
        for item in self.stock:
            print(item)