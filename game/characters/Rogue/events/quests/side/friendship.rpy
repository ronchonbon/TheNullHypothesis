init python:

    def Rogue_friendship_Quest():
        name = f"{Rogue.name}: Friendship"

        string = "Rogue_friendship_Quest"

        Quest_type = "side"

        chapter = 1

        description = "Befriend your favorite Southern belle goth"

        objectives = {
            "Gain Love": ["Rogue.love", Rogue_thresholds["dating"][0]],

            "Gain Trust": ["Rogue.trust", Rogue_thresholds["dating"][1]]}

        optional_objectives = {}

        rewards = {}

        criteria = [
            "chapter == 1 and season == 1"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)