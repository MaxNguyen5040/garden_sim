class Sound:
    def __init__(self):
        self.sound_effects = []

    def add_effect(self, effect):
        self.sound_effects.append(effect)

    def play_effects(self):
        for effect in self.sound_effects:
            print(f"Playing {effect} sound effect.")