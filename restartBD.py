from repository.db_atlas import db_atlas

db_atlas.connectDB().delete_many({})
inventario = [["Normal_item", 10, 20],
                  ["Aged_brie", 2, 0],
                  ["Normal_item", 5, 7],
                  ["Sulfuras", 0, 80],
                  ["Sulfuras", -1, 80],
                  ["Back_stage", 15, 20],
                  ["Back_stage", 10, 49],
                  ["Back_stage", 5, 49],
                  ["Conjured", 3, 6]]

inventarioDict = []
for item in inventario:
    inventarioDict.append({"name":item[0],"quality":item[1],"sell_in":item[2]})
db_atlas.connectDB().insert_many(inventarioDict)