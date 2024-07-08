class Plant:
    def __init__(self, name):
        self.name = name
        self.growth_stage = 0
        self.max_growth_stage = 5
        self.disease = None
        self.special_ability = self.get_special_ability()

    def grow(self):
        if self.growth_stage < self.max_growth_stage:
            self.growth_stage += 1
            self.check_for_disease()

    def is_ready_for_harvest(self):
        return self.growth_stage == self.max_growth_stage and self.disease is None

    def get_special_ability(self):
        abilities = ["fast_growth", "resistant", "high_yield"]
        return random.choice(abilities)

    def apply_special_ability(self):
        if self.special_ability == "fast_growth":
            self.growth_stage += 1
        elif self.special_ability == "resistant":
            self.disease = None
        elif self.special_ability == "high_yield":
            pass

    def check_for_disease(self):
        if random.random() < 0.1:  # 10% chance to get a disease
            self.disease = "Blight"

    def cure_disease(self):
        self.disease = None
