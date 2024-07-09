class Activity:
    def __init__(self, description, reward):
        self.description = description
        self.reward = reward

    def complete(self):
        print(f"Activity completed: {self.description}")
        print(f"Reward: {self.reward}")

activity_biodiversity = Activity(
    "Identify 5 different plant species in your garden.",
    "Unlock a rare plant seed."
)
activity_symbiosis = Activity(
    "Introduce a pollinator to your garden.",
    "Gain a boost in plant growth."
)
activity_food_web = Activity(
    "Create a balanced food web with at least 3 trophic levels.",
    "Unlock an educational badge."
)

activity_photosynthesis = Activity(
    "Grow a plant under different light conditions and observe the changes.",
    "Unlock a new plant species."
)
activity_pollination = Activity(
    "Introduce different pollinators and observe their effects on plant reproduction.",
    "Unlock a new animal companion."
)
activity_decomposition = Activity(
    "Create a compost bin and observe the decomposition process.",
    "Gain a nutrient boost for your plants."
)

activity_biodiversity.complete()
activity_symbiosis.complete()
activity_food_web.complete()