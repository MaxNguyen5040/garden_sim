import random

class MarketEconomics:
    def __init__(self, base_prices):
        self.base_prices = base_prices
        self.price_multipliers = {item_name: 1.0 for item_name in base_prices.keys()}

    def apply_price_shock(self, item_name, shock_multiplier):
        self.price_multipliers[item_name] *= shock_multiplier

    def reset_price_multiplier(self, item_name):
        self.price_multipliers[item_name] = 1.0

    def get_adjusted_price(self, item_name):
        return round(self.base_prices[item_name] * self.price_multipliers[item_name], 2)

# Example base prices for items
base_prices = {
    "Carrot Seeds": 10,
    "Tomato Seeds": 12,
    "Lettuce Seeds": 8,
    "Chickens": 20,
    "Bees": 18,
    "Goats": 25,
    "Watering Can": 15,
    "Shovel": 12,
    "Fertilizer": 8,
    "Garden Gnome": 30,
    "Wind Chimes": 25,
    "Fountain": 35
}

# Initialize market economics with base prices
market_economics = MarketEconomics(base_prices)

def apply_random_price_shock():
    items = list(base_prices.keys())
    item_to_shock = random.choice(items)
    shock_multiplier = random.uniform(0.5, 1.5)
    market_economics.apply_price_shock(item_to_shock, shock_multiplier)
    return f"{item_to_shock} price has been adjusted by {shock_multiplier:.2f}"

def reset_all_price_multipliers():
    for item_name in base_prices.keys():
        market_economics.reset_price_multiplier(item_name)
