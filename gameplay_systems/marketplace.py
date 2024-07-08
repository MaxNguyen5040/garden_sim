import random

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Shopkeeper:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
        self.market = Market()

    def display_prices(self):
        prices = self.market.get_prices()
        print(f"{self.name}'s Shop Prices: {prices}")

    def apply_market_event(self):
        self.market.apply_price_event()

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

# Create shopkeepers and items with random prices
def generate_random_price(base_price):
    return round(base_price * random.uniform(0.8, 1.2), 2)

seed_shopkeeper = Shopkeeper("Seed Shop")
seed_items = ["Carrot Seeds", "Tomato Seeds", "Lettuce Seeds"]
for item_name in seed_items:
    seed_shopkeeper.add_item(Item(item_name, generate_random_price(10)), generate_random_price(15))

animal_shopkeeper = Shopkeeper("Animal Shop")
animal_items = ["Chickens", "Bees", "Goats"]
for item_name in animal_items:
    animal_shopkeeper.add_item(Item(item_name, generate_random_price(20)), generate_random_price(25))

tool_shopkeeper = Shopkeeper("Tool Shop")
tool_items = ["Watering Can", "Shovel", "Fertilizer"]
for item_name in tool_items:
    tool_shopkeeper.add_item(Item(item_name, generate_random_price(15)), generate_random_price(20))

decoration_shopkeeper = Shopkeeper("Decoration Shop")
decoration_items = ["Garden Gnome", "Wind Chimes", "Fountain"]
for item_name in decoration_items:
    decoration_shopkeeper.add_item(Item(item_name, generate_random_price(30)), generate_random_price(35))

# Initialize the marketplace and add shopkeepers
marketplace = Marketplace()
marketplace.add_shopkeeper(seed_shopkeeper)
marketplace.add_shopkeeper(animal_shopkeeper)
marketplace.add_shopkeeper(tool_shopkeeper)
marketplace.add_shopkeeper(decoration_shopkeeper)

# Example usage: Buying and selling items
item_to_buy = marketplace.buy_item("Seed Shop", "Carrot Seeds")
if item_to_buy:
    print(f"Bought {item_to_buy.name} for {item_to_buy.price} coins.")
else:
    print("Item not available.")

item_to_sell = seed_shopkeeper.sell_item("Tomato Seeds")
if item_to_sell:
    print(f"Sold {item_to_sell.name} for {item_to_sell.price} coins.")
else:
    print("Failed to sell item.")

# Example usage: Checking inventory after transactions
print("Seed Shop Inventory:", [item.name for item in seed_shopkeeper.inventory.values()])
print("Animal Shop Inventory:", [item.name for item in animal_shopkeeper.inventory.values()])
print("Tool Shop Inventory:", [item.name for item in tool_shopkeeper.inventory.values()])
print("Decoration Shop Inventory:", [item.name for item in decoration_shopkeeper.inventory.values()])
