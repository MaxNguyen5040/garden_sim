import random

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Shopkeeper:
    def __init__(self, name):
        self.name = name
        self.inventory = {}

    def add_item(self, item, price):
        self.inventory[item.name] = Item(item.name, price)

    def sell_item(self, item_name):
        if item_name in self.inventory:
            return self.inventory.pop(item_name)
        return None

class Marketplace:
    def __init__(self):
        self.shopkeepers = {}

    def add_shopkeeper(self, shopkeeper):
        self.shopkeepers[shopkeeper.name] = shopkeeper

    def buy_item(self, shopkeeper_name, item_name):
        if shopkeeper_name in self.shopkeepers:
            shopkeeper = self.shopkeepers[shopkeeper_name]
            return shopkeeper.sell_item(item_name)
        return None

# Create shopkeepers and items
seed_shopkeeper = Shopkeeper("Seed Shop")
seed_shopkeeper.add_item(Item("Carrot Seeds", 10), 15)
seed_shopkeeper.add_item(Item("Tomato Seeds", 8), 12)
seed_shopkeeper.add_item(Item("Lettuce Seeds", 5), 10)


