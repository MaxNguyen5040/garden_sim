class Plant:
    def __init__(self, name):
        self.name = name
        self.growth_stage = 0
        self.max_growth_stage = 5
        self.special_ability = self.get_special_ability()

    def grow(self):
        if self.growth_stage < self.max_growth_stage:
            self.growth_stage += 1

    def is_ready_for_harvest(self):
        return self.growth_stage == self.max_growth_stage

    def get_special_ability(self):
        abilities = ["fast_growth", "resistant", "high_yield"]
        return random.choice(abilities)

    def apply_special_ability(self):
        if self.special_ability == "fast_growth":
            self.growth_stage += 1
        elif self.special_ability == "resistant":
            pass  # Implement resistance logic
        elif self.special_ability == "high_yield":
            pass  # Implement high yield logic
