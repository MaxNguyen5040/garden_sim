import random

class NPC:
    def __init__(self, name, behaviors):
        self.name = name
        self.behaviors = behaviors

    def perform_action(self, player, garden):
        for behavior in self.behaviors:
            if behavior in possible_behaviors:
                possible_behaviors[behavior](self, player, garden)
            else:
                print(f"{self.name} does not have a valid behavior defined.")

    def generate_dynamic_schedule(self):
        dynamic_schedule = self.base_schedule.copy()
        if random.random() < 0.1:  # 10% chance of random event
            dynamic_schedule["14:00"] = "Random event"
        return dynamic_schedule

    def boost_plants(self, garden):
        print(f"{self.name} boosts plants in the garden.")

    def steal_items(self, player):
        print(f"{self.name} steals items from {player.name}'s inventory.")

    def sell_items(self, player):
        print(f"{self.name} sells items to {player.name}.")

    def provide_quest(self, player):
        print(f"{self.name} provides a quest to {player.name}.")

    def trade_items(self, player):
        print(f"{self.name} trades items with {player.name}.")

    def offer_advice(self, player, garden):
        print(f"{self.name} offers advice to {player.name} about the garden.")

    def attack(self, player, garden):
        print(f"{self.name} attacks {player.name} or the garden.")

    def heal(self, player, garden):
        print(f"{self.name} heals {player.name} or the garden.")

    def influence_environment(self, garden):
        print(f"{self.name} influences the environment in the garden.")

    def change_game_state(self, player, garden):
        print(f"{self.name} changes the game state.")

# Example usage
player = Player("Player1")
garden = Garden()

npcs = [
    npc1 = NPC("Alice", {
    "06:00": "Boost plants in garden",
    "12:00": "Offer advice or information",
    "18:00": "Boost plants in garden"
    })

    npc2 = NPC("Bob", {
        "08:00": "Steal items from inventory",
        "14:00": "Attack player or garden",
        "20:00": "Steal items from inventory"
    })

    npc3 = NPC("Charlie", {
        "09:00": "Sell items to player",
        "13:00": "Provide quest or task",
        "17:00": "Sell items to player"
    })

    npc4 = NPC("Diana", {
        "10:00": "Provide quest or task",
        "16:00": "Influence environment",
        "22:00": "Provide quest or task"
    })

    npc5 = NPC("Eve", {
        "07:00": "Trade items with player",
        "15:00": "Heal player or garden",
        "19:00": "Trade items with player"
    })
    ]

# Perform actions for each NPC
for npc in [npc1, npc2, npc3, npc4, npc5]:
    npc.perform_action(player, garden)
