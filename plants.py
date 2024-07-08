class Plant:
    def __init__(self):
        self.growth_stage = 0

    def grow(self):
        self.growth_stage += 1

    def is_ready_for_harvest(self):
        return self.growth_stage >= 3