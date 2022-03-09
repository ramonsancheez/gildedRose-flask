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
    
