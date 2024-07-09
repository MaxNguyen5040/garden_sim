class EnhancedUI(UI):
    def display_tooltip(self, tooltip):
        print(f"Enhanced Tooltip Display: {tooltip.title}")
        print(f"Description: {tooltip.content}")

    def display_activity(self, activity):
        print(f"Enhanced Activity Display: {activity.description}")
        print(f"Reward: {activity.reward}")

    def display_progress(self, player):
        print(f"Enhanced Progress Display for {player.name}")
        for activity in player.completed_activities:
            print(f"- Completed: {activity.description}")