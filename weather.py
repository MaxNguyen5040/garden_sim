import random

class Weather:
    def __init__(self):
        self.current_weather = "Sunny"

    def change_weather(self):
        weather_types = ["Sunny", "Rainy", "Stormy", "Cloudy"]
        self.current_weather = random.choice(weather_types)

    def affect_garden(self, garden):
        if self.current_weather == "Sunny":
            pass  # Normal growth
        elif self.current_weather == "Rainy":
            for plant in garden.plants:
                plant.grow()
        elif self.current_weather == "Stormy":
            garden.plants = [plant for plant in garden.plants if random.random() > 0.2]  # 20% chance plants get destroyed
        elif self.current_weather == "Cloudy":
            pass  # Slow growth
