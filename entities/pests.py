class Pest:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class PestManagement:
    def __init__(self):
        self.active_pests = []

    def introduce_pest(self, pest):
        self.active_pests.append(pest)

    def remove_pest(self, pest):
        self.active_pests.remove(pest)

# Example usage:
pest_management = PestManagement()
aphids = Pest("Aphids", 5)
pest_management.introduce_pest(aphids)
print(f"Active pests: {[pest.name for pest in pest_management.active_pests]}")