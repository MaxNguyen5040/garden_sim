# soil.py
class Soil:
    def __init__(self):
        self.nutrient_levels = 50  # Initial nutrient level

    def add_fertilizer(self, amount):
        self.nutrient_levels += amount

    def deplete_nutrients(self):
        self.nutrient_levels -= 1

    def get_nutrient_levels(self):
        return self.nutrient_levels
