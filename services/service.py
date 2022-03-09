from repository.bd import bd

class service:
    def inventario():
        stock = bd.get_stock()
        items = []

        for item in stock:
            items.append(item)
        return items