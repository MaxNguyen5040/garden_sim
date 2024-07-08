class PlayerStats:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.experience = 0
        self.money = 100  # starting money
        self.crops_grown = 0
        self.animals_raised = 0
        self.items_collected = 0

    def add_experience(self, amount):
        self.experience += amount
        self.check_level_up()

    def check_level_up(self):
        level_thresholds = [100, 300, 600, 1000]  # Example thresholds
        while self.experience >= level_thresholds[self.level - 1]:
            self.level += 1
            print(f"Level up! You are now level {self.level}.")

    def add_money(self, amount):
        self.money += amount

    def spend_money(self, amount):
        if self.money >= amount:
            self.money -= amount
            return True
        return False

    def grow_crop(self):
        self.crops_grown += 1
        self.add_experience(10)

    def raise_animal(self):
        self.animals_raised += 1
        self.add_experience(15)

    def collect_item(self):
        self.items_collected += 1
        self.add_experience(5)
