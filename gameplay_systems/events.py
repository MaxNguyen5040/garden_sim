import random

class Event:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def trigger(self):
        return f"A {self.name} occurs! {self.description}"

class Garden:
    def __init__(self):
        self.events = []
    
    def add_event(self, event):
        self.events.append(event)
    
    def get_random_event(self):
        return random.choice(self.events)

festival = Event("Festival", "Local villagers come to celebrate with music and dance.")
rainstorm = Event("Rainstorm", "Heavy rain pours down, watering your plants abundantly.")
drought = Event("Drought", "Dry weather persists, requiring extra irrigation.")
heat_wave = Event("Heat Wave", "Temperatures soar, stressing your plants.")
pest_infestation = Event("Pest Infestation", "Insects invade your garden, damaging crops.")
meteor_shower = Event("Meteor Shower", "Bright meteors light up the night sky.")
solar_eclipse = Event("Solar Eclipse", "The sun is obscured by the moon for a brief period.")
harvest_time = Event("Harvest Time", "Crops are ready for harvest, providing a bountiful yield.")
earthquake = Event("Earthquake", "The ground shakes, causing minor damage to structures.")
flower_bloom = Event("Flower Bloom", "Colorful flowers bloom, enhancing your garden's beauty.")

my_garden = Garden()
my_garden.add_event(festival)
my_garden.add_event(rainstorm)
my_garden.add_event(drought)
my_garden.add_event(heat_wave)
my_garden.add_event(pest_infestation)
my_garden.add_event(meteor_shower)
my_garden.add_event(solar_eclipse)
my_garden.add_event(harvest_time)
my_garden.add_event(earthquake)
my_garden.add_event(flower_bloom)

# For future Max! this is how you trigger an event!
# -Max
random_event = my_garden.get_random_event()
print(random_event.trigger())
