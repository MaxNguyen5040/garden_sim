import random

class PriceEvent:
    def __init__(self, event_name, impact_factor):
        self.event_name = event_name
        self.impact_factor = impact_factor

class MarketGoods:
    def __init__(self):
        self.prices = {
            "seeds": 100,
            "fertilizer": 200,
            "animals": 300
        }
        self.price_events = [
            PriceEvent("Drought", 1.5),
            PriceEvent("Bumper Harvest", 0.5),
            PriceEvent("Economic Boom", 2.0),
            PriceEvent("Economic Recession", 0.75),
            PriceEvent("Fertilizer Shortage", 2.5),
            PriceEvent("Seed Surplus", 0.75),
            PriceEvent("Animal Disease Outbreak", 1.8),
            PriceEvent("Government Subsidy", 0.5),
            PriceEvent("Market Crash", 0.6),
            PriceEvent("Festive Season", 1.2)
        ]

    def random_event(self):
        event = random.choice(self.events)
        return event.effect()

    def random_shipment(self):
        item = random.choice(list(self.seed_shop.keys()) + list(self.animal_shop.keys()))
        quantity = random.randint(1, 10)
        self.inventory[item] += quantity
        return f"A random shipment has arrived! You received {quantity} of {item}"

    def treasure_cache(self):
        money_found = random.randint(50, 200)
        self.money += money_found
        return f"You found a treasure cache! You received ${money_found}"

    def government_shipment(self):
        item = random.choice(list(self.seed_shop.keys()) + list(self.animal_shop.keys()))
        quantity = random.randint(5, 15)
        self.inventory[item] += quantity
        return f"A government shipment has arrived! You received {quantity} of {item}"

    def market_crash(self):
        for item in self.seed_shop:
            self.seed_shop[item] *= random.uniform(0.1, 0.5)
        for item in self.animal_shop:
            self.animal_shop[item] *= random.uniform(0.1, 0.5)
        return "Market crash! Prices have dropped significantly."

    def apply_price_event(self):
        event = random.choice(self.price_events)
        for item in self.prices:
            self.prices[item] *= event.impact_factor
        print(f"Event: {event.event_name} | New Prices: {self.prices}")

    def get_prices(self):
        return self.prices

#This is how I would do it
# market.apply_price_event()
