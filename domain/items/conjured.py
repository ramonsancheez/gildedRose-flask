from items.normalItem import normalItem
class Conjured(normalItem):
    def __init__(self, name, quality, sellIn):
        super().__init__(name, quality, sellIn)
    
    def changeQuality(self):
        qualityModified = -2
        if self.sellIn < 0:
            qualityModified = -4 
        self.setQuality(self.getQuality() + qualityModified)