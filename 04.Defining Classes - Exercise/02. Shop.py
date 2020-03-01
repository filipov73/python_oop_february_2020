class Shop:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)


shop = Shop("1", ["Apples", "Bananas", "Cucumbers"])
shop.items.append("123")
print(shop.get_items_count())
