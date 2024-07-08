class Achievement:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True
        print(f"Achievement unlocked: {self.name}")