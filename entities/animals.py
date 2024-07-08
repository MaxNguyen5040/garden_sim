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

bees = CompanionAnimal("Bees", "Pollination")
raccoons = CompanionAnimal("Raccoons", "Steal your food")
cats = CompanionAnimal("Cats", "Chase away pests")
dogs = CompanionAnimal("Dogs", "Provide protection")
birds = CompanionAnimal("Birds", "Scare off insects")
butterflies = CompanionAnimal("Butterflies", "Help with pollination")
worms = CompanionAnimal("Worms", "Aerate the soil")
ladybugs = CompanionAnimal("Ladybugs", "Eat harmful pests")
frogs = CompanionAnimal("Frogs", "Control insect population")
squirrels = CompanionAnimal("Squirrels", "Plant trees by burying nuts")

animals = [bees, raccoons, cats, dogs, birds, butterflies, worms, ladybugs, frogs, squirrels]
for animal in animals:
    print(animal.interact())