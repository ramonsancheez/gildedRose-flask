from items.item import Item

class normalItem(Item):

    def __init__(self, name, sellIn, quality):
        super().__init__(name, sellIn, quality)
    
    def setQuality(self, newQuality):
        if newQuality > 0:
            self.quality = newQuality
        else:
            self.quality = 0
        if newQuality > 50:
            self.quality = 50

    def getSelling(self):
        return self.sellIn

    def getQuality(self):
        return self.quality

    def reduceSellIn(self):
        self.sellIn -= 1
    
    def changeQuality(self):
        qualityModified = -1
        if self.sellIn < 0:
            qualityModified = -2 
        self.setQuality(self.getQuality() + qualityModified)

    def updateQuality(self):
        self.reduceSellIn()
        self.changeQuality()