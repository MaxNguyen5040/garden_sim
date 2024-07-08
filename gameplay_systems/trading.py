class Trader:
    def __init__(self):
        self.prices = {"water": 1, "seeds": 2, "fertilizer": 3}

    def buy(self, player, item, amount):
        if item in self.prices:
            cost = self.prices[item] * amount
            if player.resources["seeds"] >= cost:
                player.resources["seeds"] -= cost
                player.inventory.add_item(item, amount)
                print(f"Bought {amount} {item}(s) for {cost} seeds.")
            else:
                print("Not enough seeds to buy that.")
        else:
            print("Item not available.")

    def sell(self, player, item, amount):
        if item in player.inventory.items and player.inventory.items[item] >= amount:
            player.inventory.remove_item(item, amount)
            earnings = self.prices[item] * amount // 2
            player.resources["seeds"] += earnings
            print(f"Sold {amount} {item}(s) for {earnings} seeds.")
        else:
            print("Not enough items to sell.")
