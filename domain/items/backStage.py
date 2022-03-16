from items.normalItem import normalItem

class BackStage(normalItem):
    def __init__(self, name, quality, sellIn):
        super().__init__(name, quality, sellIn)
    
    def changeQuality(self):
        qualityModified = 1
        if self.sellIn < 0:
            qualityModified = -self.getQuality() 
        elif self.sellIn < 5:
            qualityModified = 3
        elif self.sellIn < 10:
            qualityModified = 2
        else:
            pass
        self.setQuality(self.getQuality() + qualityModified)