class Pest:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class PestManagement:
    def __init__(self):
        self.active_pests = []

    def introduce_pest(self, pest):
        self.active_pests.append(pest)

    def remove_pest(self, pest):
        self.active_pests.remove(pest)

class Insect:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def interact_with_plant(self, plant):
        if self.effect == "help":
            plant.health += random.randint(5, 15)
            print(f"{self.name} helped {plant.name}, increasing its health!")
        elif self.effect == "harm":
            plant.health -= random.randint(5, 15)
            print(f"{self.name} harmed {plant.name}, decreasing its health!")

class BeneficialInsect(Insect):
    def __init__(self, name):
        super().__init__(name, "help")

pest_management = PestManagement()
ladybug = BeneficialInsect("Ladybug")
bee = BeneficialInsect("Bee")
aphids = Pest("Aphid")
beetle = Pest("Beetle")
pest_management.introduce_pest(aphids)
print(f"Active pests: {[pest.name for pest in pest_management.active_pests]}")