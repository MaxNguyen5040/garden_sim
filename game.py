from events import random_event
from quests import quest_list
from trading import Trader
from weather import Weather
import random 

class GardenSim:
    def __init__(self):
        self.garden = Garden()
        self.player = Player()
        self.quests = quest_list()
        self.trader = Trader()
        self.weather = Weather()


    def start_game(self):
        while True:
            self.display_menu()
            choice = input("Choose an action: ")
            self.handle_choice(choice)
            for quest in self.quests:
                quest.check_completion(self.garden, self.player)
            if random.random() < 0.3:
                event = random_event()
                event.apply(self.garden)
                print(f"Event: {event.name}")
            self.weather.change_weather()
            self.weather.affect_garden(self.garden)
            print(f"Weather: {self.weather.current_weather}")


    def display_menu(self):
        print("1. Plant")
        print("2. Water")
        print("3. Harvest")
        print("4. Check Resources")
        print("5. Save Game")
        print("6. Load Game")
        print("7. Exit")

    def handle_choice(self, choice):
        if choice == "plant":
            self.player.plant(self.garden)
        elif choice == "water":
            self.player.water(self.garden)
        elif choice == "fertilize":
            self.player.fertilize(self.garden)
        elif choice == "harvest":
            self.player.harvest(self.garden)
        elif choice == "check resources":
            self.player.check_resources()
        elif choice == "buy":
            item = input("Enter item to buy: ")
            amount = int(input("Enter amount to buy: "))
            self.trader.buy(self.player, item, amount)
        elif choice == "sell":
            item = input("Enter item to sell: ")
            amount = int(input("Enter amount to sell: "))
            self.trader.sell(self.player, item, amount)

    def save_game(self):
        save_game(self.garden, self.player)

    def load_game(self):
        self.garden, self.player = load_game()
