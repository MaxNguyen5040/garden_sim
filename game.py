from events import random_event

class GardenSim:
    def __init__(self):
        self.garden = Garden()
        self.player = Player()

    def start_game(self):
        while True:
            self.display_menu()
            choice = input("Choose an action: ")
            self.handle_choice(choice)
            if random.random() < 0.3:  # 30% chance of an event
                event = random_event()
                event.apply(self.garden)
                print(f"Event: {event.name}")


    def display_menu(self):
        print("1. Plant")
        print("2. Water")
        print("3. Harvest")
        print("4. Check Resources")
        print("5. Save Game")
        print("6. Load Game")
        print("7. Exit")

    def handle_choice(self, choice):
        if choice == "1":
            self.player.plant(self.garden)
        elif choice == "2":
            self.player.water(self.garden)
        elif choice == "3":
            self.player.harvest(self.garden)
        elif choice == "4":
            self.player.check_resources()
        elif choice == "5":
            self.save_game()
        elif choice == "6":
            self.load_game()
        elif choice == "7":
            exit()
        else:
            print("Invalid choice.")

    def save_game(self):
        save_game(self.garden, self.player)

    def load_game(self):
        self.garden, self.player = load_game()
