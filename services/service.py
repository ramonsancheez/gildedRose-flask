from repository.bd import bd

class service:
    @staticmethod
    def get_stock():
        stock = bd.get_stock()
        items = []
        for item in stock:
            items.append(item)
        return items
    
    @staticmethod
    def get_oneItem(name, quality, sell_in):
        stock = bd.get_oneItem(name, quality, sell_in)
        items = []
        for item in stock:
            items.append(item)
        return items

    @staticmethod
    def get_nombre(itemNombre):
        stock = bd.get_nombre(itemNombre)
        items = []
        for item in stock:
            items.append(item)
        return items

    @staticmethod
    def get_quality(numQuality):
        stock = bd.get_quality(numQuality)
        items = []
        for item in stock:
            items.append(item)
        return items

    @staticmethod
    def get_sellIn(numSellIn):
        stock = bd.get_sellIn(numSellIn)
        items = []
        for item in stock:
            items.append(item)
        return items
    
    @staticmethod
    def delete_item(deletedItemName):
        if service.get_nombre(deletedItemName) == []:
            return "No se ha podido encontrar el item: " + deletedItemName+ ", que desea eliminar"
        else:
            bd.delete_item(deletedItemName)
            return "El item con nombre " + deletedItemName + " ha sido eliminado"

    @staticmethod
    def newItem(name, quality, sell_in):
        items = ["Conjured", "Sulfuras", "Aged_brie", "Back_stage", "Normal_item"]
        name = name.capitalize()
        if name in items:
            newItem = {"name": name, "quality": int(quality), "sell_in": int(sell_in)}
            bd.newItem(newItem)
            return "El item se ha creado correctamente"
        else:
            return "No se ha podido crear el item: " + name

    @staticmethod
    def updateItem(item, quality, sell_in):
        bd.updateItem(item, quality, sell_in)
        return service.get_nombre(item)