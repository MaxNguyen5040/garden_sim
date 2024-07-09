class Garden:
    def __init__(self):
        self.plants = []
        self.insects = [ladybug, bee, aphid, beetle]

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to the garden!")

    def remove_insect(self, insect):
        if insect in self.insects:
            self.insects.remove(insect)
            print(f"{insect.name} removed from the garden.")
        else:
            print(f"{insect.name} not found in the garden.")

    def attract_beneficial_insects(self):
        self.insects.extend([ladybug, bee])
        print("Beneficial insects attracted to the garden.")

    def simulate_day(self):
        for plant in self.plants:
            plant.grow()
            insect = random.choice(self.insects)
            insect.interact_with_plant(plant)
