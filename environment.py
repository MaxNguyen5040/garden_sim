class Environment:
    def __init__(self, season):
        self.season = season
        self.weather = "Sunny"

    def change_weather(self, new_weather):
        self.weather = new_weather

env = Environment("Spring")
print(f"Current weather: {env.weather}") 


def apply_environment_effects(garden, environment):
    if environment.weather == "Rainy":
        for plant in garden.plants:
            plant.growth_rate -= 0.1  #

