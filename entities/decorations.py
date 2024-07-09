class Decoration:
    def __init__(self, name, weight, space, bonus=None):
        self.name = name
        self.weight = weight
        self.space = space
        self.bonus = bonus  # Optional: bonus for plant growth

class Garden:
    def __init__(self):
        self.decorations = []

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def remove_decoration(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)

    def get_total_weight(self):
        total_weight = sum(decoration.weight for decoration in self.decorations)
        return total_weight

    def get_total_space(self):
        total_space = sum(decoration.space for decoration in self.decorations)
        return total_space

    def apply_decoration_bonuses(self):
        pass

decoration1 = Decoration("Stone Statue", 50, 4, bonus=5) 
decoration2 = Decoration("Zen Garden", 30, 2, bonus=3)   
decoration3 = Decoration("Fountain", 40, 3, bonus=4)     
decoration4 = Decoration("Pathway Lights", 20, 1)        
decoration5 = Decoration("Rose Arch", 60, 5, bonus=7)    
decoration6 = Decoration("Garden Bench", 35, 2)          
decoration7 = Decoration("Bird Bath", 45, 3, bonus=6)    
decoration8 = Decoration("Gazebo", 70, 6)                 
decoration9 = Decoration("Wind Chimes", 25, 1, bonus=2)  
decoration10 = Decoration("Topiary", 55, 4)               