class Inventory:
    def __init__(self):
        self.items = {"water": 10, "seeds": 5, "fertilizer": 2}

    def add_item(self, item, amount):
        if item in self.items:
            self.items[item] += amount
        else:
            self.items[item] = amount

    def remove_item(self, item, amount):
        if item in self.items and self.items[item] >= amount:
            self.items[item] -= amount
        else:
            print(f"Not enough {item} in inventory.")

    def check_inventory(self):
        for item, amount in self.items.items():
            print(f"{item}: {amount}")
