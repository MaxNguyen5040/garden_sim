class Plant:
    def __init__(self, name, growth_rate, yield_amount):
        self.name = name
        self.description = description
        self.growth_time = growth_time
        self.water_needed = 0  # Placeholder for water needed
        self.sunlight_needed = 0  # Placeholder for sunlight needed
        self.has_flowers = False
        self.has_fruits = False
        self.is_harvestable = False
        self.is_dead = False
        self.is_watered = False
        self.is_sunlit = False


    def breed(self, partner_plant):
        offspring_name = f"{self.name}-{partner_plant.name}"
        offspring_description = f"A hybrid of {self.name} and {partner_plant.name}"
        offspring_growth_time = (self.growth_time + partner_plant.growth_time) // 2
        return Plant(offspring_name, offspring_description, offspring_growth_time)

    def grow(self):
        self.water_needed += 1
        self.sunlight_needed += 1
        if self.water_needed >= 3 and self.sunlight_needed >= 3:
            self.is_harvestable = True
        elif self.water_needed >= 1 and self.sunlight_needed >= 1:
            self.has_flowers = True

    def is_ready_for_harvest(self):
        return self.growth_stage >= self.max_growth_stage and self.disease is None

    def use_insecticide(self, garden, insect):
        if self.inventory["insecticide"] > 0:
            self.inventory["insecticide"] -= 1
            garden.remove_insect(insect)
            print(f"{self.name} used insecticide on {insect.name}.")
        else:
            print("No insecticide left!")

    def use_nectar(self, garden):
        if self.inventory["nectar"] > 0:
            self.inventory["nectar"] -= 1
            garden.attract_beneficial_insects()
            print(f"{self.name} used nectar to attract beneficial insects.")
        else:
            print("No nectar left!")

    def get_special_ability(self):
        abilities = ["fast_growth", "resistant", "high_yield"]
        return random.choice(abilities)

    def apply_special_ability(self):
        if self.special_ability == "fast_growth":
            self.growth_stage += 1
        elif self.special_ability == "resistant":
            self.disease = None
        elif self.special_ability == "high_yield":
            self.yield_amount += 1

    def check_for_disease(self):
        if random.random() < 0.1:  # 10% chance to get a disease
            self.disease = "Blight"

    def cure_disease(self):
        self.disease = None

plants = []

plants.extend([
    Plant("Sunflower", "A bright and cheerful flower", 6),
    Plant("Apple Tree", "Produces delicious apples", 12),
    Plant("Cactus", "A desert plant with spines", 8),
    Plant("Orchid", "A delicate and exotic flower", 7),
    Plant("Maple Tree", "Known for its colorful autumn leaves", 15)
])
