from repository.db_atlas import db_atlas

class bd:
    @staticmethod
    def get_stock():
        return db_atlas.connectDB().find({},{"_id":False})
    
    @staticmethod
    def get_nombre(itemNombre):
        return db_atlas.connectDB().find({"name": itemNombre}, {"_id":False})
    
    @staticmethod
    def get_quality(numQuality):
        return db_atlas.connectDB().find({"quality": int(numQuality)}, {"_id":False})

    @staticmethod
    def get_sellIn(numSellIn):
        return db_atlas.connectDB().find({"sell_in": int(numSellIn)}, {"_id":False})