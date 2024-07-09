class Competition:
    def __init__(self, name, type, criteria):
        self.name = name
        self.type = type  # e.g., beauty contest, productivity challenge
        self.criteria = criteria  # list of criteria for judging
        self.participants = []

    def add_participant(self, player):
        self.participants.append(player)
        print(f"{player} has entered the {self.name}!")

    def announce_winner(self):
        winner = self.determine_winner()
        if winner:
            print(f"The winner of the {self.name} is {winner}!")
            self.give_rewards(winner)
        else:
            print(f"No winner determined for the {self.name}.")

    def give_rewards(self, winner):
        if winner in self.rewards:
            print(f"{winner} receives {self.rewards[winner]} as a reward!")
        else:
            print(f"No specific reward for {winner}.")

competition1 = Competition("Beauty Contest", "beauty", ["Flower Arrangement", "Garden Design"])
competition1.add_participant("Player1")
competition1.add_participant("Player2")
competition1.announce_winner()
