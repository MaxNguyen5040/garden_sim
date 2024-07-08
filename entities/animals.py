class CompanionAnimal:
    def __init__(self, name, function):
        self.name = name
        self.function = function

class CompanionManagement:
    def __init__(self):
        self.available_companions = []

    def add_companion(self, companion):
        self.available_companions.append(companion)

    def remove_companion(self, companion):
        self.available_companions.remove(companion)

companion_management = CompanionManagement()
bees = CompanionAnimal("Bees", "Pollination")
companion_management.add_companion(bees)
print(f"Available companions: {[companion.name for companion in companion_management.available_companions]}")
