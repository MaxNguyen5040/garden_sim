import pickle

def save_game_state(player, garden):
    with open('game_state.pkl', 'wb') as f:
        pickle.dump((player, garden), f)

def load_game_state():
    try:
        with open('game_state.pkl', 'rb') as f:
            player, garden = pickle.load(f)
            return player, garden
    except FileNotFoundError:
        print("No saved game state found.")
        return None, None


save_game_state(player, garden)
loaded_player, loaded_garden = load_game_state()
