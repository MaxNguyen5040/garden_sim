class Plot:
    def __init__(self, size, terrain_type, challenges=None, opportunities=None):
        self.size = size  
        self.terrain_type = terrain_type  
        self.challenges = challenges or []  
        self.opportunities = opportunities or [] 

    def describe(self):
        description = f"Plot Size: {self.size}\nTerrain Type: {self.terrain_type}\n"
        if self.challenges:
            description += "Challenges:\n"
            for challenge in self.challenges:
                description += f"- {challenge}\n"
        if self.opportunities:
            description += "Opportunities:\n"
            for opportunity in self.opportunities:
                description += f"- {opportunity}\n"
        return description
    

plot1 = Plot(size="Small", terrain_type="Grassland", challenges=["Pest infestation", "Poor soil quality"],
             opportunities=["Natural spring for irrigation", "Fertile soil for certain plants"])
plot2 = Plot(size="Medium", terrain_type="Forest", challenges=["Limited sunlight", "Wild animal threats"],
             opportunities=["Rich biodiversity", "Special plants that thrive in shade"])
plot3 = Plot(size="Large", terrain_type="Desert", challenges=["Water scarcity", "Extreme temperatures"],
             opportunities=["Cactus garden", "Unique desert flora"])