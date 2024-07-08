import random

class Event:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def apply(self, garden):
        self.effect(garden)

def random_event():
    events = [
        Event("Drought", lambda garden: [plant.grow() for plant in garden.plants]),
        Event("Pest Attack", lambda garden: garden.plants.pop() if garden.plants else None),
        Event("Rain", lambda garden: [plant.grow() for plant in garden.plants])
    ]
    return random.choice(events)