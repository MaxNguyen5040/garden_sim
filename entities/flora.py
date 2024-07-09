class Tree(Plant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.height = 0

    def grow(self):
        if self.health > 0:
            self.height += 10  # Increment height as tree grows
            print(f"{self.name} is growing taller.")
        else:
            print(f"{self.name} is unhealthy and cannot grow.")

class Foliage(Plant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.color = "Green"

    def change_color(self, new_color):
        self.color = new_color
        print(f"{self.name} foliage changed to {self.color}.")