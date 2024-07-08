# ui.py

from tkinter import Tk, Label, Button
from player_stats import PlayerStats

class GameUI:
    def __init__(self, player):
        self.player = player
        self.root = Tk()
        self.root.title("Garden Sim Game")

        self.button_save_game = Button(self.root, text="Save Game", command=self.save_game)
        self.button_save_game.pack()

        self.button_load_game = Button(self.root, text="Load Game", command=self.load_game)
        self.button_load_game.pack()

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

        self.label_npc_activities = Label(self.root, text="NPC Activities")
        self.label_npc_activities.pack()

        self.npc_activity_labels = {}
        for npc in npcs:
            label = Label(self.root, text=f"{npc.name}: {npc.get_activity('06:00')}")
            label.pack()
            self.npc_activity_labels[npc.name] = label

        self.update_npc_activities("06:00")
        self.root.after(60000, self.update_npc_activities)  # Update every in-game hour

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

    def update_npc_activities(self, current_time):
        activities = get_npc_activities(current_time)
        for npc_name, activity in activities.items():
            self.npc_activity_labels[npc_name].config(text=f"{npc_name}: {activity}")

        next_time = self.get_next_time(current_time)
        self.root.after(60000, lambda: self.update_npc_activities(next_time))  # Update every in-game hour

    def get_next_time(self, current_time):
        hours, minutes = map(int, current_time.split(":"))
        minutes += 60
        if minutes >= 60:
            minutes = 0
            hours += 1
        if hours >= 24:
            hours = 0
        return f"{hours:02d}:{minutes:02d}"

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

    def save_game(self):
        self.player.save_stats()
        print("Game saved successfully!")

    def load_game(self):
        self.player.load_stats()
        self.update_stats()
        print("Game loaded successfully!")

if __name__ == "__main__":
    player = PlayerStats("Player1")
    GameUI(player)
