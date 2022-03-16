from items.normalItem import normalItem

class Sulfuras(normalItem):  
    def __init__(self, name, sellIn, quality):
        super().__init__(name, sellIn, quality)
    
    def updateQuality(self):
        self.quality = 80