# ui.py

from tkinter import Tk, Label, Button
from player_stats import PlayerStats

class GameUI:
    def __init__(self, player):
        self.player = player
        self.root = Tk()
        self.root.title("Garden Sim Game")

        self.label_name = Label(self.root, text=f"Player: {self.player.name}")
        self.label_name.pack()

        self.label_level = Label(self.root, text=f"Level: {self.player.level}")
        self.label_level.pack()

        self.label_experience = Label(self.root, text=f"Experience: {self.player.experience}")
        self.label_experience.pack()

        self.label_money = Label(self.root, text=f"Money: {self.player.money}")
        self.label_money.pack()

        self.label_crops_grown = Label(self.root, text=f"Crops Grown: {self.player.crops_grown}")
        self.label_crops_grown.pack()

        self.label_animals_raised = Label(self.root, text=f"Animals Raised: {self.player.animals_raised}")
        self.label_animals_raised.pack()

        self.label_items_collected = Label(self.root, text=f"Items Collected: {self.player.items_collected}")
        self.label_items_collected.pack()

        self.button_grow_crop = Button(self.root, text="Grow Crop", command=self.grow_crop)
        self.button_grow_crop.pack()

        self.button_raise_animal = Button(self.root, text="Raise Animal", command=self.raise_animal)
        self.button_raise_animal.pack()

        self.button_collect_item = Button(self.root, text="Collect Item", command=self.collect_item)
        self.button_collect_item.pack()

        self.button_buy_item = Button(self.root, text="Buy Item", command=self.buy_item)
        self.button_buy_item.pack()

        self.button_sell_item = Button(self.root, text="Sell Item", command=self.sell_item)
        self.button_sell_item.pack()

        self.root.mainloop()

    def update_stats(self):
        self.label_level.config(text=f"Level: {self.player.level}")
        self.label_experience.config(text=f"Experience: {self.player.experience}")
        self.label_money.config(text=f"Money: {self.player.money}")
        self.label_crops_grown.config(text=f"Crops Grown: {self.player.crops_grown}")
        self.label_animals_raised.config(text=f"Animals Raised: {self.player.animals_raised}")
        self.label_items_collected.config(text=f"Items Collected: {self.player.items_collected}")

    def grow_crop(self):
        self.player.grow_crop()
        self.update_stats()

    def raise_animal(self):
        self.player.raise_animal()
        self.update_stats()

    def collect_item(self):
        self.player.collect_item()
        self.update_stats()

    def buy_item(self):
        if self.player.spend_money(50):
            print("Item bought successfully!")
        else:
            print("Not enough money!")
        self.update_stats()

    def sell_item(self):
        self.player.add_money(20)
        self.update_stats()

if __name__ == "__main__":
    player = PlayerStats("Player1")
    GameUI(player)
