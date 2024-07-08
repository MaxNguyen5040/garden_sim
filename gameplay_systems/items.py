class Item:
    def __init__(self, name, material):
        self.name = name
        self.material = material

class CraftingSystem:
    def __init__(self):
        self.recipes = {}

    def add_recipe(self, result_item, ingredients):
        self.recipes[result_item] = ingredients

    def craft_item(self, item):
        if item in self.recipes:
            ingredients = self.recipes[item]
            return f"{item.name} crafted using {', '.join([ingredient.name for ingredient in ingredients])}"
        else:
            return "Recipe not found"

crafting_system = CraftingSystem()
crafting_system.add_recipe(Item("Potion", "Herbs"), [Item("Herbs", "Plants")])
print(crafting_system.craft_item(Item("Potion", "Herbs")))
