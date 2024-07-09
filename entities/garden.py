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

    def add_animal(self, animal):
        self.animals.append(animal)
        self.check_symbiosis()

    def check_biodiversity(self):
        if len(set([plant.species for plant in self.plants])) > 5:
            tooltip_biodiversity.display()

    def check_symbiosis(self):
        if any(animal for animal in self.animals if animal.role == "pollinator"):
            tooltip_symbiosis.display()

    def simulate_day(self):
        for plant in self.plants:
            plant.grow()
            insect = random.choice(self.insects)
            insect.interact_with_plant(plant)
