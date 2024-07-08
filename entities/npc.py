import random

# Define possible NPC behaviors
possible_behaviors = {
    "Boost plants in garden": lambda npc, garden: npc.boost_plants(garden),
    "Steal items from inventory": lambda npc, player: npc.steal_items(player),
    "Sell items to player": lambda npc, player: npc.sell_items(player),
    "Provide quest or task": lambda npc, player: npc.provide_quest(player),
    "Trade items with player": lambda npc, player: npc.trade_items(player),
    "Offer advice or information": lambda npc, player, garden: npc.offer_advice(player, garden),
    "Attack player or garden": lambda npc, player, garden: npc.attack(player, garden),
    "Heal player or garden": lambda npc, player, garden: npc.heal(player, garden),
    "Influence environment": lambda npc, garden: npc.influence_environment(garden),
    "Change game state": lambda npc, player, garden: npc.change_game_state(player, garden)
}

# NPC class definition
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

# Example NPC instances with dynamic behaviors
npc1 = NPC("Alice", ["Boost plants in garden", "Offer advice or information"])
npc2 = NPC("Bob", ["Steal items from inventory", "Attack player or garden"])
npc3 = NPC("Charlie", ["Sell items to player", "Provide quest or task"])
npc4 = NPC("Diana", ["Provide quest or task", "Influence environment"])
npc5 = NPC("Eve", ["Trade items with player", "Heal player or garden"])

# Perform actions for each NPC
for npc in [npc1, npc2, npc3, npc4, npc5]:
    npc.perform_action(player, garden)
