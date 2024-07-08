from marketplace import Marketplace

market = Marketplace()

# Function to interact with the marketplace
def marketplace_interaction():
    print("Welcome to the Marketplace!")
    while True:
        action = input("Would you like to buy, sell, or check prices? (buy/sell/check/exit): ").lower()
        if action == "buy":
            shop_type = input("Which shop? (seeds/animals): ").lower()
            shop = market.seed_shop if shop_type == "seeds" else market.animal_shop
            item = input(f"Available items: {', '.join(shop.keys())}\nWhat would you like to buy? ")
            quantity = int(input("How many would you like to buy? "))
            print(market.buy_item(shop, item, quantity))
        elif action == "sell":
            item = input(f"Available items in inventory: {', '.join(market.inventory.keys())}\nWhat would you like to sell? ")
            quantity = int(input("How many would you like to sell? "))
            print(market.sell_item(item, quantity))
        elif action == "check":
            print(f"Current money: ${market.money}")
            print("Seed shop prices:")
            for item, price in market.seed_shop.items():
                print(f"{item}: ${price:.2f}")
            print("Animal shop prices:")
            for item, price in market.animal_shop.items():
                print(f"{item}: ${price:.2f}")
            print("Inventory:")
            for item, quantity in market.inventory.items():
                print(f"{item}: {quantity}")
        elif action == "exit":
            print("Leaving the marketplace. Goodbye!")
            break
        else:
            print("Invalid action. Please try again.")

marketplace_interaction()
