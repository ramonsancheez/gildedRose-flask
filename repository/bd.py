from repository.db_atlas import db_atlas

class bd:
    @staticmethod
    def get_stock():
        return db_atlas.connectDB().find({},{"_id":False})
    
    @staticmethod
    def get_nombre(itemNombre):
        return db_atlas.connectDB().find({"name": itemNombre}, {"_id":False})