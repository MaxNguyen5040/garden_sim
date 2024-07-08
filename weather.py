import random

class Weather:
    def __init__(self):
        self.current_weather = "Sunny"

    def change_weather(self):
        weather_types = ["Sunny", "Rainy", "Stormy", "Cloudy"]
        self.current_weather = random.choice(weather_types)

    def affect_garden(self, garden):
        for plant in garden.plants:
            if self.current_weather == "Sunny":
                plant.affect_health(5)
            elif self.current_weather == "Rainy":
                plant.affect_health(10)
            elif self.current_weather == "Stormy":
                plant.affect_health(-10)
            elif self.current_weather == "Cloudy":
                plant.affect_health(0)

