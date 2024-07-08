class Quest:
    def __init__(self, description, condition, reward):
        self.description = description
        self.condition = condition
        self.reward = reward
        self.completed = False

    def check_completion(self, garden, player):
        if self.condition(garden, player):
            self.completed = True
            player.resources["seeds"] += self.reward
            print(f"Quest completed: {self.description} Reward: {self.reward} seeds")

def quest_list():
    return [
        Quest("Grow 5 plants", lambda g, p: len(g.plants) >= 5, 10),
        Quest("Harvest 10 plants", lambda g, p: p.resources["seeds"] >= 10, 15)
    ]
