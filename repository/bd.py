from repository.db_atlas import db_atlas

class bd:
    @staticmethod
    def get_stock():
        return db_atlas.connectDB().find({},{"_id":False})
    
    @staticmethod
    def get_oneItem(name, quality, sell_in):
        return db_atlas.connectDB().find({"name": name, "quality": int(quality),"sell_in": int(sell_in)}, {"_id":False})

    @staticmethod
    def get_nombre(itemNombre):
        return db_atlas.connectDB().find({"name": itemNombre}, {"_id":False})
    
    @staticmethod
    def get_quality(numQuality):
        return db_atlas.connectDB().find({"quality": int(numQuality)}, {"_id":False})

    @staticmethod
    def get_sellIn(numSellIn):
        return db_atlas.connectDB().find({"sell_in": int(numSellIn)}, {"_id":False})
        
    @staticmethod
    def delete_item(deletedItemName):
        db_atlas.connectDB().delete_one({"name":deletedItemName})
    
    @staticmethod
    def newItem(newItem):
        db_atlas.connectDB().insert_one(newItem)

    @staticmethod
    def updateItem(item, quality, sell_in):
        updatedItem = {"name": item}
        updatedInfo = {"$set": {"quality": int(quality), "sell_in": int(sell_in)}}
        db_atlas.connectDB().update_one(updatedItem, updatedInfo)
