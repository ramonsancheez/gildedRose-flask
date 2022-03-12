from items.normalItem import normalItem
class AgedBrie(normalItem):
    
    def __init__(self, name, sellIn, quality):
        super().__init__(name, sellIn, quality)

    def changeQuality(self):
        qualityModified = 1
        if self.sellIn < 0:
            qualityModified += 1
        self.setQuality(self.getQuality() + qualityModified)