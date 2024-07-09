class Tooltip:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def display(self):
        print(f"{self.title}: {self.content}")

tooltip_biodiversity = Tooltip(
    "Biodiversity",
    "Biodiversity refers to the variety of plant and animal species in a particular habitat."
)
tooltip_symbiosis = Tooltip(
    "Symbiosis",
    "Symbiosis is a close and long-term biological interaction between two different biological organisms."
)
tooltip_food_web = Tooltip(
    "Food Web",
    "A food web is a system of interlocking and interdependent food chains."
)

tooltip_biodiversity.display()
tooltip_symbiosis.display()
tooltip_food_web.display()
