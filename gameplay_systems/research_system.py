class ResearchSystem:
    def __init__(self):
        self.available_technologies = []
        self.player_progress = {}

    def add_technology(self, technology_name, requirements):
        self.available_technologies.append({
            'name': technology_name,
            'requirements': requirements
        })

    def unlock_technology(self, player, technology_name):
        if technology_name in self.available_technologies:
            self.player_progress[player][technology_name] = True
            print(f"{player} has unlocked {technology_name}!")

    def check_progress(self, player, technology_name):
        if player in self.player_progress and technology_name in self.player_progress[player]:
            return self.player_progress[player][technology_name]
        return False

research_system = ResearchSystem()
research_system.add_technology("Advanced Fertilizers", ["Complete tutorial", "Achieve Level 10 Gardening"])
research_system.add_technology("Automated Irrigation", ["Complete basic quests"])
research_system.unlock_technology("Player1", "Automated Irrigation")
print(research_system.check_progress("Player1", "Automated Irrigation"))
