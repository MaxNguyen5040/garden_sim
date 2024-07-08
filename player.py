class Player:
    def __init__(self):
        self.resources = {"water": 10, "seeds": 5}

    def plant(self, garden):
        if self.resources["seeds"] > 0:
            garden.add_plant()
            self.resources["seeds"] -= 1
            print("Planted a seed.")
        else:
            print("No seeds left.")

    def water(self, garden):
        if self.resources["water"] > 0:
            garden.water_plants()
            self.resources["water"] -= 1
            print("Watered the plants.")
        else:
            print("No water left.")

    def harvest(self, garden):
        harvested = garden.harvest_plants()
        self.resources["seeds"] += harvested
        print(f"Harvested {harvested} seeds.")

    def check_resources(self):
        print(f"Water: {self.resources['water']}, Seeds: {self.resources['seeds']}")
