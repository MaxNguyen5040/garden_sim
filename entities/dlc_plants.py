class DesertPlant:
    def __init__(self, name, type):
        self.name = name
        self.type = type  
        self.water_need = "Low"  
        self.sunlight_need = "High"  

    def grow(self):
        print(f"{self.name} is growing slowly under the desert conditions.")

    def breed(self, partner_plant):
        offspring_name = f"{self.name}-{partner_plant.name}"
        offspring_type = f"{self.type}-{partner_plant.type}"
        print(f"Breeding {self.name} with {partner_plant.name} resulted in {offspring_name} ({offspring_type}).")

    def adapt_to_environment(self, environment):
        if environment == "Low Water":
            print(f"{self.name} adapts to low water conditions.")
        elif environment == "High Sunlight":
            print(f"{self.name} thrives in high sunlight.")
        else:
            print(f"{self.name} adapts to its environment.")

desert_plants = [
    DesertPlant("Cactus", "Cactus"),
    DesertPlant("Succulent", "Succulent"),
    DesertPlant("Agave", "Agave"),
    DesertPlant("Yucca", "Yucca"),
    DesertPlant("Aloe Vera", "Aloe")
]

