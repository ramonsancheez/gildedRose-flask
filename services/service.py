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
        stock = bd.delete_item(deletedItemName)
        return "El item con nombre " + deletedItemName + " ha sido eliminado"

    @staticmethod
    def newItem(name, quality, sell_in):
        newItem = {"name": name, "quality": quality, "sell_in": sell_in}
        stock = bd.newItem(newItem)
        return "El item se ha creado correctamente"

        