import random

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
    def __init__(self, name, effect, lifecycle_stages):
        self.name = name
        self.effect = effect
        self.lifecycle_stages = lifecycle_stages
        self.current_stage = lifecycle_stages[0]

    def interact_with_plant(self, plant):
        if self.effect == "help":
            plant.health += random.randint(5, 15)
            print(f"{self.name} ({self.current_stage}) helped {plant.name}, increasing its health!")
        elif self.effect == "harm":
            plant.health -= random.randint(5, 15)
            print(f"{self.name} ({self.current_stage}) harmed {plant.name}, decreasing its health!")

    def progress_lifecycle(self):
        current_index = self.lifecycle_stages.index(self.current_stage)
        if current_index < len(self.lifecycle_stages) - 1:
            self.current_stage = self.lifecycle_stages[current_index + 1]
            print(f"{self.name} progressed to {self.current_stage} stage.")

class BeneficialInsect(Insect):
    def __init__(self, name):
        super().__init__(name, "help", ["egg", "larvae", "pupa", "adult"])

class Pest(Insect):
    def __init__(self, name):
        super().__init__(name, "harm", ["egg", "larvae", "pupa", "adult"])

# Example insects
ladybug = BeneficialInsect("Ladybug")
bee = BeneficialInsect("Bee")
aphid = Pest("Aphid")
beetle = Pest("Beetle")


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