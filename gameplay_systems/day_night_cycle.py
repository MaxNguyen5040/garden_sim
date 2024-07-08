possible_time_phases = ["Morning", "Afternoon", "Evening", "Night"]

class DayNightCycle:
    def __init__(self):
        self.current_phase = random.choice(possible_time_phases)

    def advance_time(self):
        current_index = possible_time_phases.index(self.current_phase)
        next_index = (current_index + 1) % len(possible_time_phases)
        self.current_phase = possible_time_phases[next_index]

    def apply_time_effects(self, player, garden, npcs):
        if self.current_phase == "Morning":
            print("It's morning. Plants grow faster in the garden.")
            garden.boost_plant_growth()
        elif self.current_phase == "Afternoon":
            print("It's afternoon. NPCs are active and offer quests.")
            for npc in npcs:
                npc.offer_quest(player)
        elif self.current_phase == "Evening":
            print("It's evening. Some NPCs rest while others prepare for night activities.")
            for npc in npcs:
                if random.random() < 0.5:
                    npc.rest()
                else:
                    npc.prepare_night_activities()
        elif self.current_phase == "Night":
            print("It's night. Some NPCs may be asleep, while others engage in nocturnal activities.")
            for npc in npcs:
                if random.random() < 0.3:
                    npc.sleep()
                else:
                    npc.perform_nocturnal_activities(player)


for _ in range(5):
    day_night_cycle.apply_time_effects(player, garden, npcs)
    day_night_cycle.advance_time()