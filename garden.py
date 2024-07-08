class Garden:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def water_plants(self):
        for plant in self.plants:
            plant.grow()
            plant.apply_special_ability()

    def fertilize_plants(self):
        for plant in self.plants:
            plant.grow()
            plant.grow()
            plant.apply_special_ability()

    def harvest_plants(self):
        ready_plants = [plant for plant in self.plants if plant.is_ready_for_harvest()]
        harvested_amount = sum(plant.yield_amount for plant in ready_plants)
        self.plants = [plant for plant in self.plants if not plant.is_ready_for_harvest()]
        return harvested_amount
