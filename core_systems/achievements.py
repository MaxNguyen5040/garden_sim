class Achievement:
    def __init__(self, name, description, condition):
        self.name = name
        self.description = description
        self.condition = condition
        self.achieved = False
    
    def check_condition(self):
        return self.condition()
    
    def unlock(self):
        print(f"Achievement Unlocked: {self.title}")
        print(f"Description: {self.description}")

class AchievementsManager:
    def __init__(self):
        self.achievements = []
    
    def add_achievement(self, name, description, condition):
        achievement = Achievement(name, description, condition)
        self.achievements.append(achievement)
    
    def check_achievements(self):
        for achievement in self.achievements:
            if not achievement.achieved and achievement.check_condition():
                print(f"Achievement unlocked: {achievement.name}")
                achievement.achieved = True

def has_10_plants():
    if self.plants >= 10:
        return True  
    else:
        return False

achievements_manager = AchievementsManager()

achievement_ecologist = Achievement(
    "Ecologist",
    "Complete all educational activities related to ecological principles."
)
achievement_photographer = Achievement(
    "Photographer",
    "Capture images of all different types of plants and animals in the garden."
)
# Checking achievements (simulate progress)
achievements_manager.check_achievements()
