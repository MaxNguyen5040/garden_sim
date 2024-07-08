from inventory import Inventory

class Player:
    def __init__(self):
        self.inventory = Inventory()
        self.skills = {"gardening": 1, "watering": 1, "harvesting": 1}
        self.experience = 0

    def plant(self, garden):
        plant_name = input("Enter plant name: ")
        if self.inventory.items["seeds"] > 0:
            garden.add_plant(Plant(plant_name))
            self.inventory.remove_item("seeds", 1)
            self.gain_experience(10)
            print(f"Planted a {plant_name}.")
        else:
            print("No seeds left.")

    def water(self, garden):
        if self.inventory.items["water"] > 0:
            garden.water_plants()
            self.inventory.remove_item("water", 1)
            self.gain_experience(5)
            print("Watered the plants.")
        else:
            print("No water left.")

    def fertilize(self, garden):
        if self.inventory.items["fertilizer"] > 0:
            garden.fertilize_plants()
            self.inventory.remove_item("fertilizer", 1)
            self.gain_experience(15)
            print("Fertilized the plants.")
        else:
            print("No fertilizer left.")

    def harvest(self, garden):
        harvested = garden.harvest_plants()
        self.inventory.add_item("seeds", harvested)
        self.gain_experience(20)
        print(f"Harvested {harvested} seeds.")

    def check_resources(self):
        self.inventory.check_inventory()

    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= 100:
            self.level_up()

    def level_up(self):
        self.skills["gardening"] += 1
        self.skills["watering"] += 1
        self.skills["harvesting"] += 1
        self.experience -= 100
        print("Leveled up")
