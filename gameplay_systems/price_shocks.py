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

    def apply_price_event(self):
        event = random.choice(self.price_events)
        for item in self.prices:
            self.prices[item] *= event.impact_factor
        print(f"Event: {event.event_name} | New Prices: {self.prices}")

    def get_prices(self):
        return self.prices

#This is how I would do it
# market.apply_price_event()
